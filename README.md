# Nexus AI Agent (Mini Project - 1)

A lightweight full-stack AI agent project with:
- **Python backend** (FastAPI) for planning + execution
- **React frontend** for submitting goals and viewing results
- **Tool-based execution pipeline** with browser search support and safe fallbacks

The project is designed to demonstrate a clean, modular agent loop:
`Goal -> Plan -> Execute Steps -> Return Results`

## Project Intent

This system accepts a user goal, generates a structured plan using an LLM, executes each step through tool adapters, and returns a machine-readable response that the UI displays.

Primary objective:
- Use real API-based planning when API key and credits are valid.
- Use mock/fallback behavior only when required (missing/invalid key, exhausted quota, or tool-level runtime fallback).

## Repository Structure

```text
Mini Project - 1/
|- README.md
|- requirements.txt
`- ai-agent/
   |- api/
   |  `- main.py               # FastAPI app and /run-agent endpoint
   |- planner/
   |  `- planner.py            # LLM planning + fallback logic
   |- executor/
   |  `- executor.py           # Tool selection and execution strategy
   |- control_loop/
   |  `- loop.py               # Step-by-step loop with retry and limits
   |- tools/
   |  |- base_tool.py          # Tool contract/interface
   |  |- browser_tool.py       # Browser tool wrapper
   |  `- browser_adapter.py    # Playwright browser search implementation
   |- schemas/
   |  |- action_schema.py      # Action schema
   |  `- plan_schema.py        # Plan/Step schema
   |- config/
   |  `- settings.py           # Environment-driven settings
   |- .env                     # Local environment variables (not for commit)
   `- ai-agent-ui/
      |- src/App.js            # Main frontend screen and API call
      `- package.json          # Frontend dependencies/scripts
```

## How the System Works

1. Frontend posts a `goal` to backend endpoint `POST /run-agent`.
2. `Planner` generates a structured plan (`steps[]`) with OpenAI API.
3. `run_loop` executes each step using `Executor`.
4. `Executor` selects a tool/mode and runs it.
5. Backend returns both `plan` and `results` as JSON.

## API and Fallback Behavior

Planner behavior in `ai-agent/planner/planner.py`:
- If API key is available and valid, planning uses OpenAI.
- If API key is missing, invalid, or quota is exhausted, planner returns a mock plan fallback.
- Non-auth/non-quota runtime errors are raised instead of silently hiding real failures.

This keeps API as the primary mode and mock as a controlled safety fallback.

## Prerequisites

- Python 3.10+ recommended
- Node.js 18+ and npm
- Internet access for API/tool usage
- OpenAI API key (for primary planning mode)

## Setup Instructions

### 1) Backend setup (PowerShell)

From repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

Create/update `ai-agent/.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
MAX_STEPS=20
RETRY_LIMIT=3
ENABLE_BROWSER_TOOL=true
ENABLE_GOOGLE_TOOL=false
```

Run backend:

```powershell
cd ai-agent
uvicorn api.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

### 2) Frontend setup

In a new terminal:

```powershell
cd ai-agent\ai-agent-ui
npm install
npm start
```

Frontend URL: `http://localhost:3000`

## Running the Project

1. Start backend (`uvicorn api.main:app --reload` inside `ai-agent`).
2. Start frontend (`npm start` inside `ai-agent/ai-agent-ui`).
3. Enter a goal in UI and click **Run Agent**.
4. Inspect JSON output (`plan` + `results`) in the frontend.

## Key Files and Responsibilities

- `ai-agent/api/main.py`
  - Exposes `POST /run-agent`.
  - Creates planner/executor and orchestrates end-to-end run.

- `ai-agent/planner/planner.py`
  - Converts user goal into structured plan.
  - Contains API-first behavior and fallback conditions.

- `ai-agent/control_loop/loop.py`
  - Executes steps sequentially with max-step and retry controls.

- `ai-agent/executor/executor.py`
  - Chooses strategy/tool for each step and returns normalized result.

- `ai-agent/tools/browser_adapter.py`
  - Uses Playwright for real browser-backed search.
  - Returns adapter-level fallback text if runtime browsing fails.

- `ai-agent/ai-agent-ui/src/App.js`
  - Collects user goal and calls backend endpoint.
  - Displays result payload in formatted JSON.

## API Contract

### Request
`POST /run-agent`

```json
{
  "goal": "Find latest information about X"
}
```

### Response

```json
{
  "plan": {
    "steps": [
      {
        "id": "1",
        "task": "Search for information",
        "tool": "browser",
        "input": "..."
      }
    ]
  },
  "results": [
    {
      "status": "success",
      "tool": "browser",
      "action": "search",
      "result": "..."
    }
  ]
}
```

## Troubleshooting

- **Frontend shows connection error**
  - Confirm backend is running on `127.0.0.1:8000`.

- **Planner not using API**
  - Verify `OPENAI_API_KEY` in `ai-agent/.env`.
  - Check API key validity and quota/credits.

- **Browser search returns mock-like text**
  - Ensure Playwright browsers are installed (`playwright install`).
  - Confirm environment/network allows browser automation.

## Notes for Development

- Keep `.env` private and never commit secrets.
- Keep backend and frontend terminals separate while developing.
- Extend tools by adding new classes in `ai-agent/tools/` and wiring them in `executor.py`.

