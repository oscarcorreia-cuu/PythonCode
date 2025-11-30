# uvicorn API_Example_02:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create a new FastAPI app instance
app = FastAPI()

# Define a Pydantic model to represent an item
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# Root endpoint: returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API"}

# GET endpoint with a path parameter to retrieve an item by its ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # For demonstration, we return a dummy item if the ID is positive
    if item_id < 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item", "price": 42.0}

# POST endpoint to create a new item. Expects data matching the Item model.
@app.post("/items/")
def create_item(item: Item):
    # Here, you might normally store the item in a database
    return {"message": "Item created successfully", "item": item}

# Code to run the app with Uvicorn when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
