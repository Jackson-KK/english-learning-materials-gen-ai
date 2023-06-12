
from langchain.chat_models import ChatOpenAI

from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os
from langchain.text_splitter import TokenTextSplitter

import openai
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']



def split_article_into_phragraphs(article):
    text_splitter = TokenTextSplitter(chunk_size=100, chunk_overlap=0)
    phragraphs = text_splitter.split_text(article)
    return phragraphs


def get_translations(phragraphs, native_language):
    chat = ChatOpenAI(temperature=0)
    batch_messages = [
        [
            SystemMessage(content=f"You are a helpful assistant that translates English to {native_language}."),
            HumanMessage(content=f"""
                         Please translate the following paragraph
                         paragraph: ```{p}```
                         """)
        ] for p in phragraphs
    ]
    result = chat.generate(batch_messages)
    print("result:", result)
    formattedResult = []
    for generations in result.generations:
        for index, generation in enumerate(generations):
            formattedResult.append({
                "translation": generation.text,
                "englishText": phragraphs[index]
            })
    print("formattedResult:", formattedResult)
    return formattedResult


def get_generated_language_learning_materials(article, native_language, english_level):
    phragraphs = split_article_into_phragraphs(article)
    translations = get_translations(phragraphs, native_language)
    return { "translations": translations }

