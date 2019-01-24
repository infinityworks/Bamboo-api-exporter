*BambooHR API Version:* V1
*Last update:* 24/01/2019

# BambooHR-api-exporter
Open source toolkit for exporting data via bambooHR's API

### Installation
`pip3 install git+https://github.com/infinityworks/Bamboo-api-exporter.git`

Add into the imports:
`from bambooHRappy.bambooHRappy import bambooHrApi`

### How to use

First, you need to initialise the module within your code.

`bamboo = Bamboo(api_key, organisation)`

This will authenticate yourself when calling the BambooHR API.

You can now run the following:

#### Pull from Bamboo

- To pull back a table of your choosing
  - `bamboo.get_table(employee_id, table_name)`
- To get an employee's details
  - `bamboo.get_employee(employee_id, comma, seperated, data, you, want)`
- Get a custom report
  - `bamboo.custom_report(report_id)`
- Get annual leave for employees
  - `bamboo.get_annual_leave(start_date, end_date, annual_leave_status)`
- Get who's out the office
  - `get_whos_out(self, start_date, end_date)`

#### Post to Bamboo
- Make a holiday request for a user
  - `time_off_request(self, employee_id, approval_status, start_date, end_date, time_off_type_id, amount_of_days)`

An Example:
```
def __init__(self):
        self.bamboo = bambooHrApi(os.environ.get('BAMBOO_API_TOKEN'), 'RocketCorp')

 def pull_leave_data(self, start_date, end_date):
     response = self.bamboo.get_whos_out(start_date, end_date)
     print(response)
     
     ```
