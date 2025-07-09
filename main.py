import click
import json

# Lista simulando uma estante de livros

#carrega os dados
with open("estante.json", "r", encoding="utf-8") as arquivo:
    estante =  json.load(arquivo)

#funcao de salvar dados
def salvar():
    with open("estante.json", "w", encoding="utf-8") as f:
        json.dump(estante, f, ensure_ascii=False, indent=4)

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
    salvar()

@cli.command()
@click.argument('nome')
def remover(nome):
    """Remove um livro da estante."""
    if nome in estante:
        estante.remove(nome)
        click.echo(f"Livro '{nome}' removido.")
        salvar()
    else:
        click.echo("Livro não encontrado.")

if __name__ == '__main__':
    cli()