"""
433 MHz radio signal outlet codes to be used with codesend
"""
# Enter codes for each outlet
rfcodes = {'1': {'on': '21811', 'off': '21820'},
           '2': {'on': '21955', 'off': '21964'},
           '3': {'on': '22275', 'off': '22284'},
           '4': {'on': '23811', 'off': '23820'},
           '5': {'on': '29955', 'off': '29964'}}


led_pins = {'on': 24, 'off': 23, 'num': 3, 'speed': 0.15}
codesend = {'pin': '0',               # Set pin number (GPIO: 17)
            'length': '189',          # Set pulse length
            'exec': './codesend'}     # Set codesend script path (should be in rfoutlet)
