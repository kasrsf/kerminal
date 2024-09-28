import typer
from kerminal.core.services import MathService

app = typer.Typer()


@app.command()
def add(a: float, b: float):
    """
    add inputs
    """
    result = MathService.add(a, b)
    typer.echo(f"The sum of {a} and {b} is: {result}")


if __name__ == "__main__":
    app()
