# -*- coding:utf-8 -*-
import json
import multiprocessing
import os


# worker 数取值方式
# web_concurrency_str > 启用max_worker --> max(workers_per_core_str*cores, 2)
#                     > 没启用max_worker --> min(max(workers_per_core_str*cores, 2), use_max_workers)
# 对应环境变量
# web_concurrency_str  WEB_CONCURRENCY
# use_max_workers      MAX_WORKERS
# workers_per_core_str WORKERS_PER_CORE

# 每个核的worker数，用于下边计算
workers_per_core_str = os.getenv("WORKERS_PER_CORE", "1")
# 最大worker数
max_workers_str = os.getenv("MAX_WORKERS")
use_max_workers = None
if max_workers_str:
    use_max_workers = int(max_workers_str)
# web当前的worker数
web_concurrency_str = os.getenv("WEB_CONCURRENCY", None)
# 根据核数计算默认worker数
cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
default_web_concurrency = workers_per_core * cores
if web_concurrency_str:
    web_concurrency = int(web_concurrency_str)
    assert web_concurrency > 0
else:
    # 默认核数，最小为2
    web_concurrency = max(int(default_web_concurrency), 2)
    # 若启用最大worker数，则为当前worker 和 max workers 最小值
    if use_max_workers:
        web_concurrency = min(web_concurrency, use_max_workers)

# 地址和端口的绑定
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "80")
bind_env = os.getenv("BIND", None)
if bind_env:
    use_bind = bind_env
else:
    use_bind = "{}:{}".format(host, port)  # f"{host}:{port}"

# 日志级别
use_loglevel = os.getenv("LOG_LEVEL", "info")

accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "120")
timeout_str = os.getenv("TIMEOUT", "120")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables
workers = web_concurrency
bind = use_bind
loglevel = use_loglevel
worker_tmp_dir = ""
errorlog = use_errorlog
accesslog = use_accesslog
# 接收到restart信号后，worker可以在graceful_timeout时间内，继续处理完当前requests。
graceful_timeout = int(graceful_timeout_str)
# 链接超时
timeout = int(timeout_str)
# 链接保持，默认2s, 可减少链接频繁断开造成取用超时问题
keepalive = int(keepalive_str)


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "workers_per_core": workers_per_core,
    "use_max_workers": use_max_workers,
    "host": host,
    "port": port,
}
print(json.dumps(log_data))
