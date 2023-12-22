
import re
import sys
import markdown
from google_gemini_api import send_query_to_ai
from google_gemini_api import calculate_token_size
from docx import Document
import frontend_lib
import google.generativeai as genai

