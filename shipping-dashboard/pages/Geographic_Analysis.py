import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.data_loader import load_data

st.title("🌎 Geographic Shipping Analysis")

df = load_data()




state_analysis = df.groupby(
    'State/Province'
).agg(
    Avg_Lead_Time=('Lead_time', 'mean'),
    Total_Shipments=('Order ID', 'count')
).reset_index()

state_analysis = state_analysis.sort_values(
    by='Avg_Lead_Time',
    ascending=False
)


st.subheader("🚨 Top Bottleneck States")

st.dataframe(
    state_analysis.head(10)
)




top_states = state_analysis.head(10)

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(
    top_states['State/Province'],
    top_states['Avg_Lead_Time']
)

ax.set_xlabel("Average Lead Time")
ax.set_ylabel("State")

ax.set_title("Top 10 Bottleneck States")

ax.invert_yaxis()

st.pyplot(fig)


region_analysis = df.groupby(
    'Region'
).agg(
    Avg_Lead_Time=('Lead_time', 'mean'),
    Total_Shipments=('Order ID', 'count')
).reset_index()



st.subheader("📍 Region Performance")

st.dataframe(region_analysis)


fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    region_analysis['Region'],
    region_analysis['Avg_Lead_Time']
)

ax.set_xlabel("Region")
ax.set_ylabel("Average Lead Time")

ax.set_title("Lead Time by Region")

st.pyplot(fig)


region_analysis['Congestion_Score'] = (
    region_analysis['Avg_Lead_Time']
    *
    region_analysis['Total_Shipments']
)

st.subheader("🚦 Congestion Analysis")

st.dataframe(
    region_analysis.sort_values(
        by='Congestion_Score',
        ascending=False
    )
)


fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    region_analysis['Region'],
    region_analysis['Congestion_Score']
)

ax.set_title(
    "Regional Congestion Score"
)

ax.set_ylabel(
    "Congestion Score"
)

st.pyplot(fig)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "States Analyzed",
        state_analysis.shape[0]
    )

with col2:
    st.metric(
        "Regions",
        region_analysis.shape[0]
    )

with col3:
    st.metric(
        "Highest Congestion",
        region_analysis.sort_values(
            by='Congestion_Score',
            ascending=False
        ).iloc[0]['Region']
    )