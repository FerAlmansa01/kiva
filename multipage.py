# Imports
import streamlit as st 

# Define a multipage class in order to manage the multiple pages in the web app
class MultiPage:
    # The multipage framework 
    def __init__(self) -> None:
        # list to store all the applications
        self.pages = []

    def add_page(self, title, func) -> None:
        # Class method to add multiply pages to the web app
        self.pages.append({
            "title": title,
            "function":  func})
    
    def run(self):
        # Define the sidebar navigation
        st.sidebar.markdown('# 🧭 Navigation')
        
        page = st.sidebar.radio(label='Go to', options=self.pages, format_func=lambda x: x['title'])
        st.sidebar.markdown(' *** ')

        # Run the app function
        page['function']()

