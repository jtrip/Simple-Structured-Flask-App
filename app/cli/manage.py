import click
from flask import current_app


def register(app):
    @app.cli.group()
    def manage():
        """Commands for app management"""

    @manage.command()
    @click.argument("env-var")
    def show(env_var):
        """echo requested environment variable"""
        click.echo(f"{current_app.config.get(env_var)=}")
