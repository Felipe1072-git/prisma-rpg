# Dano e Cura

| Resumo rápido | |
|---|---|
| Vida Máxima | **20 + Nível + (Defesa × 2)** + Vida de equipamento |
| Recuperação | metade no descanso curto, tudo no longo |
| Tipos de dano físico | Cortante, Perfurante, Impacto (da arma), Arcano (foco mágico) |
| Resistência / Imunidade / Vulnerabilidade | dano cai pela metade / é ignorado / dobra |
| Chegando a 0 de Vida | fica **Caído** — d100 vs Dificuldade 50 no início do turno seguinte |

Quanto você aguenta, o que te machuca mais, como você se recupera — e o que acontece quando a Vida chega a zero.

## Vida

**Vida Máxima = 20 (base) + Nível + (Defesa × 2) + Vida de equipamento**

Exemplo: nível 0, Defesa 5 (baseline de criação) → 20 + 0 + 10 = 30. Nível 100, Defesa 85 (foco pesado) → 20 + 100 + 170 = 290.

O termo de equipamento é 0 pra quase tudo — hoje só as [Armaduras](../equipamento/regras.md#armaduras) somam algo, de +10 (leve) a +75 (Placa de Torneio). É a mesma forma do [Mana Máximo](mana.md#mana-maximo) (só trocando Magia por Defesa e Mana de equipamento por Vida de equipamento) — de propósito: armadura ajuda a **aguentar mais pancada**, não a desviar dela, então soma aqui e não na Evasão (quem cuida da Evasão agora é o [Escudo](../equipamento/regras.md#escudos)).

Vida é recalculada a cada vez que Defesa muda (subir de nível, um buff, um debuff) — não é cumulativa como no sistema antigo, é sempre "o número de agora".

## Recuperação

- **Descanso curto** (~1h): recupera **metade** da Vida máxima
- **Descanso longo** (noite): recupera **toda** a Vida

Mesma lógica do [Mana](mana.md#recuperacao) — sem dados de vida pra gastar ou controlar, só a fração recuperada por tipo de descanso.

## Cura por Habilidade

Cura por Habilidade (ver [Suporte](../habilidades/suporte.md)) funciona a qualquer momento, não só em descanso — é justamente por isso que ter um curandeiro no grupo importa: ele estica o dia sem precisar parar.

Como toda habilidade, cura tem [Intensidade](../habilidades/regras.md#intensidade): não há teste de acerto, mas o tamanho do efeito escala com o quanto você paga.

## Tipos de Dano

Todo dano tem um tipo, e é por isso que a arma escolhida importa contra certas criaturas. Os três primeiros são físicos, e vêm da arma empunhada (ver a coluna **Tipo** na [Tabela de Dados de Dano](../equipamento/regras.md#tabela-de-dados-de-dano)):

| Tipo | De onde vem | Contra o que costuma ser bom |
|---|---|---|
| **[Cortante](../glossario.md#cortante)** | espadas, machados, foices, garras | carne e criaturas de tecido mole |
| **[Perfurante](../glossario.md#perfurante)** | lanças, adagas, flechas, projéteis | brechas de armadura, alvos volumosos |
| **[Impacto](../glossario.md#impacto)** | martelos, bastões, punhos, manguais | ossos, cascas, armaduras rígidas, esqueletos |
| **[Arcano](../glossario.md#arcano)** | focos mágicos, canalizações sem forma definida | quem depende de resistência física |

Habilidades de **[Mágicas por Elemento](../habilidades/magicas-elementais.md)** causam dano do próprio elemento (fogo, gelo, sombras...), não desses quatro — é o elemento que o alvo resiste ou não.

**Dano Desarmado** é sempre Impacto, salvo quando um traço racial disser outra coisa (garras naturais cortam).

## Dado de Dano

O dano de uma habilidade de arma é o **dado da própria arma**, que escala com a Intensidade: a Intensidade I usa o dado da [Tabela de Dados de Dano](../equipamento/regras.md#tabela-de-dados-de-dano) sem alteração (de 1d4 a 1d12, dependendo do peso da arma); a Intensidade II sobe um degrau (d4→d6, d6→d8, d8→d10, d10→d12, d12→d20); a Intensidade III dobra o dado já escalado da II. Habilidades gerais têm o próprio dado, escrito na ficha.

Pra estimar dano de qualquer combinação de dados, ou improvisar um número na mesa, ver a [Tabela de referência de dano médio](../mestre/testes.md#calibracao-de-dano) e a [Tabela de Dano Improvisado](estresse.md#tabelas-de-referencia-rapida).

## Resistência, Imunidade e Vulnerabilidade

Aplicadas a um tipo de dano — físico ou elemental — sempre **depois** de qualquer outro cálculo, incluindo Crítico:

| | Efeito |
|---|---|
| **[Resistência](../glossario.md#resistencia)** | o dano daquele tipo cai pela **metade** (arredondado pra baixo) |
| **[Imunidade](../glossario.md#imunidade)** | o dano daquele tipo é **ignorado** por completo (0) |
| **[Vulnerabilidade](../glossario.md#vulnerabilidade)** | o dano daquele tipo é **dobrado** |

Uma criatura nunca tem Resistência e Vulnerabilidade ao mesmo tipo; se algum efeito criar essa situação, as duas se cancelam e o dano é normal. Duas Resistências ao mesmo tipo também não somam — ver [Acúmulo de bônus](../glossario.md#acumulo-de-bonus).

Vulnerabilidade é a ferramenta que transforma conhecimento em vantagem: descobrir que o morto-vivo cai mais rápido sob Luz, ou que a criatura de gelo derrete no Fogo, vale mais que um bônus numérico — e é o que faz um grupo trocar de arma antes de entrar na masmorra.

## Chegando a 0 de Vida

Zero não é morte. O personagem fica **Caído**: inconsciente, sem agir, sem rolar nada — e com **uma única chance** de não morrer.

**No início do próximo turno dele, role d100 contra Dificuldade 50.** A Dificuldade não soma nenhum Atributo — o dado mede só a sorte do momento, igual pra todos. **Sucesso: fica Estável. Falha: morre.**

Diferente do sistema antigo, não existe mais uma sequência de falhas até morrer — com a Vida na escala atual, um personagem aguenta muitos golpes antes de cair; quando cai, o risco precisa ser real na hora.

**Como sair de Caído antes da rolagem:**

- **Estabilizar** — um aliado adjacente gasta uma **Ação Básica (◈)** e faz um **teste de Exploração contra Dificuldade 50**. Sucesso: o personagem fica **Estável** direto, sem precisar rolar contra a morte — acorda ao fim da cena com 1 de Vida. Falha: a tentativa não funcionou, mas não piora nada; pode tentar de novo se ainda houver tempo. (As origens *Curandeiro de Vila* e *Salvou uma Vida* fazem isso como Reação e sem custo — ver [Origem](../origens/index.md).)
- **Cura** — qualquer efeito que devolva Vida traz o personagem de volta com aquela Vida, e ele age normalmente no próximo turno.

Isso vale só pros personagens jogadores: uma **criatura a 0 de Vida morre** (ver [Bestiário](../mestre/criando-criaturas.md#criatura-a-0-de-vida-morre)).

## O Último Turno

Um personagem Caído pode escolher **não resistir**. Em vez de rolar contra a morte, ele decide que aquele é o fim — e se levanta pra gastar tudo o que resta.

Declarado no início de um turno dele enquanto estiver Caído, o Último Turno funciona assim:

- Ele **se levanta e joga um turno completo**: 3 PA, Mana, habilidades, tudo. Ainda rola pra acertar normalmente.
- **Todo sucesso é tratado como Crítico** — dano máximo, rolagem extra e [sobe 1 Intensidade de graça](../habilidades/regras.md#resolucao), mesmo sem cair dentro do limiar de Sorte.
- **Falha aqui não tem meio-termo** — não há acerto raspado; o que dá errado, dá errado por completo.
- **Nenhuma cura funciona nele** durante o Último Turno. Não há como voltar atrás depois de declarar.
- **Ao fim do turno, o personagem morre.** Sem rolagem, sem resistência, sem chance. Foi o preço.

É a única escolha do sistema em que o jogador **troca a chance de sobreviver por certeza de impacto**. Um personagem que ia morrer de qualquer jeito, sem agir, pode em vez disso derrubar o chefe com um golpe garantido como crítico — e sair de cena tendo decidido como.

!!! mestre "Cabe ao Mestre dar espaço pra isso"
    Se um jogador declara o Último Turno, a mesa para e escuta: é o momento daquele personagem, e ele não vai ter outro.
