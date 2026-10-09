from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server-teste")


@mcp.tool()
def somar(a: float, b: float) -> float:
    """Soma dois números."""
    return a + b


@mcp.tool()
def saudar(nome: str) -> str:
    """Retorna uma saudação para o nome informado."""
    return f"Olá, {nome}! 👋"


@mcp.tool()
def agora() -> str:
    """Retorna a data e hora atual do servidor."""
    return datetime.now().isoformat(timespec="seconds")


def main() -> None:
    mcp.run()  # transporte stdio


if __name__ == "__main__":
    main()
