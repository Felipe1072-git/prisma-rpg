# Prompt — Listagem única de Pacotes (para nova conversa)

Uso: abrir conversa nova neste projeto (`Sistema RPG`), de preferência com **Opus 5** — a
parte de cross-link com Habilidades exige os mesmos julgamentos finos que apareceram na
reestruturação de Habilidades (colisão de nome entre armas, ids globais únicos). Colar o
bloco abaixo como primeira mensagem.

---

Quero fazer com **Pacotes** exatamente o que fizemos com Habilidades na sessão anterior:
consolidar numa **listagem única com filtro facetado**, no mesmo espírito e reaproveitando
a mesma arquitetura já construída em `hooks/prisma.py` e `docs/assets/{css,js}/prisma.css`.

**Leia primeiro:** `CLAUDE.md` (regras do projeto — é proibido inventar conteúdo de jogo
sem consultar) e a memória do projeto sobre `docs/` ser sempre a fonte da verdade (nunca
migrar pra YAML, o hook só transforma pra exibição). Depois leia `hooks/prisma.py` inteiro
— a lógica de Habilidades já resolveu vários problemas que você vai encontrar de novo aqui,
e reaproveitar as mesmas funções é melhor que reescrever.

## O que existe hoje

`docs/pacotes/index.md` (2175 linhas) tem duas partes:

1. **5 seções `## Vertente`** (Campeões do Aço, Senhores do Arcano, Sombras e
   Perdigueiros, Arautos e Devotos, Exploradores e Híbridos), cada uma com uma tabela
   `| d20 | Pacote | Conceito |` de 20 linhas — "role 1d20 pra sortear um pacote dessa
   vertente". As 5 tabelas somam os 100 pacotes.
2. **`## Pacotes Detalhados`** — 100 seções `### Nome do Pacote`, cada uma com:
   - uma linha de flavor em itálico
   - `- **Arma inicial:** [Nome](../jogador/arsenal.md#slug)`
   - `- **Atributo em foco:** Força` (ou composto, ex: "Força ou Agilidade")
   - uma tabela `| Nível | Habilidade |` com 10 linhas (níveis 1,3,5,7,9,11,13,15,17,19):
     os níveis 1/5/9 são sempre `"ArmaNome - Grau"` (Básica/Avançada/Especial daquela
     arma), os demais são nomes de habilidade em texto puro, e o nível 19 quase sempre
     traz uma Suprema — às vezes o nível 13 traz uma "Maior" também.

Todos os 100 pacotes já têm a seção `###` detalhada — não há pacote "só catalogado".

## O que já decidimos (não precisa perguntar de novo)

1. **As 5 tabelas de sorteio saem da listagem** e vão para uma página de referência nova
   — mesmo padrão de `habilidades/regras.md`: conteúdo físico próprio (não uma
   transclusão ao vivo, já que essas tabelas não existem em nenhum outro lugar pra
   duplicar — é conteúdo original, não como Dano Desarmado que sobrevive noutro arquivo).
   Sugestão de nome: `docs/pacotes/sorteio.md`, nav "Sorteio de Pacote" ao lado de
   "Pacotes". **Adicione um botão "Sortear pacote"** na listagem única (com select
   opcional de vertente) que rola 1d20 em JS e abre o card resultante — a mesma função
   da tabela em papel, sem duplicar a lista. Guarde o número do d20 de cada pacote como
   `data-d20` no card (dá pra mostrar como um selo pequeno, tipo "nº 7").
2. **Cross-link da trilha para a Listagem de Habilidades**: cada nome de habilidade nas
   tabelas de nível vira link pro card já existente em `habilidades/index.md`. Duas
   formas na mesma tabela, tratamento diferente:
   - `"ArmaNome - Grau"` (níveis 1/5/9): não é o nome real da habilidade — é preciso
     achar, dentro da seção daquela arma no Arsenal, qual habilidade carrega aquele
     qualificador de grau (reaproveite `extrai_secoes_de_arma` +
     `extrai_blocos_de_habilidade`, já em `hooks/prisma.py`, pra montar um dicionário
     `(arma_slug, grau) -> id_do_card` uma vez só).
   - Nome solto (demais níveis, às vezes com `*(Supremo)*`/`*(Maior)*` no rabo): procure
     por nome exato num dicionário global `nome -> id_do_card` construído a partir dos
     571 cards de Habilidades.
   - **Cuidado com colisão de nome**: a sessão anterior descobriu que "Onda de Choque",
     "Golpe Ascendente" e "Investida Celestial" cada um pertence a **duas armas
     diferentes** (por isso o id do card ganhou prefixo de arma — veja `monta_card` e o
     comentário ao lado do `ident =`). Se um nome solto da trilha bater em mais de um
     card sem contexto de arma pra desambiguar, **não invente qual é o certo** — deixe
     o texto sem link nesse caso específico e sinalize pro usuário quais ocorrências
     ficaram assim.
3. **Filtros da listagem**: Vertente (5), Arma inicial (reaproveita o mesmo vocabulário
   de arma já usado em Habilidades — mesmo `slug()`, mesmo `data-arma-nome`), Atributo em
   foco (reaproveite `computa_atributos()` de `hooks/prisma.py`, já trata "Força ou
   Agilidade"), e **Suprema/Maior final** (a habilidade de nível 19, ou 13 quando for
   "Maior" — um pacote pode ter as duas; considere se o filtro deve cobrir só a de nível
   19 ou ambas, e pergunte ao usuário se não tiver certeza). Mantenha também a busca
   livre por texto, incluindo a trilha inteira no índice de busca (mesmo princípio do
   `data-busca` de Habilidades: "quero achar todo pacote que usa Fluxo" tem que funcionar
   digitando "fluxo" na busca, não só pelo filtro).

## Armadilhas já conhecidas (economize o retrabalho que já tivemos)

- `mkdocs serve` **não recarrega `hooks/prisma.py`** sozinho — pare e suba o servidor de
  novo a cada mudança no hook antes de checar no navegador.
- Nos scripts de verificação em Python no Windows, chame
  `sys.stdout.reconfigure(encoding='utf-8')` antes de imprimir texto com ◈ ou acento, ou
  quebra com `UnicodeEncodeError`.
- `mkdocs build --strict` pega link/âncora quebrado, mas **não pega id duplicado** —
  depois de gerar os cards, rode uma checagem manual de unicidade de `id="..."` (regex +
  `collections.Counter`, igual foi feito pra Habilidades).
- Se a porta 8000 estiver ocupada por outro chat, use a config alternativa
  `prisma-docs-alt` (porta 8011) já em `.claude/launch.json`.
- Ids de card precisam ser globalmente únicos: siga a mesma convenção
  (`hab-{arma-slug}-{slug(nome)}` quando for habilidade de arma, `hab-{slug(nome)}`
  quando não for) — se você inventar um esquema de id novo pra pacotes, ele também
  precisa ser único e estável o bastante pra o cross-link funcionar.
- O painel do navegador às vezes recusa `screenshot` ("not displayed"). Use
  `get_page_text` / `read_page` / `javascript_tool` como verificação principal; screenshot
  só quando o painel já estiver confirmado visível.

## Antes de escrever em `docs/`

Nada aqui é invenção de conteúdo — é reorganização e ferramenta de exibição, igual foi
feito pra Habilidades. Ainda assim, se aparecer qualquer decisão que pareça de conteúdo
(por exemplo: um pacote cuja Arma inicial não bate com nada no Arsenal, ou uma
ambiguidade de nome que precise de escolha), **pare e pergunte** — não resolva sozinho.
Mostre o diff antes de gravar qualquer alteração de conteúdo já existente (mesma regra do
`CLAUDE.md`).

Responda em português.
