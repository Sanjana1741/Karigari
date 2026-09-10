import json
from dotenv import load_dotenv
import os
import time 
from io import BytesIO
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from pydantic import BaseModel, Field
from google import genai
from google.genai import types


# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()

# Enable CORS so your frontend can communicate without browser blocking
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Output Schema
class ProductMetadata(BaseModel):
    product_title: str = Field(description="Catchy Amazon-style product title")
    category: str = Field(description="Primary category")
    color_palette: list[str] = Field(description="Primary and secondary colors")
    estimated_dimensions: str = Field(description="Size or dimensions estimate")
    materials: list[str] = Field(description="Likely materials")
    key_features: list[str] = Field(description="4-5 bullet points")
    amazon_description: str = Field(description="Product description")

# 2. Serve your HTML file at the root URL
@app.get("/", response_class=HTMLResponse)
async def serve_home():
    if not os.path.exists("index.html"):
        return HTMLResponse("<h1>index.html not found! Please place index.html in the project folder.</h1>")
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# 3. API Endpoint to process the image and return AI data
# 3. API Endpoint to process the image and return AI data
@app.post("/api/analyze-product")
async def analyze_product(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        prompt = (
            "You are an expert e-commerce cataloger. Analyze this product image "
            "and generate structured Amazon-ready metadata."
        )
        
        # Retry up to 3 times on 503 errors
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=[image, prompt],
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                        response_schema=ProductMetadata,
                        temperature=0.2,
                    )
                )
                return json.loads(response.text)
            except Exception as e:
                if "503" in str(e) and attempt < max_retries - 1:
                    time.sleep(2) # Wait 2 seconds before retrying
                    continue
                raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))