# Bestiário

Criaturas prontas pra usar em mesa, e as regras pra montar as suas.

## Como Ler uma Ficha de Criatura

Criatura não é personagem: ela não sobe de nível, não distribui pontos e não precisa de ficha completa. O que define uma criatura é o **[Tier de Ameaça](../jogador/sistema-d20.md#base-de-resiliência)** — e dele saem quase todos os números dela.

| Tier | Base de Resiliência | Vida | Pontos de Ação | Ficha | Ataques |
|---|---|---|---|---|---|
| **Comum** | 6 | 8 | ◈ (1) | só os atributos relevantes | custo fixo |
| **Treinado** | 8 | 25 | ◈◈ (2) | só os atributos relevantes | custo fixo |
| **Formidável** | 10 | 60 | ◈◈◈ (3) | os 8 atributos | com [Intensidade](../habilidades/index.md#intensidade) + Mana |
| **Lendário** | 14 | 180 | ◈◈◈ (3) + Ação de Lenda | os 8 atributos | com Intensidade + Mana |

### Vida é valor fixo

Sem rolagem: abra a ficha e use o número. A Vida foi calibrada contra o dano real que um grupo entrega — um **Comum cai num único golpe** (o dano médio de uma habilidade em Intensidade I é ~6), um **Treinado** aguenta 2-3, um **Formidável** absorve mais ou menos uma rodada inteira de um grupo de 4, e um **Lendário** dura 3-5 rodadas.

### Pontos de Ação por Tier

Um personagem tem 3 ◈. Se cada capanga também tivesse 3, seis goblins gerariam dezoito ataques por rodada — a mesa travaria e o grupo morreria. Então o PA é a primeira medida de ameaça: um **Comum age uma vez** (move **ou** ataca, não os dois), um Treinado tem dois, e só a partir de Formidável a criatura joga com o turno completo de um personagem.

### Couraça Natural

O bônus que faltava ser definido na [tabela de Defesa](../jogador/sistema-d20.md#defesa). Soma **só na Defesa física** (dano, empurrar, derrubar) — não protege contra veneno, medo ou ilusão:

| Couraça | Bônus | Exemplo |
|---|---|---|
| Nenhuma | +0 | pele nua, tecido, gente comum |
| Coriácea | +1 | couro curtido, pelagem densa, pele grossa |
| Escamada | +2 | escamas, carapaça de quitina, cota de malha |
| Blindada | +3 | placas ósseas, armadura de placas, casco pesado |
| Dracônica | +4 | escamas de dragão adulto, pedra viva, aço encantado |

**Defesa física = Base de Resiliência + Agilidade + Couraça Natural.**

### Ataques: capangas são fixos, chefes decidem

**Comum e Treinado** têm ataques de **custo fixo**, sem Mana: o Mestre lê a linha e rola. É o que permite rodar oito capangas sem administrar oito reservas de recurso.

**Formidável e Lendário** são chefes: têm **Mana** e usam [Intensidade](../habilidades/index.md#intensidade) como um jogador — o Mestre decide se gasta 1 PA num golpe rápido ou queima o turno inteiro numa Intensidade III. É onde a decisão tática vale a pena, porque é uma criatura só.

### Ação de Lenda

Exclusiva do Tier Lendário: **uma vez por rodada, fora do próprio turno**, a criatura pode usar uma habilidade sua pagando o custo normal. É o que evita que um Lendário sozinho seja simplesmente cercado e morto sem reagir — ele responde no turno dos personagens.

---

## Goblin

*Baixo, magro e covarde sozinho — mas eles nunca estão sozinhos.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Couraça:** Coriácea (+1)
- **Atributos:** Agilidade +1, Vitalidade -1
- **Defesa física:** 6 + 1 + 1 = **8**
- **Iniciativa:** d20 + 0

**Adaga Enferrujada** — ◈ | 1 criatura adjacente
: 1d4 de dano.

**Bando** *(passiva)*
: Se houver outro Goblin adjacente ao mesmo alvo, o ataque causa +1d4. Goblin é ameaça por quantidade, não por indivíduo.

**Covardia** *(passiva)*
: Ao ficar com 3 ou menos de Vida, o Goblin usa seu PA pra fugir na direção mais segura, se houver rota. Não é medo mecânico — é o Mestre jogando o bicho como ele é.

## Lobo

*Ele não ataca o mais forte do grupo. Ataca o que se afastou.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Couraça:** Coriácea (+1)
- **Atributos:** Agilidade +2, Vitalidade +1, Sabedoria +1
- **Defesa física:** 6 + 2 + 1 = **9**
- **Movimento:** 5 casas (3 + Agilidade) — mais rápido que a maioria dos personagens
- **Iniciativa:** d20 + 0

**Mordida** — ◈ | 1 criatura adjacente
: 1d6 de dano. Se o alvo estiver sozinho (nenhum aliado dele adjacente), derruba também.

**Matilha** *(passiva)*
: O ataque rola com Vantagem se outro Lobo estiver adjacente ao mesmo alvo.

**Faro** *(passiva)*
: Não pode ser surpreendido por criatura que dependa apenas de ocultação visual.

## Bandido

*Sabe exatamente onde doer, e cobra pela informação.*

- **Tier:** Treinado | **Vida:** 25 | **PA:** ◈◈ (2) | **Couraça:** Coriácea (+1)
- **Atributos:** Força +2, Agilidade +2, Vitalidade +1, Vontade +1
- **Defesa física:** 8 + 2 + 1 = **11**
- **Iniciativa:** d20 + 0

**Espada Curta** — ◈ | 1 criatura adjacente
: 1d8 de dano.

**Golpe Sujo** — ◈◈ | 1 criatura adjacente
: 1d8 de dano + o alvo fica [Sangrando](../glossario.md#sangrando). Contra alvo já derrubado, 2d8 em vez de 1d8.

**Recuar e Atirar** — ◈◈ | 1 criatura a até 8 casas
: o Bandido se afasta até 3 casas e dispara uma besta de mão: 1d6 de dano. Não provoca reação ao se afastar.

## Esqueleto

*Cortar não resolve. Ele não tem o que sangrar.*

- **Tier:** Treinado | **Vida:** 25 | **PA:** ◈◈ (2) | **Couraça:** Escamada (+2, ossos e escudo velho)
- **Atributos:** Força +2, Agilidade +0, Vitalidade +3
- **Defesa física:** 8 + 0 + 2 = **10**
- **Imunidades:** [Sangrando](../glossario.md#sangrando), [Envenenado](../glossario.md#envenenado), veneno, doença, medo
- **Resistência:** [Cortante](../glossario.md#cortante) e [Perfurante](../glossario.md#perfurante) — lâmina e ponta não têm o que rasgar num esqueleto
- **Vulnerabilidade:** [Impacto](../glossario.md#impacto) — osso quebra; martelos e maças causam o **dobro**
- **Iniciativa:** d20 + 0

**Lâmina Antiga** — ◈ | 1 criatura adjacente
: 1d8 de dano.

**Investida de Ossos** — ◈◈ | 1 criatura a até o Movimento
: avança e golpeia: 1d8 de dano + empurra 1 casa.

**Remontar** *(passiva)*
: Ao chegar a 0 de Vida pela primeira vez, o Esqueleto se remonta no início do próprio próximo turno com **8 de Vida** — a não ser que o golpe final tenha sido de [Impacto](../glossario.md#impacto), ou que os ossos tenham sido espalhados (uma Ação Básica de um personagem adjacente resolve).

## Slime

*Bater com a espada só faz dois problemas onde havia um.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Couraça:** Nenhuma (+0)
- **Atributos:** Vitalidade +2, Agilidade -2
- **Defesa física:** 6 - 2 + 0 = **4** (é lento e não desvia; acertar é fácil, resolver não)
- **Imunidades:** derrubar, empurrar, [Sangrando](../glossario.md#sangrando), veneno
- **Resistência:** [Cortante](../glossario.md#cortante) e [Perfurante](../glossario.md#perfurante) — a lâmina atravessa a gelatina sem cortar nada
- **Iniciativa:** d20 + 0

**Investida Ácida** — ◈ | 1 criatura adjacente
: 1d4 de dano, e o alvo fica [Envenenado](../glossario.md#envenenado) (o ácido continua corroendo).

**Divisão** *(passiva)*
: Quando sofre dano **[Cortante](../glossario.md#cortante) ou [Perfurante](../glossario.md#perfurante)** e sobrevive, o Slime se divide: surge um segundo Slime adjacente com metade da Vida atual (arredondada pra baixo, mínimo 1), e o original fica com a outra metade. Dano de [Impacto](../glossario.md#impacto), [Arcano](../glossario.md#arcano) e elemental não divide — esmaga ou queima.

## Dragão Filhote

*Ainda não voa bem. Já queima tudo.*

Primeiro chefe do Bestiário: usa **Mana e [Intensidade](../habilidades/index.md#intensidade)**, e o Mestre decide quanto investir em cada turno, como um jogador faria.

- **Tier:** Formidável | **Vida:** 60 | **PA:** ◈◈◈ (3) | **Mana:** 20 | **Couraça:** Blindada (+3)
- **Atributos:** Força +3, Vitalidade +3, Agilidade +2, Inteligência +2, Sabedoria +1, Vontade +2, Sorte +0, Sanidade +2
- **Defesa física:** 10 + 2 + 3 = **15**
- **Defesa mental:** 10 + 2 = **12**
- **Resistência:** fogo
- **Movimento:** 5 casas no chão, 8 casas voando (mas precisa de 1 ◈ pra alçar voo)
- **Iniciativa:** d20 + 0

**Garras e Presas** — ◈ | 0 Mana | 1 criatura adjacente
: 2d6 de dano. É o ataque de rotina — não gasta Mana.

**Baforada** — 1 criatura ou área, conforme a Intensidade | **Atributo:** Força
: A assinatura do elemento [Fogo](../habilidades/magicas-elementais.md#fogo): o alvo pega fogo e continua queimando.
: **Intensidade I — ◈ (1 PA) + 3 Mana:** cone de 3 casas, 2d6 de dano em cada alvo + cada alvo fica [Queimando](../glossario.md#queimando)
: **Intensidade II — ◈◈ (2 PA) + 6 Mana:** cone de 3 casas, 2d6 de dano + cada alvo fica [Queimando](../glossario.md#queimando), e o fogo se espalha para 1 criatura adjacente a cada alvo
: **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** cone de 5 casas, 3d6 de dano + [Queimando](../glossario.md#queimando) causando 2d4 por turno, e o fogo se espalha para todas as criaturas adjacentes
: **Crítico (20 natural):** dano máximo dos dados da Intensidade usada + uma rolagem extra igual, e sobe 1 Intensidade

**Voo Rasante** — ◈◈ | 2 Mana | linha de 6 casas
: o Dragão sobrevoa a linha causando 2d6 em cada criatura nela, e termina o movimento fora do alcance corpo a corpo de todas. Só pode ser usada se já estiver voando.

**Escamas Quentes** *(passiva)*
: Quem atinge o Dragão com ataque corpo a corpo sofre 1d4 de dano de fogo.
