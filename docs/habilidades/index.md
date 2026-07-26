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
- **Chave** — para habilidades de arma: "Arma - Grau" (ex: "Espada - Básica"). Para habilidades gerais de grupo: "Grupo - Subtipo" (ex: "Marcial - Especial")
- **Atributo** — atributo usado no teste (ex: FOR)
- **Efeitos / Alvos**
- **Intensidade I / II / III** — as três versões da habilidade, cada uma com seu custo em Pontos de Ação e Mana
- **Crítico** — 20 natural

### Intensidade

Toda habilidade de ataque existe em **três Intensidades**. Elas não são compradas com escolhas de nível: estão todas disponíveis desde o momento em que o personagem aprende a habilidade. O que muda é quanto custa usar cada uma — o jogador decide **na hora de ativar**, conforme quanto do turno e do Mana quer investir.

| Intensidade | Pontos de Ação | O que ela entrega |
|---|---|---|
| I | ◈ (1) | O efeito base — normalmente só o dano |
| II | ◈◈ (2) | Acrescenta o efeito secundário (empurrar, Sangrando, Marcado) |
| III | ◈◈◈ (3) | O efeito completo (derrubar, Atordoado) — consome o turno inteiro |

O custo em Mana sobe junto com a Intensidade (ver [Escala de Mana por Intensidade](../jogador/mana.md#escala-de-mana-por-intensidade)).

**Alcance e área nunca escalam com Intensidade.** Uma habilidade que cobre 2 casas de raio cobre 2 casas de raio em qualquer Intensidade — o que a Intensidade compra é o efeito, não o tamanho.

### Habilidades de Custo Fixo

Algumas habilidades não têm Intensidade: trazem **Custo fixo** e um único resultado de **Acerto** na ficha. São os casos em que a força da habilidade já está em outro lugar:

- **Área de 3 casas de raio ou mais** — a área já é o poder; escalar o efeito por cima seria demais
- **Habilidades Supremas** — o custo em Mana (16+) já as coloca fora da escala
- **Buffs e efeitos sem rolagem** — não há teste de ataque pra graduar

### Habilidades com Tiers de Resultado

Um punhado de habilidades faz algo que **não deveria ser garantido só por pagar o custo** — trazer um aliado morto de volta é o caso central. Nessas, o d20 volta a graduar o resultado: a rolagem decide entre falha catastrófica, falha recuperável e sucesso.

| Total (d20 + Atributo) | Resultado |
|---|---|
| ≤ 10 | Falha total — a pior consequência possível |
| 11–16 | Falha, mas recuperável |
| ≥ 17 | Sucesso |
| 20 natural | Sucesso ampliado |

Essas habilidades têm **Custo fixo** (não têm Intensidade) e escrevem as faixas explicitamente na ficha. São deliberadamente raras — a graduação existe justamente pra impedir que um efeito dessa magnitude se torne confiável. Hoje só [Ressuscitar](suporte.md) usa esse formato.

### Resolução

1. O jogador declara a habilidade e **a Intensidade**, e paga o PA + Mana daquela Intensidade.
2. Rola **d20 + Atributo da habilidade**.
3. O total precisa **igualar ou superar a Defesa do alvo** (ver [Defesa](../jogador/sistema-d20.md#defesa)). Por padrão isso é a Defesa física (Agilidade) — habilidades que impõem outra coisa (efeito mental, veneno etc.) declaram qual atributo testar em vez disso, mas a lógica de comparação é sempre a mesma.
4. **Acertou** → aplica o efeito da Intensidade paga. **Não acertou** → nenhum efeito; o PA e o Mana foram gastos de todo jeito.
5. **1 natural** sempre falha, independente do total.
6. **20 natural** é **Crítico**: sempre acerta, soma o dano máximo do dado + mais uma rolagem normal do mesmo dado, e **sobe 1 Intensidade de graça** — aplica o efeito da Intensidade acima da que foi paga, sem pagar a diferença. Usado já em Intensidade III (ou numa habilidade de Custo fixo), o Crítico entrega apenas o bônus de dano.

O d20 responde só "acertou ou não" — **quão forte** o golpe é já foi decidido no momento em que o jogador escolheu a Intensidade.

Habilidades sem teste de ataque (buffs puros, efeitos automáticos como uma Habilidade Suprema inevitável) não checam Defesa nem têm Intensidade — o efeito simplesmente acontece, sem rolagem.
