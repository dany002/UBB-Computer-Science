# 💻 Assignment 06 - 08
## Requirements
- You will solve one of the problems below using simple feature-driven development
- Your program must provide a menu-driven console-based user interface. Implementation details are up to you
- Implementation must employ layered architecture and classes

### For week 8 (25% of grade)
- Implement features 1 and 2
- Have at least 20 procedurally generated items in your application at startup
- Provide specification and tests for all non-UI classes and methods for the first functionality
- Implement and use your own exception classes.

### For week 9 (25% of grade)
- Implement features 3 and 4
- Implement **PyUnit test cases**

### For week 10 (50% of grade)
- All features must be implemented

## Bonus possibility (0.1p, deadline week 10)
- 95% unit test code coverage for all modules except the UI (use *PyCharm Professional*, the *[coverage](https://coverage.readthedocs.io/en/coverage-5.3/)* or other modules)

## Bonus possibility (0.2p, deadline week 10)
- Implement a graphical user interface, in addition to the required menu-driven UI. Program can be started with either UI, without changing the source code.

## Problem Statement
### Students Register Management
A faculty stores information about:
- **Student**: `student_id`, `name`
- **Discipline**: `discipline_id`, `name`
- **Grade**: `discipline_id`, `student_id`, `grade_value`

Create an application to:
1. Manage students and disciplines. The user can add, remove, update, and list both students and disciplines.
2. Grade students at a given discipline. Any student may receive one or several grades at any discipline. Deleting a student also removes their grades. Deleting a discipline deletes all grades at that discipline for all students.
3. Search for disciplines/students based on ID or name/title. The search must work using case-insensitive, partial string matching, and must return all matching disciplines/students.
4. Create statistics:
    - All students failing at one or more disciplines (students having an average <5 for a discipline are failing it)
    - Students with the best school situation, sorted in descending order of their aggregated average (the average between their average grades per discipline)
    - All disciplines at which there is at least one grade, sorted in descending order of the average grade(s) received by all students
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying)
