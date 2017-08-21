import subprocess
import datetime
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


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
        out = subprocess.check_output('ls')
        print(out)
    else:
        out = subprocess.check_output('pwd')
        print(out)
    return outlet


if __name__ == '__main__':
    app.run(host='0.0.0.0')
