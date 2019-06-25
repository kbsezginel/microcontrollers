import os
import subprocess

rfcodes = {'1': {'on': '21811', 'off': '21820'},
           '2': {'on': '21955', 'off': '21964'},
           '3': {'on': '22275', 'off': '22284'},
           '4': {'on': '23811', 'off': '23820'},
           '5': {'on': '29955', 'off': '29964'},
           '6': {'on': '10000', 'off': '10010'},
           '7': {'on': '11000', 'off': '11010'},
           '8': {'on': '12000', 'off': '12010'},
           '9': {'on': '13000', 'off': '13010'}}

def rf_send(num, state, codes=rfcodes):
    code = codes[num][state]    # Read code from signal
    codesend = './codesend'     # Set codesend script path (should be in rfoutlet)
    pin = '0'                   # Set pin number (GPIO: 17)
    length = '189'              # Set pulse length
    print('Running codesend with %s | %s ' % (num, state))
    subprocess.call([codesend, code, '-p', pin, '-l', length])
