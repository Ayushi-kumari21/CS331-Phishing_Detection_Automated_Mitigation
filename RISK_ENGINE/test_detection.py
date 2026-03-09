# import requests

# # API endpoint
# url = "http://127.0.0.1:5000/detect"

# # List of emails for testing
# emails = [

# # Safe Emails
# """Subject: Meeting Reminder
# Hi Team,
# This is a reminder that we have our weekly project meeting tomorrow at 10 AM in the conference room.
# Thanks,
# Rahul""",

# """Subject: Assignment Submission
# Dear Professor,
# I have submitted the lab assignment through the portal. Please let me know if any changes are required.
# Regards,
# Dipti""",

# """Subject: Lunch Plan
# Hi,
# Are you free for lunch today at 1 PM? Let me know.
# Thanks""",

# """Subject: Event Invitation
# Hello,
# You are invited to attend the college tech fest on Saturday. Please register through the campus portal.
# Best regards""",

# """Subject: Project Update
# Hi Team,
# The backend API integration has been completed successfully. We will begin testing tomorrow.
# Regards""",

# # Suspicious Emails
# """Subject: Security Notice
# Dear User,
# We noticed unusual activity on your account. Please confirm your login information.
# Support Team""",

# """Subject: Important Account Notification
# Hello,
# Your account requires verification. Please confirm your details to avoid service interruption.
# Thank you""",

# """Subject: Password Reset Request
# Dear Customer,
# A password reset was requested for your account. If this was not you, please review your security settings.
# Support""",

# """Subject: Payment Confirmation
# Hello,
# We received a payment request from your account. Please confirm the transaction if you initiated it.
# Billing Team""",

# """Subject: Update Your Profile
# Dear User,
# Please update your profile information to continue using our services.
# Thanks""",

# # Phishing Emails
# """Subject: URGENT: Account Suspension
# Dear Customer,
# Your bank account will be suspended within 24 hours. Click the link below to verify immediately:
# http://secure-bank-login-update.com
# Bank Security Team""",

# """Subject: Verify Your Account Now
# Dear User,
# We detected suspicious login attempts. Verify your account immediately:
# http://account-verification-secure.com
# Failure to verify will result in account suspension.""",

# """Subject: Prize Winner Notification
# Congratulations!
# You have won a $500 gift card. Claim your reward now by visiting:
# http://claim-reward-now.com""",

# """Subject: PayPal Alert
# Dear PayPal User,
# Your account has been limited. Login immediately to restore access:
# http://paypal-login-verification.net""",

# """Subject: Email Account Warning
# Your email storage is full. Click here to upgrade your mailbox immediately:
# http://mailbox-update-service.com""",

# """Subject: Netflix Payment Failed
# Dear Customer,
# Your payment failed. Update your payment details now to continue using Netflix:
# http://netflix-payment-update.net""",

# """Subject: Immediate Action Required
# Your account will be deleted unless you verify your details immediately.
# http://secure-verification-login.com""",

# """Subject: Bank Security Alert
# We detected unusual transactions on your account. Verify your identity here:
# http://bank-security-check.com""",

# """Subject: Tax Refund Available
# You are eligible for a tax refund. Submit your banking information here:
# http://tax-refund-processing.com""",

# """Subject: Urgent Password Reset
# Your account has been compromised. Reset your password immediately:
# http://secure-password-reset.com"""
# ]

# # Send each email to API
# for i, email in enumerate(emails, start=1):

#     response = requests.post(url, json={"email": email})

#     print("\n-----------------------------")
#     print(f"Email {i}:")
#     print(email[:120], "...")  # show preview
#     print("Detection Result:", response.json())
import requests
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# API endpoint
url = "http://127.0.0.1:5000/detect"

# Test emails with expected labels (Subject, Body, Label)
test_data = [

# Safe Emails
("Meeting Reminder", "Meeting tomorrow at 10 AM in conference room", "Safe"),
("Lunch Plan", "Lunch plan today at 1 PM?", "Safe"),
("Project Update", "Backend integration completed successfully", "Safe"),
("Tech Fest Invitation", "You are invited to the college tech fest event", "Safe"),
("Assignment Submission", "Assignment has been submitted on the portal", "Safe"),

# Suspicious Emails
("Security Notice", "Please confirm your login information for security reasons", "Suspicious"),
("Account Notification", "Your account requires verification to continue services", "Suspicious"),
("Password Reset", "Password reset request detected on your account", "Suspicious"),
("Payment Confirmation", "Confirm this payment request from your account", "Suspicious"),
("Profile Update", "Update your profile information immediately", "Suspicious"),

# Phishing Emails
("Urgent Account Suspension", "Your account will be suspended. Click http://fakebank-login.com to verify", "Phishing"),
("Verify Account", "Verify your account immediately http://secure-login-update.com", "Phishing"),
("Prize Winner", "You won a $500 gift card claim at http://claim-reward-now.com", "Phishing"),
("PayPal Alert", "PayPal alert login now http://paypal-login-verification.net", "Phishing"),
("Mailbox Full", "Your mailbox is full update here http://mailbox-update-service.com", "Phishing"),
("Netflix Payment Failed", "Netflix payment failed update here http://netflix-payment-update.net", "Phishing"),
("Immediate Action Required", "Immediate action required verify account http://secure-verification-login.com", "Phishing"),
("Bank Security Alert", "Bank security alert verify identity http://bank-security-check.com", "Phishing"),
("Tax Refund", "Tax refund available submit details http://tax-refund-processing.com", "Phishing"),
("Password Reset Urgent", "Reset your password immediately http://secure-password-reset.com", "Phishing")

]

true_labels = []
predicted_labels = []

print("\nTesting Emails...\n")

for i, (subject, body, label) in enumerate(test_data, start=1):

    # Combine subject and body
    email_text = subject + " " + body

    response = requests.post(url, json={"email": email_text})
    result = response.json()

    predicted = result["category"]

    true_labels.append(label)
    predicted_labels.append(predicted)

    print("-----------------------------------")
    print(f"Email {i}")
    print("Subject:", subject)
    print("Body:", body)
    print("Expected:", label)
    print("Predicted:", predicted)
    print("Risk Score:", result["risk_score"])

# Evaluation Metrics
accuracy = accuracy_score(true_labels, predicted_labels)
precision = precision_score(true_labels, predicted_labels, average="weighted")
recall = recall_score(true_labels, predicted_labels, average="weighted")
matrix = confusion_matrix(true_labels, predicted_labels)

print("\n==============================")
print("Evaluation Results")
print("==============================")

print("Accuracy:", round(accuracy,3))
print("Precision:", round(precision,3))
print("Recall:", round(recall,3))

print("\nConfusion Matrix:")
print(matrix)