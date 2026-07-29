"""Checagens que o `mkdocs build --strict` não faz.

O --strict reclama de página inexistente, mas **âncora** quebrada ele só reporta
como INFO — e id duplicado ele não vê de jeito nenhum. Como as listagens geram
centenas de ids, essas duas checagens precisam existir à parte.

Rode depois do build:

    python -m mkdocs build && python notas/verifica.py
"""

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")

SITE = Path("site")
RE_ID = re.compile(r'\bid="([^"]+)"')
RE_HREF = re.compile(r'\bhref="([^"]+)"')

paginas = sorted(SITE.rglob("index.html")) + sorted(SITE.glob("*.html"))
ids: dict[str, set[str]] = {}
problemas = 0

for pagina in paginas:
    html = pagina.read_text(encoding="utf-8", errors="replace")
    url = pagina.parent.relative_to(SITE).as_posix()
    url = "" if url == "." else url
    achados = RE_ID.findall(html)
    ids[url] = set(achados)

    repetidos = [i for i, n in Counter(achados).items() if n > 1]
    if repetidos:
        problemas += len(repetidos)
        print(f"[id duplicado] /{url}/ → {', '.join(sorted(repetidos))}")

for pagina in paginas:
    html = pagina.read_text(encoding="utf-8", errors="replace")
    url = pagina.parent.relative_to(SITE).as_posix()
    url = "" if url == "." else url
    for href in RE_HREF.findall(html):
        if "#" not in href or href.startswith(("http", "mailto")):
            continue
        destino, _, ancora = href.partition("#")
        ancora = unquote(ancora)
        if not ancora:
            continue
        # Só links internos do próprio site: mesma página, ou ../outra/
        if destino in ("", "./"):
            alvo = url
        elif destino.startswith(("../", "./")) or not destino.startswith("/"):
            partes = [p for p in (url.split("/") if url else []) if p]
            for pedaco in destino.strip("/").split("/"):
                if pedaco == "..":
                    if partes:
                        partes.pop()
                elif pedaco not in (".", ""):
                    partes.append(pedaco)
            alvo = "/".join(partes)
        else:
            continue
        if alvo not in ids:
            continue  # página fora do site (ou arquivo solto): não é nosso caso
        if ancora not in ids[alvo]:
            problemas += 1
            print(f"[âncora quebrada] /{url}/ → {href}")

print(f"\n{len(paginas)} páginas verificadas, {problemas} problema(s).")
sys.exit(1 if problemas else 0)
