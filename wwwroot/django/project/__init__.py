# python3已不支持MySQLdb，改用pymysql并映射成MySQLdb
import pymysql
pymysql.install_as_MySQLdb()