'''
Get all the loan information by calling the API with the Loan ID.
'''

#Imports
import requests
import json
import pandas as pd

def get_params(loan_id_input):

    # Define GraphQL Query 
    graphql_query = f"""query{{
                    lend {{
                        loans(filters: {{loanIds: {loan_id_input}}}, sortBy: newest) {{
                        values {{
                            name
                            description
                            use
                            originalLanguage {{name}}
                            activity {{name}}
                            sector {{name}}
                            geocode {{country {{name}}}}
                            terms {{currency}}
                            lenderRepaymentTerm
                            gender
                            repaymentInterval
                            loanAmount
                            distributionModel
                            image {{url}}
                            fundraisingDate
                            lenders {{totalCount}}
                            tags
                        }}}}}}}}"""
    base_url = 'https://api.kivaws.org/graphql?query=' # Kiva GraphQL API Base URL   
    API_query = base_url+graphql_query # Construct API Query             
    r = requests.get(API_query) # Send a request to API
    
    # Initialise and populate parameters dictionary
    params = {} 
    params['LOAN_NAME'] = [r.json()["data"]["lend"]["loans"]["values"][0]['name']]
    params['DESCRIPTION'] = [r.json()["data"]["lend"]["loans"]["values"][0]['description']]
    params['LOAN_USE'] = [r.json()["data"]["lend"]["loans"]["values"][0]['use']]
    params['ORIGINAL_LANGUAGE'] = [r.json()["data"]["lend"]["loans"]["values"][0]["originalLanguage"]["name"]]
    params['ACTIVITY_NAME'] = [r.json()["data"]["lend"]["loans"]["values"][0]["activity"]["name"]]
    params['SECTOR_NAME'] = [r.json()["data"]["lend"]["loans"]["values"][0]["sector"]["name"]]
    params['COUNTRY_NAME'] = [r.json()["data"]["lend"]["loans"]["values"][0]["geocode"]["country"]["name"]]
    #params['CURRENCY_POLICY']
    params['CURRENCY'] = [r.json()["data"]["lend"]["loans"]["values"][0]["terms"]["currency"]]
    params['LENDER_TERM'] = [r.json()["data"]["lend"]["loans"]["values"][0]["lenderRepaymentTerm"]]
    #params['NUM_JOURNAL_ENTRIES']
    #params['NUM_BULK_ENTRIES']
    params['BORROWER_GENDERS'] = [r.json()["data"]["lend"]["loans"]["values"][0]["gender"]]
    #params['BORROWER_PICTURED']
    params['REPAYMENT_INTERVAL'] = [r.json()["data"]["lend"]["loans"]["values"][0]['repaymentInterval']]
    params['LOAN_AMOUNT'] = [r.json()["data"]["lend"]["loans"]["values"][0]['loanAmount']]
    params['DISTRIBUTION_MODEL'] = [r.json()["data"]["lend"]["loans"]["values"][0]['distributionModel']]
    params['IMAGE_URL'] = r.json()["data"]["lend"]["loans"]["values"][0]['image']['url']
    params['POSTED_TIME'] = [r.json()["data"]["lend"]["loans"]["values"][0]["fundraisingDate"]]
    params['NUM_LENDERS_TOTAL'] = [r.json()["data"]["lend"]["loans"]["values"][0]["lenders"]["totalCount"]]
    params['TAGS'] = [r.json()["data"]["lend"]["loans"]["values"][0]["tags"]]

    return params

def get_params_df(params):
    return pd.DataFrame(params, index=[f'{params["LOAN_NAME"]}'])