import unittest
from validation.validation import Validation


class TestValidation(unittest.TestCase):

    validator = Validation()


    def test_valid_fields_returns_true(self):
        field = ('firstName', 'lastName')
        result = self.validator.valid_fields(field)
        self.assertTrue(result)

    
    def test_valid_fields_returns_false(self):
        field = ('firstName', 'primaryName')
        result = self.validator.valid_fields(field)
        self.assertFalse(result)


    def test_fields_to_url_returns_string(self):
        fields = ('firstName', 'lastName')
        result = self.validator.fields_to_url(fields)
        self.assertEqual(result, 'firstName,lastName')