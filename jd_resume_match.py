import pandas as pd
from sentence_transformers import SentenceTransformer, util
from utils.text_extraction import extract_text_from_pdf

# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_resumes(jd_text, resume_files):
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    scores = []

    for resume in resume_files:
        text = extract_text_from_pdf(resume)
        embedding = model.encode(text, convert_to_tensor=True)
        similarity = util.cos_sim(jd_embedding, embedding).item()
        scores.append({"Resume": resume.name, "Score": round(similarity, 3)})

    return pd.DataFrame(sorted(scores, key=lambda x: x["Score"], reverse=True))
