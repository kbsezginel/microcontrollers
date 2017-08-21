import subprocess
import datetime
from flask import Flask, render_template, redirect, url_for, request
from blink2 import Blink
app = Flask(__name__)

# Enter codes for each outlet
codes = {'1': {'on': '21811', 'off': '21820'},
         '2': {'on': '21955', 'off': '21964'},
         '3': {'on': '22275', 'off': '22284'},
         '4': {'on': '23811', 'off': '23820'},
         '5': {'on': '29955', 'off': '29964'}}


def rf_send(num, state):
    code = codes[num][state]    # Read code from signal
    codesend = './codesend'     # Set codesend script path (should be in rfoutlet)
    pin = '0'                   # Set pin number (GPIO: 17)
    length = '189'              # Set pulse length
    subprocess.call([codesend, code, '-p', pin, '-l', length])


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


@app.route('/postmethod', methods=['POST'])
def get_post():
    outlet, status = request.form['outlet'], request.form['status']
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    print('Time: %s | Outlet: %s | Status: %s' % (time, outlet, status))
    if status == 'on':
        Blink(24, 3, 0.3)
    else:
        Blink(23, 3, 0.3)
    return outlet


if __name__ == '__main__':
    app.run(host='0.0.0.0')
