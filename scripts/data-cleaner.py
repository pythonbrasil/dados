import pandas as pd
import click
import re


def normalize_column_name(column_name):
    # Convert to lowercase
    column_name = column_name.lower()
    # Replace spaces with underscores
    column_name = column_name.replace(' ', '_')
    # Remove special characters using regex
    column_name = re.sub(r'[^a-zA-Z0-9_]', '', column_name)
    return column_name


def normalize_column_names(df):
    # Apply normalization to all column names
    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


def remove_columns(df, columns_to_remove):
    # Drop the specified columns
    return df.drop(columns=columns_to_remove)


@click.group()
def cli():
    """A tool for manipulating CSV files."""
    pass


@cli.command()
@click.argument('input_csv', type=click.Path(exists=True))
@click.argument('output_csv', type=click.Path())
@click.argument('columns', nargs=-1)
def remove_columns_cmd(input_csv, output_csv, columns):
    """
    Remove specified columns from the CSV file.

    \b
    INPUT_CSV: Path to the input CSV file.
    OUTPUT_CSV: Path to the output CSV file.
    COLUMNS: List of column names to remove.
    """
    # Read the CSV file
    df = pd.read_csv(input_csv, sep=';', na_values=['', ' '], encoding='utf-8')
    if not columns:
        columns = [
            "nome",
            "sobrenome",
            "email",
            "participante_n",
            "endereo_residencial_1",
            "endereo_residencial_2",
            "cidade_de_residncia",
            "estado_de_residncia",
            "cep_residencial",
            "pas_de_residncia",
            "endereo",
            "complemento",
            "cidade",
            "cep",
            "pas",
            "n_do_pedido"
        ]
    click.echo(df.columns)

    # Remove specified columns
    for col in columns:
        if col not in df.columns:
            click.echo(f"Column {col} not found in the CSV file.")
            return
    df = remove_columns(df, columns)
    

    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_csv, index=False, sep=';', encoding='utf-8')
    click.echo(f"Removed columns: {columns} and saved to {output_csv}")


@cli.command()
@click.argument('input_csv', type=click.Path(exists=True))
@click.argument('output_csv', type=click.Path())
def normalize_columns_cmd(input_csv, output_csv):
    """
    Normalize column names in the CSV file (lowercase, remove special characters, replace spaces with underscores).

    \b
    INPUT_CSV: Path to the input CSV file.
    OUTPUT_CSV: Path to the output CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(input_csv, sep=';', na_values=['', ' '], encoding='utf-8')

     # Criar tabela em Markdown
    markdown_output = "| column                  | data_value                                                                 |\n"
    markdown_output += "|------------------------------------------|------------------------------------------------------------------------------------------|\n"
    
    # Iterar sobre as colunas e gerar a tabela
    for column in df.columns:
        normalized_name = normalize_column_name(column)
        markdown_output += f"| {normalized_name:<40} | {column:<100} |\n"
        df.rename(columns={column: normalized_name}, inplace=True)

    # Write to the output CSV file
    df.to_csv(output_csv, index=False, sep=';', encoding='utf-8')
    
    # Imprimir a tabela Markdown
    click.echo(markdown_output)

if __name__ == '__main__':
    cli()
