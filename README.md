# 🚀 Nexus AI Agent System

A modular full-stack AI agent that can **plan, decide, and execute tasks** using multi-tier execution strategies (fast responses + real browser interaction).

---

## ✨ Highlights

* 🧠 **AI Planning System** (LLM + structured steps)
* ⚙️ **Execution Engine** with control loop + retries
* 🌐 **Browser Automation** using Playwright
* ⚡ **Fast Mode** for instant responses
* 🔌 **Tool-based Architecture** (plug-and-play tools)
* 🛡️ **Fallback-safe system** (never crashes)

---

## 🧩 System Overview

```text
User Input
   ↓
Planner (LLM / Mock)
   ↓
Executor (Strategy Layer)
   ↓
Tools (Browser / Fast Mode)
   ↓
Results
```

---

## 🎯 Problem This Solves

Most AI apps:

* Only generate responses ❌
* Cannot execute real-world tasks ❌

This system introduces:

> ✅ **AI that can plan + act + execute using tools**

---

## 🏗️ Architecture

```text
backend/
  ├── api/              # FastAPI endpoints
  ├── planner/          # Goal → Plan
  ├── executor/         # Strategy + tool selection
  ├── control_loop/     # Step execution + retry
  ├── tools/            # Tool implementations
  ├── schemas/          # Data contracts
  └── config/           # Environment settings

frontend/
  └── React UI for interaction
```

---

## ⚙️ How It Works

1. User submits a goal from frontend
2. Planner generates structured steps
3. Control loop executes steps sequentially
4. Executor selects execution strategy
5. Tools perform real or fallback actions
6. Results returned to UI

---

## 🧪 Example

### Input

```json
{
  "goal": "Find latest AI tools"
}
```

### Output

```json
{
  "plan": {...},
  "results": [...]
}
```

---

## ⚡ Execution Modes

| Mode            | Description                             |
| --------------- | --------------------------------------- |
| ⚡ Fast Mode     | Instant response (no browser)           |
| 🌐 Browser Mode | Real-world search via Playwright        |
| 🧠 Future Mode  | Advanced agents (browser-harness, APIs) |

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **Frontend:** React
* **Automation:** Playwright
* **AI:** OpenAI (optional / fallback supported)

---

## 🚀 Setup

### Backend

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

Create `.env`:

```env
OPENAI_API_KEY=your_key_here
MAX_STEPS=20
RETRY_LIMIT=3
```

Run:

```bash
uvicorn api.main:app --reload
```

---

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🔗 API Endpoint

```
POST /run-agent
```

---

## 🛡️ Fallback Design

* No API key → mock planning
* Browser failure → safe fallback
* System never crashes

---

## 🧠 Key Concepts Implemented

* Control Loop Execution
* Strategy Layer Decision Making
* Tool Abstraction
* Adapter Pattern
* Multi-tier Execution System

---

## 🔮 Future Scope

* 🔗 Google Workspace Integration
* 🌍 Browser Harness Integration
* 🧠 Memory (RAG) Layer
* 🤖 Autonomous Agent Behavior

---

## 📌 Notes

* `.env` is excluded for security
* Designed for extensibility
* Built with system-level thinking

---

## 👨‍💻 Author

Faheem

---

## ⭐ If you found this useful

Give this repo a star 🌟
