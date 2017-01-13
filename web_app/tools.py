import json
import numpy


null_stats = {'workoutsnumber':'0', 'totaltime':'0:00:00'}


def from_json_to_object(payload):
    '''
    Load json data into a python object
    :param payload:
    :return: python dictionary
    '''
    return json.loads(json.dumps(payload))


def calc_running_heart_zones(lhtr):
    '''
    Calculates heart rate zones for running
    :param self:
    :param lhtr: lactate heart rate threshold
    ::return: dictioanary with heart zones for running
    '''
    zones = {}
    lhtr = int(lhtr)
    zones['zone_1'] = int(0.85 * lhtr)
    zones['zone_2'] = [int(0.85 * lhtr), int(0.89 * lhtr)]
    zones['zone_3'] = [int(0.90 * lhtr), int(0.94 * lhtr)]
    zones['zone_4'] = [int(0.95 * lhtr), int(0.99 * lhtr)]
    zones['zone_5a'] = [int(1.0 * lhtr), int(1.02 * lhtr)]
    zones['zone_5b'] = [int(1.03 * lhtr), int(1.06 * lhtr)]
    zones['zone_5c'] = int(1.06 * lhtr)

    return zones


def calc_cycling_heart_zones(lhtr):
    '''
    Calculates heart rate zones for cycling
    :param self:
    :param lhtr: lactate heart rate threshold
    :return: dictionary with heart zones for cycling
    '''
    zones = {}
    lhtr = int(lhtr)
    zones['zone_1'] = int(0.81 * lhtr)
    zones['zone_2'] = [int(0.81 * lhtr), int(0.89 * lhtr)]
    zones['zone_3'] = [int(0.90 * lhtr), int(0.93 * lhtr)]
    zones['zone_4'] = [int(0.94 * lhtr), int(0.99 * lhtr)]
    zones['zone_5a'] = [int(1.0 * lhtr), int(1.02 * lhtr)]
    zones['zone_5b'] = [int(1.03 * lhtr), int(1.06 * lhtr)]
    zones['zone_5c'] = int(1.06 * lhtr)

    return zones


def calc_power_zones(ftp):
    '''
    Calculates power zones
    :param ftp: Functional Threshold power
    :return: dictionary with power zones
    '''
    zones = {}
    ftp = int(ftp)
    zones['zone_1'] = int(0.55 * ftp)
    zones['zone_2'] = [int(0.56 * ftp), int(0.75 * ftp)]
    zones['zone_3'] = [int(0.76 * ftp), int(0.90 * ftp)]
    zones['zone_4'] = [int(0.91 * ftp), int(1.05 * ftp)]
    zones['zone_5'] = [int(1.06 * ftp), int(1.2 * ftp)]
    zones['zone_5b'] = int(1.21 * ftp)

    return zones


def compute_workouts_statistics(workouts, sport = None):
    '''
    Compute workouts statistics
    :param workouts: workout dictionary
    :return: dict with workouts statistics
    '''
    # compute the number of workouts
    workouts_stats = {}
    workouts_stats['workoutsnumber'] = len(workouts)

    workouts_stats['totaltime'] = '0:00:00'

    if len(workouts) > 0:
        #compute total time
        workouts_stats['totaltime'] = sum_up_time([v['duration'] for k, v in workouts.iteritems()])

        heart_rate = [v['averageheartrate'] for k,v in workouts.iteritems() if 'averageheartrate' in v]
        power = [v['averagepower'] for k,v in workouts.iteritems() if 'averagepower' in v]
        calories = [v['calories'] for k,v in workouts.iteritems() if 'calories' in v]
        distance = [v['distance'] for k, v in workouts.iteritems()]

        # compute averages
        workouts_stats['averagedistance'] = numpy.mean(distance)
        workouts_stats['averageheartrate'] = numpy.mean(heart_rate)
        workouts_stats['averagepower'] = numpy.mean(power)
        workouts_stats['averagecalories'] = numpy.mean(calories)

        # compute average pace if statistics are by sport
        if sport:
            if sport == "cycling" or sport == "running":
                workouts_stats['averagepace'] = calculate_run_ride_pace(workouts_stats['totaltime'], sum(distance))
            elif sport == "swimming":
                workouts_stats['averagepace'] = calculate_swim_pace(workouts_stats['totaltime'], sum(distance))
    return workouts_stats


def calculate_run_ride_pace(time, distance):
    '''
    Calculate average pace
    :param time: format "HH:MM:SS"
    :param distance: km or miles
    :return: average pace as string
    '''
    hours, minutes, seconds = time.split(':')
    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)

    seconds_per_mile = float(total_seconds) / float(distance)
    minutes_per_mile = int(seconds_per_mile / 60)
    seconds_remainder = int(seconds_per_mile - (minutes_per_mile * 60))

    return '{}:{:0=2d}'.format(minutes_per_mile, seconds_remainder)


def calculate_swim_pace(time, distance):
    '''
    :param time: format "HH:MM:SS"
    :param distance: distance in km
    :return: average pace as time per 100m
    '''
    #distance in meters
    distance *= 1000
    hours, minutes, seconds = time.split(':')
    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)

    seconds_per_100m = float(total_seconds) / float(distance / 100)
    minutes_per_100m = int(seconds_per_100m / 60)
    seconds_remainder = int(seconds_per_100m - (minutes_per_100m * 60))

    return'{}:{:0=2d}'.format(minutes_per_100m, seconds_remainder)


def sum_up_time(timelist):
    '''
    Sum time in the list in the format "HH::MM:SS"
    :param timelist:
    :return: total time
    '''
    totalSecs = 0
    for tm in timelist:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    return  "%d:%02d:%02d" % (hr, min, sec)


def filter_workouts_by_sport(workouts, sport):
    '''
    Filter workouts by sport
    :param workout: workout dict
    :return: workouts filtered by sport
    '''
    filtered_dict = {k: v for k, v in workouts.iteritems() if sport in v['type']}

    return filtered_dict








