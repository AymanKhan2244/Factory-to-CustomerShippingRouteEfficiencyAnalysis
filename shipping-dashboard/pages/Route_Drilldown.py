import streamlit as st
from utils.data_loader import load_data

st.title("🔍 Route Drill-Down")

df = load_data()



selected_state = st.selectbox(
    "Select State",
    sorted(df['State/Province'].unique())
)
#selected_region = st.selectbox(
    #"Select Region",
   # sorted(df['Region'].unique())
#)

filtered_df = df[
    df['State/Province'] == selected_state
]


if filtered_df.empty:
    st.warning(
        "No data available for selected filters."
    )
    st.stop()


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Orders",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Average Lead Time",
        round(
            filtered_df['Lead_time'].mean(),
            2
        )
    )

with col3:
    st.metric(
        "Factories",
        filtered_df['Factory'].nunique()
    )

st.subheader(
    "📊 State Performance"
)

st.dataframe(
    filtered_df[
        [
            'Factory',
            'State/Province',
            'Ship Mode',
            'Lead_time'
        ]
    ]
)

st.subheader(
    "📦 Order-Level Shipment Timeline"
)

timeline_df = filtered_df[
    [
        'Order ID',
        'Order Date',
        'Ship Date',
        'Lead_time',
        'Ship Mode',
        'Factory'
    ]
]

st.dataframe(timeline_df)


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(
    filtered_df['Lead_time'],
    bins=20
)

ax.set_title(
    "Lead Time Distribution"
)

ax.set_xlabel(
    "Lead Time"
)

st.pyplot(fig)


route_summary = filtered_df.groupby(
    'Route'
).agg(
    Avg_Lead_Time=('Lead_time','mean'),
    Shipments=('Order ID','count')
).reset_index()


st.subheader(
    "🚚 Route Summary"
)

st.dataframe(route_summary)