from fastapi import APIRouter, Request, Query, status
from fastapi.responses import JSONResponse
from settings.settings import setting
from mysql_project import mysql_1

router = APIRouter(
    # prefix='/get',
    tags=[setting.get_tag]
)


@router.get('/base')
async def get_base(*, request: Request):
    res = {
        # 客户端连接的 host
        "host": request.client.host,
        # 客户端连接的端口号
        "port": request.client.port,
        # 请求方法
        "method": request.method,
        # 请求路径
        "base_url": request.base_url,
        # request headers
        "headers": request.headers,
        # request cookies
        "cookies": request.cookies
    }
    return res


@router.get('/get/{items_id}')
async def get_url(*,
                  items_id: str,
                  # Query: 请求参数
                  name: str = Query(default=None, max_length=10),
                  request: Request):
    res = {
        # 请求 url
        "url": str(request.url),
        # 总的组成
        "components": request.url.components,
        # 请求协议
        "scheme": request.url.scheme,
        # 请求 host
        "hostname": request.url.hostname,
        # 请求端口
        "url_port": request.url.port,
        # 请求 path
        "path": request.url.path,
        # 请求查询参数
        "query": request.url.query,
        "fragment": request.url.fragment,
        "password": request.url.password
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=res)


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
