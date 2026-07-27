# Pontos de Ação (◈)

Mantidos do sistema Diablo RPG anterior.

Cada personagem tem **3 Pontos de Ação (◈◈◈)** por turno.

| Ação | Custo |
|---|---|
| Movimento | ◈ (1) |
| Ação Básica | ◈ (1) |
| Ataque Básico | ◈ (1) |
| Reação | o custo normal da habilidade usada (0 se for dedicada) — consome do mesmo pool |

**Ataque Básico** funciona com qualquer arma equipada, mesmo uma cujas Habilidades o personagem nunca aprendeu — causa o dado de dano da arma, sem nenhum efeito extra. É o que permite "ter uma arma na mão" desde o nível 1 sem precisar gastar uma Habilidade nela (ver [Criação de Personagem](sistema-d20.md#criacao-de-personagem)).

**Qualquer Habilidade pode ser usada como Reação**, fora do seu turno, desde que o personagem ainda tenha PA sobrando no pool (do turno anterior) pra pagar o custo normal dela. O sistema é deliberadamente livre nesse ponto — se o jogador guardou PA, pode reagir com o que quiser, não só com uma lista fixa de "habilidades de reação".

**Habilidades dedicadas a Reação** (o texto diz explicitamente "usada como Reação", ex: Defesa Mágica, Cambalhota) são a exceção: custam **0 PA — só Mana**. Ficam sempre disponíveis como rede de segurança, mesmo se o personagem já gastou todo o PA no próprio turno.

## Movimento

Movimento base = **3 casas + Agilidade** (valor com sinal).
Mínimo de movimento: **1 casa**.

"Casas" é uma unidade abstrata — o mapa pode usar quadrados ou hexágonos.

O jogo **não tem regra de orientação** (facing): quando uma habilidade fala em "à frente" ou "pra trás", leia como **na direção do alvo** e **na direção oposta ao alvo** (ou ao atacante, no caso de uma Reação).

### Voo

Quem pode voar (traço racial ou habilidade) se move em três dimensões pelo **mesmo custo de Movimento** — cada casa de altura conta como uma casa andada.

- **Alcance:** corpo a corpo só alcança quem voa a 1 casa de altura; acima disso, só ataques à distância (e o voador enxerga por cima de obstáculos baixos).
- **Queda:** quem fica [Atordoado](../glossario.md#atordoado) ou é derrubado no ar **despenca**: sofre 1d6 de dano de Impacto a cada 2 casas de altura e aterrissa [Derrubado](../glossario.md#derrubado).
- [Imóvel](../glossario.md#imovel) no ar: para de se deslocar, mas plana no lugar — não cai.

## Custo em PA de Habilidades

O custo em PA de uma Habilidade **é a Intensidade escolhida** — não um valor fixo por habilidade. Isso vale igualmente para habilidades de arma e habilidades gerais de grupo:

| PA | Intensidade | O que ela entrega |
|---|---|---|
| ◈ (1) | I | O efeito base — normalmente só o dano |
| ◈◈ (2) | II | Acrescenta o efeito secundário (empurrar, Sangrando, Marcado) |
| ◈◈◈ (3) | III | O efeito completo (derrubar, Atordoado) |

Como o pool é de 3 PA por turno, isso vira uma decisão a cada turno: **uma habilidade em Intensidade III consome o turno inteiro** (sem movimento, sem reação guardada), enquanto três usos em Intensidade I fazem muito mais coisa por muito menos efeito cada. Ver [Intensidade](../habilidades/index.md#intensidade).

Vale igualmente para buffs, cura e mobilidade: não há teste de ataque neles, mas há Intensidade — o que cresce é o tamanho do efeito, não a chance de acertar (ver [Buffs, Suporte e Mobilidade](../habilidades/index.md#buffs-suporte-e-mobilidade-tambem-tem-intensidade)).

!!! regra "Exceções — habilidades de Custo fixo"
    Áreas de 3 casas de raio ou mais, Supremas, e efeitos absolutos que não têm degrau acima (uma Reação que anula um ataque por completo) cobram um valor fixo de PA e entregam um único resultado.

**Reações dedicadas** são um caso próprio: custam **0 PA** em qualquer Intensidade — é o que garante uma defesa reativa mesmo depois de gastar o turno inteiro atacando. Nelas, a Intensidade escolhe só quanto Mana gastar.
