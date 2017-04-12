from config import *
import requests
import json

#I have no other name idea for this function.
def condtemp():
    res = requests.get(weatherurl)
    data = json.loads(res.text)
    condition = data['currently']['summary']
    temperature = data['currently']['temperature']
    temp = round(temperature)
    return 'The weather today is: '  + condition + ' with temperatures around: ' + str(temp) + ' Degrees Celsius'
