import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split


def prep_wines(df):
    
    # replacing spaces with underscores in column names
    df.columns = df.columns.str.replace(' ', '_')

    # lowercasing all column names
    df.columns = df.columns.str.lower()

    # creating boolean columns to reflect good and bad wines
    df['is_good_wine']= np.where(df.quality >= 6, 1, 0)

    # adding column strictly for use in plotting
    # text column is useful for plotting so I don't have to customize labels
    df['good_or_bad']= np.where(df.quality >= 6, 'Good', 'Bad')

    # dropping 'quality' column since I have a binned version
    df.drop(columns = 'quality', inplace = True)

    # splitting data
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    # creating list of DFs
    df_list = [train, validate, test]
    # creating empty list to hold names of columns to scale
    cols_to_scale_l = []
    # creating empty list to hold names of scaled columns
    scaled_cols_l = []

    # iterating through each column to be scaled of each df
    for dataframe in df_list:
        for col in dataframe:
            if col != 'is_good_wine' and col != 'good_or_bad':
                # making temporary variable that holds current column name concatenated with '_s' at the end
                scaled_col_name = col + '_s'
                # appending col name to list
                cols_to_scale_l.append(col)
                # appending concatenated col name to list
                scaled_cols_l.append(scaled_col_name)
                # adding column with concatenated col name to current df
                dataframe[scaled_col_name] = 0
                
    # creating scaler object
    scaler = sklearn.preprocessing.MinMaxScaler()

    # fitting scaler to train column and scaling after
    train[scaled_cols_l] = scaler.fit_transform(train[cols_to_scale_l])

    # scaling data in validate and test dataframes
    validate[scaled_cols_l] = scaler.transform(validate[cols_to_scale_l])
    test[scaled_cols_l] = scaler.transform(test[cols_to_scale_l])

    # moving 'is_good_wine' and 'good_or_bad' columns to end of each df
    for dataframe in df_list:
        quality_col = dataframe.pop('is_good_wine')
        good_or_bad_col = dataframe.pop('good_or_bad')
        dataframe['good_or_bad'], dataframe['is_good_wine'] = good_or_bad_col, quality_col

    # returning DFs
    return train, validate, test