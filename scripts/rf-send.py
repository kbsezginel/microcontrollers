import os
import subprocess

# Enter codes for each outlet
codes = {'1': {'on': '21811', 'off': '21820'},
         '2': {'on': '21955', 'off': '21964'},
         '3': {'on': '22275', 'off': '22284'},
         '4': {'on': '23811', 'off': '23820'},
         '5': {'on': '29955', 'off': '29964'}}

num = input('Enter outlet number: ')
state = input('Enter on/off: ')

code = codes[num][state]    # Read code from signal
codesend = './codesend'     # Set codesend script path (should be in rfoutlet)
pin = '0'                   # Set pin number (GPIO: 17) 
length = '189'              # Set pulse length

subprocess.call([codesend, code, '-p', pin, '-l', length])
