import typer

app = typer.Typer()

@app.command()
def foo(name: str):
    """Print a greeting message"""
    typer.echo(f"Hello, {name}!")

@app.command()
def bar(count: int):
    """Print a message multiple times"""
    for i in range(count):
        typer.echo(f"Bar {i+1}!")

if __name__ == "__main__":
    app()