import uvicorn
import time
from celery import Celery
from fastapi.responses import HTMLResponse
from settings.settings import setting
from api import get_router, post_router
from settings.fast_app import app


CeleryApp = Celery(
    'my_task',
    broker=setting.BROKER,
    time=setting.TIMEZONE
)


# Fast-api 路由功能
app.include_router(get_router.router)
app.include_router(post_router.router)


@app.get("/index")
async def index():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


@app.get('/Health')
# @CeleryApp.tasks
async def health():
    time.sleep(5)
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
