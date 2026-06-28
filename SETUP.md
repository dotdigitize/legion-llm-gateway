# Setup

## Backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Run tests:

```bash
python -m pytest
```

## Frontend

```bash
npm install
npm run dev
```

Build:

```bash
npm run build
```

## Ollama

Ollama is optional. The gateway returns deterministic fallback output when `ENABLE_OLLAMA=false`.

```bash
ENABLE_OLLAMA=true
OLLAMA_BASE_URL=http://localhost:11434
```

## Database

MariaDB is optional for tests and local fallback operation. Keep `ENABLE_DATABASE=false` for in-memory runtime state and sample read-only operational data.

See [db/README.md](db/README.md).
