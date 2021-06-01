""" Locust 依赖的第三方库
gevent：在Python中实现协程的第三方库（一种网络库），协程又叫微线程Corouine，使用gevent可以获取极高的并发能力。
flask：Python下的一个Web开发框架，和Django相当。
requests：支持HTTP/HTTPs请求访问的库。
msgpack-python：一种快速、紧凑的二进制序列化格式，使用类似JSON的数据，主要提供MessagePack数据序列化及反序列化的方法。
six：Python 2和Python 3兼容库，用来封装处理Python 2和Python 3之间的差异性。
pyzmq：主要用来实现Locust的分布式模式运行，安装这个第三方库，可以把Locust运行在多个进程或多个机器（分布式）

缺点：不支持对服务器的资源监控需要借助其他监控工具。
使用：既支持python代码执行也可以使用cmd命令行运行。

"""

from locust import HttpLocust,TaskSet,task,between
