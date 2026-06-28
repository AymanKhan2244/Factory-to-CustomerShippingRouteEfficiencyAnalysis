import pandas as pd
from pathlib import Path




def load_data():
    df = pd.read_csv("data/Cleaned_shipping_data.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    return df



