

# 🗣️ **ChatPDF**: Ask Questions About Your PDF Documents Using Azure RAG

**ChatPDF** is an interactive Streamlit application that allows you to upload a PDF and query it using a Retrieval-Augmented Generation (RAG) pipeline powered by Azure OpenAI and HuggingFace embeddings.

---

## 🚀 Features

- Upload and parse any PDF document.
- Chunk content with LangChain’s smart text splitter.
- Use HuggingFace embeddings to embed document chunks (stored in FAISS).
- Ask questions about the document using Azure OpenAI (ChatGPT).
- Clean, modular codebase for easy maintainability and reusability.

---

## 🗂️ Project Structure

```
ChatPDF/
│
├── app.py                     # Main Streamlit app
├── .env                       # API keys and environment settings
├── requirements.txt           # Python dependencies
│
├── utils/                     # Modular helper functions
│   ├── __init__.py            # Marks utils/ as a package
│   ├── pdf_utils.py           # PDF text extraction
│   ├── text_processing.py     # Text chunking and preprocessing
│   ├── vectorstore.py         # FAISS vector store setup
│   └── qa_chain.py            # RAG chain setup with Azure OpenAI
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/samyakshrma/ChatPDF.git
cd ChatPDF
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following contents:

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_TEMPERATURE=0

# Embedding model
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

---

## 🖥️ Run the App

```bash
streamlit run app.py
```

This will launch the ChatPDF app in your browser.

---

## 🧪 Example Usage

1. Upload a PDF document (e.g., a research paper, report, etc.).
2. Ask questions such as:
   - "Summarize this document."
   - "What are the key findings?"
   - "List the financial figures mentioned."
   - "What are the main topics covered?"

The app will process the PDF and generate answers based on its contents using the Azure OpenAI model.

---

## 📦 Dependencies

The following Python libraries are used in this project:

- `streamlit`: Web app framework
- `pdfplumber`: PDF text extraction
- `langchain`: For text chunking and LangChain integration
- `faiss-cpu`: FAISS vector search library
- `huggingface-hub`: HuggingFace embeddings
- `python-dotenv`: Environment variable management
- `langchain-openai`: LangChain integration for Azure OpenAI
- `torch`: Patched for compatibility with Streamlit file watcher

> Full dependencies are listed in `requirements.txt`.

---

## 🛡️ Notes

- **FAISS** is used for local vector search — no cloud storage required.
- Temporary files are used to handle PDFs securely during processing.
- The application patches `torch.classes` to avoid Streamlit’s file watcher crash, which can occur due to how PyTorch interacts with the Streamlit development server.

---

## 🧰 TODO / Future Improvements

- Support for other document formats (e.g., DOCX, TXT).
- Persistent vectorstore caching to improve performance.
- Enhanced UI/UX features, such as document previews or summaries.
- Dockerfile for easy containerization and deployment.

---

## 📄 License

MIT License – Feel free to fork, modify, and use the project under the terms of the MIT license.

---

### 🌟 Contributing

We welcome contributions! Please feel free to fork the repo, make improvements, and submit pull requests.

---

