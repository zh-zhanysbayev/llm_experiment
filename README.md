# llm_experiment

Небольшие опыты с токенами и LLM. Результаты каждого опыта лежат в репозитории.

## Опыт 1. Токенизация русского и английского

Одна и та же по смыслу фраза прогнана через токенайзеры `tiktoken`.

| Токенайзер | EN токенов | RU токенов | RU / EN |
|---|---|---|---|
| `cl100k_base` (GPT-4) | 12 | 30 | 2.50x |
| `o200k_base` (GPT-4o) | 11 | 16 | 1.45x |

Вывод: на старом словаре русский стоит в 2.5 раза дороже английского, у нового токенайзера разрыв заметно меньше, но остаётся.
Это один пример, а не статистика: на одной фразе общие выводы делать нельзя.

- Скрипт: [experiment1_tokenizer.py](experiment1_tokenizer.py)
- Подробный разбор по токенам: [results_experiment1.md](results_experiment1.md)
- Сырые данные: [results_experiment1.json](results_experiment1.json)

Запуск:

```bash
python -m venv .venv && .venv/Scripts/pip install tiktoken
.venv/Scripts/python experiment1_tokenizer.py
```
