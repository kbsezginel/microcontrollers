"""
Web server settings
"""
# 433 MHz Outlet Codes -----------------------------------------------------------------------------
rfcodes = {'1': {'on': '', 'off': ''},
           '2': {'on': '', 'off': ''},
           '3': {'on': '', 'off': ''},
           '4': {'on': '', 'off': ''},
           '5': {'on': '', 'off': ''}}
# 433 MHz transmission settings --------------------------------------------------------------------
codesend = {'pin': '0',               # Set pin number (GPIO: 17)
            'length': '189',          # Set pulse length
            'exec': './codesend'}     # Set codesend script path (should be in rfoutlet)
# LED settings -------------------------------------------------------------------------------------
led_settings = {'on': 24,             # Green LED GPIO
                'off': 23,            # Red LED GPIO
                'num': 2,             # Number of times to blink
                'speed': 0.15,        # Speed of blink (s)
                'blink': True}        # Blink when outlets are switched
# Bus API settings ---------------------------------------------------------------------------------
pgh_api_key = ''                      # PGH API key
bus_stops = {'id': [],                # PGH bus stop id
             'name': [],              # Bus stop name
             'max_prd': 1}            # Max number of predictions
# --------------------------------------------------------------------------------------------------
