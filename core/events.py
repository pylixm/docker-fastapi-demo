from typing import Callable
from loguru import logger

from core.db import database


def create_start_app_handler() -> Callable:  # type: ignore
	async def startup():
		await database.connect()

	return startup


def create_stop_app_handler() -> Callable:  # type: ignore
	@logger.catch
	async def shutdown():
		await database.disconnect()

	return shutdown
