# 🎓 CourseMate AI — Your AI-Powered Study Assistant

CourseMate AI is an intelligent, **Retrieval-Augmented Generation (RAG)** application that helps students learn more efficiently by answering questions from their academic PDF documents.

Built with Python, LangChain, Google Gemini, and ChromaDB, it allows users to upload study materials and ask context-aware questions. Instead of generating answers from general knowledge alone, CourseMate AI retrieves relevant information from uploaded documents and uses it to generate accurate, context-based responses.

---

## ✨ Key Features

- **PDF Upload:** Upload academic PDFs and use them as your personal knowledge base.
- **Intelligent Document Processing:** Extracts text from PDFs and splits it into smaller, manageable chunks.
- **Semantic Search:** Uses Google Gemini embeddings to understand the meaning of queries and document content.
- **Vector Database:** Stores document embeddings in ChromaDB for efficient similarity search.
- **Context-Aware Answers:** Uses a RAG pipeline to generate answers based on retrieved document content.
- **MMR-Based Retrieval:** Uses Maximal Marginal Relevance (MMR) to retrieve relevant and diverse document chunks.
- **Source References:** Displays source document information and page numbers alongside answers.
- **Interactive Interface:** Provides a simple and user-friendly interface using Streamlit.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| LangChain | RAG pipeline and application orchestration |
| Google Gemini | Large Language Model (LLM) |
| Gemini Embeddings | Text embedding generation |
| ChromaDB | Vector database |
| PyPDF | PDF document processing |
| Recursive Character Text Splitter | Document chunking |
| Python Dotenv | Environment variable management |

---

## 🏗️ Project Architecture

CourseMate AI follows a Retrieval-Augmented Generation (RAG) architecture consisting of two main workflows.

### 1. Document Ingestion Pipeline

When a user uploads a PDF:

1. PyPDFLoader extracts text from the PDF.
2. RecursiveCharacterTextSplitter divides the extracted text into smaller chunks.
3. Google Gemini Embeddings converts each chunk into a numerical vector.
4. ChromaDB stores the vectors along with their corresponding text and metadata.

**Workflow:**

```text
       PDF Upload
           |
           v
      PyPDFLoader
           |
           v
    Text Extraction
           |
           v
   Text Chunking
           |
           v
  Gemini Embeddings
           |
           v
       ChromaDB
    (Vector Storage)
```

### 2. Question Answering Pipeline

When a user asks a question:

1. The user's query is converted into an embedding.
2. ChromaDB retrieves relevant document chunks using semantic search and MMR.
3. Retrieved chunks are combined into a context.
4. The RAG prompt passes the context and question to the Gemini LLM.
5. Gemini generates an answer based on the retrieved information.
6. The application displays the answer along with source references.

**Workflow:**

```text
       User Question
             |
             v
      Query Embedding
             |
             v
       ChromaDB Search
             |
             v
     Relevant Documents
             |
             v
       RAG Prompt
             |
             v
       Gemini LLM
             |
             v
      Generated Answer
             |
             v
    Answer + Sources
```

---

## 📁 Project Structure

```text
CourseMate-AI/
│
├── app.py                     # Main Streamlit application
│
├── config/
│   ├── __init__.py
│   └── settings.py            # Application configuration
│
├── core/
│   ├── __init__.py
│   ├── document_processor.py  # PDF loading and text splitting
│   ├── embeddings.py          # Gemini embedding initialization
│   ├── vectorstore.py         # ChromaDB operations
│   └── rag_pipeline.py        # RAG question-answering pipeline
│
├── prompts/
│   ├── __init__.py
│   └── rag_prompt.py          # RAG prompt template
│
├── utils/
│   ├── __init__.py
│   └── helpers.py             # Helper functions
│
├── data/
│   ├── uploads/               # Uploaded PDF documents
│   └── chroma_db/             # Persistent vector database
│
├── .env                       # API key configuration
├── .gitignore                 # Git ignored files
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Installation and Setup

Follow these steps to run CourseMate AI locally.

### Prerequisites

Make sure you have installed:

- Python 3.10 or above
- Git
- A Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/CourseMate-AI.git
```

Navigate to the project directory:

```bash
cd CourseMate-AI
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your actual API key.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 🔑 API Configuration

CourseMate AI uses the Google Gemini API for:

- Generating document embeddings.
- Generating context-aware answers.

You can obtain an API key from:

[Google AI Studio](https://aistudio.google.com/)

**Important:** Never upload your `.env` file or expose your API key in a public repository.

---

## 🧠 Understanding the RAG Approach

Traditional LLM applications generate responses using information learned during model training. However, they may not know the specific content of a user's study materials.

CourseMate AI addresses this limitation using Retrieval-Augmented Generation.

The RAG approach combines:

- **Retrieval:** Finds relevant information from uploaded PDF documents.
- **Augmentation:** Adds the retrieved information to the LLM prompt as context.
- **Generation:** Uses Google Gemini to generate an answer based on the provided context.

This helps produce more relevant answers grounded in the user's uploaded study materials.

---

## 🚀 Future Enhancements

Planned improvements include:

- [ ] Support for additional document formats such as DOCX and TXT.
- [ ] Conversation memory for context-aware follow-up questions.
- [ ] User authentication and personalized study spaces.
- [ ] Multiple course and subject management.
- [ ] Chat history storage.
- [ ] Improved document retrieval and ranking.
- [ ] Deployment to a cloud platform.
- [ ] AI-generated summaries and practice questions.

---

## 🎯 Project Objective

The primary objective of CourseMate AI is to make academic learning more interactive and accessible by allowing students to communicate directly with their study materials.

It demonstrates the practical implementation of Retrieval-Augmented Generation, semantic search, vector databases, and Large Language Models in an educational application.

---

## 👨‍💻 Author

**PRADIP ADHIKARY**



---

⭐ If you find this project interesting, consider giving it a star!
