import app
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator
translator = Translator()
def page_1():
    st.title("Translate text into multiple languages")

    language_name = st.selectbox("Select a Language:", list(app.language_mapping.keys()))

    st.subheader("Translate the following sentence into the selected language:")
    sentence = st.text_input("Enter a Sentence in English:")
    if sentence:
        translation = translator.translate(sentence, dest=app.language_mapping[language_name]).text
        st.write(translation)
        app.text_to_voice(translation, app.language_mapping[language_name])