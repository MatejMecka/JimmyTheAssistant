from config import *
import requests
import json

def newsfunc1():

    res = requests.get(news1)
    data = json.loads(res.text)
    url = data['articles'][0]['url']
    return url

def newsfunc2():

    res = requests.get(news2)
    data = json.loads(res.text)
    url = data['articles'][0]['url']
    return url

def newsfunc3():

    res = requests.get(news3)
    data = json.loads(res.text)
    url= data['articles'][0]['url']
    return url

def newsfunc4():

    res = requests.get(news4)
    data = json.loads(res.text)
    url = data['articles'][0]['url']
    return url
