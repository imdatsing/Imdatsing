import streamlit as st
from streamlit_option_menu import option_menu

import Model1, Model2, Model3

st.set_page_config(
    page_title="Imdatsing",
)

class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self, title, function):
        sef.apps.append({
            "title": title,
            "function": function
        })
    
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Imdatsing',
                options=['Model 1', 'Model 2', 'Model 3'],
                menu_icon='chat-text-fill',
                default_index=1
            )

        if app=='Model 1':
            Model1.app()
        if app=='Model 2':
            Model2.app()
        if app=='Model 3':
            Model3.app()
    run()