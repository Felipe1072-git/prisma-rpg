"""Checagens que o `mkdocs build --strict` não faz.

O --strict reclama de página inexistente, mas **âncora** quebrada ele só reporta
como INFO — e id duplicado ele não vê de jeito nenhum. Como as listagens geram
centenas de ids, essas duas checagens precisam existir à parte.

Além delas, confere o único número que o projeto repete de propósito em dois
lugares: o dado de dano de cada arma, que aparece na tabela do Equipamento e de
novo no verbete do glossário.

Rode depois do build:

    python -m mkdocs build --strict && python notas/verifica.py
"""

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, "hooks")

SITE = Path("site")
DOCS = Path("docs")
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

# ------------------------------------- dado de dano: tabela vs glossário

import prisma  # noqa: E402  (precisa do sys.path ajustado acima)

arsenal = (DOCS / "equipamento" / "index.md").read_text(encoding="utf-8")
fichas = prisma.le_tabelas_de_arma(arsenal)
verbetes = prisma.extrai_verbetes(
    (DOCS / "glossario.md").read_text(encoding="utf-8")
)

# Dois verbetes com o mesmo nome geram `termo` e `termo_1` — um id que depende
# da ordem do arquivo. Os links apontam pro primeiro, e o dicionário do popover
# fica com o último: o leitor clica num verbete e o mouse mostra outro. Foi o
# que aconteceu com "Escudo" (a condição e o item). A cura é âncora explícita,
# `### Nome {: #ancora }`; esta checagem é o alarme.
vistos: dict[str, str] = {}
for v in verbetes:
    if v.ancora in vistos:
        problemas += 1
        print(
            f"[âncora repetida] '{v.termo}' ({v.categoria}) e "
            f"'{vistos[v.ancora]}' disputam #{v.ancora} — dê âncora explícita a um"
        )
    vistos[v.ancora] = v.termo

armas = 0
for v in verbetes:
    if v.categoria != "Armas":
        continue
    armas += 1
    ficha = fichas.get(prisma.slug(v.termo))
    if not ficha:
        problemas += 1
        print(f"[arma sem ficha] '{v.termo}' está no glossário mas não na tabela")
        continue
    na_tabela = prisma.texto_puro(ficha.campos["Dado"])
    m = re.search(r"dano (\d+d\d+)", " ".join(v.corpo))
    if not m:
        problemas += 1
        print(f"[dado ausente] '{v.termo}': o glossário não diz o dado ({na_tabela})")
    elif m.group(1) != na_tabela:
        problemas += 1
        print(
            f"[dado divergente] '{v.termo}': glossário diz {m.group(1)}, "
            f"tabela diz {na_tabela}"
        )

print(
    f"\n{len(paginas)} páginas e {armas} armas verificadas, {problemas} problema(s)."
)
sys.exit(1 if problemas else 0)
