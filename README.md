# 监控平台
用于监控客户网站
#sendMail.py
邮件发送模块
1.取关键字：getkeyWord()
返回字典：{'id': 'name'}

2.插入漏洞(匹配所有关键字)：wooyun_insert():
    插入name, link, time
返回id

3.发送邮件：获取邮件设置getMailSet(), 返回['smtp服务器', 'smtp端口', '邮箱账户', '邮箱密码']
    获取关注人的邮箱:
        getFollowMail(keyword_id), 传入匹配到的keyword id, 返回关注人的邮箱列表['1@1.com', '1@2.com']


4.插入漏洞对应的关键字wooyun_keyword_insert():
    插入wooyun表中的id，keyword的id，keyword的name。匹配到多个关键字时，依次插入

5.获取最后更新的链接：wooyun_last()

6.更新最后更新的链接：wooyun_last_update()
