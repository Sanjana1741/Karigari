import os
import json
import streamlit as st
from PIL import Image
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# 1. Define the desired output schema using Pydantic
class ProductMetadata(BaseModel):
    product_title: str = Field(description="Catchy Amazon-style product title including main characteristics")
    category: str = Field(description="Primary category and subcategory of the item")
    color_palette: list[str] = Field(description="Primary and secondary colors identified in the image")
    estimated_dimensions: str = Field(description="Estimated physical dimensions or size category (e.g., Small, Medium, 10x12 inches)")
    materials: list[str] = Field(description="Likely materials visible (e.g., Leather, Stainless Steel, Cotton, Plastic)")
    key_features: list[str] = Field(description="4-5 bullet points emphasizing selling points and design features")
    amazon_description: str = Field(description="A 2-3 paragraph persuasive product description for e-commerce listings")

# 2. Initialize Gemini Client
@st.cache_resource
def get_gemini_client():
    # Automatically picks up GEMINI_API_KEY from environment variables
    return genai.Client()

def generate_product_info(image: Image.Image) -> ProductMetadata:
    client = get_gemini_client()
    
    prompt = (
        "You are an expert e-commerce product cataloger. Analyze the provided product photo "
        "uploaded by a manufacturer. Identify key visual features, primary colors, likely materials, "
        "and size/dimensions. Generate an optimized Amazon-style listing based strictly on visual inspection."
    )
    
    # Request structured output using Pydantic schema
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[image, prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ProductMetadata,
            temperature=0.2, # Low temperature for accurate, grounded attributes
        )
    )
    
    # Parse and validate JSON output
    data = json.loads(response.text)
    return ProductMetadata(**data)

# 3. Streamlit User Interface
st.set_page_config(page_title="AI Product Cataloger", layout="wide")
st.title("📦 AI Automatic Product Description Generator")
st.write("Upload a product image to automatically generate Amazon-ready attributes and copy.")

uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption="Uploaded Product Photo", use_container_width=True)
    
    with col2:
        if st.button("Generate Product Details", type="primary"):
            with st.spinner("Analyzing image and drafting product details..."):
                try:
                    result = generate_product_info(image)
                    
                    st.subheader(result.product_title)
                    st.caption(f"**Category:** {result.category}")
                    
                    st.markdown("### Key Attributes")
                    st.markdown(f"**Colors:** {', '.join(result.color_palette)}")
                    st.markdown(f"**Materials:** {', '.join(result.materials)}")
                    st.markdown(f"**Est. Size/Dimensions:** {result.estimated_dimensions}")
                    
                    st.markdown("### Bullet Points")
                    for feature in result.key_features:
                        st.markdown(f"* {feature}")
                        
                    st.markdown("### Full Description")
                    st.write(result.amazon_description)
                    
                    # Optional: Allow manufacturer to download as JSON
                    st.download_button(
                        label="Download Data (JSON)",
                        data=json.dumps(result.model_dump(), indent=2),
                        file_name="product_listing.json",
                        mime="application/json"
                    )
                except Exception as e:
                    st.error(f"Error processing image: {e}")