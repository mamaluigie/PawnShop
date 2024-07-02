import click





@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="your name", help="the person to greet")
@click.option("--item", prompt="Enter the item name to search on ebay")
# This will be a command line tool to see price to pawn item with information being output
def main(count, name, item):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

    print(item)


if __name__ == '__main__':
    main()