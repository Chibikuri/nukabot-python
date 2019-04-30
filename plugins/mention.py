from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import time
from datetime import datetime as dt
from datetime import timedelta as delta
veg_list = []

listing = ['きゅうり', '大根']


@respond_to('きゅうり')
def mention_func(message):
    n = int(list(message.body['text'])[-1])
    veg_list.append(('きゅうり', n, dt.now() + delta(hours=14)))
    message.reply('きゅうりを追加しました！')
    num = 0
    for i in veg_list:
        if i[0] == 'きゅうり':
            num += i[1]
    mes = '現在のきゅうりの数は' + str(num) + '本です.'
    message.reply(mes)


@respond_to('大根')
def mention_func(message):
    n = int(list(message.body['text'])[-1])
    for i in range(n):
        veg_list.append(('大根', time.time()))
    message.reply('大根を追加しました！')
    num = veg_list.count('大根')
    mes = '現在の大根の数は' + str(num) + '本です.'
    message.reply(mes)


@respond_to('中身')
def content(message):
    message.reply('今の中身は')
    # kyuuri = veg_list.count('きゅうり')
    # daikon = veg_list.count('大根')
    # message.reply('きゅうり' + str(kyuuri) + '本')
    # message.reply('大根' + str(daikon) + '本')
    # message.reply('です.')


@respond_to('は？')
def good_time(message):
    tabegoro = False
    for i in veg_list:
        if i[2] - dt.now() < delta(minutes=60):
            message.reply(i[0] + i[1] + '本が食べごろです．')
            tabegoro = True
    if tabegoro is not True:
        message.reply('まだ食べごろはありません')


@respond_to('いつ')
def pre_tabegoro(message):
    for i in veg_list:
        tst = str(i[2] - dt.now()).split(':')
        message.reply(i[0] + str(i[1]) + '本があと' + tst[0] + '時間' + tst[1] + '分で食べごろです.')