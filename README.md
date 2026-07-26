# 🚀 SauceDemo Selenium Python Automation Framework

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-success)
![Pytest](https://img.shields.io/badge/Pytest-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-ready Selenium Automation Framework built with **Python**, **Pytest**, and the **Page Object Model (POM)**. The framework is designed to be scalable, maintainable, and CI/CD-ready, supporting cross-browser execution, environment-based configuration, automatic screenshots on failure, logging, and HTML reporting.

---

# 📌 Features

- ✅ Selenium 4
- ✅ Python 3
- ✅ Pytest Test Framework
- ✅ Page Object Model (POM)
- ✅ Cross Browser Testing
  - Chrome
  - Firefox
  - Edge
- ✅ Headless Execution
- ✅ Environment Variable Configuration (.env)
- ✅ Automatic WebDriver Management
- ✅ HTML Test Reports
- ✅ Screenshots on Test Failure
- ✅ Logging
- ✅ GitHub Actions CI/CD Integration
- ✅ Clean Project Structure
- ✅ Easy to Extend

---

# 🏗 Framework Architecture

```
Tests
   │
   ▼
Page Objects
   │
   ▼
Driver Factory
   │
   ▼
Selenium WebDriver
   │
   ▼
Browser
```

---

# 📂 Project Structure

```
SauceDemo-Selenium-Python-Framework
│
├── config/
│   ├── config.py
│   └── credentials.py
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── test_data/
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   ├── screenshot.py
│   └── excel_reader.py
│
├── logs/
├── reports/
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── selenium.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Selenium | Browser Automation |
| Pytest | Test Framework |
| webdriver-manager | Driver Management |
| python-dotenv | Environment Variables |
| pytest-html | HTML Reporting |
| GitHub Actions | Continuous Integration |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/hassnain11/SauceDemo-Selenium-Python-Framework.git
```

Navigate to the project

```bash
cd SauceDemo-Selenium-Python-Framework
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root.

Example:

```env
BASE_URL=https://www.saucedemo.com/
BROWSER=chrome
HEADLESS=False
IMPLICIT_WAIT=10
```

---

# ▶️ Running Tests

Run all tests

```bash
pytest
```

Run a specific test

```bash
pytest tests/test_login.py
```

Run tests in headless mode

```bash
pytest
```

(Set `HEADLESS=True` in the `.env` file.)

Run using Firefox

```env
BROWSER=firefox
```

Run using Edge

```env
BROWSER=edge
```

---

# 📊 Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open

```
reports/report.html
```

to view the report.

---

# 📸 Screenshots on Failure

Whenever a test fails, the framework automatically captures a screenshot and saves it inside the `screenshots/` directory.

This helps in quickly identifying UI failures during execution.

---

# 📝 Logging

The framework logs important execution details including:

- Browser initialization
- Test execution
- Navigation
- Failures
- Screenshot paths

Logs are stored inside the `logs/` directory.

---

# 🌐 Cross Browser Support

Supported browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

Browser selection is managed through the `.env` configuration.

---

# 🤖 Continuous Integration

GitHub Actions automatically:

- Installs project dependencies
- Starts the browser in headless mode
- Executes all test cases
- Generates execution reports

This ensures every push is automatically validated.

---

# 📈 Current Framework Capabilities

- Page Object Model
- Driver Factory Pattern
- Environment-based Configuration
- Cross Browser Testing
- Headless Execution
- Automatic Driver Management
- HTML Reporting
- Screenshot Capture
- Logging
- CI/CD Pipeline
- Scalable Framework Design

---

# 🔮 Future Enhancements

- Allure Reports
- Parallel Execution (pytest-xdist)
- Docker Support
- Jenkins Pipeline
- Browser Matrix Testing
- Slack Notifications
- Email Test Reports

---

# 👨‍💻 Author

**Muhammad Hassnain Raza**

Software Quality Assurance Engineer

GitHub: https://github.com/hassnain11


---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps support the project and motivates further improvements.
