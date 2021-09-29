# Imports
import streamlit as st
import kiva_api
import preprocessing
import time
import numpy as np
from PIL import Image
import lightgbm as lgb

def app():
    st.markdown(''' # 📗 KIVA Loan Funding Predictor ''')
    b1, b2, b3, b4 = st.columns((1, 10, 1, 6)) # Divide the upper section of the page into two columns
    with b2:
        # Page title and information for user
        
        st.markdown('''
            > ### About the Project
            > This site is a Loan Predictor. It is intended to accuratly predict the Loan Outcome of active loans on the Kiva Crowdfunding Site.     
            > The machine learning model used has been trained on *~2,000,000* past Kiva loan requests.
            > More infomation is available on the project description page.
            ''')
        #> The biggest contributing factors towards the outcome prediction of the model will be shown.
        st.markdown('''
        > ### How to Use
        > 1. Find a loan that you would like to predict its outcome on the [**Kiva**](https://www.kiva.org/lend/filter?sortBy=loanAmountDesc) Crowdfunding Site.
        > 2. Input your [*Kiva*](https://www.kiva.org/lend/filter?sortBy=loanAmountDesc) Loan URL in the form to the top right to predict the Loan outcome.  
          
                       ''')
    with b4:
        st.markdown('''
        ### Input URL for Prediction 📊
        ''')
        # Declare a form and call methods directly on the returned object
        with st.form('Form1'):
            loan_id_input = st.text_input(label='Enter Active Loan URL or Loan ID (try 2243523)')
            submit_button = st.form_submit_button(label='🚀 Get Predictions')

    if loan_id_input != "":

        try:
            loan_id_input = loan_id_input.split('/')[-1]
            params = kiva_api.get_params(loan_id_input)
            X_user = preprocessing.preprocessing(params) # Get user information and preprocess it
            bst = lgb.Booster(model_file='lgb.txt') # Load LightGBM Model
            prediction = bst.predict(X_user) # predict the outcome of the loan request
            if prediction[0] > 0.975:
                st.balloons()
            

            st.markdown(f'''
            *** ''')

            st.markdown(f'''
            ## Model Prediction:''')

            st.markdown(f'''
            > ## **{np.round(100*prediction[0], decimals=2)}%** Chance of Funding! ''')

            st.markdown(f'''
            ### Loan Name: {params['LOAN_NAME'][0]}''')

            st.markdown('#### Loan Description')
            st.markdown(f'''
            {params['DESCRIPTION'][0]}
            ''')

            s = """
            params = kiva_api.get_params(loan_id_input) # Call get_params function in kiva_api file
            image = st.image(f"{params['IMAGE_URL']}")
            st.markdown(f"### Loan Use \n {params['LOAN_USE'][0]}")
            st.markdown(f"### {params['LOAN_NAME'][0]}")
            st.write(params['DESCRIPTION'][0])
            df = kiva_api.get_params_df(params)
            st.table(df[['ORIGINAL_LANGUAGE','ACTIVITY_NAME','SECTOR_NAME','COUNTRY_NAME','LENDER_TERM','BORROWER_GENDER','REPAYMENT_INTERVAL','LOAN_AMOUNT','DISTRIBUTION_MODEL']])
            """
        except IndexError: 
            st.markdown('### Oops! That was an invalid Loan ID. Enter an active Loan ID')

    
    
