# LLM_LITE_APP


## Prerequisites
___
**YOU MUST rename any file with `.TEMPLATE_env` to `.env.local`, and ensure that you update the values correctly if needed.**
___


1. **Install Python**
   Ensure that Python is installed on your system. You can install Python using one of the following methods:
   - **Official Website**: [Download Python](https://www.python.org/downloads/)
   - **Homebrew (macOS)**:
     ```bash
     brew install python
     ```
   - **Chocolatey (Windows)**:
     ```bash
     choco install python
     ```


## Setup Instructions
### 1. Create a Virtual Environment

Creating a virtual environment ensures that your project's dependencies are isolated.

```bash
python -m venv .env
```

### 2. Activate the Virtual Environment
#### For macOS and Linux:

```bash
source .env/bin/activate
```

#### For Windows:
```bash
.env\Scripts\activate
```

### 3. Install Required Packages
Ensure that your virtual environment is activated, then install the required packages:

```bash
pip install -r backend/python/commons/requirements.in
# better via .txt
# pip install -r backend/python/commons/requirements.txt 
```

```bash
docker-compose up rag_app qdrant_db pgsql  --build

```


```bash
python -m notebook
```


## Ckeck Run
Check If App Working 
### FastAPI
- http://127.0.0.1:9876/docs
### qdrant_db
- http://127.0.0.1:6333/dashboard
