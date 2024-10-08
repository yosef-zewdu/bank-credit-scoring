import pandas as pd 




def aggeregatef(df):
    '''
            Aggregating customers transaction count , total and average
    '''
    return df.groupby('CustomerId').agg(

    Transaction_count = ('TransactionId', 'nunique'),
    Total_Transaction = ('Amount', 'sum'),
    Average_Transaction = ('Amount','mean'),
    Transaction_std = ("Amount", 'std')
    
        )
     