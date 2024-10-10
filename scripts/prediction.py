import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, OneHotEncoder


def encoder(method, dataframe, columns_featured):
    if method == 'labelEncoder':      
        df_lbl = dataframe.copy()
        for col in columns_featured:
            label = LabelEncoder()
            label.fit(list(dataframe[col].values))
            df_lbl[col] = label.transform(df_lbl[col].values)
        return df_lbl, label 
    
    elif method == 'oneHotEncoder':
        df_lbl = dataframe.copy()
        encoder = OneHotEncoder(sparse_output=False, drop='first')
        
         # Fit the encoder on the specified columns (ensure 2D input)
        encoder.fit(df_lbl[columns_featured])  # Fit on the entire DataFrame subset

        # Transform the DataFrame
        encoded_array = encoder.transform(df_lbl[columns_featured])

        # Create a DataFrame with the encoded features
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out(columns_featured))

        # Drop the original columns and concatenate the new encoded columns
        df_lbl = df_lbl.drop(columns=columns_featured).reset_index(drop=True)
        df_lbl = pd.concat([df_lbl, encoded_df], axis=1)

        # Save the fitted encoder
        joblib.dump(encoder, 'one_hot_encoder.pkl')
        
        return df_lbl 

def scaler(method, data, columns_scaler):    
    if method == 'standardScaler':        
        Standard = StandardScaler()
        df_standard = data.copy()
        df_standard[columns_scaler] = Standard.fit_transform(df_standard[columns_scaler])  

        joblib.dump(Standard, 'standard_scalar.pkl')

        return df_standard
        
    elif method == 'minMaxScaler':        
        MinMax = MinMaxScaler()
        df_minmax = data.copy()
        df_minmax[columns_scaler] = MinMax.fit_transform(df_minmax[columns_scaler])        
        return df_minmax
    
    elif method == 'npLog':        
        df_nplog = data.copy()
        df_nplog[columns_scaler] = np.log(df_nplog[columns_scaler])        
        return df_nplog
    
    return data

def evaluate_model(model, X_test, y_test):
    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mae, mse, r2, y_pred