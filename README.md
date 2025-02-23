# Multi-Document AI Chatbot for PDF, DOCX, and PPT Files 📚

This application uses **Streamlit** to create an interactive chatbot capable of answering questions based on the content of PDF, DOCX, and PPTX files. It uses **LangChain** for conversation management and **FAISS** for vector search.  

---

## Features 🚀
- 📄 **Content extraction** from PDF, DOCX, and PPTX files.  
- 🤖 **Intelligent chatbot** powered by a LLM model using `LlamaCpp`.  
- 🔎 **Contextual search** through integration with `FAISS`.  
- 📂 **Multi-document support** to query multiple files simultaneously.  
- 💾 **Conversation download** to save the chat history.  

---

## Prerequisites 🛠️
Before running the application, make sure you have the following installed:  
- **Python 3.9+**  
- **pip** for managing Python packages  
- **Streamlit** for the user interface  
- **LangChain**, **HuggingFaceEmbeddings**, **FAISS**, **LlamaCpp**, **PyPDFLoader**, and **python-docx** for document processing and chatbot.  

---

## Installation ⚙️
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On MacOS/Linux
    .\venv\Scripts\activate   # On Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Dependencies 📦
The main modules used in this project are:
- **Streamlit**: For creating the interactive user interface.
- **LangChain**: For managing the conversations with the AI.
- **FAISS**: For efficient vector search.
- **HuggingFaceEmbeddings**: For creating embeddings from the text.
- **LlamaCpp**: For the LLM model used in the chatbot.
- **PyPDFLoader**: For extracting text from PDF files.
- **python-docx**: For handling DOCX files.
- **python-pptx**: For extracting text from PPTX files.

You can install them manually or by using the `requirements.txt` file.

---

## Usage 🚀
1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to the following URL:
    ```
    http://localhost:8501
    ```

3. **Upload** one or more files (PDF, DOCX, PPTX) from the sidebar.
4. **Ask a question** in the text box and the chatbot will respond based on the content of the uploaded files.
5. **Download the conversation** using the provided button.


---

## How It Works ⚙️
1. **File Upload**: The user uploads PDF, DOCX, or PPTX files.
2. **Text Extraction**: Text is extracted using `PyPDFLoader`, `python-docx`, and `python-pptx`.
3. **Vectorization**: The text is split into chunks and transformed into embeddings using `HuggingFaceEmbeddings`.
4. **Contextual Search**: Embeddings are stored in a **FAISS** index for fast retrieval.
5. **Conversational Chatbot**: `LlamaCpp` is used to generate contextual responses based on user queries.

---

## Model Used 🤖
The chatbot uses the model `mistral-7b-instruct-v0.1.Q4_K_M.gguf` with `LlamaCpp`. Be sure to download the model from [HuggingFace](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf) and place it in your project directory. Update the model path in the code:
```bash
model_path = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

---

## Important Reminder ⚠️
Please **do not forget to download the model** from Hugging Face before running the chatbot. The model is required for the chatbot to work properly.  

You can download the model **mistral-7b-instruct-v0.1.Q4_K_M.gguf** from the following Hugging Face link:
- [Download Mistral-7B-Instruct Model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf)

Once downloaded, place the model file in the project directory and update the `model_path` in the code accordingly:
```python
model_path = "path/to/your/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
```
