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
│   ├── mestre/               ← Livro do Mestre; bestiario.md = listagem,
│   │                            criando-criaturas.md = as regras
│   ├── glossario.md          ← vira popover ao passar o mouse nos termos
│   └── assets/{css,js,img}/  ← prisma.css, prisma.js, SVGs de brasão/divisor
├── hooks/prisma.py           ← camada de exibição (ver abaixo) — não altera docs/
├── mkdocs.yml                ← nav, tema, extensões
├── .github/workflows/        ← deploy.yml: publica a cada push na main
├── notas/                    ← rascunhos, auditoria, prompts (não publicado)
└── referencia/               ← material de referência pessoal (não publicado)
```

O header tem 6 abas: **Início · Jogando o Jogo · Criação de Personagem · Compêndio ·
Livro do Mestre · Glossário**. Toda listagem filtrável mora no Compêndio.

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
| `habilidades/index.md` | as 571 habilidades viram cards (grupo, elemento, arma, atributo, alvo, Mana) | `hab-{arma}-{nome}` ou `hab-{nome}` |
| `racas/index.md` | as 24 seções `##` viram cards (leva, atributos, nº de traços); as duas divisórias de leva viram prosa acima da lista | `rac-{nome}` |
| `origens/index.md` | as 3 tabelas d20 viram 60 cards (eixo, tipo de traço, atributo) + sorteio | `ori-{eixo}-{nome}` |
| `equipamento/index.md` | as 62 seções de arma + escudos + armaduras viram 68 cards; a ficha vem da tabela de dado de dano | `equ-{nome}` |
| `pacotes/index.md` | as 100 seções `###` viram cards (vertente, arma, atributo, Suprema final) + sorteio | `pac-{nome}` |
| `mestre/bestiario.md` | as seções `##` viram cards de criatura (tier, couraça, PA) | `bes-{nome}` |
| `habilidades/*.md` (grupos) | cada habilidade vira um ponteiro de uma linha pro card | — |
| `habilidades/regras.md`, `equipamento/regras.md`, `jogar/condicoes.md` | montam-se lendo ao vivo seções que vivem noutro arquivo — nenhum texto duplicado em disco | — |
| `glossario.md` | cada verbete vira popover ao passar o mouse | — |

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

`on_post_build` também escreve as páginas de redirecionamento dos endereços antigos
(`jogador/sistema-d20`, `jogador/pontos-de-acao`, `jogador/mana`, `jogador/introducao`,
`jogador/tocado`), preservando a âncora quando ela tem destino equivalente. Mexer nos
mapas `REDIRECIONA` / `ANCORAS_*` é o que mantém link antigo funcionando.

Ao mexer nisso:

- `mkdocs serve` **não** recarrega `hooks/prisma.py` — pare e suba o servidor de novo.
- **`--strict` não basta.** Ele pega página inexistente, mas âncora quebrada ele só
  reporta como INFO, e id duplicado ele não vê. Sempre feche com:

  ```bash
  python -m mkdocs build --strict && python notas/verifica.py
  ```

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

O que existe: 571 habilidades — 385 gerais nos 10 grupos mais 186 de arma (62 armas × 3 graus) —,
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

Duas contagens estavam erradas e foram corrigidas contra os cards gerados: são **571**
habilidades (não 573) e **24** raças (não 25). E uma tabela do Arsenal tinha régua de 5 colunas
pra 4 cabeçalhos — nunca renderizou como tabela no site publicado; agora renderiza.

Fases seguintes, já acordadas com o autor: **(3)** glossário ganha índice A–Z, filtro por
categoria, e para de duplicar armas/grupos/elementos; **(4)** auto-link do glossário e popover
de habilidade; **(5)** Livro do Mestre.

Em aberto:
1. **Ficha de personagem imprimível** — a construir do zero, elemento por elemento (ver acima)
2. **Dano dos PJs escala pouco** (2,7x contra 7,6x da Vida) — problema conhecido, adiado de
   propósito porque a correção mexeria nas 573 habilidades. Só reabrir se ele trouxer
3. Os sete itens da seção 4.3 de `notas/auditoria.md` — exigem escolha de conteúdo, não correção
4. Conteúdo novo é sempre bem-vindo, mas nenhuma lacuna estrutural de regra permanece
