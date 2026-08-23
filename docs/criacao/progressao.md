# Progressão de Nível

**Você sobe de nível a cada sessão jogada.** Não há experiência pra somar: jogou, subiu — ver [Progressão: um nível por sessão](../mestre/recompensas.md#progressao-um-nivel-por-sessao) pro lado do Mestre.

O jogo tem **100 níveis**. Dois ganhos correm em paralelo, em ritmos diferentes de propósito:

- **Atributo** — a cada **nível par**, +5 pontos pra distribuir entre os 8 atributos. Constante do nível 2 ao 100 (ver [Atributos](../jogar/atributos.md#a-faixa-de-valores)).
- **Habilidade** — rápido no início, raro depois. A criação já concede a 1ª (ver [Passo 4](index.md#4-primeira-habilidade)); a partir do nível 1, **mais uma a cada nível ímpar até o 39** (19 delas — fecha 20 no total por volta da metade da carreira); depois, só **a cada 10 níveis** (50, 60, 70, 80, 90, 100 — mais 6). **26 Habilidades ao todo.**

| Fase | Níveis | Habilidade | Atributo |
|---|---|---|---|
| Criação | 0 | 1ª (Passo 4) | base 5 + 15 livres |
| Rápida | 1–39 (ímpares) | +1 a cada nível ímpar (19 no total) | — |
| — | 2–40 (pares) | — | +5 a cada nível par |
| Lenta | 50, 60, 70, 80, 90, 100 | +1 em cada marco (6 no total) | — |
| — | 42–100 (pares) | — | +5 a cada nível par |

**Por que esse ritmo:** a mesma lógica que já vale pros atributos — a maioria das campanhas reais não passa de umas 10 sessões, então a progressão rápida (uma Habilidade quase todo nível, nos primeiros 40) é onde a maior parte das mesas realmente vive. Depois do meio de carreira, o personagem já tem um kit amplo — o que os níveis restantes entregam é principalmente **poder** (Atributo, e por consequência Vida/Mana/Estresse/Evasão), não mais botões novos na ficha. 26 habilidades, não 50: escolha continua pesando, em vez de acumular até virar ruído.

## Escolhendo a habilidade do nível

Todas as habilidades do jogo estão abertas a qualquer personagem, em qualquer nível — não há pré-requisito de nível, atributo, raça ou classe (ver [Requisito suave de Atributo](../jogar/mana.md#requisito-suave-de-atributo) pra quando vale a pena esperar). As duas únicas travas do sistema:

- **Ordem dentro de uma arma:** Básica → Avançada → Especial, e sempre da **mesma** arma.
- **26 escolhas na carreira inteira.** É essa escassez que faz a build.

Use os filtros da [Listagem de Habilidades](../habilidades/index.md) pra ver só o que faz sentido pro seu personagem — por grupo, elemento, arma, atributo, alvo ou Mana disponível.

!!! exemplo "Especializar ou espalhar"
    Investir três escolhas numa única arma (Básica, Avançada, Especial) fecha o kit dela cedo, com uma Intensidade III que resolve encontros sozinha — e sobra a maior parte das 26 pra reforçar em outra direção. Espalhar as escolhas entre grupos diferentes dá um personagem que tem resposta pra tudo e teto pra nada. Nenhuma das duas é errada; o sistema só cobra que você escolha.

## O que cresce sozinho

Vida, Mana e Estresse crescem automaticamente todo nível, sem gastar nenhuma das escolhas acima — são fórmula, não escolha:

- **[Vida Máxima](../jogar/dano-e-cura.md#vida)** — 20 + Nível + (Defesa × 2) + Vida de equipamento, recalculado a cada nível.
- **[Mana Máximo](../jogar/mana.md#mana-maximo)** — 20 + Nível + (Magia × 2) + Mana de equipamento, recalculado a cada nível.
- **[Estresse Máximo](../jogar/estresse.md)** — 20 + Nível + (Sanidade × 2) + equipamento, recalculado a cada nível.

## Subir de atributo

O ponto de atributo do nível par pode ir pra qualquer um dos oito, sem teto por nível (até o teto geral de 100). Vale lembrar o que muda de imediato:

| Se você subir | Muda na hora |
|---|---|
| Ataque | o dano dos seus ataques físicos |
| Defesa | [Vida Máxima](../jogar/dano-e-cura.md#vida) e Fortitude Física |
| Magia | [Mana Máximo](../jogar/mana.md#mana-maximo), Fortitude Mágica e dano mágico |
| Agilidade | [Evasão](../jogar/combate.md#defesa), [Movimento](../jogar/combate.md#movimento) e [Iniciativa](../jogar/combate.md#iniciativa) |
| Sorte | [Iniciativa](../jogar/combate.md#iniciativa), o limiar de [Crítico](../jogar/testes.md#criticos) e o número de [rerolagens](../jogar/testes.md#rerolagens) por descanso longo |
| Sanidade | [Estresse Máximo](../jogar/estresse.md) |
| Social | testes de persuadir, intimidar, enganar (e resistir a tudo isso) |
| Exploração | testes de perceber, rastrear, se orientar, sobreviver |
