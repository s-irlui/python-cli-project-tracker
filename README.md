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

## Project Structure

S.irlui
app/
  models.py
  storage.py
  cli.py
data/
  database.json
tests/
  test_models.py
main.py
requirements.txt
README.md