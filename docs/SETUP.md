# EmpireOS Setup Guide

## Prerequisites

- **macOS**: 14+ (Sonoma/Sequoia)
- **Xcode**: 15+ with Swift 6.3+
- **Python**: 3.11+
- **RAM**: 8GB minimum (optimized for MacBook Air M3)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/abdalla-holmes/empire-os-master.git
cd empire-os-master
```

### 2. Setup Python Backend

```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp docs/ENV.example .env
# Edit .env with your API keys
```

### 4. Run the Backend

```bash
uvicorn main:app --reload --port 8000
```

### 5. Build macOS App

```bash
cd apps/macos
open EmpireOS.xcodeproj
# Press Cmd+B to build, Cmd+R to run
```

## API Key Configuration

### LM Studio (Local Models — Recommended)

1. Download LM Studio from https://lmstudio.ai
2. Install a model (e.g., Gemma 4 E4B GGUF for M3 8GB)
3. Start the local server (default: http://localhost:1234)
4. No API key needed

### Google Gemini 2.5 (Optional)

1. Get API key from https://aistudio.google.com
2. Add to `.env`: `EMPIREOS_GOOGLE_API_KEY=your_key`

### OpenAI (Optional)

1. Get API key from https://platform.openai.com
2. Add to `.env`: `EMPIREOS_OPENAI_API_KEY=your_key`

### Anthropic Claude (Optional)

1. Get API key from https://console.anthropic.com
2. Add to `.env`: `EMPIREOS_ANTHROPIC_API_KEY=your_key`

## Verification

Open http://localhost:8000/health in your browser to verify the backend is running.

The EmpireOS app will connect to the backend automatically on startup.
