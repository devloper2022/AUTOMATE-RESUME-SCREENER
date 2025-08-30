Resume Shortlisting Tool
Overview

This project is an automated resume screening tool for Salesforce Engineer hiring. It uses Natural Language Processing (NLP) and Machine Learning to match resumes with a Job Description (JD) and ranks them based on relevance.

The project includes a Streamlit dashboard for easy interaction — simply paste a JD, upload resumes, and get a ranked shortlist.

Features

Upload multiple resumes (PDF) at once

Paste Job Description text

Scores resumes based on semantic similarity with JD

Displays a ranked table of candidates

Fully interactive Streamlit dashboard

Folder Structure
resume-shortlisting-nlp/
│── app.py                # Streamlit dashboard
│── jd_resume_match.py    # Core logic for JD-Resume matching
│── requirements.txt      # Python dependencies
│── data/                 # Sample data
│    ├── sample_jd.txt
│    ├── sample_resume1.txt
│── utils/
│    └── text_extraction.py  # Helper function to extract text from PDFs

Sample Data

Job Description (sample_jd.txt):

We are hiring a Salesforce Engineer with experience in Apex, Lightning, and REST APIs.


Sample Resume (sample_resume1.txt):

John Doe
Skills: Salesforce, Apex, Lightning, Python


You can add more resumes in the data/ folder as text or PDF files.

Installation & Setup

Clone the repository

git clone <your-repo-url>
cd resume-shortlisting-nlp


Install dependencies

pip install -r requirements.txt


Run the Streamlit dashboard

streamlit run app.py


Open the dashboard in your browser (usually opens at http://localhost:8501).

Usage

Paste the Job Description in the text box.

Upload one or multiple resumes (PDF or text).

Click Shortlist.

The table will display resumes with similarity scores in descending order.

How It Works

The JD and resumes are converted into embeddings using the SentenceTransformer model (all-MiniLM-L6-v2).

Cosine similarity is calculated between JD and each resume.

Resumes are ranked by similarity score.

Dependencies

Python 3.8+

Streamlit

pandas

pdfminer.six

sentence-transformers

spacy

numpy

Install all via:

pip install -r requirements.txt

Notes

PDF resumes are extracted using pdfminer.six.

For text resumes, you can directly read the text files.

You can add more sample resumes to the data/ folder for testing.

Screenshots

Dashboard view:

+---------------------------------------------+
| Resume Shortlisting Tool                     |
+---------------------------------------------+
| [Job Description Box]                        |
| [Upload Resumes Button]                      |
| [Shortlist Button]                           |
+---------------------------------------------+
| Resume Name        | Score                   |
| resume1.pdf        | 0.87                    |
| resume2.pdf        | 0.79                    |
| resume3.pdf        | 0.65                    |
+---------------------------------------------+
