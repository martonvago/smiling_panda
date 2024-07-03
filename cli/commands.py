import click

from core.logic import get_bamboos_with_min_michelin_stars


@click.command()
def say_hello():
    click.echo('Hello World!')

@click.command()
@click.option('--min-stars', default=0, help='Minimum number of Michelin stars.')
def bamboo(min_stars):
    bamboos = get_bamboos_with_min_michelin_stars(min_stars)

    click.echo(f"Showing only bamboo species satisfying a sophisticated taste level of at least {min_stars} Michelin stars:")
    for bamboo in bamboos:
        click.echo(f"{bamboo.species}: {bamboo.michelin_stars}")