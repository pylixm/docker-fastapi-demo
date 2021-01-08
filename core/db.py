import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL

# SQLALCHEMY_DATABASE_URL = "mysql://root:Root1024@localhost/fastapi"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL.__str__())
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

# 异步查询db链接
database = databases.Database(DATABASE_URL)
