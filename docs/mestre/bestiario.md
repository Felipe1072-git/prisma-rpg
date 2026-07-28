# Bestiário

Criaturas prontas pra usar em mesa, e as regras pra montar as suas.

## Como Ler uma Ficha de Criatura

Criatura não é personagem: ela não sobe de nível, não distribui pontos e não precisa de ficha completa. O que define uma criatura é o **[Tier de Ameaça](../jogador/sistema-d20.md#base-de-resiliencia)** — e dele saem quase todos os números dela.

| Tier | Base de Resiliência | Vida | Pontos de Ação | Ficha | Ataques |
|---|---|---|---|---|---|
| **Comum** | 6 | 8 | ◈ (1) | só os atributos relevantes | custo fixo |
| **Treinado** | 8 | 25 | ◈◈ (2) | só os atributos relevantes | custo fixo |
| **Formidável** | 10 | 60 | ◈◈◈ (3) | os 8 atributos | com [Intensidade](../habilidades/regras.md#intensidade) + Mana |
| **Lendário** | 14 | 180 | ◈◈◈ (3) + Ação de Lenda | os 8 atributos | com Intensidade + Mana |

### Como resolver o ataque de uma criatura

**Quem age, rola** — vale pra criatura do mesmo jeito que vale pro personagem. Quando a criatura ataca, **o Mestre rola**:

**d20 + o Ataque da criatura vs a Defesa do personagem.**

Cada ficha traz o **Ataque** já calculado, pra você não precisar somar atributo na hora. A Defesa do personagem vem da ficha dele: aventureiros são **Treinado**, então **Defesa física = 8 + Agilidade + Armadura** e **Defesa mental = 8 + Vontade** (ver [Defesa](../jogador/sistema-d20.md#defesa)).

- **1 natural** sempre falha.
- **20 natural** é crítico: **dano máximo dos dados + uma rolagem extra**, e nada além disso. Criatura **não** sobe de Intensidade no crítico — esse bônus é dos personagens.
- Ataque que impõe efeito mental, veneno ou medo é comparado à **Defesa mental** (ou à Defesa do atributo que o efeito indicar), não à física. Por isso toda ficha traz as duas.

**Como ler a linha de um ataque.** Cada ataque vem escrito assim:

```
Mordida — ◈ | +2 vs Defesa física | 1 criatura adjacente
```

Isso é, na ordem: o **custo em PA** (◈), o **bônus que o Mestre soma no d20** e contra qual **Defesa** comparar, e quem pode ser **alvo**. No caso: gasta 1 PA, role d20+2 contra a Defesa física do alvo, atingindo uma criatura adjacente.

### Um turno jogado

O [Dragão Filhote](#dragao-filhote) (Ataque **+3**, 3 PA, 20 Mana) está à frente de dois personagens: a **Guerreira** (Defesa física **10**) e o **Mago** (Defesa física **16** — ágil e difícil de acertar).

**O Mestre escolhe a Baforada em Intensidade II:** gasta **2 PA** e **6 Mana**, sobrando 1 PA e 14 Mana.

1. **Quem é alvo?** A Baforada em Intensidade II é um cone de 3 casas à frente. Os dois estão dentro, então os dois são alvos.
2. **Rola o dado:** sai **12** no d20. Somando o Ataque +3, o total é **15**. Uma rolagem só, comparada com cada alvo.
3. **Compara com cada Defesa:**

| Alvo | Defesa física | Comparação | Resultado |
|---|---|---|---|
| Guerreira | 10 | 15 ≥ 10 | **acertou** — 2d6 de dano, e fica [Queimando](../glossario.md#queimando) |
| Mago | 16 | 15 < 16 | **errou** — nada acontece com ele |

4. **O efeito extra não precisa de rolagem.** A Intensidade II espalha o fogo para 1 criatura adjacente a cada alvo atingido: se o Ladino estiver ao lado da Guerreira, ele pega fogo automaticamente. Espalhamento não é ataque, então não há d20.
5. **Ainda sobrou 1 PA.** O Dragão usa **Garras e Presas** (◈, 0 Mana) na Guerreira: rola de novo, sai 8 → 8+3 = **11** contra a Defesa 10, acerta, mais 2d6.
6. **No turno seguinte da Guerreira**, ela perde 1d4 de Vida pelo Queimando antes de agir — e vai continuar perdendo até alguém apagar o fogo.

**O que limitou as escolhas do Mestre:** o **PA** decide quantas coisas ele faz no turno (Baforada III sozinha consome os 3; Baforada II + Garras também dá 3; três Garras dão 3 rolagens separadas). O **Mana** decide quantas vezes na luta inteira — com 20 de Mana e sem recarga, cabem só duas Baforadas em Intensidade III (9 + 9 = 18) e o tanque seca. É justamente por isso que **Garras e Presas custa 0 Mana**: é o ataque de rotina que mantém o chefe relevante depois de gastar o combustível.

### Criatura a 0 de Vida morre

Personagens ficam [Caídos](../jogador/sistema-d20.md#chegando-a-0-de-vida) e rolam contra a morte. **Criaturas não**: chegou a zero, acabou. Nenhuma rolagem, nenhum turno de agonia.

É o que impede a mesa de travar — oito goblins derrotados seriam oito contagens paralelas pra você administrar. E preserva o peso da regra: rolar contra a morte é privilégio de quem tem nome.

!!! mestre "Exceção que vale usar"
    Um chefe ou NPC importante pode ficar Caído como um personagem, se você quiser a chance de capturá-lo vivo, ou o drama de vê-lo se arrastar. Aí é escolha sua, anunciada na hora — não regra.

### Vida é valor fixo

Sem rolagem: abra a ficha e use o número. Os valores desta tabela valem pra personagens de **nível 1 a 4** — grupos mais fortes usam a [Vida por faixa de nível](encontros.md#vida-por-faixa-de-nivel). A Vida foi calibrada contra o dano real que um grupo entrega: um **Comum cai em um ou dois golpes**, um **Treinado** aguenta 2-3, um **Formidável** absorve mais ou menos uma rodada inteira de um grupo de 4, e um **Lendário** dura 3-5 rodadas.

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

- **Defesa física** = Base de Resiliência + Agilidade + Couraça Natural
- **Defesa mental** = Base de Resiliência + Vontade

### Ataques: capangas são fixos, chefes decidem

**Comum e Treinado** têm ataques de **custo fixo**, sem Mana: o Mestre lê a linha e rola. É o que permite rodar oito capangas sem administrar oito reservas de recurso.

**Formidável e Lendário** são chefes: têm **Mana** e usam [Intensidade](../habilidades/regras.md#intensidade) como um jogador — o Mestre decide se gasta 1 PA num golpe rápido ou queima o turno inteiro numa Intensidade III. É onde a decisão tática vale a pena, porque é uma criatura só.

### Ação de Lenda

Exclusiva do Tier Lendário: **uma vez por rodada, fora do próprio turno**, a criatura pode usar uma habilidade sua pagando o custo normal. É o que evita que um Lendário sozinho seja simplesmente cercado e morto sem reagir — ele responde no turno dos personagens.

---

## Criando uma Criatura

Você não precisa calcular nada: escolha o Tier e copie a coluna.

### Tabela de construção

| | Comum | Treinado | Formidável | Lendário |
|---|---|---|---|---|
| **Base de Resiliência** | 6 | 8 | 10 | 14 |
| **Vida** (nível 1–4) | 8 | 25 | 60 | 180 |
| **Pontos de Ação** | ◈ (1) | ◈◈ (2) | ◈◈◈ (3) | ◈◈◈ + Ação de Lenda |
| **Ataque** | +1 a +2 | +2 a +3 | +3 a +5 | +5 a +7 |
| **Dano por ataque** | 1d4 – 1d6 | 1d8 | 2d6 | 2d8 – 3d8 |
| **Mana** | — | — | 20 | 40 |
| **Couraça típica** | +0 a +1 | +1 a +2 | +2 a +3 | +3 a +4 |
| **Atributo principal** | +1 a +2 | +2 a +3 | +3 | +4 a +5 |
| **Traços especiais** | 1 | 1 a 2 | 2 a 3 | 3 a 4 |

Para grupos acima do nível 4, troque a linha de Vida pela [Vida por faixa de nível](encontros.md#vida-por-faixa-de-nivel). Todo o resto continua igual.

No **Ataque**, use o topo da faixa quando a criatura for precisa ou treinada, e o piso quando for desajeitada ou lenta. Nas criaturas deste livro: [Lobo](#lobo) +2 (caçador), [Goblin](#goblin) +1 (desajeitado), [Bandido](#bandido) +2 (competente, não excepcional).

!!! mestre "Os valores são ponto de partida, não algema"
    Desviar é o que dá personalidade — e desviar *pra baixo* também é desviar: o [Slime](#slime) tem Ataque +0 e Defesa física 4, abaixo de qualquer faixa, porque é lento e não desvia de nada. Ele compensa em outro lugar (imunidades e a *Divisão*). Se você tirar de um canto, devolva em outro.

### Os cinco passos

**1. Escreva o conceito em uma frase.** Não os números — a frase. *"Ele não ataca o mais forte do grupo, ataca o que se afastou."* Tudo depois disso é consequência dela: se o conceito é caçar quem se separou, o bicho precisa de Movimento alto e de um bônus contra alvo isolado.

**2. Escolha o Tier pela função na cena, não pelo tamanho do bicho.** Um urso enorme que serve de obstáculo de estrada é **Treinado**; um assassino humano magro que é o vilão do arco é **Formidável**. O Tier responde "quanto de atenção essa criatura merece nesta mesa", não "quantos quilos ela tem".

**3. Copie a coluna** — Vida, PA, Ataque, dano, Couraça. Some as Defesas:
   - **Defesa física** = Base + Agilidade + Couraça
   - **Defesa mental** = Base + Vontade

**4. Escolha os atributos que a frase pede, e só eles.** Comuns e Treinados listam **apenas o que importa**; o resto vale 0 por omissão. Um lobo tem Agilidade, Vitalidade e Sabedoria (faro) — não precisa de Inteligência nem Sanidade. Chefes (Formidável e Lendário) listam os 8, porque contra eles os jogadores vão tentar de tudo: charme, medo, veneno, ilusão.

**5. Dê os traços especiais — é aqui que a criatura nasce.** Os números do passo 3 fazem duas criaturas do mesmo Tier serem idênticas; os traços são o que as separa. Um Comum tem 1, um Lendário tem 3 ou 4.

### O que cada campo da ficha faz por você

| Campo | Para que serve na mesa | Vem de |
|---|---|---|
| **Tier** | resume a ameaça e define quase todo o resto | sua escolha |
| **Vida** | quantos golpes a criatura aguenta | tabela, pelo Tier |
| **PA** | quantas coisas ela faz por turno — a primeira medida de ameaça | tabela, pelo Tier |
| **Ataque** | o número que o Mestre soma no d20, já pronto | tabela, ±1 pelo conceito |
| **Defesa física** | o alvo que o jogador precisa superar pra acertar | Base + Agilidade + Couraça |
| **Defesa mental** | o alvo de charme, medo, provocação e teste social | Base + Vontade |
| **Iniciativa** | bônus somado ao d20 na ordem de turnos | Sorte (0 na maioria) |
| **Couraça** | só a Defesa física; não protege de veneno nem medo | conceito (couro, escamas, placas) |
| **Atributos** | o valor usado quando algo incomum é testado nela | conceito |
| **Movimento** | quantas casas anda por PA gasto | 3 + Agilidade |
| **Mana** | só chefes: quantas vezes usam as habilidades boas na luta | tabela, pelo Tier |

### Três tipos de traço, e o que cada um resolve

Traço é o que transforma estatística em criatura. Pensando no que você quer que aconteça na mesa:

- **Traço que muda o alvo** — faz a criatura ameaçar quem normalmente está seguro. *Matilha* (Vantagem quando cercam), *Bando* (+1d4 com aliado adjacente), a Mordida do Lobo derrubando quem está sozinho. Estes forçam o grupo a se reposicionar.
- **Traço que muda a solução** — faz a ferramenta importar mais que o dano. A [Vulnerabilidade](../glossario.md#vulnerabilidade) a Impacto do Esqueleto, a *Divisão* do Slime, uma imunidade a fogo. Estes recompensam preparação e conhecimento.
- **Traço que muda o tempo** — faz a luta não acabar quando parecia. *Remontar* do Esqueleto, cura, invocação de reforços, uma segunda forma. Estes criam clímax, e são os mais fortes: use no máximo um por criatura.

!!! cuidado "Combine no máximo dois"
    Uma criatura com quatro traços não é interessante, é uma ficha que o Mestre esquece de aplicar no meio do combate.

### Exemplo: do conceito à ficha

**Conceito:** *"Uma aranha gigante que não persegue — ela espera na teia, e quem se solta chega machucado."*

Isso pede: um Treinado (obstáculo sério, não vilão), veneno, e algo que prenda. Copiando a coluna Treinado e desviando onde a frase pede:

**Aranha das Cavernas**

*Ela não persegue. Ela espera — e a teia trabalha por ela.*

- **Tier:** Treinado | **Vida:** 25 | **PA:** ◈◈ (2) | **Iniciativa:** +0
- **Ataque:** +3 | **Defesa física:** 11 | **Defesa mental:** 8
- **Atributos:** Agilidade +1, Vitalidade +2, Sabedoria +2 (sente vibração) | **Couraça:** Escamada (+2, quitina)

**Mordida Peçonhenta** — ◈ | +3 vs Defesa física | 1 criatura adjacente

- **1d8** de dano ([Perfurante](../glossario.md#perfurante)) + o alvo fica [Envenenado](../glossario.md#envenenado).

**Teia** — ◈ | +3 vs Defesa física | 1 criatura a até 6 casas

- O alvo fica [Imóvel](../glossario.md#imovel) até se soltar: gastar uma Ação Básica e sofrer 1d4 de dano ao arrancar a teia.

**Sentinela da Teia** *(passiva)*

- Enquanto estiver na própria teia, a Aranha rola ataques com **Vantagem** e não pode ser derrubada.

Repare no que veio de onde: **Vida, PA, Ataque e dano saíram direto da tabela**. Agilidade +1 (em vez de +2 ou +3) veio da frase — ela não persegue, então não precisa ser rápida. Os dois traços cobrem tipos diferentes: *Teia* muda o alvo (prende quem tentava passar), *Sentinela* muda o terreno (lutar na teia dela é pior). E o veneno não é um terceiro traço — é o dano dela, do tipo que continua depois.

---

## Goblin

*Baixo, magro e covarde sozinho — mas eles nunca estão sozinhos.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Iniciativa:** +0
- **Ataque:** +1 | **Defesa física:** 8 | **Defesa mental:** 6
- **Atributos:** Agilidade +1, Vitalidade -1 | **Couraça:** Coriácea (+1)

**Adaga Enferrujada** — ◈ | +1 vs Defesa física | 1 criatura adjacente

- **1d4** de dano ([Perfurante](../glossario.md#perfurante)).

**Bando** *(passiva)*

- Se houver outro Goblin adjacente ao mesmo alvo, o ataque causa **+1d4**. Goblin é ameaça por quantidade, não por indivíduo.

**Covardia** *(passiva)*

- Ao ficar com 3 ou menos de Vida, usa seu PA pra fugir pela rota mais segura, se houver. Não é medo mecânico — é o Mestre jogando o bicho como ele é.

## Lobo

*Ele não ataca o mais forte do grupo. Ataca o que se afastou.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Iniciativa:** +0
- **Ataque:** +2 | **Defesa física:** 9 | **Defesa mental:** 6
- **Atributos:** Agilidade +2, Vitalidade +1, Sabedoria +1 | **Couraça:** Coriácea (+1)
- **Movimento:** 5 casas — mais rápido que a maioria dos personagens

**Mordida** — ◈ | +2 vs Defesa física | 1 criatura adjacente

- **1d6** de dano ([Perfurante](../glossario.md#perfurante)). Se o alvo estiver sozinho (nenhum aliado dele adjacente), **derruba** também.

**Matilha** *(passiva)*

- O ataque rola com **Vantagem** se outro Lobo estiver adjacente ao mesmo alvo.

**Faro** *(passiva)*

- Não pode ser surpreendido por criatura que dependa apenas de ocultação visual.

## Bandido

*Sabe exatamente onde doer, e cobra pela informação.*

- **Tier:** Treinado | **Vida:** 25 | **PA:** ◈◈ (2) | **Iniciativa:** +0
- **Ataque:** +2 | **Defesa física:** 11 | **Defesa mental:** 9
- **Atributos:** Força +2, Agilidade +2, Vitalidade +1, Vontade +1 | **Couraça:** Coriácea (+1)

**Espada Curta** — ◈ | +2 vs Defesa física | 1 criatura adjacente

- **1d8** de dano ([Cortante](../glossario.md#cortante)).

**Golpe Sujo** — ◈◈ | +2 vs Defesa física | 1 criatura adjacente

- **1d8** de dano + o alvo fica [Sangrando](../glossario.md#sangrando). Contra alvo já derrubado, **2d8** em vez de 1d8.

**Recuar e Atirar** — ◈◈ | +2 vs Defesa física | 1 criatura a até 8 casas

- Afasta-se até 3 casas e dispara uma besta de mão: **1d6** de dano ([Perfurante](../glossario.md#perfurante)).

## Esqueleto

*Cortar não resolve. Ele não tem o que sangrar.*

- **Tier:** Treinado | **Vida:** 25 | **PA:** ◈◈ (2) | **Iniciativa:** +0
- **Ataque:** +2 | **Defesa física:** 10 | **Defesa mental:** imune a efeito mental
- **Atributos:** Força +2, Agilidade +0, Vitalidade +3 | **Couraça:** Escamada (+2, ossos e escudo velho)
- **Imunidades:** [Sangrando](../glossario.md#sangrando), [Envenenado](../glossario.md#envenenado), veneno, doença, e **todo efeito mental** (medo, charme, provocação, ilusão) — não há mente pra atingir
- **Resistência:** [Cortante](../glossario.md#cortante) e [Perfurante](../glossario.md#perfurante) — lâmina e ponta não têm o que rasgar num esqueleto
- **Vulnerabilidade:** [Impacto](../glossario.md#impacto) — osso quebra; martelos e maças causam o **dobro**

**Lâmina Antiga** — ◈ | +2 vs Defesa física | 1 criatura adjacente

- **1d8** de dano ([Cortante](../glossario.md#cortante)).

**Investida de Ossos** — ◈◈ | +2 vs Defesa física | 1 criatura a até o Movimento

- Avança e golpeia: **1d8** de dano + **empurra 1 casa**.

**Remontar** *(passiva)*

- Ao chegar a 0 de Vida pela primeira vez, remonta-se no início do próprio próximo turno com **8 de Vida** — a não ser que o golpe final tenha sido de [Impacto](../glossario.md#impacto), ou que os ossos sejam espalhados (uma Ação Básica de um personagem adjacente resolve).

## Slime

*Bater com a espada só faz dois problemas onde havia um.*

- **Tier:** Comum | **Vida:** 8 | **PA:** ◈ (1) | **Iniciativa:** +0
- **Ataque:** +0 | **Defesa física:** 4 | **Defesa mental:** imune a efeito mental
- **Atributos:** Vitalidade +2, Agilidade -2 | **Couraça:** Nenhuma (+0)
- **Imunidades:** derrubar, empurrar, [Sangrando](../glossario.md#sangrando), veneno, e **todo efeito mental**
- **Resistência:** [Cortante](../glossario.md#cortante) e [Perfurante](../glossario.md#perfurante) — a lâmina atravessa a gelatina sem cortar nada

Defesa física 4 é de propósito: o Slime é lento e não desvia de nada. **Acertar é fácil; resolver não.**

**Investida Ácida** — ◈ | +0 vs Defesa física | 1 criatura adjacente

- **1d4** de dano, e o alvo fica [Envenenado](../glossario.md#envenenado) — o ácido continua corroendo.

**Divisão** *(passiva)*

- Quando sofre dano **[Cortante](../glossario.md#cortante) ou [Perfurante](../glossario.md#perfurante)** e sobrevive, o Slime se divide: surge um segundo Slime adjacente com metade da Vida atual (arredondada pra baixo, mínimo 1), e o original fica com a outra metade. Dano de [Impacto](../glossario.md#impacto), [Arcano](../glossario.md#arcano) e elemental não divide — esmaga ou queima.

## Dragão Filhote

*Ainda não voa bem. Já queima tudo.*

Primeiro chefe do Bestiário: usa **Mana e [Intensidade](../habilidades/regras.md#intensidade)**, e o Mestre decide quanto investir em cada turno, como um jogador faria.

- **Tier:** Formidável | **Vida:** 60 | **PA:** ◈◈◈ (3) | **Mana:** 20 | **Iniciativa:** +0
- **Ataque:** +3 | **Defesa física:** 15 | **Defesa mental:** 12
- **Atributos:** Força +3, Vitalidade +3, Agilidade +2, Inteligência +2, Sabedoria +1, Vontade +2, Sorte +0, Sanidade +2
- **Couraça:** Blindada (+3) | **Resistência:** fogo
- **Movimento:** 5 casas no chão, 8 voando — alçar voo custa ◈

**Garras e Presas** — ◈ | 0 Mana | +3 vs Defesa física | 1 criatura adjacente

- **2d6** de dano ([Cortante](../glossario.md#cortante)). É o ataque de rotina: não gasta Mana.

**Baforada** — +3 vs Defesa física | cone de 3 casas à frente

Assinatura do elemento [Fogo](../habilidades/magicas-elementais.md#fogo): quem é atingido pega fogo e continua queimando. O Mestre rola **uma vez** e compara o resultado com a Defesa física de cada alvo dentro do cone. Como toda habilidade, [a área não muda com a Intensidade](../habilidades/regras.md#intensidade) — o que cresce é o fogo.

- **Intensidade I — ◈ (1 PA) + 3 Mana:** **2d6** de dano em cada alvo + cada alvo fica [Queimando](../glossario.md#queimando)
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** **2d6** de dano + cada alvo fica [Queimando](../glossario.md#queimando), e o fogo se espalha para 1 criatura adjacente a cada alvo
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** **3d6** de dano + [Queimando](../glossario.md#queimando) causando 2d4 por turno, e o fogo se espalha para todas as criaturas adjacentes

**Voo Rasante** — ◈◈ | 2 Mana | +3 vs Defesa física | linha de 6 casas

- **2d6** de dano em cada criatura na linha, e o Dragão termina o movimento fora do alcance corpo a corpo de todas. Só pode ser usada se já estiver voando.

**Escamas Quentes** *(passiva)*

- Quem atinge o Dragão com ataque corpo a corpo sofre **1d4** de dano de fogo.
