# Day 13: Making Your First Real AI API Call
import requests
import os

# 1. Fetch your secret API key securely from your computer's environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. The official Google Gemini API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# 3. Structure the payload following Gemini's expected format
payload = {
    "contents": [
        {
            "parts": [
                {"text": "Explain quantum computing in one simple sentence for a beginner."}
            ]
        }
    ]
}

# 4. Set headers specifying we are sending JSON
headers = {
    "Content-Type": "application/json"
}

try:
    print("Sending prompt to Gemini cloud server...")
    
    # 5. Fire the POST request with a safety timeout
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    
    # 6. Guard against bad status codes
    response.raise_for_status()
    
    # 7. Parse and print the AI's answer
    data = response.json()
    ai_response = data["candidates"][0]["content"]["parts"][0]["text"]
    
    print("\n--- Gemini's Response ---")
    print(ai_response)

except requests.exceptions.HTTPError as err:
    if response.status_code == 400:
        print("❌ Bad Request (400): Check your payload structure or API key.")
    elif response.status_code == 403:
        print("❌ Forbidden (403): Your API key is missing, invalid, or restricted.")
    else:
        print(f"❌ HTTP Error: {err}")
except requests.exceptions.Timeout:
    print("❌ Error: The AI server took too long to respond.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")