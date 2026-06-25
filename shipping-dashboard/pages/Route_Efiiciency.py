import streamlit as st
# pyrefly: ignore [missing-import]
from utils.data_loader import load_data
import matplotlib.pyplot as plt 
df = load_data()

st.title("📊 Route Efficiency Overview")


total_shipments = len(df)

avg_lead_time = round(
    df['Lead_time'].mean(),
    2
)

st.metric(
    "Total Shipments",
    total_shipments
)

st.metric(
    "Average Lead Time",
    f"{avg_lead_time} Days"
)


route_summary = df.groupby('Route').agg(
    Avg_Lead_Time=('Lead_time','mean'),
    Total_Shipments=('Order ID','count')
).reset_index()


top_routes = route_summary.sort_values(
    by='Avg_Lead_Time'
).head(10)

st.subheader("🏆 Top 10 Efficient Routes")

st.dataframe(top_routes)



fig, ax = plt.subplots(figsize=(10,5))

ax.barh(
    top_routes['Route'],
    top_routes['Avg_Lead_Time']
)

ax.invert_yaxis()

st.pyplot(fig)