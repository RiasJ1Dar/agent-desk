[Українська](README.md) · **English**

# agent-desk

Human layer on top of [agent-exchange](https://github.com/RiasJ1Dar/agent-exchange):
render `NOW.md` and point at the live `127.0.0.1:9750` board.

Exchange already serves a read-only GET UI and writes `NOW.md`. This repo does
not add write APIs — locks/ack stay as agent MCP tools.

```bash
pip install -e .
agent-desk view ./NOW.md -o /tmp/now.html
```

## License

MIT
