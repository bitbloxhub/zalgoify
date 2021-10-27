import click
import zalgoify

@click.command()
@click.argument("string")
@click.option("--zalgonum", default=5, help="number of zalgos to use")
def main(string, zalgonum):
    click.echo(zalgoify.zalgoify(string, zalgonum))

main()