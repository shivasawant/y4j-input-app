import streamlit as st
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import date

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
