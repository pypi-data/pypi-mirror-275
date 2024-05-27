import click

from .create_team import create_team


@click.group()
def teamai():
    """Top-level command group for teamai."""


@teamai.command()
@click.argument("project_name")
def create(project_name):
    """Create a new team."""
    create_team(project_name)


if __name__ == "__main__":
    teamai()
