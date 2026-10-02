import streamlit as st, PyPDF2
st.title("AI Resume Checker")
skills=["Python","SQL","Power BI","ML","GenAI"]
def get_text(p):
 r=PyPDF2.PdfReader(p)
 return "".join([x.extract_text() for x in r.pages])
f=st.file_uploader("Upload Resume",type=["pdf"])
if f:
 t=get_text(f).lower()
 k=[s for s in skills if s.lower() in t]
 s=int(len(k)/len(skills)*100)
 st.metric("Fit Score",f"{s}%")
 st.write("Found:",k)
