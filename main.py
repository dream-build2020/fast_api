import uvicorn
from fastapi import FastAPI
from settings.settings import setting
from api import api_router

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
)

app.include_router(api_router.router)


@app.get('/')
async def index():
    return {
        'items': 'index'
    }


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=setting.HOST,
        port=setting.PORT
    )
    pass
