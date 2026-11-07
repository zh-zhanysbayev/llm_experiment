"""Опыт 1: одна и та же фраза на русском и английском через токенайзеры tiktoken."""
import json
import tiktoken

PHRASES = {
    "en": "Artificial intelligence is changing the way people work and learn.",
    "ru": "Искусственный интеллект меняет то, как люди работают и учатся.",
    "ru_latin": "Iskusstvennyj intellekt menyaet to, kak lyudi rabotayut i uchatsya.",
    "kk": "Жасанды интеллект адамдардың жұмыс істеу және оқу тәсілін өзгертіп жатыр.",
}
ENCODINGS = ["cl100k_base", "o200k_base"]  # GPT-4 / GPT-4o


def pieces(enc, text):
    ids = enc.encode(text)
    out = []
    for i in ids:
        b = enc.decode_single_token_bytes(i)
        try:
            out.append(b.decode("utf-8"))
        except UnicodeDecodeError:  # токен - обрывок многобайтового символа
            out.append(f"<0x{b.hex()}>")
    return ids, out


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
    ratios = [f"{lang} / en = **{r['tokens']/en:.2f}x**"
              for lang in PHRASES if lang != "en"
              for r in results if r["encoding"] == name and r["lang"] == lang]
    lines += ["Отношение к английскому по токенам: " + ", ".join(ratios), ""]

with open("results_experiment1.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
with open("results_experiment1.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
