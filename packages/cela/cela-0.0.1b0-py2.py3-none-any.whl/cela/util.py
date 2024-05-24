import os
import glob


# Check if the migration system has been initialized.
def is_inited():
    return os.path.exists('migrations')


# Get all migration files that have a version greater than the given version.
def get_greater_migration_files(version):
    all_files = glob.glob('migrations/*.yaml')
    migration_files = []
    for f in all_files:
        basename = os.path.basename(f)
        if not basename[:8].isdigit():
            continue
        if int(basename[:8]) > version:
            migration_files.append(f)
    migration_files = sorted(migration_files, key=lambda f: int(os.path.basename(f)[:8]))
    return migration_files


# Get the migration file that has a version greater than the given version.
def get_greater_migration_file(version):
    migration_files = get_greater_migration_files(version)
    return migration_files[0] if migration_files else None


# Convert column to sql string.
def column_to_sql(column):
    if column.get('type') in ['int', 'integer']:
        column_sql_string = 'INT'
    elif column.get('type') == 'text':
        column_sql_string = 'TEXT'
    elif column.get('type') == 'float':
        column_sql_string = 'FLOAT'
    elif column.get('type') == 'double':
        column_sql_string = 'DOUBLE'
    elif column.get('type') == 'decimal':
        column_sql_string = 'DECIMAL'
    elif column.get('type') == 'boolean':
        column_sql_string = 'BOOLEAN'
    elif column.get('type') == 'date':
        column_sql_string = 'DATE'
    elif column.get('type') == 'datetime':
        column_sql_string = 'DATETIME'
    elif column.get('type') == 'time':
        column_sql_string = 'TIME'
    elif column.get('type') == 'timestamp':
        column_sql_string = 'TIMESTAMP'
    elif column.get('type') == 'json':
        column_sql_string = 'JSON'
    elif column.get('type') == 'binary':
        column_sql_string = 'BLOB'
    else:
        column_sql_string = 'VARCHAR'

    # Set column length.
    if column.get('length') is not None:
        column_sql_string += f"({column['length']})"
    else:
        if column.get('type') in ['string', 'text']:
            column_sql_string += "(255) "
        else:
            column_sql_string += " "

    # Set column primary, default, nullable.
    if column.get('primary') is True:
        column_sql_string += "PRIMARY KEY "
    if column.get('default') is not None:
        column_sql_string += f"DEFAULT {column['default']} "
    if column.get('nullable') is True:
        column_sql_string += "NULL "
    return column_sql_string


# Get the column's data type.
def get_column_data_type(connection, table_name, column_name):
    database = connection.db.decode('utf-8')
    with connection.cursor() as cursor:
        sql = f"""
        SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0] if result else None


# Set column nullable.
def set_column_nullable(connection, table_name, column_name, is_nullable):
    database = connection.db.decode('utf-8')
    if is_nullable is not None:
        # Get the column's current data type.
        data_type = get_column_data_type(connection, table_name, column_name)
        with connection.cursor() as cursor:
            # Check if the column is NOT NULL.
            sql = f"""
            SELECT IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'
            """
            cursor.execute(sql)
            result = cursor.fetchone()

            # Check column status is okay.
            if result and data_type:
                if result[0] == 'YES':
                    existed_nullable = True
                else:
                    existed_nullable = False

                # If current column status is not equal to the new column status about nullable.
                if is_nullable != existed_nullable:
                    if is_nullable:
                        nullable_string = "NULL"
                    else:
                        nullable_string = "NOT NULL"
                    sql = f"ALTER TABLE {table_name} MODIFY {column_name} {data_type} {nullable_string}"
                    cursor.execute(sql)


# Set or unset primary key.
def set_column_primary_key(connection, table_name, column_name, is_primary_key):
    if is_primary_key is not None:
        # Get the column's current data type.
        data_type = get_column_data_type(connection, table_name, column_name)
        with connection.cursor() as cursor:
            # Check if the column is a primary key.
            sql = f"""
            SHOW INDEX FROM {table_name} WHERE Key_name = 'PRIMARY'
            """
            cursor.execute(sql)
            result = cursor.fetchall()

            # The row[4] means seq_in_index in the result.
            if any(row[4] == column_name for row in result) and data_type:
                existed_primary_key = True
            else:
                existed_primary_key = False

            if is_primary_key != existed_primary_key:
                if is_primary_key:
                    sql = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({column_name})"
                else:
                    sql = f"ALTER TABLE {table_name} DROP PRIMARY KEY, ADD COLUMN {column_name} {data_type}"
                cursor.execute(sql)


# Set or unset auto increment.
def set_column_auto_increment(connection, table_name, column_name, is_auto_increment):
    database = connection.db.decode('utf-8')
    if is_auto_increment is not None:
        # Get the column's current data type.
        data_type = get_column_data_type(connection, table_name, column_name)
        with connection.cursor() as cursor:
            # Check if the column is AUTO_INCREMENT.
            sql = f"""
            SELECT EXTRA FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{database}' AND TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'
            """
            cursor.execute(sql)
            result = cursor.fetchone()

            if result and result[0] == 'auto_increment':
                existed_auto_increment = True
            else:
                existed_auto_increment = False

            if is_auto_increment != existed_auto_increment:
                if is_auto_increment:
                    auto_increment_string = " AUTO_INCREMENT"
                else:
                    auto_increment_string = ""
                sql = f"ALTER TABLE {table_name} MODIFY {column_name} {data_type} {auto_increment_string}"
                cursor.execute(sql)


# Set or unset unique.
def set_column_unique(connection, table_name, column_name, is_unique):
    database = connection.db.decode('utf-8')
    if is_unique is not None:
        with connection.cursor() as cursor:
            # Check if the column is UNIQUE.
            sql = f"""
            SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC
            JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KCU
            ON TC.CONSTRAINT_NAME = KCU.CONSTRAINT_NAME
            WHERE TC.TABLE_SCHEMA = '{database}' AND TC.TABLE_NAME = '{table_name}' AND TC.CONSTRAINT_TYPE = 'UNIQUE' AND KCU.COLUMN_NAME = '{column_name}'
            """
            cursor.execute(sql)
            result = cursor.fetchone()

            if result and result[0] > 0:
                existed_unique = True
            else:
                existed_unique = False

            if is_unique != existed_unique:
                if is_unique:
                    sql = f"ALTER TABLE {table_name} ADD UNIQUE ({column_name})"
                else:
                    sql = f"ALTER TABLE {table_name} DROP INDEX {column_name}"
                cursor.execute(sql)


# Set or unset index.
def set_column_index(connection, table_name, column_name, is_index):
    if is_index is not None:
        with connection.cursor() as cursor:
            # Check if the column is INDEX.
            sql = f"""
            SHOW INDEX FROM {table_name} WHERE Column_name = '{column_name}'
            """
            cursor.execute(sql)
            result = cursor.fetchall()

            if result:
                existed_index = True
            else:
                existed_index = False

            if is_index != existed_index:
                if is_index:
                    sql = f"ALTER TABLE {table_name} ADD INDEX ({column_name})"
                else:
                    sql = f"ALTER TABLE {table_name} DROP INDEX {column_name}"
                cursor.execute(sql)


# Set or unset default value.
def set_column_default(connection, table_name, column_name, default_value):
    # Get the column's current data type.
    data_type = get_column_data_type(connection, table_name, column_name)
    with connection.cursor() as cursor:
        # Check if the column has a default value.
        sql = f"""
        SELECT COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table_name}' AND COLUMN_NAME = '{column_name}'
        """
        cursor.execute(sql)
        result = cursor.fetchone()

        if result and result[0] is not None:
            existed_default = True
        else:
            existed_default = False

        # If current column default status is not equal to the new column default status.
        if (default_value is not None) != existed_default:
            if default_value is not None:
                sql = f"ALTER TABLE {table_name} ALTER COLUMN {column_name} SET DEFAULT {default_value}"
            else:
                sql = f"ALTER TABLE {table_name} ALTER COLUMN {column_name} DROP DEFAULT"
            cursor.execute(sql)
