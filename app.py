import streamlit as st
import io

from datetime import date
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseUpload

def upload_to_drive(file_name, content, mime_type='text/plain'):
    # Use the token from the logged-in volunteer session
    credentials = st.user.token 
    service = build('drive', 'v3', credentials=credentials)
    
    # 1. Define the destination (Your 2 TB Folder ID)
    # Replace 'ROOT_OR_FOLDER_ID' with your actual Folder ID from the URL
    file_metadata = {
        'name': file_name,
        'parents': ['ROOT_OR_FOLDER_ID'] 
    }
    
    # 2. Prepare the file data
    media = MediaIoBaseUpload(io.BytesIO(content.encode()), mimetype=mime_type)
    
    # 3. Execute the upload
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

st.set_page_config(page_title="Y4J Candidate Info Builder", layout="centered")

# 1. Force Login
if not st.experimental_user.is_logged_in:
    st.header("Volunteer Portal")
    st.info("Please log in with your Google account to contribute.")
    if st.button("Log in with Google"):
        st.login()
    st.stop()

# 2. Authenticated View
user = st.experimental_user
st.sidebar.write(f"Logged in as: {user.email}")
if st.sidebar.button("Logout"):
    st.logout()

st.title("🏗️ Y4J Candidate Info Builder")
st.write("Welcome to the production builder. Use the tools below to submit data.")

# 3. Data Entry Form
with st.form("entry_form", clear_on_submit=True):
    st.subheader("New Contribution")
    
    # Text input for the title
    info_title = st.text_input("Information Title", placeholder="e.g., Annual Report 2025")
    
    # Dropdown for better organization in your 2 TB Drive
    category = st.selectbox("Category", ["Finance", "Legal", "Marketing", "Research", "Other"])
    
    # Date picker (helps with sorting files/rows)
    entry_date = st.date_input("Document Date", date.today())
    
    # Multi-line text for details
    details = st.text_area("Details/Description", placeholder="Enter a brief summary of the info...")
    
    # Optional: File uploader for the 2 TB Drive
    uploaded_file = st.file_uploader("Attach Document (PDF, PNG, JPG)", type=["pdf", "png", "jpg"])
    
    # The submit button
    submit = st.form_submit_button("Upload to Production")

if submit:
    if not info_title:
        st.error("Please provide a title before submitting.")
    else:
        # DATA PROCESSING LOGIC GOES HERE
        st.success(f"Processing '{info_title}' for the {category} folder...")
