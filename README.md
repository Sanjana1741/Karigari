 🧵 Karigari — Local Hands, Global Reach

Empowering local artisans to take their craft into the digital world.

Karigari is an accessible, AI-powered digital platform designed to help local artisans **showcase, promote, and grow their products online, even with limited digital literacy.

The project was developed as part of our **Smart India Hackathon (SIH)** journey, with a focus on making digital tools simpler, more accessible, and more useful for artisans.

🌟 Why Karigari?

Many local artisans create unique and valuable handmade products but face challenges when trying to enter the digital marketplace.

Some of these challenges include:

* Limited digital literacy
* Difficulty creating professional product listings
* Difficulty writing product descriptions
* Difficulty promoting products online
* Creating social-media content takes time and effort
* Language barriers
* Limited access to digital marketing tools
* Lack of accessible digital interfaces

Karigari aims to bridge this gap by combining AI, accessibility, multilingual support, and simple digital tools in one platform.


💡 Our Solution

Karigari provides artisans with a simple platform where they can upload their products and use AI-powered tools to create and promote their digital presence.

An artisan can:

1. Create an account
2. Upload a product image
3. Provide basic product information
4. Use AI assistance to generate product metadata and descriptions
5. Automatically generate promotional captions
6. Generate promotional content for different social-media platforms
7. Use accessibility and language features to interact with the platform
8. Showcase their products digitally

The goal is to reduce the technical and creative effort required from artisans while helping them reach a wider audience.

✨ Key Features

🧑‍🎨 Artisan Registration & Login

A simple registration and login interface designed with accessibility and ease of use in mind.

📸 Product Image Upload

Artisans can upload images of their handmade products and provide basic product information.

The uploaded product information can then be used by the platform's AI-powered features.



🤖 AI-Powered Product Assistance

Karigari uses AI to assist artisans in creating professional product information.

The AI can help generate:

* Product metadata
* Product descriptions
* Product-related information
* Structured content based on the uploaded product

This reduces the need for artisans to manually write detailed product descriptions.


📣 AI-Powered Product Promotion

One of Karigari's key features is **AI-assisted digital marketing for artisans**.

Instead of expecting artisans to manually create promotional content, Karigari can automatically generate marketing material based on their products.

The system can generate:

* Promotional posts
* Product-specific captions
* Marketing content
* Social-media promotional content
* Platform-specific promotional text

This allows artisans to promote their products without requiring prior knowledge of digital marketing.

📱 Multi-Platform Social Media Promotion

Karigari helps artisans create promotional content suitable for **different social-media platforms.

The AI-generated content can be adapted according to the requirements and style of different platforms, allowing artisans to promote the same product across multiple social-media channels.

This reduces the effort required to manually create separate promotional content for every platform.

✍️ Automated Product Captions

Karigari can automatically generate **product-specific promotional captions.

Instead of writing a new caption for every product, the artisan can provide their product information and let the AI generate suitable promotional content.

The process can be simplified to:

Product → AI → Caption → Promotion

This makes digital marketing easier for artisans with limited experience in creating social-media content.


♿ Accessibility Features

Karigari includes an accessibility panel with features such as:

* High contrast mode
* Adjustable text size
* Hover highlighting
* Text-to-speech
* Accessibility controls integrated into the interface

The aim is to make the platform easier to use for people with different accessibility needs.

🌐 Multilingual Support

Karigari is designed to support multiple languages, helping make the platform more accessible to artisans from different linguistic backgrounds.

Supported interface languages include:

* English
* Hindi
* Kannada
* Tamil
* Telugu
* Malayalam

🔊 Text-to-Speech

Text-to-speech functionality allows users to listen to important interface content rather than relying entirely on written text.

This can help users who may have difficulty reading or navigating text-heavy interfaces.

🎤 Voice Dashboard

Karigari includes work toward a **voice-oriented dashboard** to make important dashboard interactions easier through voice-based interaction.

The broader goal is to reduce dependence on complex menus and conventional digital navigation.

 🛠️ Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask
* FastAPI
* REST APIs
* Pydantic

### AI

* Google Gemini API
* AI-assisted product metadata generation
* AI-assisted product description generation
* AI-generated promotional content
* Automated social-media captions

### Image Processing

* Pillow (PIL)

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Uvicorn
* Python Virtual Environment

### Environment & Security

* Python `python-dotenv`
* Environment variables for API keys



🏗️ Project Architecture


                         ┌──────────────────────┐
                         │       ARTISAN        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Karigari Frontend  │
                         │      HTML / CSS / JS │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                ┌─────────────────┐    ┌─────────────────┐
                │   Flask App     │    │   FastAPI       │
                │     app.py      │    │    main.py      │
                └────────┬────────┘    └────────┬────────┘
                         │                      │
                         └──────────┬───────────┘
                                    ▼
                         ┌──────────────────────┐
                         │       AI Layer       │
                         │     Gemini API       │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
        ┌────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ Product        │ │ Product         │ │ Promotional     │
        │ Metadata       │ │ Description     │ │ Content         │
        └────────────────┘ └─────────────────┘ └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │ Social Media    │
                                               │ Captions/Posts  │
                                               └─────────────────┘



📂 Project Structure


Karigari/
│
├── .gitignore
├── app.py
├── main.py
├── index.html
├── karigar.html
└── README.md


### Main Files

| File           | Purpose                                                       |
| -------------- | ------------------------------------------------------------- |
| `index.html`   | Main user-facing interface                                    |
| `karigar.html` | Artisan-focused interface/dashboard                           |
| `app.py`       | Application/backend functionality                             |
| `main.py`      | FastAPI backend and API functionality                         |
| `.gitignore`   | Prevents sensitive and unnecessary files from being committed |
| `README.md`    | Project documentation                                         |


⚙️ Getting Started

1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

## 2. Navigate to the Project

```bash
cd Karigari
```

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not currently present in the repository, add one containing the Python packages required by the project.

## 6. Configure Environment Variables

Create a `.env` file and add your API credentials.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit your actual API key to GitHub.**

Make sure `.env` is included in `.gitignore`.

## 7. Run the Application

For FastAPI:

```bash
uvicorn main:app --reload
```

For Flask:

```bash
python app.py
```

---

# 🔐 Security

Karigari uses environment variables to keep API credentials outside the source code.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

Sensitive credentials should never be committed to GitHub.

---

# 🚀 Future Scope

Karigari can be further expanded with features such as:

* 🛍️ Dedicated artisan marketplace
* 🗺️ Craft and artisan discovery map
* 📦 Order management
* 📈 Artisan growth analytics
* 📣 One-click social-media publishing
* 🎤 Expanded voice-based navigation
* 🎨 Festival and seasonal collections
* 💬 AI-powered business and growth assistant
* 💳 Digital payment integration
* 📱 Mobile-first/PWA experience
* 📊 Social-media performance analytics
* 🌍 Wider regional-language support

---

# 🎯 Project Vision

Karigari aims to create a digital ecosystem where artisans can:

**Create → Showcase → Promote → Reach → Grow**

without needing advanced technical or digital-marketing knowledge.

The goal is not simply to put artisan products online, but to give artisans digital tools that can help them **present, promote, and grow their craft**.

---

# 🏆 Smart India Hackathon

Karigari was developed and presented as part of our college's **Smart India Hackathon internal selection process**.

Our team has progressed to the **next round of the SIH selection process**.

---

# 👩‍💻 Team Karigari

This project was developed collaboratively by:

* Sanjana K
* Bhawana Kumari
* Nandhini
* Shannan Juilya J
* Tejsri Reddy
* Theertha A


Built with teamwork, experimentation, continuous learning, and a lot of debugging. ❤️

---

## ❤️ Karigari — Local Hands, Global Reach

> Technology should not replace the craft.
> It should help the people behind the craft reach further.
