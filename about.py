# Imports
import streamlit as st
from PIL import Image

def app():
    b1, b2 = st.columns((15,1))
    c1, c2, c3 = st.columns((2,2,1))
    with b1:
        st.markdown('''
            # ⚙️ Engineering Student 🎓 & Developer 🖥️
            ''')
        st.markdown(''' *** ''')
    

    with c1:
        st.markdown(''' 
            Hello, my name is Fernando Almansa, and I'm a 3rd Year Engineering Science student at the University of Oxford. When I'm not busy being a student, I enjoy working on Data Science and Software Engineering projects.

            #### Check out my 🔗 [LinkedIn](https://www.linkedin.com/in/fernando-almansa-1ba085198/)
    ''')
    with c2:
        st.markdown(''' 
            ### Third Year Modules
            - Information Theory 
            - Software Engineering
            - Control Theory
            - Electronic Devicies
            - Circuits and Communications

            ### Third Year Group Project
            - Designing Intelligent Musical Desgin Technology
        ''')
    with c3:
        image = Image.open('fernando-almansa.jpg')
        c3.image(image)

        
    

