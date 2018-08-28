# 此模块适用于自动生成iview-admin
不过说实话，如果是开发，还是自己去容器内npm 生成比较合适

FROM node:9.11
MAINTAINER Wicon.Wang <wiconwang@gmail.com>

# 改为淘宝节点
RUN yes | npm install -g cnpm --registry=https://registry.npm.taobao.org

# 下载iview基础包并安装
RUN yes | git clone https://github.com/iview/iview-admin.git /iview \
&& cd /iview

RUN yes | cnpm install

# 初始化项目
# RUN yes | npm init -y


VOLUME ../../../../wwwroot/vue_demo /sites

RUN yes | mv /iview/* /sites/


WORKDIR /sites


# 启动
# RUN npm run dev

