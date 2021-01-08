from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from core import config
from core.events import create_start_app_handler, create_stop_app_handler
from core.routes import page_routes, api_routes


def create_app():
    app = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG, version=config.VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount('/static', StaticFiles(directory='static'), name='static')

    # 应用启动和关闭时，增加监听事件，用来创建和关闭数据库链接。
    app.add_event_handler("startup", create_start_app_handler())
    app.add_event_handler("shutdown", create_stop_app_handler())

    # 路由
    app.include_router(page_routes)
    app.include_router(api_routes, prefix=config.API_PREFIX)
    return app


app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app, host="127.0.0.1", port=8001, log_level="debug")
    # gunicorn -b 127.0.0.1: 8001 -k uvicorn.workers.UvicornWorker main: api
