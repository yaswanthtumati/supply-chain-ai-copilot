import streamlit as st
import pandas as pd
from ai_agent import create_agent
from visualization import warehouse_delay_chart, product_speed_chart

def load_data():

    df = pd.read_csv("data/orders.csv")

    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    df["delivery_date"] = pd.to_datetime(df["delivery_date"])

    df["processing_time"] = (df["ship_date"] - df["order_date"]).dt.days
    df["shipping_delay"] = (df["delivery_date"] - df["ship_date"]).dt.days

    return df

st.title("Supply Chain AI Copilot")

df = pd.read_csv("data/orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])
df["delivery_date"] = pd.to_datetime(df["delivery_date"])

df["processing_time"] = (df["ship_date"] - df["order_date"]).dt.days
df["shipping_delay"] = (df["delivery_date"] - df["ship_date"]).dt.days

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Charts")

st.plotly_chart(warehouse_delay_chart(df))
st.plotly_chart(product_speed_chart(df))

agent = create_agent(df)

st.subheader("Ask AI")

question = st.text_input("Ask a question about the supply chain data")

if question:
    response = agent(question)
    st.write(response)