from request.web_util import WebUtil
from request.request_type import RequestType
from dataobjects.default_data_object import DefaultDataObject
from dataobjects.auth.signin import SignInData
from request.exceptions import WFMarketInvalidRequestException


class WFMarket:
    def __init__(
            self,
            api_url_base: str = 'https://api.warframe.market/',
            api_url_version: str = 'v1',
            login_url: str = 'https://warframe.market/auth/signin'
    ) -> None:
        self._api_url = api_url_base + api_url_version
        self._login_url = login_url
        self._web_util = WebUtil(self._api_url, self._login_url)

    def request(self, request_type: RequestType, url: str, data: dict | DefaultDataObject | None = None):
        if type(data) is DefaultDataObject:
            data = data.get_as_dict()

        response = self._web_util.request(request_type.value, url, data)

        return self._return_normalized_data(response)

    def signin(self, data: SignInData) -> dict:
        return WFMarket._return_normalized_data(self._web_util.signin(data.get_as_dict()))

    @staticmethod
    def _return_normalized_data(data: dict) -> dict:
        if 'error' in data:
            raise WFMarketInvalidRequestException(data['error'])
        elif 'payload' in data:
            return data['payload']
        else:
            raise WFMarketInvalidRequestException(data)
