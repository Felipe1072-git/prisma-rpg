"""
Hooks de build do Prisma RPG.

O markdown continua sendo a fonte da verdade: nada aqui altera arquivo em disco.
O que este hook faz, durante o `mkdocs build`:

1. `cards`      — reconhece os blocos de habilidade escritos no formato do projeto
                  (`**Nome**` + flavor em itálico + bullets) e os reescreve como
                  cards colapsáveis com cabeçalho em colunas, no espírito das
                  listas de magias do D&D Beyond.
2. `glossario`  — extrai cada verbete do glossário para `assets/glossario.json`,
                  que o JS usa para mostrar o termo num popover ao passar o mouse,
                  em vez de obrigar o leitor a sair da página.

Se o parser não reconhecer um bloco, ele é deixado exatamente como está — o pior
caso é a página continuar igual a hoje.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------- utilidades


def slug(texto: str) -> str:
    """Mesma normalização de âncora usada nos links do projeto (sem acento)."""
    txt = unicodedata.normalize("NFKD", texto)
    txt = "".join(c for c in txt if not unicodedata.combining(c))
    txt = txt.lower()
    txt = re.sub(r"[^a-z0-9]+", "-", txt)
    return txt.strip("-")


_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def texto_puro(md: str) -> str:
    """Markdown inline -> texto puro, para o cabeçalho do card."""
    txt = _LINK.sub(r"\1", md)
    txt = re.sub(r"\*\*([^*]+)\*\*", r"\1", txt)
    txt = re.sub(r"\*([^*]+)\*", r"\1", txt)
    txt = txt.replace("`", "")
    return txt.strip()


def sem_acento(texto: str) -> str:
    txt = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in txt if not unicodedata.combining(c)).lower()


def escapa(texto: str) -> str:
    return (
        texto.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# ------------------------------------------------------------------- parsing

# O nome de uma habilidade, com o qualificador opcional que vem depois dele:
#   **Corte Duplo**
#   **Erradicação** *(Supremo)*
#   **Cambalhota** *(usada como Reação)*
#   **Corte Impactante** — *Básica*
RE_NOME = re.compile(r"^\*\*([^*]+)\*\*(?:\s*(?:—|-)?\s*\*\(?([^*]+?)\)?\*)?\s*$")
# Uma linha que é só *texto em itálico* — o flavor.
RE_FLAVOR = re.compile(r"^\*[^*].*\*\s*$")
# Um bullet de ficha: - **Rótulo:** valor
RE_CAMPO = re.compile(r"^-\s+\*\*([^:*]+):?\*\*\s*(.*)$")
# Vários rótulos podem dividir a mesma linha: **Atributo:** X | **Alvos:** Y
RE_PAR = re.compile(r"\*\*([^:*]+):\*\*\s*([^|]*)")


def campos_da_linha(linha: str) -> dict[str, str]:
    """Todos os pares rótulo/valor de um bullet, inclusive os separados por |."""
    pares = RE_PAR.findall(linha)
    if not pares:
        return {}
    return {rot.strip(): val.strip() for rot, val in pares}

# Rótulos que viram coluna no cabeçalho colapsado, na ordem em que aparecem.
COLUNAS = ("Chave", "Atributo", "Custo", "Alvos")

# Ordem de grandeza dos grupos, para colorir o chip.
GRUPOS_CHIP = {
    "marciais": "marciais",
    "pontaria": "pontaria",
    "arcano": "arcano",
    "magicas": "arcano",
    "sociais": "sociais",
    "infiltracao": "infiltracao",
    "mobilidade": "mobilidade",
    "buff": "buff",
    "debuff": "debuff",
    "suporte": "suporte",
    "basica": "grau",
    "avancada": "grau",
    "especial": "grau",
    "maior": "grau",
    # cobre "Supremo" e "Suprema"
    "suprem": "suprema",
    "reacao": "reacao",
    "dupla empunhadura": "dupla",
    # Os 11 elementos têm cor própria: a Chave é o que se lê primeiro na lista.
    "fogo": "fogo",
    "gelo": "gelo",
    "terra": "terra",
    "raio": "raio",
    "vento": "vento",
    "agua": "agua",
    "luz": "luz",
    "sombras": "sombras",
    "veneno": "veneno",
    "sangue": "sangue",
    "espaco-tempo": "espacotempo",
}


def classe_chip(rotulo: str) -> str:
    chave = sem_acento(rotulo).strip()
    # Exato primeiro: por substring, "Debuff" casaria com "buff".
    if classe := GRUPOS_CHIP.get(chave):
        return classe
    for termo, classe in GRUPOS_CHIP.items():
        if termo in chave:
            return classe
    return "neutro"


def limpa_qualificador(bruto: str) -> str:
    """'(usada como Reação)' -> 'Reação'; corta o detalhe depois do dois-pontos.

    O detalhe que sai daqui não se perde: continua no corpo do card, na linha
    de Requisito.
    """
    txt = bruto.strip().strip("()").strip()
    txt = re.sub(r"^usada como\s+", "", txt, flags=re.I)
    return txt.split(":")[0].strip()


def resume_atributo(bruto: str) -> str:
    """'Força (ou Agilidade, se a arma for Finesse)' -> 'Força/Agilidade'.

    O cabeçalho é uma varredura de olho; a condição completa fica no corpo.
    """
    txt = texto_puro(bruto)
    principal = txt.split("(")[0].strip()
    alternativo = ""
    if m := re.search(r"\(ou ([A-ZÀ-Ú][a-zà-ú]+)", txt):
        alternativo = m.group(1)
    if alternativo:
        return f"{principal}/{alternativo}"
    return principal.replace(" ou ", "/")


def custo_resumido(campos: dict[str, str]) -> str:
    """Uma string curta de custo para o cabeçalho: '◈–◈◈◈ · 1–6 Mana'."""
    if bruto := campos.get("Custo fixo"):
        txt = texto_puro(bruto).split("|")[0].strip()
        pa = "".join(re.findall(r"◈", txt))
        mana = m.group(1) if (m := re.search(r"(\d+)\s*Mana", txt)) else ""
        if pa and mana:
            return f"{pa} · {mana} Mana"
        return txt

    manas: list[int] = []
    pas: list[int] = []
    for rotulo, valor in campos.items():
        if not rotulo.startswith("Intensidade"):
            continue
        cabeca = rotulo + " " + valor
        if m := re.search(r"(\d+)\s*PA", cabeca):
            pas.append(int(m.group(1)))
        if m := re.search(r"(\d+)\s*Mana", cabeca):
            manas.append(int(m.group(1)))

    if not pas and not manas:
        return ""

    partes = []
    if pas:
        lo, hi = min(pas), max(pas)
        partes.append("◈" * lo if lo == hi else f"{'◈' * lo}–{'◈' * hi}")
    if manas:
        lo, hi = min(manas), max(manas)
        partes.append(f"{lo} Mana" if lo == hi else f"{lo}–{hi} Mana")
    return " · ".join(partes)


def monta_card(
    nome: str,
    flavor: str,
    campos: dict[str, str],
    corpo: list[str],
    qualificador: str = "",
) -> str:
    ident = "hab-" + slug(nome)

    rotulos: list[str] = []
    chave = campos.get("Chave", "")
    if chave:
        rotulos = [texto_puro(p) for p in re.split(r"\s+-\s+|\s+·\s+", chave)]
    if qualificador and qualificador not in rotulos:
        rotulos.append(qualificador)

    chips = "".join(
        f'<span class="prg-chip prg-chip--{classe_chip(r)}">{escapa(r)}</span>'
        for r in rotulos
        if r
    )

    # O custo sai na primeira faixa, alinhado entre todos os cards: é o número
    # que o jogador compara ao varrer a lista. O resto vai na faixa de baixo.
    valores_busca = [nome]
    custo = custo_resumido(campos)
    if custo:
        valores_busca.append(custo)

    colunas = ""
    for rotulo in COLUNAS:
        if rotulo in ("Chave", "Custo"):
            continue
        bruto = campos.get(rotulo, "")
        valor = (
            resume_atributo(bruto)
            if rotulo == "Atributo"
            else texto_puro(bruto).split("|")[0].strip()
        )
        if not valor:
            continue
        valores_busca.append(valor)
        colunas += (
            f'<span class="prg-card__col" data-rot="{rotulo}">'
            f"{escapa(valor)}</span>"
        )

    valores_busca.extend(rotulos)

    detalhe = "\n".join(corpo).strip()

    # A ficha inteira entra no índice: procurar por "sangrando" ou "atordoado"
    # e ver quais habilidades aplicam aquilo é o filtro que mais importa.
    valores_busca.append(flavor)
    valores_busca.append(texto_puro(detalhe))
    busca = escapa(sem_acento(" ".join(" ".join(valores_busca).split())))

    return (
        # markdown="block" no container: sem ele, o md_in_html trata o card
        # inteiro como HTML cru e a ficha nunca vira markdown.
        f'<div class="prg-card" id="{ident}" data-busca="{busca}" markdown="block">\n'
        f'<button class="prg-card__hd" type="button" aria-expanded="false" '
        f'aria-controls="{ident}-bd">\n'
        f'<span class="prg-card__nome">{escapa(nome)}</span>\n'
        f'<span class="prg-card__chips">{chips}</span>\n'
        f'<span class="prg-card__custo">{escapa(custo)}</span>\n'
        f'<span class="prg-card__seta" aria-hidden="true"></span>\n'
        f'<span class="prg-card__cols">{colunas}</span>\n'
        f"</button>\n"
        f'<div class="prg-card__bd" id="{ident}-bd" markdown="1">\n\n'
        f"{'*' + flavor + '*' if flavor else ''}\n\n"
        f"{detalhe}\n\n"
        f"</div>\n"
        f"</div>\n"
    )


def transforma_habilidades(markdown: str) -> tuple[str, int]:
    linhas = markdown.split("\n")
    saida: list[str] = []
    i = 0
    total = 0

    while i < len(linhas):
        m = RE_NOME.match(linhas[i])
        if not m:
            saida.append(linhas[i])
            i += 1
            continue

        nome = m.group(1).strip()
        qualificador = limpa_qualificador(m.group(2)) if m.group(2) else ""
        j = i + 1
        while j < len(linhas) and not linhas[j].strip():
            j += 1

        flavor = ""
        if j < len(linhas) and RE_FLAVOR.match(linhas[j].strip()):
            flavor = linhas[j].strip().strip("*").strip()
            j += 1
            while j < len(linhas) and not linhas[j].strip():
                j += 1

        # Um bloco só é habilidade se a ficha em bullets vier logo em seguida.
        if j >= len(linhas) or not RE_CAMPO.match(linhas[j]):
            saida.append(linhas[i])
            i += 1
            continue

        corpo: list[str] = []
        campos: dict[str, str] = {}
        while j < len(linhas):
            linha = linhas[j]
            if RE_CAMPO.match(linha):
                for rotulo, valor in campos_da_linha(linha).items():
                    campos.setdefault(rotulo, valor)
                corpo.append(linha)
                j += 1
            elif linha.startswith(("  ", "\t", "- ", "*(")) and linha.strip():
                corpo.append(linha)
                j += 1
            elif not linha.strip():
                # Linha em branco encerra a ficha, salvo se ainda houver bullet.
                k = j + 1
                while k < len(linhas) and not linhas[k].strip():
                    k += 1
                if k < len(linhas) and linhas[k].startswith(("- ", "*(")):
                    corpo.append("")
                    j = k
                else:
                    break
            else:
                break

        saida.append(monta_card(nome, flavor, campos, corpo, qualificador))
        total += 1
        i = j

    return "\n".join(saida), total


# --------------------------------------------------------------- glossário

RE_VERBETE = re.compile(r"^###\s+(.+?)\s*$")

_glossario: dict[str, dict[str, str]] = {}


def html_do_verbete(md: str) -> str:
    """Markdown do verbete -> HTML mínimo para o popover.

    Links viram texto realçado de propósito: o popover é uma espiada, não um
    novo lugar pra clicar e se perder. O link de verdade continua na página.
    """
    txt = escapa(md)
    txt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"<b>\1</b>", txt)
    txt = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", txt)
    txt = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", txt)
    return " ".join(txt.split())


def coleta_glossario(markdown: str) -> None:
    linhas = markdown.split("\n")
    atual: str | None = None
    buffer: list[str] = []

    def grava() -> None:
        if not atual:
            return
        corpo = "\n".join(buffer).strip()
        # Só o essencial: o primeiro parágrafo já define o termo.
        resumo = corpo.split("\n\n")[0].strip()
        if resumo:
            _glossario[slug(atual)] = {
                "titulo": atual,
                "corpo": html_do_verbete(resumo),
            }

    for linha in linhas:
        if m := RE_VERBETE.match(linha):
            grava()
            atual = m.group(1).strip()
            buffer = []
        elif linha.startswith("## "):
            grava()
            atual = None
            buffer = []
        elif atual is not None:
            buffer.append(linha)
    grava()


# ----------------------------------------------------------------- arte

_ARTE: dict[str, str] = {}
_DIR_ARTE = Path(__file__).resolve().parent.parent / "docs" / "assets" / "img"


def svg(nome: str) -> str:
    """SVG inline (herda currentColor, acompanha o tema claro/escuro)."""
    if nome not in _ARTE:
        arquivo = _DIR_ARTE / f"{nome}.svg"
        _ARTE[nome] = (
            arquivo.read_text(encoding="utf-8").strip() if arquivo.exists() else ""
        )
    return _ARTE[nome]


def aplica_arte(markdown: str, brasao: str) -> str:
    """Capa de capítulo antes do H1 e divisor ornamental entre as seções."""
    linhas = markdown.split("\n")
    saida: list[str] = []
    visto_h1 = False
    visto_h2 = False
    dentro_de_bloco = False

    for linha in linhas:
        if linha.startswith("```"):
            dentro_de_bloco = not dentro_de_bloco

        if not dentro_de_bloco:
            if not visto_h1 and linha.startswith("# "):
                arte = svg(brasao) or svg("brasao-padrao")
                if arte:
                    saida.append(f'<div class="prg-capa">{arte}</div>\n')
                visto_h1 = True
            elif linha.startswith("## "):
                if visto_h2 and (orn := svg("divisor")):
                    saida.append(f'<div class="prg-ornamento">{orn}</div>\n')
                visto_h2 = True

        saida.append(linha)

    return "\n".join(saida)


# ------------------------------------------------------------------- hooks

PAGINAS_COM_CARD = ("habilidades/",)


def on_page_markdown(markdown, page, config, files, **kwargs):
    caminho = page.file.src_uri

    if caminho == "glossario.md":
        coleta_glossario(markdown)

    if caminho.startswith(PAGINAS_COM_CARD) and not caminho.endswith("index.md"):
        grupo = Path(caminho).stem
        markdown = aplica_arte(markdown, f"brasao-{grupo}")
        markdown, total = transforma_habilidades(markdown)
        if total:
            barra = (
                '<div class="prg-filtro" data-alvo=".prg-card">\n'
                '<input type="search" class="prg-filtro__campo" '
                'placeholder="Filtrar habilidades desta página…" '
                'aria-label="Filtrar habilidades">\n'
                '<span class="prg-filtro__contagem"></span>\n'
                '<button type="button" class="prg-filtro__tudo">Expandir tudo</button>\n'
                "</div>\n\n"
            )
            # A barra pertence à lista, não ao topo da página: entra logo antes
            # do primeiro card, depois do título e do texto de abertura.
            marca = '<div class="prg-card"'
            corte = markdown.find(marca)
            markdown = markdown[:corte] + barra + markdown[corte:]

    return markdown


def on_post_build(config, **kwargs):
    destino = Path(config["site_dir"]) / "assets" / "glossario.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        json.dumps(_glossario, ensure_ascii=False), encoding="utf-8"
    )
