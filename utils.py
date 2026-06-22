import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def detect_risk_factors(text):
    risks = []
    suspicious = {
        "registration fee":"Payment request detected",
        "pay money":"Financial scam signal",
        "urgent hiring":"Artificial urgency detected",
        "immediate joining":"Urgency pressure pattern",
        "no interview":"No formal hiring process",
        "easy income":"Unrealistic earning promise",
        "whatsapp":"Informal communication"
    }
    for k,v in suspicious.items():
        if k in text.lower():
            risks.append(v)
    if len(text.split()) < 15:
        risks.append("Very limited job details")
    return risks