FROM php:7.2-fpm
# important !! this Dockerfile version is PHP7.2 ,Change URL and config with Other version
# You may need proxy
# RUN export http_proxy=192.168.0.111:1080
# RUN export https_proxy=192.168.0.111:1080

# Update debian Source to aliyun
RUN yes |  echo "deb http://mirrors.163.com/debian/ stretch main non-free contrib" > /etc/apt/sources.list \
    && echo "deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.163.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.163.com/debian/ stretch main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.163.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.163.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib" >> /etc/apt/sources.list \
    && apt-get update
# RUN yes | apt-get update



# mcrypt
RUN apt-get install -y  curl libcurl3 libxml2-dev libldb-dev libldap2-dev libmcrypt-dev libicu-dev sqlite3 libsqlite3-dev libfreetype6-dev libjpeg62-turbo-dev  libcurl4-openssl-dev


RUN docker-php-ext-install json mbstring pdo pdo_sqlite tokenizer simplexml xml sockets  bcmath  zip pcntl opcache pdo_mysql mysqli soap ctype \
&& cp -frp /usr/lib/x86_64-linux-gnu/libldap* /usr/lib/ \
&& docker-php-ext-install ldap \
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&& docker-php-ext-install -j$(nproc) gd \
&& docker-php-ext-install -j$(nproc) intl


# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer


# XDEBUG yaf redis
RUN yes | pecl channel-update pecl.php.net && pecl install xdebug-beta \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.xdebug.remote_host=127.0.0.1" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && printf "\n" | pecl install yaf \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/yaf.so" > /usr/local/etc/php/conf.d/docker-php-ext-yaf.ini \
    && printf "\n" | pecl install yar \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/yar.so" > /usr/local/etc/php/conf.d/docker-php-ext-yar.ini \
    && printf "\n" | pecl install redis \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/redis.so" > /usr/local/etc/php/conf.d/docker-php-ext-redis.ini

# SQL Server
RUN yes | apt-get install wget unixodbc-dev \
    && wget http://pecl.php.net/get/pdo_sqlsrv-4.3.0.tgz \
    && tar -zxvf pdo_sqlsrv-4.3.0.tgz \
    && cd pdo_sqlsrv-4.3.0 \
    && phpize \
    && ./configure\
    && make  \
    && make install \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/pdo_sqlsrv.so" > /usr/local/etc/php/conf.d/docker-php-ext-pdo_sqlsrv.ini \
    && printf "\n" | pecl install sqlsrv \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/sqlsrv.so" > /usr/local/etc/php/conf.d/docker-php-ext-sqlsrv.ini


# memcache &memcached
RUN yes | wget  https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz \
    && tar -zxf libmemcached-1.0.18.tar.gz \
    && cd libmemcached-1.0.18 \
    && ./configure --prefix=/usr/local/libmemcached --with-memcached \
    &&  make  &&  make install \
    &&  printf "/usr/local/libmemcached --with-memcached --disable-memcached-sasl \n" | pecl install memcached \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/memcached.so" > /usr/local/etc/php/conf.d/docker-php-ext-memcached.ini \
    &&  cd ../ \
    &&  rm -rf ./libmemcached-1.0.18*

RUN yes | apt-get install -y git \
    && git clone https://github.com/websupport-sk/pecl-memcache memcache \
    &&  cd memcache \
    &&  phpize \
    &&  ./configure \
    &&  make && make install \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/memcache.so" > /usr/local/etc/php/conf.d/docker-php-ext-memcache.ini \
    &&  cd ../ \
    &&  rm -rf ./memcache*

# Mongodb
RUN yes | apt-get install openssl  libssl-dev \
    &&  pecl install mongodb \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/mongodb.so" > /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini
# Swoole
RUN yes | pecl install swoole \
    &&  echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/swoole.so" > /usr/local/etc/php/conf.d/docker-php-ext-swoole.ini



