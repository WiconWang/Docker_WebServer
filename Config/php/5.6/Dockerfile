FROM php:5.6-fpm
# important !! this Dockerfile version is PHP5.2 ,Change URL and config with Other version

# You may need proxy
# RUN export http_proxy=192.168.0.111:1080
# RUN export https_proxy=192.168.0.111:1080

# Update debian Source to aliyun
RUN yes |  echo "deb http://mirrors.aliyun.com/debian/ jessie main non-free contrib" > /etc/apt/sources.list \
&& echo "deb http://mirrors.aliyun.com/debian/ jessie-updates main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb http://mirrors.aliyun.com/debian/ jessie-backports main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb-src http://mirrors.aliyun.com/debian/ jessie main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb-src http://mirrors.aliyun.com/debian/ jessie-updates main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb-src http://mirrors.aliyun.com/debian/ jessie-backports main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb http://mirrors.aliyun.com/debian-security/ jessie/updates main non-free contrib" >> /etc/apt/sources.list \
&& echo "deb-src http://mirrors.aliyun.com/debian-security/ jessie/updates main non-free contrib" >> /etc/apt/sources.list \
&& apt-get update




# mcrypt
RUN apt-get install -y libmcrypt-dev libicu-dev sqlite3 libsqlite3-dev libjpeg62-turbo-dev  curl libcurl3 libldb-dev openssl  git wget unixodbc-dev \
&& docker-php-ext-install json mbstring pdo pdo_sqlite tokenizer   sockets mcrypt pcntl opcache pdo_mysql mysqli

# bcmath
RUN docker-php-ext-install bcmath

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer \
&& composer config -g repo.packagist composer https://packagist.laravel-china.org


#  yaf redis
RUN yes |pecl download yaf-2.3.5 \
    && tar zxvf yaf-2.3.5.tgz \
    && cd yaf-2.3.5 \
    && phpize \
    && ./configure \
    && make && make install \
    && echo "extension=yaf.so" > /usr/local/etc/php/conf.d/docker-php-ext-yaf.ini \
    && cd ../ && rm -rf yaf-2.3.5* \
    && printf "\n"
# RUN yes | pecl install yar \
#     && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/yar.so" > /usr/local/etc/php/conf.d/docker-php-ext-yar.ini \
#     && printf "\n"
RUN no | pecl install redis-4.1.0 \
    && echo "extension=redis.so" > /usr/local/etc/php/conf.d/docker-php-ext-redis.ini \
    && printf "\n"


# XDEBUG
RUN yes | pecl install xdebug-2.5.5 \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_host=172.17.0.1" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_port=9009" >> /usr/local/etc/php/conf.d/xdebug.ini

        #Mongodb
RUN yes | pecl install mongodb-1.5.1 \
    &&  echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini

RUN yes | pecl install swoole-2.0.11 \
    &&  echo "extension=swoole.so" > /usr/local/etc/php/conf.d/docker-php-ext-swoole.ini






