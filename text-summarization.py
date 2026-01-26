# install requests and gradio for the ML & AI GUI app
import requests
import gradio as gr

# DeepSeek API Endpoint (Ollama)
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """
    Uses DeepSeek AI to summarize a given text.
    """
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Generate a technical summary of the following text in **3 bullet points**:\n\n{text}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio Interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(lines=5, label="Summary"),
    title="AI-Powered Text Summarization",
    description="Enter a long text and DeepSeek AI will generate a concise summary."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()