
import re
import sys
import markdown
from google_gemini_api import send_query_to_ai
from google_gemini_api import calculate_token_size
from docx import Document
import frontend_lib
import google.generativeai as genai

def send_query_to_ai (prompt, API_KEY):
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(e)
        return False

def calculate_token_size(text):
    words = text.split()
    token_count = len(words)
    return token_count


if __name__ == '__main__':
    #print(frontend_lib.st.session_state)
             markdown_testplan = send_query_to_ai(prompt, API_KEY)
