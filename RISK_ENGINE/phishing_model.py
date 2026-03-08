from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ealvaradob/bert-finetuned-phishing"
)

def predict_email(email_text):
    result = classifier(email_text)[0]
    return result