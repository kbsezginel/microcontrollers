import subprocess
import datetime
from flask import Flask, render_template, redirect, url_for, request
from blink import blink
from usa_weather import usa_weather
from pgh_bus_time import get_bus_schedule, get_next_buses
from settings import rfcodes, led_settings, codesend, bus_stops

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
    weather = usa_weather()
    prd = get_bus_schedule(bus_stops['id'], bus_stops['name'])
    next_buses = get_next_buses(prd, n_bus=1)
    bus_image = url_for('static', filename='img/bus-%s.png' % next_buses[0][0])
    bus_data = {'img': bus_image, 'min': next_buses[0][1], 'time': next_buses[0][2]}
    index_data = {'high': weather['high'], 'low': weather['low'], 'bus': bus_data}
    return render_template('index.html', **index_data)


@app.route('/outlet')
def rf_outlet():
    return render_template('rf-outlet.html')


@app.route('/outlet2')
def rf_outlet():
    return render_template('power-outlet.html')


@app.route('/led')
def led_page():
    return render_template('led.html')


@app.route('/bus-schedule')
def bus_page():
    bus_image = url_for('static', filename='img/bus-75.png')
    # bus_schedule = get_bus_schedule(bus_stops['id'], bus_stops['name'])
    # bus_schedule['image'] = bus_image
    # bus_schedule['bus'] = '75'
    bus_data = {'bus': ['75', '71A'], 'image': bus_image}
    return render_template('bus-schedule.html', **bus_data)


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
    if blink_settings['blink']:
        blink(led_settings[status], led_settings['num'], led_settings['speed'])
    return outlet


# Route for sending RF signal to outlets
@app.route('/blink', methods=['POST'])
def get_blink():
    outlet, status = request.form['outlet'], request.form['status']
    blink(led_settings[status], led_settings['num'], led_settings['speed'])
    return outlet


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
