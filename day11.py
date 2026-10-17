# Day 11: Using Headers and Authentication for API Requests
import requests

url = "https://api.github.com/user" # Notice this is '/user', not '/users/octocat'

# Headers act like your ID badge when entering a secure building
# (In a real AI app, you would put your secret AI provider API key here)
headers = {
  #  "Accept": "application/vnd.github+json",
    # "Authorization": "Bearer YOUR_SECRET_API_KEY_HERE" # This is how you pass real keys later!
}

try:
    print("Sending authenticated request to GitHub...")
    # We pass our headers dictionary into the requests.get() function
    response = requests.get(url, headers=headers, timeout=5)
    
    # Check if the request succeeded
    response.raise_for_status()
    
    data = response.json()
    print(f"Successfully connected! Logged-in profile data received.")

#except requests.exceptions.HTTPError as err:
    # Since we didn't provide a real API key for this secure endpoint, 
    # GitHub will throw a 401 Unauthorized error—let's watch our error handler catch it!
    #if response.status_code == 401:
       # print("❌ Authentication Error (401): Access denied. A valid API key is required for this endpoint.")
   # else:
    #    print(f"❌ HTTP Error: {err}")
except Exception as e:
    print(f"❌ An error occurred: {e}")