# Imports
import streamlit as st
import kiva_api
import preprocessing
import time
import numpy as np
from PIL import Image
import lightgbm as lgb

#st.latex(r''' e^{i\pi} + 1 = 0''')

st.set_page_config(layout="wide")

# Declare a form and call methods directly on the returned object


b1, b2 = st.columns((2,1))

with b1:
    # Page title and information for user
    st.markdown(''' # 📗 KIVA Loan Funding Predictor ''')
    st.markdown('''
    > Please input your [*Kiva*](https://www.kiva.org/lend/filter?sortBy=loanAmountDesc) Loan ID to analyse your loan application.  
    > This machine learning model has been trained on *~2,000,000* past Kiva loan requests.  
    > The biggest contributing factors towards the models loan outcome prediction will be shown.
                    ''')


with b2:
    with st.form('Form1'):
        loan_id_input = st.text_input(label='Enter Active Loan ID')
        submit_button = st.form_submit_button(label='🚀 Get Predictions')

if loan_id_input != "":
    st.empty()
    try:
        params = kiva_api.get_params(loan_id_input)
        X_user = preprocessing.preprocessing(loan_id_input) # Get user information and preprocess it
        bst = lgb.Booster(model_file='lgb.txt') # Load LightGBM Model
        prediction = bst.predict(X_user) # predict the outcome of the loan request
        if prediction[0] > 0.975:
            st.balloons()
        #if prediction[0] > 0.8:
        #   st.markdown("<font color=‘blue’>THIS TEXT WILL BE RED</font>", unsafe_allow_html=True)
        st.markdown(f'''
        ***
        > ## Model Prediction: **{np.round(100*prediction[0], decimals=2)}%** chance of funding
        > #### Welcome {params['LOAN_NAME'][0]}
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

st.sidebar.markdown('# 🧭 Navigation')
st.sidebar.radio('Go to', ['🏠 Home','📝 Project Description', '🔬 Model Explainability', '🧑 About'])


import cv2
import numpy as np
import streamlit as st

#uploaded_file = st.file_uploader("C:\\Users\\Windows\\Documents\\PYTHON\\SHAP_summary_plot.png", type="png")
d = """
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")
    """
#summary_plot = Image.open('C:\\Users\\Windows\\Documents\\PYTHON\\SHAP_summary_plot.png')
##st.image(summary_plot, caption='SHAP summary plot')

c = """
with st.form(key='Form2'):
    c4, c5, c6 = st.beta_columns((1,1,1))
    c4.slider(label = 'Num Lenders 1', min_value=0, max_value=10)
    c4.text_input('Loan Name')
    c5.slider(label = 'Num Lenders 3 ', min_value=0, max_value=10)
    c5.slider(label = 'Num Lenders 4', min_value=0, max_value=10)
    c5.slider(label = 'Num Lenders 5', min_value=0, max_value=10)
    c6.slider(label = 'Num Lenders 6', min_value=0, max_value=10)
    c6.slider(label = 'Num Lenders 7', min_value=0, max_value=10)
    c6.slider(label = 'Num Lenders 8', min_value=0, max_value=10)
    c4.slider(label = 'Num Lenders 9', min_value=0, max_value=10)
    submitted = st.form_submit_button('Submit')
"""    
    