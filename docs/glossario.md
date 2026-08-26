# Glossário de Termos

Os **146 termos** que o jogo usa: estatísticas do personagem, condições, tipos de dano, termos de resolução, armas, grupos e elementos. Cada um linka pra sua página de origem, e cada menção a um termo no resto do site abre o verbete num popover ao passar o mouse.

Há duas formas de chegar num termo: o **índice alfabético** abaixo, se você já sabe o nome, ou a **busca e o filtro por categoria**, se você está procurando o que existe.

## Termos de Resolução

### Vantagem

Role **2d100 e use o melhor**. Fontes múltiplas de Vantagem não acumulam — rola-se 2d100 uma vez só.

### Desvantagem

Role **2d100 e use o pior**. Também não acumula. Se uma mesma rolagem tiver Vantagem e Desvantagem ao mesmo tempo (de qualquer quantidade de fontes), **elas se cancelam** e rola-se 1d100 normal.

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

### Base de Resiliência

O Tier de ameaça de uma criatura — Comum, Treinado, Formidável, Lendário. Não soma mais como bônus fixo em nenhuma fórmula: serve só de referência de faixa esperada pros atributos que o Mestre escreve na ficha dela (um personagem jogador é sempre **Treinado**). Ver [Combate → Defesa](jogar/combate.md#defesa) e [Bestiário](mestre/criando-criaturas.md).

### Acúmulo de bônus

**Bônus numéricos planos de buffs diferentes não somam — vale o maior.** Um personagem sob Disciplina Marcial (+4 de dano) e Bênção Divina (+2 de dano) usa +4, não +6 (uma habilidade que declara empilhar **consigo mesma**, como a Bênção Divina, é exceção explícita e só empilha com ela própria). Bônus de fontes de natureza diferente (buff + item + traço racial) somam normalmente. **Resistências ao mesmo tipo de dano também não acumulam** — duas Resistências a Fogo valem uma.

### Resolução

Toda habilidade declara como se resolve: **Ataque** (o usuário rola d100 + Atributo contra o número-alvo do alvo — o padrão, ver [Testes de d100](jogar/testes.md)) ou **Teste de Resistência** (o **alvo** rola d100 + o atributo que a ficha declarar, contra o **Atributo de lançamento do usuário, cru** — usado quando o efeito acontece em **área**, quando o corpo resiste a ele **por dentro** (veneno, maldição plantada), ou quando não há como se esquivar dele: dobra do espaço, gravidade, sucção). Ver [Testes de d100 → Teste de Resistência](jogar/testes.md#teste-de-resistencia).

### Componentes

O que ativar uma habilidade exige fisicamente: **Verbal** (fala — negado por [Silenciado](#silenciado)), **Somático** (gesto — negado só por [Atordoado](#atordoado)) e **Material** (a arma ou foco precisa estar equipado). Ver [Regras de Habilidade → Componentes](jogar/regras-de-habilidade.md#componentes).

### Cooldown

Depois de usada, a habilidade fica indisponível por um tempo — **independente de quanto Mana sobrou**: sem cooldown, 1–2 [rodadas](#rodada), 3–4 rodadas, 1x por [cena](#cena) ou 1x por descanso, conforme o grau ou potência dela. Ver [Regras de Habilidade → Cooldown](jogar/regras-de-habilidade.md#cooldown).

### Vida

A barra que mede quanto dano o corpo aguenta antes de cair a 0. **Vida Máxima = 20 + Nível + (Defesa × 2)** + Vida de equipamento. Recupera metade num descanso curto, tudo num descanso longo. Ver [Dano e Cura](jogar/dano-e-cura.md#vida).

### Mana

O recurso que ativa toda Habilidade — não existe sistema de magia separado, a [Intensidade](#intensidade) escolhida é paga em Mana. **Mana Máximo = 20 + Nível + (Magia × 2)** + Mana de equipamento. Recupera metade num descanso curto, tudo num descanso longo. Ver [Mana](jogar/mana.md#mana-maximo).

### Estresse

A barra que mede quanto a cabeça aguenta, não o corpo. **Estresse Máximo = 20 + Nível + (Sanidade × 2)** + Estresse de equipamento. Encher a barra causa um Colapso imediato e, depois, uma Cicatriz permanente. Ver [Estresse](jogar/estresse.md).

### Intensidade

O quanto uma Habilidade entrega, escolhido na hora de ativar — o d100 só responde se acertou ou não, quem decide **quão forte** é a Intensidade. Vai de I (◈, efeito base) a III (◈◈◈, efeito completo), e o custo em Mana sobe junto. Ver [Regras de Habilidade](jogar/regras-de-habilidade.md#intensidade).

### Pontos de Ação

◈ — o que se gasta no turno pra mover, atacar ou usar uma Habilidade. Todo personagem tem **3 por turno**, sem exceção de raça, arma ou nível. Ver [Combate](jogar/combate.md).

### Defesa

Um dos oito atributos — resistência física, o quanto o corpo aguenta e encaixa impacto. Soma na [Vida](#vida) Máxima, e o próprio valor cru **é** a Fortitude Física. Ver [Os Oito Atributos](jogar/atributos.md).

### Evasão

O número-alvo que um ataque físico precisa superar pra acertar. **Evasão = Agilidade + Escudo/Couraça Natural**. Decide só **se** o golpe acerta — o quanto ele faz já foi escolhido pela [Intensidade](#intensidade) paga. Ver [Combate → Defesa](jogar/combate.md#defesa).

### Fortitude Física

O número-alvo contra veneno, doença, exaustão, petrificação e qualquer efeito que o corpo resiste por dentro, não desvia — **o próprio valor de [Defesa](#defesa), cru**. Ver [Combate → Defesa](jogar/combate.md#defesa).

### Fortitude Mágica

O número-alvo contra controle mental de origem mágica e maldição — **o próprio valor de Magia, cru**. Ver [Combate → Defesa](jogar/combate.md#defesa).

### Movimento

Quantas casas um personagem anda ao gastar ◈ pra se mover. **Movimento = 6 + (Agilidade ÷ 10)** casas, arredondado, mínimo 1. Ver [Combate → Movimento](jogar/combate.md#movimento).

### Iniciativa

Define a ordem dos turnos no início de um combate. Role **d100 + Agilidade + Sorte**; ordem decrescente do resultado decide quem age primeiro. Ver [Combate → Iniciativa](jogar/combate.md#iniciativa).

### Último Turno

A escolha que um personagem [Caído](#caido) tem no lugar de rolar contra a morte: levantar e gastar tudo. Um turno completo (3 PA, Mana, habilidades), em que **todo acerto é tratado como Crítico** — dano máximo, rolagem extra e sobe 1 Intensidade, mesmo fora do limiar de Sorte. Nenhuma cura funciona durante ele, e **ao fim o personagem morre**, sem rolagem. É a única troca do sistema em que se abre mão da chance de sobreviver por certeza de impacto. Regra completa em [O Último Turno](jogar/dano-e-cura.md#o-ultimo-turno).

## Condições

Estados que mudam o que uma criatura pode fazer — impostos por uma habilidade, pelo dano ou pela situação. Salvo quando a habilidade disser outra coisa, duram **até o fim do próximo turno do alvo**.

### Sangrando

Perde **4d4 de Vida** no início do próximo turno dele. **Role uma vez só e marque o mesmo resultado também em Estresse** — o mesmo sangue que sai do corpo é o que sobra na cabeça. Efeito de uma vez só — ferida que fecha.

- **Não acumula.** Reaplicado antes de disparar, vale só o **dado maior** (um "Sangrando 6d4" substitui o 4d4 — mesma lógica de Queimando). Depois de disparar, o alvo pode voltar a Sangrar normalmente.

### Queimando

Perde **4d4 de Vida imediatamente ao pegar fogo**, e mais **4d4 no início de cada turno dele**. **Cada uma dessas rolagens vale o mesmo em Estresse** — pegar fogo (e continuar em chamas) é tão traumático quanto doloroso. Assinatura do elemento [Fogo](habilidades/magicas-elementais.md#fogo) — diferente de Sangrando justamente por não ter prazo.

- **Não acumula.** Pegar fogo de novo não soma um segundo dado: vale o valor maior entre os dois (mesma lógica do [Escudo](#escudo)). Uma habilidade que diz "Queimando causando 8d4 por turno" simplesmente substitui o 4d4 enquanto durar — o Estresse escala junto.
- **Não para sozinho durante o combate.** Termina de três formas: o alvo gasta uma **Ação Básica** pra se apagar, um aliado **adjacente** gasta a dele, ou o alvo entra em contato com água em quantidade (o Mestre decide o que conta). **Sofrer dano de Gelo ou Água também apaga o fogo.**
- **Espalhamento:** quando uma habilidade diz que o fogo "se espalha" pra uma criatura adjacente, **o usuário escolhe qual** (pode ser um aliado — fogo não distingue). Quem pegou fogo por espalhamento **não espalha de novo**: não há cadeia.
- **Apaga no fim do combate.** Encerrada a cena de combate, o fogo se apaga sozinho — ninguém sai queimando pela estrada.

### Lento

Movimento reduzido à **metade**. Afeta só o **Movimento** (a ação de ◈) — deslocamentos concedidos por habilidades (saltos, investidas, teleportes) não são reduzidos.

### Imóvel

**Movimento 0** — não sai do lugar **por vontade própria**, nem voando. Continua agindo normalmente: Ações Básicas, Habilidades e Reações seguem disponíveis. É o degrau acima de Lento, e não se confunde com [Atordoado](#atordoado), que trava tudo.

!!! regra "Força externa ainda move — e teleporte também"
    Empurrar, puxar e teleportar não são movimento do alvo — são coisas feitas *a* ele, e funcionam normalmente contra quem está Imóvel. Um alvo preso no lugar pode ser arrancado dele por um empurrão de Vento ou pela [Dobra Espacial](habilidades/espaco-tempo.md). O mesmo vale pro **teleporte próprio**: quem está Imóvel não anda nem salta, mas ainda pode se teleportar (Passo Sombrio, Fora de Lugar) — ele não se move, ele deixa de estar ali. Deslocamentos **físicos** de habilidade (saltos, investidas) continuam negados.

### Atordoado

**Não pode agir** — nem ação, nem movimento, nem reação. Marca **3d6 de Estresse** ao ficar Atordoado — perder o controle do próprio corpo é perturbador.

### Amedrontado

O pavor trava a pontaria e o julgamento: enquanto durar, o alvo rola com [Desvantagem](#desvantagem) em qualquer teste de ataque, e marca **3d6 de Estresse** ao ficar Amedrontado. Salvo quando a habilidade disser outra coisa, dura até o fim do próprio próximo turno do alvo.

### Cego

Não enxerga: rola com [Desvantagem](#desvantagem) em qualquer teste de ataque, ataques contra o alvo rolam com [Vantagem](#vantagem), e marca **2d6 de Estresse** ao ficar Cego. Salvo quando a habilidade disser outra coisa, dura até o fim do próprio próximo turno do alvo.

### Possuído

Outra criatura está no controle do corpo. Quem possui gasta os **◈ do possuído** e usa as habilidades, a Vida e o Mana dele; o possuidor **sai do mapa** enquanto durar, e não pode ser alvo direto. O possuído marca **5d6 de Estresse** ao ser possuído — perder o próprio corpo pra outra mente é uma das piores coisas que podem acontecer com alguém.

- **O jogador continua jogando.** No início de cada turno dele, o personagem possuído pode gastar o turno inteiro (**◈◈◈**) e rolar **d100 + Magia** contra a [Fortitude Mágica](jogar/combate.md#defesa) do possuidor. Passando, expulsa-o.
- **[Luz](habilidades/magicas-elementais.md#luz) atravessa:** dano de Luz no corpo possuído fere **o possuidor**, não o corpo.
- **Se o corpo cair a 0 de Vida**, a possessão acaba e o possuidor reaparece adjacente.

Quem tira alguém dessa condição de fora é o [Exorcismo](habilidades/suporte.md).

### Petrificado

A carne vira pedra, de baixo pra cima. Acumula em **graus**, como o [Exausto](#exausto) — nunca cai de uma vez, e é isso que dá ao grupo tempo de agir:

| Grau | Efeito |
|---|---|
| **1** | fica [Lento](#lento) — a pedra sobe pelas pernas |
| **2** | fica [Imóvel](#imovel) |
| **3** | **não pode agir** (nem ação, nem movimento, nem reação), e o corpo é pedra: [Resistência](#resistencia) a [Cortante](#cortante), [Perfurante](#perfurante) e [Impacto](#impacto). Não respira, não sangra, não envelhece |

**Some 1 grau** por acerto do efeito que petrifica. Quem aplica declara — nenhuma habilidade leva do 0 ao 3 num golpe só. Ao atingir o **grau 1** pela primeira vez (sentir a própria carne endurecer), o alvo marca **5d6 de Estresse**.

**Nos graus 1 e 2**, remove 1 grau cada vez que o alvo recebe uma habilidade que **cure Vida** (a Intensidade não importa), ou por [descanso longo](jogar/exploracao.md#descanso). **No grau 3**, a pedra já tomou conta do corpo — cura comum não basta: só [Panaceia](habilidades/suporte.md) ou descanso longo removem o grau.

!!! cuidado "Estátua quebrada não volta"
    No grau 3 o corpo é pedra — e pedra racha. Se ele sofrer dano que o levaria a 0 de Vida enquanto está petrificado, o personagem **morre de vez**: não fica [Caído](jogar/dano-e-cura.md#chegando-a-0-de-vida), não rola contra a morte, não há [Ressuscitar](habilidades/suporte.md) que junte os cacos. A resistência a dano físico existe justamente pra dar ao grupo a chance de tirar a estátua da linha de fogo antes disso.

### Derrubado

Está **no chão**. Enquanto Derrubado, seu Movimento é 0, e ataques **corpo a corpo** contra ele rolam com [Vantagem](#vantagem). **Levantar custa ◈ (1)** no próprio turno e encerra a condição. Não se confunde com **Caído** ([a 0 de Vida](jogar/dano-e-cura.md#chegando-a-0-de-vida)) — Derrubado é chão, Caído é morte chegando.

### Desprevenido

Foi pego de surpresa: **não pode agir nem reagir durante a primeira rodada do combate**. É o que acontece com um grupo emboscado sem vigia (ver [Exploração](mestre/exploracao.md#detectar-e-desarmar)). "Surpreendido" é a mesma condição.

### Agarrado

Está preso por uma criatura ou restrição física: fica [Imóvel](#imovel) enquanto durar, e marca **2d6 de Estresse** ao ser agarrado. **Escapar custa ◈ (1)** e um teste de **Ataque ou Agilidade** (o que for maior) contra a Evasão de quem prende — ou contra a Dificuldade da restrição, se for um objeto. Quem prende solta automaticamente se ficar Atordoado ou Caído.

### Silenciado

Impede a ativação de qualquer habilidade que tenha [Componente](#componentes) Verbal — inclusive Habilidades Sociais baseadas em fala. Habilidades sem esse componente continuam disponíveis normalmente.

### Marcado

O **próximo ataque de um aliado** contra ele **nesta rodada** rola com Vantagem.

### Envenenado

Perde **4d4 de Vida por acúmulo** no início de cada turno dele, até ser curado. **Cada rolagem de dano vale o mesmo em Estresse.** Diferente do fogo, o veneno leva tempo pra agir: **não há dano no momento em que é aplicado** — a primeira perda de Vida acontece no início do próximo turno do alvo.

- **Acúmulos:** cada nova aplicação soma 1 acúmulo, e cada acúmulo vale 4d4 por turno (1 acúmulo = 4d4, 2 = 8d4, 3 = 12d4). O **máximo é 3 acúmulos** (12d4 por turno).
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

**Some 1 grau** a partir do **segundo dia** de privação (o primeiro só incomoda) e por noite sem descanso adequado depois de um dia de esforço — ver [Exaustão](jogar/exploracao.md#exaustao), que é a regra completa. Ao atingir o **grau 3** (desmaiar), marca **3d6 de Estresse**. **Remove 1 grau** por [descanso longo](jogar/exploracao.md#descanso) — desde que a causa tenha sido resolvida (comeu, bebeu, se aqueceu). Descansar com fome não remove nada.

### Risco

Algumas habilidades cobram um preço de quem as usa: se **algum dos dados de dano cair em 1**, a habilidade escapa ao controle e o usuário sofre o efeito descrito na ficha dela. Reservado a habilidades de tema perigoso — lâminas amaldiçoadas, magia de sangue, poder emprestado.

### Caído

A 0 de Vida o personagem cai: **inconsciente, sem agir e sem rolar nada**, com uma única chance de não morrer. No início do próximo turno dele, role **d100 contra Dificuldade 50** — sem somar Atributo nenhum, porque o dado mede só a sorte do momento. **Sucesso:** fica [Estável](#estavel). **Falha:** morre.

- **Sair antes da rolagem:** um aliado adjacente gasta ◈ e passa num teste de Exploração contra Dificuldade 50 (fica Estável direto), ou qualquer cura o traz de volta com aquela Vida.
- **Ou o [Último Turno](#ultimo-turno):** desistir de sobreviver pra jogar um turno completo com todo acerto virando Crítico.
- **Vale só para personagens jogadores** — uma criatura a 0 de Vida morre.

Regra completa em [Chegando a 0 de Vida](jogar/dano-e-cura.md#chegando-a-0-de-vida).

### Estável

Sobreviveu ao [Caído](#caido) — por ter passado na rolagem contra a morte, ou porque um aliado o estabilizou a tempo. Continua inconsciente, mas **fora de risco**: não rola mais contra a morte, e **acorda ao fim da cena com 1 de Vida**. Qualquer cura o traz de volta antes disso.

## Efeitos de Terreno

Ao contrário das Condições, que ficam grudadas numa criatura, estes efeitos ficam grudados no **chão** — e valem para quem quer que passe por ali.

Duas regras valem pra **todo** efeito de terreno criado por habilidade, de qualquer elemento:

- **Não somam.** Onde duas zonas de dano se sobrepõem — sejam de Sombras, Fogo, Raio ou qualquer outro tema — vale só a **mais forte**, nunca a soma.
- **Cobertura e prazo padrão:** salvo texto contrário na ficha, o terreno criado cobre a **área da habilidade** e dura **até o fim do combate**.

### Terreno Difícil

Atravessar **custa o dobro de Movimento**: cada casa consome duas. Vale para escombros, lama, gelo, mato fechado, escada, e para o terreno que algumas habilidades criam.

Não é dano nem condição — é o chão cobrando pedágio. Num sistema onde deslocar-se custa ◈, dobrar esse custo é uma das formas mais baratas de mudar como uma luta se desenrola.

### Zona Amaldiçoada

Assinatura de [Sombras](habilidades/magicas-elementais.md#sombras) em área: a região atingida continua ferindo depois do golpe. Qualquer criatura que **entrar** na área, ou que **terminar o turno** dentro dela, sofre o dano indicado pela habilidade (tipicamente 4d4, ou 8d4 na Intensidade III).

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

Toda arma concede 3 habilidades, aprendidas nessa ordem obrigatória (ver [Equipamento](equipamento/index.md)). O grau **não** define o custo — cada uma tem suas próprias [Intensidades](jogar/regras-de-habilidade.md#intensidade) I/II/III. O que o grau define é o quanto a técnica entrega e o quanto de Mana ela cobra:

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

Arma marcial, dano 1d4. Ver [Equipamento → Adagas](equipamento/index.md#equ-adagas).

### Alfange

Arma marcial, dano 1d8. Ver [Equipamento → Alfange](equipamento/index.md#equ-alfange).

### Garras

Arma marcial, dano 1d6. Ver [Equipamento → Garras](equipamento/index.md#equ-garras).

### Katana Nodachi

Arma marcial (duas mãos), dano 1d10 (lâmina longa clássica). Ver [Equipamento → Katana Nodachi](equipamento/index.md#equ-katana-nodachi).

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

Arma mágica (Foco Mágico), dano 1d8, ataca com Magia (invoca criaturas através de uma gema com pentagramas e hexagramas). Ver [Equipamento → Manopla Mística](equipamento/index.md#equ-manopla-mistica).

### Pistolas

Dupla de pistolas leves, dano 1d6 — usadas sempre em par, uma em cada mão. Ver [Equipamento → Pistolas](equipamento/index.md#equ-pistolas).

### Punhal

Adaga, dano 1d6. Ver [Equipamento → Punhal](equipamento/index.md#equ-punhal).

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

Arma marcial, dano 1d6. Ver [Equipamento → Florete](equipamento/index.md#equ-florete).

### Flintlock

Pistola de precisão, dano 1d8. Ver [Equipamento → Flintlock](equipamento/index.md#equ-flintlock).

### Katana Muramasa

Arma marcial (duas mãos), dano 1d10 (lâmina amaldiçoada, exige sangue). Ver [Equipamento → Katana Muramasa](equipamento/index.md#equ-katana-muramasa).

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

Arma marcial de haste Híbrida, dano 1d10. Ver [Equipamento → Glaive](equipamento/index.md#equ-glaive).

### Égide

Arma marcial (espada e escudo), dano 1d6. Ver [Equipamento → Égide](equipamento/index.md#equ-egide).

### Lâmina do Crepúsculo

Arma marcial pesada, dano 1d10 (renomeada de "Tirfing" — lâmina amaldiçoada, concede poder imenso mas corrói com trevas quem a empunha). Ver [Equipamento → Lâmina do Crepúsculo](equipamento/index.md#equ-lamina-do-crepusculo).

### Violino

Arma marcial de Social, dano 1d6 (instrumento sonoro, exige Social 20). Ver [Equipamento → Violino](equipamento/index.md#equ-violino).

### Báculo

Arma marcial Ressonante, dano 1d8 (bastão com lâmina circular e cristal, símbolo dos bardos). Ver [Equipamento → Báculo](equipamento/index.md#equ-baculo).

### Bolsa de Truques

Foco mágico pesado, dano 1d10 (renomeada de "Pandora" — bolsa mágica com itens aleatórios). Ver [Equipamento → Bolsa de Truques](equipamento/index.md#equ-bolsa-de-truques).

### Tonfas

Par de tonfas, dano 1d6. Ver [Equipamento → Tonfas](equipamento/index.md#equ-tonfas).

### Bastão

Arma marcial de haste média, dano 1d8 (arma real é a Chamma). Ver [Equipamento → Bastão](equipamento/index.md#equ-bastao).

### Vajras

Arma marcial de Magia, dano 1d8 (cetro divino, exige Magia 30). Ver [Equipamento → Vajras](equipamento/index.md#equ-vajras).

### Rapiers

Par de lâminas finas, dano 1d6. Ver [Equipamento → Rapiers](equipamento/index.md#equ-rapiers).

### Soluna

Arma marcial pesada, dano 1d10 (lâmina lendária, duas metades — Sol e Lua). Ver [Equipamento → Soluna](equipamento/index.md#equ-soluna).

### Revólver Maverick

Revólver pesado Híbrido, dano 1d8 — quase uma espingarda de uma mão só, usado sempre sozinho por causa do coice e do poder de fogo (a outra mão fica livre). Ver [Equipamento → Revólver Maverick](equipamento/index.md#equ-revolver-maverick).

### Marreta Mágica

Arma marcial pesada Híbrida, dano 1d12. Ver [Equipamento → Marreta Mágica](equipamento/index.md#equ-marreta-magica).

### Módulo Alado

Arma mágica (Foco Mágico), dano 1d10, ataca com Magia (enxame tecnológico de lâminas voadoras; não é empunhado — conta como Duas Mãos pra fins de regra). Ver [Equipamento → Módulo Alado](equipamento/index.md#equ-modulo-alado).

### Tridente

Arma marcial Leve, dano 1d8 (combina com Escudo). Ver [Equipamento → Tridente](equipamento/index.md#equ-tridente).

### Chicote

Arma marcial, dano 1d6 (alcance incomum, puxa e prende). Ver [Equipamento → Chicote](equipamento/index.md#equ-chicote).

### Mangual

Arma marcial pesada, dano 1d10 (ignora bônus de Escudo na Especial). Ver [Equipamento → Mangual](equipamento/index.md#equ-mangual).

### Zarabatana

Arma de pontaria, dano 1d4 (foco em veneno e status, não em dano bruto). Ver [Equipamento → Zarabatana](equipamento/index.md#equ-zarabatana).

### Pistola Arcana

Arma de pontaria Híbrida (Ataque ou Magia), dano 1d8. Ver [Equipamento → Pistola Arcana](equipamento/index.md#equ-pistola-arcana).

## Propriedades de Arma

### Dano Desarmado

Golpes desarmados (socos, chutes) não usam o dado de nenhuma arma — escalam sozinhos conforme o nível do personagem: 2d6 (nível 0–25), 2d12 (26–50), 2d20 (51–75), 3d20 (76–100). Traço racial de "1 grau acima" empurra pra faixa seguinte da tabela. O tipo de dano é [Impacto](#impacto), salvo quando um traço racial disser outra coisa. Ver [Habilidades Marciais → Dano Desarmado](habilidades/marciais.md#dano-desarmado).

### Híbrida

O usuário escolhe Ataque ou Magia (o que for maior) no teste de ataque. Ver [Equipamento → Armas Híbridas](jogar/regras-de-equipamento.md#hibrida).

### Ressonante

O usuário escolhe, no teste de ataque, entre Físico (Ataque, dano Impacto) e Arcano (Magia, dano Arcano) — o tipo de dano muda junto com o atributo. Ver [Equipamento → Armas Ressonantes](jogar/regras-de-equipamento.md#ressonante).

### Dupla Empunhadura

Habilidade geral que exige duas armas específicas equipadas ao mesmo tempo; o dano soma os dados das duas. Ver [Equipamento → Dupla Empunhadura](jogar/regras-de-equipamento.md#dupla-empunhadura).

### Leve

Arma que ocupa só uma mão — a mão secundária fica livre pra outra arma Leve, um escudo, ou magia/interação. Ver [Equipamento → Leve](jogar/regras-de-equipamento.md#leve).

### Escudo (item) {: #escudo-item }

Item de mão secundária (Broquel, Escudo, Pesado ou Torre) que concede bônus passivo de Defesa e habilita um punhado de habilidades gerais que exigem ter algum Escudo equipado — [Cúpula Protetora](habilidades/buff.md), [Muralha de Ferro](habilidades/buff.md), [Escudo Elemental](habilidades/buff.md) e [Ataque com Escudo](habilidades/marciais.md) funcionam com qualquer um deles; [Bloqueio](habilidades/buff.md) exige Escudo, Pesado ou Torre, e o Broquel habilita [Aparar](habilidades/buff.md) no lugar. Ver [Equipamento → Escudos](equipamento/index.md#equ-escudo). Não confundir com a **condição** [Escudo](#escudo), que dá pontos que absorvem dano.

## Grupos de Habilidade

### Marciais

Armas corpo a corpo / combate a curta distância. Ver [página do grupo](habilidades/marciais.md).

### Pontaria

Armas à distância e precisão (inclui feitiços de precisão). Ver [página do grupo](habilidades/pontaria.md).

### Mágicas por Elemento

Fogo, Gelo, Terra, Sombras, Luz, Raio, Arcano, etc. Ver [página do grupo](habilidades/magicas-elementais.md).

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

### Necromancia

Drenar vigor, amaldiçoar, erguer mortos, gastar a própria vitalidade. Ver [página do grupo](habilidades/necromancia.md).

### Projeção Mental

Telepatia, ler mentes, ilusão mental, dano psíquico — funciona em qualquer mente, sem depender de palavras (não confundir com [Sociais](#sociais), que é persuasão via fala/presença). Ver [página do grupo](habilidades/projecao-mental.md).

### Alquimia de Mana

Mana altera a matéria: endurecer o corpo, transmutar, consertar objetos, imbuir armas. Ver [página do grupo](habilidades/alquimia-de-mana.md).

### Percepção Arcana

Enxergar o invisível, rastrear pelo resíduo de mana, premonição em combate. Ver [página do grupo](habilidades/percepcao-arcana.md).

### Conjuração

Trazer aliados de outros lugares/planos pra lutar ao seu lado — familiar simples, aliado de combate, vínculo com um Ser maior, e o Companheiro Animal. Ver [página do grupo](habilidades/conjuracao.md).

### Espaço-Tempo

Reposicionar à força, distorcer gravidade e manipular o fluxo do tempo — teleporte, puxar, empurrar, ganhar uma ação extra, refazer um resultado que já aconteceu. Ver [página do grupo](habilidades/espaco-tempo.md).

## Elementos (dentro de Mágicas por Elemento)

### Fogo

**Consome com o tempo.** [Queimando](#queimando), que se espalha pros adjacentes e escala até 8d4 por turno. Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Terra

**Põe no chão e prende.** Derruba o alvo, e escala até [Lento](#lento) e [Imóvel](#imovel). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Gelo

**Trava o movimento.** [Lento](#lento), depois sem Reações, até [Imóvel](#imovel). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Raio

**Rouba a ação.** Tira a Reação do alvo, depois a Ação Básica também, até [Atordoar](#atordoado). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Sombras

**Nega o terreno e drena.** Deixa uma [Zona Amaldiçoada](#zona-amaldicoada) que persiste por rodadas, ou dreno de Vida crescente contra alvo único. Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Luz

**Prende e cala.** Tira a Reação e aplica [Marcado](#marcado), até deixar o alvo [Imóvel](#imovel). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Água

**Arrasta.** Puxa o alvo pra perto, cada vez mais longe e mais [Lento](#lento). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Vento

**Arremessa longe.** Empurra o alvo cada vez mais forte, até derrubar. Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Veneno

**Acumula.** [Envenenado](#envenenado) que empilha a cada nova aplicação, em vez de resetar. Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

### Sangue

**Troca Vida por poder.** Custa Vida em vez de Mana, e o dreno cresce com a Intensidade, sempre sob [Risco](#risco). Ver [Assinatura de Elemento](habilidades/magicas-elementais.md#assinatura-de-elemento).

*(Outros elementos ainda sem habilidades — a criar)*
