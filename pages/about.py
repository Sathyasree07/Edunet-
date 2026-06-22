import streamlit as st

st.title("📘 About JobShield AI")

st.markdown("""
# 🛡 JobShield AI  
### Intelligent Fake Job Detection System

JobShield AI is an AI-powered fraud detection platform designed to identify suspicious and fraudulent job postings.  
With the rise of online job scams, many students and job seekers fall victim to fake opportunities that demand money, personal information, or offer unrealistic promises.

This system helps users verify job postings before applying.

---

## 🎯 Project Objective

The primary goal of JobShield AI is to:

- Detect fraudulent job postings using Machine Learning
- Reduce the risk of job scams
- Provide risk-based analysis for job seekers
- Improve trust in online recruitment systems
- Educate users about scam patterns

---

## 🚨 Problem Statement

Job fraud has become a serious issue in digital recruitment platforms.

Common scam indicators include:

- Asking for registration fees
- Fake company profiles
- Unrealistic salary offers
- Immediate joining without interviews
- Work-from-home scams
- Poorly written job descriptions

Traditional job platforms often fail to detect these patterns effectively.

JobShield AI solves this problem.

---

## ⚙ How JobShield AI Works

### Step 1: User Input
The user enters:

- Job title
- Location
- Salary range
- Company profile
- Job description
- Requirements
- Benefits

---

### Step 2: Text Preprocessing

The system cleans and processes the input using:

✔ Lowercasing  
✔ Removing special characters  
✔ Removing unnecessary spaces  
✔ Feature extraction preparation  

---

### Step 3: Feature Extraction

We use:

**TF-IDF Vectorization (Term Frequency–Inverse Document Frequency)**

This converts text into numerical values for machine learning.

---

### Step 4: Machine Learning Prediction

The trained Logistic Regression model analyzes:

- Text patterns
- Scam keywords
- Salary anomalies
- Risk factors

The model calculates fraud probability.

---

### Step 5: Risk Analysis Engine

Additional fraud rules are applied:

- Payment request detection
- Urgency patterns
- Informal communication channels
- Unrealistic earning promises
- Missing hiring processes

---

### Step 6: Final Output

The system provides:

✔ Fraud Score (%)  
✔ Risk Level (Low / Medium / High)  
✔ Scam Indicators  
✔ Final Recommendation  

---

## 🧠 Machine Learning Model

### Model Used:
**Logistic Regression**

Reason:
- Fast
- Efficient
- Works well for text classification
- Interpretable probabilities

---

### Vectorizer:
**TF-IDF Vectorizer**

Used for converting text into numerical format.

---

## 📊 Model Performance

Current performance:

- Accuracy: **97.2%**
- Precision: **1.00**
- Recall: **0.45**
- F1 Score: **0.62**

### Important Note:
Accuracy alone is not enough.

Recall is very important because:

Missing a fake job is more dangerous than wrongly flagging a genuine one.

Future improvements will focus on improving recall.

---

## 📁 Dataset Information

Dataset Source:
Kaggle Fake Job Posting Dataset

Contains:

- 17,000+ job postings
- Genuine job posts
- Fraudulent job posts

Key columns:

- Title
- Location
- Salary Range
- Company Profile
- Description
- Requirements
- Benefits
- Fraudulent Label

---

## 📈 Dashboard Features

The dashboard provides:

- Total jobs analyzed
- Fake vs genuine graph
- Fraud score trends
- Historical report logs
- Prediction analytics

---

## 🔒 Future Improvements

Future upgrades:

- Company website verification
- LinkedIn verification
- Domain legitimacy checking
- NLP-based deep fraud detection
- Resume-job matching
- Real-time API integration

---

## 💻 Tech Stack

Frontend:
- Streamlit

Backend:
- Python

Machine Learning:
- Scikit-learn

Visualization:
- Matplotlib

Data Processing:
- Pandas, NumPy

---

## 👨‍💻 Developed By

**Sathya Sree M**  
Integrated M.Tech Data Science  
VIT Vellore

Project Type:
Academic + Real-world Fraud Detection Solution
""")