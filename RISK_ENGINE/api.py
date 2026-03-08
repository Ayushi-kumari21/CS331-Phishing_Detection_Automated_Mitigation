from flask import Flask, request, jsonify
from risk_engine import calculate_risk

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():

    email_text = request.json['email']

    result = calculate_risk(email_text)

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000)