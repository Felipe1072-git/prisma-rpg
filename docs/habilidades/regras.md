# Regras de Habilidade

Como toda habilidade é escrita e resolvida por baixo do capô — grupos, Intensidade, custo, Dano Desarmado e a assinatura mecânica de cada elemento. Pra navegar e filtrar as habilidades em si, veja a [Listagem de Habilidades](index.md).

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

!!! regra "Alcance e área nunca escalam com Intensidade"
    Uma habilidade que cobre 2 casas de raio cobre 2 casas de raio em qualquer Intensidade — o que a Intensidade compra é o efeito, não o tamanho.

### Habilidades de Custo Fixo

Algumas habilidades não têm Intensidade: trazem **Custo fixo** e um único resultado de **Acerto** na ficha. São os casos em que a força da habilidade já está em outro lugar:

- **Área de 3 casas de raio ou mais** — a área já é o poder; escalar o efeito por cima seria demais
- **Habilidades Supremas** — o custo em Mana (16+) já as coloca fora da escala
- **Efeitos sem nada pra graduar** — quando o efeito é absoluto, não há degrau acima dele. Uma Reação que **anula por completo** um ataque é o caso típico: não existe "anular mais"

O preço de uma habilidade de Custo fixo segue duas regras:

- **Mana:** o valor da Intensidade III da escala em que ela viveria (6-12 pra habilidades comuns; 16+ pra Supremas).
- **PA:** **◈◈◈**, como uma Intensidade III — com duas exceções: **Avançadas de arma** de área cobram **◈◈** (padrão consolidado do Arsenal: ◈◈ + 9 Mana), e **Reações dedicadas** cobram 0. Habilidades utilitárias fora de combate podem declarar PA menor na própria ficha.

!!! regra "Custo fixo não dispensa a rolagem"
    Habilidade de Custo fixo com alvo hostil **rola teste de ataque normalmente** contra a Defesa do alvo. Só ficam sem rolagem os casos que a [Resolução](#resolucao) isenta: buffs, cura, e Supremas declaradas como inevitáveis.

### Buffs, Suporte e Mobilidade também têm Intensidade

Não ter teste de ataque **não** significa não ter Intensidade. O que escala num buff não é a chance de acertar — é o tamanho do efeito. Cada habilidade escala pelo eixo que faz sentido pra ela:

| Eixo | Quando se aplica | Exemplo |
|---|---|---|
| **Magnitude** | Há um valor que é a identidade do buff | Escudo Mágico: Escudo de 1d8 → 2d8 → 3d8 |
| **Duração** | O efeito é absoluto e não tem número pra crescer | Postura Inabalável: não pode ser derrubado por 2 → 3 → 4 rodadas |
| **Ambos** | Buff de grupo ou transformação, que tem valor *e* prazo | Bênção Divina: +1 → +2 → +3 de bônus, por 3 → 4 → 5 rodadas |

!!! regra "Habilidades dedicadas a Reação são a exceção parcial"
    Continuam custando **0 PA** sempre — essa é a rede de segurança que permite reagir mesmo tendo gastado o turno inteiro. Nelas a Intensidade escolhe apenas **quanto Mana** queimar no momento em que você é atacado.

Como o buff mantém na Intensidade I exatamente o efeito e o custo em Mana que sempre teve, subir de Intensidade é sempre ganho — nunca um pedágio pra ter o de antes.

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
6. **20 natural** é **Crítico**: sempre acerta, soma o dano máximo do dado + mais uma rolagem normal do mesmo dado, e **sobe 1 Intensidade de graça** — aplica o efeito da Intensidade acima da que foi paga, sem pagar a diferença. Usado já em Intensidade III (ou numa habilidade de Custo fixo), o Crítico entrega o bônus de dano — mais o efeito extra de Crítico que a própria ficha declarar, se houver.

!!! regra "Vários alvos, uma rolagem"
    Habilidade que atinge mais de uma criatura rola **um único d20**, comparado à Defesa de **cada** alvo individualmente — pode acertar uns e errar outros. Um 20 natural é Crítico contra todos os que acertou; um 1 natural erra todos.

!!! regra "Deslocamento do usuário vale em toda Intensidade"
    Quando uma habilidade desloca o usuário (salto, investida, recuo), essa cláusula vale em **todas** as Intensidades, mesmo que o texto das linhas II/III não a repita — o deslocamento é a identidade da técnica, não um efeito comprado.

O d20 responde só "acertou ou não" — **quão forte** o golpe é já foi decidido no momento em que o jogador escolheu a Intensidade.

Habilidades sem teste de ataque (buffs, cura, efeitos automáticos como uma Habilidade Suprema inevitável) **não checam Defesa** — o efeito simplesmente acontece. Mas isso não as isenta de Intensidade: elas ainda escolhem quanto investir, e o que cresce é o tamanho do efeito (ver acima).
