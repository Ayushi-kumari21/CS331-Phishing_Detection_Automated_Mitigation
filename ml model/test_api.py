import requests

url = "http://127.0.0.1:5000/detect"

data = {
    "text": "Verify your account immediately http://fakebank-login.xyz"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)