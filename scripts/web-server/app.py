from flask import Flask
from blink2 import Blink
from rf_send import rf_send

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/blink')
def blink():
    Blink(26, 10, 0.3)
    return 'blinking'

@app.route('/5off')
def rf():
    rf_send('5', 'off')
    return 'Closing light 5'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
