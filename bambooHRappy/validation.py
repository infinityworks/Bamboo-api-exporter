import requests
from .validate_fields import bamboo_fields, bamboo_tables


class Validation:


    def valid_table(self, table):
        """Returns false if table name does not appear in list of valid bamboo tables"""
        if not table in bamboo_tables:
            print(table + ' is not a valid BambooHR table name as of Nov 2018')
            return False

        return True


    def valid_fields(self, fields_tuple):
        """Returns false if field name does not appear in list of valid bamboo fields"""
        for field in fields_tuple:
            if not field in bamboo_fields:
                print(field + ' is not a valid BambooHR field name as of Nov 2018')
                return False

        return True


    def fields_to_url(self, fields_tuple):
        """Converts fields tuple into string to be used in URL"""
        fields = []
        for field in fields_tuple:
            fields.append(field + ',')
        
        # Removes last comma from list
        fields = fields[:-1] + [fields[-1][:-1]]

        return ''.join(fields)


    def valid_response(self, api_response):
        """Returns response JSON datatype if response status code is 200.
           Else returns status code error"""
        if api_response.status_code == requests.codes.ok:
            response_json = api_response.json()
            return response_json
        else:
            api_response.raise_for_status()
