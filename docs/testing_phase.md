# Test Plan

## 1. Objective of Testing

The objective of testing is to verify that the phishing detection system correctly scans emails, classifies them based on risk, performs appropriate mitigation actions (such as moving phishing emails to spam), and generates notifications for the user.

---

## 2. Scope

The following modules are included in testing:

- Email Scanning Module (Gmail API integration)
- Risk Classification Module (phishing detection)
- Mitigation Module (move to spam)
- Notification Module
- Database Operations (DAL functions)
- Frontend Notification Display

---

## 3. Types of Testing

### Unit Testing
Testing individual functions such as `save_email()` and `create_notification()`.

### Integration Testing
Testing interaction between modules (e.g., scanning → classification → database → notification).

### System Testing
Testing the complete workflow from scanning emails to displaying results in the UI.

### Functional Testing (Black Box)
Verifying correct output for given inputs without knowledge of internal code.

### White Box Testing
Testing internal logic such as conditions and loops in the scanning function.

---

## 4. Tools Used

- Backend: FastAPI (API testing via Swagger UI)
- Database: SQLite (`sentinelphish.db`)
- Frontend: React UI
- Testing Method: Manual testing using API calls and UI interaction

---

## 5. Entry Criteria

- Backend server is running successfully
- Database is created and migrated
- Gmail account is connected
- Risk engine is functional

---

## 6. Exit Criteria

- All test cases executed
- All critical functionalities working correctly
- No high-severity defects remain
- Notifications and mitigation actions verified
