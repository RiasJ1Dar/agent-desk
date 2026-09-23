**Українська** · [English](README.en.md)

# agent-desk

Людський шар над [agent-exchange](https://github.com/RiasJ1Dar/agent-exchange):
швидкий перегляд `NOW.md` і ярлики на живу дошку `http://127.0.0.1:9750`.

Exchange уже віддає read-only HTML на 9750 (лише `GET`) і сам пише `NOW.md`.
Цей репо **не** дублює MCP і **не** додає POST unlock/ack у сервер — замки й
ack лишаються інструментами агентів. Тут зручний перегляд для людини.

## Що вміє

| | |
|---|---|
| `agent-desk view NOW.md` | Рендер у HTML (stdout або `-o`) |
| `web/index.html` | Статична сторінка-ярлик + інструкція |
| docs | Як читати дошку поруч із двома агентами |

## CLI

```bash
pip install -e .
agent-desk view ./NOW.md -o /tmp/now.html
# відкрий /tmp/now.html у браузері
```

Поки крутиться exchange UI — відкривай просто http://127.0.0.1:9750

## Ліцензія

MIT
