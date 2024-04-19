# Budget Tracker Notes

## Core Functionality

- input project, budget, timeline, staff names/rates (think about formats)
- return used budget, remaining budget, burn rate
- ability to input expected burn rates (task- or project-level)
- create snapshots of project status on entry of new inputs
- export table showing status at each point in time (visualize?)

## Future Extensions

- add tasks, expected amounts for comparison against actuals
- dynamic updating

## Data Model

- store record of tracked projects
- structured data (YAML)--single file per project
- information import via CSV and/or specific reports (from Agresso)

## Interface

start with command line, convert to web app later?

## Business Logic

- function to show percent of budget used
- function to show budget remaining (either in value or percentage)
- function to calculate average burn rate
- function to show actual spend over timeline -- compare with plan
- ability to change project status

## To-do

- think about data structure
- implement Project class
  - assign attribute values
  - implement basic methods
  - demonstrate private methods
  - save project updates
  - test Project class
- rework interface
  - clean up text output
- units
  - periods (allow user to specify days, weeks, months)
  - units (assume dollars)
- additional business logic
  - margins
  - tracking against plan
    - allow initial budget by staff/category as CSV
    - store data in SQLite database
    - update of actual spend can be done via CSV or in tracker interface
    - if possible, allow flexible categorization (could be by staff or other category)
    - enable aggregation in reporting if desired
  - staff
  - cost to complete
- export project snapshot
- allow user to retrieve specific info
- could we replace YAML file with an alternative (or include in DB)?

## Steps in budget definition/update

- define CSV structure
- implement CSV import logic
- implement budget update logic (may be combined with above)
- facilitate population of budget data using PID (or PSR)

## Database functionality

- create database
- create project table
- create budget_details table
- add record to project table upon project creation
- add records to budget_details table when budget data is supplied
- query database
- update records in all tables
- remove projects (delete records)
- copy project
