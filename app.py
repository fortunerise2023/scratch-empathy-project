
   import streamlit as st
   import pandas as pd
   import matplotlib.pyplot as plt

   st.set_page_config(page_title="Scratch Empathy Project", layout="wide")

   # --- Hero Header ---
   col1, col2 = st.columns([1, 8])
   with col1:
       st.image("assets/scratch-logo.png", width=80)
   with col2:
       st.title("Scratch Empathy Project")
       st.subheader("Inclusive Coding Education for Neurodiverse Learners")
       st.markdown("> *'Coding is a language — every brain deserves a voice.'*  
— **Yixuan Li**, Project Creator")

   st.divider()

   st.header("📘 Project Overview")
   st.markdown("""
   This is a self-initiated education-tech project built by Yixuan Li (BJIBS Class of 2026) to teach logic and creativity to children with autism using Scratch. The project merges programming education with cognitive scaffolding and emotional inclusivity.
   """)

   st.divider()
   st.header("📚 Curriculum Design")
   st.markdown("""
   - **Module 1**: Avatar and Identity Expression  
   - **Module 2**: Interactive Stage Animation  
   - **Module 3**: Sound & Sensory Feedback  
   - **Module 4**: Logic Games with If-Else & Loops  
   - **Module 5**: Capstone: Create & Present Own Game
   """)

   st.divider()
   st.header("📊 Learning Engagement Data")
   try:
       df = pd.read_csv("data/feedback.csv")
       fig, ax = plt.subplots()
       df.groupby("Lesson")["AttentionScore"].mean().plot(kind="bar", color="#4c72b0", ax=ax)
       ax.set_ylabel("Score")
       ax.set_xlabel("Lesson #")
       ax.set_title("Focus Trend")
       st.pyplot(fig)
       with st.expander("📄 Raw Feedback Table"):
           st.dataframe(df)
   except Exception as e:
       st.warning("Data failed to load: " + str(e))

   st.divider()
   st.header("🎬 In-Class Video (Highlight)")
   st.video("https://www.youtube.com/embed/YOUR_VIDEO_ID")

   st.divider()
   st.header("📎 Project Summary Download")
   with open("data/scratch_summary.pdf", "rb") as f:
       st.download_button("📄 Download Project Summary", f, file_name="ScratchEmpathy_YixuanLi.pdf")

   st.divider()
   st.header("👤 About the Creator")
   st.markdown("""
   **Yixuan Li** is a student at Beijing JunChen International Bilingual School (BJIBS), graduating 2026.  
   He is passionate about accessible computing and human-centered technology.  
   _This project is submitted as part of his MIT Research Portfolio._
   """)
