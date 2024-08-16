from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class CalculationRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(request: CalculationRequest):
    return {"result": request.a + request.b}

@app.post("/subtract")
def subtract(request: CalculationRequest):
    return {"result": request.a - request.b}

@app.post("/multiply")
def multiply(request: CalculationRequest):
    return {"result": request.a * request.b}

@app.post("/divide")
def divide(request: CalculationRequest):
    if request.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": request.a / request.b}