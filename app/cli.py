import argparse
from rich.console import Console
from rich.table import Table

from app.models import User, Project, Task
from app.storage import load_data, save_data, generate_id

console = Console()


def add_user(args):
    data = load_data()

    user_id = generate_id(data["users"], "user_id")
    user = User(user_id, args.name, args.email)

    data["users"].append(user.to_dict())
    save_data(data)

    console.print(f"[green]User added successfully: {args.name}[/green]")


def list_users(args):
    data = load_data()

    table = Table(title="Users")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Email")

    for user in data["users"]:
        table.add_row(str(user["user_id"]), user["name"], user["email"])

    console.print(table)


def add_project(args):
    data = load_data()

    user_exists = any(user["user_id"] == args.user_id for user in data["users"])

    if not user_exists:
        console.print("[red]User not found.[/red]")
        return

    project_id = generate_id(data["projects"], "project_id")
    project = Project(project_id, args.title, args.description, args.user_id)

    data["projects"].append(project.to_dict())
    save_data(data)

    console.print(f"[green]Project added successfully: {args.title}[/green]")


def list_projects(args):
    data = load_data()

    table = Table(title="Projects")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("User ID")

    for project in data["projects"]:
        table.add_row(
            str(project["project_id"]),
            project["title"],
            project["description"],
            str(project["user_id"])
        )

    console.print(table)


def search_projects(args):
    data = load_data()
    keyword = args.keyword.lower()

    results = [
        project for project in data["projects"]
        if keyword in project["title"].lower()
        or keyword in project["description"].lower()
    ]

    table = Table(title=f"Search Results for '{args.keyword}'")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("User ID")

    for project in results:
        table.add_row(
            str(project["project_id"]),
            project["title"],
            project["description"],
            str(project["user_id"])
        )

    console.print(table)

def edit_project(args):
    data = load_data()

    for project in data["projects"]:
        if project["project_id"] == args.project_id:

            if args.title:
                project["title"] = args.title

            if args.description:
                project["description"] = args.description

            save_data(data)

            console.print("[green]Project updated successfully.[/green]")
            return

    console.print("[red]Project not found.[/red]")


def user_projects(args):
    data = load_data()

    projects = [
        project for project in data["projects"]
        if project["user_id"] == args.user_id
    ]

    table = Table(title=f"Projects for User {args.user_id}")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Description")

    for project in projects:
        table.add_row(
            str(project["project_id"]),
            project["title"],
            project["description"]
        )

    console.print(table)


def add_task(args):
    data = load_data()

    project_exists = any(
        project["project_id"] == args.project_id
        for project in data["projects"]
    )

    if not project_exists:
        console.print("[red]Project not found.[/red]")
        return

    task_id = generate_id(data["tasks"], "task_id")
    contributors = args.contributors.split(",") if args.contributors else []

    task = Task(task_id, args.title, args.project_id, contributors)

    data["tasks"].append(task.to_dict())
    save_data(data)

    console.print(f"[green]Task added successfully: {args.title}[/green]")


def list_tasks(args):
    data = load_data()

    tasks = [
        task for task in data["tasks"]
        if task["project_id"] == args.project_id
    ]

    table = Table(title=f"Tasks for Project {args.project_id}")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Project ID")
    table.add_column("Contributors")
    table.add_column("Completed")

    for task in tasks:
        table.add_row(
            str(task["task_id"]),
            task["title"],
            str(task["project_id"]),
            ", ".join(task["contributors"]),
            "Yes" if task["completed"] else "No"
        )

    console.print(table)


def complete_task(args):
    data = load_data()

    for task in data["tasks"]:
        if task["task_id"] == args.task_id:
            task["completed"] = True
            save_data(data)
            console.print("[green]Task marked as complete.[/green]")
            return

    console.print("[red]Task not found.[/red]")
def delete_user(args):
    data = load_data()

    data["users"] = [
        user for user in data["users"]
        if user["user_id"] != args.user_id
    ]

    data["projects"] = [
        project for project in data["projects"]
        if project["user_id"] != args.user_id
    ]

    save_data(data)
    console.print("[green]User deleted successfully.[/green]")


def delete_project(args):
    data = load_data()

    data["projects"] = [
        project for project in data["projects"]
        if project["project_id"] != args.project_id
    ]

    data["tasks"] = [
        task for task in data["tasks"]
        if task["project_id"] != args.project_id
    ]

    save_data(data)
    console.print("[green]Project deleted successfully.[/green]")


def delete_task(args):
    data = load_data()

    data["tasks"] = [
        task for task in data["tasks"]
        if task["task_id"] != args.task_id
    ]

    save_data(data)
    console.print("[green]Task deleted successfully.[/green]")

def build_parser():
    parser = argparse.ArgumentParser(
        description="Python CLI Project Management Tool"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_user_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)
    add_user_parser.set_defaults(func=add_user)

    list_users_parser = subparsers.add_parser("list-users", help="List all users")
    list_users_parser.set_defaults(func=list_users)

    add_project_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--user-id", type=int, required=True)
    add_project_parser.set_defaults(func=add_project)

    list_projects_parser = subparsers.add_parser("list-projects", help="List all projects")
    list_projects_parser.set_defaults(func=list_projects)

    search_projects_parser = subparsers.add_parser(
        "search-projects",
        help="Search projects by title or description"
    )

    edit_project_parser = subparsers.add_parser(
        "edit-project",
        help="Edit an existing project"
    )

    edit_project_parser.add_argument(
        "--project-id",
        type=int,
        required=True
    )

    edit_project_parser.add_argument(
        "--title"
    )

    edit_project_parser.add_argument(
        "--description"
    )

    edit_project_parser.set_defaults(func=edit_project)
    search_projects_parser.add_argument("--keyword", required=True)
    search_projects_parser.set_defaults(func=search_projects)

    user_projects_parser = subparsers.add_parser(
        "user-projects",
        help="Show projects assigned to a user"
    )
    user_projects_parser.add_argument("--user-id", type=int, required=True)
    user_projects_parser.set_defaults(func=user_projects)

    add_task_parser = subparsers.add_parser("add-task", help="Add a task to a project")
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--project-id", type=int, required=True)
    add_task_parser.add_argument("--contributors", required=False)
    add_task_parser.set_defaults(func=add_task)

    list_tasks_parser = subparsers.add_parser("list-tasks", help="List tasks in a project")
    list_tasks_parser.add_argument("--project-id", type=int, required=True)
    list_tasks_parser.set_defaults(func=list_tasks)

    complete_task_parser = subparsers.add_parser(
        "complete-task",
        help="Mark a task as complete"
    )
    complete_task_parser.add_argument("--task-id", type=int, required=True)
    complete_task_parser.set_defaults(func=complete_task)

    delete_user_parser = subparsers.add_parser("delete-user", help="Delete a user")
    delete_user_parser.add_argument("--user-id", type=int, required=True)
    delete_user_parser.set_defaults(func=delete_user)

    delete_project_parser = subparsers.add_parser("delete-project", help="Delete a project")
    delete_project_parser.add_argument("--project-id", type=int, required=True)
    delete_project_parser.set_defaults(func=delete_project)

    delete_task_parser = subparsers.add_parser("delete-task", help="Delete a task")
    delete_task_parser.add_argument("--task-id", type=int, required=True)
    delete_task_parser.set_defaults(func=delete_task)

    return parser





def main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()