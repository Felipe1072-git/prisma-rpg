# Proposta — migração pra d100

Rascunho de trabalho. Nada aqui é canônico — é a base pra fechar as tabelas probabilísticas
antes de tocar em `docs/`. Se essa migração for pra frente, ela reescreve `testes.md`,
`combate.md`, `atributos.md`, `mana.md` e o custo em Mana/dano das 579 habilidades — é a
maior mudança estrutural desde a v0.2.

## Painel de Atributos e Derivados

O d100 substitui os 8 atributos atuais (Força, Vitalidade, Agilidade, Inteligência,
Sabedoria, Vontade, Sorte, Sanidade) por **8 novos** — 7 consolidados + Exploração, criado
em 2026-08-20 pra cobrir a lacuna de percepção que a Sabedoria deixava. Painel de trabalho —
vamos preenchendo as descrições aos poucos, uma de cada vez.

### Ataque
- **O que representa:** capacidade de causar dano físico em combate — força, precisão e
  técnica com armas, corpo a corpo ou à distância. Entra na rolagem de qualquer ataque
  físico (arma corpo a corpo, arco, ataque desarmado) e no tanto de dano que ele causa.
- **Deriva — Dano Físico** (corpo a corpo e à distância, confirmado 2026-08-20): o dano que
  ataques físicos causam. Fórmula exata pendente do dado de dano (ver item 5 de "Em aberto").

### Defesa
- **O que representa:** resistência física do personagem — encaixar, aguentar pancada,
  resistir a dano físico direto. Sustenta a Vida e a Fortitude Física.
- **Deriva — Vida:** o quanto de dano o personagem aguenta antes de cair. **Vida Máxima =
  20 + Nível + (Defesa × 2)** — forma provisória, coeficientes dependem do dado de dano
  (item 5 de "Em aberto").
- **Fortitude Física (renomeado de "Resistência Física", 2026-08-20):** não é um derivado
  com fórmula própria — é o **valor cru do atributo Defesa**, usado como número-alvo em
  testes que pulam a Evasão (veneno já ingerido, doença, exaustão — efeitos que o corpo
  resiste por dentro, não desvia fisicamente). Renomeado porque "Resistência" já é o nome
  da condição existente que reduz dano por tipo (`dano-e-cura.md`) — nomes diferentes,
  papéis diferentes, sem redução de dano embutida no atributo.

### Magia
- **O que representa:** poder mágico do personagem — controle sobre mana, capacidade de
  canalizar e resistir a efeitos arcanos. Sustenta a Mana, a Fortitude Mágica e o Dano
  Mágico.
- **Deriva — Mana:** total de Mana disponível pra pagar Intensidade de habilidades.
  **Mana Máximo = 20 + Nível + (Magia × 2)** — mesma forma da Vida (revisado 2026-08-20).
- **Fortitude Mágica (renomeado de "Resistência Mágica", 2026-08-20):** mesma lógica da
  Fortitude Física — não tem fórmula própria, é o **valor cru do atributo Magia**, usado
  como número-alvo em testes que pulam a Evasão (maldição, petrificação, controle mental de
  origem mágica). Controle mental não-mágico (persuasão, manipulação social) usa Social, não
  isso.
- **Deriva — Dano Mágico:** o dano que ataques mágicos causam — equivalente do Dano Físico,
  pra magia.

### Agilidade
- **O que representa:** reflexos e velocidade — capacidade de desviar de golpes e reagir
  rápido. Sustenta a Evasão e entra na Iniciativa (junto com Sorte).
- **Deriva — Evasão:** o número que quem ataca precisa superar. **Evasão = Agilidade +
  Armadura** (confirmado 2026-08-20 — sem Base de Resiliência, ver seção "Defesa em
  combate").
- **Deriva — Iniciativa:** ordem de turno em combate, junto com Sorte — mesma lógica do
  sistema atual (d20+Agilidade+Sorte), só trocando o dado.

### Sorte
- **O que representa:** o acaso e a fortuna do personagem — estar no lugar certo na hora
  certa. Sustenta a Tx. de Crítico e entra na Iniciativa (junto com Agilidade).
- **Deriva — Iniciativa:** mesma linha do derivado de Agilidade — os dois entram juntos na
  ordem de turno.
- **Deriva — Tx. de Crítico:** confirmado. Limiar = Sorte ÷ 3 (arredondado); rolar ≤ limiar
  no d100 é sucesso automático e crítico, não importa a Dificuldade. Ver "Decisões
  fechadas", item 3.
- **Deriva — Rerolagens:** confirmado. **Usos por descanso longo = 1 + (Sorte ÷ 10)**
  (reescala de "1 + Sorte" do sistema atual, que na escala 0–100 chegaria a 101 usos e
  quebraria o recurso). **Só vale pra teste que falhou** — rerolar um sucesso pra tentar
  upar em crítico (crit-fishing) não é permitido, decisão consciente pra não somar com o
  floor de crítico (Sorte alta já dá crítico sozinha; deixar rerolar sucesso também
  empilharia demais).

### Sanidade
- **O que representa:** estabilidade mental do personagem — o quanto ele resiste a horror,
  pânico e colapso psicológico. Sustenta o Estresse.
- **Deriva — Estresse:** total de Estresse que o personagem aguenta antes de sofrer as
  consequências de sobrecarga mental (mesmo papel que tem hoje). **Estresse Máximo =
  10 + (Nível ÷ 2) + (Sanidade ÷ 2)** — confirmado, ver seção "Sistema de Estresse".

### Social
- **O que representa:** presença e habilidade de influenciar os outros — o "Carisma" deste
  sistema. Usado tanto **ativamente** quanto **passivamente**: persuadir e ser persuadido,
  enganar e notar/resistir a ser enganado, intimidar e resistir a intimidação. Controle
  mental **mágico** não usa Social — é resistido pela Fortitude Mágica (Magia). Social
  cobre só a influência não-mágica, pessoa contra pessoa.
- **Deriva — Testes de persuadir, intimidar, enganar (e seus opostos passivos):** não gera
  um número derivado separado — o próprio valor de Social entra direto na rolagem desses
  testes, dos dois lados (quem tenta influenciar e quem resiste).

### Exploração
- **O que representa:** atenção ao ambiente e competência de aventureiro fora de combate e
  fora de conversa — notar algo escondido (armadilha, disfarce, item), rastrear, se
  orientar, sobreviver longe da civilização. Funciona como o Social: usado tanto
  **ativamente** (procurar algo de propósito) quanto **passivamente** (notar por acaso).
  Criado em 2026-08-20 pra cobrir a lacuna de percepção que a Sabedoria deixava.
- **Deriva — Testes de perceber, rastrear, se orientar, sobreviver:** não gera um número
  derivado separado — o próprio valor de Exploração entra direto nesses testes, ativos e
  passivos (mesma lógica do Social).

Todas as fórmulas dos derivados estão fechadas — ver "Vida e Mana", "Sistema de Estresse",
e as notas de Fortitude Física/Mágica acima.

## Simulação de arquétipos (2026-08-20)

Rodei Guerreiro/Arqueiro/Mago, cada um em Equilibrada (peso espalhado, pensando nos
derivados pra dar uma experiência sólida) e Min-Max (peso quase todo no atributo principal),
usando a curva de criação+progressão abaixo. Resultado completo ficou só na conversa (não
duplicado aqui pra não desatualizar) — o que vale registrar: **peso fixo por atributo ao
longo da carreira** é o método de simulação (não uma escolha nível a nível), e todo build
capado bate o teto de 100 no atributo principal por volta do nível 53-57, sobrando quase
metade da progressão pra investir em outro lugar — consistente com o que a tabela de
progressão geral já mostrava.

⚠ Essa simulação rodou em cima dos 7 atributos de antes do Exploração existir — os números
exatos (pesos por build) ficam desatualizados agora que são 8. Recalcular quando fizer
sentido, não é bloqueante pro resto.

## Decisões fechadas (2026-08-20)

1. **d100 = par de d10 lido como percentil (1–100)**, não a soma (2–20) — distribuição
   uniforme, necessária pro floor de crítico do item 3 fazer sentido matematicamente (soma
   daria uma curva de sino, onde cada valor tem probabilidade diferente).
2. **Resolução: d100 + Atributo vs Defesa**, mesma estrutura do `d20 + Atributo vs
   Dificuldade` atual, só recalibrada — preserva a única regra do jogo, "quem age, rola".
3. **Crítico — confirmado, substitui a ideia de doubles inteiramente:**
   **rolar ≤ limiar (Sorte ÷ 3, arredondado) = sucesso automático e crítico**, não importa
   a Dificuldade/alvo. É a mesma lógica do "20 natural sempre passa" de hoje, generalizada
   pra escalar com Sorte em vez de ser um valor fixo pra todo mundo. Como todo atributo
   nasce em 5 na criação, o limiar nunca é zero — todo personagem mantém pelo menos 1% de
   crítico garantido (limiar mínimo = 1), mesmo sem investir em Sorte.
   - Matemática: contra uma Dificuldade que precisaria de roll ≥ D normalmente, o floor só
     **adiciona** chance de sucesso quando limiar > D-1 (ou seja, quando a tarefa já seria
     difícil o bastante pra falhar nesses valores baixos). Contra tarefas fáceis, não muda
     nada — só reclassifica sucessos que já existiam como críticos.
   - Consequência aceita: com Sorte muito alta, isso pode furar o "Lendário nunca vira
     rotina" da Tabela de Dificuldades — decisão consciente do autor ("é sorte, né").
4. **Fumble — confirmado: não existe mais como mecânica.** Doubles também cobria falha
   crítica; sem doubles, falha vira só falha normal, sem penalidade extra. Autor não usa
   fumble na mesa há anos.
5. **Vantagem/Desvantagem:** 2d100, fica com o maior/menor. Fórmula (não muda com o dado):
   Vantagem = 1−(1−p)², Desvantagem = p². O crítico (item 3) checa só o dado mantido.
6. **Atributos 0–100, todos.** Teto teórico é 100, mas nenhum PJ chega lá só jogando — quem
   chega perto (foco total) atinge por volta de 100 já na metade da carreira (ver tabela).
7. **Requisito de Atributo por habilidade: confirmado como escala suave**, não bloqueio —
   qualquer habilidade continua acessível desde o nível 1 (preserva "sem restrições
   artificiais" do CLAUDE.md). Abaixo do Atributo recomendado, rola a habilidade com
   Desvantagem; no recomendado ou acima, rola normal. Ancorado na Escala que o site já usa
   (grau de arma + potência geral), não em 579 valores individuais — ver tabela abaixo.

## Progressão de atributo (confirmada, 2026-08-20)

**Nível 0 (criação):** todo atributo começa em **5** (automático, não se distribui) + o
jogador distribui **15 pontos livres** como quiser. Isso é só da criação — não soma com a
regra de nível abaixo, mesmo o nível 0 sendo par.

**A partir do nível 2, a cada nível par, ganha 5 pontos pra distribuir.** Taxa **constante**
(não escalonada) — motivo da mudança: a taxa escalonada de antes (1/2/3/4 pontos por bloco
de 25 níveis) deixava o bloco mais pobre (1 ponto/nível) bem nos níveis 1-25, exatamente
onde a maioria das campanhas reais se encerra (poucas passam de ~10 sessões). Taxa
constante entrega o mesmo total (250 pontos, 50 concessões de 5 ao longo de 100 níveis) mas
sentido desde cedo, não só pra quem chega ao fim do jogo.

Simulação em três perfis (teto 100 por atributo):

| Nível | Focado (tudo aqui) | Misto (metade aqui) | Disperso (~1/8 aqui) |
|---|---|---|---|
| 0 (criação) | 20 | 13 | 7 |
| 25 | 80 | 43 | 14 |
| 50 | 100 (bateu o teto ~nível 32) | 75 | 23 |
| 75 | 100 | 100 (bateu o teto ~nível 70) | 30 |
| 100 | 100 | 100 | 38 |

Mesmo efeito de arco que já gostávamos antes (focado termina cedo e diversifica; misto
termina mais perto do fim; disperso nunca bate teto) — só que comprimido pra caber dentro
do intervalo de níveis que uma campanha real costuma alcançar, em vez de só aparecer pra
quem chega ao nível 100.

## Requisito suave de Atributo (proposta, 2026-08-20)

Ancorado nas faixas de Mana que `mana.md` já define pra Escala geral, e nos custos por grau
que o Arsenal já define pra Escala de arma:

| Escala | Faixa de Mana (já existe) | Atributo recomendado (proposta) |
|---|---|---|
| Básica (arma) | 1/3/6 por Intensidade | 15 |
| Avançada (arma) | 2/5/9 por Intensidade | 35 |
| Especial (arma) | 3/7/12 por Intensidade | 55 |
| Menor (geral) | 1–3 | 20 |
| Moderado (geral) | 4–8 | 40 |
| Maior (geral) | 9–15 | 65 |
| Supremo (geral) | 16+ | 85 |

Abaixo do recomendado, a rolagem é feita com Desvantagem (reaproveita a mecânica do item 4,
não inventa um segundo sistema de bônus). **Números aprovados (2026-08-20)** — a
progressão bate com a curva de atributos (Menor alcançável cedo, Supremo só perto do fim da
carreira).

## Defesa em combate na escala nova (2026-08-20)

O atributo **Defesa** (deriva Vida/Fortitude Física) e o número que o atacante precisa
superar pra acertar são **coisas diferentes** — o segundo precisa de nome próprio, porque
"Defesa" já está ocupado pelo atributo.

1. **Nome do número-alvo físico — confirmado: Evasão.** Não precisa de palavra nova — é o
   próprio derivado de Agilidade que serve de alvo. **Evasão = Agilidade + Armadura**
   (sem Base de Resiliência — ver item 6 abaixo).
2. **O que decide se um ataque físico acerta — confirmado.** É a **Evasão** (derivado de
   Agilidade) que o atacante precisa superar, não o atributo Defesa. O atributo Defesa vira
   só Vida (quanto o personagem aguenta depois de já ter sido atingido) — não entra no
   "acerta ou não".
3. **Números-alvo mentais — confirmado.** Sem termo novo: controle mental mágico usa
   **Fortitude Mágica** (Magia) como alvo, e manipulação social usa o próprio **Social**
   como alvo. Os dois derivados já viram número-alvo do jeito que já são.
4. **Buraco de percepção — resolvido.** Virou o 8º atributo, **Exploração** (não coube
   dentro de Social) — ver painel. O sistema volta a ter 8 atributos, não 7.
5. **Criaturas — confirmado: valor fixo, escrito à mão por criatura.** Sem fórmula de
   progressão, igual já funciona hoje (a reescala de 2026-08-03 já dizia "o conceito manda
   no número"). O Tier vira só referência de faixa esperada, não obrigação.
6. **Base de Resiliência — confirmado: removida das fórmulas de número-alvo.** Ela existia
   porque o atributo sozinho, no d20 atual, é pequeno demais (-2 a +13) pra sustentar a
   conta sozinho — precisava de um piso fixo por baixo. Agora que o jogador investe pontos
   de verdade e o atributo chega a 100, o atributo já carrega o peso todo. Manter uma base
   fixa por cima diluiria a escolha de investimento (quem faz dump em Agilidade devia ficar
   fácil de acertar; um bônus de Tier de graça por cima disfarça isso). Fica:
   - **Evasão = Agilidade + Armadura**
   - **Fortitude Mágica** (como alvo) = o próprio valor de Magia
   - **Fortitude Física** (como alvo) = o próprio valor de Defesa
   - **Social** (como alvo) = o próprio valor de Social
   - **Exploração** (como alvo, testes passivos de percepção) = o próprio valor de Exploração

   Pras criaturas, o Tier continua como referência de faixa esperada pros atributos que o
   Mestre escreve à mão (ver item 5), só não soma mais como bônus fixo formal.

## Vida e Mana (proposta, 2026-08-20)

**Mana Máximo = 20 + Nível + (Magia × 2)** — **revisado em 2026-08-20** (era
`10 + Nível÷2 + Magia÷2`). O autor achou o pool pequeno demais perto da Vida — mesma forma
da Vida agora, só trocando Defesa por Magia. Mago focado (nível 100, Magia 98) chega a
**316** de Mana, mais até que a própria Vida dele (210) — combina com "frágil de corpo,
carrega poder de sobra". Guerreiro (pouca Magia) sobe de 65 pra **140**.

⚠ **Isso reabre o item "validado contra Grau de Poder" logo abaixo** — os custos de Mana das
habilidades (1-16) não escalaram junto, então o número de Supremos por descanso que a
fórmula antiga preservava (~6) vai subir bastante até esse reequilíbrio acontecer. Decisão
consciente do autor: fechar a forma do pool agora, deixar o reequilíbrio de custo (~×2,5 nos
579 custos de Mana) pra quando as habilidades forem recalibradas — mesma frente do dado de
dano. Mana continua universal — até quem não investe em Magia acumula bastante só pelo lado
do Nível.

**Criaturas — recalibradas junto.** Só Formidável/Lendário têm Mana (Comum/Treinado
continuam sem, por escolha de design anterior à migração). Mesma forma, com um "nível
equivalente" por Tier no lugar do Nível de PJ: **Formidável = 70 + Magia×2** (nível
equivalente ~50), **Lendário = 110 + Magia×2** (nível equivalente ~90). Ex: Súcubo (Magia
47) → 164 Mana; Tarrasque (Magia 43, burro mesmo) → 196 — bem menor que o Lich (Magia 79) →
268, apesar de os dois serem Lendário.

**Custo em Mana das ações de criatura — também resolvido (2026-08-20), diferente do custo de
habilidade de PJ.** O pool maior por si só deixava os chefes com Intensidade III quase
ilimitada (Lich chegaria a ~14 usos do Raio Necrótico). Em vez de esperar a recalibração das
579 habilidades de PJ, o autor pediu pra fechar isso agora nas 30 fichas Formidável/Lendário
— escopo bem menor (poucas ações cada). **Custo ×2,5** em toda ação com Mana (Menor 1-3→3-8,
Moderado 4-8→10-20, Maior 9-15→22-38, Supremo 16+→40+). Lich: Raio Necrótico vai de 6/12/18
pra 15/30/45 — com 268 de Mana, dá ~6 usos da Intensidade III, batendo com o alvo de "~6
Supremos por descanso" que já tínhamos validado antes pro pool antigo. **Consequência aceita
de propósito:** por enquanto criatura e personagem usam escalas de custo diferentes (criatura
já reequilibrada, PJ ainda não) — só se alinham quando as 579 habilidades gerais forem
recalibradas. Regra pra criatura nova: mesma tabela de Grau de Poder do `mana.md`, ×2,5.

**Validado contra a tabela de Grau de Poder — status revisado em 2026-08-20.** A validação
original (nível 100 banca ~6 Supremos, comparável a slots vancianos) valia pra fórmula
antiga. Com o pool novo (316 no Mago focado), o mesmo Mago banca **~19 Supremos** por
descanso — não é mais comparável, mas o autor decidiu aceitar isso como estado temporário
até o reequilíbrio de custo (ver nota acima), não como decisão final. **Decisão anterior
(manter sem teto de usos) continua valendo**: mesmo com custo maior no futuro, a resposta
pra "isso ficou generoso demais" continua sendo subir o custo do Supremo, nunca empilhar um
teto de usos — restrição dupla continua rejeitada. Pool livre (em vez de slot fixo por
"círculo") já é a identidade do sistema, e um teto de "N Supremos por descanso" seria
**restrição dupla** em cima do custo de Mana — o mesmo padrão que o autor já rejeitou antes
(Servo de Cinzas, Chamar Lâmina Espectral: "nunca dupla restrição, sobe o Mana em vez de
empilhar limite de uso"). Se algum dia isso precisar apertar, a alavanca certa é subir o
custo do Supremo (hoje 16+), não adicionar teto de usos — mas isso reabriria o threshold já
ancorado no Requisito suave, então só mexer com necessidade real.

**Vida Máxima = 20 + Nível + (Defesa × 2)** — **confirmada e validada** (atualizado
2026-08-20). Mesma lógica linear do Mana, peso maior porque Vida absorve vários golpes por
combate, não paga custos pontuais. Inicialmente marcada como provisória até o dado de dano
fechar — mas o processo de calibração do dado (ver "Dado de dano") **usou esses mesmos
números de Vida como alvo fixo** e a regra de escalada bateu com eles sem ajuste, então a
fórmula já está validada. Só falta a execução (aplicar dado calibrado nas 579 fichas), que
não deveria mudar a fórmula em si — só ajustar durante o playtest se algo destoar na
prática.

## Tabela de Dificuldades (2026-08-20)

Escala direta ×5 da tabela atual (mesma proporção de d20→d100 e atributo -2/+13→0-100),
confirmada:

| Dificuldade | DC hoje (d20) | DC nova (d100) |
|---|---|---|
| Trivial | 5 | 25 |
| Fácil | 10 | 50 |
| Média | 15 | 75 |
| Difícil | 20 | 100 |
| Muito difícil | 25 | 125 |
| Lendário | 30 | 150 |

Preserva a propriedade de hoje onde as duas dificuldades mais altas nunca viram rotina —
nem um 100 natural sozinho alcança DC 125/150 sem atributo investido. **Exceção aceita:**
quem investe pesado em Sorte fura isso via o floor de crítico (ver "Decisões fechadas",
item 3) — decisão consciente do autor, não um furo acidental.

## Em aberto, em ordem de bloqueio

1. ~~Base de Resiliência e Guarda na escala nova~~ — **resolvido**: Base de Resiliência
   removida das fórmulas de número-alvo (ver "Defesa em combate", item 6). Evasão/
   Fortitude Física/Fortitude Mágica/Social/Exploração usam o atributo puro + bônus
   (Armadura só na Evasão).
2. ~~Tabela de Dificuldades (DC)~~ — **resolvido**, ver seção acima.
3. ~~Tx. de Crítico (Sorte)~~ — **resolvido**: crítico = roll ≤ limiar (Sorte÷3), substitui
   doubles. Ver "Decisões fechadas", item 3.
4. ~~Doubles = crítico/fumble~~ — **resolvido**: doubles não existe mais como mecânica;
   fumble também foi removido. Ver "Decisões fechadas", itens 3-4.
5. **Dado de dano (d4 a d20)** — maior volume de trabalho: as 579 habilidades têm dado de
   dano escrito à mão. Deixar por último, depois que a base estiver fechada. **Bloqueia a
   revisão final de Vida e Mana** (ver seção acima).
6. ~~Ritmo de progressão do atributo~~ — **resolvido**: trocado de escalonado (1/2/3/4 por
   bloco) pra constante (5 a cada nível par), ver seção "Progressão de atributo".
7. ~~Rerolagens via Sorte~~ — **resolvido**: 1 + (Sorte ÷ 10), só em teste que falhou. Ver
   painel de Sorte.

## Dado de dano (2026-08-20)

**Achado importante:** o Atributo **não entra no dano** hoje — só no acerto
(`d20+Atributo vs Defesa`). Dano é só o dado da arma (`equipamento/index.md`, "Resolução de
Ataque"), rolado puro. Isso significa que o problema de escala que apareceu várias vezes
nesta conversa (atributo grande demais dominando a conta) **não existe aqui** — dado de
dano é território isolado, mais simples do que temido.

**Mas Vida cresceu e dano precisa acompanhar.** A fórmula de Vida que fechamos (20+Nível+
Defesa×2) chega a **290** num Guerreiro nível 100 — contra **~140** no sistema atual no
nível 20 equivalente. Isso já reabre um problema que o autor tinha apontado antes desta
conversa: **o dano de todas as habilidades do jogo já era baixo demais** frente à Vida
existente. Reescalar o dado sem revisar o dano em si só pioraria a proporção.

**Decisão: reformular o dano de todas as habilidades do zero**, em vez de só converter o
que existe pela regra de escalada por Intensidade (I = dado da arma sem alteração — d4
continua existindo —, II = dado sobe um degrau, III = 2× o dado da II, ex: Machado vira
2d20). A regra de escalada continua valendo como estrutura; o que muda é que cada
habilidade vai ser recalibrada contra a tabela abaixo, não só ter seu dado antigo
reaproveitado.

### Tabela de referência — dano médio por XdY

| Dados | d4 | d6 | d8 | d10 | d12 | d20 |
|---|---|---|---|---|---|---|
| 1 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 10,5 |
| 2 | 5 | 7 | 9 | 11 | 13 | 21 |
| 3 | 7,5 | 10,5 | 13,5 | 16,5 | 19,5 | 31,5 |
| 4 | 10 | 14 | 18 | 22 | 26 | 42 |
| 5 | 12,5 | 17,5 | 22,5 | 27,5 | 32,5 | 52,5 |
| 6 | 15 | 21 | 27 | 33 | 39 | 63 |
| 7 | 17,5 | 24,5 | 31,5 | 38,5 | 45,5 | 73,5 |
| 8 | 20 | 28 | 36 | 44 | 52 | 84 |
| 9 | 22,5 | 31,5 | 40,5 | 49,5 | 58,5 | 94,5 |
| 10 | 25 | 35 | 45 | 55 | 65 | 105 |

Referência de escala: Vida hoje (na proposta) varia de ~13 (nível 0, build disperso) a
~475 (Guerreiro nível 100, build focado) — a faixa de 10 a 65 de dano médio cobre a maioria
dos casos reais; XdY com d20 entra pros golpes mais extremos do jogo (Supremos, Lendários).

### Calibração contra Vida (2026-08-20)

**Problema que isso precisa evitar:** no sistema atual, Vida escala 7,6× do nível 1 ao 20,
mas Dano só escala 2,7× — combates ficam cada vez mais arrastados em níveis altos porque
Vida cresce muito mais rápido que a capacidade de causar dano (registrado antes desta
conversa, ver `notas/auditoria.md`). A reformulação **precisa calibrar dano contra Vida em
cada ponto da progressão**, não só nas pontas, senão repete o mesmo problema.

**Alvo usado:** ~10 golpes pra derrotar um alvo equivalente, constante em todo nível (não
só início/fim). Testado contra a Vida do Guerreiro (40→79→134→205→290 nos checkpoints):

| Nível | Vida | Dano médio alvo (Vida÷10) | XdY mais próxima |
|---|---|---|---|
| 0 | 40 | 4 | 1d6 (3,5) |
| 25 | 79 | 7,9 | 2d8 (9) ou 2d6 (7) |
| 50 | 134 | 13,4 | 2d12 (13) |
| 75 | 205 | 20,5 | 2d20 (21) |
| 100 | 290 | 29 | 3d20 (31,5) |

**Achado bom:** a regra de escalada por Intensidade (I = dado da arma, II = sobe um degrau,
III = 2× o dado da II) **já bate sozinha com essa curva**, sem precisar de ajuste extra —
arma **d10** na Intensidade III dá 2d12 (13, bate com o alvo do nível 50); arma **d12** na
Intensidade III dá 2d20 (21, bate com o alvo do nível 75). Arma pesada natural fica
calibrada pro fim-jogo, arma média pro meio-jogo — o Requisito suave de Atributo (que já
exige mais investimento pra Escala mais alta) já empurra pra esse alinhamento sozinho.

**Consequência pro escopo:** as **186 habilidades de arma** já estão estruturalmente
calibradas pela regra de escalada — não precisam de recálculo individual. O que resta é
recalibrar as **~394 habilidades gerais** com dado próprio escrito à mão (Supremos, magias
etc.) contra a tabela de referência acima — trabalho de execução, não de definição de regra.

⚠ **Corrigido na execução da Fase 2 (2026-08-20): a frase acima estava errada.** Abrir as 186
habilidades de arma de verdade mostrou que cada uma tem dado por Intensidade **escrito à
mão, individualmente** — não herdava a regra de escalada automaticamente, do jeito que essa
auditoria tinha assumido de longe. Precisaram de recálculo, sim. Resolvido com uma **regra
única por grau, aplicada igual em toda arma** (escolhida pelo autor entre as opções
apresentadas):

- **Grau define o multiplicador M** — Básica ×1, Avançada ×2, Especial ×3.
- Dentro do grau, a escalada por Intensidade continua igual à geral: **I = M × dado base da
  arma**, **II = M × dado um degrau acima**, **III = 2M × dado um degrau acima**. Degraus:
  d4→d6→d8→d10→d12→d20.
- **Custo fixo** (Especiais de área 3+ casas) usa o valor "cheio" — igual ao da Intensidade
  III (2M × dado subido) — num resultado único, sem Intensidade pra escolher.
- Exemplo (Alfange, arma d8): Básica I=1d8/II=1d8→1d10/III=2d8→2d10; Avançada
  I=2d8/II=2d8→2d10/III=3d8→4d10; Especial I=2d8→3d8/II=3d8→3d10/III=3d8→6d10.

Script de migração (`notas/` → execução, não fica versionado aqui) processou as 62 armas ×
3 graus = 186 habilidades sem perda: uma delas (**Manopla Mística / Guardião Invocado**,
Especial) usa um formato fora do padrão — dano automático em 3 aplicações ao longo de 3
rodadas, em vez de Acerto/Intensidade — e não bateu no regex do script; corrigida à mão pro
valor "cheio" do grau (2M × dado subido = 6d10 pro Especial) dividido pelas 3 aplicações =
**2d10 cada**. Renomeação de atributo aplicada junto (Força→Ataque, Inteligência→Magia,
Vontade→Social, exceto o modo Arcano do Báculo, que é Vontade→Magia — é conjuração, não
persuasão). Requisito de Atributo Mínimo das armas, Escudos e Armaduras também remapeados
nessa fase (ver tabela da "Segunda auditoria" acima; Escudos/Armaduras seguiram a mesma
regra ×5 que a Couraça Natural das criaturas).

### Vida das criaturas (2026-08-20)

O Bestiário (52 criaturas) também tem Vida fixa escrita à mão, na escala antiga — nunca foi
tocado nesta conversa. Multiplicador calculado comparando Vida de PJ (sistema antigo vs
novo) em dois personagens de referência: Guerreiro (investe pesado em Defesa) dá **~2×**;
Mago (investe pouco) dá **~1,5×**. Usei a **média dos dois (1,75×)**, pra não calibrar só
contra o extremo durão nem só contra o frágil — criaturas enfrentam o grupo inteiro,
misturado, e não temos ainda um jeito de validar contra dano agregado do grupo.

Aplicado às faixas de Vida por Tier da reescala de 2026-08-03 (preserva as proporções
internas entre Tiers, só multiplica tudo):

| Tier | Vida hoje | Vida proposta (×1,75) |
|---|---|---|
| Comum | 4–24 | 7–42 |
| Treinado | 20–60 | 35–105 |
| Formidável | 55–150 | 96–263 |
| Lendário | 200–680 (Tarrasque) | 350–1190 |

O Ataque/dano das 52 criaturas precisa do mesmo tratamento que as habilidades gerais
(recalibrar contra a tabela de referência XdY) — mesma frente de execução já registrada
acima, não uma decisão nova.

## Auditoria antes de ir pro site (2026-08-20)

Releitura do rascunho inteiro contra os sistemas atuais, procurando fórmula que ninguém
revisitou. Três buracos reais achados:

1. **Movimento — resolvido.** `6 casas + Agilidade` quebrava (~106 casas com Agilidade 100).
   **Movimento = 6 + (Agilidade ÷ 10)**, arredondado — mesma divisão usada em Rerolagens,
   mantém a faixa de hoje (4-19 casas) com curva suave. Ex: Agilidade 79 → 14 casas.
2. **Falhas até morrer (Caído, 0 de Vida) — resolvido, simplificado.** Em vez de reescalar
   a tabela de Vitalidade (que também quebrava com Defesa 0-100), o autor decidiu **jogar a
   mecânica fora e simplificar**, já que os HP ficaram grandes demais pra um sistema de
   múltiplas falhas fazer sentido:
   - **Falhas até morrer = sempre 1**, não escala mais com Defesa.
   - Ao cair a 0: no início do próximo turno, rola **d100 vs DC 50** (Fácil), sem somar
     atributo (mesma regra de hoje — "o dado mede só a sorte, igual pra todos"). Sucesso =
     Estável. Falha = morre.
   - Um aliado pode estabilizar antes disso (mesma Ação Básica de sempre), mas agora
     precisa de um **teste de Exploração vs DC 50** pra funcionar — deixa de ser automático,
     ganha risco de verdade. Exploração cobre "sobreviver" na própria descrição, então
     primeiros socorros de campo cabe sem precisar de atributo novo.
   - Cura continua resolvendo, como já era.
3. **Estresse Máximo — resolvido**, ver seção "Sistema de Estresse" abaixo.

**Inconsistência menor — resolvida.** Fortitude Física (Defesa) e Sanidade (contra
horror/pânico) confirmados como número-alvo direto, mesmo padrão dos outros quatro — sem
Base de Resiliência. No caminho, apareceu e foi resolvida uma colisão de nome: "Resistência
Física/Mágica" tinha o mesmo nome da condição **Resistência** que já existe no jogo (reduz
dano por tipo, concedida por item/habilidade). Os derivados foram renomeados pra
**Fortitude Física/Mágica** — e viraram só uma forma de dizer "use o valor cru de
Defesa/Magia aqui", não um número com fórmula própria. A ideia original de redução passiva
de dano não morreu: continua existindo, mas através da condição Resistência já existente
(concedida por item mágico ou habilidade), não embutida no atributo — evita o personagem
ganhar Vida maior E dano reduzido ao mesmo tempo só por investir num atributo.

## Sistema de Estresse (redesign completo, 2026-08-20)

**Estresse Máximo = 10 + (Nível ÷ 2) + (Sanidade ÷ 2)** — mesma forma do Mana, confirmado.
Inclui Nível pra quem não investe em Sanidade ainda ganhar alguma resiliência com a
carreira.

**Fontes de Estresse — redesenhadas do zero**, porque a regra antiga dependia do Mestre
lembrar de pedir teste no momento certo (carga mental alta) e do fumble (que não existe
mais):

- **Automáticas, de graça, sem rolagem extra (1 ponto fixo cada):**
  - Tirar **exatamente 1** no d100, em qualquer teste — **mesmo quando é sucesso/crítico**
    (todo mundo tem limiar de Sorte ≥1, então tirar 1 nunca é "ruim" no resultado, mas
    ainda representa o preço mental de escapar por pouco).
  - Sofrer um crítico.
- **Narrativas, checklist fixa de 5 (não julgamento aberto do Mestre), com rolagem
  d100+Sanidade vs DC da Tabela de Dificuldades, dado por `⌈Nível÷20⌉`d6 na falha:**
  1. Presenciar horror
  2. O próprio personagem cair a 0 de Vida
  3. Ver um aliado cair a 0 de Vida
  4. Falhar em algo que importava de verdade
  5. Matar ou ferir gravemente alguém que não devia

Calibrado pra ~6 gatilhos narrativos até o Colapso, constante em todo nível (mesma lógica
usada pra calibrar dano contra Vida) — testado contra a curva "Misto" de Sanidade
(Estresse Máximo: 17→44→73→98→110 nos checkpoints), a régua `⌈Nível÷20⌉`d6 bate de perto.

### Tabelas de referência rápida (pro Mestre, sem cálculo — uso futuro nas Regras e no
Escudo do Mestre)

**Dano Improvisado** (d10 único, escala só a quantidade — mesmo espírito do "Improvising
Damage" do D&D 5e):

| Dados | Exemplos |
|---|---|
| 1d10 | tropeço feio, mordida pequena, corte raso |
| 2d10 | golpe direto, queda de pouca altura, queimadura de tocha |
| 4d10 | ferimento sério, atropelamento, fogo direto no corpo |
| 8d10 | esmagamento, explosão próxima, queda de penhasco |
| 14d10 | desabamento, jogado numa fornalha, atingido por algo colossal |
| 20d10 | cair em lava, pisoteado por um titã, o fim de tudo |

Pra escolher a linha certa por nível, cruza com "Calibração contra Vida" (Vida÷10 é o
"golpe normal" — 2d10/4d10/8d10 cobrem a faixa 0-100; 14d10/20d10 ficam pra ameaças fora da
curva, tipo Lendários).

**Estresse Improvisado** (d6 único — é a mesma régua `⌈Nível÷20⌉`d6 da seção acima, só com
exemplos):

| Dados | Exemplos |
|---|---|
| 1d6 | um susto rápido, uma ameaça velada |
| 2d6 | testemunhar violência, ser humilhado publicamente |
| 3d6 | ver um cadáver mutilado, trair a própria palavra |
| 4d6 | perder alguém querido, ser torturado |
| 5d6 | genocídio presenciado, o próprio corpo profanado |

## Segunda auditoria (2026-08-20)

Nova varredura, focada em `exploracao.md`, `equipamento/index.md` e `mestre/encontros.md`.

1. **Fôlego — resolvido.** `1 + Vitalidade rodadas` quebrava do mesmo jeito que Movimento
   (Defesa até 100 → ~101 rodadas prendendo a respiração). **Fôlego = 1 + (Defesa ÷ 10)**
   rodadas, arredondado — mesma régua do Movimento/Rerolagens.
2. **Testes de viagem (Guiar/Vigiar/Forragear/Rastrear) — resolvido.** Usavam Sabedoria
   (atributo morto) direto, com DC antiga. Viram **Exploração** (a descrição dela já cobre
   "rastrear, se orientar, sobreviver" — encaixe direto), DC escalada ×5 (Vigiar/Forragear:
   12→60; Guiar/Rastrear: mantém "DC do terreno/rastro", só que na escala nova).
3. **Requisito de Atributo Mínimo (armas) — resolvido.** Remapeamento: Força→Ataque,
   Vontade→Social (o doc já dizia "Vontade é o substituto de Carisma"), Inteligência→Magia,
   Sabedoria→Magia (só o caso do Vajras, "foco médio" — é o lado arcano da Sabedoria antiga,
   não o de percepção, que virou Exploração). Números ×5, mesma escala da Tabela de
   Dificuldades:

   | Arma | Requisito antigo | Requisito novo |
   |---|---|---|
   | Machado | Força +2 | Ataque 10 |
   | Montante | Força +3 | Ataque 15 |
   | Alfange | Agilidade +3 | Agilidade 15 |
   | Gakkung | Agilidade +6 | Agilidade 30 |
   | Violino | Vontade +4 | Social 20 |
   | Vajras | Sabedoria +6 | Magia 30 |
   | Lâmpada | Inteligência +5 | Magia 25 |
   | Katana Nodachi/Muramasa | Força ou Agilidade +3 | Ataque ou Agilidade 15 |
   | Gládio | Força +2 e Inteligência +2 | Ataque 10 e Magia 10 |
4. **Pontos de Ameaça — confirmado, não precisa de mudança.** A fórmula
   (`Vida÷10 + dano por rodada÷5`) é uma razão entre dois números que já estão sendo
   reescalados juntos (Vida ×1,75, dano recalibrado pra acompanhar) — se autocorrige,
   contanto que o dano das criaturas realmente acompanhe a mesma proporção quando calibrado
   (mesmo trabalho de execução já registrado, não é decisão nova).

**Aviso de escopo:** essa auditoria ainda não é exaustiva — falta varrer `racas/index.md`,
`origens/index.md` e `pacotes/index.md` atrás de bônus "+X atributo" espalhados (mesmo
padrão do item 3). É varredura sistemática, do mesmo tamanho da varredura das 579
habilidades — fica pra fase de execução.

## Escopo real da migração (pra não perder de vista)

Toca em `mana.md`, as 579 habilidades (Atributo, dano, qualquer texto citando "d20" ou
"natural"), o Bestiário (Defesa, Ataque, dado de dano de 52 criaturas), `criando-criaturas.md`
e o glossário (verbetes citando "d20", "20 natural", "1 natural"). Nada disso deveria ser
tocado antes dos itens 1–4 de "Em aberto" estarem fechados — mudar fórmula e remigrar
conteúdo duas vezes é o erro que o projeto já registrou evitar (substituição em cadeia, ver
CLAUDE.md).

## Reformulação de Armaduras e Escudos (2026-08-20)

Revisão pós-Fase 2, a pedido do autor: converter os bônus antigos ×5 (o que a Fase 2 tinha
feito) não fazia sentido conceitual, porque no d20 a "Defesa" da armadura ajudava a **evitar**
ser acertado — e esse papel não existe mais como um bônus fixo depois que Evasão passou a ser
"Agilidade + item", com Agilidade escalando até 100. Rodando os números: um build ágil focado
já ultrapassa qualquer bônus fixo de armadura por volta do nível 20-30, e as armaduras pesadas
(que tentavam compensar isso com "a Evasão ignora o bônus de Agilidade") só pioravam — travavam
a própria Evasão num teto que nunca sobe.

**Decisão: Armadura e Escudo saem do mesmo eixo.**

- **Escudo continua no lado "evadir"** — soma direto na Evasão, como já fazia.
- **Armadura muda pro lado "aguentar pancada"** — sai da Evasão de vez e vira o termo
  `+ Vida de equipamento` na fórmula de [Vida Máxima](../docs/jogar/dano-e-cura.md#vida),
  no mesmo molde que `+ Mana de equipamento` já existe pra Mana. A cláusula "ignora o bônus
  de Agilidade" das armaduras pesadas caiu inteira — não precisa mais dela, porque Armadura
  não toca mais em Evasão.

**Por que não virou bônus no atributo Defesa em vez de Vida direto:** Defesa também alimenta
Fortitude Física (veneno, doença, exaustão) — uma Armadura que somasse no atributo vazaria
proteção pra esses efeitos, contrariando a regra que a Couraça Natural das criaturas já
segue ("só protege contra dano, empurrão e queda, nunca veneno, medo ou ilusão"). Ir direto
na Vida evita esse vazamento.

Números novos (não é conversão do valor antigo, é redesenho do zero, calibrado contra a Vida
base de ~30 no nível 0):

| Armadura | Vida | Preço |
|---|---|---|
| Tecido Reforçado / Couro Batido | +10 | 40 p |
| Roupas Místicas | +0 (mantém +15 de Mana Máximo, subiu de +5) | 40 p |
| Escamas / Brigandina / Cota de Malha | +20 | 100 p |
| Meia-Armadura | +35 | 250 p |
| Armadura de Cerco | +55 | 250 p |
| Placa de Torneio | +75 | 300 p |

Escudos ficaram como a Fase 2 já tinha deixado (+5/+10/+15/+25 de Evasão) — não fizeram parte
da reformulação, só a Armadura.

Efeito colateral bom: como Armadura não soma mais Evasão, ela **deixou de ser comparável**
com a Couraça Natural das criaturas (que continua só em Evasão) — os dois sistemas não
precisam mais bater na mesma escala um com o outro, o que tira uma restrição que só
atrapalhava.

Arquivos tocados: `equipamento/index.md` (tabela de Armaduras reescrita, seção reescrita),
`jogar/dano-e-cura.md` (fórmula de Vida ganhou o termo de equipamento), `jogar/mana.md`
(valor da Roupas Místicas atualizado), `jogar/combate.md` (linha da tabela de Defesa:
"Agilidade + Armadura/Couraça Natural" → "Agilidade + Escudo/Couraça Natural"),
`criacao/index.md` (mesma correção nas duas linhas do resumo de criação),
`mestre/criando-criaturas.md` (mesma correção na referência rápida do Mestre).

### Requisito de Defesa nas Armaduras, e Requisito em todas as 62 armas (2026-08-20)

Duas extensões pedidas na mesma revisão, depois da reformulação acima:

**Armaduras ganharam Requisito de Defesa mínima**, a partir da Armadura de Escamas (as três
leves — Tecido Reforçado, Couro Batido, Roupas Místicas — continuam livres): Escamas/
Brigandina/Cota de Malha em Defesa 10, Meia-Armadura 15, Cerco 20, Torneio 25. Mesma régua
×5 usada em toda parte do sistema, e faz sentido temático com o novo papel da Armadura
(Vida/"aguentar pancada") — só um corpo já resistente aproveita carregar proteção pesada de
verdade.

**Requisito de Atributo Mínimo deixou de ser exceção nas armas.** Só 9 armas tinham (de 62);
o autor pediu que a maioria ganhasse um. Resolvido mantendo **4 armas livres de propósito**
— uma "genérica" por família (**Espada** e **Manopla** em Marciais, **Arco** em Pontaria,
**Cetro** em Arcano) — pra garantir que todo personagem, mesmo espalhando os 15 pontos
livres da criação por vários atributos, sempre tenha ao menos uma opção de cada estilo
disponível desde o nível 0. As outras 58 ganharam um valor de 10 a 30, seguindo o mesmo
critério que as 9 originais já usavam ("exotismo/raridade, não peso físico"): arma comum
fica em 10, incomum/pesada de guerra em 15-20, lendária/mística/tecnológica em 20-30.
Finesse usa "ou" (Ataque ou Agilidade), Híbrida usa "e" (as duas), som/carisma usa Social.
Script aplicou as 48 linhas novas nas 3 tabelas (Marciais/Pontaria/Arcano) sem avisos.

## Fase 3 — as 567 habilidades gerais, migradas (2026-08-20)

Escopo real, contado direto nos 15 arquivos de grupo (não a estimativa de ~394 que vinha
sendo usada desde o planejamento): **567 habilidades**, em `habilidades/{pontaria,
alquimia-de-mana, percepcao-arcana, sociais, infiltracao, projecao-mental, mobilidade,
conjuracao, necromancia, espaco-tempo, suporte, debuff, marciais, buff,
magicas-elementais}.md`. Todos os 15 arquivos fechados nesta sessão.

**Método, por tipo de habilidade:**

- **Dado próprio, escrito à mão** (a maioria): boa parte tinha o **mesmo dado nas três
  Intensidades** — só o efeito secundário escalava, o dano não. Corrigido com a mesma lógica
  da Fase 2: **I = dado atual (fica igual), II = degrau acima, III = dobro da contagem no
  degrau acima** (d4→d6→d8→d10→d12→d20), usando o dado que a própria Intensidade I já tinha
  como "base" — não precisa de tabela de Grau de Poder, o dado de cada habilidade já
  carregava sua própria escala. Rodado por script que detecta o padrão automaticamente
  (extrai o primeiro XdY de cada linha de Intensidade, compara os três, aplica a fórmula só
  quando os três batem) — pego em Debuff (37 de 73), Marciais (1 de 84), Mágicas por Elemento
  (87 de 155). Onde a habilidade **já escalava** (contagem ou dado subindo por conta própria),
  o script pulou sem tocar — o design original já estava certo.
- **Dado herdado da arma equipada** ("usa o dado de dano da arma equipada", "1x/2x dado de
  dano", [Dano Desarmado](#dano-desarmado-rescalado-tambem)): **não precisou de nada** — já
  herda automaticamente os valores que a Fase 2 corrigiu.
- **Custo fixo em área** ("Acerto:" único, sem Intensidade): via de regra deixado como estava
  quando o padrão já é consistente dentro do próprio grupo — abrir esse conjunto pra
  rebalancear dano bruto vs controle garantido é um projeto à parte, não recalibração de
  escala. Dois casos long puxados pro benchmark 6d10 (◈◈◈+16 Mana, mesmo teto de
  Sentença Final/Pontaria) por destoarem muito de tudo ao redor: **Arrastar pro Abismo**
  (Necromancia, 4d10→6d10) e **Ruptura Dimensional** (Espaço-Tempo, 2d8→4d8, ela tem teste de
  ataque — as outras da família são automáticas, isso já justifica menos dano).
- **Crítico**: toda linha "Crítico (20 natural): dano máximo (N) + XdY extra... sobe 1
  Intensidade" virou "dano máximo dos dados da Intensidade usada + uma rolagem extra igual"
  — o hardcode antigo travava sempre no valor da Intensidade I, mesmo quando o crítico
  acontecia numa III. Regex resolveu ~150 linhas de uma vez (busca por "sobe 1 Intensidade"
  na mesma linha do Crítico, único jeito de distinguir de custo-fixo sem essa cláusula).

**Atributo — contexto decide, não é 1:1:**

- Inteligência → **Magia**, sempre (sem exceção — o grupo inteiro que sobrava era arcano).
- Vontade e Sabedoria → **Magia** por padrão em qualquer grupo claramente arcano/curativo
  (Percepção Arcana, Conjuração, Necromancia, Espaço-Tempo, Suporte, Buff, Debuff, Mágicas
  por Elemento — todos custam Mana pra um efeito mágico, "Magia e habilidades são a mesma
  coisa"). Vontade → **Social** só nas Habilidades Sociais em si (persuasão mundana) e em
  referências genéricas a "teste de Vontade" de um alvo sem ligação com magia declarada.
  Sabedoria → **Exploração** só quando o efeito é percepção/instinto mundano, não arcano
  (Mão Leve, Instinto Ladino, Fingir a Morte em Infiltração; Laço de Sangue e Pelo em
  Conjuração — vínculo com animal é natureza, não magia; Postura do Vazio em Marciais —
  "vê o golpe antes de chegar" é instinto, não sexto sentido arcano).
- **"Defesa: mental (Vontade)" não virou uma coisa só** — a tabela de número-alvo do
  `combate.md` já separava "controle mental de origem mágica" (**Fortitude Mágica**) de
  "manipulação social" (**Social**). Toda habilidade de Projeção Mental, Necromancia, Debuff,
  Buff e Mágicas por Elemento (efeito mental de origem mágica) foi pra Fortitude Mágica; só
  as habilidades do próprio grupo Sociais foram pra Social. **Défesa: Vitalidade (é
  veneno)** — Vitalidade já tinha virado Defesa (a atributo), e o efeito de veneno já mapeia
  pra **Fortitude Física** ("o próprio valor de Defesa") no `combate.md` — remapeamento
  direto, sem ambiguidade. Achado geral no Veneno de Mágicas por Elemento: a nota do grupo
  dizia "checam Defesa (Vitalidade) em vez de Agilidade" — virou "checam Fortitude Física em
  vez de Evasão".

**Bônus permanente de atributo — mesma régua ×5 de tudo mais.** Três Passivas de Marciais
davam **+1/+2 permanente** num atributo ao aprender (Golpe Irresistível, Corpo Primordial) —
irrisório contra pontos que já vêm em blocos de +5 por nível par. Viraram **+5/+10**. Mesmo
tratamento num efeito de Crítico em Mágicas por Elemento (Praga Definitiva: -1 até o fim do
combate em três atributos → **-5** cada). Onde a mesma lógica apareceu como **Dificuldade**
em vez de bônus de atributo (Recusa da Morte, Marciais: "DC que começa em 10, sobe 5" — um
teste de resistir à morte, repetido por cena) virou **Dificuldade 50, sobe 25**, a mesma
escala ×5 da Tabela de Dificuldades.

**Achados que iam além de recalibração de dado, resolvidos no caminho:**

- **`habilidades/regras.md` nunca tinha sido tocado.** É a página mestra de resolução — a
  que toda ficha de habilidade cita ("ver Regras de Habilidade") — e ainda dizia d20, "20
  natural é Crítico", e uma regra que **não existe mais** ("1 natural sempre falha", removida
  faz tempo do sistema geral). Reescrita a seção de Resolução inteira pro Crítico por Sorte,
  e a tabela de Tiers de Resultado (Ressuscitar, Selar o Pacto) ganhou a mesma régua ×5 que
  Selar o Pacto já tinha recebido na Fase de Conjuração (≤50/51-80/81-99/100).
- **Dano Desarmado rescalado também — em três passadas.** A tabela mestra (`marciais.md`,
  citada por dezenas de habilidades e por 6 traços raciais) escalava por nível
  **1-4/5-10/11-16/17+**, presa ao teto de nível 20 antigo, com **um dado só por faixa** —
  usado igual nas três Intensidades (as habilidades que citam "Dano Desarmado" nunca tiveram
  um multiplicador tipo "1x/2x dado" como as de arma; a escalada de Intensidade nelas mora só
  no efeito secundário, não no dado).
  1. Primeira passada: só esticar as faixas pro teto 100 (**0-25/26-50/51-75/76-100**),
     mantendo os mesmos dados (d4→d6→d8→d10). **Errado** — testado contra a Calibração
     contra Vida, o dano parava de crescer depois da primeira faixa (7→9→11→13 enquanto a
     Vida vai de 40 a 290), a mesma falha que a Fase 2 já tinha corrigido nas armas, repetida
     aqui sem eu testar.
  2. Segunda passada: tentei consertar mantendo a estrutura "dado base + Intensidade III conta
     2×" — também **errado**, por over-engineering: essa estrutura nem existe pra Dano
     Desarmado (que é um valor só, não uma escada de base/degrau), e a correção ficou confusa
     de ler sem resolver o problema de fato pra quem só quer saber "quanto eu rolo".
  3. **Versão final, do autor**: a tabela vira direto os valores-alvo já calibrados contra a
     Vida, sem dado "base" nenhum por trás — **2d6 (0-25), 2d12 (26-50), 2d20 (51-75), 3d20
     (76-100)**. Simples de ler, e são os mesmos números que a Intensidade III da versão
     anterior já mirava, só que sem a complicação de chegar lá. Traço racial de "1 grau acima"
     empurra pra faixa seguinte da tabela; no teto (76-100), não tem faixa acima — fica a
     critério do Mestre.
- **Aliados de Combate da Conjuração** (Servo de Cinzas, Corpo Provisório, Chamar Lâmina
  Espectral, Iteração Avançada, Encarnação, Guardião do Pacto) e o **Companheiro Animal**
  eram, na prática, mini-fichas de criatura que a Fase 1 (Bestiário) nunca tocou — presas nas
  mesmas faixas de nível 1-20 e na escala antiga de Vida/Ataque/Evasão. Redesenhadas do zero
  (não convertidas) contra os checkpoints de Vida de PJ já validados (40/79/134/205/290 nos
  níveis 0/25/50/75/100), como fração do grau (Menor ~25-45%, Médio ~40%, Maior ~55-65%) —
  ver detalhe na revisão de Equipamento acima, mesma sessão.
- **Um bug de conteúdo real**, não de escala: "Mão Invisível" (Projeção Mental) tinha uma
  nota final ("Custo fixo — área de 3 casas...") que não batia com o resto da habilidade
  (Intensidade normal, não é área nem custo fixo) — resíduo de copiar/colar de outra
  habilidade. Removida.

**O que ficou de fora, de propósito:** a auditoria de balanceamento fino dentro de cada grupo
(comparar Supremos entre si, tipo a auditoria dos 68 Supremos de arma que rolou antes da
migração) não foi refeita — o que mudou aqui foi escala (d20→d100, atributo, terminologia),
não redesenho de poder relativo.

## Custos de Mana ×3 (2026-08-20, depois da Fase 3)

O autor cobrou de novo o ponto que já tinha levantado antes (ver decisão anterior de manter
os custos como estavam) — e com razão: simulando um Guerreiro nível 1 (31 Mana, Magia parada
em 5), a Intensidade III do Básico de qualquer arma (6 Mana, valor puro do d20) dava **5 usos
por descanso**, e mesmo um personagem que nunca investe em Magia via o próprio pool triplicar
sozinho (31→130) só pelo `+ Nível` da fórmula — nenhum custo fixo aguenta isso sem ficar
trivial. Resolvido com a opção mais simples das duas apresentadas: multiplicar **todos** os
custos de Mana do jogo por **×3**, em cima do valor original do sistema d20 (não do valor já
ajustado por qualquer outra coisa). Fica registrado que isso **não fecha pra sempre** — o
pool continua crescendo mais rápido que um número fixo, então a mesma sensação de "sobra
Mana" deve voltar lá pelo nível 60-70; resolver de vez exigiria custo em % do Mana Máximo em
vez de número fixo, opção que o autor viu e decidiu não seguir agora.

**Escopo:** 1.761 custos multiplicados — as 186 habilidades de arma (`equipamento/index.md`,
inclusive a tabela-resumo de Grau em `mana.md` e a mesma tabela em `equipamento/index.md`) e
as 567 habilidades gerais nos 15 arquivos de grupo. Script reconhece o padrão "N PA) + N Mana"
/ "N PA + N Mana" (custo pago, sempre colado numa declaração de PA) e multiplica só o segundo
número — deixando intocado "recupera N de Mana" e "perde N Mana" (efeito sobre Vida/Mana de
terceiros, não custo de ativação). Verificado por amostragem antes de rodar em massa (1.761
casamentos, zero falso positivo/negativo nas linhas soltas de "Mana" que não bateram no
regex). Três exceções pegas à mão, fora do padrão do script: a nota de área-Especial em
`equipamento/index.md` ("◈◈◈ + 12 Mana" → 36), e duas menções de faixa em `habilidades/
regras.md` ("6-12/16+" → "18-36/48+", e "◈◈ + 9 Mana" do padrão de Avançada-de-área → 27).
`mana.md` reescrito por inteiro nas tabelas e na nota que dizia "os custos ainda não
acompanham" (removida — não é mais verdade).

**Nova tabela de Mana por grau de arma:** Básica 3/9/18, Avançada 6/15/27, Especial 9/21/36.
**Grau de Poder geral:** Menor 3-9, Moderado 12-24, Maior 27-45, Supremo 48+.
