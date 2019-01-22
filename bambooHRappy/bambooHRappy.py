from .validation import Validation
import requests


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
        response = requests.get(url, headers=self.headers, timeout=10)
        response_json = self.validation.valid_response(response)

        return response_json


    def get_employee(self, employee_id, *args):
        """Returns a JSON datatype for a specified employee ID and any field names entered"""

        # Check args match bamboo valid fields list
        self.validation.valid_fields(args)

        url = self.base_url + self.organisation + "/v1/employees/" + str(employee_id) + "?fields=" + self.validation.fields_to_url(args)
        response = requests.get(url, headers=self.headers, timeout=10)
        response_json = self.validation.valid_response(response)

        return response_json


    def custom_report(self, report_id):
        """Returns a JSON datatype using BambooHR customer report ID"""

        url = self.base_url + self.organisation + "/v1/reports/" + str(report_id) + "?format=JSON&fd=yes"
        response = requests.get(url, headers=self.headers, timeout=10)
        response_json = self.validation.valid_response(response)

        return response_json

    
    def get_annual_leave(self, start_date, end_date, annual_leave_status):
        """Returns a JSON datatype for all employees annual leave data"""

        # Checks annual leave status is valid 
        self.validation.valid_annual_leave_status(annual_leave_status)

        url = self.base_url + self.organisation + "/v1/time_off/requests/?start=" + str(start_date) + "&end=" + str(end_date) + \
        "&type=1&status=" + str(annual_leave_status) 
        response = requests.get(url, headers=self.headers, timeout=10)
        response_json = self.validation.valid_response(response)
        
        return response_json

    def get_whos_out(self, start_date, end_date):
        """Returns a JSON datatype for all employees who's had time off"""

        url = self.base_url + self.organisation + "/v1/time_off/whos_out/?start=" + str(start_date) + "&end=" + str(end_date)
        response = requests.get(url, headers=self.headers, timeout=10)
        response_json = self.validation.valid_response(response)
        
        return response_json

    

