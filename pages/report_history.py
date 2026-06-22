import streamlit as st
import pandas as pd
import os

st.title("📝 Report History")

# Auto-create history file if missing
if not os.path.exists("reports"):
    os.makedirs("reports")

if not os.path.exists("reports/history.csv"):
    empty_df = pd.DataFrame(columns=[
        "Job Title",
        "Fraud Score",
        "Risk Level",
        "Prediction"
    ])
    empty_df.to_csv("reports/history.csv", index=False)

df = pd.read_csv("reports/history.csv")

if df.empty:
    st.info("No history available yet.")
else:
    st.dataframe(df)