import datetime

name = "NAME" #Your Name
weatherurl = 'https://api.darksky.net/forecast/key/location?units=si' # WeatherAPIKey with Token,Location and the units to be si
token = "366XXXXXXXXXXXXXXXXXX" #Telegram Token
user = "id" #Your ID
news1 = "https://newsapi.org/v1/articles?source=the-verge&sortBy=top&apiKey=key"
news2 = "https://newsapi.org/v1/articles?source=mashable&sortBy=top&apiKey=key"
news3 = "https://newsapi.org/v1/articles?source=independent&sortBy=top&apiKey=key"
news4 = "https://newsapi.org/v1/articles?source=ars-technica&sortBy=top&apiKey=key"
date1 = datetime.datetime(2017, 05, 17) - datetime.datetime.now() #Date of event
date1name = " Days until Google I/O " #Description of event
date2 = datetime.datetime(2017, 12, 31) - datetime.datetime.now() #Date of event
date2name = " until the End of the Year " #Description of Event
date3 = datetime.datetime(2017, 06, 10) - datetime.datetime.now() #Date of Event
date3name = " Days until the End of the School Year " #Description of Event
