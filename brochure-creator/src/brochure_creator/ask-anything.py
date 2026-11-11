import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from brochure_creator.model import get_local_llm_model

load_dotenv(override=True)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that answers users questions."),
    HumanMessage(content="{message}"),
])

llm_chain = prompt | get_local_llm_model()

def ask_anything(message: str) -> str:
    response = llm_chain.invoke({"message": message})
    return response.content

if __name__ == "__main__":
    gr.Interface(
        fn=ask_anything,
        inputs=gr.Textbox(label="Enter your message"),
        outputs=gr.Textbox(label="Response"),
        title="Ask Anything",
        description="Enter a question and get an answer in response.",
        flagging_mode="never"
    ).launch()