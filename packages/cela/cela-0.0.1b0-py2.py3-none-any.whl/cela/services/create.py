import yaml
import cela.util
import os


def run(name):
    if not cela.util.is_inited():
        print("Please run 'cela init' first.")
        exit(1)

    files = os.listdir('migrations')
    migration_files = [f for f in files if f[:8].isdigit()]
    if migration_files:
        max_number = max(int(f[:8]) for f in migration_files)
    else:
        max_number = 0
    new_number = str(max_number + 1).zfill(8)
    file_name = f'migrations/{new_number}_{name}.yaml'

    data = {
        "database_name": "",
        "up": [
            {
                "table_name": "",
                "columns": [
                    {
                        "name": "id",
                        "type": "int",
                        "primary_key": True,
                        "auto_increment": True
                    }
                ]
            }
        ],
        "down": [
            {
                "table_name": "",
                "drop": True
            }
        ]
    }

    with open(file_name, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

    print(f"Created migration: {file_name}")
