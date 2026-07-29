# Dano e Cura

Quanto você aguenta, o que te machuca mais, como você se recupera — e o que acontece quando a Vida chega a zero.

## Vida

**Vida = 10 (base, nível 1) + soma dos dados de vida rolados a cada nível.**

O tamanho do dado rolado em cada nível depende da Vitalidade do personagem *naquele momento*:

| Vitalidade | Dado de Vida |
|---|---|
| 0–1 | d4 |
| 2–3 | d6 |
| 4–5 | d8 |
| 6–7 | d10 |
| 8+ | d12 |

Vida é cumulativa: o dado de cada nível fica "congelado" no total quando rolado — não há recálculo retroativo se a Vitalidade mudar depois.

## Dados de Vida

Além de definirem a Vida máxima, os dados de Vida são o **recurso de recuperação** do personagem — é com eles que se cura fora de combate.

**O personagem tem um Dado de Vida por nível**, no tamanho atual da tabela acima. Um personagem de nível 6 com Vitalidade +4 tem **6d8** disponíveis.

Ao [descansar](exploracao.md#descanso), o jogador escolhe quantos gastar e rola cada um, recuperando **o resultado rolado** em Vida. Não se soma Vitalidade — pela mesma razão que a Vida máxima também não soma: ela já está embutida no *tamanho* do dado, e somar de novo faria a cura passar da Vida total nos níveis altos.

| | Quantos pode gastar | Quantos voltam ao pool |
|---|---|---|
| **Descanso curto** (~1h) | até **metade do nível** (mínimo 1) | nenhum |
| **Descanso longo** (noite) | **todos** os que ainda tiver | **metade do nível** (mínimo 1), ao fim do descanso |

Os dados gastos **não voltam sozinhos**: só o descanso longo devolve, e devolve metade. Isso significa que uma sequência de dias difíceis vai esvaziando o poço — e a decisão de quantos dados queimar agora, sabendo que a noite só devolve parte, é o principal recurso de longo prazo do personagem.

!!! exemplo "Na prática"
    Gastar o limite do descanso curto devolve cerca de **45% da Vida máxima**, e esvaziar o poço num descanso longo devolve perto de **90%**. Um dia de aventura consome mais ou menos o que a noite repõe, então o poço se sustenta em ritmo normal — e só afunda quando o grupo encara vários dias duros seguidos sem voltar pra base.

## Cura por Habilidade

Cura por Habilidade (ver [Suporte](../habilidades/suporte.md)) **não** gasta Dados de Vida — é justamente por isso que ter um curandeiro no grupo importa: ele cura sem consumir o poço de ninguém.

Como toda habilidade, cura tem [Intensidade](../habilidades/regras.md#intensidade): não há teste de acerto, mas o tamanho do efeito escala com o quanto você paga.

## Tipos de Dano

Todo dano tem um tipo, e é por isso que a arma escolhida importa contra certas criaturas. Os três primeiros são físicos, e vêm da arma empunhada (ver a coluna **Tipo** na [Tabela de Dados de Dano](../equipamento/regras.md#tabela-de-dados-de-dano)):

| Tipo | De onde vem | Contra o que costuma ser bom |
|---|---|---|
| **[Cortante](../glossario.md#cortante)** | espadas, machados, foices, garras | carne e criaturas de tecido mole |
| **[Perfurante](../glossario.md#perfurante)** | lanças, adagas, flechas, projéteis | brechas de armadura, alvos volumosos |
| **[Impacto](../glossario.md#impacto)** | martelos, bastões, punhos, manguais | ossos, cascas, armaduras rígidas, esqueletos |
| **[Arcano](../glossario.md#arcano)** | focos mágicos, canalizações sem forma definida | quem depende de resistência física |

Habilidades de **[Mágicas por Elemento](../habilidades/magicas-elementais.md)** causam dano do próprio elemento (fogo, gelo, sombras...), não desses quatro — é o elemento que o alvo resiste ou não.

**Dano Desarmado** é sempre Impacto, salvo quando um traço racial disser outra coisa (garras naturais cortam).

## Resistência, Imunidade e Vulnerabilidade

Aplicadas a um tipo de dano — físico ou elemental — sempre **depois** de qualquer outro cálculo, incluindo Crítico:

| | Efeito |
|---|---|
| **[Resistência](../glossario.md#resistencia)** | o dano daquele tipo cai pela **metade** (arredondado pra baixo) |
| **[Imunidade](../glossario.md#imunidade)** | o dano daquele tipo é **ignorado** por completo (0) |
| **[Vulnerabilidade](../glossario.md#vulnerabilidade)** | o dano daquele tipo é **dobrado** |

Uma criatura nunca tem Resistência e Vulnerabilidade ao mesmo tipo; se algum efeito criar essa situação, as duas se cancelam e o dano é normal. Duas Resistências ao mesmo tipo também não somam — ver [Acúmulo de bônus](../glossario.md#acumulo-de-bonus).

Vulnerabilidade é a ferramenta que transforma conhecimento em vantagem: descobrir que o morto-vivo cai mais rápido sob Luz, ou que a criatura de gelo derrete no Fogo, vale mais que um bônus numérico — e é o que faz um grupo trocar de arma antes de entrar na masmorra.

## Chegando a 0 de Vida

Zero não é morte. O personagem fica **Caído**: inconsciente, sem agir, sem rolar nada — e morrendo devagar.

**No início de cada turno dele, role d20 contra DC 10.** Falhando, ele piora. O tanto que ele aguenta piorar antes de morrer é a **Vitalidade** dele (mínimo 1):

| Vitalidade | Falhas até morrer | Quanto tempo aguenta, em média |
|---|---|---|
| 0 ou menos | 1 | ~2 turnos |
| +2 | 2 | ~4 turnos |
| +4 | 4 | ~9 turnos |
| +8 | 8 | ~18 turnos |

A Vitalidade **não** entra na rolagem — ela já está representada em quantas falhas o corpo suporta. O dado mede só a sorte do momento, e é igual pra todos.

**Como sair de Caído:**

- **Estabilizar** — um aliado adjacente gasta uma **Ação Básica** (◈). O personagem para de rolar e fica **Estável**: segue inconsciente, mas fora de risco. Acorda ao fim da cena com 1 de Vida. (As origens *Curandeiro de Vila* e *Salvou uma Vida* fazem isso como Reação e sem custo — ver [Origem](../origens/index.md).)
- **Cura** — qualquer efeito que devolva Vida traz o personagem de volta com aquela Vida, e ele age normalmente no próximo turno.

Sofrer dano enquanto Caído conta como **uma falha imediata**, além da rolagem do turno.

Isso vale só pros personagens jogadores: uma **criatura a 0 de Vida morre** (ver [Bestiário](../mestre/criando-criaturas.md#criatura-a-0-de-vida-morre)).

## O Último Turno

Um personagem Caído pode escolher **não resistir**. Em vez de rolar contra a morte, ele decide que aquele é o fim — e se levanta pra gastar tudo o que resta.

Declarado no início de um turno dele enquanto estiver Caído, o Último Turno funciona assim:

- Ele **se levanta e joga um turno completo**: 3 PA, Mana, habilidades, tudo. Ainda rola pra acertar normalmente.
- **Todo sucesso é tratado como Crítico** — dano máximo, rolagem extra e [sobe 1 Intensidade de graça](../habilidades/regras.md#resolucao), mesmo sem tirar 20.
- **Toda falha é tratada como falha crítica** — não há acerto raspado; o que dá errado, dá errado por completo.
- **Nenhuma cura funciona nele** durante o Último Turno. Não há como voltar atrás depois de declarar.
- **Ao fim do turno, o personagem morre.** Sem rolagem, sem resistência, sem chance. Foi o preço.

É a única escolha do sistema em que o jogador **troca a chance de sobreviver por certeza de impacto**. Um personagem que ia morrer de qualquer jeito em duas rodadas, sem agir, pode em vez disso derrubar o chefe com um golpe garantido como crítico — e sair de cena tendo decidido como.

!!! mestre "Cabe ao Mestre dar espaço pra isso"
    Se um jogador declara o Último Turno, a mesa para e escuta: é o momento daquele personagem, e ele não vai ter outro.
