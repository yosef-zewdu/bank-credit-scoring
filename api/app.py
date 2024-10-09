
# 1. Library imports
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import logging
import joblib 

# Initialize logging
logging.basicConfig(level=logging.INFO)


# Define a Pydantic model for input data
class credit(BaseModel):
    ProviderId: object
    ProductId:  object
    ProductCategory:object 
    ChannelId:  object
    PricingStrategy: object
    Amount: float
    TransactionYear: int
    TransactionMonth: int
    TransactionDay: int
    TransactionHour: int

# Create the app object
app = FastAPI()
# Load your trained model, encoder, and scaler
model_filename = 'model_20241008_214241.pkl'
model = joblib.load(model_filename)
encoder = joblib.load('one_hot_encoder.pkl')
scaler = joblib.load('standard_scalar.pkl')


# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Route with a single parameter, returns the parameter within a message
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome! Calculate your credit score': f'{name}'}


# Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Credit risk with the confidence
@app.post('/predict')
def predict_creditrisk(data:credit):
    try:
        print('credit risk')   
        input_data = pd.DataFrame([data.dict()])
        # Encode categorical variables
        categorical_feature = ['ProviderId', 'ProductId', 'ProductCategory', 'ChannelId','PricingStrategy']
        num_cat = [ 'Amount', 'TransactionYear', 'TransactionMonth',
        'TransactionDay', 'TransactionHour']
        encoded_data = encoder.transform(input_data[categorical_feature])
        # Scale the numerical features
        scaled_data = scaler.transform(input_data[num_cat])
        # Combine processed features
        processed_data = np.hstack((encoded_data, scaled_data))

        # Make predictions
        predictions = model.predict(processed_data)

        return {"prediction": predictions[0]}
     
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload