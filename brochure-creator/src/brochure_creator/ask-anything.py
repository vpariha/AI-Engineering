import os
import gradio as gr
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv(override=True)

LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "llama3.2:1b")   
LLM_MODEL_PROVIDER = os.getenv("LOCAL_LLM_MODEL_PROVIDER", "ollama")

model = init_chat_model(
    LLM_MODEL,
    model_provider=LLM_MODEL_PROVIDER,
)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant that answers users questions."),
    HumanMessage(content="{message}"),
])

llm_chain = prompt | model

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