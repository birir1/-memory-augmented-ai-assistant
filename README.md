# Memory-Augmented Personal AI Assistant

## Project Overview

This project focuses on developing a context-aware AI assistant using locally deployed LLMs. The assistant maintains long-term memory to provide personalized and consistent user interactions.

---

## Features

* Local LLM deployment (Ollama / Gemma / LLaMA)
* Long-term memory using SQLite
* Context-aware responses
* Web-based chat interface
* Prompt optimization for natural interaction

---

## System Architecture

* **Frontend:** Web-based UI (chat interface)
* **Backend:** Flask API
* **Memory System:** SQLite database
* **LLM Engine:** Local inference (Ollama / LLaMA / Gemma)

---

## Team

| Name                       | Role                              |
| -------------------------- | --------------------------------- |
| Birir Sospeter Kipchirchir | Project Lead & System Integration |
| Brinner Chepngeno          | AI/LLM                    |
| Vincent Mwania Ngundi      | Backend & Memory Developer        |
| 정현경                        | Frontend & UX + LLM Support       |

---

# Branching Strategy

This project follows a **controlled branching model** to allow parallel development without interference.

## Main Branches

| Branch    | Purpose                             |
| --------- | ----------------------------------- |
| `main`    | Stable production-ready code        |
| `develop` | Integration branch for all features |

---

## Feature Branches

Each team member works independently on their assigned branch:

| Branch                       | Owner         | Description                                |
| ---------------------------- | ------------- | ------------------------------------------ |
| `feature/backend-memory`     | Vincent       | Memory system (SQLite, storage, retrieval) |
| `feature/backend-api`        | Vincent       | Flask APIs and backend services            |
| `feature/llm-setup`          | Brinner & 정현경 | Local LLM setup (Ollama, LLaMA, Gemma)     |
| `feature/prompt-engineering` | Brinner & 정현경 | Prompt tuning and response optimization    |
| `feature/frontend-ui`        | 정현경           | Web interface and user experience          |
| `feature/system-integration` | Sospeter      | Final system integration and deployment    |

---

# How to Work with Branches

## 1. Get Latest Updates

Always start from `develop`:

```bash
git checkout develop
git pull origin develop
```

---

## 2. Switch to Your Branch

```bash
git checkout feature/your-branch-name
```

Example:

```bash
git checkout feature/backend-memory
```

---

## 3. Work and Commit

```bash
git add .
git commit -m "Describe your changes"
```

---

## 4. Push Your Work

```bash
git push origin feature/your-branch-name
```

Example:

```bash
git push origin feature/backend-memory
```

---

## 5. Keep Your Branch Updated (Optional but Recommended)

```bash
git checkout develop
git pull origin develop
git checkout feature/your-branch-name
git merge develop
```

---

# Important Rules

*  Do NOT push directly to `main`
*  Do NOT push directly to `develop`
*  Do NOT merge other feature branches
*  Work ONLY on your assigned branch
*  Push frequently to avoid losing work

---

#  Integration Process (Handled by Project Lead)

During integration phase:

1. All feature branches will be merged into `develop`
2. Conflicts will be resolved centrally
3. Final tested version will be merged into `main`

---

#  Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/memory-augmented-ai-assistant.git
cd memory-augmented-ai-assistant

pip install -r requirements.txt
python src/backend/app.py
```

---

#  Milestones

| Phase                 | Timeline   |
| --------------------- | ---------- |
| Setup & Architecture  | Week 1–2   |
| LLM Deployment        | Week 3–4   |
| Memory System         | Week 5–6   |
| Backend APIs          | Week 7–8   |
| Frontend UI           | Week 9–10  |
| Integration & Testing | Week 11–12 |
| Final Deployment      | Week 13    |

---

#  Notes

* Keep commits clean and meaningful
* Avoid large, unstructured changes
* Document important functions and modules
* Log errors and test frequently

---

##  Goal

Build a **fully local, privacy-focused, memory-augmented AI assistant** capable of adapting to users over time and delivering meaningful, context-aware interactions.


## This is the full project structure with all the user roles.( Please check your responsibility and workspace)

memory-augmented-ai-assistant/
│
├── README.md
├── LICENSE
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── .env.example
│
├── docs/
│   ├── proposal.md
│   ├── architecture.md
│   ├── api_spec.md
│   ├── milestones.md
│   ├── team_roles.md
│
├── src/
│   │
│   ├── backend/                         #  Vincent (Backend)
│   │   ├── app.py
│   │   ├── config.py
│   │   │
│   │   ├── routes/
│   │   │   ├── chat_routes.py
│   │   │   ├── memory_routes.py
│   │   │
│   │   ├── services/
│   │   │   ├── llm_service.py
│   │   │   ├── memory_service.py
│   │   │   ├── embedding_service.py
│   │   │
│   │   ├── models/
│   │   │   ├── user_model.py
│   │   │   ├── memory_model.py
│   │   │
│   │   ├── database/
│   │   │   ├── db.py
│   │   │   ├── schema.sql
│   │   │
│   │   ├── utils/
│   │   │   ├── logger.py
│   │   │   ├── helpers.py
│   │
│   ├── llm/                             #  Brinner & 정현경 (LLM)
│   │   ├── inference/
│   │   │   ├── ollama_client.py
│   │   │   ├── local_model.py
│   │   │
│   │   ├── prompts/
│   │   │   ├── system_prompt.txt
│   │   │   ├── chat_prompt.txt
│   │   │
│   │   ├── tuning/
│   │   │   ├── parameters.py
│   │   │   ├── prompt_versions/
│   │   │
│   │   ├── evaluation/
│   │   │   ├── eval_metrics.py
│   │   │   ├── test_cases.json
│   │
│   ├── frontend/                        #  정현경 (Frontend)
│   │   ├── index.html
│   │   ├── styles/
│   │   │   ├── main.css
│   │   │
│   │   ├── scripts/
│   │   │   ├── app.js
│   │   │   ├── api.js
│   │
│   ├── integration/                     #  Sospeter (You)
│   │   ├── pipeline.py
│   │   ├── context_builder.py
│   │   ├── orchestrator.py
│
├── data/
│   ├── memory.db
│   ├── logs/
│   │   ├── app.log
│   │   ├── errors.log
│   │
│   ├── embeddings/
│
├── tests/
│   ├── test_backend.py
│   ├── test_memory.py
│   ├── test_llm.py
│
├── notebooks/
│   ├── experiments.ipynb
│   ├── prompt_testing.ipynb
│
├── scripts/
│   ├── setup_env.sh
│   ├── run_backend.sh
│   ├── run_frontend.sh
│
└── docker/
    ├── Dockerfile
    ├── docker-compose.yml