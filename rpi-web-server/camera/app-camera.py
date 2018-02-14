import datetime
from flask import Flask, render_template, redirect, url_for, request
import picamera
from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
    index_data = {'high': weather['high'], 'low': weather['low'], 'bus': bus_data}
    return render_template('index.html', **index_data)


@app.route('/camera')
def camera_page():
    return render_template('camera.html')


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


@app.route('/postcamera', methods=['POST'])
def get_camera():
    req = request.form['request']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d_%H-%M")
    if req == 'photo':
        filename = '%s.jpg' % time
        camera.capture(filename)
    elif req == 'video':
        filename = '%s.h264' % time
        camera.start_recording(filename)
        sleep(5)
        camera.stop_recording()
    return filename


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
