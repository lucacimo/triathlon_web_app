users = \
        [
        {
            'name': 'luca',
            'gender': 'male',
            'age': 33,
            'body': {
                'weight': 65,
                'height': 170
            },
            'fitnessparam': {
                'lhtr': 150,
                'ftp': 123
            }
        },
        {
            'name': 'marco',
            'gender': 'male',
            'age': 25,
            'body': {
                'weight': 68,
                'height': 180
            },
            'fitnessparam': {
                'lhtr': 155,
                'ftp': 150
            }
        },
    ]

dates = ["2017-02-01", "2017-02-02", "2017-02-03"]

workouts = \
            [{
                "type":"cycling",
                "description":"Normal endurance ride",
                "distance":60,
                "duration":"2:00:15",
                "averagepower":200,
                "averageheartrate":140,
                "calories":1500,

                "powerzones":{
                    "zone_5":"0:00:00",
                    "zone_4":"0:10:15",
                    "zone_1":"0:10:00",
                    "zone_3":"0:10:00",
                    "zone_2":"0:10:00"
                },

                "heartratezones":{
                    "zone_5a":"0:00:00",
                    "zones_5c":"0:00:00",
                    "zones_5b":"0:00:00",
                    "zone_4":"0:15:15",
                    "zone_1":"0:10:00",
                    "zone_3":"0:10:00",
                    "zone_2":"0:10:00"
                }
            },
            {
                "type": "running",
                "description": "Interval training",
                "distance": 10,
                "duration": "0:45:30",
                "averageheartrate": 150,
                "calories": 500,

                "heartratezones": {
                    "zone_5a": "0:00:00",
                    "zones_5c": "0:00:00",
                    "zones_5b": "0:00:00",
                    "zone_4": "0:15:15",
                    "zone_1": "0:10:00",
                    "zone_3": "0:10:00",
                    "zone_2": "0:10:00"
                }
            },
{
                "type": "swimming",
                "description": "Technique session",
                "distance": 2,
                "duration": "0:40:15",
                "averageheartrate": 145,
                "calories": 450,

                "heartratezones": {
                    "zone_5a": "0:00:00",
                    "zones_5c": "0:00:00",
                    "zones_5b": "0:00:00",
                    "zone_4": "0:15:15",
                    "zone_1": "0:10:00",
                    "zone_3": "0:10:00",
                    "zone_2": "0:10:00"
                }
            }]