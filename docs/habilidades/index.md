# Habilidades

Não existem classes no Prisma RPG. Em vez disso, todas as habilidades do jogo são organizadas em **grupos temáticos**, e qualquer personagem pode escolher de qualquer grupo ao subir de nível.

## Grupos

| Grupo | Escopo |
|---|---|
| [Marciais](marciais.md) | Armas corpo a corpo / combate a curta distância |
| [Pontaria](pontaria.md) | Armas à distância e precisão (inclui feitiços de precisão) |
| [Mágicas Básicas](magicas-basicas.md) | Uso básico de magia |
| [Mágicas por Elemento](magicas-elementais.md) | Fogo, Gelo, Terra, Sombras, Luz, etc. |
| [Sociais](sociais.md) | Persuasão e afins |
| [Infiltração](infiltracao.md) | Furtividade, ladinagem |
| [Mobilidade](mobilidade.md) | Voo, deslocamento |
| [Buff](buff.md) | Incremento de força, imbuir elementos em armas, etc. |
| [Debuff](debuff.md) | Desvantagens para inimigos ou em testes |
| [Suporte](suporte.md) | Cura e apoio a aliados |

*(Lista de grupos pode crescer — ainda em definição com o usuário.)*

## Ficha de Habilidade

Cada habilidade é registrada com:

- **Nome**
- **Descrição breve** — 1 frase evocativa, deixando claro o que a habilidade faz
- **Chave** — para habilidades de arma: "Arma - Tier" (ex: "Espada - Básica"). Para habilidades gerais de grupo: "Grupo - Subtipo" (ex: "Marcial - Especial")
- **Custo em Mana**
- **Custo em Pontos de Ação (◈)** — 1, 2 ou 3, conforme o grau ou tipo de habilidade
- **Atributo** — atributo usado no teste (ex: FOR)
- **Efeitos / Alvos**
- **Tiers de Sucesso** (inspirado em Draw Steel) — o resultado do teste determina qual tier de efeito é aplicado
- **Crítico** — 20 natural

### Resolução

1. O usuário rola **d20 + Atributo da habilidade**.
2. **20 natural** sempre acerta e conta automaticamente como Tier 3 (além do bônus de dano do Crítico) — mesmo que o total não chegasse lá sozinho. **1 natural** sempre falha, sem nenhum efeito, independente do total.
3. Nos demais casos, o total precisa **igualar ou superar a Defesa do alvo** (ver [Defesa](sistema-d20.md#defesa)). Se não superar, a habilidade não causa nenhum efeito.
4. Se superar a Defesa, o total (sem ajuste) é comparado à tabela abaixo pra determinar o Tier:

| Tier | Total (d20 + Atributo) |
|---|---|
| Tier 1 (fraco) | ≤ 10 |
| Tier 2 (médio) | 11–16 |
| Tier 3 (forte) | ≥ 17 |
| Crítico | 20 natural — sempre acerta, conta como Tier 3, e soma dano máximo do dado + mais uma rolagem normal do mesmo dado |

Como a Defesa da maioria dos alvos já é 11 ou mais, **Tier 1 na prática só ocorre contra alvos fracos ou despreparados** (Defesa ≤10) — contra a maioria dos inimigos, o pior resultado que ainda causa efeito já é Tier 2.

Habilidades sem teste de ataque (buffs puros, efeitos automáticos como uma Habilidade Suprema inevitável) não precisam de Tiers de Sucesso nem checam Defesa — o efeito simplesmente acontece, sem rolagem.
