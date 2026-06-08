import streamlit as st
import matplotlib.pyplot as plt
from utils.data_loader import load_data

st.title("🚚 Ship Mode Performance Analysis")

df = load_data()



ship_mode_analysis = df.groupby(
    'Ship Mode'
).agg(
    Avg_Lead_Time=('Lead_time', 'mean'),
    Total_Shipments=('Order ID', 'count'),
    Avg_Sales=('Sales', 'mean'),
    Avg_Profit=('Gross Profit', 'mean')
).reset_index()



col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Ship Modes",
        ship_mode_analysis.shape[0]
    )

with col2:
    st.metric(
        "Avg Lead Time",
        round(
            ship_mode_analysis['Avg_Lead_Time'].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Total Shipments",
        len(df)
    )

st.subheader("📋 Ship Mode Performance")

st.dataframe(ship_mode_analysis)



fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    ship_mode_analysis['Ship Mode'],
    ship_mode_analysis['Avg_Lead_Time']
)

ax.set_title(
    "Average Lead Time by Ship Mode"
)

ax.set_ylabel(
    "Average Lead Time"
)

st.pyplot(fig)



fig, ax = plt.subplots(figsize=(5,8))

ax.pie(
    ship_mode_analysis['Total_Shipments'],
    labels=ship_mode_analysis['Ship Mode'],
    autopct='%1.1f%%'
)

ax.set_title(
    "Shipment Distribution by Ship Mode"
)

st.pyplot(fig)


st.subheader(
    "💰 Cost-Time Tradeoff"
)

st.dataframe(
    ship_mode_analysis[
        [
            'Ship Mode',
            'Avg_Lead_Time',
            'Avg_Sales',
            'Avg_Profit'
        ]
    ]
)

best_mode = ship_mode_analysis.sort_values(
    by='Avg_Lead_Time'
).iloc[0]

st.success(
    f"Best performing ship mode: {best_mode['Ship Mode']}"
)