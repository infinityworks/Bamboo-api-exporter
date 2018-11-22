import requests
import json


class BambooCaller():


    def __init__(self, api_key, organisation):
        self.api_key = api_key
        self.organisation = organisation
        