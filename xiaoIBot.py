# coding=utf8
from wxpy import *

bot = Bot()

my_friend = bot.friends(True)
xiaoi = XiaoI('你申请的 Key', '你申请的 Secret')


# 使用小 i 机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    xiaoi.do_reply(msg)

embed()