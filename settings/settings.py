import logging
from pydantic import BaseConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


class APISettings(BaseConfig):
    # Celery settings
    BROKER: str = "redis://192.168.31.101:6379"
    BACKEND: str = "redis://192.168.31.101:6379"
    TIMEZONE: str = "Asia/Shanghai"

    HOST: str = "0.0.0.0"
    PORT: int = 8088
    TITLE: str = "FAST-API"
    VERSION: float = 0.1

    # router get tag
    get_tag: str = "get_tag"
    put_tag: str = "put_tag"

    # mysql settings
    mysql_url = "mysql+pymysql://root:123456@192.168.31.43:3306/dev_tables"
    Base = declarative_base()
    engine = create_engine(
        mysql_url,
        echo=True,
        max_overflow=5
    )

    # 日志配置
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.DEBUG)


setting = APISettings()
