import uvicorn
from fastapi import FastAPI, Depends, status
from fastapi.security import APIKeyHeader
from settings.settings import setting
from api import get_router, post_router

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
)

api_key = APIKeyHeader(name='X-API-key')

# Fast-api 路由功能
app.include_router(get_router.router)
app.include_router(post_router.router)


async def get_apikey(apikey: str = Depends(api_key)):
    if apikey != 'my-api-key':
        return False


@app.get('/')
async def index():
    return {
        'Stat': 'Health'
    }


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=setting.HOST,
        port=setting.PORT,
        reload=True,
        # debug=True
    )
    pass
