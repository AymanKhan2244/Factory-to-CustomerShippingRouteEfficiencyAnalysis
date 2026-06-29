import streamlit as st
import pandas as pd
import joblib
# pyrefly: ignore [missing-import]
from utils.data_loader import load_data
from pathlib import Path
df = load_data()



BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "CandyDistributerModel.joblib"

model = joblib.load(MODEL_PATH)

st.title("🤖 Delay Prediction")

ship_mode = st.number_input("Ship Mode", min_value=1)
region = st.number_input("Region", min_value=1)
state = st.number_input("State/Province", min_value=1)
division = st.number_input("Division", min_value=1)
factory = st.number_input("Factory", min_value=1)

sales = st.number_input("Sales")
cost = st.number_input("Cost")
gross_profit = st.number_input("Gross Profit")
order_month = st.number_input("Order Month", min_value=1, max_value=12)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "Ship Mode": [ship_mode],
        "Region": [region],
        "State/Province": [state],
        "Division": [division],
        "Factory": [factory],
        "Sales": [sales],
        "Cost": [cost],
        "Gross Profit": [gross_profit],
        "Order Month": [order_month]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error("🚨 Shipment is likely to be DELAYED")
    else:
        st.success("✅ Shipment is likely to be ON TIME")

    st.metric(
        "Delay Probability",
        f"{probability*100:.2f}%"
    )