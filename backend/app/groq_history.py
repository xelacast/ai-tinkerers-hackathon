from langchain_groq import ChatGroq
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import JSONLoader
from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_text_splitters import RecursiveCharacterTextSplitter


from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="llama-3.1-8b-instant")

def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["title"] = record.get("title")
    metadata["dish_name"] = record.get("dishName")

    return metadata

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Load json db
file_path = "../db/recipes.json"
loader = JSONLoader(file_path=file_path, jq_schema=".[]", text_content=False)
docs = loader.load()

# Create a vectorstore and retriever
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

system_prompt = (
    "You are a profressional chef and a chef's assistant. You will be given a recipe and you will need to extract the ingredients and the instructions from the recipe. Format the recipes in a easy to read and sequential manner. Add the ingredient amounts to the instructions. DO NOT USE ingredients that are not present to you. If the name of the dish, title, ingredients, and instructions are duplicated ONLY USE ONE. \n\n {context}"
)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, qa_prompt
)

question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


conversational_rag_chain_with_history = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)