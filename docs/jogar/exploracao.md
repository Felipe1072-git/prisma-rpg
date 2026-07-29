# Exploração

Tudo o que acontece entre um combate e o outro: viajar, descansar, aguentar o mundo.

São regras que o **jogador** aplica — é aqui que se decide quanto do poço de recursos sobra pro próximo combate. O lado do Mestre (armadilhas, ritmo de masmorra, pressão de tempo) está em [Exploração na Mesa](../mestre/exploracao.md).

## Descanso

Duas escalas, e é delas que dependem as dezenas de habilidades que dizem "1x por descanso longo".

| | Dura | Recupera |
|---|---|---|
| **Descanso curto** | cerca de **1 hora** — respirar, enfaixar, comer algo | metade do [Mana](mana.md) máximo, e permite gastar até **metade do nível** em [Dados de Vida](dano-e-cura.md#dados-de-vida) |
| **Descanso longo** | uma **noite de sono** (~8 horas) em lugar minimamente seguro | todo o Mana; permite gastar **todos** os Dados de Vida restantes e devolve **metade do nível** ao pool; remove 1d6 de [Estresse](estresse.md) e 1 grau de [Exausto](../glossario.md#exausto) (este só se a causa foi resolvida — ver [Exaustão](#exaustao)); reseta habilidades "1x por descanso longo" e as [rerolagens](testes.md#rerolagens) |

!!! regra "Descanso longo precisa de segurança mínima"
    Dormir de armadura no chão de uma masmorra com criaturas rondando não conta — o grupo consegue no máximo um descanso curto. Isso não é punição: é a regra que faz "voltar pra cidade" ser uma decisão de verdade.

### A Vida volta, mas custa recurso

Diferente do Mana, a Vida **não se recupera sozinha** ao descansar: ela vem dos [Dados de Vida](dano-e-cura.md#dados-de-vida), que o personagem gasta e que só voltam pela metade a cada noite.

Na prática, isso cria a decisão que faz a exploração ter peso: *"curo agora e chego fraco no fim da masmorra, ou aguento machucado e guardo o poço?"*. E é o que dá valor real a quem investiu em [Cura](../habilidades/suporte.md) — a cura por Habilidade não consome Dado de Vida de ninguém, então um curandeiro no grupo literalmente economiza o recurso de longo prazo dos companheiros.

## Viagem

Distância se mede em **trechos**. Um trecho é **meio dia de marcha** — a mesma abstração das "casas" no combate: não vale em quilômetros, vale em relação aos outros trechos.

| Ritmo | Trechos por dia | O que custa, o que ganha |
|---|---|---|
| **Cauteloso** | 1 | [Vantagem](../glossario.md#vantagem) pra notar perigo, emboscada ou rastro; ninguém se cansa |
| **Normal** | 2 | nada de especial — é o padrão |
| **Forçado** | 3 | ao fim do dia, cada personagem ganha **1 grau de [Exausto](../glossario.md#exausto)** |

O Mestre diz as distâncias em trechos: *"a torre fica a cinco trechos, ou três se cortarem pelo pântano"*. Isso já é ferramenta de decisão — o atalho é mais curto e pior.

!!! regra "Terreno pesado dobra a conta"
    Em [Terreno Difícil](../glossario.md#terreno-dificil) — pântano, montanha, neve funda, mata fechada — cada trecho conta como **dois**. É a mesma lógica do combate, na escala da estrada.

**Montaria** troca cansaço por dinheiro: um cavalo (200 p) permite ritmo Forçado sem ganhar Exausto, mas o animal precisa de descanso, água e não sobe montanha.

### Quem faz o quê na estrada

Cada personagem pode assumir **uma** função por dia de viagem. Isso dá papel a quem não luta e transforma viagem em cena em vez de narração:

| Função | Teste | Se passar |
|---|---|---|
| **Guiar** | Sabedoria vs DC do terreno | o grupo não se perde nem gasta trecho extra |
| **Vigiar** | Sabedoria (DC 12) | passando, o grupo **não** fica [Desprevenido](../glossario.md#desprevenido) numa emboscada; sem ninguém vigiando (ou falhando), o grupo começa o combate Desprevenido |
| **Forragear** | Sabedoria vs DC 12 | comida e água pra todos naquele dia |
| **Rastrear** | Sabedoria vs DC do rastro | descobre o que passou por ali, quando e quantos |

As DCs vêm da [tabela de Dificuldades](../mestre/testes.md#a-tabela) — estrada conhecida é DC 5, floresta densa DC 15, pântano sem trilha DC 20.

## Exaustão

[Exausto](../glossario.md#exausto) acumula em graus, e é como o mundo cobra de quem não se cuida:

| Grau | Efeito (acumulativo) |
|---|---|
| 1 | [Desvantagem](../glossario.md#desvantagem) em todos os testes |
| 2 | também fica [Lento](../glossario.md#lento) |
| 3 | cai inconsciente até receber ajuda ou descansar |

**Ganha 1 grau** a cada:

- **dia sem comida ou água** (a partir do segundo dia sem — o primeiro só incomoda)
- **noite sem descanso longo adequado**, quando o grupo já vinha de um dia de viagem
- **dia de ritmo Forçado**
- **dia exposto a clima extremo** sem proteção adequada (ver abaixo)

**Remove 1 grau** por descanso longo — **desde que a causa esteja resolvida**. Dormir com fome não remove nada, e é isso que faz a comida virar item de verdade sem precisar de planilha de peso.

## Clima extremo

Duas origens do jogo já concedem resistência a isso ([Deserto](../jogador/origem.md#ambiente-de-origem) e Tundra), então a regra precisa existir pra que o traço signifique algo.

| Clima | Sem proteção adequada |
|---|---|
| **Calor extremo** | 1 grau de Exausto por dia, e o consumo de água dobra |
| **Frio extremo** | 1 grau de Exausto por dia, e descanso longo ao relento não recupera Mana |
| **Tempestade, nevasca** | Terreno Difícil em todo lugar, e Desvantagem pra Vigiar e Rastrear |

**Proteção adequada** é o que a ficção pedir: roupa apropriada, abrigo, fogo, uma habilidade de elemento oposto. Quem tem a origem **Deserto** ignora calor extremo (e gasta metade da água e comida); quem tem **Tundra** ignora frio extremo.

## Água

A regra que vários traços de [Raça](../racas/index.md) e [Origem](../jogador/origem.md) modificam (Marinheiro, Costa, Pântano, Ilha, Sereia, Golfinho, Respiração Aquática):

- **Nadar:** água funda é [Terreno Difícil](../glossario.md#terreno-dificil) — cada casa custa o dobro de [Movimento](combate.md#movimento). Traços de "sem penalidade em água" ignoram esse pedágio; bônus como "+4 de Movimento na água" somam por cima.
- **Fôlego:** debaixo d'água, um personagem aguenta **1 + Vitalidade** rodadas (mínimo 1) antes de começar a se afogar. Afogando, sofre **1 grau de [Exausto](../glossario.md#exausto) por rodada** até respirar — quem chega ao grau 3 desmaia e passa a rolar como [Caído](dano-e-cura.md#chegando-a-0-de-vida). Quem respira na água ignora tudo isso.
- **Combate na água:** sem um traço aquático, ataques corpo a corpo rolam com Desvantagem e armas de Pontaria não funcionam submersas.

## Luz e escuridão

A origem **Subterrâneo** concede "sem Desvantagem por escuridão parcial" e o traço élfico **Visão no Escuro** promete enxergar no escuro total — as duas dependem desta regra.

| Iluminação | Efeito |
|---|---|
| **Luz plena** | nada |
| **Escuridão parcial** (crepúsculo, tocha ao longe, névoa) | Desvantagem em testes que dependam de ver: perceber, mirar à distância, rastrear |
| **Escuridão total** | só é possível agir contra o que estiver **adjacente**; ataques à distância são impossíveis, e todo teste visual falha |

**Visão no Escuro** (traço racial) ignora as duas linhas: quem tem enxerga normalmente. **Subterrâneo** (origem) ignora só a escuridão parcial.

Uma tocha ilumina o suficiente pra anular a escuridão parcial ao redor de quem a carrega — e denuncia a posição dele a qualquer coisa que esteja olhando. Esse é o preço, e é o que faz a decisão de acender ou não ser interessante.
