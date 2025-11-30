from fastapi import FastAPI

app = FastAPI()

# Testing
@app.get("/")
def read_root():
    return {"Hello": "World"}
    if not app:
        raise RuntimeError("App instance is null")
    # Return a simple message
