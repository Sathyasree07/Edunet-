import streamlit as st
import pickle, pandas as pd, os
import re
from utils import clean_text, detect_risk_factors
import os

# Create reports folder and history file if missing
if not os.path.exists("reports"):
    os.makedirs("reports")

if not os.path.exists("reports/history.csv"):
    import pandas as pd
    empty_df = pd.DataFrame(columns=[
        "Job Title",
        "Fraud Score",
        "Risk Level",
        "Prediction"
    ])
    empty_df.to_csv("reports/history.csv", index=False)
st.set_page_config(page_title="JobShield AI", page_icon="🛡", layout="wide")

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("🛡 JobShield AI")
st.subheader("AI-based Fake Job Detection")

job_title = st.text_input("Job Title")
location = st.text_input("Location")
salary = st.text_input(
    "Salary Range (Example: 5-10 LPA or 500000)"
)
company_profile = st.text_area("Company Profile")
description = st.text_area("Job Description")
requirements = st.text_area("Requirements")
benefits = st.text_area("Benefits")

if st.button("Analyze Job"):
    combined = f"{job_title} {location} {salary} {company_profile} {description} {requirements} {benefits}"
    cleaned = clean_text(combined)
    transformed = vectorizer.transform([cleaned])

    probability = model.predict_proba(transformed)[0][1]
    fraud_score = probability * 100
    threshold = 0.50
    prediction = 1 if probability >= threshold else 0

    risk_level = "Low Risk" if fraud_score < 30 else "Medium Risk" if fraud_score < 60 else "High Risk"

    if prediction:
        st.error(f"⚠ Fraudulent Job ({risk_level})")
    else:
        st.success(f"✅ Genuine Job ({risk_level})")

    st.progress(int(fraud_score))
    st.write(f"Fraud Score: {fraud_score:.2f}%")

    risks = detect_risk_factors(cleaned)
    st.subheader("Risk Analysis")
    if risks:
        for r in risks:
            st.warning(r)
    else:
        st.success("No suspicious indicators.")

    report = {
        "Job Title": job_title,
        "Fraud Score": fraud_score,
        "Risk Level": risk_level,
        "Prediction": "Fake" if prediction else "Genuine"
    }

    df = pd.DataFrame([report])

    if os.path.exists("reports/history.csv"):
        df.to_csv("reports/history.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("reports/history.csv", index=False)


def parse_salary(salary):
    if not salary:
        return 0

    salary = str(salary).lower().replace(",", "").strip()

    # Handle Lakhs Per Annum (LPA)
    if "lpa" in salary:
        numbers = re.findall(r'\d+\.?\d*', salary)

        if len(numbers) == 1:
            return float(numbers[0]) * 100000

        elif len(numbers) >= 2:
            return max(map(float, numbers)) * 100000

    # Handle "k" format (example: 120k)
    elif "k" in salary:
        numbers = re.findall(r'\d+\.?\d*', salary)

        if numbers:
            return float(numbers[0]) * 1000

    # Handle monthly salary
    elif "month" in salary:
        numbers = re.findall(r'\d+\.?\d*', salary)

        if numbers:
            return float(numbers[0]) * 12

    # General number extraction
    else:
        numbers = re.findall(r'\d+\.?\d*', salary)

        if numbers:
            return max(map(float, numbers))

    return 0