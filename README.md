# EmpireOS Master

> **Version**: 1.0.0 | **Date**: 2026-06-28
> **Platform**: macOS 14+ (Sonoma/Sequoia) | **Language**: Swift 6.3+ / Python 3.11+
> **UI Framework**: AppKit + SwiftUI Hybrid | **Backend**: FastAPI

---

## What is EmpireOS?

**EmpireOS Master** is the unified native macOS application combining **BAKER OS v3** (184 agents, 14 divisions) and **EmpireOS Native macOS App** into one master mega application.

It is a Claude-like AI assistant dashboard with:
- **Voice Interaction** — Speak back with very low latency, interruptible
- **Vision** — Sees your screen in real-time
- **Computer Control** — Takes control of your Mac (mouse, keyboard, apps)
- **184 AI Agents** — Across 14 divisions, selectable for any task
- **Website Generator** — Creates and deploys React/Next.js websites
- **Tool Integrations** — Image generation, video generation, ComfyUI, web search
- **Chat Zone** — Full markdown, code highlighting, streaming responses
- **Coding Zone** — Code editor with syntax highlighting + integrated terminal
- **Agent Room** — Browse, search, activate agents. Agents speak together
- **Co-Work Zone** — Shared whiteboard, Kanban board, team collaboration

---

## Architecture

```
EmpireOS — Native macOS App (Swift 6.3+, AppKit + SwiftUI)
│
├── Menu Bar App (LSUIElement — no dock icon, star ★ in menu bar)
├── 3-Column Dashboard (Sidebar | Main Content | Context Panel)
│   ├── Chat Zone
│   ├── Agent Room (184 agents, 14 divisions)
│   ├── Coding Zone
│   ├── Co-Work Zone
│   └── Settings
│
└── Python Backend (FastAPI + WebSocket)
    ├── LLM Proxy Router (LM Studio → Gemini → OpenAI → Anthropic)
    ├── Voice Pipeline (6 models, WebSocket streaming)
    ├── Vision System (screen capture + AI analysis)
    ├── Agent Execution Engine (184 agents)
    ├── Computer Control (macOS automation)
    ├── Website Generator (React/Next.js/Vite)
    └── Tool Integrations (image, video, ComfyUI, search)
```

---

## Project Structure

```
empire-os-master/
├── README.md                          # This file
├── BUILD.md                           # Developer build guide
├── ARCHITECTURE.md                    # Full architecture document
├── API.md                             # API reference
├── SETUP.md                           # Setup instructions
│
├── apps/
│   └── macos/                         # Native macOS App
│       ├── Package.swift              # SPM manifest
│       ├── EmpireOS.xcodeproj/        # Xcode project
│       ├── Info.plist                 # App bundle config
│       ├── EmpireOS.entitlements      # Security capabilities
│       │
│       ├── app-shell/                 # App lifecycle, menu bar, windows
│       │   ├── EmpireOSApp.swift
│       │   ├── MenuBarController.swift
│       │   ├── WindowManager.swift
│       │   ├── DashboardWindow.swift
│       │   ├── ContentView.swift
│       │   ├── Constants.swift
│       │   └── Extensions.swift
│       │
│       ├── dashboard/                 # Main Claude-like UI
│       │   ├── DashboardView.swift
│       │   ├── SidebarView.swift
│       │   ├── MainContentView.swift
│       │   ├── ContextPanelView.swift
│       │   ├── TopBarView.swift
│       │   ├── InputBarView.swift
│       │   ├── Theme.swift
│       │   └── ZoneRouter.swift
│       │
│       ├── chat-zone/                 # Chat interface
│       │   ├── ChatZoneView.swift
│       │   ├── MessageBubbleView.swift
│       │   ├── CodeBlockView.swift
│       │   ├── MessageListView.swift
│       │   ├── ConversationListView.swift
│       │   ├── MessageInputView.swift
│       │   ├── TypingIndicatorView.swift
│       │   ├── MarkdownRenderer.swift
│       │   ├── ChatViewModel.swift
│       │   └── ConversationModel.swift
│       │
│       ├── agent-room/                # 184 agents, 14 divisions
│       │   ├── AgentRoomView.swift
│       │   ├── AgentModels.swift
│       │   ├── AgentRoomViewModel.swift
│       │   ├── DivisionSelectorView.swift
│       │   ├── AgentCardView.swift
│       │   ├── AgentGridView.swift
│       │   ├── AgentDetailView.swift
│       │   ├── AgentActivationView.swift
│       │   ├── ActiveAgentsPanelView.swift
│       │   ├── AgentTeamBuilderView.swift
│       │   └── AgentSearchBarView.swift
│       │
│       ├── coding-zone/               # Code editor + terminal
│       │   ├── CodingZoneView.swift
│       │   ├── CodeEditorView.swift
│       │   ├── FileTreeView.swift
│       │   ├── TerminalView.swift
│       │   ├── SyntaxHighlighter.swift
│       │   ├── EditorTabBarView.swift
│       │   ├── BreadcrumbView.swift
│       │   ├── CodeRunner.swift
│       │   ├── EditorViewModel.swift
│       │   └── FileModels.swift
│       │
│       └── co-work-zone/              # Collaborative workspace
│           ├── CoWorkZoneView.swift
│           ├── SharedCanvasView.swift
│           ├── DrawingEngine.swift
│           ├── ParticipantListView.swift
│           ├── TeamChatPanelView.swift
│           ├── CursorTrackingView.swift
│           ├── TaskBoardView.swift
│           ├── ActivityFeedView.swift
│           ├── CoWorkViewModel.swift
│           └── CoWorkModels.swift
│
├── server/                            # Python Backend
│   ├── main.py                        # FastAPI entry point
│   ├── config.py                      # Configuration
│   ├── models.py                      # Pydantic models
│   ├── auth.py                        # Authentication
│   ├── logger.py                      # Structured logging
│   ├── llm_router.py                  # Multi-provider LLM routing
│   ├── voice_pipeline.py              # TTS/STT service
│   ├── vision_service.py              # Screen analysis
│   ├── agent_engine.py                # Agent execution
│   ├── tool_registry.py               # Tool plugin system
│   ├── websocket_manager.py           # WebSocket connections
│   ├── requirements.txt               # Dependencies
│   │
│   ├── providers/                     # LLM providers
│   │   ├── lmstudio.py
│   │   ├── gemini.py
│   │   ├── openai.py
│   │   └── anthropic.py
│   │
│   ├── voice/                         # Voice pipeline
│   │   ├── voice_service.py
│   │   ├── stt_engine.py
│   │   ├── tts_engine.py
│   │   ├── vad_engine.py
│   │   ├── audio_buffer.py
│   │   ├── audio_utils.py
│   │   ├── noise_suppressor.py
│   │   ├── voice_models.py
│   │   └── voice_config.py
│   │
│   ├── vision/                        # Vision system
│   │   ├── vision_service.py
│   │   ├── screen_capture.py
│   │   ├── image_analysis.py
│   │   ├── ai_vision.py
│   │   ├── frame_streamer.py
│   │   ├── privacy_guard.py
│   │   ├── vision_models.py
│   │   └── vision_config.py
│   │
│   ├── computer-control/              # macOS automation
│   │   ├── computer_control.py
│   │   ├── mouse_controller.py
│   │   ├── keyboard_controller.py
│   │   ├── app_controller.py
│   │   ├── window_manager.py
│   │   ├── accessibility_api.py
│   │   ├── safety_guard.py
│   │   ├── audit_logger.py
│   │   └── ...
│   │
│   ├── website-generator/             # Website generation
│   │   ├── website_generator.py
│   │   ├── template_engine.py
│   │   ├── code_generator.py
│   │   ├── preview_server.py
│   │   ├── deploy_service.py
│   │   └── templates/
│   │
│   └── tools/                         # Tool integrations
│       ├── tool_registry.py
│       ├── image_generation.py
│       ├── video_generation.py
│       ├── comfyui_client.py
│       ├── web_search.py
│       ├── code_executor.py
│       └── browser_tool.py
│
└── docs/                              # Documentation
    ├── ARCHITECTURE.md
    ├── API.md
    ├── SETUP.md
    └── ENV.example
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| macOS App | Swift 6.3+, AppKit + SwiftUI Hybrid |
| Build System | Xcode 15+, Swift Package Manager |
| Backend | Python 3.11+, FastAPI |
| Real-time | WebSocket (bidirectional) |
| Voice | Whisper.cpp, Piper TTS, ElevenLabs, Silero VAD |
| Vision | Core Graphics, Vision framework, AI models |
| LLM Routing | Custom proxy with fallback chain |
| Storage | Core Data + UserDefaults + SQLite |
| Networking | URLSession + Starscream |

---

## Quick Start

### Prerequisites
- macOS 14+ (Sonoma/Sequoia)
- Xcode 15+
- Python 3.11+
- 8GB+ RAM (optimized for MacBook Air M3)

### Build macOS App
```bash
cd apps/macos
open EmpireOS.xcodeproj
# In Xcode: Cmd+B to build, Cmd+R to run
```

### Run Backend
```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Configure API Keys
```bash
cp docs/ENV.example .env
# Edit .env with your API keys:
# - LM Studio (local, default)
# - Gemini 2.5 (optional)
# - OpenAI (optional)
# - Anthropic (optional)
```

---

## Features

### 8 Core Zones

| Zone | Description | Status |
|------|-------------|--------|
| **Chat** | Claude-like chat with markdown, code, streaming | ✅ |
| **Agent Room** | 184 agents across 14 divisions | ✅ |
| **Coding Zone** | Code editor + terminal + file explorer | ✅ |
| **Co-Work Zone** | Whiteboard, Kanban, team chat | ✅ |
| **Voice** | 6 models, WebSocket streaming, interruption | ✅ |
| **Vision** | Screen capture + AI analysis | ✅ |
| **Computer Control** | Mouse, keyboard, app automation | ✅ |
| **Website Generator** | React/Next.js/Vite + deploy | ✅ |

### Voice Pipeline (6 Models)
| Model | Role | Type |
|-------|------|------|
| Whisper.cpp | Primary STT | Local |
| OpenAI Whisper | Fallback STT | Cloud |
| Silero VAD | Barge-in detection | Local |
| Piper TTS | Primary TTS | Local |
| ElevenLabs Turbo | Premium TTS | Cloud |
| Edge TTS | Free fallback TTS | Cloud |

### LLM Fallback Chain
```
LM Studio (local) → Gemini 2.5 → OpenAI → Anthropic
```

---

## Stats

| Metric | Value |
|--------|-------|
| **Total Files** | 252 |
| **Total Lines** | 87,417 |
| **Swift Code** | 30,619 lines (59 files) |
| **Python Code** | 36,422 lines (69 files) |
| **Documentation** | 6,208 lines |
| **Agents** | 184 across 14 divisions |
| **API Endpoints** | 35+ REST + 2 WebSocket |

---

## License

MIT License — EmpireOS Master is open source.

---

*EmpireOS Master — Built with 150+ agents across 14 divisions. Resilience is not survival. It is self-healing intelligence.*
