# Sauce Demo Selenium Automation

Test automation project for [Sauce Demo] **Selenium WebDriver**, **Behave** (Cucumber para Python) and **pytest**.


## 📦 Requirements

- Python 3.8 or superior
- Git


![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![pytest](https://img.shields.io/badge/pytest-7.0+-green.svg)
![Behave](https://img.shields.io/badge/behave-1.2+-orange.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-red.svg)

## 🚀 Installation and configuratio 

### 1. Clone the repository 

``` bash ````
git clone <url-do-repositorio>
cd sauce-demo-automation


### Venv

- ``` python -m venv .venv ```
- ``` .venv\Scripts\Activate.ps1 ```
- ``` Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ```

### Install Selenium

- ``` pip install selenium ```
- ``` pip install webdriver-manager ```

### Pytest

- ``` pip install pytest ```
- ``` pip install pytest-xdist ``` To execute parallel test
- ``` pip install pytest-html ``` To generate a HTML report

### Cucumber

- ``` pip install behave ```


sauce-demo-selenium-automation/
├── features/                   # .feature (Gherkin) files and steps from Behave
│   ├── login.feature
│   ├── checkout.feature
│   └── steps/
│       ├── login_steps.py
│       └── checkout_steps.py
├── pages/                      # Page Objects (POM): elements and actions from each page
│   ├── login_page.py
│   ├── home_page.py
│   ├── checkout_page.py
│   └── base_page.py
├── tests/                      # Tests with pytest
│   ├── test_login.py
│   └── test_checkout.py
├── utilities/                  # Reusable helper functions
│   ├── driver_manager.py
│   ├── config_reader.py
│   └── logger.py
├── configs/                    # Configuration files (URLs, credentiais, etc.) 
│   └── config.ini
├── reports/                    # Test reports (HTML, Allure, etc.)
│   └── report.html
├── screenshots/                # Screenshots fom fails
├── conftest.py                 # Globals Fixtures from pytest
├── environment.py              # Hooks configuration from Behave (before_all, after_all)
├── pytest.ini                  # Pytest configurations (markers, etc.)
└── requirements.txt            # Project dependencies