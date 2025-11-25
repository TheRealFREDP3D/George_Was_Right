import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=api_key)

print("Fetching available models...")
models_data = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            models_data.append({
                "name": m.name,
                "display_name": m.display_name,
                "description": m.description,
                "supported_generation_methods": m.supported_generation_methods,
                "input_token_limit": m.input_token_limit,
                "output_token_limit": m.output_token_limit,
            })
    
    with open('available_models.json', 'w') as f:
        json.dump(models_data, f, indent=2)
    print(f"Successfully saved {len(models_data)} models to available_models.json")

except Exception as e:
    print(f"Error listing models: {e}")
