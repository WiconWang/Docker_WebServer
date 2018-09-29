# 指定我们的基础镜像是node，版本是v9.11
FROM node:9.11
MAINTAINER WICON.WANG
 
# VOLUME /app
WORKDIR /app 
# 把Vue源改成淘宝的
# RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
# 全局安装 vue-cli
RUN npm install --global vue-cli
RUN vue init webpack . 

# # 配置环境变量
ENV HOST 0.0.0.0
ENV PORT 9071

# # 容器对外暴露的端口号
EXPOSE 9071


COPY . /app

# # 容器启动时执行的命令，类似npm run start
CMD ["npm", "run", "dev"]