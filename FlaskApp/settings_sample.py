"""
Web server settings
"""
# Enter codes for each outlet
rfcodes = {'1': {'on': '', 'off': ''},
           '2': {'on': '', 'off': ''},
           '3': {'on': '', 'off': ''},
           '4': {'on': '', 'off': ''},
           '5': {'on': '', 'off': ''}}


led_pins = {'on': 24, 'off': 23, 'num': 3, 'speed': 0.15}
codesend = {'pin': '0',               # Set pin number (GPIO: 17)
            'length': '189',          # Set pulse length
            'exec': './codesend'}     # Set codesend script path (should be in rfoutlet)

pgh_api_key = ''                      # PGH API key
bus_stops = {'id': [],                # PGH bus stop id
             'name': [],              # Bus stop name
             'max_prd': 1}            # Max number of predictions
