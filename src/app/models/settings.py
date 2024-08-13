from dataclasses import dataclass


@dataclass
class PostgresSetting:
    driver: str
    username: str
    password: str
    hostname: str
    database_name: str
