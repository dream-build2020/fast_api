from fastapi import APIRouter, Header, Response, status, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from project import project_1
from settings.settings import setting

router = APIRouter(
    prefix='/user',
    tags=[setting.get_tag]
)


class QueryCheck(object):
    def __init__(self, content: str):
        self.content = content

    def __call__(self, q: str = ""):
        if q:
            return self.content in q
        return False


checker = QueryCheck("bar")

@router.get('/me')
async def user():
    project_1
    return True

@router.get('/node1/{token}')
async def node1(token: str, response: Response):
    response.headers['x-auth-token'] = '123'
    if token == "123":
        response.status_code = status.HTTP_200_CREATED
        return {
            'heartbeat': 'hearth'
        }


@router.get('/node2/{key}')
async def node2(key: str):
    content = {"message": "Come to the dark"}
    response = JSONResponse(content)
    return response


@router.get('/node3/')
async def node3(content: bool = Depends(checker)):
    return {
        'item': content
    }