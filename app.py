import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Scratch Empathy Project", page_icon="🧠", layout="wide")

# --- Hero Header ---
col1, col2 = st.columns([1, 8])
with col1:
    st.image("assets/scratch-logo.png", width=80)
with col2:
    st.markdown("### 🧩 MIT Research Supplement")
    st.title("Scratch Empathy Project")
    st.subheader("Inclusive Coding Education for Neurodiverse Learners")
    st.markdown("""
> *Coding is a language — every brain deserves a voice.*  
— **Yixuan Li**
""")

st.divider()

# --- Project Overview ---
st.header("📘 Project Overview")
st.markdown("""
The **Scratch Empathy Project** is a student-driven initiative developed by **Yixuan Li**, a high school student at *Beijing JunChen International Bilingual School*.

It teaches logical thinking and creative storytelling to children on the autism spectrum using MIT Scratch. The curriculum is inclusive, playful, and research-informed.
""")

st.divider()

# --- Curriculum Design ---
st.header("📚 Curriculum Modules")
st.markdown("A 5-module sequence designed for neurodiverse engagement:")
cols = st.columns(5)
modules = [
    ("🧍 Avatar Logic", "personalization & identity"),
    ("🎭 Stage Animation", "motion + storytelling"),
    ("🔊 Sound Triggers", "reaction + sensory"),
    ("🧩 Logic Games", "conditions & loops"),
    ("🎮 Capstone", "make your own Scratch game")
]
for i, (title, desc) in enumerate(modules):
    with cols[i]:
        st.markdown(f"**{title}**  
<sub>{desc}</sub>", unsafe_allow_html=True)

st.divider()

# --- Feedback and Data ---
st.header("📊 Student Focus Trends")
try:
    df = pd.read_csv("data/feedback.csv")
    avg = df.groupby("Lesson")["AttentionScore"].mean()
    fig, ax = plt.subplots()
    avg.plot(kind="bar", color="#FF914D", ax=ax)
    ax.set_ylabel("Avg. Focus Score (1–5)")
    ax.set_title("🧠 Avg. Attention per Module")
    ax.set_xlabel("Module #")
    st.pyplot(fig)
    with st.expander("📄 View Raw Feedback Table"):
        st.dataframe(df)
except Exception as e:
    st.error(f"Data load failed: {e}")

st.divider()

# --- Video Block ---
st.header("🎬 Live Teaching Sample")
st.video("https://www.youtube.com/embed/YOUR_VIDEO_ID")

# --- PDF download ---
st.divider()
st.header("📎 Download Project Summary")
with open("data/scratch_summary.pdf", "rb") as f:
    st.download_button("📄 Download PDF", f, file_name="ScratchEmpathy_YixuanLi.pdf")

# --- About the Creator ---
st.divider()
st.header("👤 About the Creator")
st.markdown("""
**Yixuan Li** is a student at *Beijing JunChen International Bilingual School*, Class of 2026.  
He is passionate about accessible computing and inclusive education.  
This work is submitted as part of his **MIT Research Portfolio**.
""")
