# -*- coding: utf-8 -*-
import schedule
import time
import telepot
from pprint import pprint
import requests
import datetime
import json
from config import *
from news import *
from weather import condtemp

bot = telepot.Bot(token)



def Morning():
    day = time.strftime('%A')
    bot.sendMessage(user, 'Good Morning' + name)
    time.sleep(3)
    bot.sendMessage(user, 'Today is: ' + time.strftime('%A') + ' ' + time.strftime('%D'))
    time.sleep(3)
    bot.sendMessage(user, 'There are: ' + str(date1.days) + date1name + str(date2.days) + date2name + str(date3.days) + date3name)
    time.sleep(5)
    finweather = condtemp()
    bot.sendMessage(user, finweather)

    if day == "Monday":
        bot.sendMessage(user, 'Today is Monday. The beginning of the week and probably the day your classes will end fast. Today you have:')
        time.sleep(5)
        bot.sendMessage(user, 'First class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Second class:')
        time.sleep(5)
        bot.sendMessage(user, 'Third class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fourth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fifth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Sixth & Seventh class: ')

    elif day == "Tuesday":
        bot.sendMessage(user, 'Today is Tuesday so. Science Today Niceee. Today you have:')
        time.sleep(5)
        bot.sendMessage(user, 'First class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Second class: ' )
        time.sleep(5)
        bot.sendMessage(user, 'Third class: ' )
        time.sleep(5)
        bot.sendMessage(user, 'Fourth class:')
        time.sleep(5)
        bot.sendMessage(user, 'Fifth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Sixth & Seventh class:')

    elif day == "Wednesday":
        bot.sendMessage(user, 'Today is Wednesday. 2 More Days and weekend :D. Today you have:')
        time.sleep(5)
        bot.sendMessage(user, 'First class:')
        time.sleep(5)
        bot.sendMessage(user, 'Second class: Maths. ')
        time.sleep(5)
        bot.sendMessage(user, 'Third class: English. ')
        time.sleep(5)
        bot.sendMessage(user, 'Fourth class: Macedonian.')
        time.sleep(5)
        bot.sendMessage(user, 'Fifth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Sixth & Seventh class: ')

    elif day == "Thursday":
        bot.sendMessage(user, 'Today is Thursday. 1 More Day. You can make it. Today you have:')
        time.sleep(5)
        bot.sendMessage(user, 'First class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Second class:')
        time.sleep(5)
        bot.sendMessage(user, 'Third class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fourth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fifth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Sixth & Seventh class: ')

    elif day == "Friday":
        bot.sendMessage(user, 'Today is Friday. School ended finnaly. Today you have:')
        time.sleep(5)
        bot.sendMessage(user, 'First class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Second class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Third class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fourth class: ')
        time.sleep(5)
        bot.sendMessage(user, 'Fifth class:')
        time.sleep(5)
        bot.sendMessage(user, 'Sixth & Seventh class: ')
    elif day == "Saturday":
        bot.sendMessage(user, 'Today is Saturday. You can relax yeey')
    else:
        bot.sendMessage(user, 'Time flied so fast that it's sunday. Relax because this is your last day you can enjoy yourself!')
        
    bot.sendMessage(user, "Ok Enough from me telling you about the day. Here are some articles you might find interesting to read:")

    news1tosend = newsfunc1()
    bot.sendMessage(user, news1tosend.url)
    time.sleep(5)
    news2tosend = newsfunc2()
    bot.sendMessage(user, news2tosend.url)
    time.sleep(5)
    news3tosend = newsfunc3()
    bot.sendMessage(user, news3tosend)
    time.sleep(5)
    news4tosend = newsfunc4()
    bot.sendMessage(user, news4tosend)
    time.sleep(120)
    bot.sendMessage(user, 'Have a Good day! Be safe.')

schedule.every().day.at("7:30").do(Morning)

while True:
    schedule.run_pending()
