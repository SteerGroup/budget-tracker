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

CSV (or similar) or SQLite database

## Interface

start with command line, convert to web app later?

## Business Logic

- function to show percent of budget used
- function to show budget remaining (either in value or percentage)
- function to calculate average burn rate

- function to show actual spend over timeline -- compare with plan
