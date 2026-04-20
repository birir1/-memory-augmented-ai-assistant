import os

BASE_DIR = "memory-augmented-ai-assistant"

# =========================
# Folder structure
# =========================
folders = [
    "",
    "docs",
    "src/backend/routes",
    "src/backend/services",
    "src/backend/models",
    "src/backend/database",
    "src/backend/utils",
    "src/llm/inference",
    "src/llm/prompts",
    "src/llm/tuning/prompt_versions",
    "src/llm/evaluation",
    "src/frontend/styles",
    "src/frontend/scripts",
    "src/integration",
    "data/logs",
    "data/embeddings",
    "tests",
    "notebooks",
    "scripts",
    "docker"
]

# =========================
# Files to create
# =========================
files = {
    "README.md": "# Memory-Augmented AI Assistant\n",
    "LICENSE": "",
    "requirements.txt": "",
    "requirements-dev.txt": "",
    ".gitignore": "__pycache__/\n.env\nvenv/\ndata/logs/\n",
    ".env.example": "FLASK_ENV=development\nPORT=5000\n",

    # Docs
    "docs/proposal.md": "",
    "docs/architecture.md": "",
    "docs/api_spec.md": "",
    "docs/milestones.md": "",
    "docs/team_roles.md": "",

    # Backend
    "src/backend/app.py": """from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp
from routes.memory_routes import memory_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)
app.register_blueprint(memory_bp)

if __name__ == "__main__":
    app.run(debug=True)
""",

    "src/backend/config.py": "",
    "src/backend/routes/chat_routes.py": "",
    "src/backend/routes/memory_routes.py": "",
    "src/backend/services/llm_service.py": "",
    "src/backend/services/memory_service.py": "",
    "src/backend/services/embedding_service.py": "",
    "src/backend/models/user_model.py": "",
    "src/backend/models/memory_model.py": "",
    "src/backend/database/db.py": "",
    "src/backend/database/schema.sql": "",
    "src/backend/utils/logger.py": "",
    "src/backend/utils/helpers.py": "",

    # LLM
    "src/llm/inference/ollama_client.py": "",
    "src/llm/inference/local_model.py": "",
    "src/llm/prompts/system_prompt.txt": "You are a helpful AI assistant.",
    "src/llm/prompts/chat_prompt.txt": "",
    "src/llm/tuning/parameters.py": "",
    "src/llm/evaluation/eval_metrics.py": "",
    "src/llm/evaluation/test_cases.json": "[]",

    # Frontend
    "src/frontend/index.html": """<!DOCTYPE html>
<html>
<head><title>AI Assistant</title></head>
<body>
<h1>AI Assistant</h1>
<input id="input" />
<button onclick="send()">Send</button>
<div id="chat"></div>
<script src="scripts/app.js"></script>
</body>
</html>
""",
    "src/frontend/styles/main.css": "",
    "src/frontend/scripts/app.js": "",
    "src/frontend/scripts/api.js": "",

    # Integration
    "src/integration/pipeline.py": "",
    "src/integration/context_builder.py": "",
    "src/integration/orchestrator.py": "",

    # Data placeholders
    "data/memory.db": "",
    "data/logs/app.log": "",
    "data/logs/errors.log": "",

    # Tests
    "tests/test_backend.py": "",
    "tests/test_memory.py": "",
    "tests/test_llm.py": "",

    # Notebooks
    "notebooks/experiments.ipynb": "",
    "notebooks/prompt_testing.ipynb": "",

    # Scripts
    "scripts/setup_env.sh": "#!/bin/bash\n",
    "scripts/run_backend.sh": "#!/bin/bash\n",
    "scripts/run_frontend.sh": "#!/bin/bash\n",

    # Docker
    "docker/Dockerfile": "",
    "docker/docker-compose.yml": ""
}


# =========================
# Create folders
# =========================
for folder in folders:
    path = os.path.join(BASE_DIR, folder)
    os.makedirs(path, exist_ok=True)

# =========================
# Create files
# =========================
for file_path, content in files.items():
    full_path = os.path.join(BASE_DIR, file_path)

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully!")