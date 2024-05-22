from fastapi import APIRouter
from settings.settings import setting

router = APIRouter(
    tags=[setting.put_tag]
)


@router.put('/{items_id}')
async def put(items_id: int):
    return {
        "items_id": items_id
    }
