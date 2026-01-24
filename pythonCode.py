
# install request and  gradio for gui of the ml and ai app
import requests
import gradio as gr

#deepseek API Endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def summerize_text(text):
  """
  Uses DeepSeek AI to Summarize a given text.

  """
  payload={
      "model": "deepseek-r1",
      "prompt": f" Generate a technical Summary the following text in **3 bullet points**:\n\n{text}",
      "stream":False
  }

  respone = requests.post(OLLAMA_URL,json=payload)

  if respone.status_code == 200:
    return respone.json().get("response","No summary generated.")
  else:
    return f'error : {respone.text}'
# Create Gradio Interface
interface = gr.Interface(
    fn=summerize_text,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summerize"),
    outputs=gr.Textbox(lines=5, label="Summary"),
    title="AI-Powered Text Summerization",
    discription="Enter a long text and DeepSeek AI will generate a concise summary."
)

# Launch the web app
if __name__ == "__main__":
  interface.launch()




#  #Test Summarization
# if __name__ == "__main__":
#  sample_text = """
# Artificial Intelligence (AI) is rapidly transforming industries across the globe.
# AI models like DeepSeek can analyze large datasets, identify patterns, and make predictions more efficiently than humans.
# Businesses leverage AI to enhance productivity, improve customer experience, and gain competitive advantages.
# As AI technology advances, ethical considerations, such as data privacy and bias, become increasingly important.
# AI-driven personalized recommendations are now common in e-commerce, healthcare, and entertainment,
# offering users tailored experiences based on their preferences and behavior.
# """


# print("### Summary ###")
# print(summerize_text(sample_text))







