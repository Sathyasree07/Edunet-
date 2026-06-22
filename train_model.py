import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from utils import clean_text

df = pd.read_csv("dataset/fake_job_postings.csv")
df.fillna("", inplace=True)

df["combined_text"] = (
    df["title"] + " " + df["location"] + " " + df["salary_range"] + " " +
    df["company_profile"] + " " + df["description"] + " " +
    df["requirements"] + " " + df["benefits"]
)

df["combined_text"] = df["combined_text"].apply(clean_text)

X = df["combined_text"]
y = df["fraudulent"]

vectorizer = TfidfVectorizer(stop_words="english", max_features=7000)
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

model = LogisticRegression(class_weight="balanced")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Model and vectorizer saved.")