from fastapi import APIRouter
from settings.settings import setting

router = APIRouter(
    prefix='/user',
    tags=[setting.router_tag]
)


@router.get('/node')
async def node():
    return {
        'items': '/index/node'
    }
