import uvicorn
from fastapi import FastAPI
from settings.settings import setting
from api import get_router, put_router

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
)

app.include_router(get_router.router)
app.include_router(put_router.router)


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
