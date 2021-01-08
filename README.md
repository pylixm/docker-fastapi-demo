# docker-fastapi-demo

Fastapi 脚手架

## alembic 数据库迁移

一个迁移过程基本如下：

```bash 
# 1/ 初始化环境 
alembic init migrations 

# 2/ 修改alembic.ini参数
# alembic.ini 
sqlalchemy.url = mysql://root:Root1024@localhost/fastapi

# migrations/env.py
import sys 
sys.path = ['', '..'] + sys.path[1:]
from service.models import Base

...
target_metadata = Base.metadata  # 一个app model 
target_metadata = [Base.metadata, Base2.metadata]  # 多个app model

# 3/ 生成迁移脚本
alembic revision --autogenerate -m "init"

# 4/ 应用迁移脚本到数据库
alembic upgrade head 
```

alembic 还支持数据库的回滚、历史版本的查看等操作。更多内容，可参考：https://alembic.sqlalchemy.org/en/latest/index.html。


## 编译启动 

docker build -t fastapi-mysql:v1.0 .

docker run -p 80:80 -d -e DB_CONNECTION="mysql://root:Root1024@xxxx/fastapi" fastapi-mysql:v1.0 ./start.sh 