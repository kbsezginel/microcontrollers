from pghbustime import *
import datetime
import math
from settings import pgh_api_key

api = BustimeAPI(pgh_api_key)

# Summerlea, Bellefonte, Graham
stops = [8245, 3144, 8192, 2566]
stop_names = ['Summerlea', 'Bellefonte', 'Graham', 'Thackeray']


def get_next_buses(predictions, n_bus=2, bus_list=['75', 'P3', '71A', '71C', '71A', '71B']):
    """ Gets next *n_bus* buses that will arrive in given list of stops """
    next_buses = []
    for stop in predictions:
        if predictions[stop]['message'] != 'No arrivals':
            for bus_idx, bus in enumerate(predictions[stop]['bus']):
                if bus in bus_list:
                    min_left = predictions[stop]['min'][bus_idx]
                    bus_time = predictions[stop]['time'][bus_idx]
                    next_buses.append([bus, min_left, bus_time])
    if len(next_buses) > 0:
        next_buses = sorted(next_buses, key=lambda x: x[1])[:n_bus]
    else:
        next_buses = [['75', '100', '???']]
    return next_buses


def get_bus_schedule(stops, stop_names):
    """ Gets bus predictions for given stops """
    now = datetime.datetime.now()
    predictions = {}
    for i, stop in enumerate(stops):
        predictions[stop_names[i]] = dict(bus=[], time=[], min=[], message=[])
        try:
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
                    min_left = int(math.ceil(t_delta.total_seconds() / 60))
                    # print('%s arriving in %i minutes at %i:%i' % (bus_name, min_left, hr, mn))
                    predictions[stop_names[i]]['bus'].append(bus_name)
                    predictions[stop_names[i]]['time'].append('%i:%i' % (hr, mn))
                    predictions[stop_names[i]]['min'].append(min_left)
                    predictions[stop_names[i]]['message'].append('%s in %i minutes' % (bus_name, min_left))
        except Exception as e:
            print(e)
            predictions[stop_names[i]]['message'] = 'No arrivals'
    return predictions


def get_bus_image(bus_name):
    """
    Get corresponding bus icon for pghbustime predictions
    """
    img_dir = 'static/img/'
    img_path = '%sbus-%s.png' % (img_dir, bus_name)
    return img_path


if __name__ == '__main__':
    print(get_bus_schedule(stops, stop_names))
