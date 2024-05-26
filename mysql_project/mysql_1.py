from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from settings.settings import setting


class Tables(setting.Base):
    __tablename__ = 'dev_user_tables'

    # 表的结构
    ID = Column(Integer, autoincrement=True)
    User_ID = Column(Integer, primary_key=True)
    User = Column(String)
    Date = Column(DateTime)

    LOGGER = setting.LOGGER

    @staticmethod
    def fetch_data():
        mysql_session = sessionmaker(bind=setting.engine)
        session = mysql_session()
        try:
            lists = []
            # 查询所有行
            rows = session.query(Tables).all()
            for row in rows:
                # print(f"ID: {row.ID}, User_ID: {row.User_ID}, User: {row.User}, Date: {row.Date}")
                Tables.LOGGER.info(f"ID: {row.ID}, User_ID: {row.User_ID}, User: {row.User}, Date: {row.Date}")
                data = {
                    'ID': row.ID,
                    'User_ID': row.User_ID,
                    'User': row.User,
                    'Date': row.Date
                }
                lists.append(data)
        except Exception as e:
            Tables.LOGGER.error(e)
        else:
            return lists
        finally:
            # 关闭会话
            session.close()
