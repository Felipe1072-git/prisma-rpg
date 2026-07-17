---
name: criar-habilidade
description: Cria ou ajusta habilidades de jogo do Prisma RPG (o RPG de mesa homebrew deste repositório), mantendo o padrão mecânico e de formatação já estabelecido no projeto. Use esta skill sempre que o usuário pedir pra criar, desenhar, balancear ou revisar uma habilidade, feitiço, magia, golpe de arma, ou "poder" de personagem — inclusive quando o pedido vier como "cria uma habilidade parecida com X do anime/filme/jogo Y", ou como uma ideia solta tipo "queria algo tipo controle mental" ou "e se tivesse voo?". Também use ao criar uma arma nova (que precisa de 3 tiers de habilidade) ou um elemento/subgrupo novo dentro de Mágicas por Elemento.
---

# Criar Habilidade — Prisma RPG

Esta skill existe porque o padrão de habilidades do Prisma RPG foi fixado com bastante detalhe numa sessão de design, e é fácil perder essa consistência em sessões futuras (esquecer um campo, comprimir os tiers numa linha só, inventar uma habilidade sem consultar o usuário). Ela é uma referência de consulta rápida — leia as fontes vivas linkadas abaixo quando precisar do valor exato de algo, não confie de cor em números que possam ter mudado.

**Fontes vivas** (sempre a verdade mais atual — releia se um número aqui parecer estranho):
- [docs/habilidades/index.md](../../docs/habilidades/index.md) — Ficha de Habilidade, tiers de sucesso, lista de grupos
- [docs/jogador/arsenal.md](../../docs/jogador/arsenal.md) — armas existentes e suas 3 habilidades
- [docs/jogador/mana.md](../../docs/jogador/mana.md) — Custo por Tier de Poder
- [docs/glossario.md](../../docs/glossario.md) — todo termo que pode virar um link de Chave
- [CLAUDE.md](../../CLAUDE.md) — regras gerais do projeto (nunca inventar sem consultar, sempre AskUserQuestion pra escolhas)

## O processo, não pule etapas

O CLAUDE.md do projeto proíbe escrever conteúdo de jogo em `docs/` sem aprovação explícita. Isso vale em dobro pra habilidades novas:

1. **Proponha no chat primeiro** — nome, descrição evocativa, Chave, custos, e os tiers com valores já preenchidos (nunca "TBD"). O usuário precisa conseguir avaliar a habilidade pronta, não uma ideia vaga.
2. **Pergunte o que não é óbvio.** Se o atributo, o grupo, um valor numérico ou uma escolha de design não tiver uma resposta clara a partir do que já existe no projeto, use `AskUserQuestion` em vez de decidir sozinho. É melhor perguntar demais do que inventar uma regra que o usuário depois tem que desfazer.
3. **Só grave depois do "pode gravar" / aprovação explícita.** Mostre o preview, espere confirmação, então edite o arquivo.

Se a habilidade for inspirada numa obra (anime, filme, jogo — Grand Chase é a referência usada até agora), pode pesquisar a fonte pra entender o conceito, mas o nome e a mecânica final precisam ser **originais**. No chat, parafraseie o conceito da fonte em 1-2 frases — nunca reproduza texto longo dela.

## A Ficha de Habilidade

Toda habilidade — sem exceção — tem estes campos, cada um em seu próprio bullet:

- **Nome**
- *Descrição breve*, em itálico, logo abaixo do nome: 1 frase evocativa que deixa claro o que a habilidade faz. Evite números específicos que o jogador possa confundir com regra (ex: não diga "cinco flechas" se mecanicamente é só 1 rolagem de dano — isso já aconteceu e gerou confusão).
- **Chave** — ver seção própria abaixo
- **Custo** em Mana e em Pontos de Ação (◈), normalmente na mesma linha: `- **Custo:** X Mana | ◈◈ (2 PA)`
- **Atributo**
- **Alvos** (e **Alcance** sempre que a habilidade não for corpo a corpo — nunca deixe alcance ou raio de área vagos tipo "uma área", sempre um número de casas)
- **Tiers de Sucesso**, um bullet por tier, cada um com o valor numérico completo já resolvido (nunca "dano da arma" genérico, nunca dois tiers comprimidos na mesma linha com `|`)
- **Crítico**

### Tiers de Sucesso

O teste é **d20 + Atributo**. Os tiers são:

| Tier | Total (d20 + Atributo) |
|---|---|
| Tier 1 (fraco) | ≤ 10 |
| Tier 2 (médio) | 11–16 |
| Tier 3 (forte) | ≥ 17 |
| Crítico | 20 natural — efeito extra, além do tier 3 |

**Habilidades sem teste de ataque não precisam de tiers.** Um buff puro (ex: um escudo de valor fixo) ou um efeito automático (ex: uma habilidade Suprema que causa dano inevitável, sem chance de esquiva) pode pular direto pra um campo **Efeito** único, sem tabela de tiers — porque não existe rolagem cujo resultado varie o efeito. Isso é uma escolha de design válida, não um campo esquecido; só não abuse dela pra fugir de decidir números.

## Chave — e por que ela precisa ser um link

Toda habilidade deve linkar seus termos pro [Glossário](../../docs/glossario.md), pra funcionar como navegação cruzada quando o site for publicado.

- **Habilidade de arma:** `[Arma](../glossario.md#arma) - [Tier](../glossario.md#tier)` — ex: `[Espada](../glossario.md#espada) - [Básica](../glossario.md#básica)`
- **Habilidade geral de grupo, sem subtipo:** `[Grupo](../glossario.md#grupo)` — ex: `[Buff](../glossario.md#buff)`
- **Habilidade geral de grupo, com subtipo** (hoje só Mágicas por Elemento tem subtipos): `[Grupo](../glossario.md#grupo) - [Subtipo](../glossario.md#subtipo)` — ex: `[Mágicas por Elemento](../glossario.md#mágicas-por-elemento) - [Terra](../glossario.md#terra)`

O caminho relativo depende de onde o arquivo da habilidade mora: tanto `docs/jogador/` quanto `docs/habilidades/` ficam um nível abaixo de `docs/`, então ambos usam `../glossario.md`.

**Propriedades de arma** (ex: Finesse) entram como um 3º segmento na Chave, mas **só nas habilidades da própria arma que tem a propriedade** — ex: `[Adagas](../glossario.md#adagas) - [Básica](../glossario.md#básica) - [Finesse](../glossario.md#finesse)`. Habilidades gerais de grupo que apenas *mencionam* a propriedade condicionalmente no texto (ex: "Força, ou Agilidade se a arma equipada for Finesse") não ganham esse segmento — a Chave descreve o que a habilidade **é**, não toda regra que ela pode tocar de leve.

**Se a habilidade introduzir um termo que ainda não existe no Glossário** (uma arma nova, um grupo novo, um elemento novo), adicione uma entrada `###` correspondente em `docs/glossario.md` no mesmo lote de edição — senão o link fica quebrado.

## Custo por Tier de Poder

O custo em Mana é um eixo **independente** do custo em Pontos de Ação — um mede quanto da força bruta da habilidade, o outro quanto do turno ela consome. Ver [docs/jogador/mana.md](../../docs/jogador/mana.md) pra fórmula de Mana máximo, mas o guia de custo é:

| Tier de Poder | Custo em Mana | Uso esperado |
|---|---|---|
| Menor | 1–3 | Várias vezes por combate |
| Moderado | 4–8 | 2–4 vezes por descanso |
| Maior | 9–15 | 1–2 vezes por descanso |
| Supremo | 16+ | 1 vez por descanso, possivelmente com restrição extra |

**As 3 habilidades de toda arma (Básica/Avançada/Especial) usam sempre o tier Menor** — são as técnicas do dia a dia, não deveriam competir por relevância com as habilidades grandiosas dos grupos. Habilidades gerais de grupo (feitiços, buffs, ultimates) variam o Custo em Mana conforme o impacto real do efeito: algo que invoca um clone ou controla o campo de batalha inteiro pesa mais que um golpe a mais.

**PA é um eixo independente de Mana** — mede tempo de execução, não força. Pra habilidades de arma, PA já vem fixo pelo tier (Básica=1, Avançada=2, Especial=3). Pra habilidades gerais, use este critério (ver [docs/jogador/pontos-de-acao.md](../../docs/jogador/pontos-de-acao.md)):

| PA | Critério | Exemplos já criados |
|---|---|---|
| ◈ (1) | Efeito instantâneo/reativo — buff rápido, defesa, gesto único | Escudo Mágico |
| ◈◈ (2) | Conjuração padrão — a maioria dos ataques/efeitos de alvo único ou área pequena | Antigravidade, Cura, Petrificar, Relâmpago |
| ◈◈◈ (3) | Domina o turno inteiro — grandes áreas, invocações, ultimates | Fúria da Lâmina, Dança Élfica, Chuva de Meteoros, Raios e Relâmpagos |

## Armas mágicas são genéricas — não travam feitiços

Isso é uma decisão de design deliberada, ligada ao fato de o Prisma RPG não ter classes: as 3 habilidades de uma arma mágica (Cetro é o único exemplo até agora) são canalizações **neutras**, sem elemento ou tema fixo (ex: "Investida Arcana", um pulso de dano sem forma definida). Se uma arma mágica travasse "Petrificar" ou "Cura" como sua Habilidade Básica, isso empurraria o jogo de volta pra uma lógica de classe ("mago do cetro só petrifica"), o que contradiz a premissa central do sistema.

Os feitiços temáticos (fogo, cura, controle mental, o que for) **não** vivem no Arsenal — vivem soltos nos grupos de Habilidades (Mágicas por Elemento, Buff, Debuff, Suporte etc.), disponíveis pra qualquer personagem, com qualquer arma, sem lock algum. Se o usuário pedir uma habilidade nova claramente mágica/temática, ela quase certamente é uma "Habilidade Geral" de grupo, não uma habilidade de arma.

## Onde a habilidade mora

- Habilidade de arma → `docs/jogador/arsenal.md`, na seção `## NomeDaArma`
- Habilidade geral de grupo → `docs/habilidades/<grupo>.md`, numa seção `## Habilidades Gerais` (crie a seção se ainda não existir)
- Feitiço elemental → `docs/habilidades/magicas-elementais.md`, numa sub-seção `## NomeDoElemento` (crie se o elemento ainda não tiver seção — e adicione o elemento na lista do topo do arquivo e no Glossário)
- Se o pedido não se encaixa em nenhum grupo existente, isso é uma decisão de design (criar grupo novo) — pergunte ao usuário antes de inventar um, mesma lógica do resto do processo. "Suporte" foi criado assim durante a sessão que gerou esta skill.

## Checklist antes de gravar

- [ ] Descrição breve é 1 frase evocativa, sem número que confunda mecânica com narrativa
- [ ] Chave é um link válido pros 1-2 termos corretos no Glossário (e o Glossário tem essas entradas)
- [ ] Custo em Mana bate com o Tier de Poder certo, e Custo em PA bate com o critério de PA — avaliados separadamente, um não implica o outro
- [ ] Alcance/raio em casas, se não for corpo a corpo
- [ ] Cada Tier de Sucesso é seu próprio bullet, com valor numérico completo (ou a habilidade explicitamente não usa tiers, com justificativa implícita clara)
- [ ] Crítico definido (ou "sem tiers" documentado)
- [ ] Usuário aprovou explicitamente antes da escrita no arquivo

## Exemplo completo (referência de formatação)

De `docs/jogador/arsenal.md`, a Habilidade Básica da Espada:

```markdown
**Golpe Certeiro** — *Básica*

*Um golpe preciso e brutal, direto ao ponto fraco do inimigo.*

- **Chave:** [Espada](../glossario.md#espada) - [Básica](../glossario.md#básica)
- **Custo:** 1 Mana | ◈ (1 PA) | **Atributo:** Força | **Alvos:** 1 criatura
- **Tier 1 (≤10):** 1d8 de dano
- **Tier 2 (11–16):** 1d8 de dano + empurra 1 casa
- **Tier 3 (≥17):** 1d8 de dano + derruba o alvo
- **Crítico:** dano máximo (8) + 1d8 extra, e derruba o alvo
```

E um exemplo sem tiers, de `docs/habilidades/buff.md`:

```markdown
**Escudo Mágico**

*Uma barreira translúcida se ergue, absorvendo o impacto antes que ele chegue.*

- **Chave:** [Buff](../glossario.md#buff)
- **Custo:** 4 Mana | ◈ (1 PA) | **Atributo:** Inteligência | **Alvos:** 1 criatura (pode ser o próprio usuário)
- **Efeito:** o alvo ganha um Escudo de 1d8 + Inteligência pontos, que absorve dano antes da Vida ser afetada. Dura até o fim do próximo turno do alvo, ou até ser destruído.
- *(Sem Tiers de Sucesso — habilidade de buff, sem teste de ataque)*
```
