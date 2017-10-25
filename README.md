# Docker_PHP_Server
docker-compose.yml 文件中包含以下程序配置，  

1.  Nginx   
1.  PHP7.1 （ Config/php/Dockerfile）
1.  Mysql    
1.  Redis   
1.  Memcached   
1.  MongoDB   
1.  java-maven-tomcat   （ java-maven-tomcat/Dockerfile）
1.  java-tomcat-supervisor   （ java-tomcat-supervisor）

---  
git clone 后。请按需求组合，并启用您需要的环境：    

LNMP环境，启用以下环境 （后三项可选）：     
nginx + php7.1 + mysql + redis + memcached + mongo  

JAVA环境有两种，此两种环境互斥：   
java-tomcat-supervisor ：此环境内置httpd但此处有bug  
java-maven-tomcat ： 自动启用maven编译环境  
 
---  
LNMP相关配置文件、Dockerfile在Config中，默认目录在wwwroot下  
JAVA相关配置、Dockerfile、默认目录均在两个组件文件夹下  
因环境编译时多个组件 需要连接官网下载，如编译出错，请核实地址后，修改对应的Dockerfile文件
