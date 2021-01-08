from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from pydantic import BaseModel

router = APIRouter()


class User(BaseModel):
    name: str
    age: int


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get('/user')
async def user(user_id: int = Query(..., title="The ID of the user to get", gt=0)):
    return {'user_id': user_id}


@router.put('/user/{user_id}')
async def user(user_id: int = Path(..., title="The ID of the user to get", gt=0)):
    return {'user_id': user_id}


@router.post("/users/")
async def create_user(user: User):
    return user


@router.delete('/user/{user_id}')
async def user(user_id: int = Path(..., title="The ID of the user to get", gt=0)):
    return {'user_id': user_id}