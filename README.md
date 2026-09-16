# Kronika Baronii Basleur

Materiały od Mistrza Gry do sesji Warhammer Fantasy Roleplay 2ed, złożone w jedną stronę.

**Na żywo:** https://marcinoinc.github.io/kronika-basleur/

## Jak to jest zbudowane

| Plik | Co to |
|---|---|
| `page.html` | **Źródło.** Forma artefaktu Claude — bez `doctype`, `head` i `body`, bo platforma dokleja je sama. Tu się edytuje. |
| `index.html` | **Generowany.** To, co serwuje GitHub Pages. Nie edytować ręcznie. |
| `build.py` | Opakowuje `page.html` w kompletny dokument: szkielet HTML, favicon, meta `og:` pod podgląd linku. |
| `ryciny/` | Ryciny od MG, przeskalowane do 1500 px i zapisane jako JPEG. |

Po każdej zmianie w `page.html`:

```bash
python3 build.py && git add -A && git commit && git push
```

GitHub Pages przebudowuje się sam, ok. 40 sekund po pushu.
