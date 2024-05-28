import cela.util
import yaml
import pymysql


def run(action):
    if not cela.util.is_inited():
        print("Please run 'cela init' first.")
        exit(1)
    with open(cela.util.migration_directory() + '/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    connection = pymysql.connect(**config)
    database = config['database']
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"USE {database}")
            while True:
                try:
                    # do up or down migration.
                    current_version = cela.util.get_current_version(connection)
                    if action == 'up':
                        migration_file = cela.util.get_bigger_migration_file(current_version)
                    else:
                        migration_file = cela.util.get_matching_migration_file(current_version)

                    if migration_file is None:
                        print("No waiting migration files.")
                        break

                    connection.begin()

                    # break migrations if there is no greater migration file.
                    if not migration_file:
                        break

                    with open(migration_file, 'r') as file:
                        blueprint = yaml.safe_load(file)
                        for table in blueprint[action]:
                            # single table blueprint from here.
                            table_name = table['table_name']
                            print(f'doing migration of table named: {table_name}')

                            # get existed table.
                            sql = "SHOW TABLES"
                            cursor.execute(sql)
                            existed_tables = [table[0] for table in cursor.fetchall()]

                            # check if the table exists.
                            if table_name in existed_tables:

                                # get table existed columns.
                                sql = f"SHOW COLUMNS FROM {table_name}"
                                cursor.execute(sql)
                                existed_columns = [column[0] for column in cursor.fetchall()]

                                # check if the table should be dropped.
                                if table.get('drop') is True:
                                    sql = f"DROP TABLE IF EXISTS {table_name}"
                                    cursor.execute(sql)
                                    print(f"Dropped table {table_name}.")
                                    continue

                                # check if the table should be renamed.
                                if table.get('new_name') is True:
                                    sql = f"ALTER TABLE {table_name} RENAME TO {table['new_name']}"
                                    cursor.execute(sql)
                                    print(f"Renamed table {table_name} to {table['new_name']}.")
                                    continue

                                # alert table
                                sql = f"ALTER TABLE {table_name} "
                                for column in table['columns']:
                                    column_name = column['name']
                                    print(f'doing migration of column named: {column_name} in {table_name}')
                                    # drop column
                                    if column.get('drop') is True:
                                        sql += f"DROP COLUMN {column_name}"
                                        cursor.execute(sql)
                                        continue

                                    # rename column
                                    if column.get('new_name') is not None:
                                        sql += f"CHANGE COLUMN {column_name} {column['new_name']} "
                                        cursor.execute(sql)

                                    # add column
                                    if column_name not in existed_columns:
                                        column_sql_string = cela.util.column_to_sql(column)
                                        sql += f"ADD COLUMN {column_name} {column_sql_string} "
                                        cursor.execute(sql)

                                    # set default value
                                    if column.get('default') is not None:
                                        sql += f"ALTER COLUMN {column_name} SET DEFAULT {column['default']}"
                                        print(sql)
                                        cursor.execute(sql)

                                    # drop default value
                                    if column.get('drop_default') is True:
                                        sql += f"ALTER COLUMN {column_name} DROP DEFAULT"
                                        cursor.execute(sql)

                                    # set or unset nullable
                                    cela.util.set_column_nullable(connection, table_name, column_name,
                                                                  column.get('nullable'))

                                    # set or unset primary key
                                    cela.util.set_column_primary_key(connection, table_name, column_name,
                                                                     column.get('primary_key'))

                                    # set or unset auto increment
                                    cela.util.set_column_auto_increment(connection, table_name, column_name,
                                                                        column.get('auto_increment'))

                                    # set or unset unique
                                    cela.util.set_column_unique(connection, table_name, column_name,
                                                                column.get('unique'))

                                    # set or unset index
                                    cela.util.set_column_index(connection, table_name, column_name, column.get('index'))

                            else:
                                # table not exists, create new table.
                                sql = f"CREATE TABLE {table_name} ("
                                column_string_array = []
                                for column in table['columns']:
                                    column_sql_string = cela.util.column_to_sql(column)
                                    column_string_array.append(f"{column['name']} {column_sql_string} ")
                                sql += ", ".join(column_string_array)
                                sql += ")"
                                cursor.execute(sql)

                        # if action is up, the current version should be updated to the current filename.
                        if action == 'up':
                            current_version = cela.util.get_version_from_migration_file(migration_file)
                        # if action is down, the current version should be updated to the smaller version filename.
                        if action == 'down':
                            smaller_migration_file = cela.util.get_smaller_migration_file(current_version)
                            if smaller_migration_file is not None:
                                current_version = cela.util.get_version_from_migration_file(smaller_migration_file)
                            else:
                                current_version = 0

                        if current_version is None:
                            raise Exception("Error: current version is None.")

                        sql = f"UPDATE migrations SET version = {current_version} LIMIT 1"
                        cursor.execute(sql)
                        connection.commit()
                        print(f"Migration {migration_file} {action} successfully.")
                except Exception as e:
                    raise
                    # connection.rollback()
                    # print(f"Error: {e}")
                    # break
    finally:
        connection.close()
