# Arquitetura — Conjuração de Pacto (sistema completo de invocação/vínculo)

Rascunho de trabalho, não aprovado. Nada aqui deve ser copiado pra `docs/` sem revisão do
autor. Este documento é **arquitetura**, não habilidades prontas — ele decide como cada peça
funciona mecanicamente antes de qualquer habilidade de Conjuração de Pacto ser escrita.

**Como este arquivo se relaciona com o anterior:** `notas/proposta-invocacao-e-habilidades-novas.md`
continua valendo — as 28 habilidades de Necromancia, Projeção Mental, Alquimia de Mana e
Percepção Arcana propostas lá não mudam. A seção "Conjuração de Pacto — opções mecânicas"
daquele arquivo analisava só uma habilidade solta (três caminhos: A, B, C) e ficou obsoleta:
numa conversa falada, o autor revelou que quer uma **família inteira de mecânicas de
invocação**, não uma habilidade só — no espírito de como D&D 5e tem *Find Familiar*,
*Conjure Animals*, *Conjure Elemental* e *Planar Binding* como coisas distintas dentro do
mesmo tema. Este arquivo substitui aquela seção.

O **Caminho B** do rascunho anterior (ficha própria + turno próprio na Iniciativa) é a base
da peça 2 abaixo (**Aliado de Combate**) — o autor confirmou gostar dessa direção antes de
pedir o escopo maior.

## O princípio que organiza tudo

**Convocação não pode ser descartável.** É a instrução mais enfática que o autor deu, com uma
referência específica: o vínculo dono-de-pet em anime, onde a criatura protege o personagem
*porque é forte o bastante pra isso*, e a morte dela pesa de verdade — não é um botão de reset
pra chamar outra igual no turno seguinte.

Isso não significa que toda peça pesa igual. O autor já decidiu que **o peso escala com o
tier**: quanto mais barata/frequente a invocação, mais leve a consequência da morte; quanto
mais rara/cara, mais permanente. As sete peças abaixo (cinco seções, com duas fusões) formam
essa escada, do mais leve pro mais pesado:

```
Familiar Simples  →  Aliado de Combate (menor → médio → maior)  →  Companheiro Animal  →  Vínculo com Ser Maior
     peso baixo              peso baixo (as três)                    peso próprio           peso alto
```

O Companheiro Animal não entra nessa escada de forma limpa — ver seção 4, é onde mora a
tensão que o autor levantou e que precisa de uma regra própria.

---

## 1. Familiar Simples

**Como funciona.** Um bichinho, espírito menor ou construto miniatura que acompanha o
personagem — corvo, gato, chama-fada, boneco de argila do tamanho de uma mão. Ele **não é uma
peça de combate**: não tem ataque relevante, não muda o resultado de uma luta. O valor dele é
utilitário — carregar um item pequeno, espiar por uma fresta que o personagem não cabe, ler um
pergaminho à distância pelos olhos dele, dar Vantagem numa Percepção específica porque ele
avisou antes.

**Quem controla.** O jogador, sempre — é baixa complexidade, não compete com o próprio turno.

**Duração.** Permanente, como vínculo — existe entre sessões, do mesmo jeito que o Companheiro
Animal (seção 4), mas **sem crescer**. É a mesma criatura fraca do primeiro dia até o nível 20.
Isso é a diferença estrutural que justifica ele ser peça própria e não uma versão fraca do
Companheiro Animal: um cresce com o personagem, o outro não deveria — a fantasia do familiar
clássico é utilidade constante, não força.

**Ficha.** Mínima, mas existe — precisa ter Vida (baixa, ex: 1 a 3) e Defesa pra que a
possibilidade de "matarem o familiar do mago" seja real e conte como ameaça narrativa, sem
nunca ser uma ameaça de combate. Sem Ataque, ou um poke simbólico (1 de dano) só se o autor
quiser que ele possa participar de alguma forma. Movimento normalmente alto ou com um traço de
deslocamento incomum (voar, nadar, entrar em frestas) — é isso que faz o utilitário valer a
pena.

**Custo.** Habilidade geral, Grau **Menor** (1–3 Mana), Custo fixo, sem Intensidade — é
utilitário, não tem o que graduar. Barato o bastante pra não pesar no orçamento do dia, o que é
o próprio pedido do autor ("sempre disponível").

**Consequência de morte.** A mais leve da escada: o familiar dissolve/foge e reaparece ao
próximo **descanso curto** (mais leve até que o descanso longo do Aliado médio, porque é a
peça de menor peso emocional da família inteira).

**Exemplos de nome/conceito:**
- *Olhos Emprestados* — um corvo que voa e mostra o que vê pela mente do usuário.
- *Chama de Bolso* — uma pequena chama-fada que ilumina, aquece e não se apaga no vento.

---

## 2. Aliado de Combate (menor / médio / maior)

**Como funciona.** A invocação vira um combatente de verdade: **ficha própria no molde do
Bestiário, rola a própria Iniciativa, age no próprio turno**. É a peça central do sistema — a
fantasia de "chamar algo que luta ao seu lado", em três degraus de força.

### Por que três tiers, e por que não são os Tiers do Bestiário

Comum/Treinado/Formidável/Lendário foram calibrados pra **ameaça de Mestre** — quanto uma
criatura aguenta contra um grupo de 4 personagens. Um Aliado de Combate é o oposto: é **força
de PJ**, comprada com o próprio Mana e PA do personagem, lutando ao lado do grupo, não contra
ele. Usar a régua do Bestiário direto criaria o problema que o rascunho anterior identificou no
Caminho B: um Treinado tem a força de combate de um personagem inteiro, e invocá-lo em nível 1
efetivamente dobra o grupo por uma cena.

Por isso, escala própria — **menor, médio, maior** — ancorada nas proporções do Bestiário mas
deliberadamente mais fraca em cada degrau, porque este é o Mana do *jogador* comprando um
segundo corpo, não o Mestre montando um encontro:

| Tier | Vida | PA | Ataque | Dano | Defesa física | Ancoragem |
|---|---|---|---|---|---|---|
| **Menor** | 6 | ◈ (1) | +1 | 1d4 | 7 | mais fraco que Comum (Comum: Vida 8, PA 2) |
| **Médio** | 10 | ◈◈ (2) | +2 | 1d6 | 9 | ~ Comum (Vida 8, PA 2, dano 1d4–1d6) |
| **Maior** | 22 | ◈◈◈ (3) | +3 | 1d8 | 11 | ~ Treinado (Vida 25, PA 3, dano 1d8) |

⚠ Números de trabalho, não finais — servem pra mostrar a proporção (cada degrau
aproximadamente dobra o anterior), o autor deve ajustar como achar melhor.

### Quem controla — o critério

O autor pediu que o controle varie por habilidade, com critério explícito. Proposto:

- **Menor e Médio: o jogador controla diretamente.** Ficha simples (1–2 PA, um único ataque,
  sem lista de opções), roda junto do próprio turno sem atrasar a mesa — o mesmo motivo que já
  faz Comum e Treinado terem ataques de custo fixo em vez de Intensidade no Bestiário
  (`criando-criaturas.md`, "Ataques: capangas são fixos, chefes decidem").
- **Maior: o Mestre controla como NPC aliado.** Na força de um Treinado, com decisões táticas
  reais (quando avançar, quando seria melhor recuar) — pedir ao jogador rodar essa ficha *e* a
  própria no mesmo turno é o problema de sobrecarga que o autor já havia citado.
- **Qualquer habilidade que invoque mais de uma criatura ao mesmo tempo — Mestre controla,
  independente do tier.** Duas fichas simultâneas é o mesmo problema de sobrecarga mesmo se
  cada uma for Menor. Isso deixa espaço pra uma futura habilidade tipo "invoca uma pequena
  matilha" sem quebrar o critério.

### Duração e custo

Diferente de Vínculo Selvagem (que persiste até o próximo descanso longo), o Aliado de Combate
é pensado pra durar **a cena/o combate**, porque agora tem turno próprio e é isso que o
diferencia de uma invocação passiva:

| Tier | Duração | Custo (Intensidade) | Grau de Poder |
|---|---|---|---|
| **Menor** | 2 → 3 → 4 rodadas | ◈+3 / ◈◈+6 / ◈◈◈+9 Mana | Moderado |
| **Médio** | 3 → 4 → 5 rodadas | ◈+5 / ◈◈+9 / ◈◈◈+13 Mana | Maior |
| **Maior** | até o fim da cena | Custo fixo: ◈◈◈ + 18 Mana, **1x por descanso longo** | Supremo |

O Maior segue a recomendação que o próprio rascunho anterior já apontava: é onde esse caminho
fica defensável — caro, raro, declaradamente 1x por descanso, o Mestre sabe que só acontece uma
vez de verdade por sessão.

**Peso de mesa.** É o mais caro dos três em atenção — mais um turno pra resolver a cada rodada,
inclusive concorrendo com o limite de 8 criaturas em cena (`encontros.md`) quando o Mestre já
tem NPCs/monstros próprios rodando.

**Consequência de morte.** Todos os três tiers seguem o **peso baixo** que o autor já
especificou pro "Aliado de Combate médio": foge/some e volta a existir no próximo **descanso
longo**. Isso inclui o Maior — ver a seção de Decisões de Interpretação sobre se isso é
adequado dado que ele já é Suprema/1x por descanso (talvez mereça algo intermediário).

**Exemplos de nome/conceito:**
- **Menor** — *Servo de Cinzas*: um pequeno construto de brasa que ataca corpo a corpo.
- **Médio** — *Chamar Lâmina Espectral*: uma arma senciente que luta sozinha por conta própria.
- **Maior** — *Convocar Guardião do Pacto*: um espírito guerreiro na força de um combatente
  treinado, só nas horas mais difíceis.

---

## 3. Vínculo com Ser Maior (Binding / Prender-Vincular ao Serviço)

**Nota de fusão** ⚠ — o autor mencionou esta peça duas vezes na conversa, com nomes
ligeiramente diferentes: uma vez como "Binding" (o termo de D&D, convocar algo tipo um demônio
maior ou um Deva) e outra como "prender/vincular um ser ao seu serviço". Este documento trata
as duas como **a mesma peça de sistema** — ritual raro, de risco real, que resulta num Ser
poderoso ligado ao conjurador. A justificativa: mecanicamente as duas descrições pedem a mesma
coisa (um ritual de alto risco que cria um vínculo de serviço com uma entidade poderosa) e não
há, no que foi dito, nenhuma diferença de escopo entre "vincular" e "prender ao serviço" — só
vocabulário diferente pro mesmo ato. **Se o autor quis dizer duas coisas distintas** (por
exemplo: Binding é convocar/negociar com algo já disposto a um pacto, e "prender" é subjugar à
força algo que resiste), esta seção precisa virar duas, e a diferença mecânica mais óbvia seria
o risco de instabilidade ser maior em "prender à força" do que em "negociar vínculo". Fica
marcado aqui pra confirmação.

**Como funciona.** Um ritual — não uma habilidade de combate, não algo que se ativa no meio de
um turno. Convoca uma entidade poderosa (um demônio maior, um Deva, um espírito ancestral) e
tenta prendê-la a um vínculo de serviço. O risco é real: o ritual pode dar errado de um jeito
que fere o próprio conjurador.

**Mecânica de risco — reaproveitando Ressuscitar.** Em vez de Intensidade, usa
[Tiers de Resultado](../docs/habilidades/regras.md#habilidades-com-tiers-de-resultado), o
mesmo padrão de `Ressuscitar`: o d20 decide o **resultado do ritual**, não a potência do Ser
vinculado.

| Total (d20 + Atributo) | Resultado |
|---|---|
| ≤ 10 | **Falha catastrófica** — o Ser se solta hostil, ou o vínculo se volta contra o próprio conjurador (ver consequência abaixo) |
| 11–16 | **Falha recuperável** — o ritual não prende nada, mas nada de ruim acontece; os componentes/o tempo investido se perdem, e pode tentar de novo depois |
| ≥ 17 | **Sucesso** — o vínculo se forma; o Ser passa a responder ao conjurador |
| 20 natural | **Sucesso amplo** — o vínculo se forma nas melhores condições possíveis (o Mestre decide o que isso significa: menos restrições, o Ser mais disposto) |

**A ficha do Ser vinculado não é fixa na habilidade — é montada pelo Mestre.** Um demônio maior
e um Deva têm fichas completamente diferentes; travar um stat block único na habilidade
impediria a variedade que a fantasia pede. Em vez disso, a habilidade **aponta pro andaime de
`criando-criaturas.md`**: o Mestre monta o Ser usando a Tabela de Construção, tipicamente no
Tier **Formidável** (ocasionalmente Lendário, pra pactos de campanha inteira) — o mesmo
princípio que `Levante Breve` já usa (reaproveitar a ficha existente em vez de inventar uma
nova estrutura).

**Quem controla.** O Mestre, como NPC aliado — na força de um Formidável/Lendário, é
tacitamente demais pra um jogador rodar junto da própria ficha, e narrativamente o Ser tem
vontade própria (é "vinculado", não "domesticado" — ele pode negociar, relutar, cobrar um
preço).

**Duração.** O vínculo em si é **permanente** (como uma relação, não como um efeito de cena) —
uma vez selado, existe entre sessões, como o Companheiro Animal. Mas **manifestar o Ser numa
cena** (trazê-lo pra lutar ao lado do conjurador) é um custo separado, ativado como uma
habilidade Suprema normal — o vínculo é a *relação*, a manifestação é o *uso* dela.

**Custo.** ⚠ Emenda (2026-08-15): o ritual e a manifestação viraram **uma única habilidade**,
não duas — exigir duas escolhas de nível separadas só pra acessar um vínculo pesava demais no
orçamento de habilidades da carreira. A habilidade tem duas partes internas (ritual, depois
convocação), com os custos abaixo cada uma:
- **O ritual em si:** fora de combate, exige tempo e lugar (não é algo que se faz num descanso
  qualquer — é raridade de campanha, não de sessão; ver Decisões de Interpretação). Custo fixo
  alto em Mana (Supremo, 20+) e provavelmente um custo narrativo/material que cabe ao Mestre
  definir cena a cena (um nome verdadeiro, um sacrifício, um lugar de poder).
- **Manifestar o Ser numa cena, já vinculado:** Custo fixo, ◈◈◈ + 18–24 Mana, 1x por descanso
  longo — no mesmo patamar do Aliado Maior, mas com uma ficha potencialmente mais forte
  (Formidável em vez de Treinado).

**Consequência de morte — aqui mora o peso alto que o autor pediu.** Diferente de todas as
outras peças, a morte do Ser vinculado **não** é "some e volta". Proposto: o vínculo se rompe
de vez — o Ser, se realmente destruído, não pode ser vinculado de novo (é uma entidade
específica, não uma categoria), e o conjurador sofre uma consequência real e permanente:

- Ganha uma **[Cicatriz](../docs/jogar/estresse.md#cicatrizes)** automaticamente (sem precisar
  encher a barra de Estresse primeiro) — o trauma de um vínculo cortado à força é, por
  definição, o tipo de evento que a Cicatriz já existe pra representar.
- Perde a habilidade de Conjuração de Pacto que criou aquele vínculo específico até formar um
  **novo** vínculo — o que significa refazer o ritual do zero, nos Tiers de Resultado, com o
  mesmo risco de falha catastrófica de antes.

Isso dá peso real (perda permanente + trauma mecânico) sem travar o personagem: ele pode
tentar de novo, mas paga caro e arrisca de novo.

**Exemplos de nome/conceito:**
- *Selar o Pacto* — o ritual em si; qualquer Ser, qualquer resultado da tabela.
- *Convocar o Vinculado* — manifestar o Ser já vinculado numa cena de combate.

---

## 4. Companheiro Animal

**Diferença estrutural que separa esta peça de todas as outras.** Toda outra habilidade do
jogo (inclusive as outras seis peças deste documento) escala pagando mais Mana numa Intensidade
maior, na hora de usar. O Companheiro Animal **não funciona assim** — ele escala com o
**nível do personagem** (`criacao/progressao.md`), é permanente, existe entre sessões, e cresce
sozinho junto com o dono, do mesmo jeito que Vida e Mana Máximo crescem sozinhos a cada nível
(`progressao.md`, "O que cresce sozinho").

O autor hesitou se isso é "magia" de verdade (a fantasia de laço com um animal não é
tipicamente arcana), mas decidiu manter dentro de Conjuração de Pacto por simplicidade — não
abrir um décimo primeiro grupo pra uma habilidade só.

### Relação com Vínculo Selvagem (já existe hoje, em Buff)

Vale registrar a sobreposição de fantasia: **Vínculo Selvagem** (`docs/habilidades/buff.md`)
já invoca um "companheiro animal" — mas escala por Intensidade/Mana (1d6→2d6→3d6), não por
nível, e some/volta no próximo descanso longo se o dono cair. Na prática, Vínculo Selvagem já
preenche o papel que o **Aliado de Combate Menor** (seção 2) preenche agora — é o Caminho A do
rascunho anterior, e coexiste sem conflito com esta peça nova, do mesmo jeito que D&D tem
*Find Familiar* (fraco, permanente, utilitário) e *Conjure Animals* (forte, temporário, pago em
slot) coexistindo sem se pisarem. O Companheiro Animal desta seção é o análogo ao companheiro
de Patrulheiro/Druida: **permanente, cresce com você, é a mesma criatura a campanha inteira.**
Fica como nota pro autor decidir se quer manter os dois nomes/conceitos numa mesma família ou
se prefere unificar depois.

### Progressão — ancorada em `progressao.md`

Como o Companheiro cresce sozinho junto com o dono (não é escolha de nível, é um efeito
contínuo de uma habilidade já aprendida), a progressão precisa de uma tabela própria, no
mesmo espírito da tabela **Vida por faixa de nível** que o Bestiário já usa pra escalar
criaturas por nível de grupo (`encontros.md`):

| Faixa de nível | Vida do Companheiro | Ataque | Dano | Defesa física |
|---|---|---|---|---|
| **1–4** | 12 | +2 | 1d6 | 9 |
| **5–10** | 30 | +4 | 2d6 | 12 |
| **11–15** | 55 | +6 | 3d6 | 16 |
| **16–20** | 85 | +8 | 4d6 | 19 |

⚠ Números de trabalho — a proporção segue a mesma curva de crescimento que
`encontros.md` usa pra "Vida por faixa" dos Tiers do Bestiário, escalada pra ficar sempre um
pouco abaixo de um Comum/Treinado equivalente da mesma faixa (o Companheiro **acompanha**, não
substitui o personagem).

**"Usa (ou reflete) os atributos do próprio personagem"** — o pedido do autor: proponho que o
**Ataque** do Companheiro some o mesmo atributo que o próprio personagem usaria pra uma
habilidade daquele estilo (ex: Sabedoria, se a build for de vínculo natural), em vez de ter um
atributo fixo e independente — assim o Companheiro melhora quando o jogador investe pontos de
nível par no atributo relevante, reforçando a sensação de que é uma extensão do personagem, não
uma ficha paralela.

**Quem controla.** O jogador — é a peça mais "sua" do sistema inteiro, deveria ser a mais fácil
de rodar, não a mais delegada.

**Custo.** Aprendida como qualquer habilidade — ocupa 1 das 10 escolhas de nível ímpar da
carreira. Sem Mana pra manter: como Vínculo Selvagem, ataca automaticamente no início do turno
do dono, sem gastar PA nem Mana — é o "sempre com você" que justifica não competir por
orçamento diário.

### Consequência de morte — a regra própria que este pedido exige

Este é o ponto que o autor levantou como tensão sem resolver sozinho: o Companheiro Animal é,
na descrição dele, o *exemplo central* do peso emocional pedido — não uma fera descartável de
invocação de combate, é o pet que acompanha a campanha inteira. Se ele simplesmente "some e
volta no próximo descanso" como um Aliado médio genérico, isso não entrega o pedido. Se a
morte for permanente e sem chance nenhuma, é dura demais pra uma peça que o jogador não escolhe
recriar por vontade própria (diferente do Vínculo com Ser Maior, que é raro e caro por opção
do jogador desde o início).

⚠ **Proposta — nem tão leve quanto "some e volta", nem tão dura quanto "perda sem chance":**

1. **Ao cair a 0 de Vida, o Companheiro fica Caído — como um personagem, não como uma
   criatura comum.** Isso é uma exceção deliberada à regra padrão do Bestiário ("criatura a 0
   de Vida morre", `criando-criaturas.md`) — mas reaproveita a mecânica de
   [Chegando a 0 de Vida](../docs/jogar/dano-e-cura.md#chegando-a-0-de-vida) que os PJs já
   usam, em vez de inventar uma rolagem nova: rola contra a morte no início de cada turno dele,
   pode ser Estabilizado por um aliado adjacente, pode ser trazido de volta por cura.
2. **Se a rolagem de morte se esgota (ou ninguém consegue estabilizar/curar a tempo), a morte é
   real.** Nesse ponto ele não pode ser trazido de volta por Ressuscitar nem qualquer outra
   habilidade — não é o mesmo aliado revivido, é uma perda de verdade.
3. **Reconquistar o vínculo depois de uma perda real custa tempo narrativo, não só Mana.** O
   jogador pode formar um vínculo com um novo animal, mas isso não pode acontecer em cena — só
   fora de perigo, e só depois de pelo menos um descanso longo dedicado (mecânica e
   narrativamente) a esse processo, não um clique instantâneo no meio da masmorra. O novo
   Companheiro nasce nas estatísticas da faixa de nível atual (não é penalizado
   mecanicamente pro resto da campanha), mas o Mestre é incentivado a tratar a cena de vínculo
   como algo que pesa — não é "comprar outro igual".

Essa proposta dá ao Companheiro Animal uma janela de resgate real (ele pode ser salvo, como um
personagem) antes de a perda se tornar definitiva, e quando a perda acontece de verdade, o
custo é tempo e peso narrativo — não uma trava mecânica permanente.

**Exemplos de nome/conceito:**
- *Laço de Sangue e Pelo* — a habilidade que forma o vínculo inicial (a forma do animal é
  escolhida ao aprender, como em Vínculo Selvagem).
- *Ele Sente o Que Eu Sinto* — upgrade opcional que deixa dono e Companheiro compartilharem uma
  Reação por cena.

---

## 5. Companheiro Transformável

**Onde encaixa — decisão e justificativa.** O autor deixou em aberto se isso é um upgrade
dentro do Companheiro Animal ou do Aliado de Combate. Proponho **dentro do Companheiro
Animal**, não do Aliado de Combate, porque a transformação é sobre a **mesma criatura
persistente** ganhando uma segunda forma de combate — isso só faz sentido pra algo que tem
identidade contínua (nome, vínculo, progressão de nível) pra transformar. O Aliado de Combate é
efêmero por natureza (dura a cena, desaparece), então não há "a mesma criatura" pra ter duas
formas — cada invocação já é uma ficha nova.

**Como funciona.** O Companheiro tem uma **forma pequena** (o estado padrão — fraca, quase
utilitária, como um Familiar Simples: baixa Vida, sem ataque relevante, boa pra viajar
discretamente, dormir no colo, entrar onde o personagem não cabe) e uma **forma grande de
combate**, que usa a progressão por nível da seção 4 inteira.

**Ativar a transformação** é a própria habilidade — Intensidade normal (Mana + PA), like
qualquer Buff de transformação: paga-se pra transformar, o efeito dura até ser desfeito ou até
o fim da cena. Volta à forma pequena automaticamente ao fim do combate, sem custo.

**A camada de proteção extra que a forma dupla permite:** se o Companheiro chegar a 0 de Vida
**na forma grande**, em vez de entrar direto na sequência de "Caído" da seção 4, ele **reverte
pra forma pequena com 1 de Vida** — um buffer natural que a própria fantasia de transformação
já sugere (a forma de combate "quebra" antes do animal real ser ferido de morte). A sequência
de Caído/perda real da seção 4 só se aplica se ele for reduzido a 0 **também** na forma
pequena. Isso dá ao Companheiro Transformável uma resiliência extra que o justifica como
upgrade — não é só cosmético, é uma segunda camada de Vida efetiva.

**Custo.** A habilidade base (Companheiro Animal) continua sendo 1 escolha de nível. O
Transformável é aprendido depois, como uma **segunda** habilidade que faz upgrade da primeira —
no molde de como uma arma exige Básica → Avançada → Especial em ordem. Ativar a transformação
em cena custa Mana normal de Intensidade (a forma grande "dura mais" ou "briga melhor" em
Intensidades mais altas, escalando como qualquer Buff — ver
[Buffs, Suporte e Mobilidade também têm Intensidade](../docs/habilidades/regras.md#buffs-suporte-e-mobilidade-tambem-tem-intensidade)).

**Exemplos de nome/conceito:**
- *Forma Verdadeira* — a habilidade que desbloqueia a transformação (upgrade de Laço de Sangue
  e Pelo).
- *Fúria Desperta* — uma versão mais agressiva da transformação, com bônus de dano mas duração
  menor.

---

## 6. Banir

**Onde mora — decisão e justificativa.** Proponho o grupo **Debuff**, não dentro de Conjuração
de Pacto. Banir é fundamentalmente um efeito de controle **contra** uma criatura hostil
(expulsá-la de volta pro plano dela), o que combina com o escopo de Debuff
("Desvantagens para inimigos ou em testes") — o mesmo prédio onde já moram efeitos como
Esquife de Ossos e Garra Demoníaca, que também lidam com criaturas convocadas/mortas-vivas sem
serem parte de Conjuração de Pacto. Conjuração de Pacto, nesta arquitetura, é inteiramente
sobre o jogador **trazer aliados**; Banir é o inverso — negar a presença de uma criatura
inimiga —, e isso é o padrão que Debuff já cobre.

⚠ **A ressalva real: o sistema não tem hoje uma faceta "planar/invocado" no Bestiário.** As
facetas atuais são Tipo, Vulnerável a, Imune a e Faz o quê (`CLAUDE.md`, seção de facetas do
Bestiário) — nenhuma marca uma criatura como "invocada" ou "planar" de forma consultável. Banir
precisa de um critério claro de alvo válido. Proposto: a habilidade define o alvo por **fluff
narrativo declarado na ficha da criatura** (Elementais, Demônios como a Súcupo, mortos-vivos
erguidos por Necromancia, e qualquer Ser vinculado da seção 3) em vez de uma faceta nova — mas
se o Bestiário crescer nessa direção, uma faceta própria pode valer a pena depois.

**Como funciona.** Habilidade de ataque comum, testando contra a Defesa mental (é a vontade do
alvo de permanecer no plano, não o corpo dele, que está sendo desafiada) — segue o padrão de
Intensidade/Mana normal de Debuff:

| Intensidade | Efeito |
|---|---|
| I | dano + o alvo perde a próxima Reação (o vínculo dele com este plano treme) |
| II | dano + o alvo é **suprimido** por N rodadas — para de agir, mas não sai da cena |
| III | dano + o alvo é **expulso**: sai da cena de vez, de volta ao plano de origem |

**Consequência pro conjurador de Conjuração de Pacto.** Um Ser vinculado (seção 3) ou um Aliado
de Combate (seção 2) de um PJ **também pode ser alvo de Banir** vindo de um inimigo — é
simetria intencional, o mesmo risco que os PJs impõem a inimigos vale ao contrário. Isso não é
uma "morte" da criatura (ela só volta pro próprio plano), então não deveria disparar a
consequência de morte de nenhuma das peças — só interrompe a cena atual.

**Exemplos de nome/conceito:**
- *Selo de Exílio* — a versão padrão, dano + expulsão em Intensidade III.
- *Fechar a Porta* — versão de área, expulsa todas as criaturas convocadas/planares numa zona.

---

## Resumo — como as sete peças se encaixam

| Peça | Escala por | Ficha vem de | Controle | Duração | Peso da morte |
|---|---|---|---|---|---|
| **1. Familiar Simples** | Custo fixo (Menor) | ficha própria, mínima | Jogador | Permanente, sem crescer | Baixíssimo — volta no descanso curto |
| **2. Aliado Menor/Médio** | Intensidade | ficha própria por tier | Jogador | 2–5 rodadas | Baixo — volta no descanso longo |
| **2. Aliado Maior** | Custo fixo (Supremo) | ficha própria por tier | Mestre | Fim da cena | Baixo (proposto) — ver ⚠ abaixo |
| **3. Vínculo com Ser Maior** | Ritual (Tiers de Resultado) + Custo fixo (Supremo) | `criando-criaturas.md`, Formidável/Lendário | Mestre | Permanente (vínculo) / cena (manifestação) | **Alto** — Cicatriz + perda da habilidade até novo ritual |
| **4. Companheiro Animal** | Nível do personagem | tabela própria, ancorada em `progressao.md`/`encontros.md` | Jogador | Permanente | Próprio — Caído + janela de resgate + custo narrativo se morrer de vez |
| **5. Companheiro Transformável** | Nível (forma grande) + Intensidade (ativação) | upgrade da peça 4 | Jogador | Por cena (forma grande) | Herda da peça 4, com buffer de forma pequena |
| **6. Banir** | Intensidade | — (efeito, sem ficha própria) | — | Instantâneo/N rodadas | N/A (não é uma invocação do jogador) |

---

## Decisões de interpretação — resolvidas em conversa com o autor (2026-08-15)

Todas as 12 decisões abaixo foram revisadas e fechadas. Este documento passa a ser a base pra
escrever as habilidades de verdade.

1. **Fusão Binding + "prender/vincular ao serviço" (seção 3).** ✅ Mantém fundido — é a mesma
   peça, um ritual só, um risco de instabilidade só.
2. **Onde o Companheiro Transformável encaixa (seção 5).** ✅ Confirmado: upgrade do
   Companheiro Animal (peça 4), não do Aliado de Combate. Transformação pede identidade
   contínua, que só o Companheiro tem.
3. **Regra de consequência de morte do Companheiro Animal (seção 4).** ✅ Aceita como proposta:
   fica Caído como um PJ, com janela de resgate; perda real custa descanso longo + tempo
   narrativo pra reconquistar o vínculo.
4. **Escala dos tiers menor/médio/maior do Aliado de Combate (seção 2).** ✅ Proporção aceita
   (menor < Comum, médio ~ Comum, maior ~ Treinado) — os números exatos (Vida 6/10/22, PA
   1/2/3 etc.) são ajustáveis na hora de escrever as habilidades, não precisam de mais revisão
   de arquitetura.
5. **Critério de quem controla cada peça — jogador vs. Mestre.** ✅ Mudou do proposto: **o
   jogador escolhe na hora de invocar** se quer rodar ele mesmo ou deixar com o Mestre, em
   qualquer tier do Aliado de Combate — não é mais um corte fixo por tier.
6. **Consequência de morte do Aliado Maior.** ✅ Mantém igual ao Menor/Médio — some, volta no
   próximo descanso longo. A raridade já vem do 1x/descanso, sem precisar empilhar punição.
7. **Onde "Banir" mora (seção 6).** ✅ Confirmado em Debuff, pela simetria com o resto do grupo.
   O critério de alvo válido fica por fluff narrativo na ficha da criatura por enquanto (sem
   faceta "planar/invocado" nova no Bestiário agora) — e a simetria foi confirmada: um
   Aliado/Ser vinculado de um PJ também pode ser alvo de Banir vindo de um inimigo, sem contar
   como morte, só interrompendo a cena.
8. **Consequência da falha catastrófica do ritual de Vínculo com Ser Maior.** ✅ Mantém regra
   fixa: Cicatriz automática + perda da habilidade até novo ritual.
9. **Raridade temporal do ritual de Vínculo com Ser Maior.** ✅ Fica a critério do Mestre, sem
   regra rígida de tempo ou gate material formal — o Mestre decide quando a oportunidade de
   campanha aparece.
10. **O Companheiro Animal ocupa uma das 10 escolhas de habilidade da carreira, como qualquer
    outra.** ✅ Confirmado — é uma escolha de nível normal, mesma contagem de qualquer outra
    habilidade.
11. **Nome do grupo.** ✅ Muda de "Conjuração de Pacto" pra **"Conjuração"** — mais amplo,
    cobre o leque inteiro (familiar, aliado de combate, vínculo, companheiro) sem sugerir que é
    só sobre pactos/binding. Todas as referências neste documento a "Conjuração de Pacto"
    devem ser lidas como "Conjuração" ao migrar pra `docs/`.
12. **Sobreposição com Vínculo Selvagem (Buff).** ✅ Vínculo Selvagem se aposenta — a fantasia
    de companheiro animal passa a ser só o Companheiro Animal novo. Consequência de
    implementação: `Vínculo Selvagem` está referenciado em 3 trilhas de Pacote
    (`docs/pacotes/index.md`, níveis 3, 3 e 17) que vão precisar de substituto quando isso for
    escrito de verdade — provavelmente o próprio Companheiro Animal, onde o nível bater.
