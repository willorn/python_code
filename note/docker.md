





/opt/fastlabel/docker/server/docker-compose.yml



### 简介

系统平滑移植，容器虚拟化技术。

Docker是基于Go语言实现的云开源项目。

· 解决了运行环境和配置问题的软件容器， 方便做持续集成并有助于整体发布的容器虚拟化技术。

![image-20230219214304848](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302192143895.png?tximg)

#### 镜像和容器

UnionFS（联合文件系统）：Union文件系统（UnionFS）是一种分层、轻量级并且高性能的文件系统，它支持对文件系统的修改作为一次提交来一层层的叠加，同时可以将不同目录挂载到同一个虚拟文件系统下(unite several directories into a single virtual filesystem)。Union 文件系统是 Docker 镜像的基础。镜像可以通过分层来进行继承，基于基础镜像（没有父镜像），可以制作各种具体的应用镜像。



Docker镜像层都是只读的，容器层是可写的 

![就是为了复用](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302202121578.png?tximg)



镜像分层最大的一个好处就是共享资源，方便复制迁移，就是为了**复用**。



**方法论：**

1. 是什么
2. 能干嘛
3. 去哪下
   1. docker官网：http://www.docker.com
   2. Docker Hub官网：https://hub.docker.com/
4. 怎么玩
5. 永远的helloworld跑起来一次





#### 安装

https://docs.docker.com/engine/install/centos/



```cmd
【安装】
·yum -y install gcc
·yum -y install gcc-c++
·yum install -y yum-utils
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum makecache fast

yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


【启动】
systemctl start docker
docker run hello-world
docker version


【卸载】
·systemctl stop docker
·yum remove docker-ce docker-ce-cli containerd.io
·rm -rf /var/lib/docker
·rm -rf /var/lib/containerd

【个人账号】
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://9cb7fdwl.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

#### hello world

![image-20230219231249305](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302192312329.png?tximg)







### 基础命令

![image-20230220002757209](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302200027254.png?tximg)

#### 帮助

```
·启动docker： systemctl start docker
·停止docker： systemctl stop docker
·重启docker： systemctl restart docker
·查看docker： systemctl status docker
·开机启动： systemctl enable docker
·查看docker概要信息： docker info
·查看docker总体帮助文档： docker --help
·查看docker命令帮助文档： docker 具体命令 --help
```

#### 镜像

```cmd
docker images 
docker images -a
docker search
docker search --limit 5 redis
docker pull nginx
docker pull ubuntu
docker pull redis:6.0.8

df -h
[root@localhost etc]# docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          2         1         72.79MB   72.78MB (99%)
Containers      2         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B


[root@localhost etc]# docker rmi ubuntu:latest 
[root@localhost etc]# docker rmi -f ubuntu:latest 
[root@localhost etc]# docker rmi -f $(docker images -qa)
```



#### 容器

```go
·docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

【交互式】
docker run -it ubuntu
docker run -it ubuntu /bin/bash
docker run -it ubuntu bash
-i: 交互式操作。
-t: 终端。

docker run --help
docker = 宿主机操作系统，无限run出来很多个容器
·run进去容器，ctrl+p+q退出，容器不停止
·run进去容器，exit退出，容器停止

【后台式】
docker run -d redis
```





```cmd
docker ps
docker ps --help
Options:
  -a, --all             Show all containers (default shows just running)
  -n, --last int        Show n last created containers (includes all states) (default -1)
  -l, --latest          Show the latest created container (includes all states)
  -q, --quiet           仅显示容器 ID(静默模式)



docker start [container ID]
docker stop [container ID]
docker restart [container ID]
docker kill [container ID]
docker rm -f $(docker ps -a -q)
docker ps -a -q | xargs docker rm

                                                                              
docker logs [container ID]·查看容器内运行的进程

docker top 容器ID ·查看容器内部细节

·docker inspect 容器ID
·进入正在运行的容器并以命令行交互

·docker exec -it 容器ID /bin/bash
- attach 直接进入容器启动命令的终端，不会启动新的进程 用exit退出，会导致容器的停止。
- exec 是在容器中打开新的终端，并且可以启动新的进程 用exit退出，不会导致容器的停止。


docker cp nginx:/etc/nginx /home/nginx
docker export nginx > nginx-backup-230220.tar
cat 文件名.tar | docker import - 镜像用户/镜像名:镜像版本号
cat nginx-backup-230220.tar | docker import - package/nginx:1.1

```



### 应用

#### 挂载

1、准备nginx标准文件目录

```go
mkdir /home/docker
cd /home/docker
docker run --name nginxtest -d nginx 	#运行一个测试的nginx
docker cp nginxtest:/etc/nginx ./ 		#把容器里的nginx的目录复制
docker rm -f nginxtest 				#删除测试的nginx-test
```

2、挂载指定文件夹

- 在/home/docker/nginx/html写个index.html测试一下是否成功
- 拷贝dist文件夹内的html文件到指定目录下

```cmd
docker run \
  --name aq \
  -d -p 8089:80 \
  -v /home/docker/nginx/html:/usr/share/nginx/html \
  -v /home/docker/nginx/conf.d:/etc/nginx/conf.d \
  -v /home/docker/nginx/nginx.conf:/etc/nginx/nginx.conf \
  -v /home/docker/nginx/log:/var/log/nginx \
  nginx

docker rm -f aqwork-ui
docker run \
  --name aqwork-ui \
  -d -p 8089:8089 \
  -v /home/docker/nginx/html:/usr/share/nginx/html \
  -v /home/docker/nginx/conf.d:/etc/nginx/conf.d \
  -v /home/docker/nginx/log:/var/log/nginx \
  nginx
```
`nginx.conf`这个文件有什么用？？？



3、修改nginx配置，连接到后台端口

```c
server {
    listen       8089;
    #listen  [::]:8089;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
    # extern
    location /api {
        proxy_set_header Host $http_host;
        proxy_set_header  X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        rewrite ^/api/(.*)$ /$1 break;  #重写
        proxy_pass http://192.168.2.9:8888; # 设置代理服务器的协议和地址
     }
    location  /form-generator {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://192.168.2.9:8888;
    }
    location /api/swagger/index.html {
        proxy_pass http://192.168.2.9:8888/swagger/index.html;
     }
}
```



- 写容器名，需要在同一个网络组才能实现

```
server {
        listen 80;
        client_max_body_size 0;
        server_name localhost;

        proxy_read_timeout 6000s;
        proxy_send_timeout 6000s;
        proxy_buffering off;

        location / {
                root   /usr/share/nginx/html;
                index  index.html index.htm;
                try_files $uri $uri/ /index.html;
                add_header Access-Control-Allow-Origin *;
                add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
                add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';
        }

        # 注意维护新增微服务，gateway 路由前缀
        location ~* ^/(auth|admin|airun|oss|base) {
           proxy_pass http://fastlabel-gateway:9999;
           #proxy_set_header Host $http_host;
           proxy_connect_timeout 600s;
           proxy_send_timeout 600s;
           proxy_read_timeout 600s;
           proxy_set_header X-Forwarded-Proto http;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    # 匹配验证码：/code
    location /code {
        proxy_pass http://fastlabel-gateway:9999;
    }

    # websocket
    location /websocket {
        proxy_pass http://fastlabel-gateway:9999;
        proxy_set_header Host $host;
        proxy_set_header X-Real-Ip $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection  "upgrade";
    }
}
```







#### 容器tets





### 参考

https://blog.51cto.com/u_6192297/3299955



