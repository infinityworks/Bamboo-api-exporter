import unittest
from bambooHRappy.validation import Validation


class TestValidation(unittest.TestCase):

    validator = Validation()

    def test_valid_table_returns_true(self):
        table = 'employmentStatus'
        result = self.validator.valid_table(table)
        self.assertTrue(result)


    def test_valid_table_returns_false(self):
        table = 'jobHistory'
        result = self.validator.valid_table(table)
        self.assertFalse(result)


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


    def test_valid_annual_leave_status_returns_false_if_invalid(self):
        status = 'upcoming'
        result = self.validator.valid_annual_leave_status(status)
        self.assertFalse(result)


    def test_valid_annual_leave_status_returns_true_if_valid(self):
        status = 'approved'
        result = self.validator.valid_annual_leave_status(status)
        self.assertTrue(result)