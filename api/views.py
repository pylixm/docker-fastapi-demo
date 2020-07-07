from typing import List
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get('/')
def index():
	return {
		'code': 0,
		'msg': 'success'
	}
