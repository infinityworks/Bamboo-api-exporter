from .validation import Validation
import requests
import logging

logger = logging.getLogger()

class bambooHrApi:


    def __init__(self, api_key, organisation):

        # Organisation API key
        self.api_key = str(api_key)

        # Organisation name
        self.organisation = str(organisation)

        # BambooHR base url used in api requests
        self.base_url = "https://api.bamboohr.com/api/gateway.php/"

        # Headers setting API key, JSON datatype and cache control
        self.headers = {
                        'Authorization': 'Basic ' + self.api_key,
                        'Accept': 'application/json',
                        'Cache-Control': 'no-cache'
                        }

        # Validation class used to validate arguments and api response
        self.validation = Validation()

    
    def get_table(self, employee_id, table_name):
        """Returns a JSON datatype containing all rows for a specified employee ID and table combination"""

        # Check table name matches valid bamboo tables list
        self.validation.valid_table(table_name)

        url = self.base_url + self.organisation + "/v1/employees/" + str(employee_id) + "/tables/" + str(table_name)
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
        except Exception as error:
            bamboo_error = 'BambooHR Get Table API call has failed - ' + str(error)
            logger.critical(bamboo_error)
            return bamboo_error


        response_json = self.validation.valid_response(response)

        return response_json


    def get_employee(self, employee_id, *args):
        """Returns a JSON datatype for a specified employee ID and any field names entered"""

        # Check args match bamboo valid fields list
        self.validation.valid_fields(args)

        url = self.base_url + self.organisation + "/v1/employees/" + str(employee_id) + "?fields=" + self.validation.fields_to_url(args)
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
        except Exception as error:
            bamboo_error = 'BambooHR Get Employee API call has failed - ' + str(error)
            logger.critical(bamboo_error)
            return bamboo_error

        response_json = self.validation.valid_response(response)

        return response_json


    def custom_report(self, report_id):
        """Returns a JSON datatype using BambooHR customer report ID"""

        url = self.base_url + self.organisation + "/v1/reports/" + str(report_id) + "?format=JSON&fd=yes"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
        except Exception as error:
            bamboo_error = 'BambooHR Get Custom Report API call has failed - ' + str(error)
            logger.critical(bamboo_error)
            return bamboo_error

        response_json = self.validation.valid_response(response)

        return response_json

