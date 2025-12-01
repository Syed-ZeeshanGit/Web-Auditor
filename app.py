import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- CONFIGURATION ---
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# --- BACKEND FUNCTIONS ---

def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
            
        return soup.get_text(separator=' ', strip=True)[:4000]
    except Exception as e:
        return f"Error: {e}"

def analyze_content(text):
    prompt = """
    You are a strict marketing analyst. Analyze the provided website text.
    Return the output ONLY as a valid JSON object with exactly these keys:
    1. "hook_score": A number between 0-100 based on how compelling the opening is.
    2. "audience_persona": A single concise sentence describing the target audience.
    3. "conversion_killers": A list of 3 strings (confusing phrases or jargon found in the text).
    
    Do not add markdown formatting. Just return the raw JSON string.
    
    Website Content:
    """ + text

    try:
        # Using 'gemini-2.5-flash' 
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}

# --- FRONTEND ---
st.set_page_config(page_title="Website Auditor", page_icon="🕵️")
st.title("🕵️ Website Auditor")

url_input = st.text_input("Enter Website URL", placeholder="https://example.com")

if st.button("Analyze Website"):
    if not url_input:
        st.warning("Please enter a URL.")
    elif not api_key:
        st.error("Gemini API Key is missing.")
    else:
        with st.spinner("Analyzing..."):
            raw_text = scrape_website(url_input)
            if raw_text.startswith("Error"):
                st.error(raw_text)
            else:
                results = analyze_content(raw_text)
                if "error" in results:
                    st.error(results['error'])
                else:
                    st.success("Done!")
                    c1, c2 = st.columns([1, 3])
                    c1.metric("Hook Score", f"{results.get('hook_score')}/100")
                    c2.info(f"**Target Audience:** {results.get('audience_persona')}")
                    st.subheader("⚠️ Conversion Killers")
                    for k in results.get('conversion_killers', []):
                        st.write(f"- {k}")