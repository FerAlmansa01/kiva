# Imports 
import streamlit as st 
from PIL import Image

def app():
    st.markdown('''
        # 🔭 SHAP Values (SHapley Additive exPlanations)

        > *SHAP was used in this project in order to interperate the results the model, trained on the Kiva data set, produced.*
        ''')
    
    # Define columns
    c1, c2, c3, c4, c5 = st.columns((2, 10, 2, 6, 2))
    with c2:
        st.markdown('''
            > ### What is SHAP?
            > - SHAP is a model interpretability method that explains the output of *any* machine learning model.      
            - SHAP uses a game theoretic approach based on [Shapley Values](https://en.wikipedia.org/wiki/Shapley_value).     
            - SHAP is model-agnostic, meaning you can apply to explain anything from a Neural Network to a Random Forest model.
            ''')
        st.markdown('')
        st.markdown('''
            > ### How They Work
            > SHAP values interpret the impact of having a certain value for a given feature in comparison to the prediction we'd make if that feature took some baseline value.''')
    
    
    with c4:
        
        st.markdown('''
            > ### Resource Links 🔗
            > - #### [SHAP Academic Paper](https://arxiv.org/pdf/1705.07874.pdf)
            > - #### [Interpretable ML Book - SHAP Chapter](https://christophm.github.io/interpretable-ml-book/shap.html)
            > - #### [Kaggle's Introduction to SHAP](https://www.kaggle.com/dansbecker/shap-values)
            > - #### [Github Repository of the Code Implementation of SHAP](https://github.com/slundberg/shap)
            > - #### [Explanitory Video](#video-explaination)
        ''')
        # st.markdown('''
        #     > ### Video Explaination 🎥
        # ''')
        # st.markdown('<li><strong><a href="#video-explaination">Video</a></strong></li>', unsafe_allow_html=True)

    d1, d2, d3 = st.columns((2,5,2))
    with d2:
        st.markdown('''
        ## **SHAP Summary plot** ''')
        @st.cache
        def load_image(file_path):
            image = Image.open(file_path)
            return image
        st.image(load_image('SHAP_summary_plot_hd-min.png'))
        with st.expander('Feature value explaination'):
            st.markdown('''
            All the categorical variables are mean encoded, so a high feature value (red on the SHAP summary plot) corresponds to a high mean encoded score of a specific feature value.

            The Loan Progress Score is a calculation of the rate of loan funding normalized by the loan amount and the proportion of time elapsed in relation to the loan's fundraising deadline date. This approach assumes that loans are funded in a linear fashion which is not the case. However, for the purpose of this model, this proved to be a fair approximation. 
            ''') 

        #st.markdown('''
        #### Plot Explaination

        #''')

        st.markdown('''
            
        ***
       
        ''')
        st.markdown('> ### Video Explaination 🎥')
        with st.expander('Video Explaining Shapley Values'):
                st.video('https://youtu.be/VB9uV-x0gtg?t=8')
        

    