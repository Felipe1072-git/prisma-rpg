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
| Habilidades Mágicas Básicas | Uso básico de magia |
| Habilidades Mágicas por Elemento | Fogo, Gelo, Terra, Sombras, Luz, etc. |
| Habilidades Sociais | Persuasão e afins |
| Habilidades de Infiltração | Furtividade, ladinagem |
| Habilidades de Mobilidade | Voo, deslocamento |
| Habilidades de Buff | Incremento de força, imbuir elementos em armas, etc. |
| Habilidades de Debuff | Desvantagens para inimigos ou em testes |

*(Lista pode crescer — usuário sinalizou que ainda vai pensar em mais grupos.)*

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
│   ├── racas/                ← index.md = listagem única (24 raças)
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
| `habilidades/index.md` | as 580 habilidades viram cards (grupo, elemento, arma, atributo, alvo, Mana) | `hab-{arma}-{nome}` ou `hab-{nome}` |
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

## Convenções de Commit

- `feat:` nova regra, habilidade, pacote ou mecânica
- `fix:` correção de erro ou inconsistência
- `docs:` atualização de texto, revisão ou reorganização
- `refactor:` reorganização sem mudança de conteúdo

## Status

**Versão 0.2 (2026-07-26) — sistema jogável de ponta a ponta.** Publicado em
[felipe1072-git.github.io/prisma-rpg](https://felipe1072-git.github.io/prisma-rpg/), sob CC BY 4.0,
com deploy automático a cada push (workflow em `.github/workflows/deploy.yml`).

O que existe: 580 habilidades — 394 gerais nos 10 grupos mais 186 de arma (62 armas × 3 graus) —,
24 raças, 100 pacotes, 11 elementos com assinatura mecânica própria, sistema Tocado, e Livro do
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
  o que estava escrito): ×1 no 1–4, ×1,8 no 5–10, ×2,7 no 11–15, ×3,7 no 16–20 — as mesmas
  proporções da tabela de Vida por faixa, aplicadas do outro lado da conta. As 52 fichas
  valem em qualquer mesa. A tabela de Vida por faixa sobrou pro caso de querer *aquela*
  criatura de volta mais séria — e aí **sobe a Ameaça junto**, com o multiplicador em ×1,
  senão o nível conta duas vezes. O guarda-corpo contra "29 goblins = Mortal no nível 16" é o
  limite de 8 criaturas, que já existia.
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

Em aberto:
1. **Ficha de personagem imprimível** — a construir do zero, elemento por elemento (ver acima)
2. **Dano dos PJs escala pouco** (2,7x contra 7,6x da Vida) — problema conhecido, adiado de
   propósito porque a correção mexeria nas 573 habilidades. Só reabrir se ele trouxer
3. Os sete itens da seção 4.3 de `notas/auditoria.md` — exigem escolha de conteúdo, não correção
4. Conteúdo novo é sempre bem-vindo, mas nenhuma lacuna estrutural de regra permanece
