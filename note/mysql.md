



MySQL忘记密码

1. 窗口1：
    - 管理员打开cmd窗口输入命令：net stop mysql
    - 切到MySQL的bin目录
        - MySQL 8.0.x 版本推荐使用：mysqld --console --skip-grant-tables --shared-memory
        - 低版本MySQL数据库：mysqld --skip-grant-tables
        - mysqld -nt --skip-grant-tables
2. 窗口2：
    - 
    - flush privileges;
    - set password for root@localhost='root':



