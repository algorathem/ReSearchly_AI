# Einstyn – Motia Research Workflow (Python)

Run the Motia workbench and research flow locally.

## Prereqs
- Node.js 18+
- Python 3.11+ available on PATH

## Setup
```bash
npm install              # install Motia CLI locally
npx motia install        # creates python_modules venv and installs Python deps
```

## Env vars
Create `.env` in the repo root (example):
```
FIRECRAWL_API_KEY=your_firecrawl_api_key
FIRECRAWL_API_URL=          # optional
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o
FIRECRAWL_CONCURRENCY_LIMIT=2
```

## Run
```bash
npm run dev
```
Then open http://localhost:3000 for the Motia workbench.

## Common hiccups
- Port in use (3000 or 24678): stop the other process (e.g., `Get-NetTCPConnection -LocalPort 3000,24678` then `taskkill /PID <pid> /F`) and rerun `npm run dev`.
- Missing Python venv: rerun `npx motia install`.

