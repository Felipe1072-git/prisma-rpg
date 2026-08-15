# Proposta — Conjuração de Pacto e habilidades novas (Necromancia, Projeção Mental, Alquimia de Mana, Percepção Arcana)

Rascunho de trabalho, não aprovado. Nada aqui deve ser copiado pra `docs/` sem revisão do autor.
Formato e custos seguem as convenções já em uso nos quatro grupos novos e nos grupos irmãos
(Debuff, Buff, Suporte) — nenhuma escala nova foi inventada.

**Convenção nova (2026-08-15):** toda habilidade que causa dano agora declara o tipo
explicitamente com um campo **Dano:** no bullet de meta (junto de Atributo/Defesa/Alcance/Alvos),
em vez de depender do leitor lembrar a regra padrão de
[Tipos de Dano](../docs/jogar/dano-e-cura.md#tipos-de-dano) (habilidade não-elemental e
não-de-arma = Arcano, salvo indicação contrária). Todas as 11 habilidades destes quatro grupos
que causam dano direto foram marcadas **Dano: Arcano** — nenhum tipo novo foi criado ainda; essa
é uma decisão em aberto, separada desta revisão (ver conversa sobre tipos de dano pra grupos
novos). Essa convenção de declarar o campo explicitamente ainda não foi retroaplicada nas 580
habilidades já publicadas em `docs/` — isso é trabalho futuro, fora do escopo desta proposta.

---

## Conjuração de Pacto — opções mecânicas

O quinto grupo ainda não tem mecânica. Antes de escrever qualquer habilidade dele, o autor
precisa decidir **como a criatura invocada existe na mesa**. Abaixo, três caminhos — não é
recomendação de qual escolher, é a análise dos três pra decisão.

Um precedente já existe no jogo e vale como âncora: **Vínculo Selvagem** (Buff,
`docs/habilidades/buff.md`) já é uma invocação — um companheiro animal com ficha própria e
fixa (15 de Vida, Defesa 10), que ataca sozinho no início do turno do usuário sem gastar PA
nem exigir controle separado. É essencialmente o Caminho A abaixo, já em produção.

### Caminho A — Companheiro de Pacto (ficha própria fixa, ação automática)

Mesma arquitetura de Vínculo Selvagem, reskinada pro tema de Conjuração (espírito, familiar
demoníaco, elemental menor, arma etérea que luta sozinha).

- **Como age:** não tem turno próprio nem exige controle separado. No início de cada turno do
  usuário, a criatura invocada ataca a criatura hostil mais próxima automaticamente, sem
  gastar Mana ou PA — o jogador só descreve o alvo se houver escolha. O jogador "controla" no
  sentido de decidir a invocação inicial e, no máximo, redirecionar o alvo do ataque.
- **Duração:** até o próximo descanso longo, ou até a invocação ser destruída (Vida própria,
  baixa). Se o usuário cair a 0 de Vida, a invocação foge/some e volta a aparecer no próximo
  descanso longo.
- **Ficha:** própria e simplificada — Vida fixa, Defesa fixa, um único dado de ataque que sobe
  com a Intensidade (ex: 1d6 → 2d6 → 3d6, no molde exato de Vínculo Selvagem). **Não** reaproveita
  o Bestiário — os números do Bestiário foram calibrados pra ameaça de Mestre, não pra escala de
  um PJ.
- **Custo:** Intensidade I/II/III normal (◈+Mana), na faixa Moderada do grupo (5–12 Mana), como
  qualquer habilidade geral.
- **Peso de mesa:** o mais leve dos três — zero rolagens extras de iniciativa, zero turno extra
  pra administrar. O ataque da invocação é só mais uma linha no próprio turno do jogador.
- **Escala:** como o dado de dano só sobe com a Intensidade escolhida (não com o nível do
  personagem), a invocação **nunca vira um segundo combatente relevante** — ela é sempre um
  complemento modesto, em qualquer nível. Isso resolve o problema de escala do enunciado, mas
  ao custo de nunca entregar a fantasia de "um exército pessoal" ou "uma fera poderosa lutando
  ao seu lado".
- **Faz sentido como Suprema?** Não precisa — Vínculo Selvagem já prova que isso funciona como
  habilidade geral comum (Buff, Moderado). Uma versão Suprema desse caminho existiria só se
  quisesse companheiro mais forte que o padrão (ficha maior, mais de um ataque por turno).

### Caminho B — Aliado de Combate (ficha do Bestiário, turno próprio, o Mestre controla)

A invocação vira um combatente de verdade: rola a própria Iniciativa, age no próprio turno,
controlada pelo Mestre como um NPC aliado — como convocar um mini-chefe temporário.

- **Como age:** turno independente na ordem de Iniciativa. O Mestre decide os PA dela, se
  move, ataca, eventualmente foge — como qualquer criatura do Bestiário.
- **Duração:** N rodadas (2–4, escalando com Intensidade) pra uma versão comum, ou até o fim
  da cena pra uma versão de custo mais alto/Suprema.
- **Ficha:** reaproveita o Bestiário diretamente — o jogador escolhe (ou a habilidade fixa) uma
  criatura existente de Tier Comum ou Treinado como a forma da invocação, e ela roda com as
  regras normais de criatura daquele Tier (PA por Tier, ataques de custo fixo se for
  Comum/Treinado).
- **Custo:** aqui mora o problema central do enunciado — o Bestiário foi calibrado pra ser
  ameaça de Mestre, não força de PJ. Duas formas de amarrar isso:
  - **Fixar sempre no Tier Comum**, e deixar a Intensidade comprar só duração ou quantidade —
    assim a invocação nunca ultrapassa "um corpo a mais modesto", em qualquer nível.
  - **Reservar Tier Treinado (ou acima) só pra uma Suprema** — custo fixo alto (16+ Mana), 1x
    por descanso, puxando uma criatura Treinada pra lutar a cena inteira. Ainda assim, um
    Treinado tem a mesma força de combate de um personagem — em nível 1 isso efetivamente
    **dobra o grupo por uma cena**, o que é forte demais sem alguma restrição extra (ex: só
    fora de combates decisivos, ou com chance de a invocação agir contra ordens).
- **Peso de mesa:** o mais pesado dos três — é literalmente mais um turno pro Mestre resolver a
  cada rodada, em cima de tudo que ele já administra (os próprios NPCs/monstros da cena).
  Some isso ao limite de 8 criaturas em cena (ver Montagem de Encontro) e a invocação de um PJ
  passa a competir por esse teto.
- **Escala:** a mais difícil de equilibrar dos três, exatamente pela tensão acima — Comum fixo
  é seguro mas frustrante em nível alto (some no ruído); Treinado é forte demais em nível baixo.
- **Faz sentido como Suprema?** É onde esse caminho fica mais defensável — como Suprema, é
  1x por descanso, cara, declaradamente rara, e o Mestre sabe que só vai acontecer uma vez por
  sessão de verdade. Como habilidade comum de Intensidade I/II/III, o risco de desequilíbrio
  (e de atrasar a mesa) é mais alto.

### Caminho C — Efeito instantâneo sem ficha (invocação-como-golpe)

A "invocação" não tem ficha nem turno — é um efeito de uma habilidade comum (like Garra
Demoníaca ou Esquife de Ossos em Debuff, que já são "invocações" no flavor: uma garra
espectral, uma boca que se abre no chão) que aparece, resolve um efeito único, e desaparece.

- **Como age:** não age — é resolvido no mesmo teste de ataque da habilidade que a convocou.
  Não há ação própria, não há ficha, não há nada pra controlar.
- **Duração:** instantânea, ou no máximo uma zona que persiste 1–3 rodadas (como Zona
  Amaldiçoada) sem nenhum ator dentro dela.
- **Ficha:** nenhuma — mecanicamente é uma habilidade de Debuff/Necromancia comum.
- **Custo:** Intensidade I/II/III na escala normal do grupo (2–9 Mana), igual a qualquer
  habilidade de ataque.
- **Peso de mesa:** nenhum além do normal — funciona exatamente como toda outra habilidade do
  jogo já funciona.
- **Escala:** automática — como escala só pela Intensidade (igual dano de qualquer outra
  habilidade), vale em qualquer nível sem ajuste nenhum.
- **Faz sentido como Suprema?** Não precisa nunca — esse caminho não pede custo especial, é o
  formato padrão de qualquer habilidade de dano/efeito do jogo.
- **A ressalva:** isso é o caminho mais seguro e mais barato de balancear, mas é questionável
  se ele *é* de fato "Conjuração/Invocação" na fantasia que o nome promete, ou se é só
  Debuff/Necromancia com um nome mais chamativo. Se o grupo inteiro fosse feito só disso, vale
  perguntar se ele merece ser grupo próprio em vez de virar mais um subtema dentro de Debuff ou
  Necromancia.

### Observação (não é decisão — só um padrão que apareceu sozinho analisando os três)

Os três caminhos não são mutuamente exclusivos dentro do mesmo grupo — um grupo de Conjuração
poderia ter habilidades comuns no molde do Caminho A ou C (companheiro fixo modesto, ou golpe
instantâneo com nome de invocação) e reservar o Caminho B só pra uma única Suprema por
arquétipo de pacto, do jeito que Vínculo Selvagem já convive no Buff ao lado de habilidades bem
diferentes dele. Fica pro autor decidir se quer estreitar pra um caminho só (mais consistente)
ou misturar (mais variedade, mais trabalho de balancear cada uma na hora de escrever).

---

## Necromancia — habilidades propostas

*Grupo existente: Derrotar, Aumento Sombrio, Flor Carmesim, Encanto das Trevas. As sete abaixo
cobrem as quatro direções combinadas: maldição que piora com o tempo, dreno em área, erguer
morto-vivo temporário (sem pisar em Ressuscitar), e enfraquecer resistência a dano.*

**Praga Definhante**

*Uma podridão lenta se instala sob a pele do alvo — hoje é uma pontada, amanhã é a Vida indo embora.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d4 de dano + alvo perde 1d4 de Vida no início do próprio próximo turno.
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d4 de dano + alvo perde 1d4 de Vida no início do próximo turno dele, e mais 2d4 no início do turno seguinte a esse (a praga piora a cada disparo).
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 1d4 de dano + alvo perde 1d4 de Vida no início do 1º turno seguinte, 2d4 no 2º, e 3d4 no 3º.
- **Crítico (20 natural):** dano máximo (4) + 1d4 extra, e sobe 1 Intensidade

**Sopro do Túmulo**

*O ar fica frio e pesado — a vida ao redor é puxada pra dentro do usuário.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 2 casas de raio do ponto
- **Intensidade I — ◈ (1 PA) + 3 Mana:** 1d6 de dano em cada alvo, e o usuário recupera Vida igual à metade do dano total causado.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** 1d6 de dano em cada alvo, e o usuário recupera Vida igual ao dano total causado.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** 1d8 de dano em cada alvo, e o usuário recupera Vida igual ao dano total causado.
- **Crítico (20 natural):** dano máximo do dado + rolagem extra em todos, e sobe 1 Intensidade

**Levante Breve**

*O corpo se levanta, mas o que o move não é mais quem ele foi.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Custo fixo:** ◈◈◈ (3 PA) + 12 Mana | **Atributo:** Inteligência | **Alcance:** 3 casas | **Alvos:** 1 aliado morto, cujo corpo ainda esteja na cena
- **Efeito:** o corpo se levanta como um servo temporário — **não é o aliado revivido**, e nada disso conta como cura ou ressurreição (não interfere com [Ressuscitar](../docs/habilidades/suporte.md), nem consome a chance única dele). O servo tem metade da Vida máxima que o aliado tinha, a mesma Defesa física dele, e ataca a criatura hostil mais próxima no início de cada turno do usuário, sem gastar Mana ou PA, causando 1d8 de dano corpo a corpo (Impacto — o servo golpeia com o próprio corpo). Dura até o fim da cena ou até ser destruído — depois disso, o corpo desmorona em pó e não pode ser levantado de novo.
- *(Sem Intensidade — Custo fixo: efeito absoluto sem nada pra graduar)*
- ⚠ **Pra decidir:** vale checar com o autor se isso deveria ter alguma cláusula de consentimento/tom (erguer o corpo de um aliado é pesado narrativamente) antes de virar regra publicada.

**Corrosão da Alma**

*A alma é roída por dentro — o que protegia o corpo já não protege mais.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d6 de dano + até o fim do próximo turno do alvo, qualquer Resistência a dano que ele tenha é ignorada.
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d6 de dano + o mesmo, por 2 rodadas, e o alvo perde 2 de Defesa nesse período.
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 1d6 de dano + o mesmo, por 3 rodadas, e qualquer Imunidade a dano do alvo vira apenas Resistência nesse período.
- **Crítico (20 natural):** dano máximo (6) + 1d6 extra, e sobe 1 Intensidade

**Preço de Sangue**

*Você não paga em Mana. Você paga na moeda mais cara: você mesmo.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Custo em Vida:** esta habilidade não gasta Mana — o custo de cada Intensidade é pago em **Vida**
- **Intensidade I — ◈ (1 PA) + 1d4 de Vida:** 2d6 de dano.
- **Intensidade II — ◈◈ (2 PA) + 2d4 de Vida:** 3d6 de dano.
- **Intensidade III — ◈◈◈ (3 PA) + 3d4 de Vida:** 4d6 de dano, e o usuário recupera Vida igual à metade do dano causado.
- **Crítico (20 natural):** dano máximo do dado + rolagem extra, e sobe 1 Intensidade

**Lamento dos Mortos**

*Um coro de vozes que já não têm dono ecoa no campo — e cada inimigo ouve o próprio fim se aproximando.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 6 casas | **Alvos:** 2 casas de raio do ponto
- **Intensidade I — ◈ (1 PA) + 3 Mana:** 1d6 de dano em cada alvo + cada um perde 1 no dano de ataques até o fim do próprio próximo turno.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** 1d6 de dano em cada alvo + perde 2 no dano de ataques, e rola o próximo teste de Vontade com Desvantagem.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** 1d6 de dano em cada alvo + perde 3 no dano de ataques, e cada alvo perde a próxima Reação.
- **Crítico (20 natural):** dano máximo (6) + 1d6 extra em todos, e sobe 1 Intensidade

**Colheita**

*Quanto mais perto da morte, mais fácil é para a foice terminar o trabalho.*

- **Chave:** [Necromancia](../docs/glossario.md#necromancia)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alvos:** 1 criatura, corpo a corpo
- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d8 de dano; se isso deixar o alvo com menos da metade da Vida máxima, o usuário recupera 1d4 de Mana.
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d8 de dano, com +1d8 extra se o alvo já estiver com menos da metade da Vida máxima; o usuário recupera 1d4 de Mana se isso acontecer.
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 1d8 de dano, com +2d8 extra se o alvo já estiver com menos da metade da Vida máxima; o usuário recupera 2d4 de Mana se isso acontecer.
- **Crítico (20 natural):** dano máximo (8) + 1d8 extra, e sobe 1 Intensidade

---

## Projeção Mental — habilidades propostas

*Grupo existente: só Repouso Forçado. As sete abaixo cobrem medo, confusão, leitura de
pensamento, ilusão sensorial, dano psíquico puro, telepatia utilitária e um controle de área —
todas contra Defesa mental (Vontade) quando rolam ataque, seguindo o padrão que Repouso Forçado
já estabeleceu.*

**Medo Puro**

*O terror não precisa de motivo — só precisa de um segundo dentro da mente do alvo.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Atributo:** Inteligência | **Defesa:** mental (Vontade) | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 3 Mana:** 1d6 de dano + no início do próprio turno, o alvo deve se afastar do usuário usando o Movimento dele, se puder.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** 1d6 de dano + o mesmo, e enquanto durar (2 rodadas) o alvo rola com Desvantagem contra o usuário.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** 1d6 de dano + por 2 rodadas, o alvo não pode se aproximar nem atacar o usuário.
- **Crítico (20 natural):** dano máximo (6) + 1d6 extra, e sobe 1 Intensidade

**Ruído Branco**

*Pensamentos que não são seus se misturam aos que são — e por um instante, não dá pra saber qual comando obedecer.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Atributo:** Inteligência | **Defesa:** mental (Vontade) | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 3 Mana:** 1d6 de dano + o próximo ataque do alvo até o fim do turno dele rola com Desvantagem.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** 1d6 de dano + Desvantagem em todos os ataques do alvo até o fim do próprio próximo turno.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** 1d6 de dano + Desvantagem em todos os ataques do alvo até o fim do próprio próximo turno, e há 50% de chance (o Mestre rola) dele atacar a criatura mais próxima — aliada ou não — em vez do alvo pretendido.
- **Crítico (20 natural):** dano máximo (6) + 1d6 extra, e sobe 1 Intensidade

**Ler a Superfície**

*Não é preciso invadir — só ouvir o que já está gritando por dentro.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Custo fixo:** ◈ (1 PA) + 4 Mana | **Atributo:** Inteligência | **Defesa:** mental (Vontade) | **Alcance:** 6 casas | **Alvos:** 1 criatura
- **Efeito:** role d20 + Inteligência contra a Defesa mental do alvo. Passando, o usuário lê o pensamento mais superficial e presente na mente dele agora — a intenção do próximo turno, uma mentira prestes a ser dita, o nome de quem ele mais teme. O Mestre decide o que é relevante ali; não funciona em mentes protegidas ou não-conscientes.
- *(Sem Intensidade — habilidade de detecção, escala só no que é revelado, a critério do Mestre)*

**Miragem**

*Os olhos veem o que a mente projeta — e a mente, nesse instante, não é mais sua.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Atributo:** Inteligência | **Alcance:** 8 casas | **Alvos:** 2 casas de raio do ponto
- **Intensidade I — ◈ (1 PA) + 3 Mana:** por 1 rodada, cria uma ilusão visual ou sonora simples (uma forma, um som) na área — não interage fisicamente com nada, mas engana quem não investigar de perto.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** por 2 rodadas, a ilusão pode se mover e imitar uma criatura ou efeito conhecido (um aliado, uma explosão, um grito); quem agir contra ela perde a ação, sem efeito real.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** por 3 rodadas, a ilusão engana também o toque (parece sólida ao contato) — só um teste ativo de investigação, a critério do Mestre, revela a farsa.
- *(Sem Crítico — não há rolagem de ataque nesta habilidade; é ilusão, não dano)*

**Grito Silencioso**

*Não sai som nenhum — mas do lado de dentro, ainda assim, dói.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Atributo:** Inteligência | **Defesa:** mental (Vontade) | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d8 de dano.
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d8 de dano, e o alvo perde 2 Mana.
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 1d8 de dano, e o alvo perde 4 Mana e rola o próximo teste de Vontade com Desvantagem.
- **Crítico (20 natural):** dano máximo (8) + 1d8 extra, e sobe 1 Intensidade

**Voz Sem Boca**

*A frase chega direto onde precisa chegar — nenhum ouvido no meio do caminho a intercepta.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Custo fixo:** ◈ (1 PA) + 2 Mana | **Atributo:** Inteligência | **Alcance:** 12 casas | **Alvos:** até 5 aliados conhecidos pelo usuário
- **Efeito:** por até 10 minutos, o usuário e os alvos compartilham um canal telepático — podem se comunicar (palavras, imagens simples) enquanto estiverem dentro do alcance, mesmo sem se ver ou ouvir.
- *(Sem Intensidade — habilidade utilitária, sem teste de ataque)*

**Colapso Mental**

*Todo mundo na área ouve, ao mesmo tempo, o próprio medo mais fundo — e não tem como não reagir.*

- **Chave:** [Projeção Mental](../docs/glossario.md#projecao-mental)
- **Custo fixo:** ◈◈ (2 PA) + 9 Mana | **Atributo:** Inteligência | **Defesa:** mental (Vontade) | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 3 casas de raio do ponto
- **Acerto:** 1d8 de dano + cada alvo não pode usar Habilidades (só Movimento, Ataque Básico e Reação) até o fim do próprio próximo turno.
- **Crítico (20 natural):** dano máximo (8) + 1d8 extra em todos
- *(Custo fixo — área de 3 casas de raio, rola teste de ataque contra a Defesa mental de cada alvo)*

---

## Alquimia de Mana — habilidades propostas

*Grupo existente: Corpo Fortalecido, Fúria da Arma. As sete abaixo cobrem transmutar terreno,
reforçar/criar objeto, imbuir arma com elemento temporário (justificado por reação química, não
fé), antídoto químico, e uma habilidade de corrosão que dissolve qualquer material — de
armadura a muralha.*

**Terra Que Cede**

*A pedra lembra que já foi lama — e por quanto tempo ela esquece de novo é você quem decide.*

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Inteligência | **Alcance:** 8 casas | **Alvos:** 2 casas de raio do ponto
- **Intensidade I — ◈ (1 PA) + 3 Mana:** o chão da área vira [Terreno Difícil](../docs/glossario.md#terreno-dificil) (ou deixa de ser, se já era) — lama, gelo liso, pedra firme, à escolha do usuário — por 2 rodadas.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** o mesmo, durando até o fim da [cena](../docs/glossario.md#cena).
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** o mesmo, **permanente** — só volta ao normal se outro efeito (ou o próprio usuário, reaplicando esta habilidade) desfizer.
- *(Sem Crítico — não há rolagem de ataque nesta habilidade)*

**Enrijecer**

*O metal amassado se realinha sozinho — não fica bonito, mas aguenta o próximo golpe. Na pele
de quem carrega o dom, o mesmo princípio vira couraça viva: pedra, aço, casca de árvore, o que
for preciso.*

⚠ **Ampliada (2026-08-15):** a pedido do autor, deixou de valer só em objeto/estrutura — agora
também funciona em criaturas (pele de pedra, pele de metal), proativa, sem virar Reação.

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Inteligência | **Alcance:** 3 casas | **Alvos:** 1 criatura (pode ser o próprio
  usuário), ou 1 objeto/estrutura (porta, escudo, ponte)
- **Intensidade I — ◈ (1 PA) + 3 Mana:** se o alvo for uma criatura, ela ganha um
  [Escudo](../docs/glossario.md#escudo) de 1d8 pontos e Resistência a um tipo de dano físico à
  escolha, por 3 rodadas. Se for um objeto/estrutura, ganha 1d8 pontos de Vida temporária (se
  não tiver Vida definida, o Mestre atribui uma) e a mesma Resistência.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** o mesmo, com 2d8 pontos e Resistência a dois tipos.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** o mesmo, com 3d8 pontos e Imunidade a um tipo de
  dano físico à escolha.
- *(Sem Crítico — não há rolagem de ataque nesta habilidade)*

**Reagente de Combate**

*Um frasco se quebra contra a lâmina — por um instante, a arma não é só metal.*

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Inteligência | **Alvos:** o próprio usuário
- **Elemento:** ao ativar, o usuário escolhe Fogo, Gelo, Raio ou Veneno — a condição aplicada muda de acordo
- **Intensidade I — ◈ (1 PA) + 5 Mana:** por 2 rodadas, os ataques do usuário que causarem dano também aplicam a condição do elemento escolhido (Fogo → [Queimando](../docs/glossario.md#queimando) 1d4; Gelo → [Lento](../docs/glossario.md#lento); Raio → perde a próxima Reação; Veneno → [Envenenado](../docs/glossario.md#envenenado), 1 acúmulo) — não empilha num mesmo alvo.
- **Intensidade II — ◈◈ (2 PA) + 8 Mana:** por 3 rodadas, o mesmo, com a versão mais forte da condição (Fogo → Queimando 2d4; Gelo → [Imóvel](../docs/glossario.md#imovel); Raio → perde Ação Básica e Reação; Veneno → Envenenado, 2 acúmulos).
- **Intensidade III — ◈◈◈ (3 PA) + 11 Mana:** por 4 rodadas, o mesmo que a Intensidade II.
- *(Sem Crítico — o efeito já é a condição em si, não um dano bônus)*

**Frasco de Emergência**

*Não é fé. É química — e cura o que reza nenhuma alcança.*

⚠ **Redesenhada (2026-08-15):** a versão original era uma cura genérica, só trocando Sabedoria
por Inteligência — o que banalizava `Cura` (Suporte) em vez de trazer identidade própria. Agora
o foco é **antídoto**, com um efeito de Vida bem menor que o de uma habilidade de cura de
verdade.

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Inteligência | **Alvos:** 1 criatura (pode ser o próprio usuário)
- **Intensidade I — ◈ (1 PA) + 4 Mana:** remove 1 acúmulo de [Envenenado](../docs/glossario.md#envenenado) do alvo (ou uma condição equivalente de origem química/toxina, a critério do Mestre), e ele recupera 1d4 de Vida.
- **Intensidade II — ◈◈ (2 PA) + 7 Mana:** remove todos os acúmulos de Envenenado do alvo, e ele recupera 2d4 de Vida.
- **Intensidade III — ◈◈◈ (3 PA) + 10 Mana:** remove Envenenado e qualquer outra condição prejudicial de origem não-mágica (toxina, doença, veneno de item) do alvo, e ele recupera 3d4 de Vida.
- *(Sem Crítico — habilidade de cura, sem teste de ataque)*

**Bolso de Reagentes**

*Um punhado de pó vira exatamente a ferramenta que a situação pede — mesmo no meio da briga.*

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Custo fixo:** ◈ (1 PA) + 6 Mana | **Atributo:** Inteligência | **Alvos:** o próprio usuário
- **Efeito:** cria um item mundano simples e não-mágico (uma corda, uma tocha, um jogo de picaretas, um ácido fraco pra corroer uma fechadura) — o Mestre decide o que é razoável. Pode ser usada dentro ou fora de combate, sem limite de [descansos](../docs/jogar/exploracao.md#descanso).
- *(Sem Intensidade — habilidade utilitária, sem teste de ataque)*

**Casca Reativa** *(usada como Reação)*

*No instante do impacto, a pele endurece e corrói — o golpe machuca os dois lados.*

⚠ **Ajustada (2026-08-15):** o autor perguntou o diferencial em relação a `Escudo Mágico`
(Buff) — e decidiu que `Escudo Mágico` também deveria virar Reação (ver proposta de mudança
nele, junto desta revisão). Com os dois reativos agora, o diferencial passa a ser **quem
protege, contra o quê, e como**: **Escudo Mágico** pode proteger **um aliado a distância**
(inclusive à distância, não só o próprio usuário), contra **qualquer** tipo de ataque, criando
um Escudo (pool de absorção). **Casca Reativa** só protege **o próprio usuário**, só contra
ataques **físicos**, e nunca vira pool — **é sempre retaliação desde a Intensidade I**, reduz
**e devolve** dano no mesmo instante. Força continua sendo o atributo (o corpo do próprio
usuário reagindo), contra Inteligência de Escudo Mágico (uma barreira conjurada à parte do
corpo, capaz de alcançar outro alvo).

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Força | **Dano:** Arcano | **Alvos:** o próprio usuário
- *(Dedicada a Reação — sempre 0 PA; a Intensidade escolhe só quanto Mana gastar)*
- **Intensidade I — 0 PA + 3 Mana:** quando for alvo de um ataque físico, o usuário pode usar esta habilidade como Reação pra reduzir o dano daquele ataque em 1d6 (mínimo 1), e o atacante corpo a corpo sofre 1d4 de dano automático de volta.
- **Intensidade II — 0 PA + 6 Mana:** o mesmo, reduzindo em 2d6, e o atacante sofre 1d6 de volta.
- **Intensidade III — 0 PA + 9 Mana:** o mesmo, reduzindo em 3d6, e o atacante sofre 2d6 de volta.

**Corrosão**

*Nada resiste por muito tempo — pedra, ferro ou carne, tudo cede à mesma química.*

⚠ **Reescrita por inteiro (2026-08-15).** A versão original ("Ferrugem Instantânea") só afetava
armas metálicas e não deixava claro se o dano era no item ou na criatura — confuso, e pequeno
demais pra fantasia de "alguém que dissolve matéria". Agora é uma habilidade de corrosão de
verdade: funciona em **qualquer material** (madeira, pedra, metal, carne) e pode mirar uma
criatura (dano + corrói o que ela veste/empunha) **ou** um objeto/estrutura sem vida (dissolve
o material de verdade — o suficiente pra abrir brecha numa muralha ou furar um casco, na
Intensidade certa). Seguindo a orientação do autor: a fantasia vem primeiro, o Mana é o que
segura o equilíbrio — não o escopo do que a habilidade pode fazer.

- **Chave:** [Alquimia de Mana](../docs/glossario.md#alquimia-de-mana)
- **Atributo:** Inteligência | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura,
  ou 1 objeto/estrutura sem vida à escolha do usuário

**Contra uma criatura** (rola teste de ataque contra a Defesa física dela):

- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d6 de dano + a armadura e a arma empunhadas pelo alvo
  perdem eficácia até o fim do próprio próximo turno dele: ele perde 2 de Defesa, e o dano dos
  ataques dele cai em 1.
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d8 de dano + o mesmo, por 2 rodadas, com -3 de
  Defesa e -2 no dano de ataques.
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 2d6 de dano + o mesmo, por 3 rodadas, com -4 de
  Defesa e -3 no dano de ataques; se o item empunhado pelo alvo já for frágil ou de baixa
  qualidade, o Mestre pode declará-lo destruído de vez.
- **Crítico (20 natural):** dano máximo do dado + rolagem extra, e sobe 1 Intensidade

**Contra um objeto ou estrutura sem vida** (sem teste de ataque — a corrosão dissolve o
material, seja madeira, pedra, metal ou qualquer outro):

- **Intensidade I:** dissolve uma seção pequena — o suficiente pra destravar uma fechadura,
  cortar uma corrente, abrir um buraco do tamanho de uma mão.
- **Intensidade II:** dissolve uma seção do tamanho de uma porta — o suficiente pra uma pessoa
  passar, ou furar um casco abaixo da linha d'água.
- **Intensidade III:** dissolve uma seção grande — o suficiente pra abrir uma brecha numa
  muralha, derrubar uma coluna estrutural, afundar um barco pequeno. O Mestre define o limite
  exato caso a caso (uma muralha de fortaleza não cai inteira, mas uma seção dela sim).

---

## Percepção Arcana — habilidades propostas

*Grupo existente: Ver Espíritos, Olhar Que Enxerga o Encanto — ambas detecção de custo fixo, sem
Intensidade. As sete abaixo mantêm esse tom (a maioria são detecção pura) e acrescentam as duas
formas de premonição em combate pedidas: Vantagem em Iniciativa e Vantagem no próximo ataque.*

**Segunda Visão**

*A verdade tem um brilho diferente — e a mentira, um tremor que ninguém mais nota.*

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Custo fixo:** ◈ (1 PA) + 3 Mana | **Atributo:** Sabedoria | **Alvos:** o próprio usuário
- **Efeito:** até o fim da [cena](../docs/glossario.md#cena), o usuário enxerga armadilhas escondidas (mágicas ou mecânicas) a até 6 casas, e sabe quando alguém que ele consegue ver está mentindo deliberadamente — não sabe a verdade, só que a fala não é sincera.
- *(Sem Intensidade — habilidade de detecção, sem teste de ataque)*

**Vislumbre**

*A pedra não esconde nada de quem sabe olhar pelo resíduo que a vida deixa nela.*

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Custo fixo:** ◈ (1 PA) + 4 Mana | **Atributo:** Sabedoria | **Alcance:** 10 casas | **Alvos:** um ponto que o usuário conheça ou consiga apontar
- **Efeito:** por um instante, o usuário enxerga através de até 2 obstáculos sólidos (paredes, portas, o chão de cima) na direção apontada — o suficiente pra saber o que tem do outro lado antes de abrir a porta. Não dura além do próprio turno do usuário.
- *(Sem Intensidade — habilidade de detecção, sem teste de ataque)*

**Instinto de Combate**

*Antes do primeiro golpe, o corpo já sabe o que vai acontecer.*

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Custo fixo:** ◈ (1 PA) + 3 Mana | **Atributo:** Sabedoria | **Alvos:** o próprio usuário
- **Efeito:** só pode ser usada antes da rolagem de Iniciativa (quando o usuário sabe que o combate está prestes a começar). O usuário rola Iniciativa com [Vantagem](../docs/glossario.md#vantagem).
- *(Sem Intensidade — habilidade utilitária, sem teste de ataque)*

**Fenda no Instante**

*Um piscar de olhos mostra o golpe antes dele acontecer — tempo o bastante pra garantir que ele não erre.*

⚠ **Redesenhada pela terceira vez (2026-08-15).** As duas correções anteriores resolveram o
problema de *True Strike*, mas a segunda ("o usuário ataca agora, garantido") perdeu a fantasia
de **premonição** — virou só um ataque melhor, não uma visão do futuro. A pedido do autor, a
habilidade deixa de ser um ataque do próprio usuário e vira o que ela sempre devia ser: o
usuário enxerga o instante à frente e **entrega essa certeza pra quem vai desferir o golpe** —
ele mesmo, ou um aliado. O próximo ataque de quem recebe a visão acerta sozinho.

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Atributo:** Sabedoria | **Alcance:** 8 casas | **Alvos:** o próprio usuário, ou 1 aliado
- **Intensidade I — ◈ (1 PA) + 4 Mana:** o usuário mostra o instante à frente pro alvo — até o fim do próprio próximo turno do alvo, o **próximo ataque** que o alvo fizer **acerta automaticamente**, sem rolar contra a Defesa do inimigo.
- **Intensidade II — ◈◈ (2 PA) + 7 Mana:** o mesmo, e esse ataque causa **+1d6 de dano extra**.
- **Intensidade III — ◈◈◈ (3 PA) + 10 Mana:** o mesmo, e esse ataque conta como um **Crítico** — dano máximo do dado da arma + uma rolagem extra —, como se tivesse saído 20 natural.
- *(Sem teste de ataque nesta habilidade — ela só garante o próximo ataque do alvo, não ataca por si mesma)*

**Rastro Arcano**

*Toda magia deixa marca — e a marca não sabe se esconder de quem procura por ela.*

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Custo fixo:** ◈ (1 PA) + 4 Mana | **Atributo:** Sabedoria | **Alvos:** 1 criatura que o usuário já tenha visto usar uma habilidade nas últimas 24 horas
- **Efeito:** o usuário sente a direção geral (não a distância exata) de onde essa criatura está agora, desde que ela tenha usado Mana em algum momento das últimas 24 horas. Não funciona em criaturas sem Mana. Só pode ser usada uma vez por [descanso curto](../docs/jogar/exploracao.md#descanso) sobre o mesmo alvo.
- *(Sem Intensidade — habilidade de detecção, sem teste de ataque)*

**Olho que Não Pisca**

*Disfarce, ilusão, invisibilidade — pra esse olhar, é tudo a mesma coisa: transparente.*

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Custo fixo:** ◈ (1 PA) + 3 Mana | **Atributo:** Sabedoria | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Efeito:** por 2 rodadas, o usuário enxerga a forma verdadeira do alvo através de disfarce, ilusão, transformação ou invisibilidade, e sabe quais efeitos benéficos ativos (buffs) ele carrega no momento.
- *(Sem Intensidade — habilidade de detecção, sem teste de ataque)*

**Aviso Silencioso** *(usada como Reação)*

*Um segundo antes do golpe, algo dentro avisa — e o golpe, sem saber por quê, erra o alvo.*

⚠ **Redesenhada (2026-08-15):** a versão original era só mais uma Reação de +Defesa
(`Defesa Mágica` e `Aparar`, em Buff, já cobrem exatamente isso). O autor pediu algo mais
parecido com divinação — em vez de o usuário ficar mais difícil de acertar, o presságio faz a
própria sorte do atacante falhar. É a primeira Reação do jogo que impõe Desvantagem no ataque
de quem mira o usuário, em vez de subir a Defesa dele.

- **Chave:** [Percepção Arcana](../docs/glossario.md#percepcao-arcana)
- **Atributo:** Sabedoria | **Alvos:** o próprio usuário
- *(Dedicada a Reação — sempre 0 PA; a Intensidade escolhe só quanto Mana gastar)*
- **Intensidade I — 0 PA + 3 Mana:** quando for alvo de um ataque, o usuário pode usar esta habilidade como Reação pra forçar o atacante a rolar o teste com [Desvantagem](../docs/glossario.md#desvantagem), antes do resultado ser conhecido.
- **Intensidade II — 0 PA + 6 Mana:** o mesmo, e se o ataque ainda assim acertar, reduz o dano recebido em 1d6 (mínimo 1).
- **Intensidade III — 0 PA + 9 Mana:** o mesmo, reduzindo em 2d6; se o ataque errar mesmo assim, o usuário identifica exatamente de onde ele veio, mesmo se estivesse escondido.

---

## Notas de revisão pro autor

- Todos os custos em Mana seguem a escala já documentada em `docs/jogar/mana.md`
  (habilidades gerais: 1/3/6 padrão, ou passos de +3 quando mais fortes; Custo fixo cobra o
  valor da Intensidade III da escala equivalente).
- Nenhuma condição nova foi inventada — tudo reaproveita o glossário existente (Sangrando,
  Queimando, Lento, Imóvel, Envenenado, Marcado, Atordoado, Vantagem, Desvantagem, Terreno
  Difícil, Escudo, Resistência, Imunidade).
- **Levante Breve** (Necromancia) é a única que pede atenção extra: ela cria um precedente —
  "erguer temporariamente o corpo de um aliado morto, sem reviver o aliado" — que não existe
  ainda no jogo. Vale confirmar o tom com o autor antes de aprovar.
- Ao copiar pra `docs/habilidades/*.md`, ajustar os links relativos: aqui eles apontam pra
  `../docs/...` (porque este arquivo vive em `notas/`); nos arquivos de grupo reais, o padrão é
  `../glossario.md#termo` e `../jogar/....md#termo`, sem o prefixo `docs/`.
