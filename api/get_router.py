from fastapi import APIRouter
from settings.settings import setting

router = APIRouter(
    prefix='/user',
    tags=[setting.get_tag]
)


@router.get('/node')
async def node():
    return {
        'items': '/index/node'
    }
