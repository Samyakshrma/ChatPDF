import os
from langchain.chains import RetrievalQA
from langchain_openai import AzureChatOpenAI

def setup_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        temperature=float(os.getenv("AZURE_OPENAI_TEMPERATURE", 0))
    )
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
