import os

from dotenv import load_dotenv
from langchain.chat_models import BaseChatModel, init_chat_model

load_dotenv(override=True)

LLM_MODEL = os.getenv("LOCAL_LLM_MODEL", "llama3.2:1b")   
LLM_MODEL_PROVIDER = os.getenv("LOCAL_LLM_MODEL_PROVIDER", "ollama")


def get_local_llm_model() -> BaseChatModel:
    model = init_chat_model(
        LLM_MODEL,
        model_provider=LLM_MODEL_PROVIDER,
    )
    return model


if __name__ == "__main__":
    model = get_local_llm_model()
    response = model.invoke("Write a funny joke about programming.")
    print(response.content)