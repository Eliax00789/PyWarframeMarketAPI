from request.request_type import RequestType
from wfmarket_preset import WFMarket

# can be altered for new or not implemented endpoints

warframe_market_api = WFMarket()
warframe_market_api.request(RequestType.POST, '/items')
