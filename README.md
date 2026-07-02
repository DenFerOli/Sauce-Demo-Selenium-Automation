# Sauce Demo Selenium Automation

Test automation project using **Selenium WebDriver**, **Behave** (Cucumber para Python) and **pytest**.


## 📦 Requirements

- Python 3.8 or superior
- Git

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




meu_projeto_de_testes/
├── features/                   # Arquivos .feature (Gherkin) e steps do Behave
│   ├── login.feature
│   ├── cadastro.feature
│   └── steps/
│       ├── login_steps.py
│       └── cadastro_steps.py
├── pages/                      # Page Objects (POM): elementos e ações de cada página [citation:1][citation:2][citation:3]
│   ├── login_page.py
│   ├── home_page.py
│   └── base_page.py
├── tests/                      # Testes com pytest (para testes mais técnicos, se houver) [citation:1][citation:2][citation:3]
│   ├── test_login.py
│   └── test_cadastro.py
├── utilities/                  # Funções auxiliares reutilizáveis [citation:1][citation:3][citation:4]
│   ├── driver_manager.py
│   ├── config_reader.py
│   └── logger.py
├── configs/                    # Arquivos de configuração (URLs, credenciais, etc.) [citation:3][citation:5]
│   └── config.ini
├── reports/                    # Relatórios de teste (HTML, Allure, etc.) [citation:1][citation:3][citation:4]
│   └── report.html
├── screenshots/                # Screenshots capturados em caso de falha [citation:1][citation:3][citation:4]
├── conftest.py                 # Fixtures globais do pytest [citation:2][citation:4][citation:5]
├── environment.py              # Hooks de configuração do Behave (before_all, after_all) [citation:5]
├── pytest.ini                  # Configurações do pytest (markers, etc.) [citation:3][citation:4][citation:5]
└── requirements.txt            # Dependências do projeto