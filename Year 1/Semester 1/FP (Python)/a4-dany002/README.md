# 💻 Assignment 4
## New Requirements
- Continue the problem statement started at **A3** by adding its code to this repository
- Implement **modular programming** by having a **UI** module, a **Functions** module and a **Start** module
## Common with A3
- Use procedural programing and the simple feature-driven software development process
- Provide a console-based user interface that accepts given commands **exactly** as required, and works when additional whitespaces are included
- Use built-in compound types to represent entities in the problem domain and access them using *getter* and *setter* functions
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
e.g.\
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

**(D) Obtain different characteristics of sublists**\
`sum <category>`\
`max day`\
`sort day`\
`sort <category>`\
e.g.\
`sum food` – display the total expense for category `food`\
`max day` – display the day with the maximum expenses\
`sort day` – display the total daily expenses in ascending order by amount of money spent\
`sort food` – display the daily expenses for category `food` in ascending order by amount of money spent

**(E) Filter expenses**\
`filter <category>`\
`filter <category> [ < | = | > ] <value>`\
e.g.\
`filter food` – keep only expenses in category `food`\
`filter books < 100` – keep only expenses in category books with amount of money `<100 RON`\
`filter clothing = 59` – keep only expenses for clothing with amount of money `=59 RON`

**(F) Undo**\
`undo` – the last operation that modified program data is reversed. The user can undo all operations performed since program start by repeatedly calling this function.
