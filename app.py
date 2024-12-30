from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample data
data = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# Pydantic model for user data
class User(BaseModel):
    id: int
    name: str
    age: int

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to MASTER!"}

# Get all users
@app.get("/users")
def get_users():
    return data

# Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in data if u["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Add a new user
@app.post("/users", status_code=201)
def add_user(user: User):
    data.append(user.model_dump())
    return {"message": "User added successfully!"}

# Run with uvicorn (if running as main)
# Command: uvicorn app:app --reload
