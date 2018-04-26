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

### LNMP环境，  
> 核心模块：nginx + php7.1 + mysql ，扩展可选模块：redis 、 memcached 、 mongo   

> 配置文件和Dockerfile 均在Config中  

> 默认目录在wwwroot下，如果想使用其它目录做站点目录，请在docker-compose.yml中，把期望目录映射到容器内目录，然后nginx配置目录使用映射目录，如果有权限问题，可以映射到/tmp/下。（如~/Sites 映射为 /sites，Nginx的vhost地址填写为/sites）    

> 另：Xdebug默认的端口是9009，请到Config/php/conf.d/xdebug.ini中修改IP为你的IP，建议使用 LAN的IP地址   

### JAVA环境
> 有两种，此两种环境互斥：   

> **Java-tomcat-supervisor** ：以wwwroot下webapps为根目录显示站点，此环境内置httpd暂不可用但有bug    

> **Java-maven-tomcat** ： 生成容器时自启动maven，并编译wwwroot下的代码    

> 建议同时请启用Mysql  

### Python环境  
> **Python 3.6 + Django 1.9 + Scrapy 1.4 **  

> 注意 wwwroot/env下，启用了一个名为docker的库并使用了帐号密码，请mysql初始化完成以后，新建此库再编译python区    

> 建议同时请启用Mysql、Redis  
---  

注: 因环境编译时多个组件如 apt 、 pecl 、 git 需要连接各官网下载，如编译出错，请核实地址后，修改对应的Dockerfile文件，如需要请布置翻墙
