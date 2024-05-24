import argparse
import cela.services.init
import cela.services.create
import cela.services.migrate
import cela.services.reset


def main():
    parser = argparse.ArgumentParser(description='Process migrations.')
    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init')

    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('--name', type=str, help='The name of the migration to create')

    migrate_parser = subparsers.add_parser('migrate')

    reset_parser = subparsers.add_parser('reset')

    args = parser.parse_args()

    if args.command == 'create':
        cela.services.create.run(args.name)
    elif args.command == 'migrate':
        cela.services.migrate.run('up')
    elif args.command == 'init':
        cela.services.init.run()
    elif args.command == 'reset':
        cela.services.reset.run()
    else:
        print("Invalid command. Please choose 'create' or 'migrate'.")


if __name__ == '__main__':
    main()
