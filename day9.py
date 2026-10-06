
import requests

# (Since tapai uses GitHub for your portfolio, let's see how GitHub's server responds!)
url = "https://api.github.com/users/octocat"

print("Sending request to GitHub's live server...")
response = requests.get(url)

# 1. Check if the request was successful 
# (Status code 200 means success! 404 means not found, 500 means server error)
if response.status_code == 200:
    # 2. Convert the live server response into a Python dictionary automatically
    data = response.json()
    
    print("\n--- Live API Data Received ---")
    print(f"Username: {data['login']}")
    print(f"Public Repositories: {data['public_repos']}")
    print(f"Profile Bio: {data['bio']}")
else:
    print(f"Request failed with status code: {response.status_code}")