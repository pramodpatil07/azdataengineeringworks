from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Dict


class ConfigError(Exception):
    """Raised when a configuration file cannot be loaded."""


@dataclass
class PythonConfig:
    app_name: str
    environment: str
    storage: Dict[str, Any]
    extras: Dict[str, Any] = None


def resolve_config_path(path: str) -> Path:
    config_path = Path(path)
    if not config_path.exists():
        raise ConfigError(f"Configuration file not found: {config_path}")
    return config_path


def load_json_config(path: str) -> Dict[str, Any]:
    config_path = resolve_config_path(path)
    if config_path.suffix.lower() != ".json":
        raise ConfigError("load_json_config expects a .json file")

    try:
        with config_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except ValueError as exc:
        raise ConfigError(f"Invalid JSON configuration: {config_path}") from exc


def load_config(path: str) -> Dict[str, Any]:
    config_path = resolve_config_path(path)
    if config_path.suffix.lower() == ".json":
        return load_json_config(path)

    raise ConfigError(
        f"Unsupported config type: {config_path.suffix}. Supported types: .json"
    )
