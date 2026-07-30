# Glossário de Termos

Os **121 termos** que o jogo usa: condições, tipos de dano, termos de resolução, armas, grupos e elementos. Cada um linka pra sua página de origem, e cada menção a um termo no resto do site abre o verbete num popover ao passar o mouse.

Há duas formas de chegar num termo: o **índice alfabético** abaixo, se você já sabe o nome, ou a **busca e o filtro por categoria**, se você está procurando o que existe.

## Termos de Resolução

### Vantagem

Role **2d20 e use o melhor**. Fontes múltiplas de Vantagem não acumulam — rola-se 2d20 uma vez só.

### Desvantagem

Role **2d20 e use o pior**. Também não acumula. Se uma mesma rolagem tiver Vantagem e Desvantagem ao mesmo tempo (de qualquer quantidade de fontes), **elas se cancelam** e rola-se 1d20 normal.

### Turno

A vez de **um** participante agir: seus 3 ◈, suas Reações pendentes, seus efeitos "no início/fim do turno".

### Rodada

Um ciclo completo da ordem de iniciativa — termina quando **todos** os participantes jogaram seu turno. Um efeito de "X rodadas" expira **no início do turno de quem o criou**, X rodadas depois da ativação.

### Cena

Uma unidade contínua de ação num mesmo lugar e tempo — uma luta, uma negociação, uma travessia. **Um combate é sempre uma cena própria**: efeitos e usos "por cena" resetam quando ele termina.

### Empurrar e Puxar

Deslocamentos forçados não são movimento do alvo (funcionam contra [Imóvel](#imovel)). O deslocamento **para ao encontrar um obstáculo** — parede, criatura, borda — e as casas não percorridas são perdidas, sem dano de colisão. Ser empurrado ou puxado pra dentro de uma zona de dano conta como **entrar** nela.

### Perde a próxima Reação

A próxima Reação que o alvo tentaria usar é negada — **inclusive Reações dedicadas** (0 PA). Vale até o fim da **próxima rodada**; se ele não tentar reagir nesse prazo, o efeito expira sem uso.

### Acúmulo de bônus

**Bônus numéricos planos de buffs diferentes não somam — vale o maior.** Um personagem sob Aura de Ataque (+3) e Bênção Divina (+2) usa +3, não +5 (uma habilidade que declara empilhar **consigo mesma**, como a Bênção Divina, é exceção explícita e só empilha com ela própria). Bônus de fontes de natureza diferente (buff + item + traço racial) somam normalmente. **Resistências ao mesmo tipo de dano também não acumulam** — duas Resistências a Fogo valem uma.

## Condições

Efeitos que uma habilidade impõe ao alvo. Salvo quando a habilidade disser outra coisa, duram **até o fim do próximo turno do alvo**.

### Sangrando

Perde **1d4 de Vida** no início do próximo turno dele. Efeito de uma vez só — ferida que fecha.

- **Não acumula.** Reaplicado antes de disparar, vale só o **dado maior** (um "Sangrando 2d4" substitui o 1d4 — mesma lógica de Queimando). Depois de disparar, o alvo pode voltar a Sangrar normalmente.

### Queimando

Perde **1d4 de Vida imediatamente ao pegar fogo**, e mais **1d4 no início de cada turno dele**. Assinatura do elemento [Fogo](habilidades/magicas-elementais.md#fogo) — diferente de Sangrando justamente por não ter prazo.

- **Não acumula.** Pegar fogo de novo não soma um segundo dado: vale o valor maior entre os dois (mesma lógica do [Escudo](#escudo)). Uma habilidade que diz "Queimando causando 2d4 por turno" simplesmente substitui o 1d4 enquanto durar.
- **Não para sozinho durante o combate.** Termina de três formas: o alvo gasta uma **Ação Básica** pra se apagar, um aliado **adjacente** gasta a dele, ou o alvo entra em contato com água em quantidade (o Mestre decide o que conta). **Sofrer dano de Gelo ou Água também apaga o fogo.**
- **Espalhamento:** quando uma habilidade diz que o fogo "se espalha" pra uma criatura adjacente, **o usuário escolhe qual** (pode ser um aliado — fogo não distingue). Quem pegou fogo por espalhamento **não espalha de novo**: não há cadeia.
- **Apaga no fim do combate.** Encerrada a cena de combate, o fogo se apaga sozinho — ninguém sai queimando pela estrada.

### Lento

Movimento reduzido à **metade**. Afeta só o **Movimento** (a ação de ◈) — deslocamentos concedidos por habilidades (saltos, investidas, teleportes) não são reduzidos.

### Imóvel

**Movimento 0** — não sai do lugar **por vontade própria**, nem voando. Continua agindo normalmente: Ações Básicas, Habilidades e Reações seguem disponíveis. É o degrau acima de Lento, e não se confunde com [Atordoado](#atordoado), que trava tudo.

!!! regra "Força externa ainda move — e teleporte também"
    Empurrar, puxar e teleportar não são movimento do alvo — são coisas feitas *a* ele, e funcionam normalmente contra quem está Imóvel. Um alvo preso no lugar pode ser arrancado dele por um empurrão de Vento ou pela [Dobra Espacial](habilidades/magicas-elementais.md#espaco-tempo). O mesmo vale pro **teleporte próprio**: quem está Imóvel não anda nem salta, mas ainda pode se teleportar (Passo Sombrio, Fora de Lugar) — ele não se move, ele deixa de estar ali. Deslocamentos **físicos** de habilidade (saltos, investidas) continuam negados.

### Atordoado

**Não pode agir** — nem ação, nem movimento, nem reação.

### Derrubado

Está **no chão**. Enquanto Derrubado, seu Movimento é 0, e ataques **corpo a corpo** contra ele rolam com [Vantagem](#vantagem). **Levantar custa ◈ (1)** no próprio turno e encerra a condição. Não se confunde com **Caído** ([a 0 de Vida](jogar/dano-e-cura.md#chegando-a-0-de-vida)) — Derrubado é chão, Caído é morte chegando.

### Desprevenido

Foi pego de surpresa: **não pode agir nem reagir durante a primeira rodada do combate**. É o que acontece com um grupo emboscado sem vigia (ver [Exploração](mestre/exploracao.md#detectar-e-desarmar)). "Surpreendido" é a mesma condição.

### Agarrado

Está preso por uma criatura ou restrição física: fica [Imóvel](#imovel) enquanto durar. **Escapar custa ◈ (1)** e um teste de **Força ou Agilidade** (o que for maior) contra a Defesa física de quem prende — ou contra a DC da restrição, se for um objeto. Quem prende solta automaticamente se ficar Atordoado ou Caído.

### Marcado

O **próximo ataque de um aliado** contra ele **nesta rodada** rola com Vantagem.

### Envenenado

Perde **1d4 de Vida por acúmulo** no início de cada turno dele, até ser curado. Diferente do fogo, o veneno leva tempo pra agir: **não há dano no momento em que é aplicado** — a primeira perda de Vida acontece no início do próximo turno do alvo.

- **Acúmulos:** cada nova aplicação soma 1 acúmulo, e cada acúmulo vale 1d4 por turno (1 acúmulo = 1d4, 2 = 2d4, 3 = 3d4). O **máximo é 3 acúmulos** (3d4 por turno).
- **Cura limpa tudo.** Qualquer efeito que cure Vida ou remova condições apaga **todos** os acúmulos de uma vez — não é preciso curar três vezes.

### Escudo

Pontos temporários que **absorvem dano** antes da Vida. Não acumulam com outro Escudo — vale o maior. Substituir um Escudo por outro maior **não** remove os demais efeitos do buff original (retaliação, anti-derrubar etc.), que valem pela duração declarada dele.

!!! regra "Escudo (condição) ≠ Escudo (item)"
    O **item** Escudo ([Equipamento → Escudos](equipamento/index.md#equ-escudo)) dá bônus passivo de **Defesa**. A **condição** Escudo dá pontos que absorvem dano. Quando uma habilidade diz "ignora bônus de Escudo", refere-se ao **item**; quando diz "ganha um Escudo de Xd6", é a condição.

### Exausto

Desgaste do corpo, acumulado em **graus**. Diferente das outras condições, não vem de habilidade: vem de [privação e viagem](jogar/exploracao.md#exaustao) — fome, sede, frio, noite sem dormir, marcha forçada.

| Grau | Efeito (acumulativo) |
|---|---|
| **1** | Desvantagem em todos os testes |
| **2** | também fica [Lento](#lento) |
| **3** | cai inconsciente até receber ajuda ou descansar |

**Some 1 grau** a partir do **segundo dia** de privação (o primeiro só incomoda) e por noite sem descanso adequado depois de um dia de esforço — ver [Exaustão](jogar/exploracao.md#exaustao), que é a regra completa. **Remove 1 grau** por [descanso longo](jogar/exploracao.md#descanso) — desde que a causa tenha sido resolvida (comeu, bebeu, se aqueceu). Descansar com fome não remove nada.

### Risco

Algumas habilidades cobram um preço de quem as usa: se **algum dos dados de dano cair em 1**, a habilidade escapa ao controle e o usuário sofre o efeito descrito na ficha dela. Reservado a habilidades de tema perigoso — lâminas amaldiçoadas, magia de sangue, poder emprestado.

## Efeitos de Terreno

Ao contrário das Condições, que ficam grudadas numa criatura, estes efeitos ficam grudados no **chão** — e valem para quem quer que passe por ali.

Duas regras valem pra **todo** efeito de terreno criado por habilidade, de qualquer elemento:

- **Não somam.** Onde duas zonas de dano se sobrepõem — sejam de Sombras, Fogo, Raio ou qualquer outro tema — vale só a **mais forte**, nunca a soma.
- **Cobertura e prazo padrão:** salvo texto contrário na ficha, o terreno criado cobre a **área da habilidade** e dura **até o fim do combate**.

### Terreno Difícil

Atravessar **custa o dobro de Movimento**: cada casa consome duas. Vale para escombros, lama, gelo, mato fechado, escada, e para o terreno que algumas habilidades criam.

Não é dano nem condição — é o chão cobrando pedágio. Num sistema onde deslocar-se custa ◈, dobrar esse custo é uma das formas mais baratas de mudar como uma luta se desenrola.

### Zona Amaldiçoada

Assinatura de [Sombras](habilidades/magicas-elementais.md#sombras) em área: a região atingida continua ferindo depois do golpe. Qualquer criatura que **entrar** na área, ou que **terminar o turno** dentro dela, sofre o dano indicado pela habilidade (tipicamente 1d4, ou 2d4 na Intensidade III).

- **A zona não repete o impacto.** Quem estava na área no momento do golpe já sofreu o dano da habilidade; a zona passa a valer **a partir daí**, atingindo quem entrar depois ou quem escolher ficar.
- **Fere todo mundo, sem distinção.** É terreno amaldiçoado, não uma armadilha inteligente: pega inimigos, aliados e o próprio usuário. Plantar uma zona no meio da batalha é uma decisão de posicionamento, não dano grátis.
- **É visível.** A mancha no chão é óbvia para qualquer um que olhe — ninguém entra sem saber. Um inimigo com um mínimo de instinto vai desviar, e é justamente assim que a zona controla o campo: negando espaço, mais do que causando dano.
- **Zonas sobrepostas não somam.** Onde duas zonas se cruzam, vale só a **mais forte** — nunca 1d4 + 1d4.
- **Duração:** a que a habilidade declarar (1, 2 ou 3 rodadas, conforme a Intensidade). Encerrado o prazo, a maldição se dissolve.

## Dano

Todo dano tem um tipo. Os três primeiros vêm da arma empunhada; o quarto, de focos mágicos. Ver [Tipos de Dano](jogar/dano-e-cura.md#tipos-de-dano).

### Cortante

Espadas, machados, foices, garras.

### Perfurante

Lanças, adagas, flechas, projéteis de arma de fogo.

### Impacto

Martelos, bastões, punhos, manguais. Também é o tipo do [Dano Desarmado](habilidades/marciais.md#dano-desarmado).

### Arcano

Focos mágicos — canalização sem forma física definida.

### Resistência

O dano daquele tipo cai pela **metade** (arredondado pra baixo).

### Imunidade

O dano daquele tipo é **ignorado** por completo.

### Vulnerabilidade

O dano daquele tipo é **dobrado** — espelho da Resistência. É o que recompensa descobrir a fraqueza de uma criatura e trocar de arma antes da luta.

## Graus de Habilidade de Arma

Toda arma concede 3 habilidades, aprendidas nessa ordem obrigatória (ver [Equipamento](equipamento/index.md)). O grau **não** define o custo — cada uma tem suas próprias [Intensidades](habilidades/regras.md#intensidade) I/II/III. O que o grau define é o quanto a técnica entrega e o quanto de Mana ela cobra:

### Básica

Primeira habilidade de qualquer arma. Parte do dado da arma + um efeito leve. Mana: 1 / 3 / 6.

### Avançada

Bate mais forte que a Básica (tipicamente o dado dobrado) e alcança condições que ela não impõe. Mana: 2 / 5 / 9.

### Especial

A habilidade mais poderosa da arma — dano alto, condição severa e frequentemente área. Mana: 3 / 7 / 12.

!!! regra "Em habilidades gerais de grupo, 'Especial' é só o subtipo"
    Uma Chave como "Marciais - Especial" marca o subtipo temático da habilidade geral — a escala de Mana continua sendo a do grupo (1/3/6 ou passos de +3), **não** a 3/7/12 das armas.

## Armas

### Espada

Arma marcial, dano 1d8. Ver [Equipamento → Espada](equipamento/index.md#equ-espada).

### Lança

Arma marcial de alcance, dano 1d10. Ver [Equipamento → Lança](equipamento/index.md#equ-lanca).

### Montante

Arma marcial pesada de duas mãos, dano 1d12. Ver [Equipamento → Montante](equipamento/index.md#equ-montante).

### Sabres

Par de lâminas leves, dano 1d6. Ver [Equipamento → Sabres](equipamento/index.md#equ-sabres).

### Arco

Arma de pontaria, dano 1d8. Ver [Equipamento → Arco](equipamento/index.md#equ-arco).

### Bestas

Par de bestas leves, dano 1d6. Ver [Equipamento → Bestas](equipamento/index.md#equ-bestas).

### Balista

Arma de pontaria pesada, dano 1d12. Ver [Equipamento → Balista](equipamento/index.md#equ-balista).

### Gakkung

Arco tradicional leve e ágil, dano 1d6. Ver [Equipamento → Gakkung](equipamento/index.md#equ-gakkung).

### Cetro

Arma mágica genérica, dano 1d8, sem elemento fixo. Ver [Equipamento → Cetro](equipamento/index.md#equ-cetro).

### Pote

Arma mágica genérica, dano 1d6, sem elemento fixo. Ver [Equipamento → Pote](equipamento/index.md#equ-pote).

### Lâmpada

Arma mágica genérica, dano 1d8, sem elemento fixo. Ver [Equipamento → Lâmpada](equipamento/index.md#equ-lampada).

### Cajado

Arma mágica genérica, dano 1d10, sem elemento fixo. Ver [Equipamento → Cajado](equipamento/index.md#equ-cajado).

### Adagas

Arma marcial Finesse, dano 1d4. Ver [Equipamento → Adagas](equipamento/index.md#equ-adagas).

### Alfange

Arma marcial Finesse, dano 1d8. Ver [Equipamento → Alfange](equipamento/index.md#equ-alfange).

### Garras

Arma marcial Finesse, dano 1d6. Ver [Equipamento → Garras](equipamento/index.md#equ-garras).

### Katana Nodachi

Arma marcial Finesse (duas mãos), dano 1d10 (lâmina longa clássica). Ver [Equipamento → Katana Nodachi](equipamento/index.md#equ-katana-nodachi).

### Machado

Arma marcial pesada, dano 1d12. Ver [Equipamento → Machado](equipamento/index.md#equ-machado).

### Gládio

Arma marcial Híbrida, dano 1d6. Ver [Equipamento → Gládio](equipamento/index.md#equ-gladio).

### Chakram

Arma de pontaria, dano 1d6. Ver [Equipamento → Chakram](equipamento/index.md#equ-chakram).

### Manopla

Arma marcial, dano 1d6. Ver [Equipamento → Manopla](equipamento/index.md#equ-manopla).

### Lâmina

Arma marcial, dano 1d8. Ver [Equipamento → Lâmina](equipamento/index.md#equ-lamina).

### Manual

Arma mágica genérica, dano 1d6, sem elemento fixo. Ver [Equipamento → Manual](equipamento/index.md#equ-manual).

### Foice

Arma marcial pesada, dano 1d10. Ver [Equipamento → Foice](equipamento/index.md#equ-foice).

### Espada Senciente

Arma marcial pesada, dano 1d12 (renomeada de "Espadão" — conceito da Grandark; absorve energias, mas dificulta a mobilidade de quem a empunha). Ver [Equipamento → Espada Senciente](equipamento/index.md#equ-espada-senciente).

### Orbe

Arma mágica genérica, dano 1d8, sem elemento fixo. Ver [Equipamento → Orbe](equipamento/index.md#equ-orbe).

### Manopla Mística

Arma mágica (Foco Mágico), dano 1d8, ataca com Inteligência (invoca criaturas através de uma gema com pentagramas e hexagramas). Ver [Equipamento → Manopla Mística](equipamento/index.md#equ-manopla-mistica).

### Pistolas

Dupla de pistolas leves, dano 1d6 — usadas sempre em par, uma em cada mão. Ver [Equipamento → Pistolas](equipamento/index.md#equ-pistolas).

### Punhal

Adaga Finesse, dano 1d6. Ver [Equipamento → Punhal](equipamento/index.md#equ-punhal).

### Espingarda

Conhecida como "A Ruptura", dano 1d10 — tiro único e devastador, arma dos Justiceiros (caçadores de recompensas de elite). Ver [Equipamento → Espingarda](equipamento/index.md#equ-espingarda).

### Metralhadora

Metralhadora giratória, dano 1d12. Ver [Equipamento → Metralhadora](equipamento/index.md#equ-metralhadora).

### Leque

Arma mágica genérica, dano 1d6, sem elemento fixo. Ver [Equipamento → Leque](equipamento/index.md#equ-leque).

### Vembrassa

Arma marcial, dano 1d6 (reflexo da Manopla — punho aberto, mão esquerda). Ver [Equipamento → Vembrassa](equipamento/index.md#equ-vembrassa).

### Martelo

Arma marcial pesada, dano 1d12. Ver [Equipamento → Martelo](equipamento/index.md#equ-martelo).

### Florete

Arma marcial Finesse, dano 1d6. Ver [Equipamento → Florete](equipamento/index.md#equ-florete).

### Flintlock

Pistola de precisão, dano 1d8. Ver [Equipamento → Flintlock](equipamento/index.md#equ-flintlock).

### Katana Muramasa

Arma marcial Finesse (duas mãos), dano 1d10 (lâmina amaldiçoada, exige sangue). Ver [Equipamento → Katana Muramasa](equipamento/index.md#equ-katana-muramasa).

### Cubo Mágico

Arma mágica genérica, dano 1d8, sem elemento fixo. Ver [Equipamento → Cubo Mágico](equipamento/index.md#equ-cubo-magico).

### Olho Mágico

Arma mágica genérica, dano 1d8, sem elemento fixo. Ver [Equipamento → Olho Mágico](equipamento/index.md#equ-olho-magico).

### Espada-Chave

Arma Híbrida, dano 1d8. Ver [Equipamento → Espada-Chave](equipamento/index.md#equ-espada-chave).

### Soqueira Pesada

Arma marcial pesada, dano 1d12. Ver [Equipamento → Soqueira Pesada](equipamento/index.md#equ-soqueira-pesada).

### Lâmina Dupla

Arma marcial, dano 1d6 (arma ancestral com lâmina em cada extremidade). Ver [Equipamento → Lâmina Dupla](equipamento/index.md#equ-lamina-dupla).

### Gadanha

Arma marcial pesada, dano 1d10. Ver [Equipamento → Gadanha](equipamento/index.md#equ-gadanha).

### Pique

Arma marcial pesada, dano 1d10 (lâminas gêmeas que se combinam num pique de alcance). Ver [Equipamento → Pique](equipamento/index.md#equ-pique).

### Glaive

Arma marcial de haste, dano 1d10. Ver [Equipamento → Glaive](equipamento/index.md#equ-glaive).

### Égide

Arma marcial (espada e escudo), dano 1d6. Ver [Equipamento → Égide](equipamento/index.md#equ-egide).

### Lâmina do Crepúsculo

Arma marcial pesada, dano 1d10 (renomeada de "Tirfing" — lâmina amaldiçoada, concede poder imenso mas corrói com trevas quem a empunha). Ver [Equipamento → Lâmina do Crepúsculo](equipamento/index.md#equ-lamina-do-crepusculo).

### Violino

Arma marcial, dano 1d6 (instrumento usado como arma contundente). Ver [Equipamento → Violino](equipamento/index.md#equ-violino).

### Báculo

Arma marcial, dano 1d8 (bastão com lâmina circular e cristal, símbolo dos bardos). Ver [Equipamento → Báculo](equipamento/index.md#equ-baculo).

### Bolsa de Truques

Arma marcial pesada, dano 1d10 (renomeada de "Pandora" — bolsa mágica com itens aleatórios). Ver [Equipamento → Bolsa de Truques](equipamento/index.md#equ-bolsa-de-truques).

### Tonfas

Par de tonfas, dano 1d6. Ver [Equipamento → Tonfas](equipamento/index.md#equ-tonfas).

### Bastão

Arma marcial de haste média, dano 1d8 (arma real é a Chamma). Ver [Equipamento → Bastão](equipamento/index.md#equ-bastao).

### Vajras

Arma marcial mística, dano 1d8. Ver [Equipamento → Vajras](equipamento/index.md#equ-vajras).

### Rapiers

Par de lâminas finas, dano 1d6. Ver [Equipamento → Rapiers](equipamento/index.md#equ-rapiers).

### Soluna

Arma marcial pesada, dano 1d10 (lâmina lendária, duas metades — Sol e Lua). Ver [Equipamento → Soluna](equipamento/index.md#equ-soluna).

### Revólver Maverick

Revólver pesado, dano 1d8 — quase uma espingarda de uma mão só, usado sempre sozinho por causa do coice e do poder de fogo (a outra mão fica livre). Ver [Equipamento → Revólver Maverick](equipamento/index.md#equ-revolver-maverick).

### Marreta Mágica

Arma marcial pesada, dano 1d12. Ver [Equipamento → Marreta Mágica](equipamento/index.md#equ-marreta-magica).

### Módulo Alado

Arma mágica (Foco Mágico), dano 1d10, ataca com Inteligência (enxame tecnológico de lâminas voadoras; não é empunhado — conta como Duas Mãos pra fins de regra). Ver [Equipamento → Módulo Alado](equipamento/index.md#equ-modulo-alado).

### Tridente

Arma marcial Leve, dano 1d8 (combina com Escudo). Ver [Equipamento → Tridente](equipamento/index.md#equ-tridente).

### Chicote

Arma marcial Finesse, dano 1d6 (alcance incomum, puxa e prende). Ver [Equipamento → Chicote](equipamento/index.md#equ-chicote).

### Mangual

Arma marcial pesada, dano 1d10 (ignora bônus de Escudo na Especial). Ver [Equipamento → Mangual](equipamento/index.md#equ-mangual).

### Zarabatana

Arma de pontaria, dano 1d4 (foco em veneno e status, não em dano bruto). Ver [Equipamento → Zarabatana](equipamento/index.md#equ-zarabatana).

### Pistola Arcana

Arma de pontaria Híbrida (Agilidade ou Inteligência), dano 1d8. Ver [Equipamento → Pistola Arcana](equipamento/index.md#equ-pistola-arcana).

## Propriedades de Arma

### Finesse

O usuário escolhe Força ou Agilidade (o que for maior) no teste de ataque. Ver [Equipamento → Armas Finesse](equipamento/regras.md#finesse).

### Híbrida

O usuário escolhe Força ou Inteligência (o que for maior) no teste de ataque. Ver [Equipamento → Armas Híbridas](equipamento/regras.md#hibrida).

### Dupla Empunhadura

Habilidade geral que exige duas armas específicas equipadas ao mesmo tempo; o dano soma os dados das duas. Ver [Equipamento → Dupla Empunhadura](equipamento/regras.md#dupla-empunhadura).

### Leve

Arma que ocupa só uma mão — a mão secundária fica livre pra outra arma Leve, um escudo, ou magia/interação. Ver [Equipamento → Leve](equipamento/regras.md#leve).

### Escudo (item) {: #escudo-item }

Item de mão secundária (Broquel, Escudo, Pesado ou Torre) que concede bônus passivo de Defesa. Escudo, Pesado e Torre habilitam a habilidade [Bloqueio](habilidades/buff.md); o Broquel habilita [Aparar](habilidades/buff.md) no lugar. Ver [Equipamento → Escudos](equipamento/index.md#equ-escudo). Não confundir com a **condição** [Escudo](#escudo), que dá pontos que absorvem dano.

## Grupos de Habilidade

### Marciais

Armas corpo a corpo / combate a curta distância. Ver [página do grupo](habilidades/marciais.md).

### Pontaria

Armas à distância e precisão (inclui feitiços de precisão). Ver [página do grupo](habilidades/pontaria.md).

### Mágicas Básicas

Uso básico de magia. Ver [página do grupo](habilidades/magicas-basicas.md).

### Mágicas por Elemento

Fogo, Gelo, Terra, Sombras, Luz, Raio, etc. Ver [página do grupo](habilidades/magicas-elementais.md).

### Sociais

Persuasão e afins. Ver [página do grupo](habilidades/sociais.md).

### Infiltração

Furtividade, ladinagem. Ver [página do grupo](habilidades/infiltracao.md).

### Mobilidade

Voo, deslocamento. Ver [página do grupo](habilidades/mobilidade.md).

### Buff

Incremento de força, imbuir elementos em armas, etc. Ver [página do grupo](habilidades/buff.md).

### Debuff

Desvantagens para inimigos ou em testes. Ver [página do grupo](habilidades/debuff.md).

### Suporte

Cura e apoio a aliados. Ver [página do grupo](habilidades/suporte.md).

## Elementos (dentro de Mágicas por Elemento)

### Fogo

Ver [Mágicas por Elemento → Fogo](habilidades/magicas-elementais.md#fogo).

### Terra

Ver [Mágicas por Elemento → Terra](habilidades/magicas-elementais.md#terra).

### Gelo

Ver [Mágicas por Elemento → Gelo](habilidades/magicas-elementais.md#gelo).

### Raio

Ver [Mágicas por Elemento → Raio](habilidades/magicas-elementais.md#raio).

### Sombras

Ver [Mágicas por Elemento → Sombras](habilidades/magicas-elementais.md#sombras).

### Luz

Ver [Mágicas por Elemento → Luz](habilidades/magicas-elementais.md#luz).

### Água

Ver [Mágicas por Elemento → Água](habilidades/magicas-elementais.md#agua).

### Vento

Ver [Mágicas por Elemento → Vento](habilidades/magicas-elementais.md#vento).

### Veneno

Ver [Mágicas por Elemento → Veneno](habilidades/magicas-elementais.md#veneno).

### Sangue

Ver [Mágicas por Elemento → Sangue](habilidades/magicas-elementais.md#sangue).

### Espaço-Tempo

Ver [Mágicas por Elemento → Espaço-Tempo](habilidades/magicas-elementais.md#espaco-tempo).

*(Outros elementos ainda sem habilidades — a criar)*
