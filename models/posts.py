from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship, backref
from core.db import Base as PostsBase


class Posts(PostsBase):
    __tablename__ = "service_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(200))
    text = Column(String(350))
    author = Column(String(100))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())


posts = Posts.__table__


