import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI app to serve API requests
app = FastAPI()

# Define a request model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Handle login requests
@app.post("/login")
async def login(request: LoginRequest):
    if request.username == "admin" and request.password == "password123":
        return {"status": "success", "message": "Login successful"}
    else:
        return {"status": "error", "message": "Invalid credentials"}

# Use Streamlit for displaying the API documentation or admin interface
st.title("Streamlit + FastAPI Integration")
st.write("API is running and ready to receive requests.")

# Run FastAPI app with Streamlit (requires `uvicorn`)
def start():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    start()
