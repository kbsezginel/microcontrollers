import subprocess
import datetime
from flask import Flask, render_template, redirect, url_for, request
from usa_weather import usa_weather
from settings import rfcodes, led_settings, codesend, weather_settings

app = Flask(__name__)


def rf_send(num, state):
    if num == '0':
        for outlet in ['1', '2', '3', '4', '5']:
            code = rfcodes[outlet][state]
            subprocess.call([codesend['exec'], code, '-p', codesend['pin'], '-l', codesend['length']])
    elif num == '10':
        for outlet in ['6', '7', '8', '9']:
            code = rfcodes[outlet][state]
            subprocess.call([codesend['exec'], code, '-p', codesend['pin'], '-l', codesend['length']])
    else:
        code = rfcodes[num][state]
        subprocess.call([codesend['exec'], code, '-p', codesend['pin'], '-l', codesend['length']])


@app.route('/')
def index():
    weather = usa_weather(city=weather_settings['city'],
                          state=weather_settings['state'],
                          unit=weather_settings['unit'],
                          precision=weather_settings['precision'])
    bus_image = url_for('static', filename='img/bus-%s.png' % 75)
    bus_data = {'img': bus_image, 'min': 2, 'time': ''}
    index_data = {'high': weather['high'], 'low': weather['low'], 'bus': bus_data}
    return render_template('index.html', **index_data)

@app.route('/outlet')
def rf_outlet():
    return render_template('rf-outlet.html')

@app.route('/outlet2')
def power_outlet():
    return render_template('power-outlet.html')

@app.route('/led')
def led_page():
    return render_template('led.html')

@app.route('/weather')
def weather_page():
    weather = usa_weather()
    weather_data = {'high': weather['high'], 'low': weather['low']}
    return render_template('weather.html', **weather_data)


# Route for sending RF signal to outlets
@app.route('/postmethod', methods=['POST'])
def get_post():
    outlet, status = request.form['outlet'], request.form['status']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    print('Time: %s | Outlet: %s | Status: %s' % (time, outlet, status))
    rf_send(outlet, status)
    return outlet

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
