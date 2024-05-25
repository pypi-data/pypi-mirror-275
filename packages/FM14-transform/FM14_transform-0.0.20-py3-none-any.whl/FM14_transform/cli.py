import click

@click.command(name='test-command')
def my_cli_command():
    print('Hello, this is my custom pygeoapi CLI command!')