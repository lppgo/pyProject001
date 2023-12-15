from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# declarative_base是一个工厂函数，用于创建所有模型类的基类, 用于定义数据库模型
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))  # 设置name列的长度为255
    age = Column(Integer)


#
user = "root"
password = "admin"
database = "mycbt"
host = "localhost"
port = "3306"
url_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8"
#
engine = create_engine(url=url_str, echo=True)


Base.metadata.create_all(engine)

# sessionmaker是一个工厂函数，用于创建数据库会话对象
Session = sessionmaker(bind=engine)
# session对象来执行数据库操作，如插入、查询、更新和删除等
session = Session()


# 插入数据
# user1 = User(name="lucas", age=18)
# # session.add(user1)
# user2 = User(name="honey", age=20)
# user3 = User(name="lucy", age=19)

# data = (user1, user2, user3)
# session.add_all(data)

# session.commit()


# 查询数据
users = session.query(User).all()
for user in users:
    print(user.id, user.name)
session.commit()


# 更新数据
user_to_update = session.query(User).filter_by(age=8).first()
user_to_update.name = 'denty'
session.commit()


# 删除数据
# user_to_delete = session.query(User).filter_by(name='李四').first()
# session.delete(user_to_delete)
# session.commit()


# 查询数据
users = session.query(User).all()
for user in users:
    print(user.id, user.name)
session.commit()


session.close()
