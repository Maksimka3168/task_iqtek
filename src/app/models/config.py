from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class RepositoryPostgresConfig:
    driver: str
    username: str
    password: str
    hostname: str
    database_name: str


@dataclass
class RepositoryConfig:
    selected_repository: str
    postgres: RepositoryPostgresConfig
    memory: dict


@dataclass
class AppConfig:
    repositories: RepositoryConfig
