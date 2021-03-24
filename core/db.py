import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import DATABASE_URL, SQLALCHEMY_DATABASE_URL, SQLALCHEMY_ASYNC_DATABASE_URL

Base: DeclarativeMeta = declarative_base()

# 异步查询db链接
# database = databases.Database(DATABASE_URL)

# sync
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# async
# mysql+aiomysql://user:password@host:port/dbname
async_engine = create_async_engine(
    SQLALCHEMY_ASYNC_DATABASE_URL, echo=True,
)

async_session = sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )

