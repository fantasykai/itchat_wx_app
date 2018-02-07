import itchat
import random
import time
import os
import sys

have_send = False
name_dic = {}

##


group_dic = {'Estino枫': 0, '': 1}
greet_dic = {0: '微信定时消息测试～～～～～～～～', 1: '微信自动短信测试～～～～～～～'}
t = '14:31:10'

itchat.auto_login()
for user in group_dic:
    name_dic[user] = itchat.search_friends(name=user)[0]['UserName']
print('get userInfo successfully!')
for user in group_dic:
    print('姓名:' + user + ' 分组:' + str(group_dic[user]))

while 1:
    if time.strftime("%H:%M:%S") == t:
        if have_send == False:
            for user in group_dic:
                greet = greet_dic[group_dic[user]]
                greet = "哈哈：" + user + "," + greet
                itchat.send(greet, toUserName=name_dic[user])
                print(user + ':' + greet)
            have_send = True
            print('发送完毕！')
