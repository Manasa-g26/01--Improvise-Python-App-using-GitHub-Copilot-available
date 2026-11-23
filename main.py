# Create a Pydantic model for the JSON body that contains a single field called 'text'
# Create a FastAPI endpoint that accepts a POST request with a JSON body containing 'text' and returns a checksum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model
class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Developed by Manasa"}
    
@app.post("/checksum")
def get_checksum(request: TextRequest):
    # Compute checksum
    checksum = hashlib.sha256(request.text.encode()).hexdigest()
    return {"checksum": checksum}



