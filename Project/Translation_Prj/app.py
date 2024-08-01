import os
import pygame
from gtts import gTTS
import streamlit as st
from googletrans import LANGUAGES, Translator
import translate_text

translator = Translator()

def main(): 
    pygame.mixer.init()  
    st.set_page_config(page_title='Translation Tool', page_icon='📚')  
    page = st.sidebar.radio('Explore', ['Home',  'Text Language Translator'])

    if page == 'Home':
        st.title('Welcome to the Translation Tool!')

    elif page == 'Text Language Translator':
        translate_text.page_1()
    

language_mapping = {name: code for code, name in LANGUAGES.items()}

def get_language_code(language_name):
    return language_mapping.get(language_name, language_name)

def translator_function(spoken_text, from_language, to_language):
    return translator.translate(spoken_text, src='{}'.format(from_language), dest='{}'.format(to_language))


if __name__ == "__main__":
    main()