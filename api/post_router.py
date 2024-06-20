from fastapi import APIRouter, Request
from datetime import datetime
from typing import Union
from settings.settings import setting
from mysql_project.mysql_1 import Tables
from utils import fast_config

router = APIRouter(
    tags=[setting.put_tag]
)

ApiConfig = fast_config.Item


@router.post("/data/")
async def create_data(item: Union[dict, None] = None):
    return item


@router.post("/items/")
async def create_item(item: ApiConfig,
                      requests: Request):
    """
    在路径操作函数内部直接访问模型对象的属性：
    :param requests: POST
    :param item:
    :return: item_dict
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax,
                          "requests": requests.method})
    return item_dict


@router.post('/mysql')
async def put_mysql(data: dict):
    ID = int(data.get('ID'))
    User_ID = int(data.get('User_ID'))
    User = data.get('User')
    Date = datetime.today()

    Tables.add_data(ID=ID,
                    User_ID=User_ID,
                    User=User,
                    Date=Date
                    )
    return {
        "ID": int(data.get('ID')),
        "User_ID": int(data.get('User_ID')),
        "User": data.get('User'),
        "Date": datetime.today()
    }
    pass
