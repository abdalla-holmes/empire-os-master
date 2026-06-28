"""
EmpireOS Pydantic Models
All request/response models for the API.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field


# =============================================================================
# Common
# =============================================================================

class APIResponse(BaseModel):
    success: bool = True
    message: str = ""
    data: dict[str, Any] | None = None


class HealthResponse(BaseModel):
    status: str = "healthy"
    version: str = "1.0.0"
    uptime: float = 0.0
    providers: list[dict[str, Any]] = []


class MetricsResponse(BaseModel):
    total_requests: int = 0
    average_latency_ms: float = 0.0
    active_connections: int = 0
    active_agents: int = 0


class SettingsResponse(BaseModel):
    host: str
    port: int
    log_level: str
    providers: list[str]
    voice_enabled: bool
    vision_enabled: bool


class SettingsUpdateRequest(BaseModel):
    log_level: str | None = None
    voice_enabled: bool | None = None
    vision_enabled: bool | None = None


# =============================================================================
# Chat / LLM
# =============================================================================

class ChatCompletionRequest(BaseModel):
    model: str = "default"
    messages: list[dict[str, str]]
    stream: bool = False
    temperature: float = 0.7
    max_tokens: int = 4096


class ChatCompletionResponse(BaseModel):
    id: str
    model: str
    message: dict[str, str]
    usage: dict[str, int] | None = None


# =============================================================================
# Voice
# =============================================================================

class STTRequest(BaseModel):
    audio: str  # base64 encoded audio
    format: str = "wav"
    language: str = "en"


class STTResponse(BaseModel):
    text: str
    language: str = "en"
    confidence: float = 1.0


class TTSRequest(BaseModel):
    text: str
    voice: str = "default"
    speed: float = 1.0
    format: str = "mp3"


class TTSResponse(BaseModel):
    audio: str  # base64 encoded audio
    format: str
    duration_ms: int


# =============================================================================
# Vision
# =============================================================================

class VisionAnalyzeRequest(BaseModel):
    image: str | None = None  # base64 encoded image
    source: Literal["screen", "window", "upload"] = "screen"
    depth: Literal["fast", "standard", "deep"] = "standard"
    query: str | None = None


class VisionAnalyzeResponse(BaseModel):
    text: str
    elements: list[dict[str, Any]] = []
    ocr_text: str = ""
    ai_description: str = ""


# =============================================================================
# Agents
# =============================================================================

class AgentStatus(str, Enum):
    IDLE = "idle"
    LOADING = "loading"
    ACTIVE = "active"
    BUSY = "busy"
    COMPLETED = "completed"
    ERROR = "error"
    OFFLINE = "offline"


class AgentCapability(BaseModel):
    name: str
    description: str
    category: str


class AgentListResponse(BaseModel):
    agents: list[dict[str, Any]]
    total: int


class AgentStatusResponse(BaseModel):
    agent_id: str
    status: AgentStatus
    progress: float = 0.0
    message: str = ""


class AgentActivateRequest(BaseModel):
    agent_id: str
    task: str
    context: dict[str, Any] | None = None


class AgentTeamRequest(BaseModel):
    agent_ids: list[str]
    task: str
    context: dict[str, Any] | None = None


# =============================================================================
# Tools
# =============================================================================

class ToolExecuteRequest(BaseModel):
    tool: str
    action: str
    params: dict[str, Any] = Field(default_factory=dict)


class ToolExecuteResponse(BaseModel):
    success: bool
    result: Any
    error: str | None = None


class ToolListResponse(BaseModel):
    tools: list[dict[str, Any]]


# =============================================================================
# Files
# =============================================================================

class FileUploadResponse(BaseModel):
    id: str
    filename: str
    size: int
    url: str


class FileListResponse(BaseModel):
    files: list[dict[str, Any]]


# =============================================================================
# WebSocket
# =============================================================================

class WSMessageType(str, Enum):
    PING = "ping"
    PONG = "pong"
    CHAT = "chat"
    VOICE = "voice"
    VISION = "vision"
    AGENT_COMMAND = "agent_command"
    AGENT_STATUS = "agent_status"
    TOOL_EXECUTE = "tool_execute"
    SETTINGS_UPDATE = "settings_update"
    ERROR = "error"


class WSMessage(BaseModel):
    type: WSMessageType
    payload: dict[str, Any] = Field(default_factory=dict)
    id: str | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
