import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

history_path = "reports/history.csv"

if os.path.exists(history_path):

    try:
        df = pd.read_csv(history_path)

        if df.empty:
            st.warning("No reports available yet.")

        elif "Prediction" not in df.columns:
            st.error("history.csv exists but required columns are missing.")
            st.write("Expected columns:")
            st.code("Job Title, Fraud Score, Risk Level, Prediction")

        else:
            total_checks = len(df)

            fake_count = len(df[df["Prediction"] == "Fake"])
            genuine_count = len(df[df["Prediction"] == "Genuine"])

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Checks", total_checks)
            col2.metric("Fake Jobs Detected", fake_count)
            col3.metric("Genuine Jobs", genuine_count)

            st.subheader("Prediction Distribution")

            fig = plt.figure(figsize=(6, 4))
            plt.bar(
                ["Fake", "Genuine"],
                [fake_count, genuine_count]
            )
            plt.title("Fake vs Genuine Jobs")
            st.pyplot(fig)

            st.subheader("Recent Reports")
            st.dataframe(df.tail(10))

    except Exception as e:
        st.error(f"Error reading history file: {e}")

else:
    st.warning("No history file found.")