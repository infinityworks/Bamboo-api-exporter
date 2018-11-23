from validation.validation import Validation
import requests
import json


class BambooHrApi():

    validation = Validation()


    def __init__(self, api_key, organisation):
        self.api_key = str(api_key)
        self.organisation = str(organisation)

    
    def get_table(self, employee_id, table_name):
        """Returns a json structure containing all rows for a specified employee ID and table combination"""

        url = "https://api.bamboohr.com/api/gateway.php/" + self.organisation + "/v1/employees/" + str(
            employee_id) + "/tables/" + str(table_name)

        headers = {
            "headers": {
                'Authorization': 'Basic ' + self.api_key,
                'Accept': 'application/json',
                'Cache-Control': 'no-cache'
            }
        }

        response = requests.get(url, headers=headers['headers'], timeout=10)
        if response.status_code == requests.codes.ok:
            response = json.loads(response.text)

            return response
        else:
            response.raise_for_status()


    def get_employee(self, employee_id, *args):
        """Returns a json structure for a specified employee ID and any field names entered """

        #check args entered are valid fields in bamboo
        self.validation.valid_fields(args)

        url = "https://api.bamboohr.com/api/gateway.php/" + self.organisation + "/v1/employees/" + str(
            employee_id) + "?fields=" + self.validation.fields_to_url(args)

        headers = {
            "headers": {
                'Authorization': 'Basic ' + self.api_key,
                'Accept': 'application/json',
                'Cache-Control': 'no-cache'
            }
        }

        response = requests.get(url, headers=headers['headers'], timeout=10)
        if response.status_code == requests.codes.ok:
            response = json.loads(response.text)

            return response
        else:
            response.raise_for_status()


    def custom_report(self, report_id):
        """Returns a json structure using BambooHR customer report ID"""

        url = "https://api.bamboohr.com/api/gateway.php/" + self.organisation + "/v1/reports/" + str(
            report_id) + "?format=JSON&fd=yes"

        headers = {
            "headers": {
                'Authorization': 'Basic ' + self.api_key,
                'Accept': 'application/json',
                'Cache-Control': 'no-cache'
            }
        }

        response = requests.get(url, headers=headers['headers'], timeout=10)
        if response.status_code == requests.codes.ok:
            response = json.loads(response.text)

            return response
        else:
            response.raise_for_status()


#if __name__ == '__main__':
