# Imports 
import streamlit as st 

def app():
    st.markdown('''
        ## Hola Mama''')
    
    # Define columns
    c1, c2 = st.columns((1,1))

    with c1:
        st.markdown(''' Write an explaination of SHAP ''')

    with c2:
        with st.expander('Video Explaining Shapley Values'):
            st.video('https://youtu.be/VB9uV-x0gtg?t=8')