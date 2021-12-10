# Docker_WebServer

## Install
1. 请安装好Docker，以及Docker-compose。（desktop版已自带）
1. 请先检查`docker-compose.yml`中的组件，关闭或者开启所需要的功能模块。   
1. 将根目录下的 `.env.example` 复制 为 `.env` 并修改内部的值，比如设置默认项目目录 、设定Mysql模块初始的Root密码。   
1. Nacos组件需要在Mysql启动后。连接进入，新建名为`nacos`git的数据库，并将本目录下的`nacos.sql`导入其中，才可以正常使用。默认帐号密码均为`nacos`

## Introduction  
docker-compose.yml 文件中包含以下程序配置，  

1.  Nginx 1.15   
2.  Nacos 2.0.3
4.  Mysql 8  
7.  MongoDB  4.1  
5.  Redis 5.0   
6.  Memcached 1.5   
7.  HBase 2.1 with Zookeeper and REST API
8.  PHP 5.6|7.X （ Config/php/XX/Dockerfile）
9.  Vue with node 9.11
10. Django 1.9 with python 3.7
11. Java-maven-tomcat   （ Java-maven-tomcat/Dockerfile）
12. Java-tomcat-supervisor   （ Java-tomcat-supervisor/Dockerfile）
13. ElasticSearch and Kibana 

---  
git clone 后。请按需求组合，并启用您需要的环境：    

### LNMP环境，  
> 核心模块：nginx + php7.1 + mysql ，扩展可选模块：php5.6、 redis 、 memcached 、 mongo   

> 各组件配置文件 和 Dockerfile 均在Config中


> 默认目录在wwwroot下，如果想使用其它目录做站点目录，请在docker-compose.yml中，把期望目录映射到容器内目录，然后nginx配置目录使用映射目录，如果有权限问题，可以映射到/tmp/下。（如~/Sites 映射为 /Sites，Nginx的vhost地址填写为/Sites）    

> 另：Xdebug默认的端口是9009，请到Config/php/conf.d/xdebug.ini中修改IP为你的IP，建议使用 LAN的IP地址  
 
>  php版本可并存，yml 文件引入PHP时起好别名，同时nginx配置中正确引入 如 fastcgi_pass   php-fpm56:9000; 

### Python环境  
> **Python 3.7 + Django 1.9 + Scrapy 1.4 **  

> Django 需要连接Mysql库 如手动编译，请mysql初始化完成以后，编译python区    

> Django 需要迁移表，可以进入容器用命令行进行迁移

### JAVA环境
> 有两种，此两种环境互斥：   

> **Java-tomcat-supervisor** ：以wwwroot下webapps为根目录显示站点，此环境内置httpd暂不可用但有bug    

> **Java-maven-tomcat** ： 生成容器时自启动maven，并编译wwwroot下的代码    

> 建议同时请启用Mysql  

### 大数据环境

> 选择启用  ElasticSearch 、 Kibana 、  HBase等

---  

注: 因环境编译时多个组件如 apt 、 pecl 、 git 需要连接各官网下载，由于这些组件的版本经常有变更，以及由于某些墙的原因，可能导致无法正常连接，如编译出错，请核实地址修改对应的Dockerfile文件，或者开启VPN。 
