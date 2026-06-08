# utils/data_loader.py

import pandas as pd

def load_data():
    df = pd.read_csv("data/cleaned_shipping_data.csv")

    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    return df