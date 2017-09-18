import os
import subprocess

# Enter codes for each outlet
# rfcodes = {'1': {'on': '', 'off': ''},
#            '2': {'on': '', 'off': ''},
#            '3': {'on': '', 'off': ''},
#            '4': {'on': '', 'off': ''},
#            '5': {'on': '', 'off': ''}}


def rf_send(num, state, codes=codes):
    code = codes[num][state]    # Read code from signal
    codesend = './codesend'     # Set codesend script path (should be in rfoutlet)
    pin = '0'                   # Set pin number (GPIO: 17)
    length = '189'              # Set pulse length
    print('Running codesend with %s | %s ' % (num, state))
    subprocess.call([codesend, code, '-p', pin, '-l', length])
