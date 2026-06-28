import streamlit as st
from deep_translator import GoogleTranslator

st.title("My Translation Tool")

languages = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "hindi": "hi",
    "german": "de"
}

col1, col2 = st.columns(2)

with col1:
    from_lang = st.selectbox("Translate From", list(languages.keys()))

with col2:
    to_lang = st.selectbox("Translate To", list(languages.keys()))

text = st.text_area("Enter your text here", height=100)

if st.button("Translate"):
    if text:
        translated_text = GoogleTranslator(
            source=languages[from_lang],
            target=languages[to_lang]
        ).translate(text)

        st.success("Translation:")
        st.write(translated_text)

    else:
        st.warning("Please enter some text")