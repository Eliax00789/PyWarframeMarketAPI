class WFMarketInvalidRequestException(Exception):
    def __init__(self, errors: dict):
        super().__init__('WFMarketInvalidRequestException: ' + str(errors))
