[Українська](README.md) · **English**

# agent-desk

A small local viewer for [agent-exchange](https://github.com/RiasJ1Dar/agent-exchange):
it turns `NOW.md` into a self-contained HTML page and links to the live board
at `http://127.0.0.1:9750`.

`agent-exchange` already maintains `NOW.md` and serves a read-only UI.
`agent-desk` does not duplicate the MCP server or mutate its state. It is the
human-facing layer for reading, snapshots, and handoff.

## Features

| Component | Purpose |
|---|---|
| `agent-desk view NOW.md` | Print a complete HTML document to stdout |
| `agent-desk view NOW.md -o now.html` | Write a static HTML snapshot |
| `web/index.html` | Static shortcut page for the local board |
| `docs/with-exchange.md` | Short workflow alongside exchange |

Input is HTML-escaped and placed in a `<pre>` block, so HTML from `NOW.md`
is not executed. This is not a Markdown renderer and the generated page does
not refresh automatically.

## Requirements and installation

- Python 3.10 or newer.
- No runtime dependencies outside the standard library.

```bash
git clone https://github.com/RiasJ1Dar/agent-desk.git
cd agent-desk
python -m pip install -e .
```

## Usage

Write a snapshot:

```bash
agent-desk view ./NOW.md -o ./now.html
```

Send HTML to stdout:

```bash
agent-desk view ./NOW.md > ./now.html
```

With `-o`, the CLI prints the created path. Without it, the complete HTML
document is printed.

## Working with agent-exchange

1. Start the `agent-exchange` MCP server and its UI.
2. Open `http://127.0.0.1:9750` for live locks and the message queue.
3. Use `NOW.md` as the compact state summary.
4. Generate an HTML snapshot when the state must be shared without the server.

See [docs/with-exchange.md](docs/with-exchange.md).

## Out of scope

- starting or configuring `agent-exchange`;
- write APIs, unlock, or acknowledgement actions;
- watching `NOW.md` for changes;
- full Markdown rendering.

## Layout

```text
agent_desk/       Python CLI and HTML generator
web/index.html    static shortcut page
docs/             short workflows
```

## Development check

```bash
python -m agent_desk --help
python -m agent_desk view ./NOW.md -o ./now.html
```

## License

MIT