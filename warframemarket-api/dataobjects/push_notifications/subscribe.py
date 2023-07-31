from dataobjects.default_data_object import DefaultDataObject


class SubscribeData(DefaultDataObject):
    def __init__(self, endpointinteger: str, p256dh: str, auth: str):
        self.device = 'web'
        self.subscription = {
            'endpointinteger': endpointinteger,
            'keys': {
                'p256dh': p256dh,
                'auth': auth
            }
        }
