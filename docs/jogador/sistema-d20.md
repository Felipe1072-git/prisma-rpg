# O Sistema d20

## Criação de Personagem

Um personagem de nível 1 é composto por:

1. **Atributos** — distribuídos por um dos 3 métodos abaixo (ver [Distribuição na Criação](#distribuição-na-criação)).
2. **Raça** — pool de atributos + 1-3 traços raciais (ver [Raças](../racas/index.md)).
3. **Origem** — 3 escolhas independentes (Passado, Ambiente de Origem, Evento Formador), cada uma com 1 traço leve (ver [Origem](origem.md)).
4. **1ª Habilidade** — de qualquer grupo, inclusive a Básica de uma arma (ver [Progressão de Nível](#progressão-de-nível) abaixo).
5. **Equipamento inicial** — a arma (ou armas) que o personagem carrega fisicamente, escolhida livremente (frequentemente sugerida por um [Pacote](../pacotes/index.md)).

**Ter uma arma em mãos e saber uma técnica nomeada dela são coisas diferentes.** Qualquer arma equipada pode ser usada com **Ataque Básico** (dano da arma, sem nenhum efeito extra — ver [Pontos de Ação](pontos-de-acao.md)), mesmo que o personagem nunca tenha aprendido nenhuma Habilidade daquela arma. Aprender a Habilidade Básica de uma arma (gastando uma escolha de nível) é o que desbloqueia a técnica nomeada e as três [Intensidades](../habilidades/index.md#intensidade) dela — e é sempre o primeiro passo: a Avançada e a Especial de uma arma só podem ser aprendidas depois da Básica (e da Avançada, respectivamente) daquela mesma arma (ver "Aprendizado progressivo" no topo do [Arsenal](arsenal.md)).

## Atributos

Personagens possuem 8 atributos:

| Atributo | Representa |
|---|---|
| Força | Poder físico bruto — ataques marciais pesados, testes de força bruta |
| Vitalidade | Resistência física — define o dado de Vida a cada nível |
| Agilidade | Reflexos e velocidade — ataques à distância/furtivos, Defesa, Movimento |
| Inteligência | Raciocínio e poder arcano — ataques de magias arcanas |
| Sabedoria | Percepção e intuição — Suporte/cura, percepção |
| Vontade | Força de vontade e presença (equivalente a Carisma neste sistema) — testes sociais, resistir controle mental, Mana Máximo |
| Sorte | Acaso e fortuna — [Iniciativa](#iniciativa), usos de [Rerolagem](#rerolagens) |
| Sanidade | Estabilidade mental — Estresse Máximo, resistir horror/pânico |

Atributos podem assumir valores negativos (ex: por penalidades, dano, debuffs).

**Na criação, cada atributo começa entre -2 e +3.** Um atributo bem focado ao longo de toda a carreira pode chegar a aproximadamente **+13** no nível 20 (ver [Progressão de Nível](#progressão-de-nível) abaixo).

### Distribuição na Criação

O grupo escolhe um dos três métodos abaixo pra distribuir os atributos iniciais — todos calibrados pro mesmo teto de poder:

**Array Fixo** — valores pré-definidos `+3, +2, +1, +1, 0, 0, -1, -2`, distribuídos livremente entre os 8 atributos.

**Rolagem** — role **1d6-3** pra cada um dos 8 atributos (resultado de -2 a +3), e distribua os 8 resultados livremente entre os atributos.

**Ponto-compra** — orçamento de **7 pontos**, gasto conforme a tabela:

| Valor | Custo |
|---|---|
| -2 | -2 (devolve 2 pontos) |
| -1 | -1 (devolve 1 ponto) |
| 0 | 0 |
| +1 | 1 |
| +2 | 3 |
| +3 | 5 |

## Progressão de Nível

O jogo tem **20 níveis**. O personagem ganha, alternando a cada nível:

- **Nível ímpar** — uma **nova Habilidade**, de qualquer [grupo](../habilidades/index.md#grupos)
- **Nível par** — **+1 ponto de Atributo**, a distribuir livremente entre os 8 atributos

| Nível | Ganho |
|---|---|
| 1 | 1ª Habilidade |
| 2 | +1 ponto de Atributo |
| 3 | 2ª Habilidade |
| 4 | +1 ponto de Atributo |
| 5 | 3ª Habilidade |
| 6 | +1 ponto de Atributo |
| 7 | 4ª Habilidade |
| 8 | +1 ponto de Atributo |
| 9 | 5ª Habilidade |
| 10 | +1 ponto de Atributo |
| 11 | 6ª Habilidade |
| 12 | +1 ponto de Atributo |
| 13 | 7ª Habilidade |
| 14 | +1 ponto de Atributo |
| 15 | 8ª Habilidade |
| 16 | +1 ponto de Atributo |
| 17 | 9ª Habilidade |
| 18 | +1 ponto de Atributo |
| 19 | 10ª Habilidade |
| 20 | +1 ponto de Atributo (final) |

**Ao fim do nível 20:** 10 Habilidades aprendidas (de qualquer grupo, em qualquer combinação) e +10 pontos de Atributo distribuídos, além do valor inicial de criação.

Vida e Mana crescem automaticamente todo nível, independente dessa tabela — ver [Vida](#vida) abaixo e [Mana](mana.md).

## Testes

Um teste é resolvido como **d20 + Atributo vs Dificuldade (DC)** definida pelo Mestre. Igualar ou superar a DC é sucesso.

Rolagens de Habilidade usam exatamente a mesma lógica, trocando a DC pela Defesa do alvo — igualou ou superou, acertou. O quanto a habilidade faz **não depende da rolagem**: depende da [Intensidade](../habilidades/index.md#intensidade) que o jogador pagou.

### Iniciativa

No início do combate, cada participante rola **d20 + Sorte**. A ordem decrescente do resultado define a sequência de turnos. Empate é resolvido por quem tem Sorte mais alta; persistindo o empate, o Mestre decide.

## Valores Derivados

### Vida

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

### Dados de Vida

Além de definirem a Vida máxima, os dados de Vida são o **recurso de recuperação** do personagem — é com eles que se cura fora de combate.

**O personagem tem um Dado de Vida por nível**, no tamanho atual da tabela acima. Um personagem de nível 6 com Vitalidade +4 tem **6d8** disponíveis.

Ao [descansar](../mestre/exploracao.md#descanso), o jogador escolhe quantos gastar e rola cada um, recuperando **o resultado rolado** em Vida. Não se soma Vitalidade — pela mesma razão que a Vida máxima também não soma: ela já está embutida no *tamanho* do dado, e somar de novo faria a cura passar da Vida total nos níveis altos.

| | Quantos pode gastar | Quantos voltam ao pool |
|---|---|---|
| **Descanso curto** (~1h) | até **metade do nível** (mínimo 1) | nenhum |
| **Descanso longo** (noite) | **todos** os que ainda tiver | **metade do nível** (mínimo 1), ao fim do descanso |

Os dados gastos **não voltam sozinhos**: só o descanso longo devolve, e devolve metade. Isso significa que uma sequência de dias difíceis vai esvaziando o poço — e a decisão de quantos dados queimar agora, sabendo que a noite só devolve parte, é o principal recurso de longo prazo do personagem.

**Na prática:** gastar o limite do descanso curto devolve cerca de **45% da Vida máxima**, e esvaziar o poço num descanso longo devolve perto de **90%**. Um dia de aventura consome mais ou menos o que a noite repõe, então o poço se sustenta em ritmo normal — e só afunda quando o grupo encara vários dias duros seguidos sem voltar pra base.

Cura por Habilidade (ver [Suporte](../habilidades/suporte.md)) **não** gasta Dados de Vida — é justamente por isso que ter um curandeiro no grupo importa: ele cura sem consumir o poço de ninguém.

### Base de Resiliência

Toda criatura (personagem ou monstro) tem uma **Base de Resiliência**, definida pelo nível de ameaça que ela representa — não pelo tamanho físico nem pela espécie. Um Lich não é fisicamente colossal, mas é Lendário o bastante pra ter a mesma Base de um dragão.

| Tier de Ameaça | Base | Exemplos |
|---|---|---|
| Comum | 6 | civis, animais pequenos, sem treino algum |
| Treinado | 8 | soldados, aventureiros, guardas experientes |
| Formidável | 10 | a maioria dos monstros, feras perigosas |
| Lendário | 14 | dragões, lichs, arqui-demônios, entidades cósmicas |

### Defesa

**Defesa = Base de Resiliência + o atributo relevante ao tipo de efeito** (+ bônus natural relevante, se houver). O padrão — ataques físicos, o caso mais comum — usa **Agilidade**. Habilidades que impõem outra coisa (um estado mental, uma doença, pânico) declaram explicitamente qual atributo testar; a fórmula é sempre a mesma, só troca o atributo.

**Um personagem jogador é Treinado** (Base 8) — a mesma linha de soldados e aventureiros experientes. Na prática:

- **Defesa física** = 8 + Agilidade + Armadura
- **Defesa mental** = 8 + Vontade
- e assim por diante, trocando o atributo conforme o efeito

Vale a pena anotar essas duas na ficha antes da sessão: são os números que o Mestre vai consultar a cada ataque de criatura.

### Quem rola o dado

**Quem age, rola.** Isso vale nos dois sentidos e é a única regra de resolução do jogo:

- O personagem ataca uma criatura → **o jogador** rola d20 + Atributo contra a Defesa da criatura.
- Uma criatura ataca o personagem → **o Mestre** rola d20 + o Ataque da criatura contra a Defesa do personagem.

Não existe rolagem de defesa: quem está sendo atacado não rola nada, seu número de Defesa é o alvo a ser superado. Ver [Bestiário](../mestre/bestiario.md#como-resolver-o-ataque-de-uma-criatura) para o lado do Mestre.

| Tipo de efeito | Atributo de Defesa | Bônus natural |
|---|---|---|
| Físico (dano, empurrar, derrubar) — padrão | Agilidade | Armadura/Couraça Natural *(a detalhar com o Bestiário/equipamentos)* |
| Mental/comportamental (charme, medo, provocação, controle) | Vontade | — |
| Veneno, doença, exaustão | Vitalidade | — |
| Horror, insanidade, colapso mental | Sanidade | — |
| Ilusão, engano | Sabedoria | — |
| Furtividade, detecção (perceber um roubo, um disfarce) | Sabedoria | — |

Essa lista não é fechada — cresce conforme habilidades novas pedirem.

A Defesa decide **se** o golpe acerta, nunca o quanto ele faz — isso já foi decidido pela [Intensidade](../habilidades/index.md#intensidade) paga. Por isso a Defesa do alvo pesa na escolha de quanto investir: contra um alvo Lendário (Base 14 + atributo), gastar 3 PA e o Mana de uma Intensidade III num único ataque é uma aposta alta — se errar, perde tudo e o turno inteiro. Contra alvos Comuns, a mesma Intensidade III praticamente não erra.

### Tipos de Dano

Todo dano tem um tipo, e é por isso que a arma escolhida importa contra certas criaturas. Os três primeiros são físicos, e vêm da arma empunhada (ver a coluna **Tipo** na [Tabela de Dados de Dano](arsenal.md#tabela-de-dados-de-dano)):

| Tipo | De onde vem | Contra o que costuma ser bom |
|---|---|---|
| **Cortante** | espadas, machados, foices, garras | carne e criaturas de tecido mole |
| **Perfurante** | lanças, adagas, flechas, projéteis | brechas de armadura, alvos volumosos |
| **Impacto** | martelos, bastões, punhos, manguais | ossos, cascas, armaduras rígidas, esqueletos |
| **Arcano** | focos mágicos, canalizações sem forma definida | quem depende de resistência física |

Habilidades de **Mágicas por Elemento** causam dano do próprio elemento (fogo, gelo, sombras...), não desses quatro — é o elemento que o alvo resiste ou não.

**Dano Desarmado** é sempre Impacto, salvo quando um traço racial disser outra coisa (garras naturais cortam).

### Resistência, Imunidade e Vulnerabilidade

Aplicadas a um tipo de dano — físico ou elemental — sempre **depois** de qualquer outro cálculo, incluindo Crítico:

| | Efeito |
|---|---|
| **Resistência** | o dano daquele tipo cai pela **metade** (arredondado pra baixo) |
| **Imunidade** | o dano daquele tipo é **ignorado** por completo (0) |
| **Vulnerabilidade** | o dano daquele tipo é **dobrado** |

Uma criatura nunca tem Resistência e Vulnerabilidade ao mesmo tipo; se algum efeito criar essa situação, as duas se cancelam e o dano é normal.

Vulnerabilidade é a ferramenta que transforma conhecimento em vantagem: descobrir que o morto-vivo cai mais rápido sob Luz, ou que a criatura de gelo derrete no Fogo, vale mais que um bônus numérico — e é o que faz um grupo trocar de arma antes de entrar na masmorra.

## Testes Sociais

Persuadir, Intimidar, Amedrontar.

Resolvidos como teste normal (ver [Testes](#testes) acima).

## Rerolagens

O jogador pode rerolar qualquer teste seu, ou um efeito usado contra si.

**Usos por descanso longo = 1 + Sorte** (mínimo 1). A grade reseta completamente a cada descanso longo.

## Estresse

O personagem recebe Estresse ao sofrer um crítico, ao tirar uma falha crítica (1 natural) em qualquer teste, ou quando o Mestre pede um teste de Estresse.

**Estresse máximo = 10 + Sanidade.**

Ao ser pedido um teste de Estresse, o jogador rola **d20 + Sanidade vs DC do Mestre**. Se falhar, marca 1-2 pontos de Estresse.

Estresse não reseta com descanso curto — representa desgaste acumulado.

### Colapso

Ao encher a barra de Estresse, o personagem sofre um surto imediato — o Mestre escolhe ou rola 1d6 na tabela abaixo. Cada surto define seu próprio efeito e duração.

| d6 | Surto |
|---|---|
| 1 | **Fuga** — foge da cena pelo caminho mais direto e seguro, ignorando perigo no caminho. Dura até sair de vista e alcance de todos os presentes; a partir daí, fica **Indisponível pelo resto da cena** (não volta a tempo de ajudar) |
| 2 | **Pânico** — trava completamente por **1 rodada completa**, gritando ou paralisado, sem realizar nenhuma ação. Ao fim da rodada volta a agir normalmente |
| 3 | **Fúria Cega** — ataca a criatura mais próxima (aliada ou inimiga, sem escolha do jogador) com o que tiver em mãos, uma única vez. Depois desse ataque o surto termina e ele volta a agir normalmente no turno seguinte |
| 4 | **Colapso Físico** — desmaia imediatamente, caindo no chão e ficando Indisponível. Volta a si sozinho após **1d4 rodadas**, ou imediatamente se um aliado gastar uma ação adjacente pra acordá-lo |
| 5 | **Dissociação** — grita ou chora sem controle e larga tudo que estava segurando. Dura até o fim do turno atual; no turno seguinte já pode agir normalmente, mas precisa gastar uma ação pra reequipar o que soltou |
| 6 | **Bloqueio** — para completamente, repetindo a mesma frase ou ação sem sentido, alheio ao redor. Dura até um aliado gastar uma ação adjacente pra trazê-lo de volta, ou até o fim da cena — o que vier primeiro |

Depois do surto, a barra reseta a 0 e o personagem ganha uma **Cicatriz**: uma condição negativa permanente, escolhida ou sorteada (d6) na tabela abaixo.

| d6 | Cicatriz |
|---|---|
| 1 | **Fobia Específica** — escolha um gatilho (fogo, sangue, altura, escuridão, multidão etc.); na presença dele, todos os testes sofrem Desvantagem até se afastar |
| 2 | **Gatilho de Fúria** — um evento específico (ver aliado cair, ser insultado etc.) força um teste de Estresse extra imediato |
| 3 | **Tique Nervoso** — Desvantagem no primeiro teste social de cada cena |
| 4 | **Isolamento** — recupera só metade do Estresse por Apoio Social (arredondado pra baixo) |
| 5 | **Paranoia** — Desvantagem em Iniciativa (sempre hesitante, desconfiado demais) |
| 6 | **Exaustão Crônica** — descanso curto não recupera Mana |

### Reduzindo Estresse

- **Descanso longo** — remove **1d6** de Estresse
- **Vício** — durante um descanso, o personagem pode se entregar a um vício pessoal escolhido na criação (bebida, jogo, violência, isolamento etc.) pra remover **1d6 de Estresse** adicional. Ao fazer isso, role 1d6: em um resultado de **1**, o vício gera uma complicação narrativa (dívida, inimigo, constrangimento público — Mestre decide conforme a cena)
- **Apoio social** — passar tempo com um aliado/vínculo remove **1** ponto de Estresse
