import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# pyrefly: ignore [missing-import]
from utils.data_loader import load_data

df = load_data()


st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Machine Learning Model Performance")

st.markdown("""
This page summarizes the performance of the XGBoost model used to predict shipment delays.
""")



accuracy = 0.6027
precision = 0.53
recall = 0.42
f1_score = 0.47

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", f"{accuracy*100:.2f}%")

with col2:
    st.metric("Precision", f"{precision*100:.2f}%")

with col3:
    st.metric("Recall", f"{recall*100:.2f}%")

with col4:
    st.metric("F1 Score", f"{f1_score*100:.2f}%")

st.divider()



st.subheader("📋 Classification Report")

st.table({
    "Metric": [
        "Precision (Class 0)",
        "Recall (Class 0)",
        "F1 Score (Class 0)",
        "Precision (Class 1)",
        "Recall (Class 1)",
        "F1 Score (Class 1)"
    ],
    "Value": [
        0.64,
        0.74,
        0.68,
        0.53,
        0.42,
        0.47
    ]
})

st.divider()



st.subheader("📌 Confusion Matrix")

cm = np.array([
    [875,314],
    [496,354]
])

fig, ax = plt.subplots(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Not Delayed","Delayed"],
    yticklabels=["Not Delayed","Delayed"],
    ax=ax
)

ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")

st.pyplot(fig)

st.divider()

st.subheader("⭐ Feature Importance")

features = [
    "State/Province",
    "Order Month",
    "Gross Profit",
    "Cost",
    "Sales",
    "Ship Mode",
    "Region",
    "Factory",
    "Division"
]

importance = [
    925,
    852,
    495,
    386,
    383,
    293,
    226,
    103,
    26
]

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(features, importance)

ax.invert_yaxis()

ax.set_xlabel("Importance Score")
ax.set_title("Feature Importance")

st.pyplot(fig)

st.divider()



st.subheader("💡 Business Insights")

st.success("""
**Key Findings**

- State/Province is the strongest predictor of shipment delays.
- Seasonal effects (Order Month) significantly influence delivery performance.
- Gross Profit and Cost contribute moderately to prediction.
- Ship Mode has a measurable impact on delivery delays.
- Factory and Division have relatively low influence compared to geographic factors.
""")

st.divider()



st.subheader("📑 Model Summary")

st.info("""
**Model Used:** XGBoost Classifier

**Problem Type:** Binary Classification

**Target Variable:** Delayed

**Evaluation Metrics**

- Accuracy : 60.27%
- Precision : 53%
- Recall : 42%
- F1 Score : 47%

The model is capable of identifying shipment delay patterns using operational and geographic features.
""")