import pandas as pd

def get_wines():
    """ 
    No arguments needed. Run function to acquire wine data from local csv file 'winequality-red.csv'.
    """
    # acquiring data from local csv 
    wines = pd.read_csv('winequality-red.csv')

    # returning df
    return wines
