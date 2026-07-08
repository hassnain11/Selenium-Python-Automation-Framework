# Login Test Scenarios

## Feature

Login

---

## Positive Test Cases

TC_001
Verify login using valid username and password.

Expected:
User should navigate to Inventory page.

---

## Negative Test Cases

TC_002
Verify login using invalid username.

Expected:
Proper error message displayed.

---

TC_003
Verify login using invalid password.

Expected:
Proper error message displayed.

---

TC_004
Verify login using invalid username and password.

Expected:
Proper error message displayed.

---

TC_005
Verify login using locked_out_user.

Expected:
Login should fail with locked user message.

---

TC_006
Verify login without username.

Expected:
Username required message.

---

TC_007
Verify login without password.

Expected:
Password required message.

---

TC_008
Verify login with both fields empty.

Expected:
Username required message.