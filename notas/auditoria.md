# Auditoria de Consistência — Prisma RPG

**Data:** 2026-07-27 · **Escopo:** os 28 arquivos de `docs/` (11.339 linhas), lidos como um corpo único pela primeira vez.

---

## Resultado em uma página

A auditoria produziu **205 achados brutos** em oito varreduras (uma transversal minha + sete por domínio). Descontadas as ~20 aparições do mesmo problema em relatórios diferentes, são **cerca de 185 achados únicos: ~36 de severidade alta, ~80 média e ~70 baixa**. Cada um está listado nas Partes 1 e 2 com arquivo, linha, severidade e confiança.

**O pior achado do sistema é um só: a condição "derrubado" não existe.** Ela é o efeito secundário mais vendido do jogo — aparece em mais de 150 pontos entre armas, elementais, debuffs e raças, é o efeito canônico da Intensidade II/III, buffs inteiros existem só pra negá-la, e o Bestiário dá bônus de dano "contra alvo já derrubado" — mas nenhuma linha em lugar nenhum diz o que estar derrubado faz, quanto custa levantar, ou como interage com ataques. Metade do valor das Intensidades pagas em Mana e PA aponta pra uma regra que não foi escrita. E o nome ainda colide com "Caído", que significa "a 0 de Vida, morrendo".

**O segundo pior é estrutural: existe um sistema paralelo de habilidades "automáticas, sem teste" que ninguém autorizou.** A regra só isenta de rolagem buffs, cura e Supremas inevitáveis — mas ~25 habilidades comuns de Debuff e Elementais se declaram "(efeito automático, sem teste de ataque)" e ignoram a Defesa que todas as vizinhas pagam pra testar. O caso extremo: Zona Cinzenta atordoa um dragão Lendário com 100% de chance por 6 Mana, enquanto quem rola paga mais e pode errar. Isso desativa os dois pilares do sistema (Defesa e Intensidade) ao mesmo tempo.

**O terceiro: os números finos estão certos e os encaixes entre páginas, não.** Verificação mecânica confirmou zero violações de PA = Intensidade e zero escadas de Mana fora do padrão em todo o sistema — mas as páginas discordam entre si sobre o que buffs são (mana.md diz Custo fixo, habilidades/index.md diz Intensidade), sobre quanto custa uma Reação (a tabela de PA diz 1, o texto da mesma página diz outra coisa), e sobre quanto Estresse um crítico gera (nenhuma diz).

O que **se confirmou sólido** também importa e está na Parte 3: dados de dano 100% consistentes, zero âncoras quebradas, zero referências de nome quebradas nos 100 pacotes (~1.100 checagens), matemática de Defesa do Bestiário fechando ficha a ficha, e descanso idêntico nos três arquivos que o descrevem.

**Situação atual:** depois da auditoria, você autorizou a aplicação das correções. **A maior parte já foi aplicada** — ver a [Parte 4](#parte-4--o-que-foi-corrigido), que registra o que mudou, as decisões de design que precisei tomar, e o que ficou pendente da sua palavra. As três verificações mecânicas passam limpas: zero anomalias de custo/PA, zero rótulos de grau fora da faixa, zero âncoras quebradas, e as 1.000 linhas de trilha dos 100 pacotes seguem sem referência quebrada. Nenhum commit foi feito.

---

## Método e cobertura

- **Varredura transversal (minha):** regras-base, glossário, termos usados-mas-nunca-definidos, verificação mecânica por script de (a) PA = Intensidade e escadas de Mana em todos os arquivos de habilidade, (b) rótulo de Grau de Poder vs teto de Mana, (c) âncoras de todos os links internos.
- **Sete varreduras por domínio (subagentes):** Arsenal (62 armas × 3), Mágicas Elementais (11 elementos), Marciais+Pontaria+Infiltração+Mobilidade, Buff+Debuff+Suporte+Sociais+Mágicas Básicas, Raças+Origem+Tocado, os 100 Pacotes (extração automatizada de ~1.100 nomes), e o Livro do Mestre (com recontagem das matemáticas de encontro).
- Cada achado exigiu as duas pontas com arquivo:linha. Cálculos que não fecharam mostram os números.
- IDs: TRA (transversal), ARS (arsenal), ELE (elementais), COM (combate), APO (apoio), PER (personagem), PAC (pacotes), MES (mestre).

---

## Parte 1 — Os doze problemas estruturais

Estes são os achados que atravessam arquivos. Cada um consolida aparições de vários relatórios.

### 1. "Derrubado" não existe — a maior dívida do sistema
**Severidade: alta · Confiança: alta** · [TRA-01 = ARS-03 = COM-01 = MES-02 = ELE-01]

- Usam a condição: [arsenal.md](../docs/jogador/arsenal.md) (117+ vezes), [magicas-elementais.md](../docs/habilidades/magicas-elementais.md) (assinatura de Terra, Água e Vento — linhas 16-18, 35-37, 1245, 1318…), [debuff.md:248](../docs/habilidades/debuff.md:248), [marciais.md](../docs/habilidades/marciais.md) (~50 vezes).
- Assumem que ela existe: [bestiario.md:252](../docs/mestre/bestiario.md:252) ("Contra alvo já derrubado, **2d8** em vez de 1d8"), [bestiario.md:191](../docs/mestre/bestiario.md:191) (Aranha "não pode ser derrubada"), [racas/index.md:53](../docs/racas/index.md:53) e [:195](../docs/racas/index.md:195) ("não pode ser derrubado"), [buff.md:44-46](../docs/habilidades/buff.md:44) (Postura Inabalável existe só pra negar derrubar), [encontros.md:67](../docs/mestre/encontros.md:67).
- Não existe: entrada no glossário, custo pra levantar, efeito sobre ataques. "Caído" ([sistema-d20.md:137](../docs/jogador/sistema-d20.md:137)) é outra coisa — 0 de Vida.
- **Na mesa:** o jogador paga a Intensidade II/III, derruba o chefe, e pergunta "e daí?". O livro não responde — e o Bandido do Bestiário cobra em dados uma condição que não tem conteúdo.

### 2. O sistema paralelo de habilidades "automáticas, sem teste"
**Severidade: alta · Confiança: alta** · [APO-04 + ELE-04 + ELE-08 + ELE-09 + ELE-22 + PER-18 + APO-26]

A regra ([habilidades/index.md:96](../docs/habilidades/index.md:96)) só dispensa rolagem pra buffs, cura e "efeitos automáticos como uma Habilidade Suprema inevitável". Mas ~25 habilidades comuns se declaram "(Sem Intensidade — efeito automático, sem teste de ataque)":

- **Zona Cinzenta** ([debuff.md:424-431](../docs/habilidades/debuff.md:424)): Atordoado + 2d6 automáticos por ◈◈ + 6 Mana, sem rolar — contra qualquer Defesa, inclusive Lendária.
- **Astrape Sombria** ([magicas-elementais.md:213-220](../docs/habilidades/magicas-elementais.md:213)): Atordoado automático em até 5 alvos por 2 PA + 7 — mais barato que o Relâmpago III (3 PA + 8), que rola e pega menos.
- **Investida Encadeada** ([magicas-elementais.md:152-159](../docs/habilidades/magicas-elementais.md:152)): 1d10 + Atordoado em raio 3, automático, 9 Mana — supera a Suprema de 16 do próprio Gelo.
- **Marca Fatal** (3d6 automáticos, 6 Mana), **Chuva de Sangue** (raio 3 automático pelos mesmos 3 PA + 8 que o Esquife de Ossos paga rolando), **Névoa Sangrenta**, **Enterrar**, **Dominação: Enfraquecer**, **Escuridão Absoluta**, **Espada Vingadora**, **Dança Encantadora**, **Provocação** (controle mental automático em 3 alvos por 5 Mana, dominando o Manipular rolado de Sociais), **Língua Presa** (traço racial que puxa inimigo sem teste), **Lacaio Reanimado** (ataca sem teste e nem tem Defesa própria). Lista completa: ELE-08 e APO-04 na Parte 2.
- **Na mesa:** contra alvos de Defesa alta, o jogador racional abandona tudo que rola dado. A Base de Resiliência — o que torna um Lendário difícil de afetar — deixa de existir contra essa classe de habilidade.

### 3. Custo fixo virou zona franca — três regras violadas ao mesmo tempo
**Severidade: alta · Confiança: alta** · [COM-13/14/15 + APO-17/18/31 + ELE-08 + ARS-05]

A regra ([mana.md:32](../docs/jogador/mana.md:32), [habilidades/index.md:49-55](../docs/habilidades/index.md:49)) diz: Custo fixo é só pra raio 3+, Supremas e efeitos absolutos, cobrando **o valor da Intensidade III**.

- **Cobram menos que a III:** Caminho da Espada (3), Dança Élfica (3), Postura da Sombra (4), Desaparecimento (5), Fumaça Cega (5), Reforço Momentâneo (3 — mais barato e mais forte que a Postura Inabalável I, que custa 4 e protege menos) — os valores de III do sistema começam em 6.
- **PA sem padrão nenhum:** Marciais usa ◈◈◈ nos fixos; Infiltração usa ◈◈ e até ◈; Reforço usa ◈. Comparação direta: Esquife de Ossos (raio 3) = ◈◈◈ + 8; Onda de Choque (raio 3) = ◈◈ + 9. E nove Avançadas de área do arsenal cobram ◈◈ + 9 num padrão uniforme que nenhuma regra descreve ([ARS-05]).
- **Não se qualificam:** Névoa Sangrenta (raio 2), Enterrar (1 casa), Marca Fatal (1 alvo), Zona Cinzenta (1 alvo), Chama Amaldiçoada (1 criatura), Fumaça Cega (raio 2), e mais uma dúzia — efeitos graduáveis, sem serem Supremas nem raio 3+ (lista completa: ELE-08, APO-18, COM-15).
- **Na mesa:** impossível precificar habilidade nova ou julgar as existentes; e as fixas costumam sair mais baratas que a III das graduadas equivalentes — o oposto da intenção.

### 4. Buffs têm Intensidade ou são Custo fixo? As páginas-base se contradizem
**Severidade: alta · Confiança: alta** · [TRA-10 = COM-04 = ELE-15]

[mana.md:32](../docs/jogador/mana.md:32) inclui "buffs" na lista de Custo fixo, sem qualificação. [habilidades/index.md:57-70](../docs/habilidades/index.md:57) dedica uma seção inteira ao contrário ("Buffs, Suporte e Mobilidade também têm Intensidade"). O CLAUDE.md diz "buffs **sem rolagem**" — o qualificador se perdeu em mana.md. Consequência: buff.md escala quase tudo por Intensidade, enquanto Couraça de Pedra, Véu de Vapor, Passos do Vento, Pacto de Sangue (elementais), Caminho da Espada (marciais), Desaparecimento e Fumaça Cega (infiltração) vieram fixos — o jogador de buff.md paga 3 degraus pelo que o de infiltracao.md leva por preço único.

### 5. O vocabulário informal nunca foi definido
**Severidade: alta (conjunto) · Confiança: alta**

| Termo | Usos | Onde deveria estar | Achado |
|---|---|---|---|
| **"rodada"** | 245 | nenhuma definição; convive com "turno" (condições duram "até o fim do próximo turno") | TRA-03 |
| **Vantagem/Desvantagem** | 87 | definida SÓ em [testes.md:88-92](../docs/mestre/testes.md:88) (Livro do Mestre) — que inclusive contém a regra "não acumulam", invisível pro jogador | TRA-02 = MES-15 |
| **"agarrado"** | [tocado.md:76](../docs/jogador/tocado.md:76), [infiltracao.md:65](../docs/habilidades/infiltracao.md:65) | nenhuma regra de agarrão existe (Chicote "prende" sem mecânica) | TRA-07 |
| **"Desprevenido" / "surpreendido"** | [origem.md:22](../docs/jogador/origem.md:22), [exploracao.md:47](../docs/mestre/exploracao.md:47), [bestiario.md:236](../docs/mestre/bestiario.md:236) | nenhuma regra de surpresa; Vigiar nem tem DC | TRA-05 = PER-01 = MES-07 |
| **"efeitos de Medo"** | [origem.md:60,75](../docs/jogador/origem.md:60) | nenhuma mecânica rotulada Medo | TRA-06 |
| **"cena" / "combate"** (recarga) | Rugido, Casco, Gladiador, Treinado por um Mestre | "cena" nunca definida; traços gêmeos usam relógios diferentes | PER-27 |
| **"doença"** | [racas/index.md:78,115](../docs/racas/index.md:78) | nenhuma doença existe no jogo | PER-20 |
| **água/nado** | 8+ traços cancelam penalidades aquáticas | exploracao.md não tem seção de água — a penalidade cancelada não existe | PER-04 |
| **Voo** | 3 raças voam ([racas:77,128,233](../docs/racas/index.md:77)); Mobilidade anuncia "Voo" sem ter; [mana.md:43](../docs/jogador/mana.md:43) chama voo sustentado de Supremo | queda, Atordoado no ar, derrubar voador, alcance contra quem voa: tudo indefinido | COM-10 = PER-12 |
| **"Petrificado"** | crítico de Petrificar ([elementais:38](../docs/habilidades/magicas-elementais.md:38)) | única ocorrência em docs/, sem definição | ELE-12 |
| **facing ("para trás", "à frente")** | [mobilidade.md:24](../docs/habilidades/mobilidade.md:24), [marciais.md:191,287](../docs/habilidades/marciais.md:191) | jogo não tem orientação de miniatura | COM-33 |

**Na mesa:** é a categoria inteira que produz o cenário que você temia — a sessão travada esperando uma resposta que o livro não dá.

### 6. Marcado não dispara, e "perde a próxima Reação" não tem prazo
**Severidade: média · Confiança: alta** · [TRA-04 = ARS-12 = APO-15 + COM-34 + ARS-20]

- **Marcado** ([glossario.md:38](../docs/glossario.md:38)): "o próximo ataque de um aliado contra ele **neste turno**". Aplicado no turno de quem ataca — turno em que nenhum aliado age. A janela só existe se "turno" significar "rodada" (ver problema 5). O efeito-assinatura da Básica do Arco evapora antes de qualquer aliado agir.
- **"Perde a próxima Reação"** (117+ ocorrências): sem prazo (se o alvo não reagir nesta rodada, fica devendo pro resto do combate?) e sem dizer se bloqueia as Reações **dedicadas**, definidas como "sempre disponíveis" ([pontos-de-acao.md:18](../docs/jogador/pontos-de-acao.md:18)).

### 7. Acúmulo e sobreposição: só tem regra onde alguém lembrou de escrever
**Severidade: alta (conjunto) · Confiança: alta** · [ARS-11 = APO-13 + ELE-07 + ELE-23 + APO-07 + PER-09 + APO-28]

- **Sangrando** — a condição mais distribuída do jogo — não tem cláusula de reaplicação/substituição (Queimando e Escudo têm), e ganhou variantes de 2d4/3d4 em pelo menos 12 habilidades. Dois Sangrandos no mesmo alvo: soma, substitui, renova?
- **Zonas persistentes** de Fogo, Raio, Água, Sangue e Espaço-Tempo (10+) não são "Zona Amaldiçoada", e a regra de não-soma ([glossario.md:84](../docs/glossario.md:84)) está amarrada a Sombras. Leitura literal: três zonas empilhadas = 3×1d6 automáticos por rodada. E várias zonas ferem "só hostis", contrariando a filosofia declarada da zona ("fere todo mundo... não é dano grátis", [glossario.md:82](../docs/glossario.md:82)).
- **Bônus planos de buffs diferentes** (Bênção Divina +3, Aura de Ataque +3, Hora da Dança +3, Totem +3, Aumento Sombrio +4…): nenhuma regra de empilhamento. Um grupo de 4 pode somar +10 de dano plano por ataque — o que detona o problema conhecido de escala de dano. A Bênção Divina define acúmulo consigo mesma, provando que o conceito existe e foi só esquecido pros demais.
- **Resistência dupla ao mesmo tipo** (Terras Vulcânicas + Tocado pela Chama + Sangue-de-Dragão): metade, um quarto, ou vale uma? Só Resistência+Vulnerabilidade tem regra.
- **Escudo dentro de buff de várias rodadas** (Bênção Divina): dura o prazo do buff ou o default de condição?

### 8. Resolução de área e Crítico em Custo fixo: os procedimentos não existem
**Severidade: média · Confiança: alta** · [COM-22 = APO-32 + ELE-11]

- A Resolução ([habilidades/index.md:87-92](../docs/habilidades/index.md:87)) só descreve 1 contra 1. Multi-alvo: uma rolagem contra a Defesa de cada um, ou uma rolagem por alvo? O 20 natural crita contra todos? Diverge na primeira área da campanha.
- [index.md:92](../docs/habilidades/index.md:92) diz que Crítico em Custo fixo dá "apenas o bônus de dano" — mas ~25 linhas de crítico de fixas entregam efeitos extras (derruba todos, Atordoado, Terreno Difícil), e duas critam **pior** que o próprio acerto (Chuva Gélida, Colheita Vermelha).

### 9. O preço não conversa entre vizinhos
**Severidade: alta (conjunto) · Confiança: alta** · [ELE-06 + APO-06 + COM-05/06/07 + ARS-14/15 + ELE-24 + APO-09/24/25/27/36 + ELE-10 + COM-24/25/26 + COM-16 + APO-19]

Cada habilidade foi precificada isolada; ninguém varreu os vizinhos. Os padrões:

- **Clones com preços diferentes:** Bomba Shuju (4/7/10) = Correntes de Água (2/5/8); Picada Tóxica (4/7/10) = Toque Debilitante (2/5/8); Etiqueta do Mordomo (2/5/8) = Arrasador (3/6/9), linha por linha; Punho Flamejante (3/6/9) = três investidas de Fogo (2/5/8); Lança Espiritual (2d6, linha 10, 2/5/8) melhor E mais barata que Lança de Fogo (1d8, linha 12, 3/6/9). Lista completa em ELE-06.
- **Área e dado dobrado de graça:** em Marciais, 1/3/6 compra 1 alvo (Corte Duplo) ou uma linha de 8 casas (Espada do Infinito, Onda Lunática) ou dano 2x (Hanuman) — o mecanismo de escala inflada previsto em mana.md:30 quase não foi usado, e quando foi, foi no lugar errado (Chute Navalha paga 2/5/8 por um clone do Ataque Desarmado de 1/3/6). No arsenal: Martelo Básica acerta adjacentes pelo preço que o Machado paga por 1 alvo; Balista Básica varre linha de 12 pelo custo unitário da Metralhadora.
- **Pontaria taxada duas vezes:** as gerais usam dados fixos pequenos e escalas infladas (Investida Certeira 1/4/7 com 1d6 — menos que o Ataque Básico grátis de Arco) enquanto Marciais dá dado da arma por 1/3/6, inclusive à distância (alcance 8 de graça).
- **Supremas desiguais:** pelos mesmos 16 Mana, Chamas Espirituais acerta 1 alvo aleatório e Raios e Relâmpagos acerta o campo inteiro; Liberação de Poder (16) é estritamente pior que Superaquecimento III (10); Olho Maligno (16) perde pro Foco Sombrio (9); das três Supremas marciais idênticas, a de menor raio é a única que acerta aliados.
- **Dominâncias internas** (o par melhor custa igual ou menos): Mergulho Furioso > Combo Punitivo, Fúria das Lâminas > Corte Cruzado (mesmos kits!), Postura da Sombra > Cambalhota, Garra Demoníaca II > Antigravidade III, Impacto Divino > Força Perfeita, Reparo de Campo < Escudo Mágico, Cura > Bênção Alquímica, Dominação < Aura de Ataque, Confete Explosivo pagando 4/7/10 por metade da Etiqueta de 2/5/8.
- **Escala 1/4/7** usada por 3 habilidades não pertence a nenhuma família documentada (COM-17).

### 10. Rótulos de Grau de Poder descolados do teto de custo
**Severidade: média · Confiança: alta** · [TRA-15/16 = ELE-13 + APO-10 + COM-36]

Verificação mecânica: 12 habilidades rotuladas fora da própria faixa — dez "(Maior)" com teto 8 (faixa Moderado) e duas "(Maior)" com teto 16 (faixa Suprema: Transformação da Deusa, Avatar Nephilim). Além delas: Enxame Flamejante e Zona de Paz chegam a 16 na III **com** escada de Intensidade (a regra diz que 16+ é Custo fixo); dezenas de habilidades com teto 9-11 não têm rótulo nenhum; "Golpe Supremo" tem "Supremo" no nome sendo Moderado; e o rótulo aparece em 2 fichas de pontaria e some das irmãs de mesmo teto. O Grau de Poder é a régua declarada de frequência de uso — hoje ela informa errado nos dois sentidos.

### 11. A remoção dos Tiers (2026-07-26) deixou cadáveres
**Severidade: alta · Confiança: alta** · [COM-02 + COM-03]

- **Dança Élfica** ([pontaria.md:13-14](../docs/habilidades/pontaria.md:13)) referenciava "os tiers da Rajada de Flechas" — sistema removido; era **irresolvível** em mesa. *(Corrigida na amostra — Parte 4.)*
- **Choque das Sombras** e **Armadilha Oculta** ([infiltracao.md:13,32](../docs/habilidades/infiltracao.md:13)) mandavam aplicar "o efeito correspondente ao tier obtido". *(Corrigidas na amostra.)*
- Vale um grep por "tier" fora de `mestre/` a cada refatoração futura.

### 12. Regra duplicada em dois lugares sempre derivou
**Severidade: média (conjunto) · Confiança: alta** · [MES-12/13/14 + TRA-08/09/12 + MES-04/06 + PER-08]

Onde uma regra vive em duas páginas, as cópias divergiram; onde vive numa só, nada quebrou (descanso, DCs, Defesa — íntegros nos 3 arquivos):

- **Exaustão:** glossário ("cada dia", sem carência) vs exploracao.md ("a partir do segundo dia"); a tabela de descanso remove Exausto sem a ressalva "causa resolvida" que o texto põe 58 linhas depois.
- **Estresse:** automático no 1 natural em [sistema-d20.md:263](../docs/jogador/sistema-d20.md:263), "se o Mestre pedir" em [testes.md:36](../docs/mestre/testes.md:36) — e a **quantidade** por crítico sofrido/1 natural não existe em lugar nenhum (a Katana Muramasa teve que definir "1 ponto" por conta própria).
- **Tabela de PA vs texto da mesma página:** [pontos-de-acao.md:12](../docs/jogador/pontos-de-acao.md:12) lista "Reação — ◈ (1)", mas as linhas 16-18 dizem que Reação custa o PA normal da habilidade (1-3) ou zero (dedicadas). A linha da tabela não corresponde a nenhum caso.
- **Equipamento inicial:** [sistema-d20.md:11](../docs/jogador/sistema-d20.md:11) dá só "a arma, escolhida livremente"; [introducao.md:55](../docs/jogador/introducao.md:55) dá "arma, armadura, e 50 de prata". Armadura de graça? Qual? Arma de 200p inclusa?
- **Quantos golpes mata um Comum:** [bestiario.md:68](../docs/mestre/bestiario.md:68) diz 1; [encontros.md:38,49](../docs/mestre/encontros.md:38) diz ~2; a conta dos 12 goblins (encontros.md:53: 12÷(12×0,75) ≈ 1,3 rodadas) só fecha com 1. Dado real: Ataque Básico 1d8 ≈ 4,5 vs 8 de Vida = 2 golpes.

---

## Parte 2 — Achados por domínio

Os relatórios completos de cada varredura, com o texto integral de cada achado, estão em `notas/auditoria-anexos/` (um arquivo por domínio). Abaixo, todos os achados que **não** foram absorvidos pelos doze problemas estruturais acima, uma linha cada.

### Arsenal (21 achados: 4 alta, 11 média, 6 baixa)

- **[ARS-01] alta/alta** — Guardião Invocado (Manopla Mística Especial, [arsenal.md:1696](../docs/jogador/arsenal.md:1696)): custo fixo de **3 Mana** onde a escala de Especial manda 12, com 3d8 de dano automático sem teste. *(Corrigido na amostra.)*
- **[ARS-02] alta/alta** — Espada Senciente, Golpe Colossal ([arsenal.md:809](../docs/jogador/arsenal.md:809)): **Atordoado na Intensidade I** (1 PA + 3 Mana + 2d12) — o efeito canônico de III pela metade do preço de qualquer equivalente.
- **[ARS-04] alta/alta** — Chicote, Chicotada em Arco ([arsenal.md:639-640](../docs/jogador/arsenal.md:639)): Intensidade II **idêntica** à I por mais que o dobro do custo.
- **[ARS-06] média/alta** — Punhal: a seção Efeito Especial ([arsenal.md:146](../docs/jogador/arsenal.md:146)) promete Ferimento Amaldiçoado "na III/Crítico"; a ficha aplica na II ([:2195](../docs/jogador/arsenal.md:2195)); e a III melhora um "Sangrando" que a habilidade não aplica. Relacionado: [TRA-11] — "não cicatriza por cura normal" vs "como Sangrando" (efeito de uma vez só): qual é o curso da ferida?
- **[ARS-07] média/alta** — Módulo Alado "não é empunhado" viola "toda arma tem exatamente uma de Leve/Duas Mãos" ([arsenal.md:106 vs :27,110](../docs/jogador/arsenal.md:106)). Pode equipar Espada junto? Escudo?
- **[ARS-08] média/alta** — Glossário chama Módulo Alado e Manopla Mística de "arma marcial" ([glossario.md:239,363](../docs/glossario.md:239)); o arsenal as lista como Arcano atacando com Inteligência.
- **[ARS-09] média/alta** — Sete armas "em par" (Pistolas, Sabres, Adagas, Garras, Tonfas, Bestas, Rapiers) têm a chave **Leve** ("mão secundária livre") sendo pares que ocupam as duas mãos. Sabres + Escudo Pesado: pode?
- **[ARS-10] média/alta** — Em ~14 habilidades de salto/investida, o deslocamento do usuário aparece **só na Intensidade I**; II/III reescrevem tudo menos ele (ex.: Crítico X, [arsenal.md:766-768](../docs/jogador/arsenal.md:766)). Idem Filo da Alma em elementais [ELE-28].
- **[ARS-13] média/alta** — Terreno Difícil criado por habilidade (Chuva de Flechas [:294](../docs/jogador/arsenal.md:294), Círculo da Perdição [:611](../docs/jogador/arsenal.md:611)) sem duração nem extensão declaradas.
- **[ARS-14] média/média** — Pique Básica II dá **2d10** onde as cinco irmãs de 1d10 dão 1d10, mesmo custo ([arsenal.md:2019](../docs/jogador/arsenal.md:2019)).
- **[ARS-16] baixa/alta** — Adagas, Corte Impactante: linha de Crítico congelada nos valores da I. *(Corrigido na amostra.)*
- **[ARS-17] baixa/alta** — Tridente, Puxão das Profundezas: "puxa 3 casas" duplicado na I; Lento some na II. *(Corrigido na amostra.)*
- **[ARS-18] baixa/alta** — Espingarda, Sentença de Hades: "ignora Armadura" duas vezes na mesma linha. *(Corrigido na amostra.)*
- **[ARS-19] baixa/média** — Égide: o escudo do pacote dá bônus de Defesa e habilita Bloqueio? Texto não afirma nem nega ([arsenal.md:73,118](../docs/jogador/arsenal.md:73)).
- **[ARS-21] baixa/alta** — Lâmina do Crepúsculo tem cláusula de Risco ([arsenal.md:1357](../docs/jogador/arsenal.md:1357)) mas não aparece na lista/chave "Efeito Especial" ([:64,142-149](../docs/jogador/arsenal.md:142)).
- Absorvidos pela Parte 1: ARS-03 (§1), ARS-05 (§3), ARS-11 (§7), ARS-12 (§6), ARS-15 (§9), ARS-20 (§6).

### Mágicas Elementais (34 achados: 8 alta, 16 média, 10 baixa)

- **[ELE-02] alta/alta** — Aceleração Temporal ([elementais:1554-1561](../docs/habilidades/magicas-elementais.md:1554)): paga **2 PA + 9 Mana pra ganhar +1 PA "neste turno"** — efeito líquido negativo; a habilidade se auto-anula.
- **[ELE-03] alta/alta** — Impacto Profundo ([:637-646](../docs/habilidades/magicas-elementais.md:637)): "todas as criaturas hostis **no campo de batalha**" com Intensidades desde 1 PA + 3 Mana (2d6 + Queimando em todos) — viola a regra de raio 3+ e supera a Suprema Julgamento Caótico (16 Mana).
- **[ELE-05] alta/alta** — Lâmina de Sangue ([:1447-1457](../docs/habilidades/magicas-elementais.md:1447)): II idêntica à I custando mais sangue; escala contradiz a assinatura (metade/total/dobrado); sem a linha de Risco que a assinatura declara obrigatória. *(Corrigido na amostra.)*
- **[ELE-09] média/alta** — Investida Encadeada: além do automático (§2), Atordoado é assinatura do **Raio** — o Gelo entrega o degrau acima da própria assinatura (Imóvel) e engole o nicho do vizinho. Idem [ELE-20] (Detonação de Choque dá Atordoado onde Nevasca, mesmo preço/forma, dá Imóvel) e [ELE-21] (Sombras empurra, dá Lento, Sangrando e Atordoado — os verbos de Vento, Gelo e Raio).
- **[ELE-14] média/alta** — Espalhamento do Queimando (~20 habilidades de Fogo): quem escolhe a criatura adjacente? Pega **aliados**? Encadeia na III?
- **[ELE-16] média/alta** — Esferas Sombrias I: cláusula de dreno **duplicada** na mesma linha. *(Corrigido na amostra.)*
- **[ELE-17] média/alta** — Buraco Negro: dois teleportes contraditórios colados na I; a identidade (puxar pra junto do usuário) some na II/III. *(I corrigida na amostra; II/III pendem de decisão sua.)*
- **[ELE-18] média/média** — Chuva de Espinhos Vermelhos III: dois drenos empilhados sem regra de soma. *(Corrigido na amostra.)*
- **[ELE-19] média/alta** — Praga Definitiva, crítico: "-1 em todos os atributos físicos" sem duração nem definição de "atributos físicos".
- **[ELE-22] média/alta** — Lacaio Reanimado: invocação **sem Defesa**, ataque automático sem teste, sem limite de lacaios simultâneos (6 Mana reutilizável).
- **[ELE-25] baixa/alta** — Selo Sombrio e Bolha Temporal reinventam Imóvel e Lento sem os nomes — imunidades e remoções de condição pegam?
- **[ELE-26] baixa/alta** — Gelo/Água acertando alvo Queimando: apaga o fogo? Nenhuma ficha dos dois elementos diz.
- **[ELE-27] baixa/alta** — Soco Ígneo e Punho Escaldante sem linha de **Alcance** (adjacente ou 8 casas?).
- **[ELE-29] baixa/alta** — Rider "perde 2 Mana" (~10 habilidades de Sombras) é nulo contra Comuns/Treinados, que não têm Mana ([bestiario.md:91](../docs/mestre/bestiario.md:91)).
- **[ELE-30] baixa/alta** — Críticos incompletos: Tremor (Terreno Difícil onde/quanto tempo?), Ira do Rei (puxa sem direção), Fúria do Vendaval (acerto **empurra 6** / crítico **puxa 2**).
- **[ELE-31] baixa/alta** — Duplicatas exatas com nomes diferentes (Força de Choque = Descarga Carregada; Voragem = Libertação Limitada; Vórtice das Trevas = Frenesi Sombrio; 3 investidas de Fogo) — fábrica de futuros pares com preços divergentes.
- **[ELE-32] baixa/média** — Petrificar domina Fúria da Natureza (mesma entrega e custo, área maior e à distância).
- **[ELE-33] baixa/média** — Choque Maligno (e Esfera Voraz, Rajada Sombria): o "dreno crescente" prometido pela assinatura de Sombras estaciona na II.
- **[ELE-34] baixa/alta** — Luz exige INT em metade das habilidades e SAB na outra metade, sem critério declarado; Chamas Espirituais é a única de Fogo em SAB.
- Absorvidos pela Parte 1: ELE-01 (§1), ELE-04/08 (§2 e §3), ELE-06/10/20/24 (§9), ELE-07/23 (§7), ELE-11 (§8), ELE-12 (§5), ELE-13 (§10), ELE-15 (§4), ELE-28 (=ARS-10).

### Marciais, Pontaria, Infiltração, Mobilidade (37 achados: 9 alta, 18 média, 10 baixa)

- **[COM-08] alta/alta** — Chute do Vento Cortante ([marciais.md:158,160](../docs/habilidades/marciais.md:158)): "se derrubar 1 alvo, recupera 3 Mana" — e a II (3 Mana) derruba automaticamente ao acertar. AoE de até 4 alvos com **custo líquido zero** todo turno.
- **[COM-09] alta/alta** — Destruição II ([marciais.md:242](../docs/habilidades/marciais.md:242)): Atordoado por 2 PA + 3 Mana, enquanto Empalar, Golpe da Alma e Ataque Frenético cobram a III inteira pelo mesmo — e as Supremas de 16 só derrubam.
- **[COM-11] média/alta** — Mão Infinita: III idêntica à II, reordenada ([marciais.md:398-399](../docs/habilidades/marciais.md:398)). Um Crítico na II "sobe" pra lugar nenhum.
- **[COM-12] média/alta** — Escapista ([infiltracao.md:65-68](../docs/habilidades/infiltracao.md:65)): diz "como Reação" (critério de dedicada = 0 PA) mas cobra ◈/◈◈/◈◈◈.
- **[COM-18] média/alta** — Armadilha Oculta: o teste ao armar rola contra a Defesa de **quem**, se não há alvo? Um Crítico ao armar sobe Intensidade contra quem pisar depois?
- **[COM-19] média/média** — Choque das Sombras: a detonação atrasada pega quem estava na área do lançamento ou quem está lá na detonação (uma rodada inteira depois)?
- **[COM-20] média/alta** — Lento/Imóvel vs deslocamentos de habilidade e auto-teleporte: o glossário isenta "teleportar" no contexto de força externa; Passo Sombrio é auto-teleporte por vontade própria — o mago prende o ladino e ele sai? Sustenta as duas leituras.
- **[COM-21] média/alta** — Montaria de Guerra ([mobilidade.md:65-67](../docs/habilidades/mobilidade.md:65)): buff sem duração ("enquanto montado" — o dia inteiro por 4 Mana?) e corcel sem Vida/Defesa/ocupação de casa.
- **[COM-27] média/média** — "Ataques que exijam vê-lo" (Desaparecimento, Fumaça Cega) nunca definido; não existe procedimento de esconder-se **dentro** do combate; nada conecta invisibilidade à condição do Golpe Furtivo.
- **[COM-23] média/alta** — [exploracao.md:100](../docs/mestre/exploracao.md:100) aponta pra "Sentidos Apurados" — a habilidade se chama **Instinto Ladino** ([infiltracao.md:95](../docs/habilidades/infiltracao.md:95)). Renomeação que vazou.
- **[COM-28] baixa/alta** — Armadilha Oculta III: "derruba o alvo" duas vezes na mesma linha; sem o duplicado, III = II. *(Corrigido na amostra: dedupe + rider padrão de III.)*
- **[COM-29] baixa/alta** — Golpe Furtivo: Crítico fixa "+2d6" ignorando a Intensidade paga.
- **[COM-30] baixa/alta** — Tiro Colossal III: "derruba **todos**... e **ele** perde a próxima Reação" — plural vira singular; nega 1 Reação ou 4?
- **[COM-31] baixa/média** — Gerais de Pontaria não exigem arma nenhuma: "Sentença Final" (3d8, flavor de armas de fogo) funciona de mãos vazias.
- **[COM-32] baixa/alta** — A chave "Marciais - Especial" linka pro grau de arma "Especial" (3/7/12) do glossário, mas as gerais assim marcadas custam 1/3/6 — o link ensina o preço errado.
- **[COM-35] baixa/média** — Empurrões/puxões de até 7 casas sem regra de colisão (parede, criatura, precipício, entrada involuntária em zona).
- **[COM-37] baixa/média** — Arrombamento I: paga 1 PA da habilidade E "a Ação Básica inteira"? Segunda cobrança ou descrição do mesmo custo?
- Absorvidos pela Parte 1: COM-01 (§1), COM-02/03 (§11), COM-04 (§4), COM-05/06/07/16/24/25/26 (§9), COM-10 (§5), COM-13/14/15 (§3), COM-17 (§9), COM-22 (§8), COM-33/34 (§5/§6), COM-36 (§10).

### Buff, Debuff, Suporte, Sociais, Mágicas Básicas (37 achados: 8 alta, 17 média, 12 baixa)

- **[APO-01] alta/alta** — Atordoado na Intensidade I por 3-4 Mana: Domador da Natureza ([debuff.md:486](../docs/habilidades/debuff.md:486)) e Fenda Dimensional ([debuff.md:287](../docs/habilidades/debuff.md:287)) — enquanto Repouso Forçado cobra ◈◈◈ + 9 pela mesma coisa. Junto com ARS-02, COM-09, ELE-04, ELE-09 e PER-05, forma o padrão "Atordoado fora do degrau III".
- **[APO-02] alta/alta** — Fenda Dimensional: II = I (texto duplicado), III empurra o que acabou de puxar, e **a casa do portal nunca é definida**. *(Texto duplicado corrigido na amostra; o resto pende.)*
- **[APO-03] alta/alta** — Catástrofe (Suprema, 16 Mana, [debuff.md:448](../docs/habilidades/debuff.md:448)): a linha de Acerto era "mesmo + derruba" — **sem dano base escrito**; injogável. *(Corrigido na amostra, dano reconstruído da linha de Crítico.)*
- **[APO-05] alta/alta** — Habilidades Sociais: todas têm Crítico (logo rolam), nenhuma declara contra qual Defesa — mentais puros cairiam na física (Agilidade), contra [sistema-d20.md:210](../docs/jogador/sistema-d20.md:210). E Barganha/Máscara Social entregam resultado garantido por Mana, colidindo com o modelo "Persuadir = teste vs DC" ([sistema-d20.md:249](../docs/jogador/sistema-d20.md:249)). Dois procedimentos pro mesmo ato, sem regra de qual vale.
- **[APO-08] alta/alta** — Vínculo Selvagem ([buff.md:545-553](../docs/habilidades/buff.md:545)): companheiro **permanente** que causa 3d6 automáticos por turno sem custo recorrente, por 12 Mana pagos uma vez — em 2 rodadas supera a Suprema de 16 equivalente; sem ficha, alcance ou teste.
- **[APO-11] média/alta** — Inspiração Arcana: rendimento líquido fixo (+3 Mana) em qualquer Intensidade — subir de Intensidade é pedágio puro, violando "subir é sempre ganho" ([index.md:70](../docs/habilidades/index.md:70)).
- **[APO-12] média/média** — Motores de Mana (Rapsódia, Divisor de Mana, Aura de Auxílio, Cubo Protetor): geram Mana líquido pro grupo sem limite de uso fora de combate — a "ciranda de Rapsódia" antes de cada porta anula o descanso (e a Cicatriz Exaustão Crônica).
- **[APO-14] média/alta** — Força Tóxica e Nuvem Mortal: habilidades de **veneno** que aplicam Sangrando rotulado "(veneno)" em vez da condição Envenenado, feita exatamente pra isso — e sem testar Vitalidade.
- **[APO-16] média/alta** — "Perde a próxima Reação" + Atordoado no mesmo pacote é rider morto (Atordoado já nega reação): Antigravidade III (8) e Abismo III (9) pagam mais pelo que Garra Demoníaca II (5) entrega igual.
- **[APO-20] média/média** — Escudo de Proteção: a retaliação e o anti-derrubar valem "enquanto o Escudo durar" — e quando um Escudo maior de outra fonte o substitui ("vale o maior")?
- **[APO-21] média/alta** — Linhas de Crítico em habilidades que não rolam nada (Discurso Inspirador cura aliados; Leitura Fria, Barganha, Máscara Social): crítico de qual rolagem?
- **[APO-22] média/alta** — Forma Selvagem: os ataques Garra/Mordida/Investida não têm custo, teste nem regra de uso; e a nota "Intensidade III deixa Sangrando" está impressa dentro das três Intensidades da forma.
- **[APO-23] média/média** — "Nenhuma cura funciona" (Golpe Sangrento) vs Redenção ("revive"), Retrocesso ("recupera Vida perdida") e a limpeza de veneno por cura: as categorias cura/recupera/revive nunca foram delimitadas.
- **[APO-26] média/alta** — Provocação (Debuff, automática, 3 alvos, 5 Mana) domina Manipular (Social, rolada, 1 alvo, até 9 Mana) — o controle mental tem dois preços e dois procedimentos.
- **[APO-37] média/média** — Discurso Inspirador I: a cura mais barata do jogo (1 Mana, até 4 aliados, 10 casas) revive qualquer Caído pela regra geral — desarma a espiral de morte e torna Estabilizar quase irrelevante.
- **[APO-28/29/30] baixa** — Escudo dentro de buff longo sem duração própria; "Escudo que bloqueia o próximo golpe" (absorve ou anula?); Repouso Silencioso "fica imóvel" minúsculo (se é a condição Imóvel, o usuário age normalmente ignorando todo dano).
- **[APO-33] baixa/média** — Dissipar: a fronteira de "efeito de Buff" (a Chave? qualquer benefício? o companheiro permanente?) não é definida — 5 Mana que valem nada ou apagam 12.
- **[APO-34] baixa/alta** — "O Amor Está no Ar": cláusula de reviver redundante que induz a leitura de que as outras curas **não** reviveriam.
- **[APO-35] baixa/alta** — Fúria Selvagem: "nenhuma Habilidade além de Ataques Básicos" — Ataque Básico não é Habilidade; e bloqueia as Reações dedicadas?
- Absorvidos pela Parte 1: APO-04 (§2), APO-06/09/19/24/25/27/36 (§9), APO-07/13 (§7), APO-10 (§10), APO-15 (§6), APO-17/18/31 (§3), APO-32 (§8).

### Raças, Origem, Tocado (29 achados: 5 alta, 14 média, 10 baixa)

- **[PER-02] alta/alta** — Três traços de Origem dão Vantagem em "testes de resistir" (Medo, ilusões, controle mental) que o defensor **nunca rola** — no modelo "quem age, rola", o Mestre rola contra Defesa estática; não há dado onde aplicar a Vantagem. O Tocado pelas Sombras mostra a gramática certa ("ataques contra ele rolam com Desvantagem").
- **[PER-03] alta/alta** — Curandeiro de Vila ≡ Salvou uma Vida: texto idêntico em tabelas independentes — pegar os dois dá 2 estabilizações por descanso? Sem regra. [PER-10] amplia: mais quatro pares duplicados (Soldado ≡ Cresceu em Guerra; Domador ≡ Domou uma Fera; Tragédia ≡ Monastério; Gladiador ≡ Emboscada Felina do Tigre) viram escolhas mortas sem aviso, inclusive **no sorteio de d20 que o próprio texto convida**.
- **[PER-05] alta/alta** — Corrente Elétrica (Enguia, [racas/index.md:326](../docs/racas/index.md:326)): Atordoado em até 3 criaturas na **Intensidade II** por 2 PA + 3 Mana, num traço racial grátis — enquanto a Baforada Dracônica ao lado segue a escada à risca.
- **[PER-06] média/alta** — Sangue-de-Dragão: "escolha 1 dos **8** elementos" — existem 11.
- **[PER-07] média/alta** — Tocados citam tipos de dano fantasmas: "imune a raio **e elétrico**" (elétrico não existe), "Resistência a **frio**" (o tipo é Gelo; e "frio extremo" de clima causa Exausto, não dano — metade de 1 grau não computa).
- **[PER-11] média/alta** — Traço racial ≡ 1 traço leve de Origem, palavra por palavra (Passo Inabalável do Bode = Montanhas; Teimosia do Anão ⊇ Monastério) — a equação declarada "Origem inteira = 1 Raça" não fecha.
- **[PER-13] média/alta** — Quase Morreu: "reduz em 1 o primeiro dano fatal, sobrevivendo com 1 de Vida" — "dano fatal" não existe e a aritmética não fecha (reduzir 1 de um golpe de 12 não deixa com 1 de Vida).
- **[PER-14] média/alta** — "Dano Desarmado 1 grau acima" (7 raças): a tabela termina em "17+ → 1d10" — o grau acima **não existe** nos níveis 17-20.
- **[PER-15] média/média** — Respiração Aquática: a lista do que o descanso longo seco concede cobre 3 de 6 efeitos (Dados de Vida? Exausto? reset de "1x/descanso"?).
- **[PER-16] média/média** — Olhos do Vazio (Tocado pelas Sombras) vs atacante com Visão no Escuro: a Desvantagem é justificada pelo corpo do Tocado, mas a regra de luz diz que Visão no Escuro "ignora as duas linhas". Vale ou não?
- **[PER-17] média/média** — Determinação Humana vs Tiers de Resultado (falha total vira qual faixa?) e vs Último Turno ("toda falha é crítica" — a raça contorna o preço da regra?).
- **[PER-18] média/média** — Língua Presa (Sapo): puxa criatura hostil automaticamente, sem teste (ver §2); e Pés Fincados proíbe "derrubado ou empurrado" — **puxado** conta?
- **[PER-29] média/média** — Afinidade Arcana (Elfo): a única Vantagem permanente e incondicional do jogo (todos os ataques INT/SAB, pra sempre) — todos os pares são racionados; outra categoria, não outro grau.
- **[PER-19/21/22] baixa** — "Testes de Infiltração" (grupo não é teste); "sem penalidade de Movimento em X" sem usar o termo Terreno Difícil; Fez um Pacto é o único ajuste de atributo entre traços (permite +4 no nv1, Vontade -3 abaixo do piso, e escolher Vontade anula o próprio traço).
- **[PER-23/24] baixa** — Traços fixos que morrem na curva de 20 níveis: Pele de Urso (-2 dano, quase-imortal no nv1, cosmético no nv20), Aprendiz de Mago (+1 Mana/descanso curto).
- **[PER-25] baixa/alta** — Tocado sobreposto à raça: metade do passivo de Sombras é redundante num Elfo, o coração do Abismo é redundante em raça aquática — e o molde de criação não manda conferir.
- **[PER-26] baixa/média** — Recolher no Casco anula "o dano" — as condições do mesmo ataque passam?
- **[PER-28] baixa/média** — "Feras não-corrompidas" (Tocado pela Natureza): categoria que o Bestiário não tem.
- Absorvidos pela Parte 1: PER-01 (§5), PER-04 (§5), PER-08 (§12), PER-09 (§7), PER-12 (§5), PER-20 (§5), PER-27 (§5).

### Pacotes (13 achados: 3 alta, 5 média, 5 baixa)

Cobertura: 100/100 pacotes, ~1.100 nomes verificados, **zero referências quebradas**, **zero violações da ordem Básica→Avançada→Especial**, todas as 1.000 linhas de trilha no padrão de níveis ímpares.

- **[PAC-01/02/03] alta/alta** — Três pacotes de espada-e-escudo **fisicamente impossíveis**: Centurião (Lança é Duas Mãos — escudo exige arma Leve), Vanguarda e Paladino do Juramento (Escudo Torre proíbe **qualquer** arma junto). Nos três, a trilha inclui Bloqueio + as 3 habilidades da arma — um dos dois lados vira letra morta. O Templário mostra a versão correta.
- **[PAC-04/05] média/alta** — Armas iniciais inequipáveis no nível 1: Violino exige Vontade +4 e Lâmpada exige Int +5, acima do teto de criação (+3) — Encantador, Skald e Portador da Luz começam sem poder empunhar a própria arma (e o Violino ainda ataca com Força, não com o foco sugerido).
- **[PAC-06] média/média** — Lanceiro nv17: Investida Dupla exige Lança + Espada **simultâneas** — a Lança é Duas Mãos; seriam três mãos. A exceção documentada só cobre o par de katanas.
- **[PAC-08] média/média** — 16 pacotes com "Atributo em foco" disjunto do atributo de ataque da arma inicial (Necromante: foco Int, Foice ataca com Força; Profeta: foco Sab, Cajado ataca com Int…) — a arma ocupa 3 das 10 escolhas e nenhum pacote avisa.
- **[PAC-07] baixa/alta** — Retalhador (2 katanas Duas Mãos): sancionado em [arsenal.md:157](../docs/jogador/arsenal.md:157), mas [arsenal.md:114](../docs/jogador/arsenal.md:114) não menciona a exceção — quem lê só a regra de Leve conclui que o pacote é ilegal.
- **[PAC-09..13] baixa** — Conceitos da tabela divergem dos kits: Pirata ("pistola numa mão, sabre na outra" — ambos são pares indivisíveis), Mentalista ("sem arma visível" × Olho Mágico), Mago de Sangue ("adagas" × Manual), Caçador de Recompensas ("boleadeiras e redes" que nem existem × 4 armas de fogo), Clérigo da Guerra ("escudos de ferro" × Martelo Duas Mãos).

### Livro do Mestre (18 achados: 2 alta, 6 média, 10 baixa)

- **[MES-01] alta/alta** — A Baforada do Dragão Filhote ([bestiario.md:317-323](../docs/mestre/bestiario.md:317)) **escala a área com a Intensidade** (cone 3→5 casas), contra a regra mais estrutural do sistema ([habilidades/index.md:46-47](../docs/habilidades/index.md:46)) — no primeiro chefe do livro, que o texto diz usar Intensidade "como um jogador faria", sem exceção declarada.
- **[MES-05] média/média** — A Vida por Tier escala em fatores diferentes (Comum ×6,25, Treinado ×4,0, Formidável ×3,7, Lendário ×3,3 do nv1 ao 20) contra dano de grupo ×2,7 — o Comum de nível alto exige ~2,3× mais golpes, contradizendo a promessa "um Comum sempre cai em ~2 golpes" da própria página. (Além do problema conhecido do 2,7×, que não reporto como novo.)
- **[MES-07] média/alta** — Vigiar é o único teste da tabela de viagem sem DC; e "Vantagem contra emboscada" não tem rolagem onde se aplicar (o emboscador rola contra Defesa estática).
- **[MES-08] média/alta** — "Afastar-se assim **não provoca reação**" (Bandido, [bestiario.md:256](../docs/mestre/bestiario.md:256)) pressupõe ataque de oportunidade que o jogo não tem — única ocorrência da expressão em docs/; ensina por implicação uma regra que o jogador nunca recebeu.
- **[MES-09/10/11] baixa/alta** — Números narrativos que não batem com as tabelas ao lado: "encontro Padrão rende 3 a **60** prata" (máximo real: 40); "5 Treinados" como exemplo Mortal 16+ (soma 15); Lendário dura "3-5 rodadas" num arquivo e "três a quatro" no outro (conta real ≈ 4,5).
- **[MES-16] baixa/alta** — [mestre/index.md:15](../docs/mestre/index.md:15): "Três coisas fogem do padrão" — seguem quatro.
- **[MES-17] baixa/média** — Exemplos de encontro cruzam a faixa de nível sem citar o ajuste de Vida (Cripta Rasa "nv 3-5" com Esqueletos de 25 Vida; no nv5 a própria tabela manda 45).
- **[MES-18] baixa/baixa** — "Mago" de exemplo com Defesa física 16 exige Agilidade+equipamento = +8 — possível, mas é um mago de escudo-torre.
- Absorvidos pela Parte 1: MES-02 (§1), MES-03 (=COM-23), MES-04/06/12/13/14 (§12), MES-15 (§5).

### Transversais restantes

- **[TRA-13] baixa/alta** — Números-vitrine: as páginas anunciam **574** habilidades; a contagem real de fichas é **573** (571 em habilidades/arsenal + 2 raciais gratuitas); [index.md:44](../docs/index.md:44) diz "os nove grupos" — são 10. (CLAUDE.md também diz "9 grupos".)
- **[TRA-14] baixa/média** — "Escudo" nomeia duas mecânicas sem parentesco: a condição (pontos temporários) e o item (bônus de Defesa). O glossário não distingue; o "ignora bônus de Escudo" do Mangual só se resolve lendo o arsenal.

---

## Parte 3 — O que se confirmou sólido

Verificado com a mesma disciplina dos achados — vale saber onde **não** mexer:

1. **A camada numérica é impecável.** Script sobre o sistema inteiro: zero violações de PA = Intensidade, zero triplas de Mana fora das escadas sancionadas (1/3/6, 2/5/9, 3/7/12, +3/+3). Os dados de dano das 62 armas batem 100% com o glossário. O problema nunca é a conta da ficha — é qual escada a ficha usa, ou o que as palavras ao lado da conta dizem.
2. **A malha de referências segura.** Zero âncoras quebradas em 28 arquivos (o fix em massa do commit 4d63c7b aguentou); zero referências de nome quebradas nos 100 pacotes (~1.100 checagens); toda promessa "ver habilidade X em Y" que testamos existia (Bloqueio, Impulso da Soqueira, Esferas Sombrias). Única exceção: "Sentidos Apurados" (COM-23).
3. **A matemática do Bestiário fecha.** Defesa das 8 fichas conferida número a número; Bases 6/8/10/14 idênticas nos dois lados; os 4 exemplos de encontro somam os pontos certos; a economia cruzada fecha (preços de armas, armadura, cavalo, 50p inicial compra armadura leve "e sobra troco").
4. **Descanso é idêntico nos três arquivos** que o descrevem (exploracao ↔ mana ↔ sistema-d20) — o melhor exemplo de que regra em um lugar só não deriva.
5. **Luz e escuridão são o modelo.** exploracao.md define escuridão parcial E total citando **nominalmente** os traços que dependem dela (Subterrâneo, Visão no Escuro, Tocado pelas Sombras) — é exatamente o que falta pra água, surpresa e voo.
6. **Ressuscitar é de fato o único Tiers de Resultado**, no formato exato (Custo fixo ◈◈◈ + 18, faixas explícitas). **Área/alcance nunca escalam com Intensidade** em nenhuma das ~760 fichas (a única violação é do Dragão do Bestiário — MES-01). **As 22 Supremas custam 16+.**
7. **testes.md é o arquivo mais limpo do sistema:** percentuais dos testes sociais exatos, projeções de atributo corretas, "quem age rola" respeitado.
8. **Os 100 pacotes respeitam a progressão** (níveis ímpares, pré-requisitos de grau) sem uma única violação — até o Retalhador, o mais complexo, encadeia perfeito.
9. **As 25 raças cumprem a regra do traço físico inconfundível** (o Humano é excluído de propósito pelo próprio texto). **Tocado** é o texto estruturalmente mais consistente do jogo. **A Baforada Dracônica** é o gabarito de traço-habilidade bem feito. **Veneno** é o elemento exemplar (acúmulos respeitados, Defesa por Vitalidade declarada — o único que cumpre a regra à risca).

---

## Parte 4 — O que foi corrigido

Com sua autorização ampla ("pode resolver o que puder"), apliquei as correções abaixo. Elas se dividem em duas naturezas, e vale distinguir: a maioria é **dedução** — o texto contradizia uma regra já escrita, e eu o alinhei. Uma minoria é **decisão de design** que eu precisei tomar porque a regra simplesmente não existia; essas estão marcadas com ⚠ e são as que merecem sua revisão.

### 4.1 — As regras novas que passaram a existir

Escrever estas dez entradas resolveu, de uma vez, centenas de pontas soltas espalhadas pelo sistema. Todas foram redigidas no tom e na lógica das regras que já existiam.

| Regra nova | Onde | O que decidi ⚠ |
|---|---|---|
| **Derrubado** | glossário | Movimento 0; ataques corpo a corpo contra ele com Vantagem; **levantar custa ◈**. Nome separado de "Caído" (0 de Vida), com nota distinguindo os dois. |
| **Vantagem / Desvantagem** | glossário | Trazidas do Livro do Mestre pro glossário. Não acumulam; ⚠ **Vantagem e Desvantagem na mesma rolagem se cancelam** (rola 1d20 limpo) — era o caso que ninguém resolvia. |
| **Turno / Rodada / Cena** | glossário | ⚠ Efeito de "X rodadas" expira **no início do turno de quem o criou**, X rodadas depois. Cena = unidade contínua de ação; **um combate é sempre uma cena própria** (resolve os "1x por cena" vs "1x por combate"). |
| **Empurrar e Puxar** | glossário | ⚠ O deslocamento **para no obstáculo** e as casas restantes se perdem, **sem dano de colisão**. Ser empurrado pra dentro de uma zona conta como "entrar" nela. |
| **Perde a próxima Reação** | glossário | ⚠ Bloqueia **inclusive Reações dedicadas**, e expira no fim da próxima rodada se não for usada. |
| **Desprevenido** | glossário + exploração | Não age nem reage na primeira rodada. O teste de Vigiar ganhou DC 12 e passou a produzir/evitar essa condição — fecha o traço Órfão de Rua e o "grupo surpreendido". |
| **Agarrado** | glossário | ⚠ Fica Imóvel; escapar custa ◈ + teste de Força/Agilidade contra a Defesa de quem prende. |
| **Acúmulo de bônus** | glossário | ⚠ **Bônus planos de buffs diferentes não somam — vale o maior** (a Bênção Divina segue empilhando consigo mesma, que era exceção declarada). Resistências ao mesmo tipo idem. Esta é a decisão de maior impacto no equilíbrio, e a que mais merece seu olhar. |
| **Efeitos de terreno (regra geral)** | glossário | A não-soma saiu de baixo da Zona Amaldiçoada e virou regra de **todas** as zonas, de qualquer elemento. ⚠ Padrão de duração: até o fim do combate. |
| **Voo** | Pontos de Ação | ⚠ Move em 3D pelo mesmo custo; corpo a corpo só alcança 1 casa de altura; **Atordoado ou derrubado no ar despenca** (1d6 por 2 casas + cai Derrubado); Imóvel plana. |
| **Água e afogamento** | exploração | ⚠ Água funda é Terreno Difícil; fôlego = 1 + Vitalidade rodadas; afogando, 1 grau de Exausto por rodada. Dá base pros 8 traços aquáticos que cancelavam uma penalidade inexistente. |

Além delas, três decisões de política que estavam empatadas entre páginas:

- **Buffs têm Intensidade** (o `mana.md` foi corrigido; era ele que discordava do resto do sistema).
- **Custo fixo agora tem preço definido**: Mana da Intensidade III, PA ◈◈◈ — com as exceções que o Arsenal já praticava (Avançada de área = ◈◈, Reação dedicada = 0). E a regra ganhou uma frase que faltava: ⚠ **Custo fixo não dispensa a rolagem**.
- **Resolução de área**: ⚠ uma única rolagem comparada à Defesa de cada alvo (o 20 natural crita contra todos que acertou).

### 4.2 — As correções nas habilidades

Todas as ~180 edições estão no `git diff`. Agrupadas por natureza:

**Custos fora da escala (dedução).** Guardião Invocado 3→12 Mana (era o pior furo do Arsenal). Investida Certeira, Armadilha Oculta e Golpe Furtivo saíram da escala inventada 1/4/7 para 1/3/6. Chute Navalha, Combo Punitivo e Corte Cruzado alinhados a 1/3/6 (eram clones caros dos vizinhos). Arrasador e Etiqueta do Mordomo, clones exatos, ficaram no mesmo preço. Doze pares de elementais idênticos com preços diferentes foram nivelados pelo mais barato. Confete Explosivo 4/7/10→2/5/8. Reforço Momentâneo e Dança Élfica e Postura da Sombra subiram para o preço real de Custo fixo.

**Atordoado voltando ao degrau III (dedução).** Seis violações independentes da mesma régua, corrigidas em seis arquivos: Espada Senciente (Arsenal), Destruição (Marciais), Domador da Natureza e Fenda Dimensional e Garra Demoníaca (Debuff), Corrente Elétrica (traço racial da Enguia), Investida Encadeada (que ainda por cima usava a assinatura do Raio dentro do Gelo — virou Imóvel).

**A camada "automático sem teste" (⚠ decisão).** As ~15 habilidades comuns que ignoravam Defesa passaram a rolar: Zona Cinzenta, Marca Fatal, Névoa Sangrenta, Enterrar, Dominação: Enfraquecer, Escuridão Absoluta, Chuva de Sangue, Provocação, Espada Vingadora, Dança Encantadora, Astrape Sombria, Chama Amaldiçoada, Oráculo, Pulso Eletrônico, Ataque Orbital, Investida Encadeada. **Mantive automáticas** as Supremas de 16 Mana (a regra as autoriza) e **todas as zonas persistentes de chão**, que funcionam como a Zona Amaldiçoada.

**Textos que não fechavam (dedução).** Catástrofe ganhou a linha de dano que não tinha (reconstruída do Crítico). Aceleração Temporal passou a custar 0 PA — antes você pagava 2 PA para ganhar 1. Impacto Profundo virou Suprema de 16 (atingia o campo inteiro por 3 Mana). Mão Infinita III e Armadilha Oculta III, que eram cópias da II, ganharam degrau real. Cláusulas duplicadas removidas em Tridente, Espingarda, Fenda Dimensional, Esferas Sombrias, Buraco Negro, Chuva de Espinhos. Críticos que entregavam menos que o acerto (Chuva Gélida, Colheita Vermelha) e críticos incompletos (Tremor, Ira do Rei, Fúria do Vendaval, Praga Definitiva, Golpe Furtivo, Adagas) corrigidos.

**Motores infinitos (⚠ decisão).** Vínculo Selvagem deixou de ser permanente (dura até o descanso longo), ganhou ficha (15 de Vida, Defesa 10), passou a rolar e limitou-se a 1 companheiro. Chute do Vento Cortante devolve 1 Mana em vez de 3 (devolvia o próprio custo). Inspiração Arcana passou a render mais nas Intensidades altas (subir era pedágio puro). Rapsódia, Divisor de Mana, Aura de Auxílio e Cubo Protetor: **só em combate** — acabou a "ciranda de Mana" antes de cada porta.

**Buffs que eram Custo fixo indevido** ganharam as três Intensidades: Caminho da Espada, Desaparecimento, Fumaça Cega, Couraça de Pedra, Véu de Vapor, Passos do Vento, Pacto de Sangue.

**Fichas incompletas.** Lacaio Reanimado e Montaria de Guerra e Forma Selvagem ganharam o que faltava (Defesa, Vida, custo dos ataques, limite). Soco Ígneo e Punho Escaldante ganharam Alcance. Sociais ganharam a Defesa mental que nenhuma declarava, e as que não rolam nada perderam a linha de Crítico.

**Vocabulário alinhado ao glossário.** Veneno passou a usar Envenenado (usava Sangrando "de veneno"); Selo Sombrio e Bolha Temporal passaram a usar Imóvel e Lento; traços de Origem passaram a citar Terreno Difícil e as condições pelo nome; "Resistência a calor/frio" virou "ignora"; tipos fantasmas ("elétrico", "frio") viraram Raio e Gelo.

**Os três pacotes impossíveis.** ⚠ Centurião trocou Lança (duas mãos) por **Tridente** — arma Leve que combina com escudo, e a trilha dele acompanhou. Vanguarda e Paladino do Juramento trocaram Escudo Torre por **Escudo Pesado** (o Torre proíbe qualquer arma). Encantador, Skald e Portador da Luz ganharam aviso do requisito de atributo e uma arma alternativa para o nível 1.

**Livro do Mestre.** A Baforada do Dragão parou de escalar a área com a Intensidade. Os números narrativos que não batiam com as tabelas ao lado foram acertados (1 vs 2 golpes, "3 a 60 prata"→40, "5 Treinados"=15 pontos, "três coisas"→quatro). "Sentidos Apurados" virou "Instinto Ladino". O ataque de oportunidade que não existe saiu do Bandido.

**Vitrine.** As contagens de 574 habilidades e "nove grupos" foram corrigidas para **573 e dez grupos** (aqui e no `CLAUDE.md`), conferidas por script.

### 4.3 — O que deixei em aberto, e por quê

Não são esquecimentos: são pontos onde qualquer escolha minha seria um palpite sobre a sua intenção.

1. **Dano dos PJs escala 2,7x contra 7,6x da Vida.** Você já sabia e adiou de propósito; a correção mexeria em centenas de fichas. Não toquei.
2. **Afinidade Arcana do Elfo** (Vantagem permanente e incondicional em todo ataque mágico) — é o único traço de Vantagem sem freio no jogo, mas "fantasia crível > equilíbrio" é decisão sua, e o pool de atributos élfico é o menor do sistema. Deixei intacto.
3. **Os 16 pacotes cujo "Atributo em foco" não bate com a arma inicial** (Necromante com foco Inteligência e Foice que ataca com Força, etc.). Corrigir exige decidir, caso a caso, se muda o foco ou a arma — é conteúdo, não consistência.
4. **Traços fixos que envelhecem mal** (Pele de Urso -2 de dano, Aprendiz de Mago +1 Mana). Escalá-los é redesenhar o traço, não corrigir um erro.
5. **Duplicatas de conceito nos pacotes** (Pirata que promete "pistola e sabre", Caçador de Recompensas com boleadeiras que não existem). São descrições de sabor divergindo do kit; reescrevê-las é escrever conteúdo novo.
6. **Buraco Negro nas Intensidades II e III**: restaurei a identidade da habilidade (puxar para junto do usuário), mas isso a afasta da assinatura genérica de Espaço-Tempo ("teleporta 4 casas"). Se preferir a assinatura, é uma linha para desfazer.
7. **"Cena" agora está definida**, mas vale você conferir se a definição que escolhi (um combate = uma cena) bate com a sua intuição de mesa — ela governa vários traços raciais.

---

## Parte 5 — O que fazer agora

Os quatro passos que este relatório originalmente sugeria (escrever o glossário, decidir as três políticas, normalizar preços, consertar os pacotes) **já foram executados** — estão registrados na Parte 4. O que resta é seu:

1. **Revise as decisões marcadas com ⚠ na Parte 4.** São ~15 pontos onde a regra não existia e eu escolhi por você. A mais importante é o **acúmulo de bônus** (buffs planos não somam, vale o maior): ela muda o teto de dano de um grupo com dois suportes, e é a única correção com efeito real sobre o equilíbrio geral. As outras são procedimentais.
2. **Leia os sete itens em aberto (4.3).** Nenhum é urgente; todos exigem uma escolha de conteúdo que é sua.
3. **Leve para a mesa.** Este sistema continua sem nenhum teste de jogo real — e agora, mais do que antes, o que ele precisa não é de outra passada de cálculo meu. As regras que escrevi para Derrubado, Voo, água e agarrão são plausíveis no papel; só uma sessão mostra se são jogáveis.
4. Quando quiser publicar, o site está pronto para rebuild — as âncoras e as contagens foram verificadas. **Nada foi commitado**: o `git diff` inteiro está à sua espera.
