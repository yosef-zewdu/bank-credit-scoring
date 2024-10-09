# Bati Bank Credit Scoring Model

This repository contains the code and documentation for developing a credit scoring model for Bati Bank. The goal is to enable a buy-now-pay-later service in partnership with an eCommerce company.

## Business Objective

Bati Bank aims to enhance its financial services by partnering with an eCommerce company to offer a buy-now-pay-later service. The key objective is to build a robust Credit Scoring Model that evaluates the creditworthiness of potential borrowers. By leveraging customer data, the model will:

- Classify Risk: Identify users as high risk or low risk.
- Predict Default Probability: Estimate the likelihood of default for new customers.
- Assign Credit Scores: Convert risk probabilities into standardized credit scores.
- Recommend Loan Terms: Predict optimal loan amounts and durations to minimize risk and optimize customer satisfaction.

### Main Tasks

1. Exploaratoty Data Analysis
2. Feature Engineering
3. Model Training
4. Model Serving API Call

## Folder Structure

- `notebooks/`: Jupyter notebooks for all the analysis and modelling.
- `scripts/`: Python scripts for the notebook files .
- `api/` : Model serving API call 

## api Folder/

```
    `app.py`                        : script for creating api to serve the model 
    `feature_eng.py`                : script for customer Feature Engineering 
    `model_20241008_214241.pkl`     : model saved from our modeling   
    `one_hot_encoder.pkl`           : encoder used for categorical features 
    `standard_scalar.pkl`           : scaler used for numerical features

```

## Setup Instructions

1. Clone the repository.
2. Set up the virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.