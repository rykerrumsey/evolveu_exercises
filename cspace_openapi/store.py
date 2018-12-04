from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

STORES = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99,
                'time_stamp': get_timestamp()
            }
        ]
    },
    {
        'name': 'Holla at your G!',
        'items': [
            {
                'name': 'Gnotes Speakers',
                'price': 200.99,
                'time_stamp': get_timestamp()
            }
        ]
    }
]

def get():
    return [x for x in STORES]
