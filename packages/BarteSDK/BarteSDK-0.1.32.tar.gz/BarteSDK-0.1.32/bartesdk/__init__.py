from .charges import chargesAPI
from .buyers import buyersAPI
from .reportsellers import ReportSellersAPI
from .plans import plansAPI

class BarteSDK:
    def __init__(self, api_key, env="prd", api_version="v2"):
        self.api_key = api_key
        self.env = env
        self.api_version = api_version
        self.charges = chargesAPI(api_key, env, api_version)
        self.buyers = buyersAPI(api_key, env, api_version)
        self.reportsellers = ReportSellersAPI(api_key, env, api_version)
        self.plans = plansAPI(api_key, env, api_version)
