import json
import requests
import time


def usa_weather(city='pittsburgh', state='pa', unit='C', precision=1):
    """
    Get weekly forecast for given state and city using Yahoo public weather API.
    """
    # Change to your location
    url = requests.get('https://query.yahooapis.com/v1/public/yql?q=select item.forecast from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s, %s")&format=json' % (city, state))
    weather = json.loads(url.text)
    results = {}
    # Gets todays High and Low
    results['high'] = weather['query']['results']['channel'][0]['item']['forecast']['high']
    results['low'] = weather['query']['results']['channel'][0]['item']['forecast']['low']
    results['code'] = weather['query']['results']['channel'][0]['item']['forecast']['code']
    results['text'] = weather['query']['results']['channel'][0]['item']['forecast']['text']

    if unit == 'C':
        results['high'] = round((int(results['high']) - 32) * 5 / 9, precision)
        results['low'] = round((int(results['low']) - 32) * 5 / 9, precision)

    return results


if __name__ == '__main__':
    weather = usa_weather(city='pittsburgh', state='pa', unit='C')
    print(weather['text'])
    print('High: %.1f' % weather['high'])
    print('Low: %.1f' % weather['low'])


"""
Yahoo Weather Codes
0	tornado
1	tropical storm
2	hurricane
3	severe thunderstorms
4	thunderstorms
5	mixed rain and snow
6	mixed rain and sleet
7	mixed snow and sleet
8	freezing drizzle
9	drizzle
10	freezing rain
11	showers
12	showers
13	snow flurries
14	light snow showers
15	blowing snow
16	snow
17	hail
18	sleet
19	dust
20	foggy
21	haze
22	smoky
23	blustery
24	windy
25	cold
26	cloudy
27	mostly cloudy (night)
28	mostly cloudy (day)
29	partly cloudy (night)
30	partly cloudy (day)
31	clear (night)
32	sunny
33	fair (night)
34	fair (day)
35	mixed rain and hail
36	hot
37	isolated thunderstorms
38	scattered thunderstorms
39	scattered thunderstorms
40	scattered showers
41	heavy snow
42	scattered snow showers
43	heavy snow
44	partly cloudy
45	thundershowers
46	snow showers
47	isolated thundershowers
3200	not available
"""
