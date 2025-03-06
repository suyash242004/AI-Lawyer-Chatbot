# 📜 AI Lawyer - RAG-Powered Legal Chatbot

AI Lawyer is a Retrieval-Augmented Generation (RAG) chatbot that provides legal assistance by answering questions based on uploaded legal documents. It leverages FAISS for vector search, DeepSeek R1 for LLM-based responses, and Streamlit for a user-friendly interface. ⚖️🤖

## ✨ Features

- 📂 **Upload Legal PDFs** - Upload legal documents to get precise legal responses.
- 🔍 **Retrieval-Augmented Generation (RAG)** - Uses FAISS for document retrieval and DeepSeek R1 LLM for intelligent responses.
- 🏛️ **Legal AI Chatbot** - Ask questions and receive answers based on the uploaded documents.
- 🎨 **User-Friendly UI** - Built using Streamlit for an interactive chat experience.

## 🛠️ Tools & Technologies Used

- 🐍 **Python** - Core programming language.
- 📚 **LangChain** - Framework for building LLM-powered applications.
- 💾 **FAISS** - Vector database for efficient document retrieval.
- 🤖 **DeepSeek R1** - LLM for natural language understanding.
- 📄 **PDFPlumber** - Extracts text from PDF files.
- 🎨 **Streamlit** - Web framework for interactive UI.
- 🔐 **dotenv** - Manages API keys securely.

## 🚀 How It Works

### 1️⃣ Upload & Load PDFs

- Users upload a legal PDF.
- The PDF is processed, and text is extracted using **PDFPlumber**.

### 2️⃣ Create Text Chunks & Generate Embeddings

- The extracted text is split into chunks using **LangChain’s RecursiveCharacterTextSplitter**.
- Each chunk is converted into vector embeddings using **DeepSeek R1 with Ollama**.

### 3️⃣ Store & Retrieve Documents

- Embeddings are stored in **FAISS**, a fast and efficient vector database.
- When a user asks a legal question, the chatbot retrieves relevant documents using FAISS.

### 4️⃣ Generate Answers Using DeepSeek R1

- Retrieved documents are passed to **DeepSeek R1 via Groq** to generate precise legal responses.
- The answer is displayed in an interactive chat format using **Streamlit**.

## 🎯 Usage

1️⃣ **Upload a PDF** 📂
2️⃣ **Enter your legal question** ✍️
3️⃣ **Get an AI-generated response** 🤖⚖️



This project is open-source under the **MIT License**.

---

Enjoy using AI Lawyer! ⚖️🤖
