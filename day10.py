# Day 10: Handling Errors in API Requests
import requests

url = "https://api.github.com/users/octocat" 

try:
    print("Attempting to connect to GitHub's server...")
    # We added a timeout so Python doesn't hang forever if the server is slow
    response = requests.get(url, timeout=5)
    
    # This line automatically triggers an error if the server returns a 4xx or 5xx failure code
    response.raise_for_status()

    # If everything is successful, process the data
    data = response.json()
    print(f"Success! Fetched user: {data['login']}")


except requests.exceptions.Timeout as a:
    print(f"the error is{a} ")
except requests.exceptions.ConnectionError:
    print("connection errror") 
except requests.exceptions.HTTPError as b:
    print(f"error is{b} ")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")