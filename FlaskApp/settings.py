"""
Web server settings
"""
# 433 MHz Outlet Codes -----------------------------------------------------------------------------
rfcodes = {'1': {'on': '21811', 'off': '21820'},
           '2': {'on': '21955', 'off': '21964'},
           '3': {'on': '22275', 'off': '22284'},
           '4': {'on': '23811', 'off': '23820'},
           '5': {'on': '29955', 'off': '29964'},
           '6': {'on': '10000', 'off': '10010'},
           '7': {'on': '11000', 'off': '11010'},
           '8': {'on': '12000', 'off': '12010'},
           '9': {'on': '13000', 'off': '13010'}}

# 433 MHz transmission settings --------------------------------------------------------------------
codesend = {'pin': '0',               # Set pin number (GPIO: 17)
            'length': '189',          # Set pulse length
            'exec': './codesend'}     # Set codesend script path (should be in rfoutlet)
# LED settings -------------------------------------------------------------------------------------
led_settings = {'on': 24,             # Green LED GPIO
                'off': 23,            # Red LED GPIO
                'num': 2,             # Number of times to blink
                'speed': 0.15,        # Speed of blink (s)
                'blink': False}       # Blink when outlets are switched
# Bus API settings ---------------------------------------------------------------------------------
pgh_api_key = "LMJrK9vutafSVnViFmFvjaXvY"
bus_stops = {'id': [8245, 3144, 8192],
             'name': ['Summerlea', 'Bellefonte', 'Graham'],
             'max_prd': 1}
# --------------------------------------------------------------------------------------------------
