from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent import agent
from app.models.schema import ChatRequest, ChatResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = agent.run(request.message)
    return {"response": result}
