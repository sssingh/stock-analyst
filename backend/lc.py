import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_ollama import ChatOllama

dotenv.load_dotenv()


def connect(
    host: Literal["azure", "openai", "ollama"],
) -> BaseChatModel:
    """Connect to specified host_type LLM

    Args:
        host (Literal["azure", "openai", "ollama"]): host type

    Returns:
        BaseChatModel: AzureChatOpenAI or ChatOpenAI or ChatOllama (local)
    """
    # connect with LLM
    if host == "azure":
        llm = AzureChatOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.7,
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_LLM_DEPLOYMENT_ID"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )
    elif host == "openai":
        llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.7,
            model="gpt-4o-mini",
        )
    elif host == "ollama":
        llm = ChatOllama(
            temperature=0.7,
            model="",
        )
    else:
        llm = None
    return llm


def make_prompt_template(
    system_prompt: str = "", user_prompt: str = ""
) -> ChatPromptTemplate:
    """prepare ChatPromptTemplate from strings

    Args:
        system_prompt (str, optional): system/persona message. Defaults to "".
        user_prompts (str, optional): user supplied message. Defaults to "".

    Returns:
        ChatPromptTemplate: the prompt template
    """
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("user", user_prompt),
        ]
    )
    return prompt_template


def predict(
    llm: BaseChatModel,
    prompt_template: ChatPromptTemplate,
    style: str,
    stock: str,
) -> str:
    """Generate response using the LLM

    Args:
        llm (BaseChatModel): connected LLM
        prompt_template (ChatPromptTemplate): prepared prompt template
        mood (str): style of response required
        stock (str): stock symbol to be analysed

    Returns:
        str: LLM generated text response
    """
    print("[INFO]: Making LLM chain...")
    chain = prompt_template | llm | StrOutputParser()
    print(f"[INFO]: LLM analyzing the {stock} stock...")
    try:
        response = chain.invoke({"style": style, "stock": stock})
    except Exception as e:
        print("[ERROR] - Request failed...")
        print(e)
    else:
        print("[INFO]: Analysis completed successfully!")
    return response
