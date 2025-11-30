# Test with curl
# GET with no parameters
# curl -X GET "http://127.0.0.1:8000/" -H "accept: application/json"

# GET with a parameter
# curl -X GET "http://127.0.0.1:8000/items/1" -H "accept: application/json"

# POST with a parameter
# curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d "{\"name\": \"Book\", \"price\": 12.99}"

import requests

# Test GET endpoint
response = requests.get("http://127.0.0.1:8000/")
print("GET / response:", response.json())

# Test GET endpoint with path parameter
response = requests.get("http://127.0.0.1:8000/items/1")
print("GET /items/1 response:", response.json())

# Test POST endpoint
payload = {"name": "Book", "price": 12.99}
response = requests.post("http://127.0.0.1:8000/items/", json=payload)
print("POST /items/ response:", response.json())
