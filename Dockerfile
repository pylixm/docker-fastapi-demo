FROM python:3.9-slim-buster

LABEL maintainer="DeanWu <pyli.xm@gmail.com>"

# stdout 无缓冲，直接输出
ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app

RUN chmod +x start.sh prestart.sh start-reload.sh

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev gcc libffi-dev make && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt && \
    pip install --no-cache-dir gunicorn

ENV PYTHONPATH=/app

EXPOSE 80

#CMD ["sh", "start.sh"]
