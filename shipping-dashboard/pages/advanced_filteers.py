import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# pyrefly: ignore [missing-import]
from utils.data_loader import load_data

st.set_page_config(
    page_title="Advanced Filters",
    page_icon="🎛️",
    layout="wide"
)


df = load_data()

st.title("🎛️ Advanced Shipping Filters")

st.markdown("""
Filter shipment records based on **Date**, **Region**, **State**, **Ship Mode**, and **Lead Time**.
""")





df["Order Date"] = pd.to_datetime(
    df["Order Date"]
   
)



st.sidebar.header("Filter Shipments")


date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(
        df["Order Date"].min(),
        df["Order Date"].max()
    )
)

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start_date, end_date = date_range
elif isinstance(date_range, (list, tuple)) and len(date_range) == 1:
    start_date = date_range[0]
    end_date = df["Order Date"].max()
else:
    start_date = df["Order Date"].min()
    end_date = df["Order Date"].max()

selected_region = st.sidebar.selectbox(
    "🌍 Region",
    options=["All"] + list(sorted(df["Region"].unique()))
)



selected_state = st.sidebar.selectbox(
    "📍 State",
    options=["All"] + list(sorted(df["State/Province"].unique()))
)


selected_ship_mode = st.sidebar.selectbox(
    "🚚 Ship Mode",
    options=["All"] + list(sorted(df["Ship Mode"].unique()))
)


lead_time = st.sidebar.slider(
    "⏱ Lead Time Threshold",
    int(df["Lead_time"].min()),
    int(df["Lead_time"].max()),
    int(df["Lead_time"].mean())
)



filtered_df = df[
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date)) &
    (df["Region"].isin([selected_region] if selected_region != "All" else df["Region"].unique())) &
    (df["State/Province"].isin([selected_state] if selected_state != "All" else df["State/Province"].unique())) &
    (df["Ship Mode"].isin([selected_ship_mode] if selected_ship_mode != "All" else df["Ship Mode"].unique())) &
    (df["Lead_time"] >= lead_time)
]



st.subheader("📊 Filter Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Filtered Shipments",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Lead Time",
        round(filtered_df["Lead_time"].mean(), 2)
    )

with col3:
    st.metric(
        "Delayed Shipments",
        filtered_df["Delayed"].sum()
    )

st.divider()



st.subheader("📄 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()



st.subheader("🚚 Ship Mode Distribution")

ship_counts = filtered_df["Ship Mode"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    ship_counts.index,
    ship_counts.values
)

ax.set_title("Filtered Shipments by Ship Mode")
ax.set_ylabel("Shipments")

st.pyplot(fig)

st.divider()



st.subheader("🌍 Region Distribution")

region_counts = filtered_df["Region"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    region_counts.index,
    region_counts.values
)

ax.set_title("Filtered Shipments by Region")
ax.set_ylabel("Shipments")

st.pyplot(fig)

st.divider()


st.subheader("⏱ Lead Time Distribution")

fig, ax = plt.subplots(figsize=(10,5))

ax.hist(
    filtered_df["Lead_time"],
    bins=20
)

ax.set_title("Lead Time Distribution")
ax.set_xlabel("Lead Time")
ax.set_ylabel("Frequency")

st.pyplot(fig)