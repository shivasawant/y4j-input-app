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
with st.form("entry_form"):
    info_title = st.text_input("Information Title")
    details = st.text_area("Details")
    submit = st.form_submit_button("Upload to Drive")

    if submit:
        # Here we will add the function to push to the 2 TB Drive
        st.success("Saving to shivasawant's Drive...")
