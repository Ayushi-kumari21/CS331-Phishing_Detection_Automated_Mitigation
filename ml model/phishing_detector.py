import pickle
import re
import numpy as np
import tldextract # type: ignore
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "phishing_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

trusted_domains = ["gmail.com","paypal.com","amazon.com"]

phishing_words = [
"verify","login","account","password",
"urgent","update","confirm","bank"
]

def clean_text(text):

    text = text.lower()
    text = re.sub(r"http\S+","",text)
    text = re.sub(r"[^a-zA-Z]"," ",text)

    return text

def extract_urls(text):

    return re.findall(r'https?://\S+',str(text))

def suspicious_domain_count(text):

    urls = extract_urls(text)

    count = 0

    for url in urls:

        domain = tldextract.extract(url).registered_domain

        if domain not in trusted_domains:
            count += 1

    return count

def keyword_score(text):

    score = 0

    for word in phishing_words:

        if word in text.lower():
            score += 1

    return score


def classify(score):

    if score < 30:
        return "Safe"

    elif score < 60:
        return "Suspicious"

    else:
        return "Phishing"


def detect_email(email_text):

    clean = clean_text(email_text)

    text_vec = vectorizer.transform([clean]).toarray()

    features = np.array([[
    len(extract_urls(email_text)),           # num_links
    suspicious_domain_count(email_text),     # suspicious_domains
    1,                                       # unknown_sender
    keyword_score(email_text)                # keyword_score
]])

    X = np.hstack((text_vec,features))

    prob = model.predict_proba(X)[0][1]

    risk_score = prob * 100

    result = classify(risk_score)

    return risk_score, result