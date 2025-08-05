import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("📝 Text Sentiment Analyzer")
st.write("Enter any text, and I will analyze the sentiment for you.")

text_input = st.text_area("✍ Enter your text here:")

if st.button("Analyze Sentiment"):
    if text_input:
        blob = TextBlob(text_input)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("😊 Positive Sentiment")
        elif sentiment < 0:
            st.error("😠 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

        st.write(f"*Polarity Score:* {sentiment}")
    else:
        st.warning("Please enter some text first.")
