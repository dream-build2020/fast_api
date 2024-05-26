from fastapi import APIRouter
from datetime import datetime
from settings.settings import setting
from mysql_project.mysql_1 import Tables
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    tags=[setting.put_tag]
)


class Item(BaseModel):
    ID: int
    User_ID: int
    User: str


@router.post('/post')
async def put(items_id: dict):
    return {
        "items_id": items_id,
        "ID": items_id.get('ID')
    }


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
    # return {
    #     "ID": int(data.get('ID')),
    #     "User_ID": int(data.get('User_ID')),
    #     "User": data.get('User'),
    #     "Date": datetime.today()
    # }
    pass
