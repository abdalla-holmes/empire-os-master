"""
EmpireOS Configuration
Centralized configuration with environment variable support.
"""

from dataclasses import dataclass, field
from pathlib import Path
import os


@dataclass
class ProviderConfig:
    name: str
    api_key: str | None = None
    base_url: str | None = None
    enabled: bool = False
    priority: int = 0


@dataclass
class Settings:
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"
    env: str = "development"
    upload_dir: Path = field(default_factory=lambda: Path("./uploads"))
    api_key: str | None = None
    max_upload_size: int = 104_857_600
    providers: list[ProviderConfig] = field(default_factory=list)
    
    def _ensure_dirs(self):
        self.upload_dir.mkdir(parents=True, exist_ok=True)


def load_settings() -> Settings:
    s = Settings()
    s.host = os.getenv("EMPIREOS_HOST", s.host)
    s.port = int(os.getenv("EMPIREOS_PORT", str(s.port)))
    s.api_key = os.getenv("EMPIREOS_API_KEY")
    s.upload_dir = Path(os.getenv("EMPIREOS_UPLOAD_DIR", "./uploads"))
    
    providers = []
    if os.getenv("EMPIREOS_LMSTUDIO_BASE_URL"):
        providers.append(ProviderConfig("lmstudio", base_url=os.getenv("EMPIREOS_LMSTUDIO_BASE_URL"), enabled=True, priority=1))
    if os.getenv("EMPIREOS_GOOGLE_API_KEY"):
        providers.append(ProviderConfig("gemini", api_key=os.getenv("EMPIREOS_GOOGLE_API_KEY"), enabled=True, priority=2))
    if os.getenv("EMPIREOS_OPENAI_API_KEY"):
        providers.append(ProviderConfig("openai", api_key=os.getenv("EMPIREOS_OPENAI_API_KEY"), enabled=True, priority=3))
    if os.getenv("EMPIREOS_ANTHROPIC_API_KEY"):
        providers.append(ProviderConfig("anthropic", api_key=os.getenv("EMPIREOS_ANTHROPIC_API_KEY"), enabled=True, priority=4))
    
    s.providers = sorted(providers, key=lambda p: p.priority)
    s._ensure_dirs()
    return s


settings = load_settings()
