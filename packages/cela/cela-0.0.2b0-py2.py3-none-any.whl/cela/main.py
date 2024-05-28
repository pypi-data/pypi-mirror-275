import argparse
import cela.services.init
import cela.services.create
import cela.services.migrate
import cela.services.reset
import cela.services.version


def main():
    parser = argparse.ArgumentParser(description='Process migrations.')
    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init')

    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('--name', type=str, help='The name of the migration to create.')

    migrate_parser = subparsers.add_parser('migrate')

    rollback_parser = subparsers.add_parser('rollback')

    reset_parser = subparsers.add_parser('reset')

    version_parser = subparsers.add_parser('version')

    args = parser.parse_args()

    if args.command == 'create':
        cela.services.create.run(args.name)
    elif args.command == 'migrate':
        cela.services.migrate.run('up')
    elif args.command == 'rollback':
        cela.services.migrate.run('down')
    elif args.command == 'init':
        cela.services.init.run()
    elif args.command == 'reset':
        cela.services.reset.run()
    elif args.command == 'version':
        cela.services.version.run()
    else:
        print("Invalid command. Please follow the usage below.")
        print("Usage: cela <command>")
        print("Commands:")
        print("  init        Initialize migration configuration. You should run this command first.")
        print("  create      Create a new migration file.")
        print("    --name    The name of the migration to create.")
        print("  migrate     Run all pending migrations.")
        print("  rollback    Rollback the last migration.")
        print("  reset       Reset the migration version.")
        print("  version     Show the current migration version.")


if __name__ == '__main__':
    main()
