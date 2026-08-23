# Estresse

A [Vida](dano-e-cura.md#vida) mede o que o corpo aguenta. O Estresse mede o que a **cabeça** aguenta — e é a única barra do jogo que o descanso curto não repõe.

**Estresse Máximo = 20 (base) + Nível + (Sanidade × 2) + Estresse de equipamento**

Exemplo: nível 0, Sanidade 5 (baseline de criação) → 20 + 0 + 10 = 30. Nível 100, Sanidade 58 (investimento moderado) → 20 + 100 + 116 = 236. Mesma forma de [Vida](dano-e-cura.md#vida) e [Mana](mana.md#mana-maximo), só trocando o atributo — de propósito: os três recursos crescem do mesmo jeito, então decorar a fórmula de um é decorar a dos três. O termo de equipamento é 0 pra tudo hoje — fica pronto pro dia que algum item conceder Estresse Máximo extra.

## Como se ganha Estresse

Duas famílias de gatilho — uma automática e de graça, outra narrativa e pontual:

**Automáticos, sem rolagem extra (1d6 cada):**

- **Tirar exatamente 1 no d100**, em qualquer teste — mesmo quando o resultado é sucesso ou crítico (todo personagem tem um limiar de [Crítico](testes.md#criticos) de pelo menos 1, então tirar 1 nunca é "ruim" no resultado, mas ainda representa o preço mental de escapar por pouco).
- **Sofrer um crítico.**

**Narrativos — uma checklist fixa, não julgamento aberto do Mestre.** Quando um destes acontece, o jogador rola **d100 + Sanidade contra a Dificuldade que o Mestre escolher** (ver [Tabela de Dificuldades](../mestre/testes.md#a-tabela)); falhando, marca **4d6** de Estresse, em qualquer nível:

1. Presenciar horror
2. O próprio personagem cair a 0 de Vida
3. Ver um aliado cair a 0 de Vida
4. Falhar em algo que importava de verdade
5. Matar ou ferir gravemente alguém que não devia

Estresse recupera na mesma escala de [Vida](dano-e-cura.md#vida) e [Mana](mana.md#mana-maximo): **metade do máximo num descanso curto, tudo num descanso longo** (ver [Descanso](exploracao.md#descanso)).

## Colapso

Ao encher a barra de Estresse, o personagem sofre um surto imediato — o Mestre escolhe ou rola 1d6 na tabela abaixo. Cada surto define seu próprio efeito e duração.

| d6 | Surto |
|---|---|
| 1 | **Fuga** — foge da cena pelo caminho mais direto e seguro, ignorando perigo no caminho. Dura até sair de vista e alcance de todos os presentes; a partir daí, fica **Indisponível pelo resto da cena** (não volta a tempo de ajudar) |
| 2 | **Pânico** — trava completamente por **1 rodada completa**, gritando ou paralisado, sem realizar nenhuma ação. Ao fim da rodada volta a agir normalmente |
| 3 | **Fúria Cega** — ataca a criatura mais próxima (aliada ou inimiga, sem escolha do jogador) com o que tiver em mãos, uma única vez. Depois desse ataque o surto termina e ele volta a agir normalmente no turno seguinte |
| 4 | **Colapso Físico** — desmaia imediatamente, caindo no chão e ficando Indisponível. Volta a si sozinho após **1d4 rodadas**, ou imediatamente se um aliado gastar uma ação adjacente pra acordá-lo |
| 5 | **Dissociação** — grita ou chora sem controle e larga tudo que estava segurando. Dura até o fim do turno atual; no turno seguinte já pode agir normalmente, mas precisa gastar uma ação pra reequipar o que soltou |
| 6 | **Bloqueio** — para completamente, repetindo a mesma frase ou ação sem sentido, alheio ao redor. Dura até um aliado gastar uma ação adjacente pra trazê-lo de volta, ou até o fim da cena — o que vier primeiro |

## Cicatrizes

Depois do surto, a barra reseta a 0 e o personagem ganha uma **Cicatriz**: uma condição negativa permanente, escolhida ou sorteada (d6) na tabela abaixo.

| d6 | Cicatriz |
|---|---|
| 1 | **Fobia Específica** — escolha um gatilho (fogo, sangue, altura, escuridão, multidão etc.); na presença dele, todos os testes sofrem [Desvantagem](../glossario.md#desvantagem) até se afastar |
| 2 | **Gatilho de Fúria** — um evento específico (ver aliado cair, ser insultado etc.) força um teste de Estresse extra imediato |
| 3 | **Tique Nervoso** — Desvantagem no primeiro teste social de cada cena |
| 4 | **Isolamento** — recupera só metade do Estresse por Apoio Social (arredondado pra baixo) |
| 5 | **Paranoia** — Desvantagem em [Iniciativa](combate.md#iniciativa) (sempre hesitante, desconfiado demais) |
| 6 | **Exaustão Crônica** — descanso curto não recupera [Mana](mana.md) |

## Tabelas de referência rápida

Duas tabelas pro Mestre improvisar dano/Estresse na mesa sem calcular nada — um dado só, a quantidade que escala com a severidade (mesmo espírito do "Improvising Damage" do D&D 5e).

**Dano Improvisado** (d10):

| Dados | Exemplos |
|---|---|
| 1d10 | tropeço feio, mordida pequena, corte raso |
| 2d10 | golpe direto, queda de pouca altura, queimadura de tocha |
| 4d10 | ferimento sério, atropelamento, fogo direto no corpo |
| 8d10 | esmagamento, explosão próxima, queda de penhasco |
| 14d10 | desabamento, jogado numa fornalha, atingido por algo colossal |
| 20d10 | cair em lava, pisoteado por um titã, o fim de tudo |

Pra escolher a linha certa por nível, cruza com a [tabela de calibração de dano](../mestre/testes.md#calibracao-de-dano) — Vida ÷ 10 é o "golpe normal" (2d10 a 8d10 cobrem a faixa 0-100 de nível); 14d10 e 20d10 ficam pra ameaças fora da curva, tipo Lendários.

**Estresse Improvisado** (d6 — pra eventos narrativos fora da checklist fixa acima; o Mestre escolhe a linha pela gravidade da cena, não pelo nível):

| Dados | Exemplos |
|---|---|
| 1d6 | um susto rápido, uma ameaça velada |
| 2d6 | testemunhar violência, ser humilhado publicamente |
| 3d6 | ver um cadáver mutilado, trair a própria palavra |
| 4d6 | perder alguém querido, ser torturado |
| 5d6 | genocídio presenciado, o próprio corpo profanado |
