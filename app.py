import streamlit as st
import pandas as pd
import joblib
from sklearn import set_config
from sklearn.pipeline import Pipeline
import plotly.graph_objects as go

set_config(transform_output="pandas")

st.set_page_config(page_title="Customer Segmentation", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #1f77b4;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Customer Segmentation and Profiling (AI)")
st.markdown("---")

@st.cache_resource
def load_model():

    model: Pipeline = joblib.load("Model/model_customer_clustering.pkl")
    return model

try:
    pipeline = load_model()
    st.success("✅ System Ready: AI Model Active!")
except FileNotFoundError:
    st.error("🚨 ERROR: Model not found!")
    st.stop()

st.sidebar.header("📊 Customer Spending Data")
st.sidebar.markdown("Enter the company's average annual (or estimated) spending on its product groups.")

def user_input_features():
    fresh = st.sidebar.number_input("Fresh", min_value=0, value=12000, step=500)
    milk = st.sidebar.number_input("Milk", min_value=0, value=5000, step=100)
    grocery = st.sidebar.number_input("Grocery", min_value=0, value=8000, step=100)
    frozen = st.sidebar.number_input("Frozen", min_value=0, value=1000, step=50)
    detergents = st.sidebar.number_input("Detergents_Paper", min_value=0, value=2000, step=50)
    delicatessen = st.sidebar.number_input("Delicatessen", min_value=0, value=1500, step=50)

    data = {
        'Fresh': fresh,
        'Milk': milk,
        'Grocery': grocery,
        'Frozen': frozen,
        'Detergents_Paper': detergents,
        'Delicassen': delicatessen
    }
    return pd.DataFrame(data, index=[0])


input_df = user_input_features()

cluster_profiles = {
    0: {
        "Name": "High Retail",
        "Desc": "Retailer profile with the highest spending potential.",
        "Action": "Campaigns are suggested for stockable products such as milk, groceries, and detergents/paper."
    },
    1: {
        "Name": "Low Horeca",
        "Desc": "Business profile with the lowest spending potential (Hotel, Restaurant, Cafe).",
        "Action": "It appears to be a medium-sized cafe and restaurant. Positive actions could be taken to increase customer loyalty."
    },
    2: {
        "Name": "Low Retaill",
        "Desc": "This is a business with high spending potential. It has a retail profile but doesn't seem to have much need for fresh or frozen food.",
        "Action": "It is recommended to conduct campaigns that will encourage the business to make high-volume purchases and enjoy increasing the amount of stock. (But you should know that fresh and frozen foods are not of interest to the business.)"
    },
    3: {
        "Name": "High Horeca",
        "Desc": "A business profile exhibiting the behavior of Horeca (Hotel, Restaurant, Cafe) businesses, which have a relatively higher spending potential.",
        "Action": "Campaigns targeting fresh and frozen foods are recommended."
    }
}

if st.sidebar.button("🔍 Analyze the Customer"):

    prediction = pipeline.predict(input_df)[0]

    profile = cluster_profiles.get(prediction, {"Name": "Bilinmeyen", "Desc": "-", "Action": "-"})

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🎯 Result:")
        st.metric(label="Customer Segment", value=profile["Name"])
        st.info(f"**Definition:** {profile['Desc']}")
        st.warning(f"**Suggested Action:** {profile['Action']}")

    with col2:
        st.subheader("🧬 Customer DNA (Radar Graph)")

        categories = list(input_df.columns)
        values = input_df.values.flatten()

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Customer Spending'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(values) * 1.2]
                )),
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👈 To start the analysis, enter the data from the menu on the left and press the button.")
