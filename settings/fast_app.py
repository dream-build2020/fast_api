from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from settings.settings import setting

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
)

# 创建 OAuth2PasswordBearer 实例
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
