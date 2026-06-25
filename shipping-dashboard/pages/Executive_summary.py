import streamlit as st
import pandas as pd
# pyrefly: ignore [missing-import]
from utils.data_loader import load_data

st.set_page_config(
    page_title="Executive Summary",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Executive Summary")
st.markdown("High-level overview of Nassau Candy shipping performance.")

# Load data
df = load_data()


total_shipments = len(df)

avg_lead_time = round(
    df['Lead_time'].mean(),
    2
)

total_states = df['State/Province'].nunique()

delay_frequency = round(
    df['Delayed'].mean() * 100,
    2
)



col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Shipments",
        total_shipments
    )

with col2:
    st.metric(
        "Average Lead Time",
        avg_lead_time
    )

with col3:
    st.metric(
        "States Covered",
        total_states
    )

with col4:
    st.metric(
        "Delay Frequency %",
        delay_frequency
    )

st.divider()



route_summary = df.groupby(
    'Route'
).agg(
    Avg_Lead_Time=('Lead_time','mean')
).reset_index()

best_route = route_summary.sort_values(
    by='Avg_Lead_Time'
).iloc[0]

worst_route = route_summary.sort_values(
    by='Avg_Lead_Time',
    ascending=False
).iloc[0]



state_congestion = df.groupby(
    'State/Province'
).agg(
    Avg_Lead_Time=('Lead_time','mean'),
    Total_Shipments=('Order ID','count')
).reset_index()

state_congestion['Congestion_Score'] = (
    state_congestion['Avg_Lead_Time']
    *
    state_congestion['Total_Shipments']
)

most_congested = state_congestion.sort_values(
    by='Congestion_Score',
    ascending=False
).iloc[0]



ship_mode_analysis = df.groupby(
    'Ship Mode'
).agg(
    Avg_Lead_Time=('Lead_time','mean')
).reset_index()

best_ship_mode = ship_mode_analysis.sort_values(
    by='Avg_Lead_Time'
).iloc[0]



st.subheader("🏆 Key Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"Best Route: {best_route['Route']}"
    )

    st.info(
        f"Best Ship Mode: {best_ship_mode['Ship Mode']}"
    )

with col2:

    st.error(
        f"Worst Route: {worst_route['Route']}"
    )

    st.warning(
        f"Most Congested State: {most_congested['State/Province']}"
    )

st.divider()



summary_df = pd.DataFrame({
    "Metric":[
        "Best Route",
        "Worst Route",
        "Most Congested State",
        "Best Ship Mode"
    ],
    "Value":[
        best_route['Route'],
        worst_route['Route'],
        most_congested['State/Province'],
        best_ship_mode['Ship Mode']
    ]
})

st.subheader("📋 Executive Highlights")

st.dataframe(
    summary_df,
    use_container_width=True
)