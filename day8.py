# Day 8: Working with JSON and API Data Structures
import json

# Simulating a response coming back from an AI model API in JSON format
# Notice it looks just like a Python dictionary stored inside a string!
api_response_json = '{"model": "gpt-4o", "tokens_used": 42, "reply": "Hello, tapai! How can I help you build AI systems today?"}'

# 1. Convert JSON string into a usable Python dictionary using json.loads()
response_dict = json.loads(api_response_json)

print("--- Parsing AI API Response ---")
print(f"Model used: {response_dict['model']}")
print(f"Tokens consumed: {response_dict['tokens_used']}")
print(f"AI Message: {response_dict['reply']}")
print(f"the model is: {response_dict['model']}")

# 2. Converting a Python dictionary back into a JSON string to send out
my_request_data = {
    "prompt": "Explain vector databases in simple terms.",
    "temperature": 0.5
}

json_payload = json.dumps(my_request_data,indent=1)
print("\n--- Outgoing JSON Payload to AI Model ---")
print(json_payload)