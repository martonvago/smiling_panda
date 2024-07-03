import click

@click.command()
def say_hello():
    click.echo('Hello World!')