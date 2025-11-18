
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analysis - RoBERTa")
st.title("Sentiment Analysis using RoBERTa")
st.write("This app uses a RoBERTa model (cardiffnlp/twitter-roberta-base-sentiment).")

@st.cache_resource
def get_classifier():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

classifier = get_classifier()

user_input = st.text_area("Enter a sentence to analyze sentiment:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = classifier(user_input)[0]
        st.subheader("Result:")
        st.write("**Label:**", result['label'])
        st.write("**Confidence:**", round(result['score'], 4))
