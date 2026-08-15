# Habilidades de Conjuração — rascunho (não aprovado)

⚠ **Rascunho de trabalho, não aprovado.** Escrito a partir de
`notas/arquitetura-conjuracao-de-pacto.md` (as 12 decisões de interpretação fechadas com o
autor em 2026-08-15). Nada aqui deve ser copiado pra `docs/` sem revisão do autor — nomes,
números de Mana/PA, atributos escolhidos e principalmente o formato novo da Peça 4 são todos
abertos a mudança. As habilidades estão prontas pra copiar (formato final), não pra publicar
sem mais uma leitura.

**Convenção de atributo** (escolha minha, não estava na arquitetura): **Sabedoria** para os
vínculos com criatura viva/espiritual — Familiar, Aliado de Combate, Companheiro Animal — pelo
mesmo motivo que Vínculo Selvagem já usava Sabedoria; **Vontade** para Vínculo com Ser Maior e
para Banir, porque as duas são um teste de força de vontade (prender um Ser / expulsar algo).
Ver a lista completa de decisões próprias no fim do arquivo.

---

## 1. Familiar Simples

Custo fixo, Grau **Menor**, sem Intensidade — ver arquitetura, seção 1.

**Olhos Emprestados**

*Um corvo pousa no ombro, e o mundo que ele vê passa a ser visível também pelos olhos de quem
o convocou.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Sabedoria | **Alvos:** o próprio usuário (invoca o familiar)
- **Custo fixo:** ◈ (1 PA) + 2 Mana | **Grau de Poder:** Menor
- **Efeito:** invoca um corvo familiar — vínculo **permanente**, existe entre sessões, mas
  **não cresce** com o nível do usuário (é a mesma criatura fraca do primeiro dia ao vigésimo
  nível). Como ação livre, o usuário pode ver e ouvir através dos olhos do corvo enquanto ele
  estiver a até 20 casas de distância — nesse período, a própria percepção do usuário fica
  reduzida à do corvo. Se o corvo observar algo relevante antes de um teste (uma emboscada, uma
  porta trancada, uma pista), esse teste rola com [Vantagem](../docs/glossario.md#vantagem).
- **O familiar:** Vida 2, Defesa física 8, Movimento 12 casas (voando). Sem ataque relevante —
  não é peça de combate.
- **Consequência de morte:** se reduzido a 0 de Vida, o corvo se dissolve e reaparece no início
  do próximo [descanso curto](../docs/jogar/exploracao.md#descanso) do usuário.

**Chama de Bolso**

*Uma pequena chama-fada paira ao lado do ombro, iluminando o caminho e não se apagando nem no
vento mais forte.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Sabedoria | **Alvos:** o próprio usuário (invoca o familiar)
- **Custo fixo:** ◈ (1 PA) + 2 Mana | **Grau de Poder:** Menor
- **Efeito:** invoca uma chama-fada — vínculo **permanente**, existe entre sessões, **não
  cresce** com o nível do usuário. Ilumina 4 casas de raio (não se apaga com vento, chuva ou
  submersão breve) e aquece o suficiente pra afastar os efeitos de frio extremo de quem estiver
  a até 2 casas dela. Pode ser mandada entrar em frestas que o usuário não cabe.
- **O familiar:** Vida 1, Defesa física 8, Movimento 6 casas (flutuando). Sem ataque relevante.
- **Consequência de morte:** se reduzida a 0 de Vida (ou apagada por um efeito que anule fogo),
  a chama se dissolve e reaparece no início do próximo
  [descanso curto](../docs/jogar/exploracao.md#descanso) do usuário.

---

## 2. Aliado de Combate (Menor / Médio / Maior)

**Regra compartilhada — quem controla.** Decisão #5 da arquitetura: em **qualquer** tier, o
jogador escolhe **no momento de invocar** se ele mesmo roda a ficha do Aliado (junto do próprio
turno) ou se passa o controle pro Mestre, que passa a agir com ele como um NPC aliado. Não é
mais um corte fixo por tier — é uma escolha declarada a cada uso. Se uma futura habilidade de
Conjuração invocar **mais de um** Aliado ao mesmo tempo, o controle vai sempre pro Mestre,
independente do tier (duas fichas simultâneas é sobrecarga de mesa mesmo em tiers baixos).

**Servo de Cinzas** *(Menor)*

*Um pequeno construto de brasa e cinza toma forma, pronto pra golpear no lugar do usuário.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Sabedoria | **Alcance:** 2 casas (onde o Aliado aparece) | **Alvos:** o próprio
  usuário (invoca 1 Aliado)
- **Controle:** ver regra compartilhada acima
- **Intensidade I — ◈ (1 PA) + 3 Mana:** invoca o Servo de Cinzas por **2 rodadas**.
- **Intensidade II — ◈◈ (2 PA) + 6 Mana:** o mesmo, por **3 rodadas**.
- **Intensidade III — ◈◈◈ (3 PA) + 9 Mana:** o mesmo, por **4 rodadas**.
- **O Aliado:** Vida 6, PA ◈ (1), Ataque +1, Dano 1d4, Defesa física 7, Movimento 6 casas. Rola
  a própria Iniciativa e age no próprio turno; ataca a criatura hostil mais próxima do usuário
  (ou onde o jogador mandar, se estiver controlando ele mesmo).
- **Ao fim da duração:** o Servo se desfaz sem penalidade — pode ser reconjurado normalmente,
  pagando PA + Mana de novo.
- **Consequência de morte:** se reduzido a 0 de Vida **antes** do fim da duração, o Servo
  foge/se dissolve, e esta habilidade fica indisponível até o próximo
  [descanso longo](../docs/jogar/exploracao.md#descanso) do usuário — mesmo não tendo, em
  condições normais, restrição de uso por descanso.

**Chamar Lâmina Espectral** *(Médio)*

*Uma arma senciente se materializa no ar, flutuando e golpeando por conta própria.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Sabedoria | **Alcance:** 2 casas (onde o Aliado aparece) | **Alvos:** o próprio
  usuário (invoca 1 Aliado)
- **Controle:** ver regra compartilhada acima
- **Intensidade I — ◈ (1 PA) + 5 Mana:** invoca a Lâmina Espectral por **3 rodadas**.
- **Intensidade II — ◈◈ (2 PA) + 9 Mana:** o mesmo, por **4 rodadas**.
- **Intensidade III — ◈◈◈ (3 PA) + 13 Mana:** o mesmo, por **5 rodadas**.
- **O Aliado:** Vida 10, PA ◈◈ (2), Ataque +2, Dano 1d6, Defesa física 9, Movimento 7 casas.
  Rola a própria Iniciativa e age no próprio turno; ataca a criatura hostil mais próxima do
  usuário (ou onde o jogador mandar, se estiver controlando ele mesmo).
- **Ao fim da duração:** a Lâmina se desfaz sem penalidade — pode ser reconjurada normalmente,
  pagando PA + Mana de novo.
- **Consequência de morte:** se reduzida a 0 de Vida **antes** do fim da duração, a Lâmina
  foge/se dissolve, e esta habilidade fica indisponível até o próximo
  [descanso longo](../docs/jogar/exploracao.md#descanso) do usuário.

**Convocar Guardião do Pacto** *(Maior)*

*Um espírito guerreiro responde ao chamado — só nas horas mais difíceis.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Alcance:** 2 casas (onde o Aliado aparece) | **Atributo:** Sabedoria | **Alvos:** o próprio
  usuário (invoca 1 Aliado)
- **Controle:** ver regra compartilhada acima
- **Custo fixo:** ◈◈◈ (3 PA) + 18 Mana, **1x por
  [descanso longo](../docs/jogar/exploracao.md#descanso)**
- **Efeito:** invoca o Guardião do Pacto, que dura **até o fim da cena**.
- **O Aliado:** Vida 22, PA ◈◈◈ (3), Ataque +3, Dano 1d8, Defesa física 11, Movimento 7 casas.
  Rola a própria Iniciativa e age no próprio turno; ataca a criatura hostil mais próxima do
  usuário (ou onde o jogador mandar, se estiver controlando ele mesmo).
- **Ao fim da cena:** o Guardião se desfaz sem penalidade além do próprio limite de 1x por
  descanso longo.
- **Consequência de morte:** se reduzido a 0 de Vida antes do fim da cena, o Guardião foge/se
  dissolve, e esta habilidade fica indisponível até o próximo descanso longo — o mesmo limite
  que ela já tinha (decisão #6: a raridade do uso já é a punição, sem empilhar outra).
- *(Sem Intensidade — [Custo fixo](../docs/habilidades/regras.md#habilidades-de-custo-fixo),
  Supremo)*

---

## 3. Vínculo com Ser Maior

**Selar o Pacto**

*Um círculo se fecha, um nome verdadeiro é dito, e algo do outro lado responde — a partir daí,
ele atende ao chamado sempre que for convocado.*

⚠ **Fundida a pedido do autor (2026-08-15):** o rascunho original tinha o ritual e a
convocação como duas habilidades separadas; exigir duas escolhas de nível só pra ter acesso a
um vínculo demandava demais do orçamento de habilidades do personagem. Agora é uma habilidade
só, em duas partes.

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Vontade | **Alvos:** 1 entidade (definida em cena, com o Mestre)

**Parte 1 — o ritual** (uma vez por vínculo, fora de combate):

- **Custo fixo:** ◈◈◈ (3 PA) + 20 Mana
- **Requisito:** ritual — fora de combate, exige tempo, lugar e um custo narrativo definido pelo
  Mestre (um nome verdadeiro, um sacrifício, um lugar de poder). A raridade fica a critério do
  Mestre, sem gate fixo de tempo ou material (decisão #9 da arquitetura) — é oportunidade de
  campanha, não de sessão.
- **Teste:** d20 + Vontade
  - **≤ 10 — Falha catastrófica:** o Ser se solta hostil e ataca o conjurador (o Mestre monta a
    ficha, tipicamente Formidável, via
    [Criando uma Criatura](../docs/mestre/criando-criaturas.md)), ou o próprio vínculo se volta
    contra ele — o Mestre decide o que serve melhor à cena. De qualquer forma, o conjurador
    ganha uma [Cicatriz](../docs/jogar/estresse.md#cicatrizes) automaticamente e só pode tentar
    de novo com um ritual **novo**, do zero, com o mesmo risco.
  - **11–16 — Falha recuperável:** o ritual não prende nada. O tempo e os componentes
    investidos se perdem, mas nada de ruim acontece — pode tentar de novo mais tarde.
  - **≥ 17 — Sucesso:** o vínculo se forma. O Ser passa a responder ao conjurador; a ficha dele
    é montada pelo Mestre, tipicamente em Tier **Formidável** (ocasionalmente **Lendário**, pra
    pactos de campanha inteira), via
    [Criando uma Criatura](../docs/mestre/criando-criaturas.md). O vínculo em si é
    **permanente** — existe entre sessões, como uma relação, não como um efeito de cena.
  - **20 natural — Sucesso ampliado:** o vínculo se forma nas melhores condições possíveis —
    menos restrições, o Ser mais disposto a cooperar (o Mestre decide o que isso significa na
    prática).

**Parte 2 — convocar o Ser vinculado** (depois que o ritual tiver sucesso, quantas vezes o
vínculo permitir):

- **Custo fixo:** ◈◈◈ (3 PA) + 20 Mana, **1x por
  [descanso longo](../docs/jogar/exploracao.md#descanso)**
- **Efeito:** o Ser vinculado se manifesta na cena, com a ficha montada no momento do ritual
  (Formidável ou Lendário). Ele age no **próprio turno**, controlado **pelo Mestre** como NPC
  aliado — diferente do Aliado de Combate, aqui não há escolha do jogador: o Ser tem vontade
  própria, é vinculado, não domesticado. Dura até o fim da cena.

**Consequência de morte do Ser vinculado — a mais pesada da escada.** Se reduzido a 0 de Vida
numa convocação, ele **morre de vez**: não volta no próximo descanso longo, não pode ser
trazido de volta por Ressuscitar nem qualquer outra habilidade, e essa entidade específica não
pode ser vinculada de novo — é uma pessoa, não uma categoria. O conjurador ganha uma
[Cicatriz](../docs/jogar/estresse.md#cicatrizes) automaticamente, e perde esta habilidade até
selar um vínculo **novo**, repetindo o ritual do zero (Parte 1), com o mesmo risco de falha
catastrófica de antes.

*(Sem Intensidade — [Custo fixo](../docs/habilidades/regras.md#habilidades-de-custo-fixo),
Supremo nas duas partes)*

!!! nota "Simetria com Banir"
    Um Ser vinculado (ou um Aliado de Combate, Peça 2) também pode ser alvo de
    [Banir](../docs/habilidades/debuff.md) vindo de um inimigo — não conta como a morte da
    criatura, só interrompe a cena. Ver Peça 6.

---

## 4. Companheiro Animal

⚠ **Formato novo, sem precedente no jogo — ver "Pontos que pedem atenção" no fim deste
documento.** Esta é a primeira habilidade que escala pelo **nível do personagem**
([Progressão de Nível](../docs/criacao/progressao.md)), não por Intensidade paga em Mana no
momento de ativar. A tabela de progressão abaixo substitui o bloco de Intensidade I/II/III, e
esse precedente precisa de aprovação explícita antes de ir pra `docs/`.

**Laço de Sangue e Pelo**

*Um vínculo formado ainda filhote — lobo, ave de rapina, urso ou outra fera à escolha — que
cresce ao seu lado, ano após ano, tão forte quanto você se torna.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Atributo:** Sabedoria (ou o atributo que o conceito do vínculo pedir — usado no ataque
  automático do Companheiro)
- **Alvos:** o próprio usuário
- **Custo:** ocupa 1 das 10 escolhas de habilidade da carreira (nível ímpar), como qualquer
  outra. **Sem Mana ou PA pra manter** — o Companheiro ataca sozinho, todo turno, sem competir
  pelo orçamento do dia.
- **Efeito:** invoca um Companheiro Animal (a forma é escolhida ao aprender esta Habilidade, e
  não muda depois) — vínculo **permanente**, existe entre sessões, e **cresce sozinho com o
  nível do usuário** (ver tabela abaixo), do mesmo jeito que Vida e Mana Máximo crescem
  sozinhos a cada nível. No início de cada turno do usuário, o Companheiro ataca a criatura
  hostil mais próxima automaticamente, sem gastar Mana ou PA, rolando **d20 + [Atributo] do
  usuário** contra a Defesa do alvo.

**Progressão por faixa de nível:**

| Faixa de nível | Vida | Ataque | Dano | Defesa física |
|---|---|---|---|---|
| 1–4 | 12 | +2 | 1d6 | 9 |
| 5–10 | 30 | +4 | 2d6 | 12 |
| 11–15 | 55 | +6 | 3d6 | 16 |
| 16–20 | 85 | +8 | 4d6 | 19 |

- **Movimento:** 6 + Agilidade do usuário (mesma fórmula do Bestiário)
- **Quem controla:** o jogador — é a peça mais "sua" do sistema inteiro.

**Consequência de queda e morte** (ver
[Chegando a 0 de Vida](../docs/jogar/dano-e-cura.md#chegando-a-0-de-vida)):

- Ao chegar a 0 de Vida, o Companheiro fica **Caído** — como um personagem, não como uma
  criatura comum (exceção deliberada a
  ["criatura a 0 de Vida morre"](../docs/mestre/criando-criaturas.md#criatura-a-0-de-vida-morre)).
  No início de cada turno dele, rola contra a morte (d20 contra DC 10); o número de falhas que
  aguenta antes de morrer usa a **Vitalidade do usuário** (o Companheiro não tem progressão
  própria de atributos — decisão de redação minha, ver "Pontos que pedem atenção"). Sofrer dano
  enquanto Caído conta como **uma falha imediata**, igual pra um personagem. Pode ser
  **Estabilizado** por um aliado adjacente, ou trazido de volta por qualquer cura.
- O Companheiro também tem acesso a [O Último Turno](../docs/jogar/dano-e-cura.md#o-ultimo-turno):
  o jogador pode declará-lo por ele, do mesmo jeito que declararia pelo próprio personagem — em
  vez de rolar contra a morte, o Companheiro se levanta pra um turno completo (PA, ataque
  automático, tudo) antes do fim.
- Se a rolagem se esgotar (ou ninguém conseguir estabilizar/curar a tempo), a morte é **real**
  — mas não necessariamente definitiva: o Companheiro conta como **aliado morto** pra efeito de
  [Ressuscitar](../docs/habilidades/suporte.md), e pode ser trazido de volta por ela, com as
  mesmas chances e o mesmo risco (inclusive a falha total da própria Ressuscitar, que aí sim
  perde o Companheiro de vez).
- **Só se Ressuscitar não for usada, ou falhar de vez, reconquistar o vínculo custa tempo, não
  só Mana.** Só fora de perigo, e só depois de pelo menos um
  [descanso longo](../docs/jogar/exploracao.md#descanso) dedicado (mecânica e narrativamente) a
  esse processo — não é um clique instantâneo no meio da masmorra. O novo Companheiro nasce nas
  estatísticas da faixa de nível atual (sem penalidade mecânica pro resto da campanha), mas o
  Mestre é incentivado a tratar a cena de vínculo como algo que pesa.

---

## 5. Companheiro Transformável

Upgrade do Companheiro Animal (Peça 4) — exige tê-lo aprendido antes, no molde
Básica → Avançada → Especial de arma.

⚠ **Redesenhada a pedido do autor (2026-08-15):** na versão original, a forma pequena era o
padrão fraco e a forma grande (com a força real) só existia enquanto ativada, pagando Mana. O
autor quer o oposto: **a força é sempre a cheia, o tempo todo** — a forma pequena é só
disfarce/furtividade, nunca uma troca de poder por outra coisa. Como as duas formas passam a
ter a mesma Vida, o "buffer de morte" da versão anterior deixou de fazer sentido e foi
removido.

**Forma Verdadeira**

*O disfarce cai fácil quando precisa — o que sempre esteve ali, revelado.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Requisito:** ter aprendido **Laço de Sangue e Pelo**
- **Atributo:** o mesmo do Companheiro Animal | **Alvos:** o próprio Companheiro
- **Efeito:** o Companheiro ganha uma **forma de disfarce** — pequena e discreta, mas que **não
  muda a força real dele**: mesma Vida, Defesa física e Movimento da tabela de progressão por
  nível (Peça 4). Nessa forma, ele simplesmente escolhe não atacar (fica quieto, some na
  paisagem) e ganha [Vantagem](../docs/glossario.md#vantagem) em qualquer teste pra passar
  despercebido, além de caber em espaços que a forma verdadeira não caberia. Alternar entre a
  forma verdadeira e o disfarce é uma **ação livre, sem custo de Mana ou PA** — inclusive fora
  do próprio turno do usuário, como reação a uma ameaça surgindo.
- *(Sem Intensidade — habilidade utilitária: a força do Companheiro nunca muda, só a aparência
  e o comportamento dele)*

**Fúria Desperta**

*Sem freio, sem cautela — só a fera, inteira.*

- **Chave:** [Conjuração](../docs/glossario.md#conjuracao)
- **Requisito:** ter aprendido **Forma Verdadeira**; só pode ser ativada enquanto o Companheiro
  estiver na forma verdadeira (não durante o disfarce)
- **Atributo:** o mesmo do Companheiro Animal | **Alvos:** o próprio Companheiro
- **Intensidade I — ◈ (1 PA) + 5 Mana:** por 2 rodadas, o Companheiro ganha +1d4 no dano do
  ataque automático, mas perde 2 de Defesa física enquanto durar.
- **Intensidade II — ◈◈ (2 PA) + 8 Mana:** o mesmo, com +2d4 no dano, por 3 rodadas.
- **Intensidade III — ◈◈◈ (3 PA) + 11 Mana:** o mesmo, com +3d4 no dano, por 4 rodadas.
- *(Termina junto com a Forma Verdadeira, se ela acabar antes da duração desta habilidade.)*

---

## 6. Banir

⚠ **Vai para `docs/habilidades/debuff.md`, não para o arquivo de Conjuração — decisão #7 da
arquitetura, por simetria com o resto do grupo Debuff.** Incluído aqui só porque nasceu junto
com o resto do sistema de invocação.

**Selo de Exílio**

*A ordem não é gritada — é dita uma vez, e o que não pertence a este mundo é lembrado disso.*

- **Chave:** [Debuff](../docs/glossario.md#debuff)
- **Atributo:** Vontade | **Dano:** Arcano | **Alcance:** 8 casas | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 2 Mana:** 1d8 de dano (testa contra
  [Defesa mental](../docs/jogar/combate.md#defesa)) + o alvo
  [perde a próxima Reação](../docs/glossario.md#perde-a-proxima-reacao)
- **Intensidade II — ◈◈ (2 PA) + 5 Mana:** 1d8 de dano + o alvo fica
  [Atordoado](../docs/glossario.md#atordoado) por 2 rodadas — impedido de agir, mas sem sair da
  cena
- **Intensidade III — ◈◈◈ (3 PA) + 8 Mana:** 1d8 de dano + o alvo é **expulso**: sai da cena de
  vez, de volta ao plano de origem
- **Crítico (20 natural):** dano máximo (8) + 1d8 extra, e sobe 1 Intensidade
- **Alvo válido:** só afeta criaturas cuja ficha declare origem invocada/planar — Elementais,
  demônios, mortos-vivos erguidos por Necromancia, e qualquer Ser vinculado da Peça 3 (critério
  por fluff narrativo na ficha, não por uma faceta nova do Bestiário — ver arquitetura, seção 6)

!!! nota "Simetria"
    Um Aliado de Combate ou Ser vinculado de um PJ (Peças 2 e 3) também pode ser alvo de
    **Selo de Exílio** vindo de um inimigo. Isso não conta como a morte da criatura — ela só
    volta pro próprio plano, e a cena atual é interrompida.

**Fechar a Porta**

*Um gesto largo, e toda porta pra outro lugar se fecha de uma vez.*

- **Chave:** [Debuff](../docs/glossario.md#debuff)
- **Custo fixo:** ◈◈◈ (3 PA) + 12 Mana | **Atributo:** Vontade | **Dano:** Arcano |
  **Alcance:** 8 casas |
  **Alvos:** todas as criaturas hostis de origem invocada/planar em 3 casas de raio do ponto
- **Acerto** (testa cada alvo contra a
  [Defesa mental](../docs/jogar/combate.md#defesa)): 1d6 de dano + cada alvo é expulso da cena,
  de volta ao plano de origem
- **Crítico (20 natural):** dano máximo (6) + 1d6 extra em todos
- *(Sem Intensidade — área de 3 casas de raio,
  [Custo fixo](../docs/habilidades/regras.md#habilidades-de-custo-fixo))*

---

## Pontos que pedem atenção do autor

Tudo abaixo é escolha minha, feita pra ter texto completo e coerente — nenhuma delas é
arquitetura fechada, e todas podem ser trocadas sem quebrar o resto do documento.

1. **Resolvido:** formato novo da Peça 4 (progressão por nível, sem Intensidade) — **aprovado**
   pelo autor. Vira precedente válido pra futuras habilidades parecidas.
2. **Resolvido:** Vitalidade usada nas falhas de morte do Companheiro Animal é a **do usuário
   (dono)** — confirmado.
3. **Resolvido:** atributos escolhidos (Sabedoria pros vínculos vivos, Vontade pro Ser Maior e
   Banir) — **confirmados como estão**.
4. **Resolvido:** números de Mana/PA de trabalho (Familiar Simples, Companheiro Transformável,
   Banir) — **aceitos como âncora**, ajustáveis na hora de migrar pra `docs/`.
5. **Obsoleto:** a escala de Intensidade de Forma Verdadeira não existe mais — a habilidade foi
   redesenhada (ver seção 5) pra ser puramente utilitária/disfarce, sem Intensidade, a pedido
   do autor. A força do Companheiro agora é sempre a cheia, em qualquer forma.
6. **Resolvido:** "Suprimido" (arquitetura, Intensidade II de Banir) reaproveita o **Atordoado**
   que já existe no glossário — **confirmado**, sem termo novo.
7. **O verbete `#conjuracao` no glossário ainda não existe** — precisa ser criado junto com a
   página do grupo (`docs/habilidades/conjuracao.md`) quando isso for aprovado, seguindo o
   padrão dos outros grupos (`docs/habilidades/regras.md`, tabela de Grupos).
8. **Resolvido (2026-08-15):** Selar o Pacto e Convocar o Vinculado eram duas habilidades
   separadas — fundidas numa só, a pedido do autor, porque exigir duas escolhas de nível pra
   acessar um único vínculo pesava demais no orçamento de habilidades da carreira. O custo
   ficou em 20 Mana nas duas partes (ritual e convocação), mantido igual por simplicidade.
9. **A troca de Vínculo Selvagem por Laço de Sangue e Pelo nas 3 trilhas de Pacote que citam o
   primeiro (decisão #12, já fechada) não foi feita neste documento** — fica pendente pro
   momento em que este grupo for aprovado e migrado pra `docs/`.
