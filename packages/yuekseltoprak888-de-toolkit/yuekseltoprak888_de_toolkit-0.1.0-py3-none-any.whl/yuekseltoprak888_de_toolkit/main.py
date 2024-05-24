import click
from yuekseltoprak888_de_toolkit.vm import start, stop, connect

@click.group()
def cli():
    """CLI for yuekseltoprak888-de-toolkit"""
    pass

# Add commands to the CLI group
cli.add_command(start)
cli.add_command(stop)
cli.add_command(connect)

if __name__ == '__main__':
    cli()
