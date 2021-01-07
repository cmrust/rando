import typer
from shared import bikecalc
from rich.console import Console
from rich.table import Table

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def calculate_gear_ratios(min_chainring: int, max_chainring: int, min_cog: int, max_cog: int):
    """Prints a table of gear ratio values."""
    gear_ratios = bikecalc.calculate_gear_ratios(min_chainring, max_chainring, min_cog, max_cog)

    console = Console()

    table = Table(show_header=True, header_style="bold")

    # Construct table header and width
    # add initial legend column
    table.add_column("Rings\nCogs")
    # walk gear_ratios hierarchy to gather all chainring values
    temp_all_chainrings = []
    for cog, chainrings in gear_ratios.items():
        for chainring in chainrings.keys():
            temp_all_chainrings.append(chainring)
    # sort and then deduplicate by unpacking them into a set
    # TODO: should this be sorted
    all_chainrings = {*temp_all_chainrings}
    # build out table columns for each chainring
    for chainring in all_chainrings:
        table.add_column(str(chainring))
    # pad far side of table with a repeat of the legend
    table.add_column("Rings\nCogs")

    # Construct table body
    def color_gear_ratios(gear_ratio: float):
        """Returns a colored string based on gear ratio value."""
        if gear_ratio >= 3:
            return "[green]" + str(gear_ratio)
        if 2 <= gear_ratio < 3:
            return "[cyan]" + str(gear_ratio)
        if gear_ratio < 2:
            return "[red]" + str(gear_ratio)

    for cog, chainrings in gear_ratios.items():
        # unpack a list comprehension to fill gear_ratio values between legend columns
        table.add_row("[bold]" + str(cog),
                      *[color_gear_ratios(gear_ratio) for gear_ratio in chainrings.values()],
                      "[bold]" + str(cog))

    console.print(table)


@app.command()
def calculate_gear_ratios_rotated(min_chainring: int, max_chainring: int, min_cog: int, max_cog: int):
    """Prints a table of gear ratio values."""
    gear_ratios = bikecalc.calculate_gear_ratios_rotated(min_chainring, max_chainring, min_cog, max_cog)

    console = Console()

    table = Table(show_header=True, header_style="bold")

    # Construct table header and width
    # add initial legend column
    table.add_column("Cogs\nRings")
    # walk gear_ratios hierarchy to gather all chainring values
    temp_all_cogs = []
    for chainring, cogs in gear_ratios.items():
        for cog in cogs.keys():
            temp_all_cogs.append(cog)
    # sort and then deduplicate by unpacking them into a set
    # TODO: should this be sorted?
    all_cogs = {*temp_all_cogs}
    # build out table columns for each chainring
    for cog in all_cogs:
        table.add_column(str(cog))
    # pad far side of table with a repeat of the legend
    table.add_column("Cogs\nRings")

    # Construct table body
    def color_gear_ratios(gear_ratio: float):
        """Returns a colored string based on gear ratio value."""
        if gear_ratio >= 3:
            return "[green]" + str(gear_ratio)
        if 2 <= gear_ratio < 3:
            return "[cyan]" + str(gear_ratio)
        if gear_ratio < 2:
            return "[red]" + str(gear_ratio)

    for chainring, cogs in gear_ratios.items():
        # unpack a list comprehension to fill gear_ratio values between legend columns
        table.add_row("[bold]" + str(chainring),
                      *[color_gear_ratios(gear_ratio) for gear_ratio in cogs.values()],
                      "[bold]" + str(chainring))

    console.print(table)


if __name__ == "__main__":
    app()
