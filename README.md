# 🕵️ Website Auditor

A Python-based application that scrapes public landing pages and uses AI to analyze their marketing messaging. It provides actionable insights including a Hook Score (indicating how compelling the opening
headline and first paragraph are), Audience Persona identification, and specific "Conversion Killers" (jargon or confusing phrasing).

## 🚀 Live Demo
https://web-auditor-3skyljueuat4b2ompe3ks4.streamlit.app/

## 📋 Features
- Hook Score: Rates the opening headline and paragraph (0-100) based on how compelling it is.
- Audience Persona: Automatically identifies the specific target audience (e.g., "Enterprise CTOs" or "Budget travelers").
- Conversion Killers: Highlights 3 specific phrases that might confuse users or lower conversion rates.
- Scraping Hygiene: Uses `BeautifulSoup` with proper browser headers to ethically fetch content.
- Fast AI Analysis: Powered by 'Google Gemini 2.5 Flash' for high-speed, cost-effective processing.

## 🛠️ Tech Stack
- Frontend: Streamlit
- Backend: Python 3.10+
- Scraping: Requests, BeautifulSoup4
- AI/LLM: Google Gemini API (`google-generativeai`)
- Environment: `python-dotenv` for local security

## ⚙️ Local Setup & Installation

Follow these steps to run the app locally on your machine.

### 1. Clone the Repository
    ```bash
    git clone <https://github.com/Syed-ZeeshanGit/Web-Auditor>
    cd web-auditor

### 2. Create a Virtual Environment
# Windows
    python -m venv venv
    venv\Scripts\activate

# Mac/Linux
    python3 -m venv venv
    source venv/bin/activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Configure API Key
a. Get a free API Key from Google AI Studio.
b. Create a file named .env in the root directory.
c. Add your key inside the file:
    GEMINI_API_KEY=your_actual_api_key_here

### 5. Run the App

    streamlit run app.py

