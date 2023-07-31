from wfmarket_preset import WFMarketPreset

warframe_market_api = WFMarketPreset()

item_data = warframe_market_api.get_item('wisp_prime_set')
print(item_data)
