# Imports
import re
import pandas as pd
import numpy as np
import datetime
from collections import Counter
from kiva_api import get_params
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import datetime as dt
import warnings
import string
import json
import streamlit as st
nltk.download('stopwords')

"""
This file takes the input data from the API call and transforms it to the required form to be evaluated by the LightGBM model
"""
def text_feature_engineering(df):
    stop_words = list(set(stopwords.words('english')))
    warnings.filterwarnings('ignore')
    punctuation = string.punctuation
    
    # Get the character length of the three text features
    df['LOAN_NAME_char_count'] = df['LOAN_NAME'].apply(len)
    df['DESCRIPTION_char_count'] = df['DESCRIPTION'].apply(len)
    df['LOAN_USE_char_count'] = df['LOAN_USE'].apply(len)

    # Calculate the word count, word density and the punctuation count of the DESCRIPTION feature
    df['DESCRIPTION_word_count'] = df['DESCRIPTION'].apply(lambda x: len(x.split()))
    df['DESCRIPTION_word_density'] = df['DESCRIPTION_char_count'] / (df['DESCRIPTION_word_count'] + 1)
    df['DESCRIPTION_punctuation_count'] = df['DESCRIPTION'].apply(lambda x: len("".join(_ for _ in x if _ in punctuation))) 

    # Calculate the word count, word density and the punctuation count of the LOAN USE feature
    df['LOAN_USE_word_count'] = df['LOAN_USE'].apply(lambda x: len(x.split()))
    df['LOAN_USE_word_density'] = df['LOAN_USE_char_count'] / (df['LOAN_USE_word_count'] + 1)
    df['LOAN_USE_punctuation_count'] = df['LOAN_USE'].apply(lambda x: len("".join(_ for _ in x if _ in punctuation)))

    df['DESCRIPTION_title_word_count'] = df['DESCRIPTION'].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['DESCRIPTION_upper_case_word_count'] = df['DESCRIPTION'].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['DESCRIPTION_stopword_count'] = df['DESCRIPTION'].apply(lambda x: len([wrd for wrd in x.split() if wrd.lower() in stop_words]))

    df['LOAN_USE_title_word_count'] = df['LOAN_USE'].apply(lambda x: len([wrd for wrd in x.split() if wrd.istitle()]))
    df['LOAN_USE_upper_case_word_count'] = df['LOAN_USE'].apply(lambda x: len([wrd for wrd in x.split() if wrd.isupper()]))
    df['LOAN_USE_stopword_count'] = df['LOAN_USE'].apply(lambda x: len([wrd for wrd in x.split() if wrd.lower() in stop_words]))
    
    return df

def categorical_feature_engineering(df):

    f = open('categorical_dictionary.json',) 
    categorical_dictionary = json.load(f)

    del_keys = ['mean_encode_PARTNER_ID', 'mean_encode_CURRENCY_POLICY', 'mean_encode_CURRENCY_EXCHANGE_COVERAGE_RATE']
    for i in del_keys: # delete the categoical features which I couldn't access using the kiva API
        del categorical_dictionary[i]

    # Transform tags feature to be 1 if its not null
    df['TAGS'] = df['TAGS'].apply(lambda x: '1' if not pd.isnull(x[0]) else 0)

    # Add equivalent categoircal values with different spelling
    categorical_dictionary['mean_encode_REPAYMENT_INTERVAL']['at_end'] = 0.9378733971414414
    categorical_dictionary['mean_encode_REPAYMENT_INTERVAL']['irregularly'] = 0.9345212585993008
    categorical_dictionary['mean_encode_DISTRIBUTION_MODEL']['fieldPartner'] = 0.9554144867605828

    for i in categorical_dictionary:
        df[i] = categorical_dictionary[i][df[i[12:]][0]]
    
    return df

def gender(gender_list):
    gen = gender_list.split(", ")
    if len(gen) == 1:
        return gen[0]
    c = Counter(gen)
    if c['female'] > c['male']:
        return 'female group'
    elif c['male'] > c['female']:
        return 'male group'
    else:
        return 'mixed group'

@st.cache
def preprocessing(loan_id_input):

    params_dict = get_params(loan_id_input) # Get the params using kiva API
    df = pd.DataFrame.from_dict(params_dict, orient='columns') # Turn params dict into pandas dataframe

    df['POSTED_TIME'] = pd.to_datetime(df['POSTED_TIME'], format='%Y-%m-%dT%H:%M:%SZ') # convert the posted time from string into pandas datetime
    duration = datetime.datetime.now() - df['POSTED_TIME'][0].to_pydatetime() # define the duration, in days, that the loan request has been on the page
    df['LIVE_TIME'] = duration.days
    df['LOAN_PROGRESS_SCORE'] = float(df['NUM_LENDERS_TOTAL'][0]) / ((float(df['LIVE_TIME'][0]+1))*(float(df['LOAN_AMOUNT'][0]))) # Calculate loan progress score

    #df['BORROWER_GENDERS'] = df['BORROWER_GENDERS'].apply(lambda x: gender(x)) # process the borrowers gender feature

    text_feature_engineering(df) # perform text feature engineering
    categorical_feature_engineering(df) # perform categorical feature engineering

    df['LOAN_AMOUNT'] = float(df['LOAN_AMOUNT'][0]) # Transform loan amount form string to float

    df = df.rename(columns = lambda x:re.sub('[_]+', '', x)) # Rename the columns to match the column names in the model

    # Select only the columns needed for the model in the same specific order 
    X_user = df[['meanencodeACTIVITYNAME', 'meanencodeSECTORNAME',
        'meanencodeCOUNTRYNAME', 'meanencodeCURRENCY',
        'meanencodeBORROWERGENDERS', 'meanencodeREPAYMENTINTERVAL',
        'meanencodeORIGINALLANGUAGE', 'meanencodeDISTRIBUTIONMODEL',
        'meanencodeTAGS', 'LENDERTERM', 'LOANAMOUNT', 'LOANPROGRESSSCORE',
        'LOANNAMEcharcount', 'DESCRIPTIONcharcount', 'LOANUSEcharcount',
        'DESCRIPTIONwordcount', 'DESCRIPTIONworddensity',
        'DESCRIPTIONpunctuationcount', 'LOANUSEwordcount', 'LOANUSEworddensity',
        'LOANUSEpunctuationcount', 'DESCRIPTIONtitlewordcount',
        'DESCRIPTIONuppercasewordcount', 'DESCRIPTIONstopwordcount',
        'LOANUSEtitlewordcount', 'LOANUSEuppercasewordcount',
        'LOANUSEstopwordcount']]

    return X_user






























# Define function that takes strings and converts to datetime 
def str_to_datetime(string):
    if type(string) == str:
        return datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f +0000')
    else:
        pass

# Define function that returns the loan funding duration on the site 
def time_delta(posted, raised, ended, status):
    if status =='funded':
        duration = raised - posted
        return abs(duration.days)
    else: 
        duration = ended - posted
        return abs(duration.days)



    
