# Docker_WebServer
docker-compose.yml 文件中包含以下程序配置，  

1.  Nginx   
1.  PHP7.1 （ Config/php/Dockerfile）
1.  Mysql    
1.  Redis   
1.  Memcached   
1.  MongoDB   
1.  Java-maven-tomcat   （ Java-maven-tomcat/Dockerfile）
1.  Java-tomcat-supervisor   （ Java-tomcat-supervisor/Dockerfile）
1.  Python3-django-scrapy   （ Python3-django-scrapy/Dockerfile）

---  
git clone 后。请按需求组合，并启用您需要的环境：    

> LNMP环境，
> 核心模块：nginx + php7.1 + mysql
> 扩展可选模块：redis + memcached + mongo  
> 配置文件、Dockerfile在Config中
> 默认目录在wwwroot下

> JAVA环境有两种，此两种环境互斥：   
> Java-tomcat-supervisor ：以wwwroot下webapps为根目录显示站点，此环境内置httpd暂不可用但有bug  
> Java-maven-tomcat ： 生成容器时自启动maven，并编译wwwroot下的代码  
> 建议同时请启用Mysql

> Python环境
> Python 3.6 + Django 1.9 + Scrapy 1.4   
> 同时请启用Mysql、Redis
---  

因环境编译时多个组件 需要连接官网下载，如编译出错，请核实地址后，修改对应的Dockerfile文件
