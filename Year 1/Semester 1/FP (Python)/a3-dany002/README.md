# 💻 Assignment 3

## Requirements
- Use procedural programing and the simple feature-driven software development process
- Provide a command-based console user interface that accepts given commands **exactly** as stated
- Handle the case of incorrect user input by displaying error messages. The program must not crash!
- Use built-in compound types to represent entities in the problem domain and access/modify them using *getter* and *setter* functions
- Have at least 10 items in your application at startup
- Provide **specification** and **tests** for all non-UI functions related to every functionality

## Problem Statement

### Family Expenses
A family wants to manage their monthly expenses. They need an application to store, for a given month, all their expenses. Each expense will be stored using the following elements: `day` (*of the month in which it was made, between 1 and 30, for simplicity*), `amount of money` (positive integer) and `expense type` (one of: `housekeeping`, `food`, `transport`, `clothing`, `internet`, `others`). Write a program that implements the functionalities exemplified below:

**(A) Add a new expense**\
`add <sum> <category>`\
`insert <day> <sum> <category>`\
e.g.\
`add 10 internet` – add to the current day an expense of `10 RON` for internet\
`insert 25 100 food` – insert to day 25 an expense of `100 RON` for food

**(B) Modify expenses**\
`remove <day>`\
`remove <start day> to <end day>`\
`remove <category>`\
`e.g.`\
`remove 15` – remove all expenses for day 15\
`remove 2 to 9` – remove all expenses between days 2 and 9\
`remove food` – remove all expenses for food

**(C) Display expenses with different properties**\
`list`\
`list <category>`\
`list <category> [ < | = | > ] <value>`\
e.g.\
`list` – display all expenses\
`list food` – display all the expenses for `food`\
`list food > 5` - display all `food` expenses with an amount of money `>5`\
`list internet = 44` - display all `internet` expenses with an amount of money `=44`
