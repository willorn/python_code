



**OpenSSL SSL_read: Connection was reset, errno 10054的解决方法**

这是服务器的SSL证书没有经过第三方机构的签署，所以报错。
错误原因可能是网络不稳定，连接超时造成的，如果你试了多次还是报这个错误，建议你执行下面的命令

```git
git config --global http.sslVerify "false"
```





