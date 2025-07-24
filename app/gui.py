import streamlit as st
from utils import clean_text
st.set_page_config(page_title="Phishing Detector", layout = "centered")
st.title("Simple Phishing Detecor")

#inputs 
subject = st.text_input("Subject:")
body = st.text_area("Body:")

#model selector dropdown 
selected_model_name = st.selectbox(
    "Choose a model for predicition:",
    ["Logistic Regression", "Naive Bayes", "SVM", "Random Forest"]
)

if st.button("check email"):
    email_text = subject + "" + body
    if email_text.strip() == "":
        st.warning("please enter something")
    else:
        st.subheader("**Your Email Content:**")
        st.info(email_text)
        
        cleaned = clean_text(email_text)
        st.subheader("Cleaned Email Text")
        st.code(cleaned)
        
        st.subheader("Selected Model")
        st.success(f"You selected: {selected_model_name}")