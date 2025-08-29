# backend.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# allow frontend (website) to talk with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # Here you can add AI logic (OpenAI, DeepSeek, etc.)
    if "weather" in user_message.lower():
        response = "Today’s weather is sunny with light clouds ☀️"
    else:
        response = f"Jarvis reply to: {user_message}"

    return {"reply": response}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=5000, reload=True)
