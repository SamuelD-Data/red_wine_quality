import pandas as pd
from sklearn.feature_selection import RFE

def rfe_ranker(df, algo):
    """
    Accepts dataframe and algorithm of choice. 
    Uses Recursive Feature Elimination to rank the given df's features in order of their usefulness in
    predicting logerror with the provided algorithm.
    """

    # fitting algo to features 
    algo.fit(df[['fixed_acidity_s', 'volatile_acidity_s',
       'citric_acid_s', 'residual_sugar_s', 'chlorides_s',
       'free_sulfur_dioxide_s', 'total_sulfur_dioxide_s', 'density_s', 'ph_s',
       'sulphates_s', 'alcohol_s']], df['is_good_wine'])

    # creating recursive feature elimination object and specifying to only rank 1 feature as best
    rfe = RFE(algo, 1)

    # using rfe object to transform features 
    x_rfe = rfe.fit_transform(df[['fixed_acidity_s', 'volatile_acidity_s',
       'citric_acid_s', 'residual_sugar_s', 'chlorides_s',
       'free_sulfur_dioxide_s', 'total_sulfur_dioxide_s', 'density_s', 'ph_s',
       'sulphates_s', 'alcohol_s']], df['is_good_wine'])

    # creating mask of selected feature
    feature_mask = rfe.support_

    # creating train df for rfe object 
    rfe_df = df[['fixed_acidity_s', 'volatile_acidity_s',
       'citric_acid_s', 'residual_sugar_s', 'chlorides_s',
       'free_sulfur_dioxide_s', 'total_sulfur_dioxide_s', 'density_s', 'ph_s',
       'sulphates_s', 'alcohol_s']]

    # creating list of the top features per rfe
    rfe_features = rfe_df.loc[:,feature_mask].columns.tolist()

    # creating ranked list 
    feature_ranks = rfe.ranking_

    # creating list of feature names
    feature_names = rfe_df.columns.tolist()

    # create df that contains all features and their ranks
    rfe_ranks_df = pd.DataFrame({'Feature': feature_names, 'Rank': feature_ranks})
    
    return rfe_ranks_df.sort_values('Rank')