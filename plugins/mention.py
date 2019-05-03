from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from datetime import datetime as dt
from datetime import timedelta as delta
import json

veg_list = []
listing = {'きゅうり': 14,
           '大根': 24,
           'だいこん': 24,
           'ミョウガ': 24,
           'にんじん': 30,
           '人参': 30}


@default_reply
def default(message):
    try:
        n = int(list(message.body['text'])[-1])
    except:
        message.reply('本数を入れてください')
        raise Exception('not int')
    veg = ''.join(list(message.body['text'])[:-1])
    if veg in listing:
        add_vegetable(message, veg, listing[veg])
    else:
        message.reply('野菜が登録されていません')


def add_vegetable(message, veg, time):
    n = int(list(message.body['text'])[-1])
    veg_list.append([veg, n, dt.now() + delta(hours=time), dt.now()])
    message.reply(veg + 'を追加しました！')
    num = 0
    for i in veg_list:
        if i[0] == veg:
            num += i[1]
    mes = '現在の' + veg + 'の数は' + str(num) + '本です.'
    message.reply(mes)


@respond_to('中身')
def content(message):
    message.reply('今の中身は')
    for content in veg_list:
        tst = str(content[2] - dt.now()).split(':')
        message.reply(tst[0] + '時間後が食べごろの' + content[0] + str(content[1]) + '本')
    message.reply('です.')


@respond_to('ある？')
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


@respond_to('とる')
def take(message):
    take_veg = message.body['text']
    vens = take_veg.split(' ')
    if len(vens) != 3:
        message.reply('もう一度入力してください.ex(とる きゅうり 2)')
    else:
        num = int(vens[-1])
        for i, val in enumerate(veg_list):
            if val[0] == vens[1]:
                val[1] = val[1] - num
                message.reply(val[0] + 'を' + str(num) + '本とりました．')
                if val[1] == 0:
                    message.reply(str(val[3]) + 'に漬けた' + val[0] + 'を全てとりました.')
                    del veg_list[i]
                if val[1] < 0:
                    message.reply(str(val[3]) + 'に漬けた' + val[0] + 'を' + str(val[1]) + '本全てとりました')
                    del veg_list[i]
            break
    content(message)
    print(veg_list)

