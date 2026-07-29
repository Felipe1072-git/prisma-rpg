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
from typing import NamedTuple
from urllib.parse import urlsplit

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


_ATRIBUTOS_BASE = ("forca", "agilidade", "inteligencia", "sabedoria", "vontade")


def computa_atributos(bruto: str) -> list[str]:
    """Todo atributo-base citado no campo Atributo, na ordem canônica.

    Cobre tanto 'Força ou Agilidade' quanto 'Força (ou Agilidade, se a arma
    for Finesse)' — qualquer um dos dois pode decidir o teste, então os dois
    entram no filtro.
    """
    texto = sem_acento(bruto)
    return [a for a in _ATRIBUTOS_BASE if a in texto]


def mana_minima(campos: dict[str, str]) -> int | None:
    """A Mana da Intensidade I (ou do Custo fixo) — o que cabe no orçamento."""
    if bruto := campos.get("Custo fixo"):
        txt = texto_puro(bruto).split("|")[0].strip()
        if m := re.search(r"(\d+)\s*Mana", txt):
            return int(m.group(1))
        return None
    manas = [
        int(m.group(1))
        for rotulo, valor in campos.items()
        if rotulo.startswith("Intensidade")
        if (m := re.search(r"(\d+)\s*Mana", rotulo + " " + valor))
    ]
    return min(manas) if manas else None


def computa_alvo_categoria(campos: dict[str, str], corpo: list[str] | None = None) -> str:
    """Agrupa os 89 textos livres de Alvos em 6 categorias fixas pro filtro.

    Um punhado de habilidades (Reação, invocação) não declara Alvos — usa o
    corpo inteiro como aproximação nesses casos, só pra a faceta não ficar
    vazia. É heurística de categorização pra filtro, não uma regra nova.
    """
    bruto = campos.get("Alvos", "")
    if not bruto and corpo:
        bruto = " ".join(corpo)
    texto = sem_acento(texto_puro(bruto))
    if not texto:
        return ""
    if "aliado" in texto:
        return "aliados"
    if re.search(r"proprio usuario", texto):
        return "si-mesmo"
    if re.search(r"\blinha\b|\bcone\b", texto):
        return "linha-cone"
    if "raio" in texto:
        return "area"
    if "adjacente" in texto:
        return "adjacentes"
    return "unico"


def computa_desarmado(campos: dict[str, str], corpo: list[str]) -> bool:
    texto = sem_acento(campos.get("Dano", "") + " " + " ".join(corpo))
    return "dano desarmado" in texto


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


_GRAUS_ARMA = ("basica", "avancada", "especial")


def monta_card(
    nome: str,
    flavor: str,
    campos: dict[str, str],
    corpo: list[str],
    qualificador: str = "",
    grupo: str = "",
    arma: str = "",
    arma_nome: str = "",
    elemento: str = "",
) -> str:
    # Prefixo da arma pra evitar colisão: armas diferentes às vezes reaproveitam
    # o mesmo nome de técnica (nunca colidiu antes porque cada arma vivia na
    # própria página — na listagem única, o id precisa ser único de verdade).
    ident = "hab-" + (f"{arma}-" if arma else "") + slug(nome)

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

    # Facetas estruturadas pro filtro combinado — além da busca livre acima.
    grau = sem_acento(qualificador)
    grau = grau if grau in _GRAUS_ARMA else ""
    atributos = computa_atributos(campos.get("Atributo", ""))
    mana_min = mana_minima(campos)
    alvo_cat = computa_alvo_categoria(campos, corpo)
    desarmado = computa_desarmado(campos, corpo)

    facetas = (
        f'data-grupo="{escapa(grupo)}" data-arma="{escapa(arma)}" '
        f'data-arma-nome="{escapa(arma_nome)}" '
        f'data-grau="{escapa(grau)}" data-elemento="{escapa(elemento)}" '
        f'data-atributos="{" ".join(atributos)}" '
        f'data-mana-min="{mana_min if mana_min is not None else ""}" '
        f'data-alvo="{escapa(alvo_cat)}" '
        f'data-desarmado="{"1" if desarmado else ""}"'
    )

    return (
        # markdown="block" no container: sem ele, o md_in_html trata o card
        # inteiro como HTML cru e a ficha nunca vira markdown.
        f'<div class="prg-card" id="{ident}" data-busca="{busca}" {facetas} markdown="block">\n'
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


class BlocoHabilidade(NamedTuple):
    inicio: int  # linha onde o bloco começa (o **Nome**)
    fim: int  # linha seguinte ao fim do bloco (exclusiva)
    nome: str
    qualificador: str
    flavor: str
    campos: dict[str, str]
    corpo: list[str]


def extrai_blocos_de_habilidade(linhas: list[str]) -> list[BlocoHabilidade]:
    """Acha todo bloco `**Nome**` [+ qualificador] + flavor + ficha de bullets
    no texto. Único lugar que sabe reconhecer uma habilidade — tanto o card
    completo quanto o ponteiro resumido partem daqui."""
    blocos: list[BlocoHabilidade] = []
    i = 0
    while i < len(linhas):
        m = RE_NOME.match(linhas[i])
        if not m:
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

        blocos.append(BlocoHabilidade(i, j, nome, qualificador, flavor, campos, corpo))
        i = j

    return blocos


def transforma_habilidades(
    markdown: str, grupo: str = "", arma: str = "", arma_nome: str = "", elemento: str = ""
) -> tuple[str, int, list[str]]:
    """Retorna (markdown com os cards no lugar, quantos cards, e a lista deles
    isolada) — a lista isolada é o que a listagem única usa pra concatenar
    cards de várias fontes sem a prosa ao redor de cada um."""
    linhas = markdown.split("\n")
    blocos = extrai_blocos_de_habilidade(linhas)

    saida: list[str] = []
    cards: list[str] = []
    cursor = 0
    for b in blocos:
        saida.extend(linhas[cursor : b.inicio])
        card_html = monta_card(
            b.nome, b.flavor, b.campos, b.corpo, b.qualificador,
            grupo=grupo, arma=arma, arma_nome=arma_nome, elemento=elemento,
        )
        saida.append(card_html)
        cards.append(card_html)
        cursor = b.fim
    saida.extend(linhas[cursor:])

    return "\n".join(saida), len(blocos), cards


def ponteiro_habilidade(bloco: BlocoHabilidade, destino: str, arma: str = "") -> str:
    """Uma linha curta linkando pro card de verdade na listagem única."""
    ident = "hab-" + (f"{arma}-" if arma else "") + slug(bloco.nome)

    rotulos: list[str] = []
    chave = bloco.campos.get("Chave", "")
    if chave:
        rotulos = [texto_puro(p) for p in re.split(r"\s+-\s+|\s+·\s+", chave)]
    if bloco.qualificador and bloco.qualificador not in rotulos:
        rotulos.append(bloco.qualificador)
    resumo = " · ".join(r for r in rotulos if r)

    custo = custo_resumido(bloco.campos)
    cauda = " — " + " · ".join(p for p in (resumo, custo) if p) if (resumo or custo) else ""

    return f"- **[{escapa(bloco.nome)}]({destino}#{ident})**{cauda}"


def transforma_para_ponteiros(markdown: str, destino: str, arma: str = "") -> tuple[str, int]:
    """Troca cada bloco de habilidade por uma linha que aponta pro card na
    listagem única — usada nas páginas de grupo e no Arsenal, que perdem os
    cards completos pra não duplicar a mesma lista em vários lugares."""
    linhas = markdown.split("\n")
    blocos = extrai_blocos_de_habilidade(linhas)
    if not blocos:
        return markdown, 0

    saida: list[str] = []
    cursor = 0
    for b in blocos:
        saida.extend(linhas[cursor : b.inicio])
        saida.append(ponteiro_habilidade(b, destino, arma=arma))
        cursor = b.fim
    saida.extend(linhas[cursor:])

    return "\n".join(saida), len(blocos)


# -------------------------------------------------------- página de regras
#
# "Regras de Habilidade" não tem conteúdo próprio: é montada lendo, sem
# editar, as seções de regra que já existem em habilidades/index.md,
# marciais.md e magicas-elementais.md. O markdown original continua exatamente
# onde está — inclusive pros links externos que apontam pra ele continuarem
# funcionando (marciais.md#dano-desarmado, etc.).


def extrai_intervalo(
    linhas: list[str], inicio_regex: str, fim_regex: str | None = None
) -> list[str]:
    """O trecho [início, fim) que casa com início_regex até fim_regex
    (exclusivo) ou o fim do arquivo."""
    ini = next((i for i, l in enumerate(linhas) if re.match(inicio_regex, l)), None)
    if ini is None:
        return []
    fim = len(linhas)
    if fim_regex:
        fim = next(
            (i for i in range(ini + 1, len(linhas)) if re.match(fim_regex, linhas[i])),
            len(linhas),
        )
    return linhas[ini:fim]


def intro_antes_da_primeira_habilidade(linhas: list[str]) -> list[str]:
    """A prosa de abertura de uma seção, antes do primeiro bloco `**Nome**`."""
    fim = next((i for i, l in enumerate(linhas) if RE_NOME.match(l)), len(linhas))
    return linhas[:fim]


def monta_dano_desarmado(docs_dir: Path) -> list[str]:
    caminho = docs_dir / "habilidades" / "marciais.md"
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    return extrai_intervalo(linhas, r"^## Dano Desarmado\s*$", r"^## Habilidades Gerais\s*$")


def monta_assinaturas_elemento(docs_dir: Path) -> list[str]:
    """A seção 'Assinatura de Elemento' inteira.

    Cada um dos 11 elementos entra só como uma linha da tabela de assinatura
    aqui dentro — o `## Nome` de cada elemento no arquivo-fonte não guarda
    nenhuma prosa própria, vai direto pros blocos de habilidade (que já vivem
    na listagem única). Não há nada além da tabela pra extrair por elemento.
    """
    caminho = docs_dir / "habilidades" / "magicas-elementais.md"
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    return extrai_intervalo(linhas, r"^## Assinatura de Elemento\s*$", r"^## Terra\s*$")


def acrescenta_regras_dos_grupos(markdown: str, docs_dir: Path) -> str:
    """Grupos e Ficha de Habilidade já são conteúdo próprio de regras.md — só
    Dano Desarmado e Assinatura de Elemento continuam vivendo em marciais.md e
    magicas-elementais.md (que não encolheram, só perderam os cards de
    habilidade), então essas duas seções são lidas ao vivo e acrescentadas."""
    partes = [
        markdown.rstrip(),
        "",
        *monta_dano_desarmado(docs_dir),
        "",
        *monta_assinaturas_elemento(docs_dir),
    ]
    return "\n".join(partes)


# -------------------------------------------------------- página de condições
#
# "Condições" também não tem conteúdo próprio: reaproveita, ao vivo, as seções
# do glossário. O glossário segue sendo a única fonte — o que muda aqui é só o
# lugar de consulta (durante o combate, dentro do Livro do Jogador).

# Link relativo à raiz de docs/ (o glossário mora lá) reescrito para uma página
# um nível abaixo. Âncora pura, URL absoluta e link já relativo ficam de fora.
RE_LINK_RAIZ = re.compile(r"\]\((?!#|https?:|/|\.\./)([^)]+)\)")


def reancora_um_nivel(linhas: list[str]) -> list[str]:
    return [RE_LINK_RAIZ.sub(r"](../\1)", l) for l in linhas]


# Âncora pura: `[Lento](#lento)`. Vale se o verbete apontado veio junto; se
# ficou no glossário (`#vantagem`), o link tem que atravessar pra lá.
RE_ANCORA_PURA = re.compile(r"\]\(#([^)]+)\)")


def religa_ancoras(linhas: list[str], presentes: set[str]) -> list[str]:
    def sub(m: re.Match) -> str:
        chave = m.group(1)
        return m.group(0) if chave in presentes else f"](../glossario.md#{chave})"

    return [RE_ANCORA_PURA.sub(sub, l) for l in linhas]


def monta_condicoes(docs_dir: Path) -> list[str]:
    linhas = (docs_dir / "glossario.md").read_text(encoding="utf-8").split("\n")
    # O `## Condições` do glossário sai fora: nesta página ele repetiria o
    # próprio título. A prosa logo abaixo dele — a duração padrão — fica.
    partes = [
        *extrai_intervalo(linhas, r"^## Condições\s*$", r"^## ")[1:],
        "",
        *extrai_intervalo(linhas, r"^## Efeitos de Terreno\s*$", r"^## "),
    ]
    presentes = {slug(m.group(1)) for l in partes if (m := RE_VERBETE.match(l))}
    return religa_ancoras(reancora_um_nivel(partes), presentes)


# ----------------------------------------------------------------- arsenal

# Seções do Arsenal que são referência (dado/preço/propriedades), não armas —
# ficam de fora da varredura de habilidades de arma.
_ARSENAL_NAO_ARMA = {
    "tabela de dados de dano",
    "propriedades de arma",
    "resolucao de ataque",
}


def mapa_grupo_por_arma(arsenal_md: str) -> dict[str, str]:
    """Nome de arma (slug) -> grupo (marciais/pontaria/arcano), lido das 3
    tabelas de dado do Arsenal — é lá que o jogo já declara essa relação."""
    mapa: dict[str, str] = {}
    grupo_atual = ""
    dentro_tabela = False
    for linha in arsenal_md.split("\n"):
        if m := re.match(r"^### (Marciais|Pontaria|Arcano)\s*$", linha):
            grupo_atual = sem_acento(m.group(1))
            dentro_tabela = True
            continue
        if linha.startswith("## "):
            dentro_tabela = False
            continue
        if not dentro_tabela or not linha.startswith("|"):
            continue
        celula = linha.strip("|").split("|", 1)[0].strip()
        if m := re.match(r"^\[([^\]]+)\]", celula):
            mapa[slug(m.group(1))] = grupo_atual
    return mapa


def extrai_secoes_de_arma(arsenal_md: str) -> list[tuple[str, str]]:
    """[(nome_da_arma, markdown_da_secao), ...] — cada `## Nome` do Arsenal
    que não é uma das seções de referência acima."""
    linhas = arsenal_md.split("\n")
    cabecalhos = [
        (m.group(1).strip(), i)
        for i, linha in enumerate(linhas)
        if (m := re.match(r"^## (.+?)\s*$", linha))
    ]
    secoes = []
    for idx, (nome, inicio) in enumerate(cabecalhos):
        if sem_acento(nome) in _ARSENAL_NAO_ARMA:
            continue
        fim = cabecalhos[idx + 1][1] if idx + 1 < len(cabecalhos) else len(linhas)
        secoes.append((nome, "\n".join(linhas[inicio:fim])))
    return secoes


def cards_de_arma(arsenal_md: str) -> tuple[list[str], int]:
    """Todos os cards das 3 habilidades de cada uma das 62 armas."""
    mapa_grupo = mapa_grupo_por_arma(arsenal_md)
    todos: list[str] = []
    total = 0
    for nome, secao_md in extrai_secoes_de_arma(arsenal_md):
        arma_slug = slug(nome)
        grupo = mapa_grupo.get(arma_slug, "")
        _md, n, cards = transforma_habilidades(
            secao_md, grupo=grupo, arma=arma_slug, arma_nome=nome
        )
        todos.extend(cards)
        total += n
    return todos, total


def ponteiros_no_arsenal(arsenal_md: str, destino: str) -> tuple[str, int]:
    """Troca as 3 habilidades de cada arma por ponteiros pra listagem única,
    preservando intactas as seções de referência (dado, propriedades, etc.)
    e o flavor/Dano/Requisito de cada arma."""
    linhas = arsenal_md.split("\n")
    cabecalhos = [
        (m.group(1).strip(), i)
        for i, linha in enumerate(linhas)
        if (m := re.match(r"^## (.+?)\s*$", linha))
    ]
    saida: list[str] = []
    cursor = 0
    total = 0
    for idx, (nome, inicio) in enumerate(cabecalhos):
        fim = cabecalhos[idx + 1][1] if idx + 1 < len(cabecalhos) else len(linhas)
        saida.extend(linhas[cursor:inicio])
        if sem_acento(nome) in _ARSENAL_NAO_ARMA:
            saida.extend(linhas[inicio:fim])
        else:
            secao_md = "\n".join(linhas[inicio:fim])
            novo_md, n = transforma_para_ponteiros(secao_md, destino, arma=slug(nome))
            saida.extend(novo_md.split("\n"))
            total += n
        cursor = fim
    saida.extend(linhas[cursor:])
    return "\n".join(saida), total


# ------------------------------------------------------- listagem única

# As 10 páginas de grupo, exceto Mágicas por Elemento — essa precisa de
# tratamento à parte porque cada uma das 11 seções vira uma faceta de
# elemento diferente, não um grupo só.
_GRUPOS_ARQUIVO = (
    "marciais", "pontaria", "magicas-basicas", "sociais",
    "infiltracao", "mobilidade", "buff", "debuff", "suporte",
)


def cards_magicas_elementais(docs_dir: Path) -> tuple[list[str], int]:
    """Cada `## Elemento` do arquivo vira sua própria faceta — o arquivo tem
    um grupo só (Mágicas por Elemento), mas 11 assinaturas diferentes."""
    caminho = docs_dir / "habilidades" / "magicas-elementais.md"
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    cabecalhos = [
        (m.group(1).strip(), i)
        for i, l in enumerate(linhas)
        if (m := re.match(r"^## (.+?)\s*$", l))
    ]
    # O primeiro ## do arquivo é sempre a intro "Assinatura de Elemento";
    # todo o resto é um elemento, na ordem em que aparece.
    todos: list[str] = []
    total = 0
    for idx, (nome, inicio) in enumerate(cabecalhos[1:], start=1):
        fim = cabecalhos[idx + 1][1] if idx + 1 < len(cabecalhos) else len(linhas)
        secao = "\n".join(linhas[inicio:fim])
        _md, n, cards = transforma_habilidades(
            secao, grupo="magicas-elementais", elemento=slug(nome)
        )
        todos.extend(cards)
        total += n
    return todos, total


def monta_listagem_habilidades(docs_dir: Path) -> tuple[list[str], int]:
    """Todos os cards do jogo — os 9 grupos simples + Mágicas por Elemento
    (facetado por elemento) + as 186 habilidades de arma do Arsenal."""
    todos: list[str] = []
    total = 0

    for stem in _GRUPOS_ARQUIVO:
        caminho = docs_dir / "habilidades" / f"{stem}.md"
        _md, n, cards = transforma_habilidades(
            caminho.read_text(encoding="utf-8"), grupo=stem
        )
        todos.extend(cards)
        total += n

    cards_elem, n_elem = cards_magicas_elementais(docs_dir)
    todos.extend(cards_elem)
    total += n_elem

    arsenal_md = (docs_dir / "jogador" / "arsenal.md").read_text(encoding="utf-8")
    cards_arma, n_arma = cards_de_arma(arsenal_md)
    todos.extend(cards_arma)
    total += n_arma

    return todos, total


# ----------------------------------------------------------------- pacotes
#
# Um pacote não é uma habilidade: é uma trilha de 10 escolhas. O card dele
# reaproveita a mesma carcaça (.prg-card) porque o comportamento de leitura é
# idêntico — abre, fecha, filtra, responde a link direto —, mas o conteúdo é
# outro: vertente, arma inicial, atributo e a tabela de níveis, com cada
# habilidade linkada para o card que já existe na Listagem de Habilidades.


class Pacote(NamedTuple):
    inicio: int  # linha do `### Nome`
    fim: int  # linha seguinte ao fim da seção (exclusiva)
    nome: str
    flavor: str
    arma_md: str  # o campo inteiro, cru — pode trazer duas armas ou nenhuma
    atributo: str
    trilha: list[tuple[str, str]]  # [(nível, habilidade), ...]


def extrai_sorteio(markdown: str) -> dict[str, dict[str, object]]:
    """Slug do pacote -> vertente, número do d20 e conceito.

    Lido das 5 tabelas de sorteio: é lá que o jogo já declara a que vertente
    cada pacote pertence e com que número ele sai no d20. A listagem não
    repete essa lista — consulta.
    """
    fora: dict[str, dict[str, object]] = {}
    vertente = ""
    for linha in markdown.split("\n"):
        if m := re.match(r"^## (.+?)\s*$", linha):
            vertente = m.group(1).strip()
            continue
        if not vertente or not linha.startswith("|"):
            continue
        celulas = [c.strip() for c in linha.strip("|").split("|")]
        if len(celulas) < 3 or not celulas[0].isdigit():
            continue
        if not (m := re.match(r"^\[([^\]]+)\]\([^)#]*#([^)]+)\)", celulas[1])):
            continue
        chave = m.group(2).removeprefix("pac-")
        fora[chave] = {
            "vertente": vertente,
            "d20": int(celulas[0]),
            "conceito": celulas[2],
        }
    return fora


def extrai_pacotes(linhas: list[str]) -> list[Pacote]:
    """Toda seção `### Nome` com flavor + arma + atributo + tabela de níveis."""
    cabecalhos = [
        (m.group(1).strip(), i)
        for i, linha in enumerate(linhas)
        if (m := re.match(r"^### (.+?)\s*$", linha))
    ]
    pacotes: list[Pacote] = []
    for idx, (nome, inicio) in enumerate(cabecalhos):
        fim = cabecalhos[idx + 1][1] if idx + 1 < len(cabecalhos) else len(linhas)
        flavor = arma_md = atributo = ""
        trilha: list[tuple[str, str]] = []
        for linha in linhas[inicio + 1 : fim]:
            txt = linha.strip()
            if not txt:
                continue
            if not flavor and RE_FLAVOR.match(txt):
                flavor = txt.strip("*").strip()
            elif m := re.match(r"^-\s+\*\*Arma inicial:\*\*\s*(.+)$", txt):
                arma_md = m.group(1).strip()
            elif m := re.match(r"^-\s+\*\*Atributo em foco:\*\*\s*(.+)$", txt):
                atributo = m.group(1).strip()
            elif txt.startswith("|"):
                celulas = [c.strip() for c in txt.strip("|").split("|")]
                if len(celulas) >= 2 and celulas[0].isdigit():
                    trilha.append((celulas[0], celulas[1]))
        # Sem trilha não é um pacote — é outra coisa que usa `###`.
        if trilha:
            pacotes.append(
                Pacote(inicio, fim, nome, flavor, arma_md, atributo, trilha)
            )
    return pacotes


class IndiceHabilidades(NamedTuple):
    por_nome: dict[str, list[str]]
    por_arma_grau: dict[tuple[str, str], str]
    nomes_de_arma: dict[str, str]


def indice_de_habilidades(docs_dir: Path) -> IndiceHabilidades:
    """Os três dicionários que a trilha precisa pra virar link e faceta:

    1. slug do nome -> ids de card com aquele nome (lista: três nomes são
       usados por duas armas diferentes, daí o prefixo de arma no id);
    2. (slug da arma, grau) -> id — porque a trilha escreve "Espada - Básica",
       que não é o nome de nenhuma habilidade, e sim uma referência indireta;
    3. slug da arma -> nome como o Arsenal escreve. É esse o vocabulário que a
       faceta de arma usa, o mesmo da Listagem de Habilidades — o texto do
       link no pacote pode divergir ("Escudo" para a seção "Escudos").
    """
    por_nome: dict[str, list[str]] = {}
    por_arma_grau: dict[tuple[str, str], str] = {}
    nomes_de_arma: dict[str, str] = {}

    arsenal = (docs_dir / "jogador" / "arsenal.md").read_text(encoding="utf-8")
    for nome_arma, secao in extrai_secoes_de_arma(arsenal):
        arma = slug(nome_arma)
        nomes_de_arma[arma] = nome_arma
        for b in extrai_blocos_de_habilidade(secao.split("\n")):
            ident = f"hab-{arma}-{slug(b.nome)}"
            por_nome.setdefault(slug(b.nome), []).append(ident)
            grau = sem_acento(b.qualificador)
            if grau in _GRAUS_ARMA:
                por_arma_grau[(arma, grau)] = ident

    for stem in _GRUPOS_ARQUIVO + ("magicas-elementais",):
        md = (docs_dir / "habilidades" / f"{stem}.md").read_text(encoding="utf-8")
        for b in extrai_blocos_de_habilidade(md.split("\n")):
            por_nome.setdefault(slug(b.nome), []).append(f"hab-{slug(b.nome)}")

    return IndiceHabilidades(por_nome, por_arma_grau, nomes_de_arma)


# Uma única linha de trilha usa um nome que existe em dois cards: o Astrólogo
# pega "Onda de Choque" no nível 7, e esse nome é tanto a Especial do Revólver
# Maverick quanto uma habilidade de Debuff. O autor decidiu (2026-07-28) que é
# a de Debuff — a trilha inteira do Astrólogo é mágica. Qualquer colisão nova
# que apareça fica sem link de propósito: apontar pro card errado é pior do
# que não apontar.
DESAMBIGUACAO = {("astrologo", "onda-de-choque"): "hab-onda-de-choque"}

RE_GRAU_DE_ARMA = re.compile(r"^(.+?)\s+-\s+(Básica|Avançada|Especial)\s*$")
RE_MARCA = re.compile(r"\s*\*\(([^)]+)\)\*\s*$")


def resolve_habilidade(
    bruto: str,
    pacote_slug: str,
    por_nome: dict[str, list[str]],
    por_arma_grau: dict[tuple[str, str], str],
) -> tuple[str, str, str]:
    """'Fluxo Elegante *(Supremo)*' -> (nome, marca, id do card ou '').

    Id vazio significa "não deu pra ter certeza" — o texto sai sem link.
    """
    marca = m.group(1) if (m := RE_MARCA.search(bruto)) else ""
    nome = RE_MARCA.sub("", bruto).strip()

    if m := RE_GRAU_DE_ARMA.match(nome):
        chave = (slug(m.group(1)), sem_acento(m.group(2)))
        return nome, marca, por_arma_grau.get(chave, "")

    if ident := DESAMBIGUACAO.get((pacote_slug, slug(nome))):
        return nome, marca, ident

    ids = por_nome.get(slug(nome), [])
    return nome, marca, ids[0] if len(ids) == 1 else ""


def armas_do_campo(arma_md: str, nomes_de_arma: dict[str, str]) -> list[tuple[str, str]]:
    """[(slug, nome), ...] de toda arma linkada no campo Arma inicial.

    O campo nem sempre é um link só: alguns pacotes começam com arma + escudo,
    com duas armas, ou com uma alternativa ("senão, comece com Báculo"). Todas
    entram no filtro, porque todas são caminhos que o texto de fato oferece.

    A identidade da arma vem da âncora do link, não do texto: o pacote escreve
    "Escudo" onde o Arsenal tem a seção "Escudos", e as duas precisam cair no
    mesmo valor de filtro que a Listagem de Habilidades usa.
    """
    achados = re.findall(r"\[([^\]]+)\]\([^)]*arsenal\.md#([^)\s]+)\)", arma_md)
    vistos: dict[str, str] = {}
    for texto, ancora in achados:
        # Âncora desconhecida (uma seção do Arsenal que não é arma, por
        # exemplo): cai no texto, que ao menos continua legível no filtro.
        vistos.setdefault(ancora, nomes_de_arma.get(ancora, texto))
    return list(vistos.items())


def monta_card_pacote(
    p: Pacote,
    meta: dict[str, object],
    indice: IndiceHabilidades,
    sem_link: list[str],
) -> str:
    ident = "pac-" + slug(p.nome)
    vertente_nome = str(meta.get("vertente", ""))
    d20 = meta.get("d20")

    linhas_trilha: list[str] = []
    nomes_trilha: list[str] = []
    final_nome = ""
    for nivel, bruto in p.trilha:
        nome, marca, alvo = resolve_habilidade(
            bruto, slug(p.nome), indice.por_nome, indice.por_arma_grau
        )
        nomes_trilha.append(nome)
        if not alvo:
            sem_link.append(f"{p.nome} · nível {nivel} · {nome}")
        texto = f"[{nome}](../habilidades/index.md#{alvo})" if alvo else nome
        if marca:
            texto += f" *({marca})*"
        linhas_trilha.append(f"| {nivel} | {texto} |")
        if nivel == "19":
            final_nome = nome

    armas = armas_do_campo(p.arma_md, indice.nomes_de_arma)
    atributos = computa_atributos(p.atributo)

    colunas = ""
    for rotulo, valor in (
        ("Arma inicial", ", ".join(n for _, n in armas) or "sem arma"),
        ("Atributo", resume_atributo(p.atributo)),
        ("Termina em", final_nome),
    ):
        if valor:
            colunas += (
                f'<span class="prg-card__col" data-rot="{rotulo}">'
                f"{escapa(valor)}</span>"
            )

    chip = (
        f'<span class="prg-chip prg-chip--vert-{slug(vertente_nome)}">'
        f"{escapa(vertente_nome)}</span>"
        if vertente_nome
        else ""
    )

    # A trilha inteira entra no índice: "que pacote usa Fluxo?" tem que se
    # responder digitando "fluxo" na busca, não só pelos menus.
    busca = escapa(
        sem_acento(
            " ".join(
                " ".join(
                    [
                        p.nome,
                        p.flavor,
                        vertente_nome,
                        str(meta.get("conceito", "")),
                        texto_puro(p.arma_md),
                        p.atributo,
                        *nomes_trilha,
                    ]
                ).split()
            )
        )
    )

    facetas = (
        f'data-vertente="{slug(vertente_nome)}" '
        f'data-vertente-nome="{escapa(vertente_nome)}" '
        f'data-d20="{d20 if d20 is not None else ""}" '
        f'data-armas="{" ".join(s for s, _ in armas) or "sem-arma"}" '
        f'data-armas-nome="{escapa("|".join(n for _, n in armas) or "Sem arma inicial")}" '
        f'data-atributos="{" ".join(atributos)}" '
        f'data-final="{slug(final_nome)}" '
        f'data-final-nome="{escapa(final_nome)}"'
    )

    corpo = [
        f"*{p.flavor}*" if p.flavor else "",
        "",
        f"- **Arma inicial:** {p.arma_md}",
        f"- **Atributo em foco:** {p.atributo}",
        "",
        "| Nível | Habilidade |",
        "|---|---|",
        *linhas_trilha,
    ]

    selo = f"nº {d20}" if d20 is not None else ""
    return (
        f'<div class="prg-card prg-card--pacote" id="{ident}" data-busca="{busca}" '
        f'{facetas} markdown="block">\n'
        f'<button class="prg-card__hd" type="button" aria-expanded="false" '
        f'aria-controls="{ident}-bd">\n'
        f'<span class="prg-card__nome">{escapa(p.nome)}</span>\n'
        f'<span class="prg-card__chips">{chip}</span>\n'
        f'<span class="prg-card__custo prg-card__d20">{escapa(selo)}</span>\n'
        f'<span class="prg-card__seta" aria-hidden="true"></span>\n'
        f'<span class="prg-card__cols">{colunas}</span>\n'
        f"</button>\n"
        f'<div class="prg-card__bd" id="{ident}-bd" markdown="1">\n\n'
        + "\n".join(corpo)
        + f"\n\n</div>\n</div>\n"
    )


def transforma_pacotes(markdown: str, docs_dir: Path) -> tuple[str, int, list[str]]:
    """Cada `### Pacote` vira um card; o resto da página fica como está.

    Retorna também a lista de pontos da trilha que ficaram sem link, pra que
    o build possa reclamar em voz alta em vez de esconder o problema.
    """
    linhas = markdown.split("\n")
    pacotes = extrai_pacotes(linhas)
    if not pacotes:
        return markdown, 0, []

    sorteio_md = (docs_dir / "pacotes" / "sorteio.md").read_text(encoding="utf-8")
    sorteio = extrai_sorteio(sorteio_md)
    indice = indice_de_habilidades(docs_dir)

    sem_link: list[str] = []
    saida: list[str] = []
    cursor = 0
    for p in pacotes:
        saida.extend(linhas[cursor : p.inicio])
        saida.append(
            monta_card_pacote(p, sorteio.get(slug(p.nome), {}), indice, sem_link)
        )
        cursor = p.fim
    saida.extend(linhas[cursor:])

    return "\n".join(saida), len(pacotes), sem_link


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

    if caminho == "habilidades/regras.md":
        return acrescenta_regras_dos_grupos(markdown, Path(config["docs_dir"]))

    if caminho == "jogar/condicoes.md":
        corpo = monta_condicoes(Path(config["docs_dir"]))
        return markdown.rstrip() + "\n\n" + "\n".join(corpo)

    if caminho == "habilidades/index.md":
        cards, total = monta_listagem_habilidades(Path(config["docs_dir"]))
        barra = (
            '<div class="prg-filtro" data-rotulo="habilidades">\n'
            '<div class="prg-filtro__linha1">\n'
            '<input type="search" class="prg-filtro__campo" '
            'placeholder="Filtrar por nome, efeito, condição…" '
            'aria-label="Filtrar habilidades">\n'
            '<span class="prg-filtro__contagem"></span>\n'
            '<button type="button" class="prg-filtro__tudo">Expandir tudo</button>\n'
            "</div>\n"
            '<div class="prg-filtro__linha2">\n'
            '<select class="prg-filtro__select" data-faceta="grupo" '
            'aria-label="Filtrar por tipo"><option value="">Todos os tipos</option></select>\n'
            '<select class="prg-filtro__select" data-faceta="elemento" '
            'aria-label="Filtrar por elemento"><option value="">Todos os elementos</option></select>\n'
            '<select class="prg-filtro__select" data-faceta="arma" '
            'aria-label="Filtrar por arma"><option value="">Todas as armas</option></select>\n'
            '<select class="prg-filtro__select" data-faceta="atributos" data-multi="1" '
            'aria-label="Filtrar por atributo"><option value="">Todos os atributos</option></select>\n'
            '<select class="prg-filtro__select" data-faceta="alvo" '
            'aria-label="Filtrar por alvo"><option value="">Todos os alvos</option></select>\n'
            "</div>\n"
            '<div class="prg-filtro__linha3">\n'
            '<label class="prg-filtro__mana">\n'
            '<span>Mana disponível: <output class="prg-filtro__mana-valor"></output></span>\n'
            '<input type="range" class="prg-filtro__mana-slider" min="0" value="0" '
            'aria-label="Mana disponível">\n'
            "</label>\n"
            '<label class="prg-filtro__desarmado">\n'
            '<input type="checkbox" class="prg-filtro__desarmado-campo"> '
            "Só Dano Desarmado\n"
            "</label>\n"
            "</div>\n"
            "</div>\n\n"
        )
        return markdown.rstrip() + "\n\n" + barra + "\n".join(cards)

    if caminho == "pacotes/index.md":
        markdown, total, sem_link = transforma_pacotes(
            markdown, Path(config["docs_dir"])
        )
        if sem_link:
            print(
                f"[prisma] {len(sem_link)} habilidade(s) da trilha sem link: "
                + "; ".join(sem_link)
            )
        barra = (
            '<div class="prg-filtro" data-rotulo="pacotes">\n'
            '<div class="prg-filtro__linha1">\n'
            '<input type="search" class="prg-filtro__campo" '
            'placeholder="Filtrar por nome, conceito, habilidade da trilha…" '
            'aria-label="Filtrar pacotes">\n'
            '<span class="prg-filtro__contagem"></span>\n'
            '<button type="button" class="prg-filtro__tudo">Expandir tudo</button>\n'
            "</div>\n"
            '<div class="prg-filtro__linha2">\n'
            '<select class="prg-filtro__select" data-faceta="vertente" '
            'aria-label="Filtrar por vertente">'
            "<option value=\"\">Todas as vertentes</option></select>\n"
            '<select class="prg-filtro__select" data-faceta="armas" data-multi="1" '
            'aria-label="Filtrar por arma inicial">'
            "<option value=\"\">Todas as armas iniciais</option></select>\n"
            '<select class="prg-filtro__select" data-faceta="atributos" data-multi="1" '
            'aria-label="Filtrar por atributo em foco">'
            "<option value=\"\">Todos os atributos</option></select>\n"
            '<select class="prg-filtro__select" data-faceta="final" '
            'aria-label="Filtrar pela habilidade de nível 19">'
            "<option value=\"\">Termina em qualquer coisa</option></select>\n"
            "</div>\n"
            '<div class="prg-filtro__linha3">\n'
            '<select class="prg-filtro__sorteio-vertente" '
            'aria-label="Vertente do sorteio">'
            "<option value=\"\">Qualquer vertente</option></select>\n"
            '<button type="button" class="prg-filtro__sortear">Sortear pacote (1d20)'
            "</button>\n"
            '<span class="prg-filtro__sorteio-saida" role="status"></span>\n'
            "</div>\n"
            "</div>\n\n"
        )
        marca = '<div class="prg-card prg-card--pacote"'
        corte = markdown.find(marca)
        return markdown[:corte] + barra + markdown[corte:] if corte != -1 else markdown

    if caminho == "jogador/arsenal.md":
        markdown, total = ponteiros_no_arsenal(markdown, "../habilidades/index.md")
        return markdown

    if caminho.startswith(PAGINAS_COM_CARD) and not caminho.endswith("index.md"):
        grupo = Path(caminho).stem
        markdown = aplica_arte(markdown, f"brasao-{grupo}")
        markdown, total = transforma_para_ponteiros(markdown, "index.md")
        if total:
            aviso = (
                f"!!! mestre \"As {total} habilidades gerais deste grupo mudaram de lugar\"\n"
                f"    Agora vivem, com o card completo, na "
                f"[Listagem de Habilidades](index.md) — filtrável por grupo, elemento, "
                f"arma, atributo, alvo e Mana. Aqui embaixo ficam só os links diretos.\n\n"
            )
            marca = "\n- **["
            corte = markdown.find(marca)
            if corte != -1:
                corte += 1  # não engole a quebra de linha anterior ao primeiro ponteiro
                markdown = markdown[:corte] + aviso + markdown[corte:]

    return markdown


# ------------------------------------------------------------ redirecionamento
#
# A reorganização de 2026-07-29 mudou o endereço de cinco páginas do Livro do
# Jogador. Links que já circulam por aí (e o histórico do navegador de quem
# leu antes) continuam valendo: cada endereço antigo vira uma página que
# redireciona, preservando a âncora quando ela tem um destino equivalente.

# url antiga (sem barra final) -> url nova
REDIRECIONA = {
    "jogador/introducao": "jogar/",
    "jogador/sistema-d20": "jogar/",
    "jogador/pontos-de-acao": "jogar/combate/",
    "jogador/mana": "jogar/mana/",
    "jogador/tocado": "criacao/tocado/",
}

# âncora antiga em jogador/sistema-d20 -> url nova completa
ANCORAS_D20 = {
    "criacao-de-personagem": "criacao/",
    "distribuicao-na-criacao": "criacao/#1-atributos",
    "progressao-de-nivel": "criacao/progressao/",
    "atributos": "jogar/atributos/",
    "testes": "jogar/testes/",
    "testes-sociais": "jogar/testes/#testes-sociais",
    "rerolagens": "jogar/testes/#rerolagens",
    "iniciativa": "jogar/combate/#iniciativa",
    "defesa": "jogar/combate/#defesa",
    "base-de-resiliencia": "jogar/combate/#base-de-resiliencia",
    "quem-rola-o-dado": "jogar/combate/#quem-rola-o-dado",
    "valores-derivados": "jogar/dano-e-cura/",
    "vida": "jogar/dano-e-cura/#vida",
    "dados-de-vida": "jogar/dano-e-cura/#dados-de-vida",
    "chegando-a-0-de-vida": "jogar/dano-e-cura/#chegando-a-0-de-vida",
    "o-ultimo-turno": "jogar/dano-e-cura/#o-ultimo-turno",
    "tipos-de-dano": "jogar/dano-e-cura/#tipos-de-dano",
    "resistencia-imunidade-e-vulnerabilidade":
        "jogar/dano-e-cura/#resistencia-imunidade-e-vulnerabilidade",
    "estresse": "jogar/estresse/",
    "colapso": "jogar/estresse/#colapso",
    "reduzindo-estresse": "jogar/estresse/#reduzindo-estresse",
}

# âncora antiga em jogador/pontos-de-acao -> url nova completa
ANCORAS_PA = {
    "movimento": "jogar/combate/#movimento",
    "voo": "jogar/combate/#voo",
    "custo-em-pa-de-habilidades": "jogar/combate/#custo-em-pa-de-habilidades",
}

# A exploração virou duas páginas: a regra foi pro jogador, o uso ficou com o
# Mestre. Só as âncoras que migraram entram aqui — as que ficaram não precisam.
ANCORAS_EXPLORACAO = {
    "descanso": "jogar/exploracao/#descanso",
    "viagem": "jogar/exploracao/#viagem",
    "exaustao": "jogar/exploracao/#exaustao",
    "clima-extremo": "jogar/exploracao/#clima-extremo",
    "agua": "jogar/exploracao/#agua",
    "luz-e-escuridao": "jogar/exploracao/#luz-e-escuridao",
}

PAGINA_REDIRECT = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<title>Esta página mudou de lugar</title>
<link rel="canonical" href="{base}{destino}">
<script>
var mapa = {mapa};
var chave = decodeURIComponent(location.hash.replace('#', ''));
var alvo = (chave && mapa[chave]) || {destino_js};
location.replace({base_js} + alvo);
</script>
<meta http-equiv="refresh" content="2; url={base}{destino}">
</head><body>
<p>Esta página mudou de lugar. Se o navegador não seguir sozinho,
<a href="{base}{destino}">clique aqui</a>.</p>
</body></html>
"""


def escreve_redirecionamentos(site_dir: Path, base: str) -> int:
    ancoras = {
        "jogador/sistema-d20": ANCORAS_D20,
        "jogador/pontos-de-acao": ANCORAS_PA,
    }
    escritos = 0
    for antiga, destino in REDIRECIONA.items():
        pasta = site_dir / antiga
        pasta.mkdir(parents=True, exist_ok=True)
        mapa = ancoras.get(antiga, {})
        (pasta / "index.html").write_text(
            PAGINA_REDIRECT.format(
                base=base,
                base_js=json.dumps(base),
                destino=destino,
                destino_js=json.dumps(destino),
                mapa=json.dumps(mapa, ensure_ascii=False),
            ),
            encoding="utf-8",
        )
        escritos += 1

    # mestre/exploracao continua existindo — só as âncoras migradas redirecionam,
    # e isso é feito por um script embutido na própria página gerada.
    pagina = site_dir / "mestre" / "exploracao" / "index.html"
    if pagina.exists():
        script = (
            "<script>(function(){var m="
            + json.dumps(ANCORAS_EXPLORACAO, ensure_ascii=False)
            + ";var c=decodeURIComponent(location.hash.replace('#',''));"
            + "if(c&&m[c]){location.replace(" + json.dumps(base) + "+m[c]);}})();</script>"
        )
        html = pagina.read_text(encoding="utf-8")
        pagina.write_text(html.replace("</head>", script + "</head>", 1), encoding="utf-8")
        escritos += 1

    return escritos


def on_post_build(config, **kwargs):
    base = urlsplit(config["site_url"] or "/").path or "/"
    n = escreve_redirecionamentos(Path(config["site_dir"]), base)
    print(f"[prisma] {n} redirecionamento(s) de endereço antigo escrito(s)")

    destino = Path(config["site_dir"]) / "assets" / "glossario.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        json.dumps(_glossario, ensure_ascii=False), encoding="utf-8"
    )
