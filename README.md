# Bati Bank Credit Scoring Model

This repository contains the code and documentation for developing a credit scoring model for Bati Bank. The goal is to enable a buy-now-pay-later service in partnership with an eCommerce company.

## Business Objective

Bati Bank aims to enhance its financial services by partnering with an eCommerce company to offer a buy-now-pay-later service. The key objective is to build a robust Credit Scoring Model that evaluates the creditworthiness of potential borrowers. By leveraging customer data, the model will:

- Classify Risk: Identify users as high risk or low risk.
- Predict Default Probability: Estimate the likelihood of default for new customers.
- Assign Credit Scores: Convert risk probabilities into standardized credit scores.
- Recommend Loan Terms: Predict optimal loan amounts and durations to minimize risk and optimize customer satisfaction.

## Project Overview

1. **Define Proxy Variable**: Identify a binary variable to classify users as high risk (bad) or low risk (good).
2. **Feature Selection**: Select features that are good predictors of default.
3. **Risk Probability Model**: Develop a model to predict the probability of default.
4. **Credit Score Model**: Convert risk probabilities into a credit score.
5. **Optimal Loan Prediction**: Predict the optimal loan amount and duration.

## Project Structure

```plaintext

bank-credit-scoring/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml               # GitHub Actions
├── src/
│   └── __init__.py
├── notebooks/
|   ├── eda.ipynb                       # Jupyter notebook for data cleaning and processing 
|   ├── feature_eng.ipynb                      # Jupyter notebook for feature engineering
│   └── README.md                       # Description of notebooks directory 
├── tests/
│   └── __init__.py
├── scripts/
|    ├── __init__.py
│    ├── eda.py                          # Script data processing, cleaning 
|    ├── feature_eng.py                  # Script feature engineering
│    └── README.md                       # Description of scripts directory
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── LICENSE                 # License information
└── .gitignore              # Files and directories to ignore in Git  
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yosef-zewdu/bank-credit-scoring.git
   cd bank-credit-scoring


2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv\Scripts\activate  # On Linux, use `venv/bin/activate`
   

3. Install the required packages:
   ```bash
   pip install -r requirements.txt