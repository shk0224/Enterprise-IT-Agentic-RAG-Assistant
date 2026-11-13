
from pathlib import Path

# Current working directory
root = Path(".")

# Folders to create
folders = [
    "app",
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "static/css",
    "static/js",
    "uploads",
    "tests",
]

# Files to create
files = [
    "app/__init__.py",
    "app/main.py",
    "ingest_sample_kb.py",
    "requirements.txt",
    "run.py",
    ".env",
    "app/api/__init__.py",
    "app/api/routes.py",
    "app/core/__init__.py",
    "app/core/config.py",
    "app/core/logging.py",
    "app/rag/__init__.py",
    "app/rag/state.py",
    "app/rag/vectorstore.py",
    "app/rag/workflow.py",
    "app/services/__init__.py",
    "app/services/main.py",
    "static/css/style.css",
    "static/js/app.js",
    "templates/index.html",
]

# Create folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

# Create files
for file in files:
    (root / file).touch(exist_ok=True)

print("Project structure created successfully.")
