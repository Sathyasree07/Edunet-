# 🛡 JobShield AI – Fake Job Detection System

JobShield AI is an AI-powered fraud detection system designed to identify fake and suspicious job postings using Machine Learning and Natural Language Processing (NLP).

With the increasing number of online recruitment scams, this project helps job seekers verify opportunities before applying.

---

## 📌 Features

- Detects fraudulent job postings using Machine Learning
- Calculates fraud probability score
- Classifies jobs into:
  - Low Risk
  - Medium Risk
  - High Risk
- Identifies scam patterns and suspicious keywords
- Stores report history
- Interactive dashboard with analytics
- User-friendly Streamlit interface

---

## 🚀 Project Workflow

1. User enters job details
2. Input text is preprocessed
3. TF-IDF converts text into numerical features
4. Logistic Regression predicts fraud probability
5. Risk factors are analyzed
6. Final result and recommendation are displayed

---

## 🧠 Machine Learning Model

### Model Used:
- Logistic Regression

### Vectorization:
- TF-IDF Vectorizer

### Data Preprocessing:
- Lowercasing
- Removing special characters
- Removing unnecessary spaces
- Handling missing values

---

## 📊 Model Performance

- Accuracy: **97.2%**
- Precision: **1.00**
- Recall: **0.45**
- F1 Score: **0.62**

---

## 📂 Dataset

Dataset used:

**Kaggle Fake Job Posting Dataset**

Contains:

- Job Title
- Location
- Salary Range
- Company Profile
- Description
- Requirements
- Benefits
- Fraudulent Label

---

## 🛠 Tech Stack

### Frontend:
- Streamlit

### Backend:
- Python

### Machine Learning:
- Scikit-learn

### Data Processing:
- Pandas
- NumPy

### Visualization:
- Matplotlib

---

## 📁 Project Structure

```text
fake_job_detection/
│── app.py
│── train_model.py
│── utils.py
│── requirements.txt
│── model.pkl
│── vectorizer.pkl
│── pages/
│   │── about.py
│   │── dashboard.py
│   │── report_history.py
│── reports/
│   │── history.csv
│── dataset/
│   │── fake_job_postings.csv
│── assets/
│   │── logo.png
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone <your-repository-link>
cd fake_job_detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Dashboard Features

- Total jobs analyzed
- Fake vs genuine job graph
- Fraud score analysis
- Historical report tracking

---

## 🔮 Future Improvements

- Company website verification
- LinkedIn verification
- Domain legitimacy checking
- Advanced NLP models
- Real-time job API integration

---

## 📚 References

- Vidros et al. (2017) – Online Recruitment Fraud Detection
- Kaggle Fake Job Posting Dataset
- Scikit-learn Documentation
- Pandas Documentation
- Research papers on Fake Job Detection using Machine Learning

---

## 👨‍💻 Developed By

**Sathya Sree M**  
Integrated M.Tech Data Science  
VIT Vellore
