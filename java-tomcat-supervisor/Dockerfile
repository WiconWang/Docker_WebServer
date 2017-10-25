FROM centos:centos6
MAINTAINER Guuuo <im@kuo.io>

#update
RUN yum -y update; yum clean all
#install tools
RUN yum install -y wget unzip tar
#install supervisor
RUN yum install -y python-setuptools \
&&  easy_install supervisor \
&&  mkdir -p /var/log/supervisor

#install httpd
RUN yum -y install httpd

#config httpd
RUN mkdir -p /data
ADD wwwroot /data/wwwroot
ADD conf/httpd/wwwconf /data/wwwconf
ADD conf/httpd/httpd.conf /etc/httpd/conf/httpd.conf

#install jdk
ENV JAVA_VERSION 8u151
ENV BUILD_VERSION b12
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/e758a0de34e24606bca991d704f6dcbf/jdk-$JAVA_VERSION-linux-x64.rpm" -O /tmp/jdk-8-linux-x64.rpm \
    &&  yum -y install /tmp/jdk-8-linux-x64.rpm \
    &&  rm -rf /tmp/jdk-8-linux-x64.rpm \
    &&  alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000 \
    &&  alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 200000 \
    &&  alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000
ENV JAVA_HOME /usr/java/latest


#install make
RUN yum -y install gcc automake autoconf libtool make openssl openssl-devel

#install tomcat
ENV TOMCAT_VERSION 8.5.23
RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.zip -O /tmp/tomcat.zip \
    && unzip /tmp/tomcat.zip -d /tmp/ \
    && rm -rf /tmp/tomcat.zip \
    && mkdir -p /data \
    && mv /tmp/apache-tomcat-$TOMCAT_VERSION /data/tomcat \
    && chmod 777 /data/tomcat/bin/*.sh
ADD conf/tomcat/tomcat-users.xml /data/tomcat/conf/tomcat-users.xml

#apr
RUN  cd /tmp  \
    &&  wget http://mirror.bit.edu.cn/apache/apr/apr-1.6.3.tar.gz \
    && tar -zxvf apr-1.6.3.tar.gz  \
    && cd apr-1.6.3 \
    && ./configure --prefix=/usr/local/apr \
    && make \
    && make install \
    && rm -rf /tmp/apr-1.6.3.tar.gz

RUN  cd /tmp  \
    &&  wget http://mirror.bit.edu.cn/apache/apr/apr-iconv-1.2.2.tar.gz  \
    && tar zxvf apr-iconv-1.2.2.tar.gz \
    && cd apr-iconv-1.2.2 \
    && ./configure --prefix=/usr/local/apr-iconv --with-apr=/usr/local/apr   \
    && make \
    && make install \
    && rm -rf /tmp/apr-iconv-1.2.2.tar.gz

RUN yum -y install  expat-devel
#apr
RUN  cd /tmp  \
    &&  wget http://mirror.bit.edu.cn/apache/apr/apr-util-1.6.1.tar.gz   \
    && tar zxvf apr-util-1.6.1.tar.gz \
    && cd apr-util-1.6.1 \
    && ./configure --prefix=/usr/local/apr-util --with-apr=/usr/local/apr --with-apr-iconv=/usr/local/apr-iconv/bin/apriconv   \
    && make \
    && make install \
    && rm -rf /tmp/apr-util-1.6.1.tar.gz

# SSL
RUN  cd /tmp \
    && wget https://www.openssl.org/source/openssl-1.0.2-latest.tar.gz \
    && tar -xzxf openssl-1.0.2-latest.tar.gz \
    && cd openssl-1.0.2l \
    && ./config --prefix=/usr/local/openssl -fPIC \
    && make \
    && make install \
    && rm -rf /tmp/openssl-1.0.2-latest.tar.gz


#install tomcat-native
RUN cp /data/tomcat/bin/tomcat-native.tar.gz /tmp/tomcat-native.tar.gz \
    && tar zxvf /tmp/tomcat-native.tar.gz -C /tmp; rm -rf /tmp/tomcat-native.tar.gz \
    && mv /tmp/tomcat-native-*-src /tmp/tomcat-native
WORKDIR /tmp/tomcat-native/native
RUN chmod +x ./configure \
    && chmod +x ./build/*.sh \
    && ./configure --with-apr=/usr/local/apr  --with-java-home=$JAVA_HOME --with-ssl=/usr/local/openssl  \
    && make && make install \
    && rm -rf /tmp/tomcat-native
#config apr
ENV LD_LIBRARY_PATH /usr/local/apr/lib

#config supervisor
ADD conf/supervisor/supervisord.conf /etc/supervisord.conf
ADD conf/supervisor/supervisord_tomcat.sh /data/tomcat/bin/supervisord_tomcat.sh
RUN chmod +x /data/tomcat/bin/supervisord_tomcat.sh

EXPOSE 80

CMD ["supervisord", "-n"]
