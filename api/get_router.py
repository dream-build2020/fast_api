from fastapi import APIRouter, Header, Response, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional, Annotated
from project import project_1
from settings.settings import setting
from mysql_project import mysql_1

router = APIRouter(
    prefix='/user',
    tags=[setting.get_tag]
)

security = HTTPBasic()


class QueryCheck(object):
    def __init__(self, content: str):
        self.content = content

    def __call__(self, q: str = ""):
        if q:
            return self.content in q
        return False


checker = QueryCheck("bar")


@router.get('/mysql')
async def mysql():
    """
    实现查询dev_user_tables表的数据
    :return: dev_user_tables数据表
    """
    data = mysql_1.Tables.fetch_data()
    return {
        "items": data
    }


items_list = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@router.get('/items')
async def items(skip: int, limit: int):
    return items_list[skip: skip + limit]


@router.get('/me')
async def user(info: Annotated[HTTPBasicCredentials, Depends(security)]):
    project_1
    return {
        'username': info.username,
        'password': info.password
    }


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
