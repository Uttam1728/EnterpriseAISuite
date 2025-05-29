import enum
import os
from typing import Optional, ClassVar

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from clerk_integration.utils import ClerkAuthHelper
from pydantic_settings import BaseSettings
from config.config_parser import docker_args

from utils.connection_manager import ConnectionManager
from utils.sqlalchemy import async_db_url

args = docker_args


class LogLevel(enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    env: str = args.env
    port: int = args.port
    host: str = args.host
    debug: bool = args.debug
    workers_count: int = 1
    mode: str = args.mode
    locksmith_db_url: str = args.locksmith_db_url
    db_url: str = async_db_url(args.locksmith_db_url)
    db_echo: bool = args.debug
    server_type: str = args.server_type
    realm: str = args.realm
    log_level: str = LogLevel.INFO.value
    connection_manager: Optional[ConnectionManager] = None

    kafka_bootstrap_servers: str = args.kafka_broker_list
    BASE_DIR: ClassVar[str] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sentry_sample_rate: float = 1.0
    sentry_environment: str = args.sentry_environment

    sentry_dsn: Optional[str] = args.sentry_dsn

    POD_NAMESPACE: str = args.K8S_POD_NAMESPACE
    NODE_NAME: str = args.K8S_NODE_NAME
    POD_NAME: str = args.K8S_POD_NAME
    aps_scheduler: Optional[AsyncIOScheduler] = None

    clerk_secret_key: str = args.clerk_secret_key
    clerk_auth_helper: ClerkAuthHelper = ClerkAuthHelper("locksmith", clerk_secret_key=clerk_secret_key)

loaded_config = Settings()
