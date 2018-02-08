# coding=utf8
from wxpy import *

bot = Bot()

# my_friend = ensure_one(bot.search('xx'))
my_friend = bot.friends(True)
tuling = Tuling(api_key='api_key')


# 图灵
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)


embed()
