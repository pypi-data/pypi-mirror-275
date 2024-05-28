import os
import click
import yaml

from log_driver.init.db import initialize_database


@click.group()
def main():
    pass


@main.command()
@click.option('--file', type=click.Path(exists=True), required=True, help="Path to the YAML file with database connection info.")
def init(file):
    click.echo("""Initialize the database with the specified YAML configuration file.""")
    if not os.path.isfile(file):
        click.echo(f"Error: The file {file} does not exist.")
        return

    with open(file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            initialize_database(config)
        except yaml.YAMLError as exc:
            click.echo(f"Error parsing YAML file: {exc}")
            return


if __name__ == '__main__':
    main()
