# CLAUDE.md

Este arquivo orienta o Claude Code ao trabalhar neste projeto.

## Sobre o Projeto

**Prisma RPG** — sistema de RPG de mesa homebrew autoral, criado por Paulo Souza. É o "D&D definitivo" do autor: um d20 tradicional simplificado, sem classes, focado em liberdade total de construção de personagem.

- **Nome do sistema:** Prisma RPG (nome de trabalho — pode mudar)
- **Versão atual:** 0.2 (sistema jogável de ponta a ponta — ver [Status](#status))
- **Pasta do projeto:** `C:\Users\Paulo Souza\Documents\Sistema RPG\`
- **Repositório:** `https://github.com/Felipe1072-git/prisma-rpg` (remoto `origin`, branch principal `main`)
- **Site publicado:** [felipe1072-git.github.io/prisma-rpg](https://felipe1072-git.github.io/prisma-rpg/) — **todo push na `main` publica**, via `.github/workflows/deploy.yml`

### Inspirações de ambientação/tom

Mushoku Tensei, Sword Art Online, Fabula Ultima, Skyrim, Dragon Age, The Witcher, Diablo, Warcraft, animes em geral, Grand Chase. Mundo autoral — não é nenhuma dessas franquias, é uma fusão de tom e sensação.

## Decisões de Design Consolidadas

Estas são decisões **já tomadas pelo usuário** — não são sugestões, são a base do sistema.

### Sistema Base
- **d20 tradicional**, simplificado.
- **Sem sistema de classes.** Todas as habilidades do jogo estão disponíveis para todos os personagens — quem quiser ser "full mago" pode, quem quiser misturar, mistura. Sem restrições artificiais.
- **Sistema de habilidades**: personagem ganha/escolhe habilidades por nível.
- **Magia e habilidades são a mesma coisa** — não existe um sistema de magia separado. Tudo funciona pela mesma estrutura de habilidades.
- **Tudo baseado em Mana** — o recurso universal para ativar habilidades.
- **Pontos de Ação (◈)** mantidos como no sistema anterior (Diablo RPG).

### Intensidade (I / II / III)

**Não existem "Tiers de Sucesso".** Foram removidos em 2026-07-26 pra simplificar o jogo. O d20 responde só "acertou ou não" (d20 + Atributo vs Defesa); **quão forte** o golpe é já foi decidido pelo jogador ao escolher a Intensidade no momento de ativar:

| Intensidade | PA | Entrega |
|---|---|---|
| I | ◈ (1) | efeito base — normalmente só o dano |
| II | ◈◈ (2) | + efeito secundário (empurrar, Sangrando, Marcado) |
| III | ◈◈◈ (3) | efeito completo (derrubar, Atordoado) |

- O Mana sobe junto com a Intensidade (ver `docs/jogador/mana.md`).
- **Alcance e área nunca escalam** — só o efeito.
- **Crítico (20 natural):** dano máximo + rolagem extra, e **sobe 1 Intensidade de graça**.
- **Custo fixo** (sem Intensidade): áreas de raio 3+, Supremas, buffs sem rolagem.
- **Tiers de Resultado:** exceção rara pra efeitos que não devem ser confiáveis — o d20 gradua falha total / falha recuperável / sucesso. Só `Ressuscitar` usa.

### Sistema de Armas
Cada arma concede acesso a 3 habilidades, em ordem de aprendizado obrigatória:
1. **Habilidade Básica**
2. **Habilidade Avançada**
3. **Habilidade Especial**

O grau **não** define o custo — cada uma tem suas 3 Intensidades. O grau define o quanto a técnica entrega e o custo em Mana: Básica 1/3/6, Avançada 2/5/9, Especial 3/7/12.

### Grupos de Habilidades

Habilidades são organizadas por grupos temáticos (não por classe):

| Grupo | Escopo |
|---|---|
| Habilidades Marciais | Armas corpo a corpo / combate a curta distância |
| Habilidades de Pontaria | Armas à distância e precisão (inclui feitiços de precisão) |
| Habilidades Mágicas por Elemento | Fogo, Gelo, Terra, Sombras, Luz, Raio, Arcano (magia pura, sem assinatura elemental), etc. |
| Habilidades Sociais | Persuasão e afins |
| Habilidades de Infiltração | Furtividade, ladinagem |
| Habilidades de Mobilidade | Voo, deslocamento |
| Habilidades de Buff | Incremento de força, imbuir elementos em armas, etc. |
| Habilidades de Debuff | Desvantagens para inimigos ou em testes |
| Habilidades de Suporte | Cura e apoio a aliados |
| Habilidades de Necromancia | Drenar vigor, amaldiçoar, erguer mortos, gastar a própria vitalidade |
| Habilidades de Projeção Mental | Telepatia, ler mentes, ilusão mental, dano psíquico — funciona em qualquer mente, sem depender de palavras (não confundir com Sociais, que é persuasão via fala/presença) |
| Habilidades de Alquimia de Mana | Mana altera a matéria: endurecer o corpo, transmutar, consertar objetos, imbuir armas |
| Habilidades de Percepção Arcana | Enxergar o invisível, rastrear pelo resíduo de mana, premonição em combate |
| Habilidades de Conjuração | Trazer aliados de outros lugares/planos pra lutar ao seu lado — familiar simples, aliado de combate (ficha própria, turno próprio), vínculo com um Ser maior (ritual, risco real), e o Companheiro Animal (escala com o nível do personagem, não com Mana) |
| Habilidades de Espaço-Tempo | Reposicionar à força, distorcer gravidade e manipular o fluxo do tempo — teleporte, puxar, empurrar, ganhar uma ação extra, refazer um resultado que já aconteceu |

*(Lista pode crescer.)*

### Pacotes

"Pacotes" são kits/sugestões (mais do que meros kits) de Armas + Habilidades para jogar dentro de um arquétipo, inspirados em **Grand Chase**. Importante: **não são classes** — são só um ponto de partida sugerido. Nada impede montar um personagem fora de qualquer pacote.

### Raças

Variadas, no estilo **Daggerheart** e animes em geral. *(Lista de raças: a definir.)*

### Ficha de Personagem

**A foto do modelo do caderno foi descartada** (decisão de 2026-07-26) — a ficha será construída do zero. O método pedido pelo usuário: **pensar elemento por elemento**, um campo de cada vez, discutindo *o que* precisa estar lá e *por quê*, antes de desenhar qualquer layout. Não montar uma ficha inteira de uma vez e apresentar pronta.

## Criação de Conteúdo — REGRAS DE TRABALHO

- **É estritamente proibido inventar regras, mecânicas, nomes, habilidades, raças ou qualquer conteúdo de jogo sem consultar o usuário primeiro.**
- Sempre apresentar a ideia/sugestão e aguardar aprovação explícita antes de escrever em qualquer documento canônico (`docs/`).
- Pode agir de forma criativa nas *sugestões*, mas a decisão final é sempre do usuário.
- Nunca assumir que algo "faz sentido" mecanicamente sem confirmar.
- Sempre usar pop-ups de escolha (AskUserQuestion) para perguntas de sim/não ou múltipla escolha.
- Mostrar diff/preview antes de gravar alterações de conteúdo já existente.

## Estrutura de Arquivos

```
Sistema RPG/
├── docs/                     ← fonte canônica; é o que o site publica
│   ├── index.md
│   ├── jogar/                ← Jogando o Jogo: atributos, testes, combate, mana,
│   │                            dano-e-cura, condicoes, estresse, exploracao
│   ├── criacao/              ← Criação de Personagem: index (5 passos),
│   │                            progressao, tocado
│   ├── habilidades/          ← index.md = listagem única; regras.md = as regras;
│   │                            um arquivo por grupo (a fonte de cada habilidade)
│   ├── racas/                ← index.md = listagem única (25 raças)
│   ├── origens/              ← index.md = listagem única; as 3 tabelas d20 são a fonte
│   ├── equipamento/          ← index.md = listagem (armas/escudos/armaduras) e a fonte
│   │                            de tudo; regras.md monta-se lendo as seções de regra
│   ├── pacotes/              ← index.md = listagem única; sorteio.md = tabelas d20
│   ├── bestiario/            ← index.md = listagem única (aba própria no header)
│   ├── mestre/               ← Livro do Mestre; criando-criaturas.md = as regras
│   │                            de montar criatura
│   ├── glossario.md          ← vira popover ao passar o mouse nos termos
│   └── assets/{css,js,img}/  ← prisma.css, prisma.js, SVGs de brasão/divisor
├── hooks/prisma.py           ← camada de exibição (ver abaixo) — não altera docs/
├── mkdocs.yml                ← nav, tema, extensões
├── .github/workflows/        ← deploy.yml: publica a cada push na main
├── notas/                    ← rascunhos, auditoria, prompts (não publicado)
└── referencia/               ← material de referência pessoal (não publicado)
```

O header tem 7 abas: **Início · Jogando o Jogo · Criação de Personagem · Compêndio ·
Bestiário · Livro do Mestre · Glossário**. Toda listagem filtrável mora no Compêndio —
menos o Bestiário, que ganhou aba própria em 2026-08-02 por ser a página que o Mestre
mais abre no meio de um turno.

⚠ **Toda seção do nav precisa do próprio `index.md` como primeiro item.** Com
`navigation.indexes` ligado, o Material adota o primeiro item da seção como página-índice
dela — e o item **perde o rótulo próprio**, passando a se chamar como a seção. Só arquivo
literalmente chamado `index.md` é adotado; `compendio.md` não servia. Foi assim que
"Habilidades" sumiu do menu por duas fases: era o primeiro item do Compêndio, que não tinha
índice, e virou o próprio "Compêndio". Ao criar seção nova, crie o `index.md` dela junto.

## Site e camada de exibição

**O markdown em `docs/` é sempre a fonte da verdade.** Nunca migrar conteúdo pra YAML,
JSON ou banco: `hooks/prisma.py` roda durante o `mkdocs build` e transforma o markdown
pra exibição, sem escrever nada em disco. Se o hook não reconhecer um bloco, ele fica
exatamente como está — o pior caso é a página continuar igual a hoje.

O que o hook faz:

São **seis listagens**, todas com a mesma carcaça (`monta_card_base`) e a mesma barra
(`monta_barra`) — o que muda é só o extrator que lê o markdown de cada uma:

| Página | O que acontece | Id do card |
|---|---|---|
| `habilidades/index.md` | as 753 habilidades viram cards (grupo, elemento, arma, atributo, alvo, Mana) | `hab-{arma}-{nome}` ou `hab-{nome}` |
| `racas/index.md` | as 24 seções `##` viram cards (leva, atributos, nº de traços); as duas divisórias de leva viram prosa acima da lista | `rac-{nome}` |
| `origens/index.md` | as 3 tabelas d20 viram 60 cards (eixo, tipo de traço, atributo) + sorteio | `ori-{eixo}-{nome}` |
| `equipamento/index.md` | as 62 seções de arma + escudos + armaduras viram 68 cards; a ficha vem da tabela de dado de dano | `equ-{nome}` |
| `pacotes/index.md` | as 100 seções `###` viram cards (vertente, arma, atributo, Suprema final) + sorteio | `pac-{nome}` |
| `bestiario/index.md` | as 52 seções `##` viram fichas no molde do stat block do D&D Beyond (tiles, grade dos 8 atributos, traços/ações em uma linha cada), mais os filtros lidos da ficha e o montador de encontro | `bes-{nome}` |
| `habilidades/*.md` (grupos) | cada habilidade vira um ponteiro de uma linha pro card | — |
| `habilidades/regras.md`, `equipamento/regras.md`, `jogar/condicoes.md` | montam-se lendo ao vivo seções que vivem noutro arquivo — nenhum texto duplicado em disco | — |
| qualquer página | `<!-- prisma:verbetes Vantagem Desvantagem -->` vira os verbetes inteiros, lidos do glossário | — |
| `glossario.md` | cada verbete vira popover ao passar o mouse; a página ganha índice A–Z, filtro por categoria e "Veja também" derivado dos links entre verbetes | o `###` (mantido: 1.400 links dependem dele) |
| `jogar/`, `criacao/`, `mestre/` | a primeira menção de cada termo de regra vira link pro glossário (e ganha popover junto) | — |

Convenções que precisam se manter estáveis (o cross-link depende delas):

- O prefixo do id de habilidade de arma existe porque três nomes são usados por duas
  armas diferentes ("Onda de Choque", "Golpe Ascendente", "Investida Celestial").
- A identidade de uma arma vem da **âncora do link** (`equipamento/index.md#equ-escudo-leve`),
  não do texto — um pacote escreve "Escudo" onde o Equipamento tem o card "Escudo Leve".
- Faceta de filtro: `data-{nome}` no card + um `<select data-faceta="{nome}">` na barra.
  Multivalor leva `data-multi="1"` e rótulos em `data-{nome}-nome` separados por `|`.
  O JS popula os menus sozinho a partir dos cards — não há lista fixa a manter. Faceta
  com ordem própria (tier, couraça, eixo) entra no mapa `ORDEM` do `prisma.js`.
- Slider de orçamento: `slider(campo, rótulo)`. `oculta_sem_valor=True` quando não ter
  valor significa "não se compra" (arma lendária), e não "não custa nada" (Mana).
- Sorteio: `sorteio(faceta, ...)` + `data-d20` no card. Serve pacote e origem.
- **Numa listagem, a lista é o conteúdo**: título → uma frase de orientação → barra de filtro,
  tudo na primeira tela. O "como isso funciona" vai pra um bloco `???` fechado (helper
  `colapsavel()`, ou escrito à mão no markdown). Régua: **até ~60 palavras visíveis** antes da
  barra. O JS abre qualquer `<details>` fechado quando a âncora cai dentro dele.
- **O card mostra o que se usa no turno, venha de onde vier.** Vida, PA e Base saem do Tier
  e aparecem; a **Ação de Lenda** também é do Tier e por isso *não* aparecia — erro corrigido
  em 2026-08-03. O critério não é a origem do valor, é se o Mestre precisa dele no meio do
  turno. Quando a resposta for sim e o texto viver noutro arquivo, injete (é o que
  `regra_da_acao_de_lenda` faz, lendo de `criando-criaturas.md`), não copie.
- **Ficha de criatura é só mecânica**: nada de justificar a regra dentro dela ("Goblin é
  ameaça por quantidade", "osso quebra", "esmaga ou queima"). O card é lido no meio de um
  turno, e comentário ali é ruído. O *porquê* de cada escolha continua existindo — em
  `mestre/criando-criaturas.md`, que é a página que ensina — e o conceito do bicho continua
  na frase em itálico no topo do card. Regra de resolução não é justificativa: "o Mestre rola
  uma vez pro cone inteiro" fica. Mas **exceção que a regra geral já cobre não é regra, é
  ruído**: o "alçar voo custa ◈" do Dragão saiu porque voar já é movimento.
- **As facetas do Bestiário são as perguntas do Mestre, não os campos da ficha.** Couraça e PA
  saíram (a primeira nem aparece no card; a segunda é quase constante dentro do Tier) e
  entraram **Tipo**, **Vulnerável a**, **Imune a** e **Faz o quê** — as três últimas **lidas da
  própria ficha**, sem campo novo: `facetas_de_defesa` varre Vulnerabilidade/Imunidades/
  Resistência contra um vocabulário fixo, e `capacidades_da_ficha` procura marcas de
  comportamento (`**Voo:**`, `[Agarrado]`, `vs Defesa mental`, `cone de`…). Criatura nova entra
  nos filtros sozinha. A exceção que a leitura precisou cobrir: material aparece como
  *"Resistência … exceto de armas de Prata"*, não como Vulnerabilidade — as duas formas caem na
  mesma faceta, porque respondem a mesma pergunta.
- **Montador de encontro** (`iniciaEncontro`, no JS): `+`/`−` em cada card de criatura e um
  painel na barra com total de pontos, **tamanho e nível do grupo**, e o rótulo de dificuldade
  calculado ao vivo. O controle é **criado pelo JS**, não pelo hook — botão dentro do
  `<button>` do cabeçalho é HTML inválido, e sem script a página fica exatamente como era.
  O nível multiplica o **orçamento** (×1 / ×1,8 / ×2,7 / ×3,7 por faixa), não a criatura: a
  ficha vale em qualquer mesa, e 2 Trolls saem de "muito além de Mortal" no nível 1 pra
  "Padrão" no 18.
- **Tile de criatura é faixa de comparação, não frase**: `valor_de_tile` corta tudo o que o
  rótulo já disse — a unidade (`8 casas` → `8`), a contagem repetida (`◈◈ (2)` → `◈◈`) e a
  qualificação (`imune a efeito mental` → `imune`). Valor que não cabe em uma palavra é sinal
  de que ele quer um campo próprio: foi assim que o voo do Dragão virou `**Voo:** 8 casas`
  em vez de um tile de texto comprido. O texto por extenso continua no markdown e nas linhas
  de defesa.
- **Criatura nova segue a forma do markdown, não um template de HTML**: bullets
  `- **Rótulo:** valor` pra ficha (rótulo de `DESTAQUES_CRIATURA` vira tile; o resto vira
  linha de defesa), `**Nome** — ◈ | +X vs Defesa | alvo` pra ataque, `**Nome** *(passiva)*`
  pra traço. Um bullet abaixo do nome sobe pra mesma linha; dois ou mais viram lista
  (é assim que as três Intensidades continuam sendo escolha visível).
- **Traço que a leva concede vale pra raça inteira**: o markdown guarda uma cópia só, na
  abertura da leva, e `monta_card_raca` injeta nos cards daquela leva. Ele conta no número de
  traços do card, porque na ficha do jogador ele é um traço como os outros.
- **Popover**: `on_post_build` grava `assets/glossario.json` e `assets/habilidades.json`;
  o JS liga o popover a qualquer link `…glossario…#termo` ou `…#hab-…`. Habilidade nova
  entra sozinha — o dicionário é montado junto com o card.
- **Auto-link**: só nas páginas de prosa (`PAGINAS_AUTOLINK`) e só nas categorias de regra
  (`CATEGORIAS_AUTOLINK`), pulando `AMBIGUOS_AUTOLINK` e as expressões de
  `GUARDAS_AUTOLINK`. Termo já linkado à mão na página não recebe outro. **Ao mexer nessas
  listas, audite os links gerados um a um** — link errado é pior que link nenhum.
- **Verbete homônimo precisa de âncora explícita**: `### Escudo (item) {: #escudo-item }`.
  Sem ela o segundo vira `escudo_1` (id que depende da ordem do arquivo) e o popover do
  primeiro mostra o verbete errado. O `notas/verifica.py` acusa.

`on_post_build` também escreve as páginas de redirecionamento dos endereços antigos
(`jogador/sistema-d20`, `jogador/pontos-de-acao`, `jogador/mana`, `jogador/introducao`,
`jogador/tocado`), preservando a âncora quando ela tem destino equivalente. Mexer nos
mapas `REDIRECIONA` / `ANCORAS_*` é o que mantém link antigo funcionando.

Ao mexer nisso:

- `mkdocs serve` **não** recarrega `hooks/prisma.py` — pare e suba o servidor de novo.
- **O CSS e o JS levam `?h=<hash>` do próprio conteúdo** (`carimba_versao`, no `on_config`).
  Sem isso o navegador de quem já visitou o site serve a cópia velha do `prisma.css` por até
  10 minutos (`max-age=600` do GitHub Pages) — HTML novo com CSS velho, e a página aparece
  sem estilo. Aconteceu de verdade no deploy do stat block.
- **`--strict` não basta.** Ele pega página inexistente, mas âncora quebrada ele só
  reporta como INFO, e id duplicado ele não vê. Sempre feche com:

  ```bash
  python -m mkdocs build --strict && python notas/verifica.py
  ```

- **Os dois juntos ainda não bastam: olhe a página renderizada.** Erro de *formatação* passa
  por build limpo e por `verifica.py` limpo, porque nenhum dos dois lê o HTML como leitor.
  O caso real: ao reescrever um `!!! cuidado`, a **primeira linha perdeu o recuo de quatro
  espaços** — o parágrafo saiu do bloco, as linhas seguintes viraram **bloco de código**, e a
  página ficou publicada assim por dois commits. **Admonition exige os quatro espaços em
  *todas* as linhas do corpo**, inclusive a primeira. Depois de mexer em `!!!`, tabela, lista
  aninhada ou recuo, abra a página e olhe.
- Ao editar por **script/regex em massa**, imprima o que casou e o que não casou, e confira
  uma amostra no fim. Substituição em cadeia é o risco silencioso: trocar `2d6→3d6` antes de
  `3d6→4d6` faz a primeira troca cair na segunda (aconteceu na reescala das criaturas — dois
  degraus de Intensidade viraram o mesmo dado). **Ordene do maior pro menor.**
- Em script de verificação no Windows, `sys.stdout.reconfigure(encoding='utf-8')` antes
  de imprimir ◈ ou acento.
- **A ficha de uma habilidade só reconhece bullets contínuos — nada mais.** `extrai_blocos_de_habilidade`
  para de ler no primeiro `**Cabeçalho em negrito**` solto ou tabela markdown que aparecer no meio
  do corpo (não é bullet, não é continuação indentada) — e para **sem erro nenhum no build**: o
  resto da habilidade só some do card, ou vira parágrafo solto entre dois cards. Aconteceu de
  verdade em três habilidades de uma leva só (`Corrosão`, `Selar o Pacto`, `Laço de Sangue e
  Pelo`) — a mais grave perdeu a tabela de progressão inteira e a regra de morte junto. Habilidade
  com duas seções (tipo "contra criatura" / "contra objeto") ou uma tabela de valores: dobre tudo
  em bullets `- **Rótulo:** valor` numa escada só (é como `Ressuscitar` já resolve seções
  múltiplas — cada resultado é um bullet, não um subtítulo), nunca um cabeçalho de parágrafo nem
  uma tabela. Depois de escrever, **abra a página e clique no card** — não basta o build passar.

## Convenções de Commit

- `feat:` nova regra, habilidade, pacote ou mecânica
- `fix:` correção de erro ou inconsistência
- `docs:` atualização de texto, revisão ou reorganização
- `refactor:` reorganização sem mudança de conteúdo

## Status

**Versão 0.2 (2026-07-26) — sistema jogável de ponta a ponta.** Publicado em
[felipe1072-git.github.io/prisma-rpg](https://felipe1072-git.github.io/prisma-rpg/), sob CC BY 4.0,
com deploy automático a cada push (workflow em `.github/workflows/deploy.yml`).

O que existe: 579 habilidades — 393 gerais nos 11 grupos mais 186 de arma (62 armas × 3 graus) —,
25 raças, 101 pacotes, 10 elementos com assinatura mecânica própria, sistema Tocado, e Livro do
Mestre em 5 partes (Bestiário, Encontros, Testes, Recompensas, Exploração).

**Auditoria de consistência (2026-07-27).** O sistema foi lido de uma vez como corpo único pela
primeira vez: ~185 achados, corrigidos em seguida. Dez termos que o jogo usava sem nunca definir
entraram no glossário (Derrubado, Vantagem, rodada/cena, empurrar, agarrado, Desprevenido, acúmulo
de bônus, zonas, voo, água). Relatório completo, lições e pendências em `notas/auditoria.md`.

⚠ **~15 decisões de design foram tomadas por mim durante essa auditoria** (marcadas com ⚠ no
relatório) porque a regra não existia e o texto precisava de uma. Já estão publicadas, mas o autor
ainda não as revisou uma a uma — a mais pesada é *bônus planos de buffs diferentes não somam, vale
o maior*. Se ele quiser mudar alguma, é edição pontual.

**Listagens únicas (2026-07-28).** Habilidades e Pacotes deixaram de estar espalhados por várias
páginas: cada um virou uma listagem só, com card colapsável, busca livre e filtro facetado —
mesma arquitetura, descrita em [Site e camada de exibição](#site-e-camada-de-exibição). As páginas
de grupo e o Arsenal continuam existindo com o texto de regra, mas suas habilidades viraram
ponteiros de uma linha pro card. As 5 tabelas de sorteio dos pacotes viraram
`pacotes/sorteio.md`, e a trilha de cada pacote agora linka, nível a nível, pro card da
habilidade correspondente.

**Nada foi testado em mesa.** Todo o equilíbrio veio de cálculo. Relato de jogo real vale mais que
qualquer simulação minha — e vale ainda mais para as regras novas acima, que fecham no papel mas
nunca passaram por uma sessão.

**Reorganização no molde do PHB (2026-07-29) — Fase 1 de 5.** O Livro do Jogador deixou de
ser um monólito: `jogador/sistema-d20.md` (299 linhas com criação + atributos + progressão +
testes + Defesa + Vida + dano + Estresse) e `pontos-de-acao.md` foram divididos em duas seções
no espírito do *Playing the Game* / *Character Creation* do D&D 5.5e — `docs/jogar/` e
`docs/criacao/`. As regras de exploração (descanso, viagem, exaustão, clima, água, luz)
migraram do Livro do Mestre pro do Jogador, porque é o jogador quem as aplica; `mestre/exploracao.md`
virou *Exploração na Mesa* e ficou só com armadilhas, pressão de tempo e o porquê disso importar.
Nenhuma regra mudou — foi recorte, ordenação e texto de transição.

**Fase 2 (2026-07-29) — as quatro listagens novas.** Raças, Origens, Equipamento e Bestiário
viraram listagens facetadas, na mesma arquitetura de Habilidades e Pacotes. `jogador/` deixou
de existir: `origem.md` virou `origens/index.md` e `arsenal.md` virou `equipamento/index.md`
(mais `equipamento/regras.md`, montada ao vivo). O Bestiário separou listagem de regra
(`criando-criaturas.md`). Os ~260 links afetados foram reescritos.

Duas contagens estavam erradas e foram corrigidas contra os cards gerados: eram **571**
habilidades (não 573) e **24** raças (não 25). E uma tabela do Arsenal tinha régua de 5 colunas
pra 4 cabeçalhos — nunca renderizou como tabela no site publicado; agora renderiza.

**Fase 3 (2026-07-29) — glossário consultável.** Os 121 verbetes ganharam índice alfabético
gerado, busca e filtro por categoria (a categoria some da tela quando fica sem verbete visível),
e um **"Veja também"** derivado dos links que os verbetes já faziam entre si — a ligação existia
num sentido só, agora navega nos dois. A fonte continua agrupada por categoria, que é como se lê;
o índice é a outra porta, pra quem já sabe o termo. As âncoras `###` foram preservadas: mais de
1.400 links do site apontam pra elas.

A duplicação que eu esperava cortar era menor do que parecia — os verbetes de arma, grupo e
elemento já eram ponteiros de uma linha. O que havia de real era o **dado de dano de 62 armas,
escrito à mão no glossário e de novo na tabela do Equipamento**: conferi um a um, os 62 batem, e
a checagem virou parte do `notas/verifica.py` pra que continuem batendo.

**Fase 4 (2026-07-29) — hovers.** O popover deixou de servir só o glossário: qualquer link
pra um card de habilidade passa a mostrar chaves, custo, atributo, alvo e o efeito da
Intensidade I sem sair da página — o que torna as trilhas de pacote legíveis sem dez idas e
voltas. O dicionário é gerado junto com o card, então habilidade nova entra sozinha.

O **auto-link** rendeu menos do que eu esperava, e isso é a notícia boa: só **14 links novos
em 7 páginas**, porque a cobertura manual já era alta (1.415 links, 111 dos 121 verbetes).
Ele é deliberadamente tímido — só páginas de prosa, só categorias de regra, primeira
ocorrência, e uma lista de termos ambíguos de fora. Auditando os links gerados um a um, 3 dos
17 primeiros estavam **errados** ("Resistência física" da Vitalidade não é a mecânica
Resistência; "Último Turno" não é o verbete Turno) — daí as guardas de contexto.

Um bug vivo apareceu no caminho: o glossário define **Escudo duas vezes** de propósito (a
condição e o item), e o segundo virava `escudo_1`. Os 3 links de `#escudo` apontavam pra
condição, mas o popover mostrava o item, porque o último lido sobrescrevia o primeiro no
dicionário. Agora o item tem âncora explícita e o `verifica.py` acusa qualquer novo homônimo.

**Fase 5 (2026-07-29) — Livro do Mestre.** O conteúdo já estava bom e no lugar certo (a
exploração saiu na Fase 1, o Bestiário virou listagem na Fase 2), então esta fase foi curta e
quase toda estrutural: o nav ganhou duas seções no molde do DMG — **Criaturas** (Bestiário,
Criando uma Criatura, Montagem de Encontro) e **Conduzindo a Mesa** (Testes, Exploração,
Recompensas) —, e `mestre/index.md` deixou de ser um sumário que repetia o nav pra virar
*O que muda pro Mestre*: as quatro diferenças do sistema, com um roteiro de primeira sessão.

A duplicação real que sobrava era **"role 2d20 e use o melhor", escrito em três lugares** —
glossário, `jogar/testes.md` e `mestre/testes.md` — já com três redações diferentes
("maior/menor" contra "melhor/pior"). Virou marcador `<!-- prisma:verbetes -->`: o glossário é
a fonte, o Livro do Jogador cita o verbete inteiro, e o Livro do Mestre ficou só com o conselho
(*quando* conceder Vantagem), que é o que cabe a ele.

Fica registrado o que o DMG do 5.5e tem e o Prisma não: *Preparando uma sessão*, *Como conduzir
uma sessão*, armadilhas com ficha, e o lado do Mestre do Estresse. **Não escrevi nenhuma delas**
— é conteúdo novo, e conteúdo novo passa pelo autor.

**Bestiário no molde do stat block (2026-08-02).** O Bestiário saiu do Livro do Mestre e
virou aba própria (`docs/bestiario/index.md`; o endereço antigo redireciona preservando a
âncora). A ficha de criatura foi refeita no molde do D&D Beyond: os números de rodada em
tiles, os **oito atributos numa grade fixa** — mesmo os que valem +0, porque é a posição que
deixa comparar duas criaturas sem reler rótulo —, imunidade e resistência logo abaixo, e
traços e ações **numa linha cada** (nome em negrito, meta do ataque em etiqueta, efeito na
sequência) em vez de título mais bullet solto. Lista só sobrevive onde é escolha: as três
Intensidades da Baforada. O markdown é o mesmo, só a exibição.

A **Couraça não aparece na ficha**: ela já está somada na Defesa física (Base + Agilidade +
Couraça), e mostrá-la de novo — em tile, e depois em legenda embaixo do número — fazia
parecer que eram dois valores. Decisão do autor, vendo as duas versões: ficha limpa vale
mais. Ela continua no markdown e no filtro da barra. O custo assumido é que os três efeitos
que **ignoram o bônus de Armadura** do alvo obrigam o Mestre a buscar o valor fora do card.

**Leva 4 — material, exorcismo e possessão (2026-08-03).** A leva que precisou de regra nova
antes das criaturas. Entraram **Stirge, Gnoll, Ogro, Aparição, Fantasma, Hidra e Lobisomem**
(o Bestiário vai a **29**), e com elas três peças de sistema:

- **Material** virou propriedade de arma (`### Material` em *Propriedades de Arma*, que o
  `equipamento/regras.md` monta sozinho — **nenhuma das 68 fichas foi tocada**). A regra:
  material é da arma individual, não do tipo; não se compra, se acha; e **quem declara qual
  material a atravessa é a ficha da criatura**, porque o sistema não tem taxonomia de tipo de
  criatura. Dois materiais, ambos com uso: **Prata** (Lobisomem) e **Aço Consagrado** (Lich,
  que até então resistia aos três tipos físicos sem exceção nenhuma).
- **Possuído** virou condição no glossário. O ponto que a torna jogável: o jogador **continua
  jogando** — pode gastar o turno inteiro e rolar d20 + Vontade contra a Defesa mental do
  possuidor; dano de Luz atravessa o corpo e fere o possuidor; e o corpo a 0 de Vida encerra.
- **Quatro habilidades de Suporte** (Exorcismo, Ver Espíritos, Solo Consagrado, Vínculo
  Guardião), nenhuma exclusiva do Fantasma: o **Exorcismo encerra qualquer controle de ações**,
  então é também a primeira resposta ao Encanto III da Súcubo, que não tinha nenhuma. A trilha
  do **Exorcista** trocou Dissipar por Exorcismo (nível 3) e Aura de Defesa por Solo Consagrado
  (nível 13) — o pacote tinha o tema e nenhuma mecânica dele.

**Reescala pela lore (2026-08-03) — a tabela deixa de reger as fichas.** As 52 criaturas
tinham Vida 8/25/60/180 e nada mais, porque seguiram a tabela de construção à risca. Decisão
do autor: **o conceito manda no número**. Vida, Ataque, Defesas, dano, Movimento e atributos
foram reescritos um a um, ancorados nas proporções do D&D 5e e esticados pra escala do Prisma.

O resultado é a distância que faltava:

| Tier | Vida | Ataque | Defesa física |
|---|---|---|---|
| Comum | 4 (Sprite) – 24 (Enxame) | +2 a +6 | 5 a 15 |
| Treinado | 20 – 60 (Cubo) | +4 a +6 | 5 a 18 |
| Formidável | 55 – 150 (Hidra) | +6 a +8 | 12 a 18 |
| Lendário | 200 (Lich) – **680** (Tarrasque) | +11 a **+16** | 19 a **25** |

O que **não** varia, e é o que o Tier continua regendo: **PA**, se usa **Mana/Intensidade**, e
o custo em **Pontos de Ameaça**. O Tier responde "quanta atenção o bicho merece", não "quanto
de Vida ele tem".

Três coisas mudaram de status junto:

- A tabela de construção virou **andaime declarado** (`criando-criaturas.md`): monta criatura
  nova em trinta segundos, **não descreve** as que existem. E **na ficha o número é o número** —
  as fórmulas (Base + Agilidade + Couraça, 6 + Agilidade) não recalculam ficha pronta.
- Os **Pontos de Ameaça deixaram de ser por Tier**: cada ficha traz o próprio campo
  **`**Ameaça:** N`**, que vira o primeiro tile do card e um **slider de orçamento** na barra
  (arraste pra 8 e a listagem esconde tudo que não cabe num encontro Padrão). A fórmula está
  escrita em *Montagem de Encontro*: **Vida ÷ 10 + dano por rodada ÷ 5**, +2 a +5 quando um
  traço faz mais que dano. Faixas: Comum 2–5, Treinado 5–10, Formidável 15–28, Lendário
  40–100. Um Formidável sozinho já passa do Mortal de um grupo de 4.
- **O nível do grupo multiplica o orçamento, não a criatura** (decisão de 2026-08-03, inverte
  o que estava escrito) — as mesmas proporções da tabela de Vida por faixa, aplicadas do outro
  lado da conta, pra as 52 fichas valerem em qualquer mesa. O orçamento fechado, **para um
  grupo de 4** (divida por 4 e multiplique pelo tamanho real do grupo):

  | Faixa | | Leve | Padrão | Difícil | Mortal |
  |---|---|---|---|---|---|
  | **1–4** | ×1 | 4 | 8 | 12 | **16** |
  | **5–10** | ×1,8 | 7 | 14 | 22 | **29** |
  | **11–15** | ×2,7 | 11 | 22 | 32 | **43** |
  | **16–20** | ×3,7 | 15 | 30 | 44 | **59** |

  A tabela de Vida por faixa sobrou pro caso de querer *aquela* criatura de volta mais séria —
  e aí **sobe a Ameaça junto**, com o multiplicador em ×1, senão o nível conta duas vezes.
  O guarda-corpo contra "29 goblins = Mortal no nível 16" é o limite de 8 criaturas, que já
  existia: **em nível alto se troca de Tier, não de quantidade** (16 pontos são 8 Goblins;
  59 são um Roc).
- A tabela **Vida por faixa de nível** virou proporção: multiplique a Vida da ficha, não troque
  pelo número da coluna.

⚠ Duas armadilhas que essa leva revelou estão registradas em
[Site e camada de exibição](#site-e-camada-de-exibição): **substituição em cadeia** em edição
por script (trocar `2d6→3d6` antes de `3d6→4d6` colapsa os dois degraus) e **admonition sem
recuo na primeira linha**, que vira bloco de código sem o build reclamar.

**Leva 5 — a lista do SRD se esgota, e o Bestiário vai a 52 (2026-08-03).** As 17 que
faltavam: **Kobold** (prepara armadilha antes da luta), **Sprite** (flecha de sono),
**Hobgoblin** (dá ◈ a um aliado — o capanga que melhora os outros), **Gárgula**, **Bárbaro
Enfurecido** (mais forte quanto mais ferido), **Fogo-fátuo** (só magia o fere), **Corujurso**,
**Mantícora**, **Múmia** (a maldição dura até ela ser destruída), **Lobo do Inverno**,
**Wyvern**, **Quimera**, **Oni**, e os quatro Lendários de escala — **Treant** (acorda
Elementais de Terra), **Roc** (sobe 8 casas e solta), **Kraken** (4 alvos agarrados de uma
vez) e **Tarrasque** (engole; sai com 30 de dano por dentro).

**Nenhuma delas pediu vocabulário novo** — foi a primeira leva inteiramente escrita com as
regras existentes, o que é o sinal de que o vocabulário amadureceu.

⚠ **O Formidável ficou inchado: 21 de 52** (Comum 9, Treinado 14, Lendário 8). É onde cabem
quase todos os monstros clássicos. Se houver leva 6, que seja de Comuns e Treinados — é o que
um grupo de nível 1–4 encontra de verdade.

**Os quatro Elementais (2026-08-03)** fecharam a leva 4 e levaram o Bestiário a **35**. Cada um
encarna a **assinatura mecânica que o elemento já tinha nas habilidades** — Fogo queima, Água
**puxa**, Vento **empurra**, Terra prende (Lento/Imóvel/Terreno Difícil) —, então nenhum efeito
novo foi inventado: a ficha é a regra do elemento em forma de bicho. As vulnerabilidades formam
um ciclo que se ensina em uma frase: **Fogo cai pra Água, Água pra Raio, Terra pro Vento, Vento
pra Terra**. Usam **Vento**, não "Ar" — o nome do elemento no jogo.

A habilidade **Petrificar** (Terra) foi reescrita na condição nova, escada inteira: II sobe
**1 grau**, III sobe **2 graus**, e o Crítico dá **+1 grau** e sobe 1 Intensidade. Em um
disparo isolado o efeito sentido é o mesmo de antes (grau 1 = Lento, grau 2 = Imóvel), mas
agora **persiste e acumula** entre usos — só sai com cura ou descanso longo. Decisão do autor,
tomada sabendo o custo: é mudança de potência, não de vocabulário. Duas consequências que caem
na mesa junto: petrificar **de verdade** um inimigo o deixa **resistente a dano físico** (grau
3), o que pode atrapalhar o próprio grupo; e o alvo a 0 de Vida no grau 3 **morre de vez**.

**Petrificado** entrou logo depois, fechando a última lacuna que travava criatura — e
**Basilisco e Medusa** saíram junto (o Bestiário vai a **31**), com o mesmo olhar dividido em
dois papéis: ele escala num alvo só (Intensidade III sobe 2 graus), ela pega **todo mundo que
a estiver vendo** por custo fixo e depois atira nas estátuas com Vantagem. Os dois trazem a
mesma cláusula de contra-jogo — **desviar o olhar** dá imunidade ao Olhar e Desvantagem em
todos os ataques do personagem enquanto durar. Acumula em **graus** como o Exausto — 1 Lento, 2 Imóvel, 3 pedra
—, porque uma condição que tira o personagem do jogo de uma vez só não dá ao grupo chance de
reagir. Remove 1 grau por **habilidade que cure Vida** (a Intensidade não importa: o que
quebra a pedra é vida entrando) ou por descanso longo. No grau 3 o corpo resiste a dano
físico, mas **cair a 0 ali mata de vez** — sem Caído, sem Ressuscitar.

⚠ **A contagem de habilidades no site estava defasada em 5** antes desta leva: dizia 571 e os
cards gerados eram 576. Agora são **580** (394 gerais + 186 de arma), conferidos contra o DOM.
Ao acrescentar habilidade, confira o contador da listagem — ele é a fonte, não o texto.

**Leva 3 — os Lendários, e o Bestiário vai a 22 (2026-08-03).** O Tier que estava vazio
ganhou quatro: **Dragão Vermelho Adulto** (a escada do Filhote), **Lich** (o Filactério
transforma o chefe em missão, e *Chamar os Mortos* invoca os Esqueletos e Zumbis que o
Bestiário já tem), **Vampiro** (fraquezas investigáveis: sol, convite, água corrente, estaca)
e **Golem de Ferro** (Fogo o **cura**, Raio o parte, e é imune a todo controle de posição).
Quatro e não seis porque cada ficha Lendária tem o tamanho de três Comuns.

A **Ação de Lenda entrou nas fichas** — e a régua ganhou um ajuste no caminho. Eu tinha
deixado de fora alegando "regra do Tier não se repete no card", mas o card já mostra Vida 180
e PA 5, que também vêm do Tier: o critério não é *de onde o valor veio*, é **se o Mestre
precisa dele no meio do turno**. Ela precisa — é uma ação a mais por rodada. A regra continua
morando uma vez só em `criando-criaturas.md`, e `regra_da_acao_de_lenda` injeta a primeira
frase dela em todo card Lendário, fechando a lista de Ações como no D&D Beyond. Mesmo arranjo
do traço de leva das Raças, e o próximo Lendário já nasce com ela.

Fica **em aberto**: um Lendário custa 30 Pontos de Ameaça contra os 16 de um encontro Mortal
para 4 PJs — nenhum deles é encontro justo em nível 1–4, e isso não está escrito em lugar
nenhum de *Montagem de Encontro*.

**Leva 2, e o Bestiário vai a 18 (2026-08-03).** **Falcão-de-sangue** (ameaça aérea barata),
**Bugbear** (alcance 2 casas, +2d8 contra Desprevenido), **Cubo Gelatinoso** (engole),
**Mímico** (a sala é a armadilha), **Súcubo** e **Gigante da Colina** (arremessa personagem).

Duas primeiras vezes que valem registro: o **Cubo tem ◈ (1)**, a primeira criatura a usar a
cláusula que a regra nova de PA abriu — agir uma vez por rodada virou traço de bicho lento —,
e o **Encanto da Súcubo rola contra a Defesa mental**, que até então era um número que toda
ficha trazia e nenhuma criatura usava. De quebra ela é inútil contra os cinco imunes a efeito
mental (Esqueleto, Zumbi, Slime, Carniçal, Cubo), o que dá contra-jogo interno ao Bestiário.

**Bestiário vai a 12 criaturas (2026-08-02).** A leva 1 saiu da lista do SRD em
`notas/bestiario-elenco.md`, escolhida por lacuna mecânica — cada uma resolve um problema que
o Bestiário não sabia fazer: **Zumbi** (não cai), **Enxame de Ratos** (arma não resolve,
divide a casa), **Orc** (avança e pune quem recuou), **Carniçal** (Atordoado por ◈◈◈ — tira o
turno), **Sombra** (incorpórea, drena Força) e **Troll** (regenera; só Fogo encerra). Números
derivados da tabela de construção, nenhum importado do SRD.

Duas coisas que o vocabulário existente forçou, e valem pra próxima leva: **não existe
"Paralisado"** (o Carniçal usa Atordoado) e **não existe dano de "Ácido"** (o Troll morre só
pra Fogo). Ao converter criatura do SRD, confira o glossário antes — nome de condição de
outro sistema não entra.

**PA das criaturas sobe um degrau em cada Tier (2026-08-02).** Comum **2** (move e ataca —
agir uma vez só virou traço de bicho lento, não regra do Tier), Treinado **3** (os mesmos de
um personagem), Formidável **4**, Lendário **5** + Ação de Lenda. Decisão do autor.

Isso **dobra a economia de ação dos capangas**, e o orçamento de encontro foi reajustado
junto: Pontos de Ameaça viraram Comum 2 / Treinado 4 / Formidável 10 / Lendário 30, o que
preserva o mapeamento antigo (Leve = aquecimento, Padrão = combate de verdade, Difícil =
empate mortal) com metade dos corpos. Os quatro exemplos prontos foram refeitos pra fechar
no novo orçamento, e a janela "4/8/12 goblins" virou "2/4/6". **Nada disso foi testado em
mesa** — é a mesma aritmética de antes, com o número novo.

**Movimento das criaturas (2026-08-02).** Todas as fichas passaram a trazer o campo, em
**6 + Agilidade**. *Criando uma Criatura* ainda dizia "3 + Agilidade", de antes da mudança da
regra — corrigido. O Dragão tinha 5 no chão / 8 voando e um "alçar voo custa ◈"; as duas eram
exceções que a regra de Voo já cobre (voa-se em três dimensões pelo mesmo custo de Movimento,
sem velocidade separada e sem pedágio de decolagem). Ficou **8 casas, no chão ou voando**.

**Iniciativa = d20 + Agilidade + Sorte (2026-08-02).** Era só Sorte. Mudança pedida pelo
autor; as seis criaturas do Bestiário e a Aranha de exemplo foram recalculadas (Sorte é 0 em
todas, então a Iniciativa virou a Agilidade delas: Lobo +2, Slime -2). Empate resolve por
Agilidade, depois Sorte, depois o Mestre. Fica registrado que a Agilidade era o atributo mais
carregado do jogo antes disso (Defesa física, Movimento, ataques à distância e furtivos) e
ganhou mais um — não foi testado em mesa, como nada aqui.

A página de redirecionamento passou a **preservar o hash** quando o endereço muda mas o
conteúdo não (o caso do Bestiário): sem mapa de âncoras, `#bes-goblin` viaja junto. Com
mapa, o comportamento é o de antes.

**Espaço-Tempo vira grupo próprio (2026-08-18).** Não era um elemento como os outros —
reposicionar não é uma assinatura de dano elemental, é um verbo diferente. Saiu de dentro de
Mágicas por Elemento (que cai pra **10 elementos**) e virou o 11º grupo de habilidades, com
página própria (`docs/habilidades/espaco-tempo.md`). Três habilidades que já eram
tematicamente de espaço/tempo mas moravam em Buff e Debuff por acidente de histórico
migraram junto: **Reverter o Instante** (Buff — rebobina um teste de d20), **Antigravidade**
e **Fenda Dimensional** (Debuff — gravidade e portal, ecoando Peso das Trevas e Fissura
Dimensional que já eram do grupo). Decisão do autor: **não existe dano do tipo Espaço-Tempo**
— as 11 habilidades do grupo que causavam "Dano: Espaço-Tempo" passaram a causar **Dano:
Arcano**, e as duas migradas de Debuff, que já eram Arcano, ficaram como estavam.

**Filtro de habilidades: Dano vira faceta universal, e entra a faceta Escala (2026-08-18).**
O tipo de dano só virava faceta filtrável dentro de Mágicas por Elemento, atribuído pela
seção `## Elemento` — fora dali (Buff, Debuff, Suporte, Espaço-Tempo etc.), o campo
`**Dano:** Arcano` que a própria habilidade já declara nunca chegava ao filtro. Agora
`elemento_do_campo_dano` lê esse campo em qualquer card sem elemento explícito e usa o
valor quando bate com um dos 11 tipos conhecidos — sem mudar nada dentro de Mágicas por
Elemento, que continua atribuindo pela seção. Entrou também o dropdown **"Toda escala"**,
juntando o grau de arma (Básica/Avançada/Especial) com a potência geral da habilidade
(Menor/Médio/Moderado/Maior/Supremo) numa faceta só, em ordem de progressão — o atributo
`data-grau` existia desde sempre mas nunca tinha select nenhum ligado a ele.

**Auditoria dos 68 Supremos, e três pares de gêmeos corrigidos (2026-08-18).** Todo Supremo
do jogo custa exatamente ◈◈◈ + 16 Mana, sem exceção — o que torna qualquer comparação de
payoff justa ponta a ponta. A auditoria (script que lê `extrai_blocos_de_habilidade` direto
do hook, não leitura manual) achou:

- **Erradicação, Queda Celestial e Nascimento das Lâminas** (Marciais) eram clones —
  "2d8 em área + só derruba", nada mais, enquanto todo outro Supremo de área do jogo soma
  status extra ou já acerta o campo de batalha inteiro. Cada uma ganhou identidade própria
  puxando do próprio flavor text: Erradicação vira 2x dado + Atordoado
  (a mais contundente); Queda Celestial passa a acertar **todos os inimigos à vista** (a
  descrição já dizia isso, a mecânica não); Nascimento das Lâminas vira dano automático em
  3 aplicações com o golpe final dobrado, combinando com "cortando repetidas vezes antes de
  um golpe final". De quebra, as três (que diziam `Dano: usa o dado de dano da arma
  equipada` e travavam o resultado em `2d8` fixo) passaram a escalar de verdade com a arma
  (`2x dado de dano`), como Divisão Espacial já fazia.
- **Reflexos Extras e Ação Extra** (Marciais) pagavam ◈◈◈ pra ganhar ◈◈◈ de volta — conta
  zerada no próprio turno. Ação Extra saiu do jogo (Reflexos Extras, que dá um turno
  completo, já cobria o mesmo papel e mais); Reflexos Extras passou a custar 0 PA + 16 Mana,
  e perdeu o requisito de "só na primeira rodada" — não fazia mais sentido com o PA de graça.
- **Golpe Sagrado** (Luz) era cópia mecânica exata de Luz Infinita — mesmo Acerto, mesmo
  Crítico, só a forma da área mudava. Virou a única Suprema **dano + cura** do jogo (inimigos
  na área sofrem 2d8, aliados recuperam 2d8), no molde que Redenção e Couraça Angelical já
  usam. **Poder Dinâmico** (Buff) era a versão estritamente pior de Liberação de Poder (mesmo
  bônus de dano, números menores) — trocou de eixo, agora estende a duração das condições
  negativas que as habilidades do usuário aplicarem, em vez de somar dano. **Império
  Sombrio** (Sombras) copiava a base de Dia do Julgamento (1d8 automático × 3) — ganhou
  dreno de vida, puxando pro verbo que Sombras já usa em alvo único (drenar) e nunca tinha
  em área.

O total do jogo cai de 580 pra **579 habilidades** (393 gerais + 186 de arma) com a saída da
Ação Extra — primeira habilidade removida do jogo, não só renomeada ou movida.

**Isekai — 4ª leva de raças, "Raças Exóticas" (2026-08-19).** O Bestiário e o Arsenal já tinham
levas próprias; as Raças ganharam a quarta, pensada pro personagem do jogador Café. Diferente das
levas anteriores (Animal, Peixe/Água), essa não parte de um tronco compartilhado — é uma leva de
origens singulares, e o Isekai é só a primeira a entrar nela. A raça é **a segunda exceção** à
regra de traço físico inconfundível (a primeira é o próprio Humano): passa por humano de
propósito, porque é gente comum de outro mundo, não uma linhagem visualmente distinta. O traço
racial, **Armadura de Roteiro**, transforma um 1 natural em 20 natural 1x por descanso longo
(aplica o [Crítico](docs/jogar/testes.md:24) normalmente e não marca Estresse da falha) — decisão
do autor, que pediu explicitamente a virada mais extrema possível em vez de uma rerolagem comum.

**Pacote MCP — arco JARVIS→Visão fechado (2026-08-19).** O pacote que ficara em aberto na entrada
do Isekai ganhou as 10 Habilidades da trilha, revisadas uma a uma com o autor e o jogador Café.
Não trava no Isekai — qualquer personagem pode pegá-lo. Três fases: **Percepção Arcana** (níveis
1-5, só informa — revela Defesas exatas, vira banco de dados permanente de conhecimento, avisa o
grupo antes de uma emboscada), **Suporte** (7-13, passa a ajudar de verdade — bônus de ataque que
escala, Escudo, remove Estresse em cena pela primeira vez no jogo, marca alvos em área), e
**Conjuração** (15-19, a IA ganha corpo) — que reaproveita o sistema de **Aliado de Combate em
três graus** que Servo de Cinzas/Lâmina Espectral/Guardião do Pacto já tinham, em vez de inventar
mecânica nova pro clímax: Corpo Provisório (Menor) → Iteração Avançada (Médio) → Encarnação
(Maior). Fica registrado o pacote em si — `docs/pacotes/index.md` — como o **101º**, de propósito
fora das 5 tabelas de sorteio (é específico demais pra sair de uma rolagem aleatória).

Duas decisões do autor viraram regra geral, não só desse pacote:

- **Nunca dupla restrição numa habilidade** — Mana já é o freio; se precisa ser mais rara, sobe o
  Mana, não empilha "1x por descanso longo" em cima. Corrigido também no Servo de Cinzas e na
  Chamar Lâmina Espectral existentes (Intensidade III de todo Aliado de Combate Menor/Médio agora
  dura até 0 de Vida, sem limite de cena, em vez de um número fixo de rodadas).
- **Comando Extra** — todo Aliado de Combate (exceto o Guardião do Pacto, que é Custo fixo) agora
  pode agir uma vez a mais na rodada se o usuário pagar ◈ (1 PA) + a Mana da própria Intensidade I
  dele, mesmo com o PA do Aliado já esgotado. Vira regra compartilhada no parágrafo de abertura do
  grupo, não repetida em cada habilidade.

⚠ **A contagem de habilidades estava defasada de novo** — o texto dizia 579, o contador ao vivo da
listagem (a fonte, não o texto) já marcava 754 antes mesmo dessas 10 entrarem, e ninguém tinha
atualizado o número. Corrigido pro valor real, mas a causa da defasagem (o quê exatamente foi
adicionado entre 579 e 744 sem registro) não foi investigada — só o sintoma.

⚠ **Uma tabela markdown aninhada dentro de um bullet quebrou o parser da habilidade** — a própria
skill já avisava disso ("para no primeiro... tabela markdown que aparecer no meio do corpo"), e
mesmo assim escrevi a escala de nível dos três Aliados como tabela na primeira tentativa. O card
truncava silenciosamente sem erro de build. Corrigido pro molde de bullets-escada que o
Companheiro Animal já usava (`**Progressão — nível X–Y:** Vida N, Ataque +N...`) — **abrir a
página e clicar no card continua sendo o único jeito confiável de pegar isso.**

**Camada A das duplicatas — os 12 grupos de clones literais (2026-08-26).** O autor pediu pra
enxugar habilidades repetidas. O levantamento saiu por script, lendo com o próprio
`extrai_blocos_de_habilidade`, e separou o problema em três camadas: **A** — escada, números e ficha
idênticos, muda só nome e flavor (12 grupos, 14 habilidades sobrando); **B** — mesma escada com
alvo/área diferente (35); **C** — mesmos verbos de regra, redação diferente (155). A camada C é a que
pega pares como *Pacto de Sangue* / *Aumento Sombrio*, que nenhuma comparação de texto acha. Relatório
completo e o que sobrou em `notas/duplicatas.md`.

A Camada A foi fechada caso a caso: **1 exclusão e 15 reformulações**, mais 14 habilidades tocadas
fora dela — porque ler cada grupo inteiro antes de escrever revelou que o problema era maior que os
pares. O jogo vai de **754 pra 753** habilidades.

O padrão que resolveu quase todos os casos: **o flavor já dizia o que a regra deveria fazer, e não
fazia**. *Explosão de Fogo* prometia empurrar e não empurrava (agora arremessa e causa dano de queda);
*Rajada Sombria* dizia "mira automaticamente" e ainda exigia teste (agora acerta sem rolar, com dado
menor); *Correntes de Água* prendia os pés e só puxava (agora ancora o alvo a 2 casas); *Espinhos de
Sangue* brotavam do chão e explodiam na hora (agora esperam quem passar).

Quatro grupos estavam quase inteiros construídos sobre uma habilidade só, e isso só apareceu ao ler
cada um por completo: **Fogo** tinha 19 de 36 no molde "área + Queimando"; **Água**, 5 de 8 na escada
`puxa 1 → puxa 2 + Lento → puxa 3 + Lento + derruba`; **Espaço-Tempo**, 7 de 18 em `teleporta 2 →
teleporta 4 → teleporta 4 + Atordoado`; e **Arcano**, 4 de 6 em "empurra + derruba".

Três decisões do autor viraram regra além da própria ficha:

- **Reposicionamento forçado passa a Teste de Resistência** (vs Fortitude Mágica do usuário) — não se
  *esquiva* de uma dobra do espaço. Sete habilidades de Espaço-Tempo mudaram de resolução, e resistir
  significa **ficar onde está, sem as condições, levando metade do dano**. O parágrafo de
  `habilidades/regras.md` que orienta quando usar cada resolução foi ajustado no mesmo lote, ganhando
  o segundo caso — senão o livro contradiria os cards.
- **Aura de Intensidade III pode ser permanente**: as duas auras novas (*Chama Espelhada* e *Descarga
  Carregada*) duram 4 rodadas com cooldown herdado menor, então mantê-las ligadas é possível pagando
  Mana de novo. O freio é o Mana, não o cooldown.
- **Cooldown continua não se escrevendo** — vem da escala (`ESCALA_COOLDOWN`). Nenhuma das 753
  declarava um; *Explosão de Fogo* é a primeira, com 2 rodadas por acumular área + Queimando + derruba
  + dano de queda.

⚠ **Lore importada e termo inexistente são o mesmo defeito.** Três habilidades de Sombras (*Libertação
Limitada*, *Extermínio*, *Apocalipse*) descreviam um **"selo"** que o Prisma nunca definiu — veio do
Dio, do Grand Chase. O autor leu e não entendeu; o flavor das três foi reescrito sem tocar na mecânica
de duas delas. Na mesma leva eu escrevi *"Ignora cobertura"* numa reformulação, e **cobertura também
não existe** no jogo — o termo correto é *linha de visada*. Antes de gravar uma ficha, confira no
glossário cada termo não-óbvio que ela usa.

⚠ **A auditoria de 2026-07-27 já tinha achado parte disso.** O item ELE-31 lista *"Força de Choque =
Descarga Carregada; Voragem = Libertação Limitada; Vórtice das Trevas = Frenesi Sombrio; 3 investidas
de Fogo idênticas"* — e nada tinha sido corrigido em treze meses. Achado que não vira tarefa não vira
correção.

Duas condições saíram do limbo: **`Silenciado`** estava definido no glossário e era aplicado por
*nenhuma* habilidade — o *Abraço das Profundezas*, agora afogamento, é a primeira a usá-lo. E o
`Desprevenido` foi descartado numa proposta por só valer na primeira rodada de combate. Vale varrer o
glossário atrás de outros termos órfãos.

Duas renomeações: *Libertação Limitada* → **Fauce do Abismo**, e *Etiqueta do Mordomo* → **Golpe
Emprestado**, que também mudou de grupo (Debuff 74 → 73, Conjuração 13 → 14) — o conceito é invocar
algo que golpeia, e Conjuração não tinha nenhuma invocação instantânea.

**Área vira Teste de Resistência (2026-08-26).** Decisão do autor, logo depois da Camada A: efeito
que acerta todos numa área **não é mirado em ninguém** — quem está lá se protege como pode. A
convenção é a mesma do D&D 5e, e o levantamento mostrou que o custo que eu esperava (mais rolagens
na mesa) **não existe**: `habilidades/regras.md` já mandava rolar um teste por alvo. O que muda é a
mão que rola — e, quando é o Mestre quem solta a área, **cada jogador rola a sua** em vez de o Mestre
rolar quatro vezes sozinho.

Três decisões de sistema saíram daí:

- **O número-alvo é o Atributo de lançamento, cru** — Magia pra magia, Ataque pra golpe marcial. A
  regra antiga mandava rolar contra a "Fortitude do usuário", o que quebrava nas **33 áreas marciais**:
  a Defesa do guerreiro passaria a medir quão difícil é resistir ao golpe dele. De quebra isso limpa um
  duplo sentido antigo — "Fortitude" era usada como número do **defensor** no glossário (`+53 vs
  Fortitude Mágica`, no Bestiário) e como número do **usuário** na regra de resistência, a ponto de o
  hook ter código só pra colar "do usuário" no rótulo e as duas leituras não se confundirem.
- **O Crítico troca de lado junto com o dado.** Num Teste de Resistência quem rola é o alvo, então é
  ele quem critica: rolando dentro do próprio limiar, **escapa por completo** em vez de sofrer metade.
  Por isso habilidade resistida **não traz bullet de Crítico** — 130 bullets saíram. A alternativa
  ("falha crítica do alvo") foi descartada pelo autor: colidiria com o limiar de Crítico, que é de quem
  rola, criando duas regras de crítico disputando o mesmo d100.
- **Resistir dá metade do dano e nenhuma condição**, no mesmo molde já usado no reposicionamento.

**Com que atributo se resiste** não vem do elemento, vem do que o efeito exige — e a ficha declara,
então ninguém julga isso no meio do turno: Agilidade (sair da frente), Defesa (o corpo aguenta),
Sanidade (a mente aguenta), Social (a vontade dobrada por voz ou presença), Magia (a realidade
alterada em volta). **A Sanidade sai do limbo**: alimentava só o Estresse Máximo e não decidia teste
nenhum; agora é a defesa contra Projeção Mental e medo.

O escopo final foi bem maior que as 136 áreas previstas — **177 fichas**: 135 áreas viraram
resistência, 6 que estavam na lista **não deviam ter teste nenhum** (zonas automáticas que o filtro
não reconhecia), 21 habilidades de alvo único foram uniformizadas pro vocabulário novo, 12 perderam
o Crítico que a regra nova contradizia (4 delas do reposicionamento, gravado horas antes), e 15
ataques de criatura do Bestiário passaram de `+53 vs Evasão` pra `resistir com Agilidade vs 53`.

⚠ **Dois blocos precisaram de julgamento por efeito, não por elemento.** Em **Gelo**, o que a
habilidade faz é fechar o gelo no corpo (Lento → Imóvel), então 6 das 7 resistem com Defesa — a
exceção é a *Investida Encadeada*, que agarra e puxa em vez de congelar. Em **Sombras**, a Zona
Amaldiçoada **já é automática por regra** (o glossário diz que quem entra ou termina o turno nela
sofre, sem teste), então o teste nunca foi sobre a zona: é sobre o golpe inicial, e 20 das 21 resistem
com Agilidade — a exceção é a *Fauce do Abismo*, que drena.

⚠ **Três classificações são julgamento meu e o autor ainda não revisou**: *Metamorfose Forçada* e
*Toque Suspenso* ficaram em **Defesa** (o corpo resiste a ser remodelado, o efeito adormecido age por
dentro), e *Dominar os Mortos* ficou em **Magia** e não Sanidade, porque mortos-vivos são imunes a
efeito mental — Sanidade ali não teria contra o que rolar.

⚠ **`git checkout -- <pasta>` pra reverter uma edição em massa leva junto o que já estava certo
naquela pasta.** Ao desfazer a primeira tentativa das 141 fichas rodei `git checkout -- docs/habilidades/`,
e isso apagou as três edições que eu já tinha feito em `habilidades/regras.md` — a regra publicada ficou
contando a história antiga ("contra a Fortitude do usuário", dois casos de uso, sem o Crítico) enquanto
as fichas contavam a nova. **Build e `verifica.py` passaram limpos**, porque nenhum dos dois lê coerência
entre páginas; quem pegou foi o autor, perguntando se a regra do Crítico tinha entrado. Reverta por
arquivo, ou reaplique as regras depois de qualquer checkout de pasta.

⚠ A edição em massa achou duas armadilhas antes de gravar, nas duas amostras que conferi: o campo
existia como **`**vs:**` minúsculo** em ~10 fichas de Debuff (o hook aceita os dois, meu regex não), e
várias habilidades **já declaravam o teste dentro do texto** ("um teste de Magia contra a Fortitude
Mágica"), o que contradizia o bullet novo. A segunda virou regra do script: **quando o corpo já diz o
atributo, ele manda na heurística**.

**Camada C, bloco 1 — o clichê marcial (2026-08-26).** O maior cluster de colisão de assinatura era
**23 habilidades "dano + empurra + derruba"**, espalhadas por Marciais, Pontaria, Debuff, Arcano e
Vento — onde a única variação era **quantas casas empurra** (1, 2, 3, 5, 6, 7). *Grande X*, *Esmagador*,
*Disparo Voraz* e *Tornados Gêmeos* eram a mesma habilidade; *Mordida*, *Arrasador* e *Tiro
Concentrado* também.

⚠ **A causa não era escrita preguiçosa, era uma lacuna de sistema: os três tipos de dano físico não
têm mecânica nenhuma.** O glossário define Cortante como "Espadas, machados, foices, garras" e para
aí — Impacto e Perfurante idem —, enquanto os 10 elementos têm uma tabela inteira de Assinatura (Fogo
consome, Gelo trava, Raio rouba a ação). Sem verbo próprio no lado físico, toda habilidade marcial
caiu no único disponível. **A lacuna continua aberta** — dar assinatura a Cortante/Impacto/Perfurante
foi oferecido e o autor preferiu distribuir à mão desta vez.

Das 23, **15 tinham justificativa e ficaram**: empurrar **é** a assinatura do Vento; Arrasador e Disparo
Voraz já foram decididos na Camada A como o empurrão forte e a versão barata; *Pressão Brutal* tem
"um empurrão bruto" no próprio flavor; e as marciais restantes têm combo de vários golpes, lançamento
ao ar ou reposicionamento do usuário como identidade.

As **8 restantes** ganharam verbo próprio, tirado da arma que o próprio flavor nomeia — foice puxa,
espada sangra, peso atordoa: *Giro Audaz* (puxa), *Mordida* (Sangrando + Desvantagem), *Confete
Explosivo* ([Cego](docs/glossario.md)), *Tornados Gêmeos* (Sangrando em área), *Grande X* (Marcado —
o único de Marciais que abre o alvo pros aliados), *Esmagador* (Lento → Atordoado), *Tiro Concentrado*
(dano dobra se o usuário não gastou Movimento) e *Rajada Sangrenta* (o Sangrando reabre toda vez que
o alvo se move).

O cluster caiu de **23 para 15**, e a Camada C de **155 para 141** colisões. Debuff e Pontaria saíram
dele por completo.

⚠ **Nem toda colisão de assinatura é defeito** — foi o que tornou a Camada C tratável. Os outros dois
clusters do topo são **assinatura funcionando**: `área + dano + Queimando` (22) é o Fogo sendo Fogo, e
`área + dano + duração` (22) é a Zona Amaldiçoada de Sombras. Só se mexe onde **nenhum elemento manda
no verbo**.

⚠ *Tiro Concentrado* quase ganhou "ignora Escudo e Resistência" — que é exatamente a **Força Perfeita**,
reformulada horas antes na mesma sessão. Ao desenhar habilidade nova, cheque o que a própria leva já
criou, não só o que existia antes dela.

**Camada C, bloco 2 — o par que abriu a revisão, e a escala do d20 que ficou pra trás
(2026-08-26).** *Pacto de Sangue* (Sangue) e *Aumento Sombrio* (Necromancia) eram a mesma ideia —
pagar Vida por bônus de dano — em dois grupos. E um era **estritamente pior**: o Aumento cobrava o
dobro da Vida (3×3d4 empilhado) pra entregar menos bônus (+12 contra +14) por menos tempo. Mesmo
defeito do *Poder Dinâmico* contra a *Liberação de Poder*, corrigido em 2026-08-18.

A separação veio do verbo que **cada grupo já declara**: Sangue "troca Vida por poder" — a própria;
Necromancia abre com "**drenar vigor**" — a dos outros. O Aumento Sombrio passou a **drenar de um
alvo** (1d6/2d6/3d6, Teste de Resistência vs Defesa) em vez de custar a própria Vida, e o Pacto de
Sangue ficou como o único que paga com o próprio sangue. *Flor Carmesim* não precisou de nada — aura
de dano com custo de Vida **por turno** já era distinta.

⚠ **A migração pro d100 deixou os bônus planos pra trás, e ninguém tinha notado.** Observação do
autor: "+1 ou +2 de dano é insignificante nos valores do d100; quando o sistema era d20 fazia
sentido". O levantamento confirmou: das **9 habilidades com bônus plano de dano**, **7 ainda usavam
+1/+2/+3** — só o Pacto de Sangue tinha sido reescalado. A incoerência que provava o diagnóstico: os
buffs que dão **dados** já entregavam mais que os planos (*Fúria Imortal* +3d4 ≈ 7,5; *Imbuir
Elemento* +3d6 ≈ 10,5, contra um "+3"). Num golpe típico de 2d10 (~11), +3 é 27%; +3d6 é quase 100%.

A escala nova, decidida pelo autor: **buff de grupo +2/+4/+6** (vale menos por cabeça porque
multiplica pelos aliados), **buff pessoal +4/+8/+12**, e o **Pacto de Sangue em +5/+10/+15** — acima
do teto comum, justificado por custar a própria Vida sob Risco, e com escada regular no lugar do
salto de +8 pra +14. Vale lembrar que [bônus planos de buffs diferentes não somam](notas/auditoria.md),
então subir todos não empilha: só torna cada um relevante sozinho.

**Os bônus de teste vieram junto (2026-08-26).** O autor pediu a varredura no mesmo fôlego, e ela
desfez metade do próprio escopo: **Movimento não precisava mudar**. A fórmula é `6 + (Agilidade ÷ 10)`
casas — não é rolagem de d100, é distância no mapa, e num Movimento típico de 6 a 16 casas um
`+2/+3/+4` já vale 20 a 60%. As 7 habilidades de Movimento ficaram intactas.

O que precisava eram **Defesa, Evasão e ataque**, que entram na comparação com `d100 + Atributo`, onde
cada **+1 vale literalmente 1% de chance**. O jogo tinha `+1/+2/+3` no ataque (1% a 3%!) e escadas de
Defesa entre `+2/+3/+4` e `+4/+5/+6`. Régua de comparação: **[Vantagem](docs/glossario.md) vale ~25%** —
o melhor buff defensivo do jogo entregava menos de um terço disso, por 27 a 30 de Mana.

**17 habilidades** foram pra `+5/+10/+15`, ainda abaixo da Vantagem, que segue sendo o efeito forte do
sistema. *Aparar* foi pra `+6/+12/+18` por já ser o teto do jogo (`+3/+5/+7`) e manter a dianteira
proporcional. Cinco tinham **valor único embutido num pacote**, não escada — *Maestria Desperta* dá
dano + Defesa + ignora Armadura no mesmo efeito —, e foram convertidas uma a uma (+2→+10, +2→+8,
+3→+10, +1→+5, +2→+10) em vez de multiplicadas cegamente.

⚠ **Bônus plano e bônus de teste são escalas diferentes, e a mesma ficha pode ter as duas.** *Bênção
Divina* e *Disciplina Marcial* têm dano numa escada (+2/+4/+6 e +4/+8/+12) e Defesa noutra
(+5/+10/+15) — o regex de reescala precisa mirar `de Defesa` / `no ataque` sem tocar em `no dano`,
`de Movimento` ou `Escudo de`.

**Limiar de Crítico no stat block (2026-08-27).** Pedido do autor, pra não calcular `Sorte ÷ 3` de
cabeça no meio do turno. **Derivado no hook, não escrito na ficha** (`limiar_de_critico`): a Sorte já
está na linha de Atributos das 56 fichas, então o tile sai no build e não dessincroniza quando a Sorte
de uma criatura mudar. Entra entre Evasão e Iniciativa. O `≤` precisou entrar em `RE_VALOR_NUMERICO`,
senão "≤20" cairia na fonte de texto em vez da de número.

O número agora visível mostra que a Sorte foi escalada por Tier e o limiar acompanha: **Comum ≤1,
Treinado ≤3, Formidável ≤6–13, Lendário ≤18–21**. Vale nos dois sentidos desde a mudança de área —
é o mesmo limiar que decide se a criatura **escapa por completo** de um efeito resistido.

**O `verifica.py` passa a ler coerência entre páginas (2026-08-27).** Era o buraco que deixou dois
erros passarem em 2026-08-26: `--strict` pega página inexistente, e as checagens antigas pegam âncora,
id duplicado e dado de arma — nenhuma delas nota **uma regra contradizendo outra**. Duas checagens
novas:

- **Vocabulário aposentado** — 10 termos que saíram do sistema (`Fortitude do usuário`, `20 natural`,
  `Tiers de Sucesso`, e os 6 atributos do d20 em contexto de teste). Um deles reaparecendo é sinal de
  página que ficou pra trás. Frases que *dizem que o termo não existe mais* são legítimas e ficam de
  fora (`NEGA_APOSENTADO`).
- **Condição usada sem existir no glossário** — "Não invente nome de condição" já era regra, e o
  projeto já pagou por ela (`Paralisado`, 9 usos). O radical corta gênero e número (senão "Marcadas"
  vira falso positivo) e vale qualquer palavra do verbete, pra "fica Amaldiçoada" achar "Zona
  Amaldiçoada". De 15 falsos positivos pra 0 depois da calibragem.

⚠ **Uma checagem que nunca falhou pode estar quebrada.** As duas foram provadas injetando os erros de
propósito numa página e conferindo que o `exit=1` vinha com as três linhas certas, antes de reverter.

**As duas acharam três coisas na estreia**, todas reais:

- O **verbete Resolução do glossário** ainda descrevia o Teste de Resistência com o vocabulário antigo
  *e* o critério antigo, sem o caso de área — uma **terceira** página contando outra história da mesma
  regra, que ninguém tinha olhado.
- **`Caído` e `Estável` não eram verbetes.** Dois estados com regra própria, citados de 5 páginas,
  sem popover e fora do filtro por categoria. Viraram verbetes.
- E, puxado pelo autor: **a seção *Chegando a 0 de Vida* não mencionava o Último Turno**. Todo o resto
  do livro já tratava os dois juntos — a ficha de personagem, `combate.md`, `mestre/index.md`, até a
  regra do Companheiro Animal —, mas a página que **é** a regra listava só Estabilizar e Cura como
  saídas. Agora lista a terceira, e o **Último Turno virou verbete** (a regra mais dramática do
  sistema não tinha popover).

A abertura da categoria **Condições** também mudou: dizia "efeitos que uma habilidade impõe ao alvo",
o que já era falso antes (`Desprevenido` vem de emboscada, `Exausto` de exploração) e ficaria pior com
Caído e Estável dentro.

**As páginas de regra saem do Compêndio (2026-08-27).** Pedido do autor: o Compêndio fica só com as
listagens (*o que existe*) e a regra vai pra *Jogando o Jogo*, que é onde o jogador a procura.
`habilidades/regras.md` → **`jogar/regras-de-habilidade.md`** e `equipamento/regras.md` →
**`jogar/regras-de-equipamento.md`**; os endereços antigos redirecionam (`REDIRECIONA` vai a 9).

Foram **cinco acoplamentos**, e o quinto só apareceu quando o build quebrou:

1. **49 links** em todo o `docs/` — o caminho relativo de cada um depende de onde ele está, então a
   reescrita usa `os.path.relpath`, não substituição de texto
2. **18 links dentro das próprias páginas** — os vizinhos do Compêndio passaram a precisar de `../`,
   e os `../jogar/` viraram vizinhos
3. As **duas condições de caminho fixo** no hook (as páginas são montadas ao vivo)
4. O **`RE_ANCORA_PURA` do card de arma**, que mandava o leitor pra `regras.md#` da mesma pasta
5. ⚠ **`religa`, dentro de `monta_regras_de_equipamento`** — gerava `](index.md#equ-…)`, correto
   quando a página vivia em `equipamento/`. **Quebrou 62 âncoras de uma vez.** A regra que faltava:
   nessas funções o caminho é relativo à página **de destino**, não à de origem

O auto-link ficou de fora das duas (`FORA_DO_AUTOLINK`): elas já linkam o glossário à mão em quase
todo termo. Provado medindo — sem a exclusão, o auto-link injetaria **10 termos numa 18ª página**.

⚠ **`git checkout` num arquivo com mudanças não commitadas apaga trabalho — pela segunda vez em dois
dias.** Ontem foi `git checkout -- docs/habilidades/` (levou as edições de `regras.md`); hoje foi
`git checkout -- hooks/prisma.py` durante um teste, e voltou as seis mudanças do hook. Pior: deixou
`FORA_DO_AUTOLINK` referenciado sem existir, o que quebra o build com `NameError`. **Commite antes de
testar hipótese com checkout**, ou faça o teste numa cópia.

**Os tipos de dano físico ganham assinatura (2026-08-27).** A causa estrutural do clichê marcial,
medida: **os quatro tipos eram estatisticamente idênticos**. Cortante derrubava em 87% das habilidades,
Impacto em 90%, Perfurante em 84%, Arcano em 94% — e empurravam em 52–84%. O que devia ser
característico aparecia pouco: Sangrando em 22% das cortantes, Atordoado em 12% das de impacto.
**O clichê não era de 23 habilidades, era de 183**: escolher espada, martelo ou lança não mudava nada.

Entrou a tabela **Assinatura de Tipo de Dano** (em `equipamento/index.md`, montada na página de regra),
espelhando a Assinatura de Elemento — três degraus, um por Intensidade:

| Tipo | Assinatura | I → II → III |
|---|---|---|
| **Cortante** | a ferida não fecha | Sangrando → 8d4 → 12d4 |
| **Impacto** | derruba a postura | derruba → derruba e Lento → levantar custa ◈ a mais |
| **Perfurante** | atravessa a defesa | ignora Couraça → e Escudo → e Resistência física |
| **Arcano** | o golpe realimenta | devolve 1 → 2 → 3 Mana |

O autor escolheu **substituir o empurrão genérico nas fichas**, não herdar por regra: dá ~150 fichas,
feitas **um tipo por vez**. Os três saíram: **Cortante** (57), **Perfurante** (57) e **Impacto** (36).
**Nenhuma arma física do jogo empurra mais** — o verbo agora vem do tipo de dano.

O Impacto foi o mais delicado dos três, porque **90% das fichas dele já derrubavam**: substituir o
empurrão por "derruba" duplicaria a cláusula. A lógica precisou somar **só o degrau que faltava**
(o `Lento` na II, o custo de levantar na III) e **grudá-lo no derrubar que já estava na frase** —
senão saíam duas orações soltas ligadas por "e" repetido.

⚠ **O Arcano não muda ficha nenhuma.** A devolução de Mana é um efeito no *usuário*, não no alvo, então
não tem o que substituir: as 19 habilidades de foco mágico que empurram **continuam empurrando**, e a
devolução vem da tabela. Se isso incomodar, é decisão nova — o empurrão delas teria que virar outra
coisa.

**Couraça vira verbete (2026-08-27).** Ela entrava na fórmula da Evasão, decidia a defesa de toda
criatura e passou a aparecer no texto de 57 habilidades perfurantes — sem nunca ter sido definida. As
checagens do `verifica.py` não pegariam: ela jamais aparece como "fica Couraça".

O verbete guarda três coisas que só existiam espalhadas: que ela soma **só na Evasão** (nunca em
Fortitude, Social, Sanidade ou Exploração — carapaça não protege de veneno nem de medo); **por que a
ficha de criatura não mostra o número** (já está somado na Evasão, e exibi-lo de novo faria parecer
dois valores — decisão de 2026-08-02 que só vivia no CLAUDE.md); e que nos personagens quem ocupa esse
lugar é o **Escudo**, enquanto a **Armadura vai pra Vida**, não pra Evasão.

As **49 menções** nas habilidades perfurantes viraram link no mesmo lote — foram escritas sem link
porque o verbete ainda não existia.

⚠ **O Arcano devolve pouco de propósito**: 3 no teto contra um custo mínimo de 3 (Básica I) e 9 (II).
A arma **estica o pool, nunca se paga** — a auditoria de 2026-07-27 já teve que corrigir uma habilidade
que devolvia o próprio custo.

⚠ **Edição em massa: o dry-run pegou dois defeitos que o build não pegaria.** Primeiro a **ordem da
frase** ("2d8 de dano *e derruba o alvo* + o alvo fica Sangrando" — eu removia o empurrão e reinseria
depois do dano, em vez de trocar no lugar); depois o **conector comido** ("1d6 de dano o alvo fica
Sangrando", sem o `+`, porque o regex do empurrão engolia o `+` anterior). E a varredura final achou
uma **palavra órfã** que sobrou de "empurra 1 casa cada alvo *atingido*". Nenhum dos três quebra build
ou `verifica.py`: só se veem lendo.

Em aberto:

**Revisado pelo autor em 2026-08-27** — este bloco está fechado:

1. **Atributos de resistência** — *Metamorfose Forçada* passou pra **Magia** (virar um sapo é a
   realidade sendo reescrita, não o corpo aguentando); *Toque Suspenso* fica em **Defesa** e
   *Dominar os Mortos* em **Magia**, como eu tinha proposto
2. **Aumento Sombrio** aprovado como está — dreno de 1d6/2d6/3d6, +3/+6/+9 de dano, sem empilhar
3. **Acúmulo de bônus mantido**: bônus planos de buffs diferentes **não somam, vale o maior**. Era a
   decisão de julho marcada como "a que mais merece seu olhar", e o autor a confirmou sabendo que
   **ela pesa muito mais hoje**: em julho os buffs davam +1/+2/+3 e somá-los rendia +5; depois da
   reescala pro d100 somariam **+18** na Intensidade III. A regra deixou de ser procedimental e virou
   a trava do teto de dano de um grupo com dois suportes
4. As outras ~14 decisões da auditoria de 2026-07-27 (Voo, Empurrar/Puxar, Cena, Perde a próxima
   Reação, Agarrado, água e afogamento…) foram dadas por revisadas sem passar uma a uma: são
   procedimentais, estão publicadas há mais de um ano e **sobreviveram à migração pro d100** —
   conferido que as versões vivas já dizem "1d100", "Ataque ou Agilidade" e não citam mais Vitalidade

⚠ **A regra de acúmulo tinha um exemplo morto.** O verbete citava "Aura de Ataque (+3) e Bênção Divina
(+2)" — números que a reescala de 2026-08-26 apagou, e que viraram um empate (+2 e +2) que não
ilustrava nada. Trocado por Disciplina Marcial (+4) e Bênção Divina (+2). **Nenhuma das duas checagens
novas do `verifica.py` pega isso**, porque é número, não vocabulário — é o buraco declarado no item 6.

**Defeitos conhecidos, medidos e não corrigidos:**

4. **Os três tipos de dano físico não têm assinatura mecânica** — Cortante, Impacto e Perfurante são
   decorativos no glossário, enquanto os 10 elementos têm tabela própria. É essa lacuna que empurra
   toda habilidade marcial nova pro mesmo "empurra + derruba"; a leva de hoje tratou 8 sintomas, não
   a causa
5. **Camadas B e C das duplicatas** — 35 redundâncias de forma e ~141 colisões de assinatura em
   `notas/duplicatas.md`. **Vale remedir**: as levas de hoje mexeram em mais de 200 fichas depois do
   último levantamento
6. **Coerência entre páginas: metade resolvida.** O `verifica.py` ganhou duas checagens em
   2026-08-27 (vocabulário aposentado e condição sem verbete), mas as duas são **listas de termos
   vigiados**, não análise de sentido: pegam uma regra que voltou a usar palavra velha, e não uma que
   passou a dizer outra coisa com palavras novas. O caso que continua invisível é o de números — se
   `regras.md` disser que um Supremo custa 48 de Mana e `mana.md` disser 45, nada acusa

7. **Área nunca mais zera** — com a mudança de 2026-08-26, resistir dá metade do dano em vez de nada.
   As áreas ficaram mais confiáveis e **nenhum dado foi reduzido pra compensar**. Só a mesa responde
8. **Lâmina de Sangue** causa 10d8 nas três Intensidades — só o dreno escala. Anomalia notada de
   passagem, nunca investigada
9. **Familiares de Conjuração** — *Olhos Emprestados* e *Chama de Bolso* têm ficha idêntica (Menor,
   ◈ + 6 Mana, vínculo permanente que não cresce); só o efeito utilitário difere
10. **Condições órfãs** — `Silenciado` estava definido no glossário e era aplicado por *nenhuma*
    habilidade até 2026-08-26. Vale varrer o glossário atrás de outras
11. **Dano dos PJs escala pouco** (2,7x contra 7,6x da Vida) — adiado de propósito. As reescalas de
    bônus de 2026-08-26 **não** atacaram isso: mexeram no bônus plano, não no dado das habilidades

**Trabalho novo, quando houver vontade:**

12. **Ficha de personagem imprimível** — a construir do zero, elemento por elemento (ver acima)
13. Os sete itens da seção 4.3 de `notas/auditoria.md` — exigem escolha de conteúdo, não correção
14. Conteúdo novo é sempre bem-vindo; nenhuma lacuna estrutural de regra permanece
