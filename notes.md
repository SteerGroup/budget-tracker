# Budget Tracker Notes

## Core Functionality

- [x] Add functionality to access existing projects
- [x] input project, budget, timeline, staff names/rates (think about formats)
- [x] return used budget, remaining budget, burn rate
- ability to input expected burn rates (task- or project-level)
- create snapshots of project status on entry of new inputs
- export table showing status at each point in time (visualize?)

## Future Extensions

- add tasks, expected amounts for comparison against actuals
- dynamic updating

## Data Model

- [x] store record of tracked projects
- information import via CSV and/or specific reports (from Agresso)

## Interface

start with command line, convert to web app later?

## Business Logic

- [x] function to show percent of budget used
- [x] function to show budget remaining (either in value or percentage)
- [x] function to calculate average burn rate
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

## Steps in budget definition/update

- [x] define CSV structure
- [x] implement CSV import logic
- implement budget update logic (may be combined with above)
- facilitate population of budget data using PID (or PSR)
- update budget details via Agresso reports
  - think about logic for assigning hours to tasks
- checking against previous data to identify changes (prompting user to accept)

## Database functionality

- [x] create database
- [x] create project table
- [x] create budget_details table
- [x] add record to project table upon project creation
- [x] add records to budget_details table when budget data is supplied
- [x] query database
- [ ] add dates to DB records to facilitate project history (update queries
  accordingly)
- [ ] remove projects (delete records)
- [ ] copy project

## Next steps

1. add timestamps to DB
2. copy/remove projects
3. implement Agresso report import
