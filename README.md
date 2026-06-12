# Python CLI Project Tracker

A command-line project management tool built with Python. It allows administrators to manage users, projects, and tasks using CLI commands.

## Features

* Create and list users
* Add projects to specific users
* View projects assigned to a user
* Search projects
* Edit projects
* Add tasks to projects
* Assign task contributors
* Mark tasks as complete
* Delete users, projects, and tasks
* Save and load data using JSON file I/O
* Pretty terminal tables using Rich
* Unit testing with Pytest

## Tech Used

* Python
* argparse
* json
* os
* Rich
* Pytest

## Project Structure

text
python-cli-project-tracker/
│
├── app/
│   ├── base.py
│   ├── models.py
│   ├── storage.py
│   ├── cli.py
│   └── __init__.py
│
├── data/
│   └── database.json
│
├── tests/
│   ├── test_models.py
│   └── test_storage.py
│
├── main.py
├── 
├── pytest.ini
└── README.md



 Usage

Display help:

bash
python main.py --help


Add a user:


python main.py add-user --name "Louis" --email "louis@example.com"


List users:
python main.py list-users


Add a project:
python main.py add-project --title "CLI Tracker" --description "Project Management Tool" --user-id 1


Search projects:
python main.py search-projects --keyword tracker


Edit a project:
python main.py edit-project --project-id 1 --title "Advanced CLI Tracker"


Add a task:
python main.py add-task --title "Create Models" --project-id 1 --contributors "Louis,James"

Mark a task complete:
python main.py complete-task --task-id 1

## Run Tests
pytest


