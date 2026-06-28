# EmpireOS Architecture

## System Overview

```
EmpireOS — Native macOS AI Assistant
├── macOS App (Swift 6.3+, AppKit + SwiftUI)
│   ├── Menu Bar (LSUIElement)
│   ├── Dashboard (3-column layout)
│   │   ├── Chat Zone
│   │   ├── Agent Room (184 agents)
│   │   ├── Coding Zone
│   │   └── Co-Work Zone
│   └── Services (Voice, Vision, WebSocket)
│
└── Python Backend (FastAPI)
    ├── LLM Proxy Router
    │   └── LM Studio → Gemini → OpenAI → Anthropic
    ├── Voice Pipeline (6 models)
    ├── Vision System
    ├── Agent Execution Engine
    ├── Computer Control
    ├── Website Generator
    └── Tool Integrations
```

## LLM Routing

The LLM proxy implements a fallback chain:

1. **LM Studio** (local) — Default for all simple tasks
2. **Gemini 2.5** — Optional upgrade via API key
3. **OpenAI** — Fallback when Gemini is unavailable
4. **Anthropic** — Final fallback

Each provider has independent circuit breaker, health monitoring, and auto-recovery.

## Voice Pipeline

6 models with WebSocket streaming:
- STT: Whisper.cpp (local) + OpenAI Whisper API
- TTS: Piper (local) + ElevenLabs + Edge TTS
- VAD: Silero VAD with barge-in detection
- Latency target: <500ms end-to-end

## Data Flow

```
User Query → Swift App → WebSocket → Python Backend
  → LLM Router → Provider → Streaming Response
  → Voice Pipeline (if voice mode)
  → Vision System (if screen context needed)
  → Agent Engine (if agent task)
  → Tool Registry (if tool execution needed)
```

## Security

- macOS App Sandbox with required entitlements
- API key authentication (HMAC)
- Computer control with 8-layer safety guard
- Screen recording privacy blocklist
- Audit logging for all control actions

## Deployment

### Local Development
```bash
uvicorn main:app --reload --port 8000
```

### Docker
```bash
docker build -t empireos .
docker run -p 8000:8000 --env-file .env empireos
```

### macOS LaunchAgent
```bash
# Auto-start on login
launchctl load ~/Library/LaunchAgents/com.empireos.backend.plist
```
