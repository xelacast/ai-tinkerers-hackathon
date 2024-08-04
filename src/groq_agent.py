# import getpass
import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["GROQ_API_KEY"] = getpass.getpass()
api_key = os.environ["GROQ_API_KEY"]
from langchain_groq import ChatGroq

model = ChatGroq(model="llama3-8b-8192", api_key=api_key)

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="here is a recipe"),
    HumanMessage(content="make me a recipe"),
]
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# model.invoke(messages)

from langchain_core.prompts import ChatPromptTemplate

system_template = "you are a nutritionist"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"recipe": "italian", "text": "hi"})

# print(result)

chain = prompt_template | model | parser

# print(chain.invoke({"language": "italian", "text": "hi"}))

from langchain_core.runnables.history import RunnableWithMessageHistory

# from langchain_community

# with_message_history = RunnableWithMessageHistory(runnable=chain, get_session_history)