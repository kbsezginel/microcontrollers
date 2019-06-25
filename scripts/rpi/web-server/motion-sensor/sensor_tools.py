"""
Helper functions for motion sensor.
"""

def init_log(log_file, time_now):
    with open(log_file, 'w') as log:
        log.write('Starting log... %s\n' % time_now.strftime('%d-%m-%Y | %H:%M:%S'))

def write_log(log_file, time_now, n_log):
    with open(log_file, 'a') as log:
        log.write('%3i | %s\n' % (n_log, time_now.strftime('%d-%m-%Y | %H:%M:%S')))
