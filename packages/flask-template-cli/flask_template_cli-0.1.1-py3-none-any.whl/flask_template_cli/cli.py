import os

import typer
from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator

from .templates import init_gen, generate_models, routes_gen, req_txt_gen
from .types import Project

app = typer.Typer()


def _primary_questions():
    q = [
        {
            "name": "name",
            "type": "input",
            "message": "Name of the project:",
            "validate": EmptyInputValidator("Project name cannot be empty")

        },

        {
            "type": "list",
            "name": "project_type",
            "message": "Type of the project:",
            "choices": ["full_stack", "api"]

        },

        {
            "type": "confirm",
            "name": "need_database",
            "message": "Do you need a database? :",
            "default": False
        },

        {
            "type": "confirm",
            "name": "need_auth",
            "message": "Do you need authentication? :",
            "default": False

        }

    ]
    return prompt(q)


def _user_database_choice():
    db_type = prompt([
        {
            "type": "list",
            "name": "database_type",
            "message": "Select the database Type:",
            "choices": ["SQL", "NoSQL"]

        }
    ])

    sql_databases = ["Postgres", "MySQL", "SQLite"]
    nosql_databases = ["MongoDB", "Cassandra", "DynamoDB"]
    db_options = sql_databases if db_type["database_type"] == "SQL" else nosql_databases
    database_engine = prompt({
        "type": "list",
        "name": "database_engine",
        "message": "Select the database engine",
        "choices": db_options
    })

    return {
        "database_type": db_type["database_type"],
        "database_engine": database_engine["database_engine"]

    }


def create_project_structure(project: Project):
    directories = [
        f"{project.name}/app",
        f"{project.name}/app/templates" if project.project_type != "api" else None,
        f"{project.name}/app/static" if project.project_type != "api" else None,
        f"{project.name}/app/models" if project.need_database else None,
        f"{project.name}/app/routes",
        f"{project.name}/app/utils",
        f"{project.name}/tests",
        f"{project.name}/migrations" if project.need_database and project.db_type == "SQL" else None,

    ]

    for directory in directories:
        if directory:
            os.makedirs(directory, exist_ok=True)


def read_template(path: str):
    with open(path, "r") as f:
        return f.read()


def _start_building(project: Project):
    function_calls = [create_project_structure, init_gen, routes_gen, generate_models, req_txt_gen]
    with typer.progressbar(length=len(function_calls), label="Creating project structure") as bar:
        for index in bar:
            function_calls[index](project)
            bar.update(index)


def _install_dependencies(project: Project):
    # ask the user if they want to install the dependencies
    # if yes, then install the dependencies
    # if no, then exit

    q = {
        "type": "confirm",
        "name": "install_dependencies",
        "message": "Do you want to install the dependencies?",
        "default": True

    }
    ans = prompt(q)
    if ans["install_dependencies"]:
        os.system(f"cd {project.name} && pip install -r requirements.txt")
    else:
        typer.echo("Please run 'pip install -r requirements.txt' to install the dependencies",
                   color=typer.colors.YELLOW)


@app.command()
def main():
    project = Project()
    primary_ans = _primary_questions()

    project.name = primary_ans["name"]
    project.project_type = primary_ans["project_type"]
    project.need_database = primary_ans["need_database"]

    if project.need_database:
        ans = _user_database_choice()
        project.db_engine = ans["database_engine"]
        project.db_type = ans["database_type"]

    _start_building(project)
    _install_dependencies(project)

    typer.echo(f"Project {project.name} has been created successfully", color=typer.colors.GREEN)


if __name__ == '__main__':
    typer.run(main)
