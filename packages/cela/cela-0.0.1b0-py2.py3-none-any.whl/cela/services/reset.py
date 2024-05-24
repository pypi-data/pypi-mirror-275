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
    try:
        connection.begin()
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for table in tables:
                table_name = table[0]
                # If the table is not 'migrations', drop it.
                if table_name != 'migrations':
                    cursor.execute(f"DROP TABLE {table_name}")
                    print(f"Dropped table {table_name}.")

            sql = f"UPDATE migrations SET version = 0 LIMIT 1"
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        connection.close()
