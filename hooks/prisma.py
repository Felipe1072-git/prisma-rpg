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
3. `mundo`      — página de docs/mundo/ com `tipo:` no cabeçalho vira wiki: o
                  bloco de bullets logo abaixo do título vira ficha lateral, e
                  a página entra em assets/mundo.json pro mesmo popover de hover.
4. `paginas`    — rede genérica pro popover: toda página (menos Mundo e o
                  próprio glossário, que já têm dicionário dedicado) entra em
                  assets/paginas.json com o primeiro parágrafo da página e de
                  cada seção (`##`/`###`) dela. Qualquer link interno que não
                  seja termo de glossário, card de habilidade nem página de
                  Mundo cai aqui — é o que faz "todo link do site tem uma
                  espiada" sem precisar escrever um resumo à mão pra cada um.

Se o parser não reconhecer um bloco, ele é deixado exatamente como está — o pior
caso é a página continuar igual a hoje.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable, NamedTuple
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
# Rótulos que viram coluna no cabeçalho colapsado, na ordem em que aparecem.
# Chave e Custo são pulados: viram chip e selo. Alvos fica por último porque é
# de longe o mais comprido (24 caracteres em média) e é o que trunca.
# Alcance e Cooldown entraram em 2026-08-25 por serem os campos que mais
# variam entre habilidades cabendo em poucos caracteres — o valor mais comum
# de cada um aparece em só 27% e 33% dos cards, então quase sempre dizem algo
# novo. Duração e Resolução ficaram de fora pelo motivo oposto.
COLUNAS = ("Chave", "Atributo", "Custo", "Alcance", "Cooldown", "Alvos")

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
    "necromancia": "necromancia",
    "projecao mental": "projecao-mental",
    "alquimia de mana": "alquimia-de-mana",
    "percepcao arcana": "percepcao-arcana",
    "conjuracao": "conjuracao",
    "basica": "grau",
    "avancada": "grau",
    "especial": "grau",
    "menor": "grau",
    "medio": "grau",
    "moderado": "grau",
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


_ATRIBUTOS_BASE = ("ataque", "agilidade", "magia", "exploracao", "social")

# Habilidade só rola com um destes cinco, mas Raça e Origem mexem nos oito.
# (d100, 2026-08-20: substitui os 8 atributos antigos — Força→Ataque,
# Vitalidade→Defesa, Inteligência→Magia, Sabedoria→Exploração, Vontade→Social,
# mais o 8º atributo novo, Exploração, que não tinha equivalente direto.)
ATRIBUTOS_TODOS = (
    ("ataque", "Ataque"),
    ("defesa", "Defesa"),
    ("agilidade", "Agilidade"),
    ("magia", "Magia"),
    ("exploracao", "Exploração"),
    ("social", "Social"),
    ("sorte", "Sorte"),
    ("sanidade", "Sanidade"),
)


def atributos_citados(bruto: str) -> list[tuple[str, str]]:
    """Os oito atributos citados num texto livre, na ordem canônica da ficha."""
    texto = sem_acento(bruto)
    return [(chave, nome) for chave, nome in ATRIBUTOS_TODOS if chave in texto]


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


# Os 10 elementos + Arcano — o mesmo vocabulário da faceta "elemento" que o
# filtro já conhece (RESUMO.elemento no prisma.js).
_ELEMENTOS_VALIDOS = {
    "fogo", "gelo", "terra", "raio", "agua", "vento",
    "luz", "sombras", "veneno", "sangue", "arcano",
}


def elemento_do_campo_dano(campos: dict[str, str]) -> str:
    """Fora de Mágicas por Elemento, ninguém atribui elemento por seção — mas
    a própria habilidade já declara `**Dano:** Fogo` (ou Arcano, de longe o
    caso mais comum em Buff/Debuff/Suporte/etc.). Quando o valor bate exato
    com um dos 11 nomes conhecidos, vira a mesma faceta que Mágicas por
    Elemento usa; texto composto ("usa o dado da arma", "Impacto") não bate
    e fica de fora — só filtra o que dá pra reconhecer com certeza."""
    candidato = slug(texto_puro(campos.get("Dano", "")))
    return candidato if candidato in _ELEMENTOS_VALIDOS else ""


def custo_resumido(campos: dict[str, str]) -> str:
    """Uma string curta de custo para o cabeçalho: '3–18 Mana'.

    **Só o Mana** (decisão do autor, 2026-08-24). O PA saía aqui como
    '◈–◈◈◈ · 3–18 Mana', mas quase toda habilidade do jogo é ◈–◈◈◈ ou ◈◈◈:
    o símbolo ocupava a coluna mais visível do cabeçalho sem distinguir um
    card do outro numa lista de 754. Ele continua onde é decisão de verdade —
    dentro de cada Intensidade, no corpo do card.

    Vale pros três lugares que usam esta string (cabeçalho, ponteiro das
    páginas de grupo e popover), porque os três são listas de varredura.
    """
    if bruto := campos.get("Custo fixo"):
        txt = texto_puro(bruto).split("|")[0].strip()
        if m := re.search(r"(\d+)\s*Mana", txt):
            return f"{m.group(1)} Mana"
        # Custo em Vida (magia de sangue) não tem Mana pra resumir: mostra o
        # que sobra depois de tirar o PA, pra não ser o único selo da lista
        # com ◈ — "◈◈ (2 PA) + 4d4 de Vida" vira "4d4 de Vida".
        return re.sub(r"^[◈\s]*\(\d+\s*PA\)\s*\+\s*", "", txt)

    manas = [
        int(m.group(1))
        for rotulo, valor in campos.items()
        if rotulo.startswith("Intensidade")
        if (m := re.search(r"(\d+)\s*Mana", rotulo + " " + valor))
    ]
    if not manas:
        return custo_em_vida(campos)
    lo, hi = min(manas), max(manas)
    return f"{lo} Mana" if lo == hi else f"{lo}–{hi} Mana"


def custo_em_vida(campos: dict[str, str]) -> str:
    """O selo de quem paga em Vida em vez de Mana (Sangue, Necromancia).

    Sem isto essas doze habilidades ficariam com o selo vazio — indistinguíveis
    de uma Passiva na lista, quando são justamente as que cobram mais caro.
    """
    # Custo único, num campo próprio: "custa sempre **4d4 de Vida**".
    if bruto := campos.get("Custo em Vida"):
        if m := re.search(r"(\d+d\d+)\s*de Vida", texto_puro(bruto)):
            return f"{m.group(1)} de Vida"

    # Ou um valor por Intensidade: "◈ (1 PA) + 1d4 de Vida". O dict preserva
    # a ordem do markdown, então o primeiro e o último são I e III.
    vidas = [
        m.group(1)
        for rotulo, valor in campos.items()
        if rotulo.startswith("Intensidade")
        if (m := re.search(r"(\d+d\d+)\s*de Vida", rotulo + " " + valor))
    ]
    if not vidas:
        return ""
    if vidas[0] == vidas[-1]:
        return f"{vidas[0]} de Vida"
    return f"{vidas[0]}–{vidas[-1]} de Vida"


_GRAUS_ARMA = ("basica", "avancada", "especial")

# A Escala de Poder — ver jogar/regras-de-habilidade.md#escala-de-poder.
# **Derivada**, não escrita na ficha: sai dos quatro eixos medidos em
# `escala_de_poder`. O vocabulário antigo (Moderado/Supremo/Médio) media o
# custo em Mana, não a entrega — e como 69 dos 71 Supremos custavam os mesmos
# 48 Mana, ele não distinguia nada: Moderado, Maior e Supremo entregavam o
# mesmo dano médio (11,4 / 11,1 / 12,3).
_ESCALA_GERAL = ("menor", "moderada", "notavel", "maior", "suprema")
_ESCALA_VALIDOS = _GRAUS_ARMA + _ESCALA_GERAL

# Os nomes na ordem em que a soma dos dois maiores eixos os produz (0 a 4).
ESCALA_POR_PESO = ("Menor", "Moderada", "Notável", "Maior", "Suprema")

# Vocabulário aposentado em 2026-08-26. Uma ficha que ainda o traga no
# qualificador é ignorada — senão as 462 que já declaravam a escala velha
# venceriam a régua nova como se fossem exceção deliberada, e a redistribuição
# não aconteceria. Exceção de verdade se escreve com `**Escala:**`.
_ESCALA_APOSENTADA = ("medio", "moderado", "supremo")

# Componentes (V/S/M) por Grupo — ver habilidades/regras.md#componentes. Buff,
# Debuff e Suporte ficam fora de propósito: misturam efeito físico e mágico,
# então não têm padrão único, e cada habilidade declara o próprio.
GRUPO_COMPONENTES = {
    "marciais": "S, M",
    "pontaria": "S, M",
    "magicas-elementais": "V, S",
    "necromancia": "V, S",
    "alquimia-de-mana": "V, S",
    "conjuracao": "V, S",
    "espaco-tempo": "V, S",
    # Projeção Mental é a exceção com peso narrativo: funciona em qualquer
    # mente, sem depender de palavras — nunca tem Verbal.
    "projecao-mental": "S",
    "sociais": "V",
    "infiltracao": "S",
    "mobilidade": "S",
    "percepcao-arcana": "S",
}

# Cooldown por grau de arma — ver jogar/regras-de-habilidade.md#cooldown. A
# faixa de baixo é o padrão; a própria habilidade sobrescreve com **Cooldown:**
# quando merece o valor alto da faixa ou a exceção "1x por descanso".
ESCALA_COOLDOWN = {
    "basica": "Sem cooldown",
    "avancada": "1 rodada",
    "especial": "2 rodadas",
}

# Cooldown das habilidades gerais — vem do **custo em Mana**, não da Escala de
# Poder. As duas coisas se separaram em 2026-08-26: a Escala passou a medir o
# que a habilidade entrega, e o cooldown continua sendo função do que ela
# custa. Amarrar o cooldown à Escala nova mudaria a mecânica de centenas de
# fichas de uma vez, sem nenhuma mesa pra verificar. As faixas são as do Grau
# (jogar/mana.md#faixas-de-mana), então o cooldown das fichas que já
# declaravam a escala certa não muda: das 83 que mudaram na virada, 63 eram
# lacunas (o card mostrava "—") e 20 eram fichas cuja escala escrita não batia
# com o próprio custo — catorze delas gerais rotuladas "Especial", que é grau
# de arma e cobrava 3 rodadas por um teto de 18 Mana.
COOLDOWN_POR_MANA = ((9, "Sem cooldown"), (24, "1 rodada"), (45, "2 rodadas"))
COOLDOWN_SUPREMO = "1x por cena"

# Fallback pra quem não gasta Mana: as habilidades de Sangue pagam com Vida, e
# sem Mana o cooldown vem da Escala de Poder.
COOLDOWN_POR_ESCALA = {
    "menor": "Sem cooldown",
    "moderada": "1 rodada",
    "notavel": "1 rodada",
    "maior": "2 rodadas",
    "suprema": "1x por cena",
}

# --- Escala de Poder: os quatro eixos -------------------------------------
#
# Ver jogar/regras-de-habilidade.md#escala-de-poder. Cada eixo vale 0, 1 ou 2,
# e a Escala é a soma dos **dois maiores** — não dos quatro. Somar todos
# achatava tudo no meio, porque os eixos são trocados entre si por desenho: uma
# habilidade de área grande dá menos dano por alvo, e as correlações medidas
# entre os quatro ficam todas perto de zero ou negativas. A soma dos dois
# maiores pergunta "quão longe ela vai naquilo em que é forte", que é o que se
# sente na mesa, e não penaliza a especialista.

_RE_LINK_MD = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def _texto_de_eixo(corpo: list[str]) -> str:
    """O corpo da ficha em texto corrido e minúsculo, sem markdown.

    Os links **precisam** cair antes da medição: "antes do fim da
    [cena](../glossario.md#cena)" não casa com "fim da cena" enquanto o alvo do
    link estiver no meio, e era isso que fazia a duração e as condições
    passarem despercebidas em boa parte das fichas.
    """
    txt = _RE_LINK_MD.sub(r"\1", "\n".join(corpo))
    return re.sub(r"[*_`]", "", txt).lower()


def eixo_dano(texto: str) -> int:
    """0 = até 7 de dano médio · 1 = 8 a 16 · 2 = 17 ou mais.

    Os cortes são os das **habilidades gerais**, que são as únicas que usam a
    Escala de Poder — as de arma se classificam pelo grau. Calibrado contra a
    distribuição real delas (p20 ≈ 5,5 · mediana ≈ 10,5 · p80 ≈ 20): com o
    corte alto em 26 que as de arma pediriam, só 12 das 494 chegavam ao degrau
    2, e o eixo praticamente não separava nada.

    Lê o maior dado da ficha inteira, sem escolher linha: a Intensidade III
    sempre traz o maior. Filtrar por linha fazia a linha de ficha das
    habilidades de Custo fixo (`**Custo fixo:** … **Dano:** Raio`) sequestrar a
    leitura — ela contém a palavra "Dano" e nenhum dado —, e com ela quase toda
    Suprema era medida como se não causasse dano nenhum.
    """
    melhor = 0.0
    for linha in texto.split("\n"):
        for m in re.finditer(r"(\d+)d(\d+)", linha):
            # 4d4 de Vida é o preço da habilidade, não o que ela entrega.
            if re.search(r"de vida|de estresse|de mana", linha[m.end():m.end() + 22]):
                continue
            melhor = max(melhor, int(m.group(1)) * (int(m.group(2)) + 1) / 2)
    return 0 if melhor <= 7 else 1 if melhor <= 16 else 2


def eixo_alcance(alvos: str, texto: str) -> int:
    """0 = um alvo ou o usuário · 1 = poucos, cone, linha, raio 1–2 · 2 = raio 3+."""
    a = _texto_de_eixo([alvos])
    if re.search(
        r"campo de batalha|à vista|todos os inimigos|todos os aliados|o grupo",
        a + " " + texto,
    ):
        return 2
    if m := re.search(r"(\d+)\s*casas? de raio", a):
        return 2 if int(m.group(1)) >= 3 else 1
    if "usuário e aliados" in a:
        return 2
    if re.search(
        r"todas as criaturas|cone de|em linha|na linha|linhas de|adjacentes"
        r"|até \d+ criaturas|\d+ alvos|\d+ criaturas",
        a,
    ):
        return 1
    return 0


# Tirar do jogo é o degrau alto do eixo: o alvo perde o turno, a posição ou a
# própria ação. Derrubar entra porque levantar custa PA.
#
# São **radicais**, não os nomes das condições: a ficha escreve o verbo com
# muito mais frequência que o particípio — "derruba" aparece em 281 fichas e
# "derrubado" em 37 —, então casar só pelo nome da condição perdia a maioria
# das habilidades que aplicam a mais comum de todas.
_TIRA_DO_JOGO = (
    "atordoa", "imóvel", "imobiliza", "petrifica", "possu", "amedronta",
    "cego", "cega o", "silencia", "agarra",
)
# Derrubar fica **fora** do degrau alto, apesar de custar PA pra levantar: ele
# aparece em 281 das 753 fichas — é o verbo padrão do jogo, não um efeito raro
# (o "clichê marcial" de 2026-08-27 é justamente isso). E o alvo derrubado
# ainda age no turno dele, enquanto o Atordoado perde o turno inteiro. Tratar
# os dois como iguais empurrava metade do jogo pro topo da Escala.
# Efeitos que reescrevem a cena em vez de modificá-la.
_EFEITO_ABSOLUTO = (
    "ressuscit", "volta à vida", "desperta nesse corpo", "invoca",
    "aliado de combate", "banir", "reverte", "refaz", "rebobina",
    "turno extra", "ação extra", "controla", "domina", "teleporta", "dissipa",
)
_CONDICAO_COMUM = (
    "sangrando", "sangra", "queimando", "queima", "lento", "envenena",
    "derruba",
    "marcado", "escudo", "risco", "desprevenido", "exausto", "maldição",
    "amaldiçoad",
)


def eixo_controle(texto: str) -> int:
    """0 = só dano · 1 = condição comum, cura, bônus pequeno · 2 = tira do jogo.

    Bônus de +10 ou mais conta como degrau alto: a reescala de 2026-08-26 pôs
    os buffs pessoais em +5/+10/+15, e medir só "tem um +N" não distinguia um
    +2 de um +15 — o que rebaixava justamente os buffs Supremos.
    """
    if any(t in texto for t in _EFEITO_ABSOLUTO) or any(t in texto for t in _TIRA_DO_JOGO):
        return 2
    if any(int(m.group(1)) >= 10 for m in re.finditer(r"\+(\d+)\b", texto)):
        return 2
    # Vantagem vale ~25%, e é o efeito forte do sistema (ver o verbete).
    if "vantagem" in texto and "desvantagem" not in texto:
        return 2
    if any(t in texto for t in _CONDICAO_COMUM):
        return 1
    if re.search(r"recupera|cura\b|\+\d+|desvantagem|subtrai", texto):
        return 1
    return 0


def eixo_duracao(texto: str) -> int:
    """0 = instantâneo · 1 = dura rodadas · 2 = dura a cena, ou é permanente."""
    if re.search(
        r"fim da cena|durante a cena|pela cena|permanente|até ser dissipad"
        r"|até .{0,30}descanso|entre sessões|enquanto ele existir",
        texto,
    ):
        return 2
    # "\d+ rodadas" sem exigir o "por": a ficha escreve a duração de várias
    # formas ("**Duração:** 3 rodadas", "dura 3 rodadas"), e exigir a preposição
    # fazia 21 fichas serem medidas como instantâneas — 12 delas classificadas
    # abaixo do que entregam.
    if re.search(r"\d+ rodadas?|fim do próximo turno|fim do turno|próxima vez", texto):
        return 1
    return 0


def escala_de_poder(campos: dict[str, str], corpo: list[str]) -> str:
    """A Escala de Poder de uma habilidade geral, já com nome ("Notável").

    Uma ficha que declare `**Escala:**` vence a régua — é como a exceção se
    escreve, no mesmo arranjo do Cooldown. A régua acerta a maioria, mas erra
    de forma previsível onde a força da habilidade está na prosa e não em dado,
    área ou condição (*Forma Incorpórea*, *Céu Compartilhado*).
    """
    if declarada := texto_puro(campos.get("Escala", "")).strip():
        return declarada
    texto = _texto_de_eixo(corpo)
    eixos = sorted(
        (
            eixo_dano(texto),
            eixo_alcance(campos.get("Alvos", ""), texto),
            eixo_controle(texto),
            eixo_duracao(texto),
        ),
        reverse=True,
    )
    return ESCALA_POR_PESO[eixos[0] + eixos[1]]


def cooldown_derivado(escala_arma: str, campos: dict[str, str], escala: str = "",
                      acao: str = "") -> str:
    """O padrão de Cooldown: pelo grau, nas de arma; pelo Mana, nas gerais.

    Reação e Passiva ficam de fora — a Reação já é limitada pelo próprio
    gatilho (é o que `regras-de-habilidade.md#cooldown` diz), e a Passiva nunca
    é ativada. Sem esta guarda elas caíam na faixa de Mana como qualquer outra.

    As habilidades que pagam com **Vida** (as de Sangue, o Preço de Sangue) não
    têm Mana pra consultar — nelas o cooldown vem da Escala de Poder, que é a
    única medida de tamanho que sobra.
    """
    if acao in ("Reação", "Passiva"):
        return "—"
    if escala_arma in ESCALA_COOLDOWN:
        return ESCALA_COOLDOWN[escala_arma]
    teto = mana_maxima(campos)
    if teto is None:
        return COOLDOWN_POR_ESCALA.get(escala, "—")
    for limite, valor in COOLDOWN_POR_MANA:
        if teto <= limite:
            return valor
    return COOLDOWN_SUPREMO


def mana_maxima(campos: dict[str, str]) -> int | None:
    """O teto: a Mana da Intensidade mais cara (ou do Custo fixo).

    Espelha `mana_minima`, que lê o piso. O teto é o que precifica a
    habilidade — ver jogar/mana.md#faixas-de-mana.
    """
    if bruto := campos.get("Custo fixo"):
        txt = texto_puro(bruto).split("|")[0].strip()
        if m := re.search(r"(\d+)\s*Mana", txt):
            return int(m.group(1))
    manas = [
        int(m.group(1))
        for rotulo, valor in campos.items()
        if rotulo.startswith("Intensidade")
        if (m := re.search(r"(\d+)\s*Mana", rotulo + " " + valor))
    ]
    return max(manas) if manas else None


# Ficha resumida de cada habilidade, pro popover. Mesmo contrato do glossário:
# o `on_post_build` grava em assets/habilidades.json e o JS mostra ao passar o
# mouse num link que aponte pro card.
_POPOVER: dict[str, dict[str, str]] = {}

# Mesmo contrato, pro card de Equipamento: on_post_build grava em
# assets/equipamento.json. Sem isso, um link tipo "Broquel" só teria a rede
# genérica de página (assets/paginas.json), que não sabe nada sobre dado de
# dano ou bônus de Defesa — só o resumo em prosa que abre a listagem inteira.
_EQUIPAMENTO: dict[str, dict[str, str]] = {}


def resumo_para_popover(
    rotulos: list[str], custo: str, campos: dict[str, str], corpo: list[str]
) -> str:
    """Uma espiada, não a ficha: chaves, custo, alvo e o efeito da Intensidade I.

    Quem quer o resto clica — o card completo está a um clique, e repetir as
    três Intensidades aqui faria um popover do tamanho da tela.
    """
    linhas: list[str] = []
    if rotulos:
        linhas.append("<b>" + escapa(" · ".join(rotulos)) + "</b>")

    ficha = " · ".join(
        p
        for p in (
            custo,
            resume_atributo(campos.get("Atributo", "")),
            texto_puro(campos.get("Alvos", "")).split("|")[0].strip(),
        )
        if p
    )
    if ficha:
        linhas.append(escapa(ficha))

    # A primeira linha de efeito: a Intensidade I, ou o Custo fixo quando a
    # habilidade não tem degrau.
    for linha in corpo:
        if m := re.match(r"^-\s+\*\*(Intensidade I\b|Acerto|Efeito)[^:]*:\*\*\s*(.+)$", linha):
            linhas.append(html_do_verbete(m.group(2)))
            break

    return "<br>".join(linhas)


# Rótulos da ficha técnica, na ordem em que aparecem — ver
# habilidades/regras.md#ficha-de-habilidade. Todo campo aparece sempre, com
# "—" quando a habilidade ainda não o declara; o retrofit das 754 habilidades
# existentes é fase própria (ver CLAUDE.md), então "—" aqui é esperado até lá.
FICHA_TECNICA_ROTULOS = (
    # quando se usa e como rola
    "Ação", "Atributo", "Resolução", "Vs",
    # o que atinge, e o que faz
    "Alvos", "Alcance", "Área", "Dano", "Duração",
    # o que restringe
    "Componentes", "Cooldown",
)
# Concentração e Ritual saíram (2026-08-25). Eram campos que diziam "Não" nas
# 754 habilidades: regras importadas do D&D que o Prisma já resolve de outro
# jeito. Concentração existe lá porque um buff dura 10 rodadas ou uma hora;
# aqui dura 2–4, e o próprio prazo é o freio — somado ao Acúmulo de bônus, que
# já impede empilhar buff numérico. E Ritual ("sem Mana, 10 minutos, fora de
# combate") tornaria gratuita toda utilitária, porque fora de combate sempre se
# tem 10 minutos: o custo em Mana de uma Suprema de 48 viraria decoração.

# Os rótulos que a ficha técnica passa a mostrar não podem continuar no corpo
# do card: o bullet `- **Atributo:** … | **Alcance:** … | **Alvos:** …` dizia
# exatamente o que o bloco acima já diz, linha por linha. O que sobra da linha
# (Custo fixo, Requisito) fica — só os pares absorvidos saem.
ABSORVIDOS_PELA_FICHA = frozenset(
    FICHA_TECNICA_ROTULOS
) | {"Resolucao", "vs", "Area", "Duracao", "Concentracao", "Alvo"}


def limpa_campos_absorvidos(corpo: list[str]) -> list[str]:
    """Reescreve o corpo sem os pares que subiram pra ficha técnica.

    Linha que fica sem nenhum par é removida inteira; linha que mistura par
    absorvido com par próprio (`**Custo fixo:** … | **Atributo:** …`) é
    remontada só com o que sobrou.
    """
    saida: list[str] = []
    for linha in corpo:
        if not RE_CAMPO.match(linha):
            saida.append(linha)
            continue
        pares = RE_PAR.findall(linha)
        if not pares:
            saida.append(linha)
            continue
        restantes = [(r, v) for r, v in pares if r.strip() not in ABSORVIDOS_PELA_FICHA]
        if len(restantes) == len(pares):
            saida.append(linha)
        elif restantes:
            saida.append(
                "- " + " | ".join(f"**{r.strip()}:** {v.strip()}" for r, v in restantes)
            )
        # sem restantes: a linha inteira virou ficha técnica, não sobra nada
    return saida


# Alcance e Área quase nunca existem como campo próprio — mas o dado já está
# dentro de "Alvos", que toda ficha escreve ("1 criatura a até 8 casas",
# "2 casas de raio do ponto"). Derivar dali é o mesmo movimento de
# `elemento_do_campo_dano`: ler o que o markdown já diz, em vez de pedir que
# 754 fichas repitam a informação noutro lugar. Campo declarado sempre vence.
# Os padrões abaixo saíram de um levantamento dos 149 textos distintos de
# Alvos, não de suposição — o que não casa fica "—", que é honesto.
RE_RAIO = re.compile(r"(\d+)\s*casas?\s+de\s+raio")
RE_CONE = re.compile(r"cone\s+de\s+(\d+)\s*casas?")
RE_LINHA_N = re.compile(r"\blinha\s+de\s+(\d+)\s*casas?|(\d+)\s*casas?\s+em\s+linha")
RE_ATE_CASAS = re.compile(r"\ba\s+ate\s+(\d+)\s*casas?")


def _casas(n: str) -> str:
    return "1 casa" if n == "1" else f"{n} casas"


def area_derivada(alvos: str) -> str:
    """Forma e tamanho da área, lidos do campo Alvos.

    Plural fica de fora de propósito: "duas linhas de 5 casas" não casa com
    `linha de (\\d+)`, então cai em "—" em vez de virar "linha de 5 casas" e
    esconder que são duas.
    """
    txt = sem_acento(alvos)
    if m := RE_RAIO.search(txt):
        return f"raio de {_casas(m.group(1))}"
    if m := RE_CONE.search(txt):
        return f"cone de {_casas(m.group(1))}"
    if m := RE_LINHA_N.search(txt):
        return f"linha de {_casas(m.group(1) or m.group(2))}"
    if "na linha" in txt:
        return "linha"
    # Precisa do plural coletivo: "o atacante (precisa estar adjacente)" é
    # alvo único com uma condição, não uma área — procurar só por "adjacent"
    # transformava a condição entre parênteses em área (bug pego na auditoria).
    if re.search(r"(criaturas|inimigos|alvos|aliados)\s+adjacentes", txt):
        return "criaturas adjacentes"
    if "campo de batalha" in txt:
        return "campo de batalha"
    return ""


def alcance_declarado(campos: dict[str, str]) -> str:
    """O Alcance escrito na ficha — inclusive sob os rótulos variantes.

    Vinte e duas habilidades não dizem "Alcance:" e sim **"Alcance do salto:"**,
    **"do avanço:"** ou **"do recuo:"**, porque nelas quem se desloca é o
    usuário. É a mesma informação — quão longe a habilidade chega —, e ignorar
    o rótulo variante deixava a Queda Meteórica sem alcance mesmo tendo um
    escrito na própria ficha. A qualificação vai entre parênteses pra não se
    perder: "até o valor de Movimento (salto)".
    """
    for rotulo, valor in campos.items():
        if not rotulo.startswith("Alcance"):
            continue
        texto = texto_puro(valor).strip()
        if not texto:
            continue
        cauda = rotulo[len("Alcance"):].strip()
        if cauda.startswith("do "):
            return f"{texto} ({cauda[3:]})"
        return texto
    return ""


def alcance_derivado(
    alvos: str, campos: dict[str, str] | None = None, corpo: list[str] | None = None,
    grupo: str = "", arma: str = "",
) -> str:
    """A distância até o alvo.

    Sai do campo Alvos quando ele responde; quando não responde, a habilidade
    costuma responder de outro jeito. O caso maior é a técnica de arma: nela o
    alcance **é o da arma** — a mesma técnica com Espada é corpo a corpo e com
    Arco são 8 casas —, e "o da arma equipada" é a resposta certa, não uma
    lacuna. Cravar "corpo a corpo" ali estaria errado em 13 delas, que
    arremessam ou disparam.

    "Pessoal" cobre o que nasce no próprio usuário — a área centrada nele, o
    cone e a linha à frente —, onde o alcance é zero e o que importa é a área.
    """
    txt = sem_acento(alvos)
    if m := RE_ATE_CASAS.search(txt):
        return _casas(m.group(1))
    # "até 3 criaturas aliadas **em** 3 casas de raio" também declara distância.
    if m := re.search(r"\bem (\d+) casas? de raio", txt):
        return _casas(m.group(1))
    if "corpo a corpo" in txt:
        return "corpo a corpo"
    if "adjacent" in txt:
        return "adjacente"
    if any(
        marca in txt
        for marca in ("ao redor do usuario", "proprio usuario", "usuario e aliados")
    ):
        return "pessoal"
    # Cone e linha "à frente" partem de quem conjura: o alcance é zero, e o
    # comprimento já está no campo Área.
    if "cone de" in txt or "linha" in txt:
        return "pessoal"
    if "campo de batalha" in txt:
        return "campo de batalha"
    if "atacante" in txt or "criatura que sofreu dano" in txt:
        return "quem atacou"
    # A arma que o próprio usuário empunha está no corpo dele.
    if "arma equipada pelo usuario" in txt:
        return "pessoal"
    # Arrombar uma fechadura exige a mão nela.
    if "mecanismo" in txt:
        return "adjacente"

    campos = campos or {}
    corpo_txt = sem_acento(" ".join(corpo or []))
    dano = sem_acento(campos.get("Dano", ""))
    # Técnica de arma: a própria ficha às vezes já diz "ao alcance da arma".
    if (
        arma
        or grupo in ("marciais", "pontaria")
        or "arma equipada" in dano
        or "desarmado" in dano
        or "alcance da arma" in txt
    ):
        return "o da arma equipada"
    # Investida mágica: o usuário vai até o alvo antes de bater.
    if "se desloca ate" in corpo_txt or "investida" in corpo_txt:
        return "corpo a corpo"
    return ""


# A duração está escrita dentro das Intensidades ("por 3 rodadas"), não num
# campo próprio — e em 52 habilidades ela é justamente o eixo que escala
# (Bênção Divina: 3 → 4 → 5). Um número só mentiria; a faixa diz a verdade,
# no mesmo formato que o selo de Mana já usa ("3–18 Mana").
RE_DURACAO = re.compile(r"\bpor (\d+) rodadas?|\bdurante (\d+) rodadas?")


def duracao_derivada(campos: dict[str, str]) -> str:
    """A duração lida das Intensidades: número quando é fixa, faixa quando
    escala, e "Instantânea" quando não há duração nenhuma no texto.

    Instantânea não quer dizer "sem consequência": a condição que a habilidade
    aplica tem prazo próprio, definido no glossário. O que acaba na hora é a
    habilidade.
    """
    duracoes = [
        int(next(g for g in m.groups() if g))
        for rotulo, valor in campos.items()
        if rotulo.startswith("Intensidade")
        or rotulo in ("Acerto", "Efeito", "Custo fixo")
        if (m := RE_DURACAO.search(rotulo + " " + valor))
    ]
    if not duracoes:
        return "Instantânea"
    lo, hi = min(duracoes), max(duracoes)
    if lo == hi:
        return "1 rodada" if lo == 1 else f"{lo} rodadas"
    return f"{lo}–{hi} rodadas"


# Existe uma terceira forma de resolver, que a regra já reconhecia mas o campo
# não: nem Ataque nem Teste de Resistência — **nada é rolado**. Buff, cura e
# zona de dano automático caem aqui, e várias fichas já dizem isso em voz alta
# ("sem teste de ataque"). Só a marca explícita conta: "dano automático"
# sozinho não serve, porque aparece em habilidade que rola normalmente e só
# aplica o dano depois de acertar.
MARCAS_AUTOMATICA = ("sem teste de ataque", "sem rolagem", "sem teste de acerto")


def componentes_por_natureza(campos: dict[str, str]) -> str:
    """Componentes de Buff, Debuff e Suporte — os três grupos sem padrão.

    Eles misturam de propósito conjuração e técnica corporal ("imbuir elemento
    na arma" mora ao lado de "postura inabalável"), então o Grupo não decide.
    Quem decide é o **Atributo**, que já declara a natureza da habilidade:
    Magia é conjuração (fala + gesto), Ataque/Agilidade é o corpo (só gesto).

    O Material entra só quando a ficha *exige* o item — Requisito de escudo
    equipado, ou dano que usa a arma. Procurar a palavra "golpe" no texto não
    serve: em "desviando o golpe que viria" o golpe é do inimigo, não do
    usuário.
    """
    atributo = sem_acento(campos.get("Atributo", ""))
    if "magia" in atributo:
        return "V, S"
    requisito = sem_acento(campos.get("Requisito", ""))
    dano = sem_acento(campos.get("Dano", ""))
    if "equipad" in requisito or "arma equipada" in dano or "desarmado" in dano:
        return "S, M"
    return "S"


# Quem só mira o próprio usuário e aliados não tem contra quem rolar — a regra
# já dizia isso ("buffs, cura e efeitos automáticos não checam número-alvo"),
# mas o campo saía como Ataque vs Evasão, inventando uma rolagem inexistente.
# As marcas hostis derrubam a leitura: `1 criatura (o atacante)` é alvo hostil
# mesmo aparecendo numa Reação de defesa.
_MARCAS_HOSTIS = ("hostil", "inimig", "atacante", "morta-viva", "cadaver")
_MARCAS_AMIGAS = ("proprio usuario", "aliado", "o usuario e", "usuario e aliados")


def alvo_so_amigo(alvos: str) -> bool:
    txt = sem_acento(alvos)
    if not txt or any(h in txt for h in _MARCAS_HOSTIS):
        return False
    return any(a in txt for a in _MARCAS_AMIGAS)


def resolucao_automatica(campos: dict[str, str], corpo: list[str]) -> str:
    # A marca costuma estar no corpo, não num bullet de campo: é a linha solta
    # "*(Sem Intensidade — efeito de zona automático, sem teste de ataque)*".
    texto = sem_acento(" ".join(campos.values()) + " " + " ".join(corpo))
    if any(m in texto for m in MARCAS_AUTOMATICA):
        return "Automática"
    return "Automática" if alvo_so_amigo(campos.get("Alvos", "")) else ""


def ficha_tecnica_valores(
    campos: dict[str, str], grupo: str, escala: str, corpo: list[str],
    qualificador: str = "", arma: str = "",
) -> dict[str, str]:
    """Um valor por campo da ficha técnica — nunca vazio.

    Nenhum campo cai em "—" por falta de fonte: Resolução, Vs, Componentes e
    Cooldown têm padrão vindo da própria regra (Ataque, Evasão, Grupo, Escala);
    Alcance e Área saem do campo Alvos; Duração sai das Intensidades. O "—"
    sobra só onde o texto realmente não responde — Alcance de "1 criatura", por
    exemplo, que depende da arma equipada.
    """
    vs_bruto = campos.get("Vs", campos.get("vs", ""))
    alvos = campos.get("Alvos", "")
    resolucao = (
        texto_puro(campos.get("Resolução", campos.get("Resolucao", "")))
        or resolucao_automatica(campos, corpo)
        or "Ataque"
    )
    vs = texto_puro(vs_bruto).split("|")[0].strip() or "Evasão"
    # Efeito automático não compara com número nenhum — dizer "Evasão" ali
    # inventaria uma rolagem que a habilidade declara não existir.
    if resolucao == "Automática":
        vs = "—"
    # Num Teste de Resistência o número-alvo troca de lado: não é a defesa do
    # alvo que o usuário precisa superar, é a Fortitude do usuário que o alvo
    # precisa superar. Sem dizer de quem é, o mesmo rótulo significaria duas
    # coisas opostas conforme a Resolução.
    if resolucao.startswith("Teste de Resist") and "do usuário" not in vs:
        vs = f"{vs} do usuário"

    # Quando a habilidade entra em jogo. Reação e Passiva vinham só como chip
    # no cabeçalho, mas mudam *como se usa* — a Reação sai fora do turno e
    # custa 0 PA, a Passiva nunca é ativada —, então são ficha, não etiqueta.
    qualif = sem_acento(qualificador)
    acao = "Reação" if qualif == "reacao" else "Passiva" if qualif == "passiva" else "Ação"
    if acao == "Passiva":
        # Passiva não resolve nada: está sempre ligada, não há rolagem nem
        # número-alvo. Dizer "Ataque vs Evasão" aqui seria inventar um teste.
        resolucao, vs = "—", "—"
    return {
        "Ação": acao,
        # Atributo, Alvos e Dano vêm crus (não por texto_puro) porque carregam
        # links que valem: `**Dano:** usa o [Dano Desarmado](…)` perderia o
        # link, e é justamente o que o leitor quer clicar. O valor é renderizado
        # como markdown no HTML da ficha.
        "Atributo": campos.get("Atributo", "").strip() or "—",
        "Resolução": resolucao,
        "Vs": vs,
        "Alvos": alvos.strip() or "—",
        "Dano": campos.get("Dano", "").strip() or "—",
        "Alcance": (
            alcance_declarado(campos)
            or alcance_derivado(alvos, campos, corpo, grupo, arma)
            or "—"
        ),
        "Área": (
            texto_puro(campos.get("Área", campos.get("Area", "")))
            or area_derivada(alvos)
            or "—"
        ),
        # Passiva é o oposto de instantânea: vale desde que foi aprendida e não
        # expira. O fallback "Instantânea" (que serve pra quem não tem duração
        # no texto) diria exatamente o contrário do que ela é.
        "Duração": (
            texto_puro(campos.get("Duração", campos.get("Duracao", "")))
            or ("Permanente" if acao == "Passiva" else duracao_derivada(campos))
        ),
        # Passiva não se ativa — está sempre ligada —, então não exige fala,
        # gesto nem item em grupo nenhum. Por isso vem antes do padrão do Grupo.
        "Componentes": (
            texto_puro(campos.get("Componentes", ""))
            or ("—" if sem_acento(qualificador) == "passiva" else "")
            or GRUPO_COMPONENTES.get(grupo, "")
            or componentes_por_natureza(campos)
        ),
        "Cooldown": texto_puro(campos.get("Cooldown", ""))
        or cooldown_derivado(escala, campos, escala, acao),
    }


def ficha_tecnica_html(
    campos: dict[str, str], grupo: str, escala: str, corpo: list[str],
    qualificador: str = "", arma: str = "",
) -> str:
    """A ficha técnica do card.

    A classe é `prg-tecnica`, e **não** `prg-ficha`: essa última já pertence à
    ficha de personagem imprimível (`assets/css/ficha.css`, carregado em todas
    as páginas). Usá-la aqui fazia o card herdar a tinta de papel (#211c14)
    sobre fundo escuro — e, pior, `body:has(.prg-ficha)` no `@media print`
    daquele arquivo mandava a listagem inteira imprimir sem header nem nav.
    """
    valores = ficha_tecnica_valores(campos, grupo, escala, corpo, qualificador, arma)
    # markdown="span" em vez de escapa(): Atributo, Alvos e Dano trazem links
    # (`usa o [Dano Desarmado](…)`) que o leitor quer clicar, e escapar mataria
    # os dois. Quem não tem markdown atravessa igual.
    campos_html = "".join(
        f'<span class="prg-tecnica__campo" data-rot="{rotulo}">'
        f'<span class="prg-tecnica__valor'
        f'{" prg-tecnica__valor--vazio" if valores[rotulo] == "—" else ""}"'
        f' markdown="span">{valores[rotulo]}</span></span>'
        for rotulo in FICHA_TECNICA_ROTULOS
    )
    # markdown="span", nunca "block": com "block" o Markdown envolve tudo num
    # <p>, o flex passa a ter um filho só e o `gap` deixa de separar os campos
    # — eles saem grudados ("MagiaRESOLUÇÃOAtaque").
    return f'<div class="prg-tecnica" markdown="span">{campos_html}</div>'


# ------------------------------------------------- facetas da ficha técnica
#
# Os campos da ficha viram filtro, mas nem todos servem crus: Alcance tem 28
# valores distintos, e um menu com 28 linhas não se lê. O que vira faceta é a
# **pergunta** que o jogador faz — "dá pra usar de longe?", "isso pega área?"
# —, não o valor exato, que continua no card.

RE_CASAS_NUM = re.compile(r"^(\d+)\s*casas?")


def faixa_de_alcance(valor: str) -> tuple[str, str]:
    """(chave, rótulo) da faixa de alcance, ou ("", "") pra quem não tem."""
    txt = sem_acento(valor)
    if not txt or txt == "—":
        return "", ""
    if txt == "pessoal":
        return "pessoal", "Pessoal"
    if "corpo a corpo" in txt or "adjacente" in txt:
        return "corpo-a-corpo", "Corpo a corpo"
    if "arma equipada" in txt:
        return "arma", "O da arma equipada"
    if m := RE_CASAS_NUM.search(txt.replace("linha de ", "")):
        n = int(m.group(1))
        if n <= 4:
            return "curto", "Curto (até 4 casas)"
        if n <= 7:
            return "medio", "Médio (5–7 casas)"
        return "longo", "Longo (8+ casas)"
    # Sem limite, conversa direta, o círculo do ritual, vínculo, campo de
    # batalha, "até o valor de Movimento" — alcance que não se mede em casas.
    return "especial", "Sem medida em casas"


FORMAS_DE_AREA = (
    ("raio", "raio", "Raio"),
    ("cone", "cone", "Cone"),
    ("linha", "linha", "Linha"),
    ("criaturas adjacentes", "adjacentes", "Adjacentes"),
    ("campo de batalha", "campo", "Campo de batalha"),
)


def forma_de_area(valor: str) -> tuple[str, str]:
    txt = sem_acento(valor)
    for marca, chave, rotulo in FORMAS_DE_AREA:
        if txt.startswith(marca) or txt == marca:
            return chave, rotulo
    return "", ""


def facetas_de_componentes(valor: str) -> tuple[str, str]:
    """Multivalor V/S/M — mais "Sem Verbal", que é a pergunta de quem está
    [Silenciado]: "o que eu ainda consigo usar?". Sem esse valor derivado o
    filtro só responderia o inverso do que se precisa saber."""
    txt = valor.strip()
    if not txt or txt == "—":
        return "", ""
    pares = []
    if "V" in txt:
        pares.append(("verbal", "Verbal"))
    else:
        pares.append(("sem-verbal", "Sem Verbal (dá pra usar Silenciado)"))
    if "S" in txt:
        pares.append(("somatico", "Somático"))
    if "M" in txt:
        pares.append(("material", "Material"))
    return " ".join(p[0] for p in pares), "|".join(p[1] for p in pares)


def chip(rotulo: str, familia: str = "") -> str:
    """Um chip colorido no cabeçalho do card."""
    classe = f"prg-chip--{familia}-{slug(rotulo)}" if familia else f"prg-chip--{classe_chip(rotulo)}"
    return f'<span class="prg-chip {classe}">{escapa(rotulo)}</span>'


def valor_de_coluna(valor: str) -> str:
    """Encurta um valor pro cabeçalho, que é linha de varredura, não ficha.

    Mesmo princípio do `valor_de_tile` no Bestiário: o que vem depois do
    travessão é explicação, e explicação não cabe onde se lê de relance. O
    Golpe Final declara "Alcance do recuo: até o valor de Movimento do
    personagem, em casas — o usuário se desloca pra trás, saindo da área
    afetada", e sem este corte a frase inteira ia parar no cabeçalho,
    empurrando o card pra 145px de altura. A ficha, ao abrir, segue completa.
    """
    return valor.split(" — ")[0].strip().rstrip(",")


def colunas_html(pares: Iterable[tuple[str, str]]) -> str:
    """As colunas do cabeçalho colapsado: rótulo (via CSS) + valor.

    O valor vive num `<span>` próprio: quando ele mistura texto solto com um
    link (ex: "...imune a [Atordoado](...)"), cada trecho de texto e cada
    link viram itens de flex separados se ficarem soltos direto dentro do
    `.prg-card__col` (que é flex) — o navegador os organiza em colunas lado a
    lado em vez de deixar o texto fluir, e a palavra do link quebra letra por
    letra tentando caber. Um span só em volta do valor inteiro vira um único
    item de flex, e o texto quebra normalmente nos espaços.
    """
    return "".join(
        f'<span class="prg-card__col" data-rot="{rotulo}">'
        f'<span class="prg-card__col-valor">{escapa(valor)}</span></span>'
        for rotulo, valor in pares
        if valor
    )


def indice_de_busca(*pedacos: str) -> str:
    """Tudo o que a busca livre precisa achar, normalizado sem acento."""
    return escapa(sem_acento(" ".join(" ".join(pedacos).split())))


def facetas_html(pares: dict[str, str]) -> str:
    return " ".join(f'data-{nome}="{escapa(valor)}"' for nome, valor in pares.items())


def monta_card_base(
    ident: str,
    nome: str,
    corpo_md: str,
    *,
    chips: str = "",
    selo: str = "",
    colunas: str = "",
    facetas: str = "",
    busca: str = "",
    classe: str = "",
    classe_selo: str = "",
) -> str:
    """A carcaça compartilhada por todos os cards do site.

    Habilidade, pacote, raça, origem, equipamento e criatura têm conteúdos
    completamente diferentes, mas o comportamento de leitura é o mesmo — abre,
    fecha, filtra, responde a link direto —, então a casca é uma só. Quem chama
    decide o que vira chip, coluna, selo e faceta.
    """
    extra = f" {classe}" if classe else ""
    selo_extra = f" {classe_selo}" if classe_selo else ""
    return (
        # markdown="block" no container: sem ele, o md_in_html trata o card
        # inteiro como HTML cru e a ficha nunca vira markdown.
        f'<div class="prg-card{extra}" id="{ident}" data-busca="{busca}" '
        f'{facetas} markdown="block">\n'
        f'<button class="prg-card__hd" type="button" aria-expanded="false" '
        f'aria-controls="{ident}-bd">\n'
        f'<span class="prg-card__nome">{escapa(nome)}</span>\n'
        f'<span class="prg-card__chips">{chips}</span>\n'
        f'<span class="prg-card__custo{selo_extra}">{escapa(selo)}</span>\n'
        f'<span class="prg-card__seta" aria-hidden="true"></span>\n'
        f'<span class="prg-card__cols">{colunas}</span>\n'
        f"</button>\n"
        f'<div class="prg-card__bd" id="{ident}-bd" markdown="1">\n\n'
        f"{corpo_md.strip()}\n\n"
        f"</div>\n"
        f"</div>\n"
    )


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

    # Grau de arma e Escala de Poder são coisas diferentes e convivem: o grau é
    # a ordem de aprendizado dentro da arma, a Escala é o tamanho do efeito.
    # Quem decide qual das duas se aplica é `arma`, não a palavra — catorze
    # habilidades **gerais** trazem "Especial" na Chave sem serem de arma, e
    # ler a palavra solta as classificava como se fossem.
    escala = sem_acento(qualificador) if arma else ""
    if arma and escala not in _GRAUS_ARMA:
        escala = next(
            (r for r in (sem_acento(x) for x in rotulos) if r in _GRAUS_ARMA), ""
        )
    # Passiva e Reação ficam fora da Escala de Poder de propósito: a primeira
    # não se ativa e a segunda sai fora do turno, então "quanto ela entrega
    # quando você gasta o turno nela" não é uma pergunta que caiba nelas.
    if not escala and sem_acento(qualificador) not in ("passiva", "reacao"):
        escala = sem_acento(escala_de_poder(campos, corpo))

    escala_nome = (
        ESCALA_POR_PESO[_ESCALA_GERAL.index(escala)]
        if escala in _ESCALA_GERAL
        else escala.capitalize().replace("Basica", "Básica").replace("Avancada", "Avançada")
        if escala
        else ""
    )

    # O rótulo do qualificador vira chip — menos quando é vocabulário
    # aposentado, que passou a ser calculado e não mais escrito.
    if qualificador and qualificador not in rotulos:
        if sem_acento(qualificador) not in _ESCALA_APOSENTADA:
            rotulos.append(qualificador)
    # A Escala derivada entra como chip próprio, do mesmo jeito que o grau de
    # arma já entrava — é o que o leitor compara ao varrer a lista.
    if escala in _ESCALA_GERAL:
        rotulos = [r for r in rotulos if sem_acento(r) not in _ESCALA_VALIDOS]
        rotulos.append(ESCALA_POR_PESO[_ESCALA_GERAL.index(escala)])

    chips = "".join(chip(r) for r in rotulos if r)

    # O custo sai na primeira faixa, alinhado entre todos os cards: é o número
    # que o jogador compara ao varrer a lista. O resto vai na faixa de baixo.
    valores_busca = [nome]
    custo = custo_resumido(campos)
    if custo:
        valores_busca.append(custo)

    mana_min = mana_minima(campos)
    elemento = elemento or elemento_do_campo_dano(campos)

    # A ficha técnica é calculada antes do cabeçalho porque ele lê dela: o
    # Alcance de 82% das habilidades e o Cooldown de quase todas são
    # **derivados**, não escritos no markdown — ler `campos` aqui deixaria as
    # duas colunas vazias justamente nos cards que mais precisam delas.
    ficha = ficha_tecnica_valores(campos, grupo, escala, corpo, qualificador, arma)

    pares_coluna: list[tuple[str, str]] = []
    for rotulo in COLUNAS:
        if rotulo in ("Chave", "Custo"):
            continue
        valor = ficha.get(rotulo, "")
        if rotulo == "Atributo":
            valor = resume_atributo(campos.get(rotulo, ""))
        valor = valor_de_coluna(texto_puro(valor).split("|")[0])
        # "—" é resposta honesta dentro do card aberto, mas no cabeçalho seria
        # uma coluna de nada ocupando espaço na varredura da lista.
        if not valor or valor == "—":
            continue
        valores_busca.append(valor)
        pares_coluna.append((rotulo, valor))

    valores_busca.extend(rotulos)

    detalhe = "\n".join(corpo).strip()

    # A ficha inteira entra no índice: procurar por "sangrando" ou "atordoado"
    # e ver quais habilidades aplicam aquilo é o filtro que mais importa.
    valores_busca.append(flavor)
    valores_busca.append(texto_puro(detalhe))

    # A ficha resumida pro popover: o que o leitor precisa pra decidir se vale
    # abrir o card. Custo e alvo vêm do cabeçalho; o resto é a primeira linha
    # de efeito, que já diz o que a habilidade faz.
    _POPOVER[ident] = {
        "titulo": nome,
        "corpo": resumo_para_popover(rotulos, custo, campos, corpo),
    }

    ficha_tecnica = ficha_tecnica_html(campos, grupo, escala, corpo, qualificador, arma)

    # A ficha técnica alimenta o filtro: os mesmos valores que o card mostra,
    # reduzidos à pergunta que o jogador faz na mesa.
    alc_chave, alc_nome = faixa_de_alcance(ficha["Alcance"])
    area_chave, area_nome = forma_de_area(ficha["Área"])
    comp_chaves, comp_nomes = facetas_de_componentes(ficha["Componentes"])
    cooldown = "" if ficha["Cooldown"] == "—" else slug(ficha["Cooldown"])
    resolucao = "" if ficha["Resolução"] == "—" else slug(ficha["Resolução"])
    # O corpo perde os pares que a ficha técnica assumiu: sem isto o card diz
    # Atributo, Alcance e Alvos duas vezes, uma no bloco e outra no bullet.
    detalhe = "\n".join(limpa_campos_absorvidos(corpo)).strip()

    return monta_card_base(
        ident,
        nome,
        f"{'*' + flavor + '*' if flavor else ''}\n\n{ficha_tecnica}\n\n{detalhe}",
        chips=chips,
        selo=custo,
        colunas=colunas_html(pares_coluna),
        busca=indice_de_busca(*valores_busca),
        facetas=facetas_html(
            {
                "grupo": grupo,
                "arma": arma,
                "arma-nome": arma_nome,
                "escala": escala,
                # O rótulo bonito: sem ele o menu mostraria o slug cru
                # ("notavel", "suprema") ao lado de "Básica" e "Menor", que
                # por coincidência já se escrevem sem acento.
                "escala-nome": escala_nome,
                "elemento": elemento,
                "atributos": " ".join(computa_atributos(campos.get("Atributo", ""))),
                "mana-min": str(mana_min) if mana_min is not None else "",
                "alvo": computa_alvo_categoria(campos, corpo),
                "desarmado": "1" if computa_desarmado(campos, corpo) else "",
                "acao": slug(ficha["Ação"]),
                "acao-nome": ficha["Ação"],
                "resolucao": resolucao,
                "resolucao-nome": ficha["Resolução"] if resolucao else "",
                "alcance": alc_chave,
                "alcance-nome": alc_nome,
                "area": area_chave,
                "area-nome": area_nome,
                "cooldown": cooldown,
                "cooldown-nome": ficha["Cooldown"] if cooldown else "",
                "componentes": comp_chaves,
                "componentes-nome": comp_nomes,
            }
        ),
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


# Uma página de regra pede verbetes inteiros do glossário assim:
#
#     <!-- prisma:verbetes Vantagem Desvantagem -->
#
# "Role 2d20 e use o melhor" estava escrito em três lugares — glossário,
# Testes de d20 e Testes e Dificuldades — já com três redações diferentes
# ("maior/menor" contra "melhor/pior"). Uma fonte, várias vistas.
RE_PEDE_VERBETES = re.compile(r"^<!--\s*prisma:verbetes\s+(.+?)\s*-->\s*$", re.M)


def puxa_verbetes(docs_dir: Path, nomes: list[str], caminho: str) -> list[str]:
    verbetes = {
        v.termo: v
        for v in extrai_verbetes(
            (docs_dir / "glossario.md").read_text(encoding="utf-8")
        )
    }
    subida = "../" * caminho.count("/")
    partes: list[str] = []
    for nome in nomes:
        if v := verbetes.get(nome):
            # O próprio termo linka pro verbete: não dá pra contar com o
            # auto-link, que só passa nas páginas de prosa.
            titulo = f"**[{v.termo}]({subida}glossario.md#{v.ancora})**"
            partes.extend([f"{titulo} — " + "\n".join(v.corpo).strip(), ""])

    # O glossário mora na raiz de docs/; os links dentro do verbete precisam
    # subir tantos níveis quantos a página que está citando.
    for _ in range(caminho.count("/")):
        partes = reancora_um_nivel(partes)
    return religa_ancoras(partes, set())


def resolve_pedidos_de_verbete(markdown: str, caminho: str, docs_dir: Path) -> str:
    def troca(m: re.Match) -> str:
        nomes = m.group(1).split()
        return "\n".join(puxa_verbetes(docs_dir, nomes, caminho)).rstrip()

    return RE_PEDE_VERBETES.sub(troca, markdown)


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


# ------------------------------------------------------- seções `## Nome`
#
# Raças, criaturas e armas usam todas a mesma forma no markdown: uma seção
# `## Nome`, um flavor em itálico, e o corpo. Quem varre é a mesma função; o
# que muda é só o que cada listagem faz com o corpo.


class Secao(NamedTuple):
    nome: str
    corpo: list[str]
    familia: str  # o último `## ` sem corpo próprio, quando a página agrupa


def extrai_secoes(
    linhas: list[str], divisorias: frozenset[str] = frozenset()
) -> list[Secao]:
    """Cada `## Nome` vira uma seção, exceto as divisórias declaradas.

    Uma divisória (`## Raças de Animal`) não é conteúdo: é o rótulo da leva que
    vem depois dela, e vira o campo `familia` das seções seguintes.
    """
    secoes: list[Secao] = []
    atual: str | None = None
    familia = ""
    buffer: list[str] = []

    def grava() -> None:
        if atual:
            secoes.append(Secao(atual, list(buffer), familia))

    for linha in linhas:
        if linha.startswith("## "):
            grava()
            nome = linha[3:].strip()
            buffer = []
            if nome in divisorias:
                familia, atual = nome, None
            else:
                atual = nome
        elif atual is not None:
            buffer.append(linha)
    grava()
    return secoes


def flavor_e_resto(corpo: list[str]) -> tuple[str, list[str]]:
    """O primeiro parágrafo em itálico é o flavor; o resto é a ficha."""
    for i, linha in enumerate(corpo):
        if not linha.strip():
            continue
        if RE_FLAVOR.match(linha.strip()):
            return linha.strip().strip("*"), corpo[i + 1 :]
        return "", corpo[i:]
    return "", []


def campos_do_bloco(corpo: list[str]) -> dict[str, str]:
    """Junta os pares rótulo/valor dos bullets de ficha do topo do bloco."""
    campos: dict[str, str] = {}
    for linha in corpo:
        if not linha.startswith("- **"):
            if campos and linha.strip():
                break  # a ficha acabou; o que vem depois é ataque ou traço
            continue
        campos.update(campos_da_linha(linha))
    return campos


# --------------------------------------------------------------- bestiário

# O Tier é o eixo do Bestiário: dele saem Vida, PA, Ataque e a forma de jogar
# a criatura. Vira chip colorido e faceta.
TIERS = ("Comum", "Treinado", "Formidável", "Lendário")

# A ficha da criatura é lida no molde do stat block do D&D Beyond, em quatro
# camadas: os números que o Mestre consulta a cada rodada, os oito atributos
# numa grade fixa (sempre no mesmo lugar, mesmo valendo +0), o que muda a
# resolução do dano, e só então traços e ações — cada uma em uma linha só.
DESTAQUES_CRIATURA = (
    "Ameaça",
    "Vida",
    "Mana",
    "PA",
    "Evasão",
    "Crítico",
    "Iniciativa",
    "Movimento",
    "Voo",
)
# Vida e Mana ficam lado a lado de propósito (d100, 2026-08-20) — os dois
# recursos "grandes" da ficha, pra comparar num olhar só. Ver cor em
# TILE_COR_ESPECIAL, mais abaixo.
TILE_COR_ESPECIAL = {"Vida": "vida", "Mana": "mana"}
# "Defesa mental" saiu dos tiles (d100, 2026-08-20): não é mais um número
# único computado — é o valor cru de Magia/Social/Sanidade/Exploração,
# dependendo do efeito, e esses já aparecem na grade de atributos. Repetir
# um deles como tile faria parecer que só ele importa.
# "Ataque" também saiu do tile de cabeçalho (mesma data): é só mais um dos
# 8 atributos agora, e já aparece na grade — deixá-lo nos dois lugares
# mostrava o mesmo número duas vezes.

# Rótulos que não entram nas linhas de defesa: os que já viraram tile ou grade,
# mais os dois que a ficha não mostra. O Tier já é o chip do cabeçalho, e a
# Couraça já está somada na Evasão — mostrá-la de novo, em tile ou em
# legenda, faz parecer que são dois números. Ela continua no markdown e no
# filtro da barra; quem precisar do valor cru consulta Criando uma Criatura.
# O que sobrar (Imunidades, Resistência, Vulnerabilidade, e qualquer rótulo
# novo que uma criatura futura invente) cai nas linhas de defesa sozinho.
IGNORA_CRIATURA = frozenset(DESTAQUES_CRIATURA) | {"Tier", "Atributos", "Couraça", "Ataque"}
# "Ataque" some do tile de topo mas continua fora das linhas de defesa: o
# valor dele já vira parte da grade (ver ficha_de_criatura), então deixá-lo
# cair aqui embaixo também repetiria o número pela terceira vez.

ABREVIA_ATRIBUTO = {
    "ataque": "ATA",
    "defesa": "DEF",
    "agilidade": "AGI",
    "magia": "MAG",
    "exploracao": "EXP",
    "social": "SOC",
    "sorte": "SOR",
    "sanidade": "SAN",
}

# Um ataque ou traço: a linha é só o nome em negrito, seguido do qualificador
# `*(passiva)*` ou da meta do ataque (`— ◈ | +1 vs Evasão | alvo`).
RE_BLOCO_CRIATURA = re.compile(r"^\*\*([^*]+?)\*\*\s*(\*\([^)]+\)\*|—\s*\S.*)?$")

# Um tile só usa o número grande quando o valor é mesmo um número: um valor que
# só se diz em palavras precisa de corpo de texto pra caber.
RE_VALOR_NUMERICO = re.compile(r"^[+\-−–≤]?[\d◈()\s+/]+$")


def valor_de_tile(valor: str) -> str:
    """Encurta o valor até o que o rótulo do tile ainda não disse.

    O tile é uma faixa de comparação: quanto mais parecidos os valores, mais
    rápido se varre a linha. Então cai fora tudo o que é redundante com o
    rótulo — a unidade ("8 casas" sob MOVIMENTO), a contagem repetida
    ("◈◈ (2)" sob PA, onde os losangos já são a contagem) e a qualificação
    ("imune a efeito mental" sob DEFESA MENTAL). O texto inteiro continua no
    markdown e nas linhas de defesa, que é onde ele se lê por extenso.
    """
    valor = re.sub(r"\s*\(\d+\)$", "", valor)
    valor = re.sub(r"^(\d+)\s+casas?$", r"\1", valor)
    if re.match(r"(?i)^imune\b", valor):
        return "imune"
    return valor


def separa_criatura(
    resto: list[str],
) -> tuple[dict[str, str], list[str], list[tuple[str, str, list[str]]]]:
    """Divide o corpo da criatura em ficha, notas de prosa e blocos.

    Cada bloco é (nome, meta, corpo) — um ataque ou um traço passivo. O que vem
    solto antes do primeiro bloco e não é bullet de ficha é nota: existe em duas
    criaturas (o aviso de chefe do Dragão, o porquê da Defesa 4 do Slime) e é
    texto que o Mestre precisa ler.
    """
    campos: dict[str, str] = {}
    notas: list[str] = []
    blocos: list[tuple[str, str, list[str]]] = []
    atual: list[str] | None = None

    for linha in resto:
        texto = linha.strip()
        if not texto:
            continue
        if m := RE_BLOCO_CRIATURA.match(texto):
            corpo: list[str] = []
            blocos.append((m.group(1).strip(), (m.group(2) or "").strip(), corpo))
            atual = corpo
        elif atual is not None:
            atual.append(texto)
        elif texto.startswith("- **") and ":**" in texto:
            campos.update(campos_da_linha(texto))
        else:
            notas.append(texto)
    return campos, notas, blocos


def tiles_criatura(campos: dict[str, str]) -> tuple[str, list[str]]:
    """Os números de rodada em destaque; devolve (html, notas de rodapé).

    Quando o valor traz um comentário depois do travessão ("5 casas — mais
    rápido que a maioria dos personagens"), o número fica no tile e o comentário
    vira nota: o tile precisa ser varrido de olho, o comentário precisa ser lido.
    """
    tiles: list[str] = []
    notas: list[str] = []
    for rotulo in DESTAQUES_CRIATURA:
        bruto = campos.get(rotulo, "")
        if not bruto:
            continue
        valor, _, cauda = texto_puro(bruto).partition("—")
        valor = valor.strip().rstrip(",")
        if not valor:
            continue
        if cauda.strip():
            notas.append(f"**{rotulo}** — {cauda.strip()}")
        valor = valor_de_tile(valor)
        if set(valor) == {"◈"}:
            # Cinco losangos num tile de número ficam maiores que qualquer
            # outro valor da faixa: o PA desenha, não conta.
            classe = " prg-bes__val--pa"
        elif RE_VALOR_NUMERICO.match(valor):
            classe = ""
        else:
            classe = " prg-bes__val--texto"
        cor = TILE_COR_ESPECIAL.get(rotulo, "")
        classe_tile = f" prg-bes__tile--{cor}" if cor else ""
        tiles.append(
            f'<span class="prg-bes__tile{classe_tile}">'
            f'<span class="prg-bes__rot">{escapa(rotulo)}</span>'
            f'<span class="prg-bes__val{classe}">{escapa(valor)}</span></span>'
        )
    if not tiles:
        return "", notas
    return '<div class="prg-bes__tiles">' + "".join(tiles) + "</div>", notas


def grade_de_atributos(bruto: str) -> str:
    """Os oito atributos, sempre todos, sempre na mesma ordem.

    A ficha no markdown só cita o que foge de zero; a grade completa o resto com
    +0 — como o bloco de FOR/DES/CON do D&D Beyond, onde a posição é o que
    permite comparar duas criaturas sem reler rótulo.
    """
    texto = sem_acento(texto_puro(bruto))
    celulas: list[str] = []
    for chave, nome in ATRIBUTOS_TODOS:
        m = re.search(chave + r"\s*([+\-−–]?\s*\d+)", texto)
        valor = re.sub(r"\s+", "", m.group(1)).replace("−", "-").replace("–", "-") if m else "0"
        if not valor.startswith("-"):
            valor = "+" + valor.lstrip("+")
        zero = " prg-bes__atr--zero" if valor == "+0" else ""
        celulas.append(
            f'<span class="prg-bes__atr{zero}" title="{escapa(nome)}">'
            f'<span class="prg-bes__rot">{ABREVIA_ATRIBUTO[chave]}</span>'
            f'<span class="prg-bes__val">{valor}</span></span>'
        )
    return '<div class="prg-bes__atrs">' + "".join(celulas) + "</div>"


def linha_de_bloco(nome: str, meta: str, corpo: list[str]) -> str:
    """Um ataque ou traço numa linha só: nome em negrito, meta, efeito.

    O formato antigo gastava duas linhas — título e um bullet solto abaixo — pra
    dizer uma frase. Quando o bloco tem mais de um bullet (as três Intensidades
    da Baforada), a lista continua embaixo: aí ela é escolha, não detalhe.
    """
    passiva = meta.startswith("*(")
    cabeca = f"**{nome}.**"
    if passiva:
        cabeca += f' <span class="prg-bes__marca">({escapa(meta.strip("*()").strip())})</span>'
    elif meta:
        partes = [p.strip() for p in meta.lstrip("—").split("|") if p.strip()]
        cabeca += ' <span class="prg-bes__meta">' + " · ".join(partes) + "</span>"

    bullets = [l for l in corpo if l.startswith("- ")]
    prosa = [l for l in corpo if not l.startswith("- ")]

    # Um bullet só é a frase do efeito: sobe pra linha do nome. O travessão
    # separa a etiqueta (quanto custa, contra o quê, em quem) do que acontece.
    if len(bullets) == 1 and not prosa:
        cabeca += (" — " if meta and not passiva else " ") + bullets[0][2:].strip()
        bullets = []

    partes_md = [cabeca, *prosa]
    corpo_md = "\n\n".join(partes_md) + ("\n\n" + "\n".join(bullets) if bullets else "")
    classe = "prg-bes__bloco" + (" prg-bes__bloco--passiva" if passiva else "")
    return f'<div class="{classe}" markdown="1">\n\n{corpo_md}\n\n</div>'


def regra_da_acao_de_lenda(docs_dir: Path) -> str:
    """A Ação de Lenda, lida da regra — pra injetar em todo card Lendário.

    Ela é regra do Tier, então mora uma vez só em `criando-criaturas.md`. Mas é
    uma ação a mais por rodada, fora do turno: o Mestre precisa dela **no meio
    do turno**, e o que o card mostra não é decidido por de onde o número veio
    (a Vida e o PA também vêm do Tier) e sim por isso. Mesmo arranjo do traço de
    leva das Raças: uma cópia no markdown, injetada nos cards.

    Só a primeira frase entra — o resto do parágrafo explica por que a regra
    existe, e explicação não entra em ficha. E cai fora o escopo antes do
    dois-pontos ("Exclusiva do Tier Lendário:"), porque o chip do card já diz
    o Tier. Se o texto mudar de forma e a extração falhar, o card fica como
    estava.
    """
    arquivo = docs_dir / "mestre" / "criando-criaturas.md"
    if not arquivo.is_file():
        return ""
    linhas = arquivo.read_text(encoding="utf-8").split("\n")
    corpo = extrai_intervalo(linhas, r"^### Ação de Lenda\s*$", r"^#{2,4} ")
    for linha in corpo[1:]:
        if not linha.strip():
            continue
        frase = linha.strip().split(". ")[0].rstrip(".")
        if ": " in frase:
            frase = frase.split(": ", 1)[1]
        # A primeira letra, não o primeiro caractere: cortado o escopo, a frase
        # costuma começar com o `**` do negrito.
        frase = re.sub(r"[a-zà-ÿ]", lambda m: m.group(0).upper(), frase, count=1)
        return frase + "."
    return ""


def limiar_de_critico(campos: dict[str, str]) -> str:
    """`Sorte ÷ 3` — o d100 puro precisa cair igual ou abaixo disso pra criticar.

    **Derivado, nunca escrito na ficha.** A Sorte já está na linha de Atributos
    de toda criatura, então o tile sai sozinho no build e não dessincroniza
    quando a Sorte de uma delas mudar. Vale nos dois sentidos: no ataque da
    criatura e na resistência dela contra uma área (ver
    [Teste de Resistência](jogar/testes.md#teste-de-resistencia)).
    """
    achado = re.search(r"Sorte\s*\+?(\d+)", texto_puro(campos.get("Atributos", "")))
    return f"≤{int(achado.group(1)) // 3}" if achado else ""


def ficha_de_criatura(
    flavor: str, resto: list[str], acao_de_lenda: str = ""
) -> tuple[str, dict[str, str]]:
    """O corpo do card inteiro, no molde do stat block."""
    campos, notas_prosa, blocos = separa_criatura(resto)
    if limiar := limiar_de_critico(campos):
        campos.setdefault("Crítico", limiar)
    tiles, notas_tile = tiles_criatura(campos)

    partes: list[str] = []
    if flavor:
        partes.append(f'<p class="prg-bes__flavor" markdown="span">{flavor}</p>')
    if tiles:
        partes.append(tiles)
    if "Atributos" in campos:
        # Ataque já é um dos 8 atributos (d100, 2026-08-20) — a grade lê o
        # campo Ataque junto, sem precisar que a ficha repita o número duas
        # vezes (uma no tile de cabeçalho, outra dentro de "Atributos").
        ataque_bruto = campos.get("Ataque", "")
        bruto_grade = campos["Atributos"] + (f" Ataque {ataque_bruto}" if ataque_bruto else "")
        partes.append(grade_de_atributos(bruto_grade))

    # Imunidade e resistência decidem se o golpe do jogador vale alguma coisa:
    # ficam logo abaixo dos números, antes de qualquer ação.
    defesas = [
        f"**{rotulo}** — {valor}"
        for rotulo, valor in campos.items()
        if rotulo not in IGNORA_CRIATURA and valor
    ]
    for linha in defesas + notas_tile:
        partes.append(f'<p class="prg-bes__defesa" markdown="span">{linha}</p>')
    for linha in notas_prosa:
        partes.append(f'<p class="prg-bes__nota" markdown="span">{linha}</p>')

    passivas = [b for b in blocos if b[1].startswith("*(")]
    acoes = [b for b in blocos if not b[1].startswith("*(")]

    # Fecha a lista de ações, como as Ações de Lenda fecham o stat block do
    # D&D Beyond: é a última coisa que o Mestre lê, e a que ele usa no turno
    # dos personagens.
    if acao_de_lenda and texto_puro(campos.get("Tier", "")) == "Lendário":
        acoes = acoes + [("Ação de Lenda", "", ["- " + acao_de_lenda])]
    for titulo, grupo in (("Traços", passivas), ("Ações", acoes)):
        if not grupo:
            continue
        partes.append(f'<p class="prg-bes__titulo">{titulo}</p>')
        partes.extend(linha_de_bloco(*b) for b in grupo)

    corpo = "\n\n".join(partes)
    return f'<div class="prg-bes" markdown="1">\n\n{corpo}\n\n</div>', campos


# O que o Mestre procura numa criatura, na ordem em que ele pergunta: "o que
# fere isso?", "o que não adianta tentar?", "o que ela faz?". As três facetas
# saem lidas da própria ficha — nenhuma exige campo novo.
VOCAB_ELEMENTO = (
    "Fogo", "Gelo", "Raio", "Sombras", "Luz", "Água", "Vento", "Terra", "Veneno",
    "Sangue", "Arcano",
)
VOCAB_FISICO = ("Cortante", "Perfurante", "Impacto")


def _acha(vocab: Iterable[str], texto: str) -> list[str]:
    sem = sem_acento(texto)
    return [v for v in vocab if sem_acento(v) in sem]


def facetas_de_defesa(campos: dict[str, str]) -> tuple[list[str], list[str]]:
    """(vulnerável a, imune a) — o que fere e o que não adianta tentar.

    "Vulnerável" aqui é a pergunta do Mestre, não o termo do glossário: o
    **material** que atravessa a resistência de um Lobisomem responde a mesma
    pergunta que o Fogo responde num Troll, e o markdown escreve os dois de
    jeitos diferentes ("Vulnerabilidade: Fogo" × "Resistência: … exceto de
    armas de Prata"). As duas formas entram na mesma faceta.
    """
    vulner = _acha(VOCAB_ELEMENTO + VOCAB_FISICO, campos.get("Vulnerabilidade", ""))
    if m := re.search(r"exceto de armas de \[?([^\]\n(]+)", campos.get("Resistência", "")):
        vulner.append(m.group(1).strip())

    bruto = " ".join(
        (campos.get("Imunidades", ""), campos.get("Imunidade", ""))
    )
    # "Defesa mental" saiu (d100, 2026-08-20) — imunidade a efeito mental
    # agora vem só do campo Imunidades, que já cobria isso em toda ficha.
    imune = _acha(VOCAB_ELEMENTO + VOCAB_FISICO, bruto)
    sem = sem_acento(bruto)
    if "efeito mental" in sem:
        imune.append("efeito mental")
    if any(p in sem for p in ("derrubar", "empurrar", "agarrar", "imovel", "lento")):
        imune.append("controle de posição")
    if "doenca" in sem:
        imune.append("doença")
    return vulner, imune


# Cada entrada é (rótulo da faceta, o que procurar na ficha inteira).
CAPACIDADES = (
    ("voa", ("**Voo:**",)),
    ("agarra", ("fica [Agarrado]", "Agarrada",)),
    ("invoca", ("levanta como", "Erguem-se", "acordam como", "surge um segundo")),
    ("incorpóreo", ("Incorpóre", "Atravessa criaturas, objetos e paredes")),
    ("petrifica", ("de [Petrificado]",)),
    ("possui", ("[Possuído]",)),
    ("regenera", ("Recupera **", "recupera **", "remonta-se", "volta com **")),
    ("veneno", ("[Envenenado]",)),
    ("ataca a mente", ("vs Fortitude Mágica", "vs Social", "vs Sanidade")),
    ("área", ("cone de", "casas de raio", "linha de")),
)


def capacidades_da_ficha(texto: str) -> list[str]:
    return [rot for rot, chaves in CAPACIDADES if any(c in texto for c in chaves)]


def monta_card_criatura(s: Secao, acao_de_lenda: str = "") -> str:
    flavor, resto = flavor_e_resto(s.corpo)
    corpo_md, campos = ficha_de_criatura(flavor, resto, acao_de_lenda)

    tier = texto_puro(campos.get("Tier", ""))
    tipo = texto_puro(campos.get("Tipo", ""))
    vida = texto_puro(campos.get("Vida", ""))
    pa = texto_puro(campos.get("PA", ""))
    ameaca = texto_puro(campos.get("Ameaça", ""))

    vulner, imune = facetas_de_defesa(campos)
    faz = capacidades_da_ficha("\n".join(resto))

    # Quantos ◈ a criatura tem por turno — a primeira medida de ameaça, e o
    # número que decide quantas rolagens o Mestre administra por rodada.
    achado = re.search(r"\((\d+)\)", pa)
    pa_n = achado.group(1) if achado else ""

    return monta_card_base(
        "bes-" + slug(s.nome),
        s.nome,
        corpo_md,
        classe="prg-card--criatura",
        chips=(chip(tier, "tier") if tier else "") + (chip(tipo, "tipo") if tipo else ""),
        selo=f"{vida} de Vida" if vida else "",
        # A Ameaça abre a faixa: é o número que o Mestre soma varrendo a lista
        # de cards fechados pra montar a sala. O resto encurta como nos tiles.
        colunas=colunas_html(
            [
                ("Ameaça", ameaca),
                ("Ataque", texto_puro(campos.get("Ataque", ""))),
                ("Evasão", texto_puro(campos.get("Evasão", ""))),
                ("PA", valor_de_tile(pa)),
            ]
        ),
        busca=indice_de_busca(s.nome, flavor, texto_puro("\n".join(resto))),
        facetas=facetas_html(
            {
                "tier": slug(tier),
                "tier-nome": tier,
                "tipo": slug(tipo),
                "tipo-nome": tipo,
                "pa": pa_n,
                "pa-nome": f"{'◈' * int(pa_n)} ({pa_n})" if pa_n else "",
                "vida": re.sub(r"\D", "", vida),
                # O que o Mestre gasta ao pôr a criatura na sala: vira slider
                # de orçamento, do mesmo jeito que a Mana nas habilidades.
                "ameaca": ameaca,
                # As três perguntas que se faz de uma criatura, nessa ordem.
                "vulneravel": " ".join(slug(v) for v in vulner),
                "vulneravel-nome": "|".join(vulner),
                "imune": " ".join(slug(v) for v in imune),
                "imune-nome": "|".join(imune),
                "faz": " ".join(slug(v) for v in faz),
                "faz-nome": "|".join(faz),
            }
        ),
    )


def monta_listagem_bestiario(markdown: str, docs_dir: Path) -> tuple[str, int]:
    linhas = markdown.split("\n")
    secoes = extrai_secoes(linhas)
    if not secoes:
        return markdown, 0
    corte = next(i for i, l in enumerate(linhas) if l.startswith("## "))
    lenda = regra_da_acao_de_lenda(docs_dir)
    cards = [monta_card_criatura(s, lenda) for s in secoes]
    return "\n".join(linhas[:corte]) + "\n\n" + "\n".join(cards), len(cards)


# -------------------------------------------------------------------- raças

# Nas Raças o campo é um parágrafo, não um bullet: `**Atributos:** ...` numa
# linha só. As duas divisórias agrupam as levas.
RE_CAMPO_PARAGRAFO = re.compile(r"^\*\*([^:*]+):\*\*\s*(.*)$")

DIVISORIAS_RACA = frozenset({"Raças de Animal", "Raças de Peixe/Água", "Raças Exóticas"})

# Quantos pontos de atributo a raça concede, no total. Duas formas aparecem:
#   "escolha 2 dentre X, Y, Z, e distribua +2/+1 entre eles"  -> 3
#   "+3 pontos (2+1), distribuídos entre quaisquer 2"          -> 3
RE_PONTOS_PAR = re.compile(r"\+(\d+)\s*/\s*\+(\d+)")
RE_PONTOS_UM = re.compile(r"\+(\d+)")


def campos_de_paragrafo(corpo: list[str]) -> dict[str, str]:
    campos: dict[str, str] = {}
    for linha in corpo:
        if m := RE_CAMPO_PARAGRAFO.match(linha.strip()):
            campos[m.group(1).strip()] = m.group(2).strip()
    return campos


def pontos_de_atributo(bruto: str) -> int:
    if m := RE_PONTOS_PAR.search(bruto):
        return int(m.group(1)) + int(m.group(2))
    if m := RE_PONTOS_UM.search(bruto):
        return int(m.group(1))
    return 0


def monta_card_raca(s: Secao, levas_com_regra: dict[str, list[str]]) -> str:
    flavor, resto = flavor_e_resto(s.corpo)
    campos = campos_de_paragrafo(resto)

    atributos_md = campos.get("Atributos", "")
    fisico = campos.get("Traço Físico", "")
    pontos = pontos_de_atributo(atributos_md)

    # A leva de água concede um traço comum a todas as raças dela, escrito uma
    # vez só na abertura. O traço é da raça tanto quanto os outros, então ele
    # entra na ficha de cada uma — o markdown continua tendo uma cópia só, o
    # hook é que a distribui.
    if tracos_leva := levas_com_regra.get(s.familia, []):
        resto = resto + ["", f"**Traço de {s.familia}:**", "", *tracos_leva]

    # Cada traço racial é um bullet `- **Nome** — efeito`, logo abaixo do
    # rótulo "Traço Racial"/"Traços Raciais". Contar é o que responde "esta
    # raça é simples ou carregada?" sem precisar abrir o card.
    nomes_traco = re.findall(r"^-\s+\*\*([^*]+)\*\*", "\n".join(resto), re.M)
    leva = s.familia or "Fundadoras"
    # "escolha 2 dentre Força, Vitalidade, Vontade" -> o pool, não a frase: é
    # o que responde "que raça serve pro personagem que eu quero".
    pool = atributos_citados(atributos_md)

    corpo_md = "\n".join(([f"*{flavor}*", ""] if flavor else []) + resto)

    return monta_card_base(
        "rac-" + slug(s.nome),
        s.nome,
        corpo_md,
        classe="prg-card--raca",
        chips=chip(leva, "leva"),
        selo=f"+{pontos} atributo" + ("s" if pontos != 1 else ""),
        colunas=colunas_html(
            [
                (
                    "Atributos",
                    " · ".join(n for _, n in pool) if pool else "livre entre os 8",
                ),
                ("Traço Físico", texto_puro(fisico).rstrip(".")),
                ("Traços", str(len(nomes_traco))),
            ]
        ),
        busca=indice_de_busca(s.nome, flavor, texto_puro("\n".join(resto))),
        facetas=facetas_html(
            {
                "leva": slug(leva),
                "leva-nome": leva,
                "atributos": " ".join(c for c, _ in pool) or "livre",
                "atributos-nome": "|".join(n for _, n in pool) or "Livre entre os 8",
                "tracos": str(len(nomes_traco)),
                "tracos-nome": f"{len(nomes_traco)} traço"
                + ("s" if len(nomes_traco) != 1 else ""),
                "pontos": str(pontos),
            }
        ),
    )


def prosa_das_levas(linhas: list[str]) -> tuple[str, dict[str, list[str]]]:
    """A apresentação de cada leva, e os traços que ela concede a todas.

    Devolve (prosa, {leva: [bullets de traço]}). A prosa é só a apresentação —
    os traços saem dela e vão pra dentro dos cards, que é onde o jogador
    procura o que a raça dele tem.
    """
    partes: list[str] = []
    tracos: dict[str, list[str]] = {}
    for i, linha in enumerate(linhas):
        nome = linha[3:].strip() if linha.startswith("## ") else ""
        if nome not in DIVISORIAS_RACA:
            continue
        corpo: list[str] = []
        for seguinte in linhas[i + 1 :]:
            if seguinte.startswith("## "):
                break
            corpo.append(seguinte)

        bullets = [l for l in corpo if l.startswith("- **")]
        if bullets:
            tracos[nome] = bullets
        # A apresentação é o que sobra: sem os bullets, e sem a frase que os
        # anunciava (ela some junto com eles).
        apresentacao = [
            l for l in corpo if l not in bullets and "traço de exceção abaixo" not in l
        ]
        texto = "\n".join(apresentacao).strip()
        if texto:
            partes.append(f"**{nome}** — {texto}")
    return ("\n\n".join(partes), tracos)


def monta_listagem_racas(markdown: str) -> tuple[str, int]:
    linhas = markdown.split("\n")
    # "Como Funcionam as Raças" é prosa de abertura, não uma raça: fica de fora
    # da varredura e continua acima da barra de filtro.
    corte = next(
        (i for i, l in enumerate(linhas) if l.startswith("## ") and "Funcionam" not in l),
        None,
    )
    if corte is None:
        return markdown, 0

    levas, com_regra = prosa_das_levas(linhas[corte:])
    secoes = extrai_secoes(linhas[corte:], DIVISORIAS_RACA)
    cards = [monta_card_raca(s, com_regra) for s in secoes]

    # A apresentação das levas entra recuada, o que a faz cair dentro do
    # bloco `???` que a página já abriu — uma caixa só, não duas.
    abertura = "\n".join(linhas[:corte]).rstrip()
    if levas:
        recuado = "\n".join(
            ("    " + l if l.strip() else "") for l in levas.split("\n")
        )
        abertura += "\n\n    As raças vieram em três levas:\n\n" + recuado
    return abertura + "\n\n" + "\n".join(cards), len(cards)


# ------------------------------------------------------------------ origens
#
# Origem não é seção: são três tabelas d20, e cada linha é uma escolha. O card
# é curto de propósito — nome, eixo, número do dado e o traço —, porque é isso
# que a linha da tabela já era. O ganho é poder filtrar e sortear as três
# tabelas ao mesmo tempo, sem perder a tabela de papel.

EIXOS_ORIGEM = {
    "Passado": "a vida ou profissão antes de aventurar",
    "Ambiente de Origem": "a paisagem e a cultura onde cresceu",
    "Evento Formador": "o momento que definiu o personagem",
}

# Como o traço age, lido do próprio texto — não é classificação nova, é o verbo
# que a linha já usa. Serve pra responder "que origem me dá um recurso, e não
# só uma Vantagem?", que é a pergunta real de quem monta ficha.
FEITIOS = (
    ("recurso", "Recurso por descanso", r"\b1x por (descanso|cena)\b"),
    ("resistencia", "Resistência ou imunidade", r"\bResist[êe]ncia\b|\bImune\b"),
    ("ignora", "Ignora uma penalidade", r"\bIgnora\b|\bNunca\b|\bSem Desvantagem\b"),
    ("desvantagem", "Impõe Desvantagem a quem age contra", r"\bcom Desvantagem\b"),
    ("atributo", "Mexe num atributo", r"[+-]\d+\s+(em|permanente)"),
    ("vantagem", "Vantagem num teste", r"\bVantagem\b"),
)

RE_LINHA_TABELA = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def feitio_do_traco(traco: str) -> tuple[str, str]:
    texto = texto_puro(traco)
    for chave, nome, padrao in FEITIOS:
        if re.search(padrao, texto, re.I):
            return chave, nome
    return "outro", "Outro efeito"


def monta_card_origem(eixo: str, d20: str, nome: str, traco: str) -> str:
    chave, feitio = feitio_do_traco(traco)
    pool = atributos_citados(traco)

    return monta_card_base(
        f"ori-{slug(eixo)}-{slug(nome)}",
        nome,
        f"- **Traço:** {traco}\n\n"
        f"*{eixo} · resultado {d20} na tabela de 1d20.*",
        classe="prg-card--origem",
        chips=chip(eixo, "eixo"),
        selo=f"nº {d20}",
        classe_selo="prg-card__d20",
        colunas=colunas_html([("Traço", texto_puro(traco))]),
        busca=indice_de_busca(nome, eixo, texto_puro(traco)),
        facetas=facetas_html(
            {
                "eixo": slug(eixo),
                "eixo-nome": eixo,
                "d20": d20,
                "feitio": chave,
                "feitio-nome": feitio,
                "atributos": " ".join(c for c, _ in pool),
                "atributos-nome": "|".join(n for _, n in pool),
            }
        ),
    )


def monta_listagem_origens(markdown: str) -> tuple[str, int]:
    """As três tabelas viram uma listagem só.

    O `## Passado`/`## Ambiente`/`## Evento` some da página junto com a frase
    "pode ser escolhido ou sorteado", que se repetia igual nos três: o eixo
    virou chip e faceta, e o sorteio virou botão. A tabela continua sendo a
    fonte no markdown — o número do d20 vira o selo de cada card, então quem
    rola em papel não perde nada.
    """
    linhas = markdown.split("\n")
    cards: list[str] = []
    eixo = ""
    corte = len(linhas)

    for i, linha in enumerate(linhas):
        if linha.startswith("## "):
            nome = linha[3:].strip()
            if nome in EIXOS_ORIGEM:
                eixo = nome
                corte = min(corte, i)
            else:
                eixo = ""
            continue
        if eixo and (m := RE_LINHA_TABELA.match(linha)):
            d20, nome_linha, traco = m.groups()
            if d20.isdigit():
                cards.append(monta_card_origem(eixo, d20, nome_linha, traco))

    return "\n".join(linhas[:corte]).rstrip() + "\n\n" + "\n".join(cards), len(cards)


# ----------------------------------------------------------------- arsenal

# Seções do Arsenal que são referência (dado/preço/propriedades), não armas —
# ficam de fora da varredura de habilidades de arma.
_ARSENAL_NAO_ARMA = {
    "graus de habilidade de arma",
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


# -------------------------------------------------------------- equipamento
#
# O Arsenal tinha 2.654 linhas: três tabelas de referência, as regras de
# propriedade, e 62 seções de arma com as 3 habilidades de cada uma. Virou
# duas páginas geradas do mesmo markdown — a listagem (cards de arma, escudo
# e armadura) e as regras (as tabelas e as propriedades, lidas ao vivo).
#
# A ficha de cada arma **já existia**, na tabela de dado de dano: Família,
# Dado, Tipo, Preço, Chaves, Requisito, Nota. O card só junta essa linha com a
# seção da arma; nada foi remodelado.

COLUNAS_TABELA_ARMA = ("Arma", "Família", "Dado", "Tipo", "Preço", "Chaves", "Requisito", "Nota")


class FichaArma(NamedTuple):
    grupo: str  # marciais / pontaria / arcano
    campos: dict[str, str]


def le_tabelas_de_arma(arsenal_md: str) -> dict[str, FichaArma]:
    """slug da arma -> a linha dela nas 3 tabelas de dado de dano."""
    fichas: dict[str, FichaArma] = {}
    grupo = ""
    for linha in arsenal_md.split("\n"):
        if m := re.match(r"^### (Marciais|Pontaria|Arcano)\s*$", linha):
            grupo = sem_acento(m.group(1))
            continue
        if linha.startswith("## "):
            grupo = ""
            continue
        if not grupo or not linha.startswith("|"):
            continue
        celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(celulas) != len(COLUNAS_TABELA_ARMA):
            continue
        m = re.match(r"^\[([^\]]+)\]", celulas[0])
        if not m:
            continue  # cabeçalho ou régua
        campos = dict(zip(COLUNAS_TABELA_ARMA, celulas))
        fichas[slug(m.group(1))] = FichaArma(grupo, campos)
    return fichas


def valor_em_prata(bruto: str) -> str:
    """'60 p' -> '60'. Arma lendária não tem preço: fica vazia e o slider a
    deixa passar sempre — não se compra, se acha."""
    m = re.search(r"(\d+)\s*p\b", texto_puro(bruto))
    return m.group(1) if m else ""


def chaves_da_arma(bruto: str) -> list[tuple[str, str]]:
    texto = texto_puro(bruto)
    if not texto or texto.startswith("*("):
        return []
    return [(slug(p.strip()), p.strip()) for p in texto.split(",") if p.strip()]


def monta_card_arma(
    nome: str, secao_md: str, ficha: FichaArma | None, destino: str
) -> str:
    # As 3 habilidades da arma viram ponteiros pros cards que já existem na
    # Listagem de Habilidades — o card de equipamento nunca repete a ficha
    # de uma técnica.
    corpo_md, _ = transforma_para_ponteiros(secao_md, destino, arma=slug(nome))
    # "Arma Finesse (ver [Finesse](#finesse) abaixo)" — o "abaixo" era a seção
    # de propriedades logo adiante na mesma página, que agora é `regras.md`.
    corpo_md = RE_ANCORA_PURA.sub(r"](../jogar/regras-de-equipamento.md#\1)", corpo_md)
    corpo = corpo_md.split("\n")
    corpo = corpo[1:] if corpo and corpo[0].startswith("## ") else corpo

    campos = ficha.campos if ficha else {}
    grupo = ficha.grupo if ficha else ""
    dado = texto_puro(campos.get("Dado", ""))
    tipo = texto_puro(campos.get("Tipo", ""))
    familia = texto_puro(campos.get("Família", ""))
    requisito = texto_puro(campos.get("Requisito", "")).strip("—- ")
    chaves = chaves_da_arma(campos.get("Chaves", ""))
    preco = valor_em_prata(campos.get("Preço", ""))

    _EQUIPAMENTO["equ-" + slug(nome)] = {
        "titulo": nome,
        "corpo": "<br>".join(
            escapa(p)
            for p in (
                " · ".join(x for x in (tipo, dado) if x),
                " · ".join(x for x in (familia, grupo.capitalize() if grupo else "") if x),
                f"Preço: {texto_puro(campos.get('Preço', ''))}",
                f"Requisito: {requisito}" if requisito else "",
            )
            if p
        ),
    }

    return monta_card_base(
        "equ-" + slug(nome),
        nome,
        "\n".join(corpo),
        classe="prg-card--equipamento",
        chips="".join(chip(g, "grupo") for g in [grupo.capitalize()] if g),
        selo=dado,
        colunas=colunas_html(
            [
                ("Tipo", tipo),
                ("Família", familia),
                ("Preço", texto_puro(campos.get("Preço", "")).replace("—", "não se compra")),
                ("Chaves", ", ".join(n for _, n in chaves)),
                ("Requisito", requisito),
            ]
        ),
        busca=indice_de_busca(
            nome, familia, dado, tipo, texto_puro(campos.get("Nota", "")),
            requisito, texto_puro("\n".join(corpo)),
        ),
        facetas=facetas_html(
            {
                "grupo": grupo,
                "categoria": "arma",
                "categoria-nome": "Arma",
                "familia": slug(familia),
                "familia-nome": familia,
                "dado": slug(dado),
                "dado-nome": dado,
                "tipo": slug(tipo),
                "tipo-nome": tipo,
                "chaves": " ".join(c for c, _ in chaves),
                "chaves-nome": "|".join(n for _, n in chaves),
                "requisito": "sim" if requisito else "nao",
                "requisito-nome": "Exige atributo mínimo" if requisito else "Sem requisito",
                "preco": preco,
            }
        ),
    )


def monta_card_protecao(categoria: str, celulas: list[str], nota: str) -> str:
    """Escudo e Armadura não concedem habilidade: são uma linha de tabela.

    Viram card pelo mesmo motivo que as armas — pra caírem no mesmo filtro de
    preço e aparecerem na mesma varredura de "o que eu compro com 50 de prata".
    """
    nome, bonus, preco_md = celulas[0], celulas[1], celulas[2]
    resto = celulas[3] if len(celulas) > 3 else ""

    _EQUIPAMENTO["equ-" + slug(nome)] = {
        "titulo": nome,
        "corpo": "<br>".join(
            escapa(p)
            for p in (
                f"{categoria} · Bônus de Defesa {texto_puro(bonus)}",
                f"Preço: {texto_puro(preco_md)}",
                f"{nota}: {texto_puro(resto)}" if resto else "",
            )
            if p
        ),
    }

    return monta_card_base(
        "equ-" + slug(nome),
        nome,
        f"- **Bônus de Defesa:** {bonus}\n"
        f"- **Preço:** {preco_md}\n"
        + (f"- **{nota}:** {resto}\n" if resto else ""),
        classe="prg-card--equipamento",
        chips=chip(categoria, "categoria"),
        selo=bonus,
        colunas=colunas_html([("Preço", preco_md.replace("—", "—")), (nota, resto)]),
        busca=indice_de_busca(nome, categoria, bonus, texto_puro(resto)),
        facetas=facetas_html(
            {
                "categoria": slug(categoria),
                "categoria-nome": categoria,
                "preco": valor_em_prata(preco_md),
            }
        ),
    )


def cards_de_protecao(arsenal_md: str) -> list[str]:
    linhas = arsenal_md.split("\n")
    cards: list[str] = []
    for titulo, categoria, nota in (
        (r"^### Escudos\s*$", "Escudo", "Restrição"),
        (r"^### Armaduras\s*$", "Armadura", "Traços"),
    ):
        bloco = extrai_intervalo(linhas, titulo, r"^#{2,3} ")
        for linha in bloco:
            if not linha.startswith("|"):
                continue
            celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
            if len(celulas) < 3 or set(celulas[0]) <= {"-", " "}:
                continue
            if celulas[1].startswith("Bônus") or celulas[0] in ("Categoria", "Armadura"):
                continue
            # "Nenhuma" é a linha de referência da tabela — a ausência de
            # armadura, não um item que se compra ou se carrega.
            if celulas[0] == "Nenhuma":
                continue
            cards.append(monta_card_protecao(categoria, celulas, nota))
    return cards


def monta_listagem_equipamento(arsenal_md: str, destino: str) -> tuple[str, int]:
    """A abertura fica; as 62 seções de arma e as duas tabelas de proteção
    viram cards. As regras vão pra `equipamento/regras.md`."""
    fichas = le_tabelas_de_arma(arsenal_md)
    linhas = arsenal_md.split("\n")
    corte = next(
        (i for i, l in enumerate(linhas) if re.match(r"^## ", l)), len(linhas)
    )
    cards = [
        monta_card_arma(nome, secao, fichas.get(slug(nome)), destino)
        for nome, secao in extrai_secoes_de_arma(arsenal_md)
    ]
    cards.extend(cards_de_protecao(arsenal_md))
    return "\n".join(linhas[:corte]).rstrip() + "\n\n" + "\n".join(cards), len(cards)


def monta_regras_de_equipamento(docs_dir: Path) -> list[str]:
    """As seções de referência do Arsenal, lidas ao vivo da listagem.

    O markdown continua num arquivo só; esta página é a outra vista dele —
    mesma ideia de `habilidades/regras.md`.
    """
    arsenal = (docs_dir / "equipamento" / "index.md").read_text(encoding="utf-8")
    linhas = arsenal.split("\n")
    partes = [
        *extrai_intervalo(linhas, r"^## Graus de Habilidade de Arma\s*$", r"^## Tabela"),
        "",
        *extrai_intervalo(linhas, r"^## Tabela de Dados de Dano\s*$", r"^## Assinatura"),
        "",
        *extrai_intervalo(linhas, r"^## Assinatura de Tipo de Dano\s*$", r"^## Propriedades"),
        "",
        *extrai_intervalo(linhas, r"^## Propriedades de Arma\s*$", r"^## [A-ZÀ-Ú]"),
        "",
        *extrai_intervalo(linhas, r"^## Resolução de Ataque\s*$"),
    ]

    # As tabelas linkam cada arma com `#florete`, que era uma seção da mesma
    # página. Agora a arma é um card na listagem: a âncora atravessa. O que
    # continua sendo regra (`#finesse`, `#leve`) fica onde está.
    armas = {slug(n) for n, _ in extrai_secoes_de_arma(arsenal)}

    def religa(m: re.Match) -> str:
        chave = m.group(1)
        return (
            f"](../equipamento/index.md#equ-{chave})" if chave in armas else m.group(0)
        )

    return [RE_ANCORA_PURA.sub(religa, l) for l in partes]


# ------------------------------------------------------- listagem única

# As 14 páginas de grupo, exceto Mágicas por Elemento — essa precisa de
# tratamento à parte porque cada uma das 11 seções (10 elementos + Arcano)
# vira uma faceta de elemento diferente, não um grupo só.
_GRUPOS_ARQUIVO = (
    "marciais", "pontaria", "sociais",
    "infiltracao", "mobilidade", "buff", "debuff", "suporte",
    "necromancia", "projecao-mental", "alquimia-de-mana", "percepcao-arcana",
    "conjuracao", "espaco-tempo",
)


def cards_magicas_elementais(docs_dir: Path) -> tuple[list[str], int]:
    """Cada `## Elemento` do arquivo vira sua própria faceta — o arquivo tem
    um grupo só (Mágicas por Elemento), mas 10 assinaturas diferentes."""
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
    """Todos os cards do jogo — os 14 grupos simples + Mágicas por Elemento
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

    arsenal_md = (docs_dir / "equipamento" / "index.md").read_text(encoding="utf-8")
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

    arsenal = (docs_dir / "equipamento" / "index.md").read_text(encoding="utf-8")
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
    "Escudo" onde o Equipamento tem o card "Escudos", e as duas precisam cair no
    mesmo valor de filtro que a Listagem de Habilidades usa.
    """
    achados = re.findall(
        r"\[([^\]]+)\]\([^)]*equipamento/index\.md#equ-([^)\s]+)\)", arma_md
    )
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

    return monta_card_base(
        ident,
        p.nome,
        "\n".join(corpo),
        classe="prg-card--pacote",
        chips=chip(vertente_nome, "vert") if vertente_nome else "",
        selo=f"nº {d20}" if d20 is not None else "",
        classe_selo="prg-card__d20",
        colunas=colunas_html(
            [
                ("Arma inicial", ", ".join(n for _, n in armas) or "sem arma"),
                ("Atributo", resume_atributo(p.atributo)),
                ("Termina em", final_nome),
            ]
        ),
        # A trilha inteira entra no índice: "que pacote usa Fluxo?" tem que se
        # responder digitando "fluxo" na busca, não só pelos menus.
        busca=indice_de_busca(
            p.nome,
            p.flavor,
            vertente_nome,
            str(meta.get("conceito", "")),
            texto_puro(p.arma_md),
            p.atributo,
            *nomes_trilha,
        ),
        facetas=facetas_html(
            {
                "vertente": slug(vertente_nome),
                "vertente-nome": vertente_nome,
                "d20": str(d20) if d20 is not None else "",
                "armas": " ".join(s for s, _ in armas) or "sem-arma",
                "armas-nome": "|".join(n for _, n in armas) or "Sem arma inicial",
                "atributos": " ".join(atributos),
                "final": slug(final_nome),
                "final-nome": final_nome,
            }
        ),
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


# ------------------------------------------------------------------- mundo
#
# Wiki de cenário: cada página em docs/mundo/ (fora index.md e mapa.md) que
# declarar `tipo:` no cabeçalho da página vira um verbete. O bloco de bullets
# `- **Campo:** valor` logo abaixo do título vira ficha lateral; o resto do
# texto flui normal. Nenhum campo é obrigatório — só entra na ficha o que a
# página realmente preencher, do mesmo jeito que a ficha de habilidade/criatura.

TIPOS_MUNDO = {
    "lugar": "Lugar",
    "faccao": "Facção",
    "pessoa": "Pessoa",
    "personagem": "Personagem",
    "evento": "Batalha/Evento",
    "recurso": "Recurso",
    "divindade": "Divindade",
}

RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

# Popover de cada página de Mundo, no mesmo contrato do glossário e das
# habilidades: on_post_build grava em assets/mundo.json e o JS mostra ao
# passar o mouse num link que aponte pra página.
_mundo: dict[str, dict[str, str]] = {}


def primeiro_paragrafo_de(md: str) -> str:
    """O primeiro parágrafo de prosa — pula título, ficha, admonition, lista."""
    for bloco in md.strip().split("\n\n"):
        bloco = bloco.strip()
        if bloco and not bloco.startswith(("#", "<", "!!!", "???", "-", "|")):
            return " ".join(bloco.split())
    return ""


def processa_pagina_mundo(md: str, tipo: str, url: str) -> str:
    """Extrai a ficha lateral de uma página de Mundo e alimenta o popover.

    A ficha continua sendo markdown de verdade dentro do `<aside markdown="1">`
    (o tema já lê isso via md_in_html) — um valor tipo `[Poponia](...)` vira
    link normal, sem precisar de um conversor de markdown à parte. O campo
    `Retrato` é especial: se presente, some o rótulo em negrito e vira a
    primeira coisa na ficha (imagem grande no topo, sem legenda).
    """
    m = RE_H1.search(md)
    if not m:
        return md

    titulo = m.group(1).strip()
    resto = md[m.end():]
    linhas = resto.split("\n")

    i = 0
    while i < len(linhas) and not linhas[i].strip():
        i += 1
    inicio_campos = i
    campos: list[tuple[str, str]] = []
    while i < len(linhas):
        campo = RE_CAMPO.match(linhas[i])
        if not campo:
            break
        campos.append((campo.group(1).strip(), campo.group(2).strip()))
        i += 1
    fim_campos = i

    resto_sem_campos = "\n".join(linhas[:inicio_campos] + linhas[fim_campos:])
    resumo = primeiro_paragrafo_de(resto_sem_campos)
    tipo_valor = next(
        (v for r, v in campos if sem_acento(r) == "tipo" and v),
        TIPOS_MUNDO.get(tipo, tipo),
    )
    corpo_popover = f"<p><i>{escapa(tipo_valor)}</i></p>"
    if resumo:
        corpo_popover += f"<p>{html_do_verbete(resumo)}</p>"
    _mundo[url] = {"titulo": titulo, "corpo": corpo_popover}

    if not campos:
        return md

    # "Retrato" (pessoa/facção) e "Mapa" (lugar) levam o mesmo tratamento: a
    # imagem sai do rótulo em negrito e vira o topo da ficha, sem duplicar a
    # lógica pra cada nome de campo.
    CAMPOS_IMAGEM = ("retrato", "mapa")
    imagem = next((v for r, v in campos if sem_acento(r) in CAMPOS_IMAGEM and v), None)
    campos_com_label = "\n\n".join(
        f"**{r}:** {v}" for r, v in campos if v and sem_acento(r) not in CAMPOS_IMAGEM
    )
    corpo_ficha = (f"{imagem}\n\n" if imagem else "") + campos_com_label
    ficha = f'<aside class="prg-ficha-lateral" markdown="1">\n\n{corpo_ficha}\n\n</aside>\n'
    return md[: m.end()] + "\n\n" + ficha + resto_sem_campos


# ---------------------------------------------------------- páginas (genérico)

# Popover genérico de página/seção, no mesmo contrato do glossário, das
# habilidades e de Mundo: on_post_build grava em assets/paginas.json e o JS
# mostra ao passar o mouse. Diferente dos outros três, ninguém escreve verbete
# à mão pra alimentar este — o primeiro parágrafo da página (ou da seção) já
# é o resumo, então toda página nova entra sozinha.
_paginas: dict[str, dict[str, str]] = {}

RE_HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.MULTILINE)


def trunca(texto: str, limite: int = 220) -> str:
    """Corta no limite de palavra mais próximo — nunca no meio de uma."""
    if len(texto) <= limite:
        return texto
    corte = texto[:limite].rsplit(" ", 1)[0]
    return corte + "…"


def coleta_paginas(markdown: str, url: str) -> None:
    """Primeiro parágrafo da página inteira, e de cada seção `##`/`###` dela.

    A âncora de cada seção usa `slug()` — a mesma normalização que o `toc` do
    MkDocs aplica pra gerar o id de verdade no HTML, então a chave bate com o
    href que qualquer link já escreve, sem precisar de mapa manual.
    """
    headings = list(RE_HEADING.finditer(markdown))
    if not headings:
        return

    def corpo_apos(inicio: int, fim: int) -> str:
        resumo = primeiro_paragrafo_de(markdown[inicio:fim])
        return html_do_verbete(trunca(resumo)) if resumo else ""

    if headings[0].group(1) == "#":
        m0 = headings[0]
        fim = headings[1].start() if len(headings) > 1 else len(markdown)
        corpo = corpo_apos(m0.end(), fim)
        if corpo:
            _paginas[url] = {"titulo": m0.group(2).strip(), "corpo": corpo}

    for i, m in enumerate(headings):
        if len(m.group(1)) not in (2, 3):
            continue
        fim = headings[i + 1].start() if i + 1 < len(headings) else len(markdown)
        corpo = corpo_apos(m.end(), fim)
        if corpo:
            titulo = m.group(2).strip()
            _paginas[f"{url}#{slug(titulo)}"] = {"titulo": titulo, "corpo": corpo}


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


class Verbete(NamedTuple):
    termo: str
    categoria: str
    corpo: list[str]
    ancora: str


# Âncora explícita num verbete: `### Escudo (item) {: #escudo-item }`.
#
# O slug automático só é único porque os nomes são únicos — e eles não são: o
# glossário define "Escudo" duas vezes de propósito (a condição e o item), e o
# próprio verbete avisa da colisão. Sem âncora explícita o segundo virava
# `escudo_1`, um id gerado por ordem de arquivo: nada podia linkar pra ele com
# segurança, e o popover de "Escudo" mostrava o verbete errado, porque o último
# a ser lido sobrescrevia o primeiro no dicionário.
RE_ANCORA_EXPLICITA = re.compile(r"^(.*?)\s*\{:\s*#([\w-]+)\s*\}\s*$")


def extrai_verbetes(markdown: str) -> list[Verbete]:
    """Cada `### Termo` do glossário, com a `## Categoria` que o contém."""
    verbetes: list[Verbete] = []
    categoria = ""
    termo = ""
    ancora = ""
    buffer: list[str] = []

    def grava() -> None:
        if termo:
            verbetes.append(Verbete(termo, categoria, list(buffer), ancora))

    for linha in markdown.split("\n"):
        if linha.startswith("## "):
            grava()
            categoria, termo, ancora, buffer = linha[3:].strip(), "", "", []
        elif m := RE_VERBETE.match(linha):
            grava()
            bruto = m.group(1).strip()
            if e := RE_ANCORA_EXPLICITA.match(bruto):
                termo, ancora = e.group(1).strip(), e.group(2)
            else:
                termo, ancora = bruto, slug(bruto)
            buffer = []
        elif termo:
            buffer.append(linha)
    grava()
    return verbetes


# A categoria é longa demais pra virar rótulo de filtro e de chip ("Elementos
# (dentro de Mágicas por Elemento)"). O nome curto é só de exibição — a fonte
# continua sendo o `## ` do arquivo.
CATEGORIA_CURTA = {
    "Elementos (dentro de Mágicas por Elemento)": "Elementos",
    "Graus de Habilidade de Arma": "Graus de Arma",
}


def indice_az(verbetes: list[Verbete]) -> str:
    """O índice alfabético que o glossário não tinha.

    A fonte continua agrupada por categoria — é assim que se lê. Isto é a outra
    entrada: quem chega sabendo o termo e só quer achar onde ele está.
    """
    por_letra: dict[str, list[Verbete]] = {}
    for v in sorted(verbetes, key=lambda v: sem_acento(v.termo)):
        por_letra.setdefault(sem_acento(v.termo)[:1].upper(), []).append(v)

    blocos = []
    for letra, itens in por_letra.items():
        links = " ".join(
            f'<a class="prg-az__item" href="#{v.ancora}">{escapa(v.termo)}</a>'
            for v in itens
        )
        blocos.append(
            f'<div class="prg-az__letra"><b>{letra}</b>{links}</div>'
        )

    return (
        '<nav class="prg-az" aria-label="Índice alfabético de termos">\n'
        + "\n".join(blocos)
        + "\n</nav>\n"
    )


def retrolinks(verbetes: list[Verbete]) -> dict[str, list[tuple[str, str]]]:
    """Quem cita quem, dentro do próprio glossário: âncora -> [(termo, âncora)].

    Não é classificação minha: se o verbete de *Agarrado* diz "fica Imóvel", os
    dois estão relacionados por decisão do texto. O "Veja também" só torna essa
    ligação navegável nos dois sentidos — hoje ela só funciona num.
    """
    existentes = {v.ancora for v in verbetes}
    citam: dict[str, set[tuple[str, str]]] = {}
    for v in verbetes:
        corpo = "\n".join(v.corpo)
        alvos = set(re.findall(r"\]\((?:[^)#]*glossario\.md)?#([\w-]+)\)", corpo))
        for alvo in alvos:
            if alvo in existentes and alvo != v.ancora:
                citam.setdefault(alvo, set()).add((v.termo, v.ancora))
    return {
        k: sorted(vs, key=lambda par: sem_acento(par[0])) for k, vs in citam.items()
    }


def monta_glossario(markdown: str) -> tuple[str, int]:
    """Envolve cada verbete pra que o filtro consiga escondê-lo, e acrescenta
    o índice A–Z e o "Veja também". O texto de cada verbete não é tocado."""
    verbetes = extrai_verbetes(markdown)
    if not verbetes:
        return markdown, 0
    citacoes = retrolinks(verbetes)

    linhas = markdown.split("\n")
    corte = next(i for i, l in enumerate(linhas) if l.startswith("## "))
    abertura = "\n".join(linhas[:corte]).rstrip()

    saida: list[str] = []
    categoria = ""
    for v in verbetes:
        if v.categoria != categoria:
            if categoria:
                saida.append("</div>\n")
            categoria = v.categoria
            curta = CATEGORIA_CURTA.get(categoria, categoria)
            saida.append(
                f'<div class="prg-grupo" data-grupo-nome="{escapa(curta)}" '
                f'markdown="block">\n\n## {categoria}\n'
            )
        corpo = "\n".join(v.corpo).strip()
        vizinhos = citacoes.get(v.ancora, [])
        if vizinhos:
            links = ", ".join(f"[{nome}](#{anc})" for nome, anc in vizinhos)
            corpo += f'\n\n<span class="prg-vejatambem">Veja também: {links}</span>'
        saida.append(
            f'<div class="prg-verbete" '
            f'data-categoria="{slug(categoria)}" '
            f'data-categoria-nome="{escapa(curta)}" '
            f'data-busca="{indice_de_busca(v.termo, texto_puro(corpo))}" '
            f'markdown="block">\n\n### {v.termo}\n\n{corpo}\n\n</div>\n'
        )
    saida.append("</div>\n")

    return abertura + "\n\n" + indice_az(verbetes) + "\n" + "\n".join(saida), len(verbetes)


# ------------------------------------------------- auto-link do glossário
#
# O popover só aparece onde alguém escreveu o link à mão. Nas habilidades a
# cobertura é alta (o campo Chave sempre linka), mas nas páginas de texto
# corrido um "fica Atordoado" costuma passar sem link — justamente onde o
# leitor mais precisaria da definição.
#
# Duas restrições deliberadas:
#
# 1. Só nas páginas de prosa. As páginas que viram listagem têm markdown
#    *estruturado* (`- **Chave:** ...`), que os extratores leem; injetar link
#    ali arriscaria quebrar o parsing pra ganhar pouco.
# 2. Só nas categorias que são regra. Linkar as 62 armas, os 14 grupos e os 11
#    elementos encheria o texto de links — "Fogo", "Luz" e "Marciais" aparecem
#    o tempo todo sem querer dizer o verbete.

CATEGORIAS_AUTOLINK = frozenset(
    {
        "Termos de Resolução",
        "Estatísticas do Personagem",
        "Condições",
        "Efeitos de Terreno",
        "Dano",
        "Graus de Habilidade de Arma",
        "Propriedades de Arma",
    }
)

# Termos que são também palavra comum do português, ou que colidem com outro
# conceito do próprio jogo. Linkar automaticamente daria links errados, que são
# piores que link nenhum — o leitor confia no que clica.
#
#   Básica/Avançada/Especial  graus de arma, mas "Ação Básica" e "caso especial"
#                             aparecem o tempo todo querendo dizer outra coisa
#   Escudo                    o item e a condição têm o mesmo nome (o próprio
#                             glossário avisa dessa colisão)
#   Leve                      propriedade de arma, armadura leve, escudo leve
#   Impacto                   tipo de dano, mas também "de impacto" corrente
#   Arcano                    tipo de dano e grupo de arma
#   Híbrida, Risco            curtos demais pra desambiguar sem contexto
#
# Continuam linkáveis à mão em qualquer lugar — o que sai daqui é só o
# automático.
AMBIGUOS_AUTOLINK = frozenset(
    {"Básica", "Avançada", "Especial", "Escudo", "Leve", "Impacto", "Arcano",
     "Híbrida", "Risco"}
)

# Termo que só é ambíguo dentro de uma expressão maior. Em vez de descartar o
# termo inteiro, descarta-se a ocorrência: (lookbehind, lookahead).
#
#   "Último Turno"       é a regra de morrer agindo, não a unidade de tempo
#   "Resistência física" é a robustez do corpo (a Vitalidade), não a mecânica
#                        que corta o dano pela metade
GUARDAS_AUTOLINK = {
    "Turno": (r"(?<!Último )", ""),
    "Resistência": ("", r"(?! física| mental)"),
}

PAGINAS_AUTOLINK = ("jogar/", "criacao/", "mestre/")
# As duas páginas de regra mudaram do Compêndio pro Livro do Jogador em
# 2026-08-27 e caíram dentro de `jogar/` — mas são páginas que já linkam o
# glossário à mão em quase todo termo. Deixá-las no auto-link poria um segundo
# link competindo com o que já existe, sem ganho nenhum.
FORA_DO_AUTOLINK = (
    "jogar/regras-de-habilidade.md",
    "jogar/regras-de-equipamento.md",
)

# Trechos onde um link não pode entrar, na ordem em que precisam ser achados:
# bloco de código, código inline, link ou imagem que já existe, elemento HTML
# de uma linha só com o próprio texto dentro (rótulo de card visual, tipo
# `<div ...>Defesa</div>`), tag HTML solta, título, e a linha de título de um
# admonition.
# O par elemento+texto+fechamento vem antes da tag solta na alternação: sem
# isso, "Defesa" dentro do rótulo de um card (ver docs/jogar/atributos.md)
# virava alvo do auto-link e o markdown quebrado aparecia como texto na
# página — a tag sozinha não protege o que está *dentro* dela.
# Nada de re.DOTALL aqui: com ele, `.*$` do título percorreria o arquivo
# inteiro até o último fim de linha e protegeria a página toda. Os padrões de
# linha usam [^\n] de propósito, e o bloco de código traz o seu próprio
# [\s\S] delimitado.
RE_PROTEGIDO = re.compile(
    r"```[\s\S]*?```"
    r"|`[^`\n]+`"
    r"|!?\[[^\]]*\]\([^)]*\)"
    r"|<([a-zA-Z][a-zA-Z0-9]*)\b[^>\n]*>[^<\n]*</\1\s*>"
    r"|<[^>\n]+>"
    r"|^#{1,6} [^\n]*"
    r"|^[ \t]*!!![^\n]*"
    r"|^[ \t]*\|[\s\-:|]+\|[ \t]*$",
    re.M,
)

_TERMOS_AUTOLINK: list[tuple[str, str]] | None = None


def termos_para_autolink(docs_dir: Path) -> list[tuple[str, str]]:
    """[(termo, slug), ...] do mais longo pro mais curto.

    A ordem importa: "Terreno Difícil" precisa ser testado antes de "Terreno",
    senão o termo curto quebra o longo ao meio.
    """
    global _TERMOS_AUTOLINK
    if _TERMOS_AUTOLINK is None:
        verbetes = extrai_verbetes(
            (docs_dir / "glossario.md").read_text(encoding="utf-8")
        )
        _TERMOS_AUTOLINK = sorted(
            (
                (v.termo, v.ancora)
                for v in verbetes
                if v.categoria in CATEGORIAS_AUTOLINK
                and v.termo not in AMBIGUOS_AUTOLINK
            ),
            key=lambda par: -len(par[0]),
        )
    return _TERMOS_AUTOLINK


def autolinka(markdown: str, caminho: str, docs_dir: Path) -> tuple[str, int]:
    """Linka a primeira ocorrência de cada termo ainda não linkado na página.

    Primeira ocorrência só: linkar as sete vezes que "Atordoado" aparece numa
    página transforma o texto num campo minado azul. A primeira basta — o
    popover está a um passar de mouse dali.
    """
    subida = "../" * caminho.count("/")
    alvo = f"{subida}glossario.md"

    # Termo que a página já linka à mão não recebe outro: quem escreveu
    # escolheu onde queria a âncora.
    ja_linkados = set(re.findall(r"\]\([^)]*glossario\.md#([a-z0-9-]+)\)", markdown))

    pendentes = [
        (termo, chave)
        for termo, chave in termos_para_autolink(docs_dir)
        if chave not in ja_linkados
    ]
    if not pendentes:
        return markdown, 0

    # O texto é fatiado nos trechos protegidos; só os pedaços entre eles são
    # candidatos. Assim nenhum regex precisa "entender" markdown.
    pedacos: list[str] = []
    fim = 0
    for m in RE_PROTEGIDO.finditer(markdown):
        pedacos.append(markdown[fim : m.start()])
        pedacos.append(m.group(0))
        fim = m.end()
    pedacos.append(markdown[fim:])

    feitos: set[str] = set()
    for i in range(0, len(pedacos), 2):  # só os índices pares são linkáveis
        for termo, chave in pendentes:
            if chave in feitos:
                continue
            antes, depois = GUARDAS_AUTOLINK.get(termo, ("", ""))
            padrao = re.compile(
                rf"(?<![\w\[]){antes}({re.escape(termo)})(?![\w\]]){depois}"
            )
            novo, n = padrao.subn(rf"[\1]({alvo}#{chave})", pedacos[i], count=1)
            if n:
                pedacos[i] = novo
                feitos.add(chave)

    return "".join(pedacos), len(feitos)


def coleta_glossario(markdown: str) -> None:
    """Alimenta o dicionário do popover, com a mesma leitura que a página usa.

    Passou a usar `extrai_verbetes` justamente por causa do "Escudo": havia
    dois parsers do mesmo arquivo, e só um sabia de âncora explícita.
    """
    for v in extrai_verbetes(markdown):
        # Só o essencial: o primeiro parágrafo já define o termo.
        resumo = "\n".join(v.corpo).strip().split("\n\n")[0].strip()
        if resumo:
            _glossario[v.ancora] = {
                "titulo": v.termo,
                "corpo": html_do_verbete(resumo),
            }


# ----------------------------------------------------------------- arte

_ARTE: dict[str, str] = {}
_DIR_ARTE = Path(__file__).resolve().parent.parent / "docs" / "assets" / "img"


_SEQ_ARTE = itertools.count()


def svg(nome: str) -> str:
    """SVG inline (herda currentColor, acompanha o tema claro/escuro).

    O divisor aparece várias vezes na mesma página, e ele carrega gradientes
    com id próprio. Inline e repetido, isso viraria id duplicado no HTML — o
    navegador resolveria toda referência pro primeiro. Cada cópia leva um
    sufixo, então cada uma aponta pro próprio gradiente.
    """
    if nome not in _ARTE:
        arquivo = _DIR_ARTE / f"{nome}.svg"
        _ARTE[nome] = (
            arquivo.read_text(encoding="utf-8").strip() if arquivo.exists() else ""
        )
    bruto = _ARTE[nome]
    if 'id="' not in bruto:
        return bruto
    sufixo = f"-{next(_SEQ_ARTE)}"
    return re.sub(r'(id="|url\(#)([\w-]+)', rf"\1\2{sufixo}", bruto)


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


# --------------------------------------------------------- barra de filtro
#
# Uma barra só, para as seis listagens. O JS popula cada menu a partir do que
# os cards de fato declaram, então aqui basta dizer que faceta existe e como
# ela se chama quando nada está selecionado.


def monta_barra(
    rotulo: str,
    placeholder: str,
    facetas: list[tuple[str, str, bool]],
    linha3: str = "",
    alvo: str = "",
    expandir: bool = True,
) -> str:
    """`alvo` troca o que a barra filtra (o padrão é `.prg-card`); `expandir`
    some com o botão de abrir tudo, que só faz sentido pra card colapsável."""
    menus = "".join(
        f'<select class="prg-filtro__select" data-faceta="{nome}"'
        + (' data-multi="1"' if multi else "")
        + f' aria-label="{escapa(vazio)}">'
        + f'<option value="">{escapa(vazio)}</option></select>\n'
        for nome, vazio, multi in facetas
    )
    return (
        f'<div class="prg-filtro" data-rotulo="{escapa(rotulo)}"'
        + (f' data-alvo="{escapa(alvo)}"' if alvo else "")
        + ">\n"
        '<div class="prg-filtro__linha1">\n'
        '<input type="search" class="prg-filtro__campo" '
        f'placeholder="{escapa(placeholder)}" '
        f'aria-label="Filtrar {escapa(rotulo)}">\n'
        '<span class="prg-filtro__contagem"></span>\n'
        + (
            '<button type="button" class="prg-filtro__tudo">Expandir tudo</button>\n'
            if expandir
            else ""
        )
        + "</div>\n"
        # Os menus e os controles de orçamento vivem num bloco próprio pra
        # poderem ser recolhidos de uma vez. A barra é `position: sticky`, e
        # com doze menus ela cobria metade da tela do celular o tempo todo,
        # não só na primeira dobra. O botão que recolhe é criado pelo JS —
        # sem script, o bloco fica visível como sempre foi.
        + '<div class="prg-filtro__avancado">\n'
        + f'<div class="prg-filtro__linha2">\n{menus}</div>\n'
        + (f'<div class="prg-filtro__linha3">\n{linha3}</div>\n' if linha3 else "")
        + "</div>\n"
        + "</div>\n\n"
    )


def slider(campo: str, rotulo: str, oculta_sem_valor: bool = False) -> str:
    """Controle de orçamento: mostra só o que cabe no valor escolhido.

    `oculta_sem_valor` decide o que fazer com o card que não declara o campo.
    No Mana, não declarar quer dizer "não custa Mana" e o card passa sempre. No
    preço quer dizer "não se compra" (arma lendária), e aí o card tem que sair
    da lista assim que o leitor define um orçamento.
    """
    return (
        '<label class="prg-filtro__mana">\n'
        f"<span>{escapa(rotulo)}: "
        f'<output class="prg-filtro__slider-valor" data-campo="{campo}"></output>'
        "</span>\n"
        f'<input type="range" class="prg-filtro__slider" data-campo="{campo}" '
        + ('data-sem-valor="oculta" ' if oculta_sem_valor else "")
        + f'min="0" value="0" aria-label="{escapa(rotulo)}">\n'
        "</label>\n"
    )


def sorteio(faceta: str, vazio: str, texto: str, lados: int = 20) -> str:
    return (
        f'<select class="prg-filtro__sorteio-grupo" aria-label="{escapa(vazio)}">'
        f'<option value="">{escapa(vazio)}</option></select>\n'
        f'<button type="button" class="prg-filtro__sortear" data-faceta="{faceta}" '
        f'data-lados="{lados}" data-campo="d{lados}">{escapa(texto)}</button>\n'
        '<span class="prg-filtro__sorteio-saida" role="status"></span>\n'
    )


def colapsavel(titulo: str, corpo: str, aberto: bool = False) -> str:
    """Bloco `???` do pymdownx.details, fechado por padrão.

    Numa página de catálogo a lista é o conteúdo: a barra de filtro precisa
    caber na primeira tela. O texto de "como isso funciona" não some — fica a
    um clique, pra quem chega sem saber.
    """
    marcador = "???+" if aberto else "???"
    recuado = "\n".join(
        ("    " + l if l.strip() else "") for l in corpo.split("\n")
    )
    return f'{marcador} regra "{titulo}"\n\n{recuado}\n'


def insere_barra(markdown: str, barra: str, marca: str) -> str:
    """Põe a barra logo antes do primeiro card, depois da prosa de abertura."""
    corte = markdown.find(marca)
    return markdown[:corte] + barra + markdown[corte:] if corte != -1 else markdown


# ------------------------------------------------------------------- hooks

PAGINAS_COM_CARD = ("habilidades/",)

_AUTOLINK_TOTAL: dict[str, int] = {}


def carimba_versao(config) -> list[str]:
    """Põe um hash do conteúdo na URL do nosso CSS e do nosso JS.

    O tema carimba os arquivos dele (`main.ec1eaa64.min.css`), mas `extra_css` e
    `extra_javascript` entram com o nome cru — e como o endereço nunca muda, o
    navegador de quem já visitou o site continua servindo a cópia velha. O HTML
    novo chega, o CSS novo não, e a página aparece sem estilo até o cache
    expirar (o GitHub Pages manda `max-age=600`). Foi exatamente o que
    aconteceu no deploy do stat block.

    Com `?h=<hash>`, toda mudança de conteúdo muda o endereço e invalida o cache
    sozinha; build sem mudança nenhuma gera o mesmo endereço e continua cacheado.
    """
    docs = Path(config["docs_dir"])
    carimbados: list[str] = []
    for lista in ("extra_css", "extra_javascript"):
        novos = []
        for item in config.get(lista) or []:
            # extra_javascript aceita string ou objeto (type/async/defer); o
            # caminho mora em `.path` no segundo caso.
            caminho_str = getattr(item, "path", item)
            arquivo = docs / caminho_str
            if "?" in str(caminho_str) or not arquivo.is_file():
                novos.append(item)
                continue
            digest = hashlib.sha256(arquivo.read_bytes()).hexdigest()[:8]
            novo = f"{caminho_str}?h={digest}"
            if hasattr(item, "path"):
                item.path = novo
            else:
                item = novo
            novos.append(item)
            carimbados.append(novo)
        config[lista] = novos
    return carimbados


def on_config(config, **kwargs):
    for url in carimba_versao(config):
        print(f"[prisma] versão no cache-buster: {url}")
    return config


def on_page_markdown(markdown, page, config, files, **kwargs):
    caminho = page.file.src_uri
    docs_dir = Path(config["docs_dir"])

    # Verbete pedido por marcador entra antes de tudo: o auto-link precisa
    # enxergar o texto já montado pra não linkar duas vezes o mesmo termo.
    if caminho != "glossario.md":
        markdown = resolve_pedidos_de_verbete(markdown, caminho, docs_dir)

    # O auto-link trabalha no markdown de prosa, e as listagens são montadas
    # depois, a partir do próprio markdown.
    if caminho.startswith(PAGINAS_AUTOLINK) and caminho not in FORA_DO_AUTOLINK:
        markdown, n = autolinka(markdown, caminho, docs_dir)
        _AUTOLINK_TOTAL[caminho] = n

    # Roda em markdown ainda de prosa, antes de qualquer página virar listagem
    # de cards abaixo — senão o "primeiro parágrafo" de uma seção de listagem
    # seria puro HTML de card, que primeiro_paragrafo_de já ignora mesmo, só
    # que aí a seção fica sem popover à toa.
    if caminho != "glossario.md" and not caminho.startswith("mundo/"):
        coleta_paginas(markdown, page.file.url)

    if caminho == "glossario.md":
        coleta_glossario(markdown)
        markdown, total = monta_glossario(markdown)
        barra = monta_barra(
            "termos",
            "Filtrar por termo ou definição…",
            [("categoria", "Todas as categorias", False)],
            alvo=".prg-verbete",
            expandir=False,
        )
        return insere_barra(markdown, barra, '<nav class="prg-az"')

    if caminho == "jogar/regras-de-habilidade.md":
        return acrescenta_regras_dos_grupos(markdown, Path(config["docs_dir"]))

    if caminho == "jogar/condicoes.md":
        corpo = monta_condicoes(Path(config["docs_dir"]))
        return markdown.rstrip() + "\n\n" + "\n".join(corpo)

    if caminho == "origens/index.md":
        markdown, total = monta_listagem_origens(markdown)
        barra = monta_barra(
            "origens",
            "Filtrar por nome ou efeito do traço…",
            [
                ("eixo", "Os três eixos", False),
                ("feitio", "Qualquer tipo de traço", False),
                ("atributos", "Todos os atributos", True),
            ],
            linha3=sorteio("eixo", "Qualquer eixo", "Sortear origem (1d20)"),
        )
        return insere_barra(markdown, barra, '<div class="prg-card')

    if caminho == "racas/index.md":
        markdown, total = monta_listagem_racas(markdown)
        barra = monta_barra(
            "raças",
            "Filtrar por nome, traço, aparência…",
            [
                ("leva", "Todas as levas", False),
                ("atributos", "Todos os atributos", True),
                ("tracos", "Qualquer nº de traços", False),
            ],
        )
        return insere_barra(markdown, barra, '<div class="prg-card')

    if caminho == "bestiario/index.md":
        markdown, total = monta_listagem_bestiario(markdown, docs_dir)
        barra = monta_barra(
            "criaturas",
            "Filtrar por nome, ataque, traço, condição…",
            [
                ("tier", "Todos os tiers", False),
                ("tipo", "Todo tipo de criatura", False),
                ("vulneravel", "Fraca contra qualquer coisa", True),
                ("imune", "Imune a qualquer coisa", True),
                ("faz", "Faz qualquer coisa", True),
            ],
            linha3=slider("ameaca", "Orçamento de encontro"),
        )
        return insere_barra(markdown, barra, '<div class="prg-card')

    if caminho == "habilidades/index.md":
        cards, total = monta_listagem_habilidades(Path(config["docs_dir"]))
        barra = monta_barra(
            "habilidades",
            "Filtrar por nome, efeito, condição…",
            [
                ("grupo", "Todos os tipos", False),
                ("elemento", "Todos os elementos", False),
                ("escala", "Toda escala", False),
                ("arma", "Todas as armas", False),
                ("atributos", "Todos os atributos", True),
                ("alvo", "Todos os alvos", False),
                # Da ficha técnica: as perguntas que se faz no meio do turno.
                ("acao", "Ação e Reação", False),
                ("resolucao", "Toda resolução", False),
                ("alcance", "Todo alcance", False),
                ("area", "Toda área", False),
                ("cooldown", "Todo cooldown", False),
                ("componentes", "Todos os componentes", True),
            ],
            linha3=slider("mana-min", "Mana disponível")
            + '<label class="prg-filtro__desarmado">\n'
            '<input type="checkbox" class="prg-filtro__desarmado-campo"> '
            "Só Dano Desarmado\n"
            "</label>\n",
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
        barra = monta_barra(
            "pacotes",
            "Filtrar por nome, conceito, habilidade da trilha…",
            [
                ("vertente", "Todas as vertentes", False),
                ("armas", "Todas as armas iniciais", True),
                ("atributos", "Todos os atributos", True),
                ("final", "Termina em qualquer coisa", False),
            ],
            linha3=sorteio("vertente", "Qualquer vertente", "Sortear pacote (1d20)"),
        )
        return insere_barra(markdown, barra, '<div class="prg-card prg-card--pacote"')

    if caminho == "equipamento/index.md":
        markdown, total = monta_listagem_equipamento(
            markdown, "../habilidades/index.md"
        )
        barra = monta_barra(
            "itens",
            "Filtrar por nome, técnica, propriedade…",
            [
                ("categoria", "Arma, escudo ou armadura", False),
                ("grupo", "Todos os estilos", False),
                ("familia", "Todas as famílias", False),
                ("tipo", "Todo tipo de dano", False),
                ("chaves", "Todas as propriedades", True),
            ],
            linha3=slider("preco", "Prata disponível", oculta_sem_valor=True),
        )
        return insere_barra(markdown, barra, '<div class="prg-card')

    if caminho == "jogar/regras-de-equipamento.md":
        corpo = monta_regras_de_equipamento(Path(config["docs_dir"]))
        return markdown.rstrip() + "\n\n" + "\n".join(corpo)

    if caminho.startswith("mundo/") and page.meta.get("tipo"):
        return processa_pagina_mundo(markdown, page.meta["tipo"], page.file.url)

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
    # O Bestiário saiu do Livro do Mestre e virou aba própria (2026-08-02). As
    # âncoras `#bes-…` são as mesmas, então o hash é preservado sem mapa.
    "mestre/bestiario": "bestiario/",
    # As duas páginas de regra saíram do Compêndio pro Livro do Jogador
    # (2026-08-27). As âncoras não mudaram, então o hash viaja junto sem mapa.
    "habilidades/regras": "jogar/regras-de-habilidade/",
    "equipamento/regras": "jogar/regras-de-equipamento/",
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
// Sem mapa de âncoras, a página inteira mudou de endereço sem mudar de
// conteúdo (o Bestiário) — aí o hash continua valendo e vai junto.
var alvo = (chave && mapa[chave]) ||
  {destino_js} + (chave && !Object.keys(mapa).length ? location.hash : '');
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
    if _AUTOLINK_TOTAL:
        print(
            f"[prisma] auto-link do glossário: {sum(_AUTOLINK_TOTAL.values())} "
            f"termo(s) em {len([p for p, n in _AUTOLINK_TOTAL.items() if n])} página(s)"
        )

    base = urlsplit(config["site_url"] or "/").path or "/"
    n = escreve_redirecionamentos(Path(config["site_dir"]), base)
    print(f"[prisma] {n} redirecionamento(s) de endereço antigo escrito(s)")

    assets = Path(config["site_dir"]) / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    (assets / "glossario.json").write_text(
        json.dumps(_glossario, ensure_ascii=False), encoding="utf-8"
    )
    (assets / "habilidades.json").write_text(
        json.dumps(_POPOVER, ensure_ascii=False), encoding="utf-8"
    )
    (assets / "mundo.json").write_text(
        json.dumps(_mundo, ensure_ascii=False), encoding="utf-8"
    )
    (assets / "paginas.json").write_text(
        json.dumps(_paginas, ensure_ascii=False), encoding="utf-8"
    )
    (assets / "equipamento.json").write_text(
        json.dumps(_EQUIPAMENTO, ensure_ascii=False), encoding="utf-8"
    )
    print(
        f"[prisma] popover: {len(_glossario)} verbetes, {len(_POPOVER)} habilidades, "
        f"{len(_mundo)} mundo, {len(_paginas)} páginas/seções, {len(_EQUIPAMENTO)} equipamento"
    )
