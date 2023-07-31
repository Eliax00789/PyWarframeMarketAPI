from dataobjects.auth.signin import SignInData
from wfmarket_preset import WFMarketPreset


warframe_market_api = WFMarketPreset()

sign_in_data = SignInData('your_email@example.com', 'your_password')
warframe_market_api.signin(sign_in_data)

# do stuff as logged-in user
