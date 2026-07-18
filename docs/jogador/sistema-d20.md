# O Sistema d20

## Atributos

Personagens possuem 8 atributos:

- Força
- Vitalidade
- Agilidade
- Inteligência
- Sabedoria
- Vontade
- Sorte
- Sanidade

*(Descrição de cada atributo — a definir)*

Atributos podem assumir valores negativos (ex: por penalidades, dano, debuffs).

**Na criação, cada atributo começa entre -2 e +3** (método exato de distribuição — array fixo, ponto-compra ou rolagem — a definir). Um atributo bem focado ao longo de toda a carreira pode chegar a aproximadamente **+13** no nível 20 (ver [Progressão de Nível](#progressão-de-nível) abaixo).

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

## Testes Sociais

Persuadir, Intimidar, Amedrontar.

Resolvidos como teste normal (ver [Testes](#testes) acima).

## Rerolagens

O jogador pode rerolar qualquer teste seu, ou um efeito usado contra si. Os usos são controlados numa grade que reseta ao descansar.

*(Número de usos por descanso — a definir)*

## Estresse

O personagem recebe Estresse ao sofrer um crítico, ao tirar uma falha crítica (1 natural) em qualquer teste, ou quando o Mestre pede um teste de Estresse.

**Estresse máximo = 10 + Sanidade.**

Ao ser pedido um teste de Estresse, o jogador rola **d20 + Sanidade vs DC do Mestre**. Se falhar, marca 1-2 pontos de Estresse.

Estresse não reseta com descanso curto — representa desgaste acumulado.

### Colapso

Ao encher a barra de Estresse, o personagem sofre um surto imediato (foge, entra em pânico, ataca o aliado mais próximo, desmaia — Mestre escolhe ou rola numa tabela de surtos, *a criar*) e fica **Indisponível** pelo resto da cena.

Depois do surto, a barra reseta a 0 e o personagem ganha uma **Cicatriz**: uma condição negativa permanente (fobia, tique, gatilho específico etc.), escolhida ou sorteada numa tabela de Cicatrizes (*a criar*).

### Reduzindo Estresse

- **Descanso longo** — remove **1d6** de Estresse
- **Vício** — o personagem pode se entregar a um vício pessoal (bebida, jogo, violência, isolamento) durante tempo de descanso pra remover mais Estresse, mas corre risco de uma complicação (*a definir*)
- **Apoio social** — passar tempo com um aliado/vínculo remove **1** ponto de Estresse
