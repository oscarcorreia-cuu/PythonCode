import requests

# Make a GET request to the root endpoint
response = requests.get("http://127.0.0.1:8000/")

# Print the JSON response from the API
print("Response from API:", response.json())