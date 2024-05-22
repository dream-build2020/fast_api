from pydantic import BaseConfig


class APISettings(BaseConfig):
    HOST: str = "127.0.0.1"
    PORT: int = 8088
    TITLE: str = "FAST-API"
    VERSION: float = 0.1

    # router tag
    router_tag: str = "router_tag"


setting = APISettings()
