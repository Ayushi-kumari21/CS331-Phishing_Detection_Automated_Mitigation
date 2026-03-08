from flask import Flask, request, jsonify
from phishing_detector import detect_email

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():

    data = request.json

    email_text = data["text"]

    score, result = detect_email(email_text)

    return jsonify({
        "risk_score": score,
        "classification": result
    })

if __name__ == "__main__":
    app.run(debug=True)