# Red Wine Quality Project


## About this project

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). [source](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)


## Data Source

https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009


## Goal

- Create a model that can effectively predict the general quality of a wine (good or bad)


## Data Dictionary

alcohol - The percent of alcohol within the wine.

chlorides - The amount of salt in the wine.

citric acid - The citric acid level of the wine. Low levels can add 'freshness' and flavor.

density - The density of the wine. 

fixed acidity - The fixed acidity level of the wine.

free sulfur dioxide - The free sulfur dioxide level present within the wine. 

is_good_wine - Boolean column that reflects if a wine is bad (quality 1 - 5) or "good" (quality 6 - 10). (0 == Bad, 1 == Good)

pH - Describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic).

quality - Quality of wine based on sensory data, score between 0 and 10.

residual sugar - The amount of sugar remaining after fermentation has concluded.

sulphates - The sulphate level present within the wine. 

total sulfur dioxide - The total sulfur dioxide level present within the wine. 

volatile acidity - The volatile acidity level of the wine. Too high of levels can lead to an unpleasant, vinegar taste.


## Project Plan

- Acquire
    - Download data as csv from Kaggle
    - Import data into Jupyter Notebook via pandas and save as data frame

- Prepare
    - Prepare data as needed for exploration and modeling including but not limited to
        - Dropping unneeded columns
        - Converting all string column values to lower case
        - Updating column names for readability and to better reflect values
        - Converting column names to all lower case
        - Change columnn name spaces to underscores
        - Update data types as needed to facilitate expected operations
        - Handle null values via imputing or dropping
        - Convert dates (if any) to datetime format if appropriate for exepected operations
        - Split categorical column values into boolean columns
        - Scaling data as needed
        - Splitting data into train, validate, and test sets

- Exploration
    - Identify variables with weak-moderate to very strong correlations to quality
    - Explore notable variables using methods that include plots and hypothesis tests
    - Note variables that are strong candidates for use in modeling to predict wine quality class (good or bad wine)
    
- Modeling
    - Identify metric(s) to judge model performance with (accuracy, precision, recall, etc.)
    - Create baseline model that always predicts dominant wine quality class
    - Create and train alternate models using train set
    - Identify best models from train phase and document performances
    - Use best models from train phase on validate set and attempt to tune hyperparameters
    - Identify best model from validate phase and document performance
    - Use best model from validate phase on test set and document performance

Conclusion
    - Summarize findings from project


## How to Reproduce

- Download the data (from [here](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009) into your working directory.

- Download and install the acquire.py file in your working directory
    - Optionally, you can download and install the prepare.py file into your working directory if you'd prefer to prepare the data with a single function instead of running each cell within the prepare section individually 
    - Detailed instructions can be found beneath header for "prepare" section of notebook

- Run the jupyter notebook


## Conclusion

- Among all of the variables present in the data, some were found to correlate with varying degress of magnitude. The list below summarizes the more notable features (ie. features with correlation values greater than .10).


- Weak-to-Moderate negative correlation with good wine
  - Chlorides (-.14)
  - Total_sulfure_dioxide (-.24)
  - Density (-.19)


- Weak-to-Moderate positive correlation with good wine
  - Citric Acid (.15)
  - Sulphates (.22)


- Moderate-to-Strong negative correlation with good wine
  - Volatile_acidity (-.33)


- Strong positive correlation with good wine
  - Alcohol (.46)

- Further exploration via plots and hypothesis reinforced the finding that these variables had notable relationships with wine quality (both positive and negative)


- I developed a model that was able to predict the classes of various wines (good or bad) with a high degree of succes. It's specs and performance metrics are listed below.

    - Model 2c - Random Forest - Top 7 Features from RFE
        - Features: 
            - volatile_acidity_s
            - alcohol_s
            - total_sulfur_dioxide_s
            - sulphates_s
            - density_s
            - chlorides_s
            - ph_s
        - Accuracy (Train): 1 (Perfect)
        - F1-score (Train): 1 (Perfect)
        - Accuracy (Validate): .80
        - F1-score (Validate): .80   
        - Accuracy (Test): .80
        - F1-score (Test): .78
