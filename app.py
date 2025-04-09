import streamlit as st
import tempfile
import os
from dotenv import load_dotenv

from utils.pdf_utils import extract_text_from_pdf
from utils.text_processing import chunk_text
from utils.vectorstore import create_vectorstore
from utils.qa_chain import setup_qa_chain

# Patch torch.classes to avoid Streamlit file watcher crash
import sys
import types
if 'torch.classes' in sys.modules:
    sys.modules['torch.classes'].__path__ = []
else:
    sys.modules['torch.classes'] = types.ModuleType("torch.classes")
    sys.modules['torch.classes'].__path__ = []

# Load environment variables
load_dotenv()

def run_rag_pipeline(file, query):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    text = extract_text_from_pdf(tmp_path)
    os.remove(tmp_path)

    chunks = chunk_text(text)
    vectorstore = create_vectorstore(chunks)
    qa_chain = setup_qa_chain(vectorstore)
    return qa_chain.invoke(query)

# Streamlit UI
st.set_page_config(page_title="PDF Q&A (Azure RAG)", layout="centered")
st.title("📄 Ask Your PDF with Azure RAG")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")
    query = st.text_input("Ask a question (e.g., 'Summarize', 'What are key points?', etc.)")

    if query:
        with st.spinner("🤖 Thinking..."):
            try:
                answer = run_rag_pipeline(uploaded_file, query)
                st.markdown("### 📌 Answer")
                st.write(answer['result'])
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
