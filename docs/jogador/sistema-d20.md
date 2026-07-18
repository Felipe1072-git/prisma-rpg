# O Sistema d20

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

Tiers de Sucesso (fraco/médio/forte) são exclusivos de rolagens de Habilidade — ver [Ficha de Habilidade](../habilidades/index.md#ficha-de-habilidade). Testes gerais usam sucesso/fracasso simples.

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

### Defesa

**Defesa = Base do arquétipo + Agilidade + bônus de Armadura/Couraça Natural.**

| Arquétipo | Base |
|---|---|
| Humanoide comum (sem treino) | 6 |
| Humanoide treinado (aventureiro, soldado) | 8 |
| Monstro comum | 10 |
| Monstro colossal (dragões, criaturas lendárias) | 14 |

*(Bônus de Armadura/Couraça Natural — a detalhar conforme o Bestiário e o sistema de equipamentos forem escritos.)*

Essa fórmula é calibrada de propósito pra ficar compatível com os [Tiers de Sucesso](../habilidades/index.md#ficha-de-habilidade): contra a maioria dos alvos (Defesa 11+), Tier 1 nunca acontece — o pior resultado que ainda causa efeito já é Tier 2. Tier 1 só é alcançável contra alvos fracos ou despreparados (Defesa ≤10). Contra monstros colossais, mesmo Tier 3 pode não ser suficiente sem um 20 natural.

### Resistência e Imunidade

**Resistência** a um tipo de dano (ex: um elemento) reduz esse dano pela metade (arredondado pra baixo). **Imunidade** ignora esse dano por completo (0 de dano). Ambas se aplicam depois de qualquer outro cálculo, incluindo Crítico.

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
