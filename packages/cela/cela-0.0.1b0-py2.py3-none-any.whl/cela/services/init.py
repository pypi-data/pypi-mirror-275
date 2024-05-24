import os
import yaml
import pymysql


def run():
    directory_name = 'migrations'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    print("Starting configurate database connection, you can press CTRL+C to exit.")
    host = input("tell me the host: ")
    port = input("tell me the port: ")
    user = input("tell me the user: ")
    password = input("tell me the password: ")
    database = input("tell me the database: ")
    config = {
        'host': host,
        'port': int(port),
        'user': user,
        'password': password,
        'database': database
    }
    with open('migrations/config.yaml', 'w') as file:
        yaml.dump(config, file)
    config.pop('database')
    connection = pymysql.connect(**config)
    try:
        with connection.cursor() as cursor:
            sql = f"CREATE DATABASE IF NOT EXISTS {database}"
            cursor.execute(sql)
            cursor.execute(f"USE {database}")

            sql = """
                    CREATE TABLE IF NOT EXISTS migrations (
                    version INT PRIMARY KEY
                    )
            """
            cursor.execute(sql)

            sql = "TRUNCATE TABLE migrations"
            cursor.execute(sql)

            sql = """
                    INSERT INTO migrations (version) VALUES (0)
            """
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

    print("Initialized migrations.")
    print("Please check migrations/config.yaml to ensure the connection of database is correct.")
