"""
Generate requirements.txt file
"""


def req_txt_gen(project):
    file_location = f"{project.name}/requirements.txt"

    with open(file_location, "w") as file:
        file.write("flask\n")

        if project.project_type == "api":
            # Add flask-restful if project type is API
            file.write("flask-restful\n")

        if project.need_database:
            # Add database requirements
            file.writelines(_database_requirements(project))


def _database_requirements(project):
    db_req = []
    if project.need_database:
        if project.db_type == "SQL":
            db_req.append("sqlalchemy\n")
            if project.db_engine == "Postgres":
                # Add psycopg2-binary if database engine is Postgres
                db_req.append("psycopg2-binary\n")
            elif project.db_engine == "MySQL":
                # Add mysql-connector-python if database engine is MySQL
                db_req.append("mysql-connector-python\n")
        elif project.db_type == "NoSQL":
            # Add mongoengine if database type is NoSQL and engine is MongoDB
            db_req.append("mongoengine") if project.db_engine == "MongoDB" else []
        return db_req
    return []
