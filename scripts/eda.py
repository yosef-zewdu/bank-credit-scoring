import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import logging



# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def load_data():
    '''
        Load training and variable definition datasets
    '''
    logging.info("Loading Data ...")
    df = pd.read_csv('../data/data.csv')
    df_def = pd.read_csv('../data/Xente_Variable_Definitions.csv')
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None) 
    logging.info("Loading Data Finshed")
    return df, df_def

# Data Overview
def data_overview(df):
    '''
        Data Overview

        Inputs: Dataframe

        Outputs: Data Overivew 
    '''
    logging.info('Loading Data Overivew')

    print(f"The shape of our Data is {df.shape}")
    print("\nData Overview:")

    # Data Types
    datype  = df.dtypes

    # Check Missing Values
    missing = df.isnull().sum()
    
    # Check number of unique values
    uniq = df.nunique()

    # Create table 
    tabl = pd.concat([datype, missing, uniq], axis=1)

    # Rename the columns
    df_table = tabl.rename(
    columns={0: 'Data Types', 1: 'Number of missing values', 2: 'Unique values'})

    # Sort by unique values
    df_table = df_table.sort_values(by='Unique values', ascending=True)

    return df_table


# Data Summary 
def summary(df):
    '''
        Statistical Summary 
    '''
    logging.info("")
    display(df.describe())
    print('Categorical Summary')
    display(df.describe(include='object'))

# print unique values 
def uniq(df, col):
    '''
        Unique values in each columns 
    '''
    logging.info('Unique Values in each columns\n')

    for i in col:
        print(f'{df[i].nunique()} Unique values of {i} {df[i].unique()}\n')


# plot categorical
def plot_cat(df,col):
    '''
        Plotting Categorical variables
    '''    

    logging.info("Plotting Categorical variables")

    # Set up the plotting environment
    plt.figure(figsize=(18, 16))

    # Loop through each categorical column
    for i, co in enumerate(col):
            plt.subplot(3, 2, i + 1)
            val = df[co].value_counts()
            val.plot(kind='bar', color='skyblue')
            plt.title(co)
            plt.xticks(rotation=45)
            plt.ylabel('Count')

    # Adjust layout and show the plot
    plt.subplots_adjust(hspace=0.5, wspace=0.3)  # Adjust vertical and horizontal spacing
    plt.show()



# plot numerical features
def plot_numerical(df):
    '''
        plotting numerical variables
    '''
    logging.info(" plotting numerical variables")

    # Create subplots
    plt.figure(figsize=(12, 6))

    # Distribution of Amount
    plt.subplot(1, 2, 1)
    sns.histplot(df['Amount'], bins=50, kde=True, color='skyblue')
    plt.title('Amount ')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Distribution of values
    plt.subplot(1, 2, 2)
    sns.histplot(df['Value'], bins=50, kde=True, color='skyblue')
    plt.title('Value')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # Show plots
    plt.tight_layout()
    plt.show()

# Function to detect outliers using IQR and count them
def count_outliers_iqr(df,col):
    '''
        Detecting Outliers using IQR method
    '''
    logging.info("Detecting Outliers using IQR method")

    outlier_counts = {}
    lower_bounds = {}
    upper_bounds = {}

    for column in col:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        # Define bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Count outliers
        outlier_count = df[(df[column] < lower_bound) | (df[column] > upper_bound)].shape[0]
        
        outlier_counts[column] = outlier_count
        lower_bounds[column] = lower_bound
        upper_bounds[column] = upper_bound
    
    return lower_bounds, upper_bounds, outlier_counts


def plot_outliers(df):
    '''
        Plotting outliers using boxplot
    '''
    logging.info("Plotting outliers using boxplot")

    # Detecting Outliers in Value
    plt.figure(figsize=(8,6))
    sns.boxplot(y=df['Value'])
    plt.title('Outliers in Value ')
    plt.show()

    # Detecting Outliers in Amount
    plt.figure(figsize=(8,6))
    sns.boxplot(y=df['Amount'])
    plt.title('Outliers in Amount ')
    plt.show()


def corr(df):
    '''
        Correlation between numerical features
    '''
    logging.info(" Correlation between numerical features")

    # Selecting only numeric variables
    numeric_df = df.select_dtypes(include=['number'])
    numeric_df.drop('CountryCode', axis=1, inplace=True)
    display(numeric_df.corr())



    f, ax = plt.subplots(figsize=(5, 5))
    ax = sns.heatmap(numeric_df.corr(),
                cmap = 'coolwarm',
                annot = True)
