"""Опыт 1: одна и та же фраза на русском и английском через токенайзеры tiktoken."""
import json
import tiktoken

PHRASES = {
    "en": "Artificial intelligence is changing the way people work and learn.",
    "ru": "Искусственный интеллект меняет то, как люди работают и учатся.",
}
ENCODINGS = ["cl100k_base", "o200k_base"]  # GPT-4 / GPT-4o


def pieces(enc, text):
    ids = enc.encode(text)
    return ids, [enc.decode_single_token_bytes(i).decode("utf-8", errors="replace") for i in ids]


results = []
lines = ["# Опыт 1: токенизация одной фразы на русском и английском", ""]
for name in ENCODINGS:
    enc = tiktoken.get_encoding(name)
    lines += [f"## Токенайзер `{name}`", ""]
    lines += ["| Язык | Символов | Токенов | Символов/токен |", "|---|---|---|---|"]
    detail = []
    for lang, text in PHRASES.items():
        ids, toks = pieces(enc, text)
        results.append({"encoding": name, "lang": lang, "text": text, "chars": len(text),
                        "tokens": len(ids), "token_ids": ids, "pieces": toks})
        lines.append(f"| {lang} | {len(text)} | {len(ids)} | {len(text)/len(ids):.2f} |")
        detail.append(f"**{lang}**: `{text}`\n\n`" + "` `".join(t.replace("`", "'") for t in toks) + "`\n")
    lines += [""] + detail
    en = next(r for r in results if r["encoding"] == name and r["lang"] == "en")["tokens"]
    ru = next(r for r in results if r["encoding"] == name and r["lang"] == "ru")["tokens"]
    lines += [f"Русский / английский = **{ru/en:.2f}x** по токенам", ""]

with open("results_experiment1.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
with open("results_experiment1.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
