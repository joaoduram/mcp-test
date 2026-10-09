# mcp-server-teste

<!-- mcp-name: io.github.joaoduram/mcp-server-teste -->

MCP server básico de teste, em Python, com 3 ferramentas:

| Tool     | O que faz                          |
|----------|------------------------------------|
| `somar`  | Soma dois números                  |
| `saudar` | Retorna uma saudação para um nome  |
| `agora`  | Retorna a data/hora do servidor    |

## Uso direto do Git (sem publicar no PyPI)

```bash
uvx --from git+https://github.com/joaoduram/mcp-server-teste mcp-server-teste
```

## Configuração no Claude Desktop / Claude Code

```json
{
  "mcpServers": {
    "teste": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/joaoduram/mcp-server-teste", "mcp-server-teste"]
    }
  }
}
```

No Claude Code também dá pra adicionar via CLI:

```bash
claude mcp add teste -- uvx --from git+https://github.com/joaoduram/mcp-server-teste mcp-server-teste
```

## Desenvolvimento local

```bash
uv run mcp-server-teste          # roda o server (stdio)
uv run mcp dev src/mcp_server_teste/server.py   # abre o MCP Inspector
```
