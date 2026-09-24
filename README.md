**Українська** · [English](README.en.md)

# agent-desk

Невеликий локальний переглядач для [agent-exchange](https://github.com/RiasJ1Dar/agent-exchange):
перетворює `NOW.md` на самодостатню HTML-сторінку і дає швидке посилання на
живу дошку `http://127.0.0.1:9750`.

`agent-exchange` уже веде `NOW.md` і віддає read-only UI. `agent-desk` не
дублює MCP-сервер і не змінює його стан. Це окремий людський шар для читання,
знімків і передачі поточного стану.

## Можливості

| Компонент | Що робить |
|---|---|
| `agent-desk view NOW.md` | Друкує готовий HTML у stdout |
| `agent-desk view NOW.md -o now.html` | Записує статичний HTML-знімок у файл |
| `web/index.html` | Статична сторінка-ярлик на локальну дошку |
| `docs/with-exchange.md` | Короткий сценарій роботи поруч з exchange |

Вхідний текст екранується й розміщується у `<pre>`: HTML із `NOW.md` не
виконується. Це не Markdown-рендерер і не автооновлювана сторінка.

## Вимоги та встановлення

- Python 3.10 або новіший.
- Runtime-залежностей поза стандартною бібліотекою немає.

```bash
git clone https://github.com/RiasJ1Dar/agent-desk.git
cd agent-desk
python -m pip install -e .
```

## Використання

Записати знімок у файл:

```bash
agent-desk view ./NOW.md -o ./now.html
```

Отримати HTML через stdout:

```bash
agent-desk view ./NOW.md > ./now.html
```

Команда друкує шлях до створеного файлу, якщо задано `-o`. Без `-o` вона
друкує весь HTML.

## Робота разом з agent-exchange

1. Запусти MCP-сервер `agent-exchange` з його UI.
2. Відкрий `http://127.0.0.1:9750` для живих замків і черги повідомлень.
3. Використовуй `NOW.md` як коротке зведення стану.
4. Створи HTML-знімок, коли треба передати стан без запущеного сервера.

Деталі: [docs/with-exchange.md](docs/with-exchange.md).

## Чого тут немає

- запуску чи налаштування `agent-exchange`;
- write API, unlock або ack;
- фонового стеження за змінами `NOW.md`;
- повного Markdown-рендерингу.

## Структура

```text
agent_desk/       Python CLI і HTML-генератор
web/index.html    статична сторінка-ярлик
docs/             короткі сценарії роботи
```

## Перевірка розробки

```bash
python -m agent_desk --help
python -m agent_desk view ./NOW.md -o ./now.html
```

## Ліцензія

MIT