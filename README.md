# Python CLI Project Tracker

A command-line project management tool built with Python. It allows administrators to manage users, projects, and tasks using CLI commands.

## Features

- Create and list users
- Add projects to specific users
- View projects assigned to a user
- Add tasks to projects
- Assign task contributors
- Mark tasks as complete
- Save and load data using JSON file I/O
- Pretty terminal tables using Rich
- Unit testing with Pytest

## Tech Used

- Python
- argparse
- json
- os
- Rich
- Pytest
- Pipenv

## Setup

If Pipenv is not installed yet:

```bash
python3 -m pip install --user pipenv
```

Install dependencies:

```bash
pipenv install --dev
```

## Usage

Show all CLI commands:

```bash
pipenv run python main.py
```

Show users, projects, and tasks in one full table:

```bash
pipenv run python main.py list-all
```

Run tests:

```bash
pipenv run pytest
```

## Project Structure

```text
S.irlui
app/
  models.py
  storage.py
  cli.py
data/
  database.json
tests/
  test_models.py
  test_storage.py
main.py
Pipfile
README.md
```
