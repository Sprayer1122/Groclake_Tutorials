import streamlit as st
import requests

# Flask API endpoints
UPLOAD_DOCUMENT_URL = "http://127.0.0.1:5000/upload_document"
CHAT_URL = "http://127.0.0.1:5000/chat"

st.title("Office HR Assistant")
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Upload Document", "Chat with Assistant"])

if page == "Upload Document":
    st.header("Upload Office Policies or Documents")
    
    # Input for document URL
    document_url = st.text_input("Enter the URL of the document (e.g., HR policies, employee handbook):")
    
    if st.button("Upload Document"):
        if not document_url:
            st.error("Please enter a document URL.")
        else:
            # Send the document URL to the Flask app
            response = requests.post(UPLOAD_DOCUMENT_URL, json={"document_url": document_url})
            
            if response.status_code == 200:
                st.success("Document uploaded and processed successfully!")
            else:
                st.error(f"Failed to upload document: {response.json().get('error')}")

elif page == "Chat with Assistant":
    st.header("Chat with the Office HR Assistant")
    
    # Input for user query
    user_query = st.text_area("Ask a question related to HR or office policies:")
    
    if st.button("Send Query"):
        if not user_query:
            st.error("Please enter your question.")
        else:
            # Send the query to the Flask app
            response = requests.post(CHAT_URL, json={"query": user_query})
            
            if response.status_code == 200:
                answer = response.json().get("answer", "No response received.")
                st.success(f"Assistant: {answer}")
            else:
                st.error(f"Failed to process query: {response.json().get('error')}")
