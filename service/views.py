from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.requests import Request
from core import templates
from core.db import database
from models.posts import posts

router = APIRouter()


@router.get('/')
async def index(request: Request):
    print(posts.select())
    post_list = await database.fetch_all(query=posts.select())
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'post_list': post_list
        }
    )


