import subprocess
import datetime
from flask import Flask, render_template, redirect, url_for, request
from blink import blink
from settings import rfcodes, led_pins, codesend

app = Flask(__name__)


def rf_send(num, state):
    if num == '0':
        for outlet in rfcodes.keys():
            code = rfcodes[outlet][state]
            subprocess.call([codesend['exec'], code, '-p', codesend['pin'], '-l', codesend['length']])
    else:
        code = rfcodes[num][state]
        subprocess.call([codesend['exec'], code, '-p', codesend['pin'], '-l', codesend['length']])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/outlet')
def rf_outlet():
    return render_template('rf-outlet.html')


@app.route('/hello/<name>')
def hello(name):
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'name': name,
        'time': timeString
    }
    return render_template('hello.html', **templateData)


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)


# Route for sending RF signal to outlets
@app.route('/postmethod', methods=['POST'])
def get_post():
    outlet, status = request.form['outlet'], request.form['status']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    print('Time: %s | Outlet: %s | Status: %s' % (time, outlet, status))
    rf_send(outlet, status)
    blink(led_pins[status], led_pins['num'], led_pins['speed'])
    return outlet


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
