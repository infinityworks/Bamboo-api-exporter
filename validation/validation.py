from validate_fields import bamboo_fields


class Validation():


    def valid_fields(self, fields_tuple):
        """Validates fields entered as arguments"""

        for field in fields_tuple:
            field = str(field)
            if not field in bamboo_fields:
                print(field + ' is not a valid BambooHR field name')
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