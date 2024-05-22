from pydantic import BaseConfig


class APISettings(BaseConfig):
    HOST: str = "127.0.0.1"
    PORT: int = 8088
    TITLE: str = "FAST-API"
    VERSION: float = 0.1

    # router get tag
    get_tag: str = "get_tag"
    put_tag: str = "put_tag"


setting = APISettings()
