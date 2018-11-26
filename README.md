# BambooHR-api-exporter
Open source toolkit for exporting data via bambooHR's API

### Installation
`pip3 install git+https://github.com/infinityworks/Bamboo-api-exporter.git`

### How to use

First, you need to initialise the module within your code.

`bamboo = Bamboo(api_key, organisation)`

This will authenticate yourself when calling the BambooHR API.

You can now run the following:

- To pull back a table of your choosing
  - `bamboo.get_table(employee_id, table_name)`
- To get an employee's details
  - `bamboo.get_employee(employee_id, comma, seperated, data, you, want)`
- Get a custom report
  - `bamboo.custom_report(report_id)`
