
import pandas as pd
import numpy as np
import lightgbm as lgb

# Core Feature: Weighted Average Price (WAP)
def calc_wap(df):
    wap = (df['bid_price1'] * df['ask_size1'] + df['ask_price1'] * df['bid_size1']) / (df['bid_size1'] + df['ask_size1'])
    return wap

# Log Returns & Realized Volatility calculation
def log_return(series):
    return np.log(series).diff().fillna(0)

def realized_volatility(series):
    return np.sqrt(np.sum(series**2))

# Model Training Parameters
params = {
    'objective': 'rmse',
    'learning_rate': 0.01,
    'boosting_type': 'gbdt',
    'metric': 'rmse',
    'n_jobs': -1
}

print("QuantRisk-Engine logic initialized.")
