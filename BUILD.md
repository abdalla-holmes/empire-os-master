# Build Guide — EmpireOS Master

## Prerequisites

- macOS 14+ (Sonoma/Sequoia)
- Xcode 15+ with Swift 6.3+
- Python 3.11+
- 8GB+ RAM

## macOS App

### Option 1: Xcode
```bash
cd apps/macos
open EmpireOS.xcodeproj
# Cmd+B to build
# Cmd+R to run
```

### Option 2: Swift Package Manager
```bash
cd apps/macos
swift build
swift run EmpireOS
```

### Code Signing
The app uses sandbox entitlements. For local development:
1. Open EmpireOS.xcodeproj
2. Select your team in Signing & Capabilities
3. Build and run

## Python Backend

### Setup
```bash
cd server
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run Development Server
```bash
uvicorn main:app --reload --port 8000
```

### Run Production Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Variables
```bash
cp docs/ENV.example .env
# Edit with your API keys
```

## Testing

### Swift Tests
```bash
cd apps/macos
swift test
```

### Python Tests
```bash
cd server
pytest
```

## Distribution

### macOS App
1. Product → Archive in Xcode
2. Distribute App → Copy App
3. Or: `swift build -c release`

### Docker Backend
```bash
cd server
docker build -t empireos-backend .
docker run -p 8000:8000 --env-file .env empireos-backend
```

## Troubleshooting

### Build Errors
- Ensure macOS 14+ SDK is selected
- Clean build folder (Cmd+Shift+K)
- Reset package cache (File → Packages → Reset Package Caches)

### Backend Issues
- Check Python version: `python --version` (must be 3.11+)
- Verify all dependencies: `pip list`
- Check port 8000 is free: `lsof -i :8000`
- Review logs: `tail -f logs/empireos.log`

### Voice Issues
- Grant microphone permission in System Settings
- Install whisper.cpp: `brew install whisper-cpp`
- Install piper-tts: `brew install piper-tts`

### Vision Issues
- Grant screen recording permission in System Settings
- Privacy & Security → Screen Recording → EmpireOS
