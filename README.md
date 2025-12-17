# Job Allocation System

## Overview
This project implements a simple job allocation system in Python.  
It has been developed as part of a university coursework to demonstrate good
object-oriented design, validation, testing, and version control practices.

The system is intentionally simplified and is not intended to be a full
real-world application.

---

## Features
- Store and manage job allocations
- Enforce validation rules:
  - Positive rate and hours
  - Maximum of 6 hours per job
  - Maximum of 8 hours per worker per day
- Add, edit, and remove jobs
- Search jobs by:
  - Category
  - Rate
  - Worker name and date
- Calculate:
  - Total cost of work per worker
  - Number of jobs per category per worker
- Save and load job data using CSV files

---

## Project Structure
job-allocation-system/

 job.py # Job class (Task 1)

 job_manager.py # JobManager class (Task 2)

 tests/
 test_jobs.py # Pytest test suite (Task 3)

README.md

.gitignore


---

## Design Notes
- The system uses two main classes:
  - `Job`: Represents a single job allocation
  - `JobManager`: Manages a collection of jobs
- Instance variables use underscore naming to indicate privacy.
- Input validation and constraints are enforced using exceptions.
- Searching uses exact matches as specified in the coursework.
- File paths are relative to ensure portability.

---

## Testing
Testing is implemented using the **pytest** framework.

The test suite covers:
- Normal cases
- Boundary conditions
- Exceptional cases

### Running tests
via PyCharm:

Right-click the tests folder
Select Run 'pytest in tests'

From the project root:
```bash
pytest
```

Version Control

The project was developed incrementally using Git and GitHub.
Each major feature was implemented in a separate commit with descriptive
commit messages to demonstrate good versioning practice.

Requirements

Python 3.9+

pytest

Author:
Abdul Hamzeh

Notes

This project does not include a user interface, in accordance with the
coursework specification.
