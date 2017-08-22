import json, requests
import time


def usa_weather(city='pittsburgh', state='pa', unit='C'):
    # Change to your location
    url = requests.get('https://query.yahooapis.com/v1/public/yql?q=select item.forecast from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s, %s")&format=json' % (city, state))
    weather = json.loads(url.text)

    # Gets todays High and Low
    today_high = (weather['query']['results']['channel'][0]['item']['forecast']['high'])
    today_low = (weather['query']['results']['channel'][0]['item']['forecast']['low'])
    
    # Gets tomorrows High and Low
    next_high = (weather['query']['results']['channel'][1]['item']['forecast']['high'])
    next_low = (weather['query']['results']['channel'][1]['item']['forecast']['low'])

    # Get weather code of tomorrows forecast
    next_forecast = (weather['query']['results']['channel'][1]['item']['forecast']['code'])

    results = {}
    results['today_high'] = int(today_high)
    results['today_low'] = int(today_low)
    
    
    if unit == 'C':
        # celcius = (f - 32) * (5/9)
        # for key in results:
        #     results[key] = (results[key] - 32) * (5/9)
        th = int(today_high)
        tl = int(today_low)
        results['today_high'] = (th - 32) * 5 / 9
        results['today_low']  = (tl - 32) * 5 / 9
        
    return results['today_high'], results['today_low']



# weather = getWeather('pittsburgh', 'pa')
