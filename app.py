# Imports 
import streamlit as st
from multipage import MultiPage
import kiva
import about
import project_description
import model_explainability

# Create an instance of the app
app = MultiPage()

# Configure page layout
st.set_page_config(
    page_title='Kiva Loan Prediction & Analysis',
    page_icon='📗',
    initial_sidebar_state='auto',
    layout='wide')

# Add all the pages to the navigation bar
app.add_page('🏠 Home', kiva.app)
app.add_page('📝 Project Description', project_description.app)
app.add_page('🔬 Model Explainability', model_explainability.app)
app.add_page('🧑 About', about.app)

# Run the main app
app.run()

#st.sidebar.radio('Go to', ['🏠 Home','📝 Project Description', '🔬 Model Explainability', '🧑 About'])