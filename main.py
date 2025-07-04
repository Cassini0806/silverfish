import click

# Lista simulando uma estante de livros
estante = [
    "livro0",
    "livro1",
    "livro2",
    "livro3",
]

@click.group()
def cli():
    """Sistema de gerenciamento de livros."""
    pass

@cli.command()
def listar():
    """Lista os livros na estante."""
    click.echo("Livros na estante:")
    for livro in estante:
        click.echo(f"\033[31m{livro}\033[0m")

@cli.command()
@click.argument('nome')
def adicionar(nome):
    """Adiciona um livro à estante."""
    estante.append(nome)
    click.echo(f"Livro '{nome}' adicionado à estante.")

@cli.command()
@click.argument('nome')
def remover(nome):
    """Remove um livro da estante."""
    if nome in estante:
        estante.remove(nome)
        click.echo(f"Livro '{nome}' removido.")
    else:
        click.echo("Livro não encontrado.")

if __name__ == '__main__':
    cli()