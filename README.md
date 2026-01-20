# 🧪 UI Automation Framework (Python + Selenium + Pytest)

## 📌 Project Overview

This project is a **scalable, enterprise-style UI automation framework** built using **Python, Selenium, and Pytest**.

The framework focuses on **stability, maintainability, and flakiness reduction**, making it suitable for dynamic, production-grade applications.

---

## 🎯 Key Objectives

* Build a **professional UI automation framework**
* Eliminate flaky tests using **explicit waits (Smart Waits)**
* Follow **Page Object Model (POM)** for maintainability
* Support **data-driven testing**
* Demonstrate **end-to-end user journeys**

---

## 🧰 Tech Stack

* **Language:** Python 3
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** Pytest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Pytest HTML reports

---

## 🌐 Application Under Test

* **Sauce Demo (Swag Labs)** – E-commerce application

  * Login
  * Product selection
  * Product removal
  * Cart
  * Checkout

---

## 📂 Project Structure

```
UI-Automation-Framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_end_to_end_checkout.py
│
├── utils/
│   ├── driver_utilities.py
│   ├── config.py
│   └── logger.py
│
├── reports/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Framework Design Highlights

### ✅ Page Object Model (POM)

* Each web page is represented as a **separate Python class**
* UI locators and actions are isolated from test logic
* Improves readability and reduces maintenance effort

### ✅ BasePage with Smart Waits (Critical)

* Centralized **explicit waits** using `WebDriverWait`
* Handles dynamic elements and asynchronous loading
* Significantly reduces flaky test failures

### ✅ Data-Driven Testing

* Test data (URLs, credentials, browser) stored in `config.py`
* No hardcoded values inside test scripts
* Easy environment and user switching

---

## 🧪 Test Coverage

### ✔ Login Tests

* Valid login verification

### ✔ End-to-End E-commerce Flow

* Login
* Add product to cart
* Remove product from cart
* Checkout process
* Order confirmation validation

These tests simulate **real customer journeys**, not isolated UI actions.

---

## ▶️ How to Run Tests Locally

### 1️⃣ Clone the Repository

```bash
git clone UI-Automation-Framework_Python-Selenium-Pytest
cd UI-Automation-Framework_Python-Selenium-Pytest
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Tests

```bash
pytest
```

### 5️⃣ Generate HTML Report

```bash
pytest --html=reports/report.html
```

## 🧾 Why This Project Is Enterprise-Ready

This framework demonstrates:

* Clean architecture & separation of concerns
* Explicit waits to handle flaky UI behavior
* CI/CD automation mindset
* Real-world E2E business flows
* Readable, maintainable test code

