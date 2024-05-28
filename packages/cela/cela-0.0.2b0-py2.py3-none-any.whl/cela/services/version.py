import cela.util
import pymysql
import yaml


def run():
    if not cela.util.is_inited():
        print("Please run 'cela init' first.")
        exit(1)
    with open('migrations/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    connection = pymysql.connect(**config)
    version = cela.util.get_current_version(connection)
    print(f"Current database migration version is {version}.")
