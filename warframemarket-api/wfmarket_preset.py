from wfmarket import WFMarket
from request.request_type import RequestType
from dataobjects.push_notifications.subscribe import SubscribeData

is_debug = False


def undocumented(_):
    if is_debug:
        print('This function is not documented in the WFMarket API.')


class WFMarketPreset(WFMarket):
    def __init__(self,
                 api_url_base: str = 'https://api.warframe.market/',
                 api_url_version: str = 'v1',
                 login_url: str = 'https://warframe.market/auth/signin',
                 debug: bool = False
                 ):
        super().__init__(
            api_url_base,
            api_url_version,
            login_url
        )
        global is_debug
        is_debug = debug

    # Items
    def get_all_items(self) -> dict:
        return self.request(RequestType.GET, '/items')

    def get_item(self, item_url_name: str) -> dict:
        return self.request(RequestType.GET, '/items/' + item_url_name)

    def get_item_orders(self, item_url_name: str) -> dict:
        return self.request(RequestType.GET, '/items/' + item_url_name + '/orders')

    def get_item_dropsources(self, item_url_name: str) -> dict:
        return self.request(RequestType.GET, '/items/' + item_url_name + '/dropsources')

    @undocumented
    def get_item_statistics(self, item_url_name: str) -> dict:
        return self.request(RequestType.GET, '/items/' + item_url_name + '/statistics')

    # Profile
    # // TODO: this

    # Liches
    def get_all_lich_weapons(self):
        return self.request(RequestType.GET, '/lich/weapons')

    def get_all_lich_ephemeras(self):
        return self.request(RequestType.GET, '/lich/ephemeras')

    def get_all_sister_quirks(self):
        return self.request(RequestType.GET, '/sister/quirks')

    # Rivens
    def get_all_riven_items(self):
        return self.request(RequestType.GET, '/riven/items')

    def get_all_riven_attributes(self):
        return self.request(RequestType.GET, '/riven/attributes')

    # Misc
    def get_all_locations(self):
        return self.request(RequestType.GET, '/locations')

    def get_all_npcs(self):
        return self.request(RequestType.GET, '/npc')

    def get_all_missions(self):
        return self.request(RequestType.GET, '/missions')

    # Auctions
    # // TODO: this

    # Auction Entry
    def get_auction(self, auction_id: str):
        return self.request(RequestType.GET, '/auctions/entry/' + auction_id)

    def get_auction_bids(self, auction_id: str):
        return self.request(RequestType.GET, '/auctions/entry/' + auction_id + '/bids')

    # Push Notifications
    def push_notifications_subscribe(self, subscribe_data: SubscribeData):
        return self.request(RequestType.POST, '/settings/notifications/push', subscribe_data)

    def push_notifications_unsubscribe(self):
        return self.request(RequestType.DELETE, '/settings/notifications/push')

    def push_notifications_get(self):
        return self.request(RequestType.GET, '/settings/notifications/push')
