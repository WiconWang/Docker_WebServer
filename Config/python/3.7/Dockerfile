FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN echo "deb http://mirrors.aliyun.com/debian stretch main contrib non-free" > /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian stretch main contrib non-free" >> /etc/apt/sources.list  && \
    echo "deb http://mirrors.aliyun.com/debian stretch-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian stretch-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.aliyun.com/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.aliyun.com/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list
    
RUN apt-get update && \
    apt-get install -y cron && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

COPY ./requirements.txt ./

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt --no-cache-dir --disable-pip-version-check

COPY . /app

ADD ./crontab /var/spool/cron/crontabs/root

RUN chmod 0644 /var/spool/cron/crontabs/root && touch /var/log/cron.log