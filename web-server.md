# Web Server (Flask)
Using Raspberry PI a web server can be setup to host a site. Using this site Raspberry PI can be controlled to do many things. For example, a home automation site can be set to control lights, outlets and monitor weather, time etc. information.
## Installation
```
pip install flask
```

## Example
Create a python file `app.py` with the following code:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```
Run with `python app.py` to Initialize web server.

Route your browser to `0.0.0.0:50000` to see the message. Alternatively use your IP adress and navigate tp `ip.address:5000` to see the web page. This address should also be accessible to any other device in the same network.


## Deployment
[Flask Deployment Options](http://flask.pocoo.org/docs/0.10/deploying/#deployment-options)
