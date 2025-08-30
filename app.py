import streamlit as st
import pandas as pd
from jd_resume_match import match_resumes

st.title("📂 Resume Shortlisting Tool")

jd = st.text_area("Paste the Job Description here:")
uploaded_files = st.file_uploader("Upload resumes (PDF)", accept_multiple_files=True)

if st.button("Shortlist"):
    if jd and uploaded_files:
        results = match_resumes(jd, uploaded_files)
        st.dataframe(results)
        st.success("Shortlisting complete ✅")
    else:
        st.error("Please provide JD and resumes")
