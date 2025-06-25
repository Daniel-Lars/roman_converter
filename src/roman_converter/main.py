import typer
from roman_converter.converter import RomanToInt
from typing import Annotated

app = typer.Typer(
    no_args_is_help=True,
    help="A converter for Roman numerals to integers and vice versa")

# Initialize the converter
converter = RomanToInt()

@app.command()
def roman_to_int(
    roman_string: str = typer.Argument(..., help="Roman numeral string to convert to integer")
):
    result = converter.roman_to_int(roman_string)
    typer.echo(result)

@app.command()
def int_to_roman(
    integer_value: int = typer.Argument(..., help="Integer value to convert to Roman numeral"),
    confirm: Annotated[
        bool,
        typer.Option(
            prompt="Sure you want to convert this integer to Roman numeral? (y/n)", 
            help="Confirm conversion"
            )
    ] = False
):
    
    if not confirm:
        typer.echo("Conversion stopped by user.")
        raise typer.Exit()
    
    
    result = converter.int_to_roman(integer_value)
    typer.echo(result)
    
if __name__ == "__main__":
    app()