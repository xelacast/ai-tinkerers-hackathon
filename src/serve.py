#!/usr/bin/env python
from typing import List
# import os

from groq_agent import chain as groq_chain

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
from groq_history import rag_chain_with_source, conversational_rag_chain_with_history, rag_chain
# from dotenv import load_dotenv
# load_dotenv()
# 1. Create prompt template
# system_template = "Translate the following into {language}:"
# prompt_template = ChatPromptTemplate.from_messages([
#     ('system', system_template),
#     ('user', '{text}')
# ])

# 2. Create model
# model = ChatGroq(model="llama3-8b-8192", api_key=os.environ["GROQ_API_KEY"])

# 3. Create parser
# parser = StrOutputParser()

# 4. Create chain
# chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    groq_chain,
    path="/chain",
)

add_routes(
    app,
    rag_chain,
    path="/rag",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)