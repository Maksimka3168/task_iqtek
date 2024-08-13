from dataclasses import dataclass
from typing import Any, Mapping


@dataclass
class AppConfig:
    type: str
    settings: Mapping[str, Any]
