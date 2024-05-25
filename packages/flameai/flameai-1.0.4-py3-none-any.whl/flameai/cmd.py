import os
import subprocess

import click

from ._env import check_hive_env
from .util import set_logger


logger = set_logger()


@click.command()
@click.option('-n', '--name', default='World', help='Name to greet')
def hey(name: str) -> None:
    """Print Hey, {name}!"""
    click.echo(f"Hey, {name}!")


@click.command()
@click.argument('file_name', type=str)
def hive_cli(file_name: str) -> None:
    """Execute Hive query and redirect the output to a CSV file."""
    if not os.path.isfile(f'{file_name}.hql'):
        logger.warning(f'{file_name}.hql not found.')
    elif check_hive_env() != 0:
        logger.warning("Hive not found. Please install Hive and add it to your PATH.")
    else:
        command = f'hive -f {file_name}.hql > {file_name}.csv'
        logger.info(f'Run `{command}`')

        try:
            res = subprocess.run(command, shell=True, text=True)
            if res.returncode != 0:
                logger.warning('Failed to execute query.')
                logger.error(f'Error: {res.stderr}')
                logger.error(f'returncode: {res.returncode}')
        except Exception as e:
            logger.error(f'An Error occurred: {e}')


if __name__ == "__main__":
    hive_cli()
