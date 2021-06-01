"""
1、Form请求参数构造
payload={"key1":"valus1","key2":"valus2"}
r = requests.post(url,data=payload)
json请求参数构造
r  = requests.post(url,json=payload)
"""

"""
2、文件上传
files = {'file':open('report.xls','rb'}
r = requests.post(url,files=files)
"""

"""
3、header构造
普通的headers= {"user-agent":"my-app/0.0.1"}
r = requests.get(url,headers=headers)
cookie
cookies=dict(cookies_are="working")
r = requests.get(url,cookies=cookies)
"""

"""
4、响应结果
基本信息：r.url,r.status_code,r.headers,r.cookies
响应结果：
r.text = r.encoding+r.content
r.json()=r.encoding+r.content+ content type json
r.raw.read(10)
对应的请求内容：r.request
"""
"""
5、xml请求
xml=“”“《?xml version="1.0" encoding="utf-8"?>
headers = {"Content-Type":"application/xml"}
r =requests.post(url,data=xml,headrs=headers).text

"""
"""
6、结构化响应断言json/xml
assert r.json()[][]  ==  XXX
assert jsonpath(r.json(),'$..name')[0] == XXX

xml断言
from requests_xml import XMLSession
session=XMLSession()
r = session.get(url)
r.xml.links
item = r.xml.xpaht('//item',first=True)
print(item.test)
"""

"""
Hamcrest 断言
schema断言

"""
"""
使用cookies参数:
headers={"User-Agent":'python-requests/2.23.0'}
cookies = dict(cookies_are='working2')
r = requests.get(url,headers=headers,cookies=cookies)
print(r.requests.headers)

认证体系：
from requests.auth import HTTPBasicAuth
r = requests.get(url,auth = HTTPBasicAuth("authXXX":"2122"))   抓包获取auth的内容

"""
"""
restful结构：
接口格式的规则
Roy_Fielding：https://en.wikipedia.org/wiki/Roy_Fielding 6
论文：https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm 6
GET：获取资源. 参数信息放到请求头
POST：新建／更新资源. 参数信息放到请求体
PUT：更新资源
DELETE：删除资源
"""

"""
测试数据：
数据生成：指标形数据（例如天线，射频信号->nv值，波段等有个明显的界限） 1、边界值：七点法
                 2、笛卡尔积
数据清洗：注意！在测试后进行清理，不是测试前
    创建方法（成员添加，端口占用，多进程 id ，文件残留，文件篡改恢复）：在 teardown 进行销毁
    删除方法（删除文件，删除成员…）：备份及恢复或伪数据
查看调试接口Charles：
    若是https，！！注意！！证书问题，设置verify=False取消证书验证
    ---设置代理proxies，需取消证书验证
    
接口测试提速：需安装并行插件pytest-dev/pytest-xdist 
    pytest执行时 zai Additional Arguments: -n auto,会根据CPU数（CPU逻辑数）进行并行
    注意：并行用例设计不要冲突，1、并行用例中存在数据相同（随机数：时间种子）
                           2、并行用例端口相同
                           3、并行用例本地的文件相同  
               可参考pytest的hook：pytest_collection_modifyitems

"""
"""

GIL锁 多线程是并发
接口跟接口间是由耦合的，但用例直接不能有耦合

"""

"""
接口生命周期：
    需求与设计阶段：接口规范
    研发阶段 
        stub服务接口
        基础测试用例编写设计
    测试阶段
        完整的接口测试用例
        持续集成
"""
"""
Owasp安全测试体系
    dvwa docker部署
    注入：sql注入，命令注入，文件注入
    越权：越过更高权限，越过同级权限
burpsuite

CSRF漏洞介绍与原理
    跨站请求伪造，也被称为one-click attack或者session riding，通常缩写为


"""