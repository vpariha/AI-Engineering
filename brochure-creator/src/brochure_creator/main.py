import gradio as gr
from langchain_community.document_loaders import WebBaseLoader

from brochure_creator.model import get_local_llm_model
from langsmith import traceable 

@traceable()
def load_web_content(url: str):
    loader = WebBaseLoader(url)
    loaded_documents = loader.load()
    content = ""
    if loaded_documents:
        for document in loaded_documents:
            content += document.page_content + "\n"
    return content

prompt = """
    system: You are a helpful assistant who is expert in generating brochures for businesses based on the content of the webpage provided. If the content does not provide enough information to generate a brochure, you should respond with 'I don't know'.
    content: {content}
"""

@traceable()
def generate_brochure(url: str):
    content = load_web_content(url)
    stream = get_local_llm_model().stream(
            prompt.format(content=content)
    )
    response_content = ""
    for event in stream:
        response_content += event.content
        yield response_content

if __name__ == "__main__":
    gr.Interface(
        fn=generate_brochure,
        inputs=gr.Textbox(label="Enter the URL of the webpage"),
        outputs=gr.Markdown(label="Generated Brochure"),
        title="Brochure Generator",
        description="Enter the URL of a webpage and get a brochure generated based on its content.",
        flagging_mode="never"
    ).launch()
