

## 学习路线

#### 浅层：

了解就好：基本指令，逐渐熟练

#### 中层：



#### 深层：





## 下载Linux

![image-20221014131411820](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202210141314158.png?tximg)


桌面程序占用大量资源



## 网络连接

### 桥接模式

ip addr

### NAT——默认的网络模式



#### Xshell连接linux虚拟机

> 一般来说，**192.168.88.2为网关地址**，**192.168.88.255为广播地址，192.168.88.0一般为网段IP**

![image-20230203184929721](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061745981.png?tximg)

再打开网络适配器（Windows的网络和Internet），找到VMware Network Adapter VMnet8，将IP分配改为手动，这里注意，子网掩码、网关都和刚刚打开的NAT设置里的相同，但是**IP地址不要一模一样**，前面的一样，最后一个小数点后面的改一下，比如我的，NAT里子网地址是0，这改成1。

![image-20230203185212874](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061745982.png?tximg)

![image-20230203185053382](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061745983.png?tximg)

```shell
C:\Users\admin>ping 192.168.88.1

Pinging 192.168.88.1 with 32 bytes of data:
Reply from 192.168.88.1: bytes=32 time<1ms TTL=128
Reply from 192.168.88.1: bytes=32 time<1ms TTL=128
Reply from 192.168.88.1: bytes=32 time<1ms TTL=128
Reply from 192.168.88.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.88.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```





![image-20230206172823453](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061745985.png?tximg)



手动设置静态IP

- 地址和子网掩码与运算之后得到端口号
- DNS是什么？域名解析



**连不上**：

1、重启网络适配器

```shell
以Win10为例：

1.打开网络适配器
2.禁用VMware Network Adapter Vmnet 8
3.再将禁用的网络重新启动，重新连接虚拟机即可。
```

2、参考：[虚拟机与本机可以互ping，但是Xshell连不上虚拟机](https://blog.csdn.net/qq_45069279/article/details/108277352)

3、最后，改了网络适配器并重启，然后就能够正常使用了

![image-20230206174319066](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061745986.png?tximg)



### host only（仅主机模式）

不能上网，只能享受局域网


## shell

### 什么是shell

Linux系统的内核负责对硬件资源的分配、调度等管理任务。 因此，系统内核对计算机的正常运行至关重要， 一 般不建议直接去编辑内核中的参数，而是让用户通过基于系统调用接口开发出的程序或服务来管理计算机，以满足日常工作的需要。Shell就是这样一个工具，充当用户与系统内核沟通的桥梁。
**终端就是一种shell**
![](C:/Users/willorn/Desktop/aebe463af21018df810c397e2d7fd134)


**Power Shell**和**cmd终端**（terminal）有什么区别？

- conhost终端模拟器
- sh (Bourne Shell)（交换式的命令解释器和命令编程语言）：
- 是UNX最初使用的shll,而且在每种UNⅨ上都可以使用
- 在shII编程方面做的很优秀，但是在处理与用户的交互方面做得不如其他几种shell
- bash(Bourne Again Shell):Linux默认，是Bourne Shellf的扩展。
- 完全兼容Bourne Shell,并在他基础上增加了很多特性如命令补全、命令历史等。有灵活和强大的编辑接口，同时有很友好的用户界面。
- 通过上下方向键来调取过往执行过的Liux命令：
- 命令或参数仅需输入前几位就可以用Tb键补全；
- 具有强大的批处理脚本；
- 具有实用的环境变量功能。



### type区分

- 内置命令
- 实际上是shel程序的一部分，其中包含的是一些比较简单的创iux系统命令，这些命令由shell程序识别并在shel程序内部完成运行，通常在linux系统加载运行时shelli就被加载并驻留在系统内存中。
- 内部命令是写在bashyi源码里面的，其执行速度比外部命令快，因为解析内部命令shl不需要创建子进程。比如：cd，echo等。
- 外部命令
- 是iux系统中的实用程序部分，因为实用程序的功能通常都比较强大，所以其包含的程序量也会很大，在系统加载时并不随系统一起被加载到内存中，而是在需要时才将其调用内存。通常外部命令的实体并不包含在shellr中，但是其命令执行过程是由sheI程序控制的。
- shell程序管理外部命令执行的路径查找、加载存放，并控制命令的执行。外部命令是在bash之外额外安装的，通常放在/bi,usr/bin、/sbin、usr/sbin等目录下。可通过“echo$PATH"命令查看外部命令的存储路径，比如：ls、vi等。



## 壳子软件

SSH为Secure Shell的缩写，【SSH】就是一个安全的shell应用程序！他一个软件包，使系统登陆和文件传输都建立在一个安全的网络上。


## 命令

### 快捷键：

man指令帮助


print working dir
list

ll是缩写

记住这一点就行：以/开头的都是绝对路径，不以/开头的都是相对路径
**cd**：cd绝对路径或相对路径（跳转到指定目录）

- cd或cd~（返回当前用户家目录），和windows一样inux会给每一个用户创建一个家目录。
- cd -（返回上一次所在的目录）
- cd ..（返回当前目录的上一级目录）
- ../ 上一级目录
- ./ 当前目录
- ~ 当前用户的家目录



**mkdir & rmdir**：创建或删除指定目录
语法：mkdir【选项】目录名称
选项：

- -p:parents，递归创建多层目录




**cp**
copy source target

- -r:recursive，递归复制整个文件夹

把b所有子文件都复制到b：

- cp -r source target 
- cp a/* b



mv source ../target
mv source newName

rm -rf b

- -f:force强制执行
- -r:recursive递归执行
- rm -rf /*


- touch
- echo
- echo $SHELL
- echo hello > demo.txt
- echo hello2 >> demo.txt
- cat 
- more 
- head -n 5 /etc/profile
- head /etc/profile ： 默认展示10行
- tail -n 200 profile
- tail -f profile： follow追踪日志使用
- wc -l demo.txt 、 wc -w demo.txt 、 字节数wc -c demo.txt
- stat profile
- file profile ： 查看文件类型



## 安装软件

### yum下载文件

YUM （yellowdog updater modified）是 一 个RPM系统的自动更新和软件包安装/卸载器。 它可以自动计算依赖和找出想要安装的软件包

![](C:/Users/willorn/Desktop/0300b2fbab4d98a62add3c998c58760b)

```cmd
yum -y vim
yum search vim
yum --version
yum install vim -y
yum remove vim -y
yum install vim
yum remove vim
// 配置仓库
yum repolist
yum clear
```



### wget

```
wget -P
```




## 文本编辑器

### vim：编辑，查看

- 高亮功能

- ![1658888100676](https://q-1306233034.cos.ap-guangzhou.myqcloud.com/company/202302061725322.png?tximg)

- ```bash
  yum install vim -y
  ```



（1）光标移动

| 操作类型       | 操作键               | 功能            |
| -------------- | -------------------- | --------------- |
| 方向移动       | H J K L或上下左右键  | 上下左右        |
| 翻页           | Page Down或Ctrl+F    | 下翻页          |
|                | Page up 或Ctrl+B     | 上翻页          |
| `行内`快速跳转 | HOME键或 `^` 、数字0 | 跳至行首        |
|                | END键或`$`           | 跳至行尾        |
| 行间快速跳转   | gg                   | 跳转文件的首行  |
|                | n+gg                 | 跳转文件的第n行 |
|                | G                    | 跳转文件的尾行  |



光标移动：

```
Page Down或Ctrl+F
Page up或Ctrl+B
：HOME、END
```

删除、复制、粘贴



```cmd
# 查找单词：
/find
/fastlabel
n、N
# 替换
:s/old/new  只替换该行首个
:s/old/new/g  替换该行全部
:%s/old/new/g  替换该文档全部

:%s/are/is/g
```





#### 1、命令模式

（1）光标移动

| 操作类型     | 操作键              | 功能            |
| ------------ | ------------------- | --------------- |
| 方向移动     | H J K L或上下左右键 | 上下左右        |
| 翻页         | Page Down或Ctrl+F   | 下翻页          |
|              | Page up 或Ctrl+B    | 上翻页          |
| 行内快速跳转 | HOME键或 ^ 、数字0  | 跳至行首        |
|              | END键或$            | 跳至行尾        |
| 行间快速跳转 | gg                  | 跳转文件的首行  |
|              | n+gg                | 跳转文件的第n行 |
|              | G                   | 跳转文件的尾行  |

（2）删除、复制、粘贴

| 操作类型 | 操作键   | 功能                                         |
| -------- | -------- | -------------------------------------------- |
| 删除     | x或Del   | 删除光标处的单个字符                         |
|          | dw       | 删除至一个单词的末尾                         |
|          | d2wgg    | 删除两个字符                                 |
|          | dd       | 删除当前光标所在行                           |
|          | n+dd     | 删除从光标所在行开始的n行内容                |
|          | d^       | 删除当前光标之前到行首的所有字符（不含光标） |
|          | d$       | 从当前光标删除到行尾（包含光标）             |
| 复制     | yy       | 复制当前行整行的内容到剪贴板                 |
|          | nyy(3yy) | 复制从光标所在行开始的n行内容                |
| 粘贴     | p        | 粘贴                                         |
| 替换     | r+字符   | 输入r+字符，替换所在位置字符                 |
|          | R+字符   | 连续替换多个字符                             |

（3）可视模式

可视模式可以进行批量文本的选择：

![1658933533888](https://www.ydlclass.com/doc21xnv/assets/1658933533888.2db866ed.png)

复制粘贴文本，次模式下可进行多行文本复制：

1. v 进入可视模式
2. 移动光标位置
3. 输入y复制文本
4. 输入p粘贴

（4）文件内容查找（区别大小写）

| 操作键 | 功能                             |
| ------ | -------------------------------- |
| /word  | 从上而下在文件中查找字符串“word” |
| n      | 向下查找匹配字符串               |
| N      | 向上查找匹配字符串               |

（5）撤销

```
u	单次撤销操作
U	撤销整行
ZZ   保存当前的文件内容并退出编辑器
```



#### 2、插入模式

| 命令 | 功能             |
| ---- | ---------------- |
| i    | 光标前插入文本   |
| a    | 光标后插入文本   |
| A    | 行末尾插入文本   |
| o    | 光标下行插入文本 |
| O    | 光标上行插入文本 |

#### 3、末行模式

（1）保存文件及退出vi编辑器

| 功能           | 命令             | 备注                 |
| -------------- | ---------------- | -------------------- |
| 保存文件       | :w               | 保存修改的内容       |
|                | :w /root/newfile | 另存为其他文件       |
| 退出vi         | :q               | 未修改退出           |
|                | :q!              | 放弃修改并退出       |
| 保存文件退出vi | :wq              | 保存修改的内容并退出 |
| 行号显示       | :set nu          | 在编辑器中显示行号   |
|                | :set nonu        | 取消编辑器中显示行号 |

| 命令          | 功能           |
| ------------- | -------------- |
| :s/old/new     | 只替换该行首个 |
| :s/old/new/g   | 替换该行全部   |
| :%s/old/new/g | 替换该文档全部 |



### grep：查看

```cmd
# 语法：grep [参数] 查找内容 源文件
grep -c 'mysql-env' my.cnf
grep -n 'content' source.txt
grep 'are' demo.txt
```



### sed：文本文件处理

#### 常规使用

> 以【行】为单位进行处理，可以将数据行进行替换、删除、新增、刷选等特定工作。



选项：

- -n∶使用安静(silent)模式。在一般 sed 的用法中，所有来自被处理和未被处理的数据都会显示在控制台。但如果加上 -n 参数后，则只有经过sed 特殊处理的那一行才会被列出来。
- -i∶直接修改读取的档案内容，而不是由控制台输出。



命令：

- a∶新增， 在下一行插入
- c∶替换， c 的后面可以接字串，这些字串可以取代 n1,n2 之间的行！
- d∶删除，因为是删除啊，所以 d 后面通常不接任何咚咚；
- i∶插入， 在上一行插入
- p∶展示，列出最终的结果。
- s∶替换，可以直接进行取代的工作哩！通常这个 s 的动作可以搭配正规表示法！例如 1,20s/old/new/g 就是啦！



``` cmd
sed [-option] 'command' 输入文本
sed -i 
sed -n '1p' demo.txt
sed -n '1,$p' demo.txt
sed -n '/^首先.*/p' demo.txt   # 找到以“首先”开头的所有行
sed -n '/$。.*/p' demo.txt  # 找到以“句号”结尾的所有行
sed -n '$d' ydlclass.txt # 删除最后一行
```



#### 替换：

c命令，整行替换

```bash
[root@localhost ydlclass]# sed '1c 黄河之水' ydlclass.txt 
黄河之水
苟不教，性乃迁。教之道，贵以专。
昔孟母，择邻处。子不学，断机杼。
[root@localhost ydlclass]# sed '1,3c 黄河之水' ydlclass.txt 
黄河之水
窦燕山，有义方。教五子，名俱扬。
养不教，父之过。教不严，师之惰。
```

s命令

格式：sed 's/要替换的字符串/新的字符串/g' （要替换的字符串可以用正则表达式）

```bash
[root@localhost ydlclass]# sed 's/子/父/g' ydlclass.txt 
人之初，性本善。性相近，习相远。
苟不教，性乃迁。教之道，贵以专。
昔孟母，择邻处。父不学，断机杼。
窦燕山，有义方。教五父，名俱扬。
```



### awk

> excel脚本会用到

```cmd
awk options 'commands' 文件

awk -v FS=" " -v OFS="|" '{print NR,$3,NF}' demo.txt 
# 等价于：
awk -F, '{print NR,$3,NF}' demo.txt
1|工资|4
2|3000|4
3|3200|4
4|4000|4
awk -v OFS="\t" '{print NR,$1,$2,$3,$4}' demo.txt  
1       张三丰  18      3000    研发部
2       李四    25      3200    销售部
3       王五    33      4000    产品部
```



### 查找

#### 1、find

语法：find [搜索范围] [匹配条件]

功能描述：查找文件或目录

参数说明

- -name：按文件名称查找
- -user：按文件拥有者查找
- -size：根按文件大小查找文件（+n大于，-n小于，n等于）



### 压缩解压

#### 1、tar

语法：tar [参数] 包名.tar.gz 待打包的内容

功能描述：打包目录，压缩后的文件格式为.tar.gz

```bash
tar -czvf   名字  文件名    打包并压缩
tar -xzvf   文件名         解压缩并解包，卸货x
tar -cvf    名字  文件名    打包，compile为二进制
```

参数：

- z：zip压缩包就用到这个
- cvf：打包到指定文件（并显示过程）

| 短指令 | 长指令                     | 描述                                                   |
| ------ | -------------------------- | ------------------------------------------------------ |
| -c     | --create                   | 打包                                                   |
| -v     | --verbose                  | 显示详细的tar处理的文件信息的过程                      |
| -f     | --file                     | 要操作的文件名                                         |
| -x     | --extract                  | 解包                                                   |
| -z     | --gzip, --gunzip, --ungzip | 通过 gzip 来进行归档压缩或解压                         |
| -C     | --directory=DIR            | 解压文件至指定的目录，如果是解压到当前目录，可以不加-C |

```bash
tar -xvf demo.tar
tar -xzvf demo.tar.gz -C /etc/sth
```



#### 2、zip和unzip

> 这里重点听一听

语法：

压缩：zip [参数] 包名.zip 待压缩内容

解压：uzip 包名.zip

参数：

- -r：recurse-paths递归压缩目录

```bash
yum install -y zip

```



#### 3、gzip和gunzip

gzip与zip区别主要是适应系统不同，还有就是压缩率不一样，Windows系统下普遍使用zip，Linux系统下面普遍使用gzip。和上者是相通的！

## 进程相关命令

### ps：展示所有的

功能描述：查看系统中所有进程

参数：

- -e：显示所有进程。
- -f：全格式。
- -a：all 显示现行终端机下的所有程序，包括其他用户的程序。
- -u：userlist 以用户为主的格式来显示程序状况
- -x： 显示所有程序，不以终端机来区分 （前面讲过终端有很多类型，不仅显示当前终端）

```bash
ps -ef
ps -aux
```



案例：

```bash
[root@localhost ~]# ps -aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.3 171652 12768 ?        Ss   20:05   0:00 /usr/lib/systemd/systemd rhgb --switched-root --system --de
root           2  0.0  0.0      0     0 ?        S    20:05   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   20:05   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   20:05   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   20:05   0:00 [netns]
```

我们也经常使用-ef参数，这两条命令基本没有区别，都是"显示全部进程"：

```bash
[root@localhost ~]# ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 20:05 ?        00:00:00 /usr/lib/systemd/systemd rhgb --switched-root --system --deserialize 31
root           2       0  0 20:05 ?        00:00:00 [kthreadd]
root           3       2  0 20:05 ?        00:00:00 [rcu_gp]
root           4       2  0 20:05 ?        00:00:00 [rcu_par_gp]
root           5       2  0 20:05 ?        00:00:00 [netns]
```

每一项内容的解释：

| 项      | 含义                                                         |
| ------- | ------------------------------------------------------------ |
| USER    | 进程是由哪个用户产生的                                       |
| PID     | 进程ID                                                       |
| %CPU    | 该进程占用CPU的百分比，占用越高，进程越耗费资源              |
| %MEM    | 该进程占用内存的百分比，占用越高，进程越耗费资源             |
| VSZ     | 占用虚拟内存的大小，单位KB                                   |
| RSS     | 占用实际物理内存的大小，单位KB                               |
| TTY     | 表示该进程在哪个终端中运行，tty1-tty7代表本地控制台终端(tty1-tty6是本地的字符界面终端，tty7是图形终端),pts/0-255代表虚拟终端 |
| STAT    | 进程状态，常用状态有：R（运行）、S（睡眠）、T（停止状态）、s（包含子进程）、+（位于后台） |
| START   | 进程启动时间                                                 |
| TIME    | 进程执行时间，即占用cpu的运算时间，不是系统时间              |
| COMMAND | 产生此进程的命令名                                           |



#### 2、管道命令 |

> 看起来很屌，

我们可以通过管道命令对上一个命令的结果进行过滤：

ps的结果内容太多，我们可以使用管道命令对ps的结果进行二次处理，筛选出满足条件的结果：

```bash
[root@localhost ~]# ps -aux | grep sshd
root         952  0.0  0.8  16084  8564 ?        Ss   20:06   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root        1502  0.0  1.2  19372 11684 ?        Ss   20:10   0:01 sshd: root [priv]
root        1531  0.4  0.8  19704  7668 ?        S    20:10   0:22 sshd: root@pts/0,pts/1
root        1556  0.0  1.2  19372 11596 ?        Ss   20:10   0:00 sshd: root [priv]
root        1606  0.0  0.7  19372  7172 ?        S    20:10   0:00 sshd: root@notty
root      307674  0.0  0.2 221812  2388 pts/0    S+   21:31   0:00 grep --color=auto sshd
```

#### 3、top

语法：top [选项]

功能描述：查看系统健康状态

参数：

- -d秒数：Delay-time，指定top命令每隔几秒更新，默认是3秒。
- -i：Idle-process，使top命令不显示任何闲置或者僵死进程
- -p：Monitor-PIDs ，通过指定监控进程ID来仅仅监控某个进程的状态
- -s：Secure-mode，使top在安全模式运行，去除交互命令所带来的潜在危险



#### 4、pidof

语法：pidof [参数] 服务名称

功能描述：查询某个指定服务进程的pid值

案例：

查看sshd服务的进程id

```bash
[root@localhost ~]# pidof sshd
1127 1118 1113 1093 961
```

终止httpd服务的所有进程

```bash
kill -9 {pid}

[root@localhost ~]# killall httpd
```





#### 2、netstat

如果该命令不能用，需要下载net-tools，yum install net-tools。

语法：netstat [参数]

- -t或--tcp 显示TCP传输协议的连接状况。
- -u或--udp 显示UDP传输协议的连接状况。
- -n或--numeric 直接使用IP地址，而不通过域名服务器。
- -l或--listening 显示监控中的服务器的Socket。
- -p或--programs 显示正在使用Socket的程序的进程号和程序名称。

功能描述：显示整个系统目前网络情况，比如目前的链接、数据包传递数据、路由表内容等

#### 7、who

语法：who [参数]

功能描述：查看当前登入主机的用户终端信息



#### 8、last

语法：last [参数]

功能描述：查看所有的系统登录记录。但是要注意，这些信息是以日志文件保存的，因此黑客可以很容易进行修改，所以不能单纯以该命令来判断是否有黑客入侵。



#### 9、history

语法：history [参数]

功能描述：显示历史执行过的命令

选项：

- -c：清除所有历史记录，但是.bash_history文件内容不会删除





### 关机提示

```bash
shutdown -h 1 "this server will shutdown after 1min"
# 重启
shutdown -r now
reboot
# 关闭系统，等同于shutdown -h now和poweroff
halt
```