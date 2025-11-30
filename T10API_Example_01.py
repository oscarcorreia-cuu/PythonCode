# cd "G:\My Drive\System Updates\1564 - BSE224-DDA1101 Python Programming 2025S01\02 - Content\Week 08\Code"
# g:
#  c:\python313\Scripts\uvicorn API_Example_01:app --reload

from fastapi import FastAPI, HTTPException, Request
import uvicorn

# Create a FastAPI app instance
app = FastAPI()

# GET endpoint for the root path
def read_root():
    return {"message": "Welcome to the BSE2224/DDA1101 Python Programming FastAPI REST API"}

# Register the root endpoint without using decorators
app.add_api_route("/", read_root, methods=["GET"])

# GET endpoint to retrieve an item by its ID
def read_item(item_id: int):
    # Check for a valid item_id
    if item_id < 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item", "price": 42.0}

# Register the GET endpoint with a path parameter
app.add_api_route("/items/{item_id}", read_item, methods=["GET"])

# POST endpoint to create a new item; we'll process the JSON data manually
async def create_item(request: Request):
    # Retrieve the JSON body from the request
    body = await request.json()
    
    # Simple validation: ensure required keys are present
    if "name" not in body or "price" not in body:
        raise HTTPException(status_code=400, detail="Missing required fields: 'name' and 'price'")
    
    # Normally, you might save the item to a database here
    return {"message": "Item created successfully", "item": body}

# Register the POST endpoint without using decorators
app.add_api_route("/items/", create_item, methods=["POST"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
