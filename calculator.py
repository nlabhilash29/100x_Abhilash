from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import os

app = FastAPI()

class Calculation(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    x: float
    y: float

@app.post("/calculate")
async def calculate(calc: Calculation):
    try:
        if calc.operation == "add":
            result = calc.x + calc.y
        elif calc.operation == "subtract":
            result = calc.x - calc.y
        elif calc.operation == "multiply":
            result = calc.x * calc.y
        elif calc.operation == "divide":
            if calc.y == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = calc.x / calc.y
        else:
            raise ValueError("Invalid operation")
        
        return {"result": result}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Calculator API"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("calculator:app", host="0.0.0.0", port=port, reload=False)
