import streamlit as st

def faq_page():
    st.title("FAQ - Frequently Asked Questions")
    
    # Liste des questions fréquemment posées et de leurs réponses
    faq_data = [
        {
            "question": "What is this app?",
            "answer": """
            This app allows you to upload PDF, DOC, and PPT files and interact with their content using artificial intelligence. 
            Once the files are uploaded, you can ask questions related to their content, and the app will generate accurate responses using an AI model, 
            allowing you to quickly extract information without having to manually read through the entire document.
            """
        },
        {
            "question": "How can I upload a PDF, DOC, or PPT file?",
            "answer": """
            To upload a PDF, DOC, or PPT, simply click on the 'Upload' button on the main page. After selecting your file, 
            the content will be processed and made available for you to ask questions based on the document's content. 
            Make sure your file is not corrupted and is in a readable format.
            """
        },
        {
            "question": "Can I upload multiple PDFs, DOCs, or PPTs?",
            "answer": """
            Yes, the app supports uploading multiple PDFs, DOCs, or PPTs at once. When you upload multiple files, 
            the app processes all the documents together, merging the contents to help answer questions based on any of the uploaded documents. 
            However, for very large documents, it may take some time to process them, so you may want to consider splitting files if they are too large.
            """
        },
        {
            "question": "How does the question-answering feature work?",
            "answer": """
            Once you upload your PDF, DOC, or PPT file, you can ask questions related to the content of that document. 
            The app uses an AI model to analyze the file and generate answers based on the extracted text. 
            This helps you find answers to specific queries quickly without needing to read the entire document.
            """
        },
        {
            "question": "What happens if the AI can't find an answer in the uploaded files?",
            "answer": """
            If the AI can't find a relevant answer in the uploaded file(s), it will notify you that the information is not available. 
            In some cases, it may attempt to provide the most relevant response possible based on the content available. 
            If your question is too specific or the document lacks relevant information, the AI may offer a generic response or suggest rephrasing the question.
            """
        },
    ]
    
    # Afficher les questions et réponses
    for faq in faq_data:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

# Intégrer cette page dans votre projet Streamlit
if __name__ == "__main__":
    faq_page()
