注意。如果使用定时任务，请在docker-composer.yml中，将/var/log以及/var/spool/cron/crontabs映射到对应位置，结构可以参考wwwroot/python，本例，使用了定时任务同时启动了 django