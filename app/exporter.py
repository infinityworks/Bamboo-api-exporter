import requests
import json
from validation import Validation

class BambooCaller():


    def __init__(self, api_key, organisation):
        self.api_key = api_key
        self.organisation = organisation

    
    def request_table(self, employee_id, table_name):
        """Returns a json structure containing all rows for a specified employee ID and table combination"""

        url = "https://api.bamboohr.com/api/gateway.php/" + self.organisation + "/v1/employees/" + employee_id + "/tables/" + table_name

        headers = {
            "headers": {
                'Authorization': 'Basic ' + self.api_key,
                'Accept': 'application/json',
                'Cache-Control': 'no-cache'
            }
        }

        response = requests.get(url, headers=headers['headers'])
        if response.status_code == requests.codes.ok:
            data = json.loads(response.text)

            return data
        else:
            data.raise_for_status()


    def request_specified_fields(self, employee_id, *args):
        """Returns a json structure for a specified employee ID and any field names entered """

        url = "https://api.bamboohr.com/api/gateway.php/" + self.organisation + "/v1/employees/" + employee_id + "?fields=" + table_name

        headers = {
            "headers": {
                'Authorization': 'Basic ' + self.api_key,
                'Accept': 'application/json',
                'Cache-Control': 'no-cache'
            }
        }

        response = requests.get(url, headers=headers['headers'])
        if response.status_code == requests.codes.ok:
            data = json.loads(response.text)

            return data
        else:
            data.raise_for_status()