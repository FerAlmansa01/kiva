# Imports 
import streamlit as st
from PIL import Image
import os 
import base64

def app():
    st.markdown('''
        # Oxford Man Institute for Quantative Finance
    ''')
    c1, c2, c3, c4 = st.columns((2,20,3,8)) # Define the page columns
    with c2: 
        c2.markdown('''
            ### Internship Project Supervisior - Dr Stefan Zohren 

            > #### Project Aims
            > - This project aims to develop a kiva loan funding *prediction model* using Machine Learning methods
            > and applying *explainable AI techniques* to comprehend the model's prediction.   
            > - By extracting the key predictors of a loan's success on kiva, 
            > and suggesting modifications to their loan requests,
            > I hope to improve the chances of sucessful loan funding for a borrower. 
        ''')
    with c4:
        image = Image.open('oxford-man.png')
        c4.image(image)
        c4.markdown('''[Oxford Man Institute](https://www.oxford-man.ox.ac.uk/)''')

    with st.expander(label = 'Data Preprocessing'):
        st.markdown('''   
            > #### Data Preprocessing
            > Raw data was downloaded from the loans dataset from the [kiva data snapshots](https://www.kiva.org/build/data-snapshots) page.   
            > I then selected relevant features from the dataset and 
            > [cleaned the data](https://towardsdatascience.com/the-ultimate-guide-to-data-cleaning-3969843991d4). 
            > This process improves the quality of the data. 
            > Ultimatley, better data leads to a better model, which in turn, leads to superior predictions.
            ''')
        
    with st.expander(label= 'Feature Engineering'):
        st.markdown('''
            > #### Categorical Feature Engineering
            > There are many ways of dealing with categorical features.  

            > *One Hot Encoding*, (mapping every category to a vector containing 1 and 0, in order to denote the presence or absence of a feature) is very commonly used. 
            > However, tree-based models suffer with one hot encoding due to the additional sparsity introduced into the dataset. (A feature with N categories will introduce N columns to the dataset, 
            > especially problematic when the feature has high cardinality). e.g the feature "COUNTRY_NAME" in the kiva dataset has high cardinality, containing over 100 countries. 
            > More information can be found [here](https://towardsdatascience.com/one-hot-encoding-is-making-your-tree-based-ensembles-worse-heres-why-d64b282b5769).  
            
            > *Target Encoding*, (replacing a categorical value with the mean of the target variable for that categorical value) was the method I choose.
            > This allowed me to encode the features without increasing the size of the dataset.
            > [Catboost](https://arxiv.org/pdf/1706.09516.pdf),
            > a recently published gradient boosting toolkit, also uses a target-based categorical encoder.
            ''')
        st.markdown('''
            > #### Textual Feature Engineering
            > With some prelimiary model traning I foundout that the loan description was an important factor in a successful loan request.
            > To extract numerical information from a textual feature I added the following numerical features.   
            > *Character count, Word count, Word density, Punctuation count, Title word count, Upper case word count, Stopword count* 
            ''')

    with st.expander(label = 'Model Selection and Hyperparmeter Tuning'):
        st.markdown('''
            > #### Model Selection
            > After training multiple models such as Logistic Regression, Decision Tree Classifier, Random Forest Classifier and LightGBM.
            > I selected LightGBM as this model had the best performance. I evaulated the performance of these models on 
            > [ROC Curves and Precision-Recall Curves](https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-imbalanced-classification/).    
            > [LightGBM](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/11/lightgbm.pdf) is an 
            > implementation of the popular Gradient Boosting Decision Tree (GBDT) alogorithm. The main difference between
            > LightGBM and XGBoost (the most popular GBDT implementation) is that LightGBM applies *leaf-wise* tree growth
            > whereas XGBoost applies *level-wise* growth. Since leaf-wise growth is mostly faster than level-wise,
            > LightGBM has been shown to offer a near x10 reduction in training time. More information can be found 
            > [here](https://sefiks.com/2020/05/13/xgboost-vs-lightgbm/).
            ''')        
        st.markdown('''
            > #### Hyperparameter Tuning
            > Hyperparameter optimisation is essential for achieving optimal model performance. Hyperparamters differ from
            > regular parameters as they are not learnt automatically by the model. They are set by the user to guide the 
            > model's learning process.    
            > I used a [Grid Search](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/) 
            > technique to tune the hyperparameters. It works by defining a grid of hyperparamter values and evaluating the model's
            > performance at every location inside the grid. After the whole grid has been searched you use the hyperparameter
            > configuration that achieved the best results for your production model.
            ''')
    
    

        

    