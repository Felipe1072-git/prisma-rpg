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

**Defesa = 10 (base) + Agilidade + bônus de Armadura.**

*(Valores de bônus por armadura — a definir)*

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
