from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from settings.settings import setting
from datetime import datetime


class Tables(setting.Base):
    __tablename__ = 'dev_user_tables'

    # 表的结构
    ID = Column(Integer, autoincrement=True)
    User_ID = Column(Integer, primary_key=True)
    User = Column(String)
    Date = Column(DateTime)

    LOGGER = setting.LOGGER
    mysql_session = sessionmaker(bind=setting.engine)

    @staticmethod
    def fetch_data():
        """
        实现查询数据功能
        :return: 查询数据
        """

        session = Tables.mysql_session()
        try:
            lists = []
            # 查询所有行
            rows = session.query(Tables).all()
            for row in rows:
                Tables.LOGGER.info(f"ID: {row.ID}, User_ID: {row.User_ID}, User: {row.User}, Date: {row.Date}")
                data = {
                    'ID': row.ID,
                    'User_ID': row.User_ID,
                    'User': row.User,
                    'Date': row.Date
                }
                lists.append(data)
        except Exception as e:
            # 执行失败后，数据库不保存数据
            session.rollback()
            Tables.LOGGER.error(e)
        else:
            return lists
        finally:
            # 关闭会话
            session.close()

    @staticmethod
    def add_data(ID:int, User_ID: int, User: str, Date: datetime):
        session = Tables.mysql_session()
        try:
            new_entry = Tables(ID=ID, User_ID=User_ID, User=User, Date=Date)
            session.add(new_entry)
            session.commit()
        except Exception as e:
            session.rollback()
            Tables.LOGGER.error(e)
        finally:
            session.close()


if __name__ == "__main__":
    # time = datetime.today()
    # Tables.add_data(2, 3000, '李四', time)
    pass
