from fastapi import FastAPI
import requests

app = FastAPI()
ollama_api_url = "http://localhost:11434/api/generate"
@app.post("/summarize/")
def summarize_text(text: str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False,
        
    }
    response = requests.post(ollama_api_url, json=payload)
    return response.json().get("response", "No summary genereted")


# To run the FastAPI app, use the command:
# uvicorn fastapi:app --reload"max_tokens": 500,
