import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .llm import LLM

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

llm = LLM()

@app.get("/")
def health_check():
    return {"message": "Hello, World!"}

@app.get("/chat/{query}")
def chat(query: str):
    response = llm.chat(query)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="127.0.0.1", port=port)
