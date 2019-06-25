from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
from rfsend import rf_send

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):
    render_message(location, status)
    return statement('Turning {} {}!'.format(location, status))

def render_message(location, status):
    loc = location.lower()
    status = status.lower()
    if loc == 'lights':
        rf_send('4', status)
        rf_send('5', status)
        rf_send('2', status)
    elif loc == 'christmas':
        rf_send('2', status)
    elif location == 'kettle':
        rf_send('1', status)

if __name__ == '__main__':
    port = 5500 #the custom port you want
    app.run(host='0.0.0.0', port=port)
