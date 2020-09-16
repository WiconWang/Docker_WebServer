FROM php:7.2-fpm-stretch
# important !! this Dockerfile version is PHP7.2 ,Change URL and config with Other version

# You may need proxy
# RUN export http_proxy=192.168.0.111:1080
# RUN export https_proxy=192.168.0.111:1080

# Update debian Source to aliyun
# RUN yes |  echo "deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list \
# && echo "deb http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib" >> /etc/apt/sources.list \
# && echo "deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list \
# && echo "deb-src http://mirrors.aliyun.com/debian/ jessie-proposed-updates main non-free contrib" >> /etc/apt/sources.list \
# && echo "deb http://mirrors.aliyun.com/debian-backports/ jessie-backports main contrib non-free" >> /etc/apt/sources.list \
# && echo "deb-src http://mirrors.aliyun.com/debian-backports/ jessie-backports main contrib non-free" >> /etc/apt/sources.list \
# && apt-get update 

RUN yes |  apt-get update
# 特殊版本的底层依赖包
# RUN apt-get install -y   --force-yes  libcurl3=7.38.0-4+deb8u11 libldap-2.4-2=2.4.40+dfsg-1+deb8u4 libxml2=2.9.1+dfsg1-5+deb8u6 zlib1g=1:1.2.8.dfsg-2+b1

# 相关组件
RUN apt-get install -y libmcrypt-dev libicu-dev sqlite3 libsqlite3-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev libxml2-dev curl libcurl3 libcurl4-openssl-dev  libldb-dev libldap2-dev openssl  libssl-dev git wget unixodbc-dev

# docker仓库扩展
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
&& docker-php-ext-install json mbstring pdo pdo_sqlite tokenizer simplexml xml sockets  ldap zip pcntl opcache pdo_mysql mysqli soap ctype  bcmath \
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&& docker-php-ext-install -j$(nproc) gd \
&& docker-php-ext-install -j$(nproc) intl


#  Mcrypt was DEPRECATED in PHP 7.1.0, and REMOVED in PHP 7.2.0.
RUN pecl install mcrypt-1.0.1 \
&& docker-php-ext-enable mcrypt


# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer \
&& composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/



# yaf yar redis
RUN yes | pecl channel-update pecl.php.net && pecl install yaf-3.0.7 \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/yaf.so" > /usr/local/etc/php/conf.d/docker-php-ext-yaf.ini \
    && printf "\n" | pecl install yar-2.0.4 \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/yar.so" > /usr/local/etc/php/conf.d/docker-php-ext-yar.ini \
    && printf "\n" | pecl install redis-4.1.1 \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/redis.so" > /usr/local/etc/php/conf.d/docker-php-ext-redis.ini

# Xdebug
RUN yes | pecl install xdebug-2.6.1 \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_host=172.21.0.1" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_port=9009" >> /usr/local/etc/php/conf.d/xdebug.ini


# SqlServer
RUN yes | wget http://pecl.php.net/get/pdo_sqlsrv-4.3.0.tgz \
    && tar -zxvf pdo_sqlsrv-4.3.0.tgz \
    && cd pdo_sqlsrv-4.3.0 \
    && phpize \
    && ./configure\
    && make  \
    && make install \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/pdo_sqlsrv.so" > /usr/local/etc/php/conf.d/docker-php-ext-pdo_sqlsrv.ini \
    && pecl install sqlsrv \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/sqlsrv.so" > /usr/local/etc/php/conf.d/docker-php-ext-sqlsrv.ini
 

# memcache
RUN yes | git clone https://github.com/websupport-sk/pecl-memcache memcache \
    &&  cd memcache \
    &&  phpize \
    &&  ./configure \
    &&  make && make install \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/memcache.so" > /usr/local/etc/php/conf.d/docker-php-ext-memcache.ini \
    &&  cd ../ \
    &&  rm -rf ./memcache*

# # memcached
# RUN yes | apt-get install -y zlib1g-dev \
#     && wget  https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz \
#     && tar -zxf libmemcached-1.0.18.tar.gz \
#     && cd libmemcached-1.0.18 \
#     && ./configure --prefix=/usr/local/libmemcached --with-memcached \
#     &&  make  &&  make install \
#     &&  printf "/usr/local/libmemcached --with-memcached \n"  | pecl install memcached-3.0.4 \
#     &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/memcached.so" > /usr/local/etc/php/conf.d/docker-php-ext-memcached.ini \
#     &&  cd ../ \
#     &&  rm -rf ./libmemcached-1.0.18*

# Mongodb
RUN yes | pecl install mongodb-1.5.3 \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/mongodb.so" > /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini

# Swoole
RUN yes | pecl install swoole-4.5.2 \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20170718/swoole.so" > /usr/local/etc/php/conf.d/docker-php-ext-swoole.ini



