from pghbustime import *
import datetime
import math
from settings import pgh_api_key

api = BustimeAPI(pgh_api_key)

# Summerlea, Bellefonte, Graham
stops = [8245, 3144, 8192, 2566]
stop_names = ['Summerlea', 'Bellefonte', 'Graham', 'Thackeray']


def get_bus_schedule(stops, stop_names):
    """ Gets bus predictions for given stops """
    now = datetime.datetime.now()
    predictions = {}
    for i, stop in enumerate(stops):
        # print('--------------------------')
        try:
            predictions[stop_names[i]] = dict(bus=[], time=[], min=[], message=[])
            p = api.predictions(stpid=stop)
            if len(p['prd']) > 0:
                for prd in p['prd']:
                    # print(prd['stpnm'])
                    bus_name = str(prd['rt'])
                    date = prd['prdtm'].split()[0]
                    year = int(date[:4])
                    month = int(date[4:6])
                    day = int(date[6:8])

                    taym = prd['prdtm'].split()[1].split(':')
                    hr, mn, sc = [int(tm) for tm in taym]

                    t_bus = datetime.datetime(year, month, day, hr, mn, sc)
                    t_delta = t_bus - now
                    min_left = math.ceil(t_delta.total_seconds() / 60)
                    # print('%s arriving in %i minutes at %i:%i' % (bus_name, min_left, hr, mn))
                    predictions[stop_names[i]]['bus'].append(bus_name)
                    predictions[stop_names[i]]['time'].append('%i:%i' % (hr, mn))
                    predictions[stop_names[i]]['min'].append(min_left)
                    predictions[stop_names[i]]['message'].append('%s in %i minutes' % (bus_name, min_left))
        except Exception as e:
            print(e)
            predictions[stop_names[i]] = dict(message='No arrivals')
            # print('No arrival for: %s' % stop_names[i])
    return predictions


def get_bus_image(bus_name):
    """
    Get corresponding bus icon for pghbustime predictions
    """
    img_dir = 'static/img/'
    img_path = '%sbus-%s.png' % (img_dir, bus_name)


if __name__ == '__main__':
    print(get_bus_schedule(stops, stop_names))
