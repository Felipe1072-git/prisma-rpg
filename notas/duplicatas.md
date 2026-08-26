# Levantamento de habilidades duplicadas e similares

Gerado por script a partir de `hooks/prisma.py` (`extrai_blocos_de_habilidade`) — 568 habilidades gerais, sem contar as 186 de arma.

Três camadas, da mais para a menos objetiva.


## Decisões da Camada A (2026-08-26)

Política: caso a caso. Resultado — **1 exclusão e 15 reformulações**, mais 14 habilidades tocadas
fora da Camada A ao ler cada grupo inteiro. **Camada A fechada em 2026-08-26.** O jogo foi de 754
para 753 habilidades; 30 fichas foram reescritas ou ajustadas.

| # | Grupo | Decisão | Estado |
|---|---|---|---|
| 1 | Fogo | Alma em Chamas / Impacto Meteórico / Explosão de Fogo — reformular as três | **feito** |
| 2 | Fogo | Punho Flamejante e Rastro Flamejante reformuladas; Chama Investida intocada | **feito** |
| 6 | Fogo | Força Flamejante reformulada; Círculo do Destino intocado | **feito** |
| 7 | Fogo | Chama Espelhada — reformulada como aura de represália | **feito** |
| 5 | Raio | Descarga Carregada — reformulada como aura móvel | **feito** |
| 8 | Sombras | Rajada Sombria — reformulada com acerto automático | **feito** |
| 9 | Sombras | Frenesi Sombrio — **apagada** (753 habilidades) | **feito** |
| 10 | Água | Correntes de Água — reformulada (prende ao ponto) | **feito** |
| 11 | Sangue | Chuva Carmesim — reformulada em duas ondas | **feito** |
| 4 | Espaço-Tempo | Peso das Trevas (campo gravitacional) e Vazio (suga e explode) | **feito** |
| 12 | Arcano | Força Perfeita (fura defesa) e Impacto Arcano (linha crescente) | **feito** |
| 3 | Debuff → Conjuração | virou **Golpe Emprestado**: invocação de golpe único (Debuff 74→73, Conjuração 13→14) | **feito** |

Fechado junto no bloco Espaço-Tempo + Arcano: **7 das 18 de Espaço-Tempo** repetiam a escada
`teleporta 2 → teleporta 4 → teleporta 4 + Atordoado`. Além do par da Camada A, ganharam verbo
próprio **Dobra Espacial** (troca duas criaturas de lugar), **Crescente Sombrio** (atravessa
barreiras e cobertura), **Fissura Dimensional** (engole o alvo, que volta no turno seguinte),
**Colapso do Vazio** (dano dobrado contra alvo preso — fecha o combo do grupo) e **Ruptura
Dimensional** (arremessa todos para fora da área; o oposto do Horizonte de Eventos).

**Decisão de sistema (2026-08-26): reposicionamento forçado vira Teste de Resistência.** Sete
habilidades passaram de `Ataque vs Evasão` para `Teste de Resistência vs Fortitude Mágica` — Dobra
Espacial, Fissura Dimensional, Fenda Dimensional, Buraco Negro, Vazio, Eco do Passado e Ruptura
Dimensional. Resistir = **fica onde está, sem condições, e leva metade do dano**. O motivo: não se
*esquiva* de uma dobra do espaço. `habilidades/regras.md` foi ajustado no mesmo lote, ganhando o
segundo caso na orientação de quando usar cada resolução — senão o livro contradiria os cards.

Fechado junto no bloco Água + Sangue (fora da Camada A, achado ao ler os dois elementos inteiros):
**Água tinha 5 das 8 habilidades na mesma escada** (`puxa 1` → `puxa 2 + Lento` → `puxa 3 + Lento +
derruba`) e **Sangue tinha três cópias**, não duas. Reformuladas: **Abraço das Profundezas** (vira
afogamento) e **Espinhos de Sangue** (vira armadilha que fere quem entra). Estrela Cadente Desperta e
Chuva de Espinhos Vermelhos ficaram intactas.

**`Silenciado` estava órfão** — definido no glossário e aplicado por *nenhuma* habilidade do jogo. O
Abraço das Profundezas é a primeira a usá-lo. Vale procurar outras condições nessa situação.

**Dano de efeito que dura rodadas precisa dizer quantas vezes acontece.** A primeira versão das
Correntes de Água não dizia, e o autor perguntou — as outras três fichas do mesmo bloco diziam. A
regra da skill sobre "efeito periódico" vale também pro caso inverso: efeito que **não** repete
precisa declarar isso. A decisão: dano no golpe, e de novo só em quem tentar fugir e for puxado de
volta.

Fechado junto, fora da Camada A: **Voragem = Libertação Limitada**, o último par do
[ELE-31](auditoria.md) — achado na auditoria de 2026-07-27 e nunca corrigido. Escapou da minha
Camada A por uma cláusula só (a Voragem acrescenta Lento na Intensidade III). A Libertação Limitada
virou **Fauce do Abismo** e trocou a Zona Amaldiçoada por dreno.

E a lore órfã que isso revelou: **três habilidades de Sombras citavam um "selo"** que o Prisma nunca
definiu — sem verbete, sem mecânica, sem lore (é do Dio, do Grand Chase). O autor não entendeu o
próprio texto ao ler, o que é o teste que importa. Flavor das três reescrito (Fauce do Abismo,
Extermínio, Apocalipse); **nenhuma mecânica mudou** em Extermínio e Apocalipse. Ver
[[feedback-nomes-genericos-nao-grandchase]] — a regra vale pro flavor, não só pro nome.

Notas de execução da leva de Fogo:

- O **cooldown não se escreve** — vem da escala (`ESCALA_COOLDOWN`, `hooks/prisma.py:382`). Nenhuma das
  568 habilidades declarava um até aqui; **Explosão de Fogo é a primeira**, com 2 rodadas em vez da 1
  herdada, por acumular área + Queimando + derruba + dano de queda.
- **Imbuir Elemento** (Buff) já ocupa "chamas envolvem a lâmina" — foi por isso que Força Flamejante
  virou queimadura crescente em vez de imbuição.
- **Aura de Intensidade III pode ser permanente** (decisão do autor, 2026-08-26): as duas auras duram
  4 rodadas na III e têm cooldown herdado menor (1 e 3), então o usuário pode mantê-las ligadas
  reaplicando — o freio é o Mana, não o cooldown. As duas declaram **Manter ativa: reaplicar antes de
  expirar renova a duração — o efeito não empilha**, no molde da Bênção Divina.
- **Atordoado recorrente não entra em aura**: na Descarga Carregada a assinatura III do Raio virou
  estouro de ativação (só quem está na área no momento em que ela sobe), senão o alvo ficaria travado
  todas as rodadas sem contra-jogo.
- O glossário proíbe **cadeia de espalhamento** ("quem pegou fogo por espalhamento não espalha de
  novo"), o que descartou a primeira ideia para Rastro Flamejante.


## Camada A — clones literais

Mesma escada de Intensidade, mesmos números, mesma ficha. Muda só nome e flavor.

- **Alma em Chamas = Impacto Meteórico = Explosão de Fogo** — Fogo · magicas-elementais.md:356 · magicas-elementais.md:537 · magicas-elementais.md:628
- **Chama Investida = Punho Flamejante = Rastro Flamejante** — Fogo · magicas-elementais.md:460 · magicas-elementais.md:494 · magicas-elementais.md:678
- **Etiqueta do Mordomo = Arrasador** — debuff · debuff.md:293 · magicas-elementais.md:1589
- **Peso das Trevas = Vazio** — espaco-tempo · espaco-tempo.md:77 · espaco-tempo.md:128
- **Força de Choque = Descarga Carregada** — Raio · magicas-elementais.md:312 · magicas-elementais.md:334
- **Força Flamejante = Círculo do Destino** — Fogo · magicas-elementais.md:386 · magicas-elementais.md:608
- **Chama Espelhada = Chama Solar** — Fogo · magicas-elementais.md:438 · magicas-elementais.md:449
- **Choque Maligno = Rajada Sombria** — Sombras · magicas-elementais.md:734 · magicas-elementais.md:929
- **Vórtice das Trevas = Frenesi Sombrio** — Sombras · magicas-elementais.md:838 · magicas-elementais.md:982
- **Bomba Shuju = Correntes de Água** — Água · magicas-elementais.md:1281 · magicas-elementais.md:1301
- **Chuva de Espinhos Vermelhos = Chuva Carmesim** — Sangue · magicas-elementais.md:1512 · magicas-elementais.md:1570
- **Força Perfeita = Impacto Arcano** — Arcano · magicas-elementais.md:1600 · magicas-elementais.md:1611

**14 habilidades a mais do que o necessário.**


## Camada B — mesmo efeito, forma diferente

Escada idêntica palavra por palavra; muda só alvo/alcance/área. Cada linha mostra a forma.


**Cluster de 6** (Fogo)

- Alma em Chamas — magia / 2 casas de raio do ponto / 8 casas / fogo · magicas-elementais.md:356
- Espada Flamejante — magia / todas as criaturas em 1 casa de raio ao redor do usuário / fogo · magicas-elementais.md:375
- Explosão em Massa — magia / 2 casas de raio ao redor do usuário / fogo · magicas-elementais.md:472
- Impacto Meteórico — magia / 2 casas de raio do ponto / 8 casas / fogo · magicas-elementais.md:537
- Lança de Fogo — magia / todas as criaturas na linha / linha de 12 casas / fogo · magicas-elementais.md:586
- Explosão de Fogo — magia / 2 casas de raio do ponto / 8 casas / fogo · magicas-elementais.md:628

**Cluster de 6** (Fogo)

- Fôlego Ardente — magia / cone de 3 casas à frente / fogo · magicas-elementais.md:397
- Chama Espelhada — magia / duas linhas de 5 casas, uma à frente e outra atrás do usuário / fogo · magicas-elementais.md:438
- Chama Solar — magia / duas linhas de 5 casas, uma à frente e outra atrás do usuário / fogo · magicas-elementais.md:449
- Investida Explosiva — magia / todas as criaturas na linha / linha de 6 casas / fogo · magicas-elementais.md:517
- Chama do Torvelinho — magia / 2 casas de raio ao redor do usuário / fogo · magicas-elementais.md:658
- Lança Ilusória — magia / todas as criaturas na linha / linha de 8 casas / fogo · magicas-elementais.md:690

**Cluster de 4** (Fogo)

- Força Desesperada — magia / 1 criatura / até o valor de movimento, em casas / fogo · magicas-elementais.md:417
- Chama Investida — magia / 1 criatura / fogo · magicas-elementais.md:460
- Punho Flamejante — magia / 1 criatura / fogo · magicas-elementais.md:494
- Rastro Flamejante — magia / 1 criatura / fogo · magicas-elementais.md:678

**Cluster de 4** (marciais)

- Tornados Gêmeos — ataque / até 3 criaturas à escolha, ao alcance da arma equipada · marciais.md:72
- Rodamoinho — ataque / todas as criaturas adjacentes · marciais.md:271
- Esmagador de Ossos — ataque / linha de 5 casas à frente · marciais.md:315
- Lampejo de Luz — ataque / todas as criaturas na linha / linha de 5 casas · marciais.md:525

**Cluster de 3** (Arcano, debuff, pontaria)

- Etiqueta do Mordomo — magia / 1 criatura / 8 casas / arcano · debuff.md:293
- Arrasador — magia / 1 criatura / 8 casas / arcano · magicas-elementais.md:1589
- Tiro Concentrado — ataque / 1 criatura / 8 casas · pontaria.md:40

**Cluster de 3** (espaco-tempo)

- Crescente Sombrio — magia / todas as criaturas na linha / linha de 8 casas / arcano · espaco-tempo.md:66
- Peso das Trevas — magia / 2 casas de raio do ponto / 8 casas / arcano · espaco-tempo.md:77
- Vazio — magia / 2 casas de raio do ponto / 8 casas / arcano · espaco-tempo.md:128

**Cluster de 3** (Raio)

- Campo Eletrônico — magia / 2 casas de raio do ponto / 4 casas / raio · magicas-elementais.md:196
- Força de Choque — magia / 2 casas de raio ao redor do usuário / raio · magicas-elementais.md:312
- Descarga Carregada — magia / 2 casas de raio ao redor do usuário / raio · magicas-elementais.md:334

**Cluster de 3** (Fogo)

- Força Flamejante — magia / 1 criatura / 8 casas / fogo · magicas-elementais.md:386
- Punho Escaldante — magia / 1 criatura / corpo a corpo / fogo · magicas-elementais.md:557
- Círculo do Destino — magia / 1 criatura / 8 casas / fogo · magicas-elementais.md:608

**Cluster de 3** (Sombras)

- Giro Espectral — magia / todas as criaturas adjacentes / sombras · magicas-elementais.md:849
- Redemoinho Sombrio — magia / 2 casas de raio ao redor do usuário / sombras · magicas-elementais.md:898
- Voragem — magia / cone de 3 casas à frente / sombras · magicas-elementais.md:949

**Cluster de 3** (Sombras)

- Carícia da Morte — magia / 2 casas de raio ao redor do usuário / sombras · magicas-elementais.md:960
- Libertação Limitada — magia / cone de 3 casas à frente / sombras · magicas-elementais.md:1040
- Pilar Sombrio — magia / 2 casas de raio do ponto / 8 casas / sombras · magicas-elementais.md:1091

**Cluster de 3** (Sangue)

- Chuva de Espinhos Vermelhos — magia / 2 casas de raio do ponto / 8 casas / sangue · magicas-elementais.md:1512
- Espinhos de Sangue — magia / 1 casa de raio do ponto / 8 casas / sangue · magicas-elementais.md:1544
- Chuva Carmesim — magia / 2 casas de raio do ponto / 8 casas / sangue · magicas-elementais.md:1570

**Cluster de 3** (Arcano, marciais)

- Disparo Voraz — magia / 1 criatura / 8 casas / arcano · magicas-elementais.md:1622
- Grande X — ataque / 1 criatura · marciais.md:282
- Esmagador — ataque / 1 criatura / 8 casas · marciais.md:568

**Cluster de 2** (Raio)

- Explosão em Cadeia — magia / todas as criaturas na linha / linha de 6 casas / raio · magicas-elementais.md:283
- Lágrimas da Deusa — magia / 2 casas de raio ao redor do usuário / raio · magicas-elementais.md:323

**Cluster de 2** (Sombras)

- Paixão Interna — magia / 1 criatura / 8 casas / sombras · magicas-elementais.md:918
- Sobrecarga — magia / 1 criatura / 12 casas / sombras · magicas-elementais.md:971

**Cluster de 2** (Luz)

- Fragmento do Espírito — magia / 2 casas de raio do ponto / 8 casas / luz · magicas-elementais.md:1188
- Nêmesis — magia / até 3 criaturas diferentes / 8 casas / luz · magicas-elementais.md:1228

**35 redundâncias de forma.**


## Camada C — mesma assinatura mecânica

Mesmo conjunto de verbos de regra (o que a habilidade *faz*), independente da redação e do grupo. É a camada que pega pares como Pacto de Sangue / Aumento Sombrio.


**26x — `dano, derruba, empurra`** · grupos: Arcano, Vento, debuff, marciais, pontaria

- Giro Audaz (debuff, Moderado) · debuff.md:60
- Mordida (debuff, Moderado) · debuff.md:91
- Etiqueta do Mordomo (debuff, Moderado) · debuff.md:293
- Confete Explosivo (debuff, Moderado) · debuff.md:465
- Rajada de Ventos (Vento, Moderado) · magicas-elementais.md:1346
- Arrasador (Arcano, Moderado) · magicas-elementais.md:1589
- Força Perfeita (Arcano, Moderado) · magicas-elementais.md:1600
- Impacto Arcano (Arcano, Moderado) · magicas-elementais.md:1611
- Disparo Voraz (Arcano, Moderado) · magicas-elementais.md:1622
- Ataque Desarmado (marciais, Moderado) · marciais.md:24
- Tornados Gêmeos (marciais, sem escala) · marciais.md:72
- Chute Meteoro (marciais, Moderado) · marciais.md:95
- Dragão Celeste (marciais, Moderado) · marciais.md:133
- Chute do Vento Cortante (marciais, sem escala) · marciais.md:170
- Corte Triplo (marciais, Moderado) · marciais.md:259
- Grande X (marciais, sem escala) · marciais.md:282
- Pressão Brutal (marciais, Moderado) · marciais.md:337
- Chute Navalha (marciais, Moderado) · marciais.md:359
- Hanuman (marciais, Moderado) · marciais.md:371
- Justiça (marciais, Moderado) · marciais.md:444
- Golpe Veloz (marciais, Moderado) · marciais.md:466
- Golpe do Desespero (marciais, Moderado) · marciais.md:489
- Escamas Cortantes (marciais, Moderado) · marciais.md:513
- Esmagador (marciais, Moderado) · marciais.md:568
- Tiro Concentrado (pontaria, Moderado) · pontaria.md:40
- Rajada Sangrenta (pontaria, Maior) · pontaria.md:62

**19x — `area, dano, duracao`** · grupos: Fogo, Raio, Sombras, Veneno, conjuracao, debuff, projecao-mental

- Espada Vingadora (conjuracao, Maior) · conjuracao.md:33
- Dança Contagiante (debuff, Supremo) · debuff.md:18
- Escuridão Absoluta (debuff, Maior) · debuff.md:257
- Aniquilação (debuff, Supremo) · debuff.md:389
- Campo da Morte (debuff, Supremo) · debuff.md:418
- Campo Estático (Raio, Moderado) · magicas-elementais.md:256
- Rastro em Chamas (Fogo, Moderado) · magicas-elementais.md:408
- Trilha de Fogo (Fogo, Moderado) · magicas-elementais.md:528
- O Fim (Fogo, Supremo) · magicas-elementais.md:649
- Onda Sombria (Sombras, Moderado) · magicas-elementais.md:723
- Fenda Profunda (Sombras, Maior) · magicas-elementais.md:745
- Lâmina Emboscada (Sombras, Moderado) · magicas-elementais.md:765
- Floração Eterna (Sombras, Maior) · magicas-elementais.md:869
- Carícia da Morte (Sombras, Moderado) · magicas-elementais.md:960
- Libertação Limitada (Sombras, Moderado) · magicas-elementais.md:1040
- Extermínio (Sombras, Maior) · magicas-elementais.md:1062
- Pilar Sombrio (Sombras, Moderado) · magicas-elementais.md:1091
- Névoa Corrosiva (Veneno, Moderado) · magicas-elementais.md:1444
- Colapso Mental (projecao-mental, Maior) · projecao-mental.md:80

**19x — `area, dano, queimando`** · grupos: Fogo

- Alma em Chamas (Fogo, Moderado) · magicas-elementais.md:356
- Espada Flamejante (Fogo, Moderado) · magicas-elementais.md:375
- Força Flamejante (Fogo, Moderado) · magicas-elementais.md:386
- Fôlego Ardente (Fogo, Moderado) · magicas-elementais.md:397
- Chama Espelhada (Fogo, Moderado) · magicas-elementais.md:438
- Chama Solar (Fogo, Moderado) · magicas-elementais.md:449
- Explosão em Massa (Fogo, Maior) · magicas-elementais.md:472
- Golpe Supremo (Fogo, Maior) · magicas-elementais.md:483
- Soco Ígneo (Fogo, Moderado) · magicas-elementais.md:506
- Investida Explosiva (Fogo, Maior) · magicas-elementais.md:517
- Impacto Meteórico (Fogo, Moderado) · magicas-elementais.md:537
- Punho Escaldante (Fogo, Moderado) · magicas-elementais.md:557
- Lança de Fogo (Fogo, Moderado) · magicas-elementais.md:586
- Lança Espiritual (Fogo, Moderado) · magicas-elementais.md:597
- Círculo do Destino (Fogo, Moderado) · magicas-elementais.md:608
- Explosão de Fogo (Fogo, Moderado) · magicas-elementais.md:628
- Impacto Profundo (Fogo, Supremo) · magicas-elementais.md:639
- Chama do Torvelinho (Fogo, Moderado) · magicas-elementais.md:658
- Lança Ilusória (Fogo, Moderado) · magicas-elementais.md:690

**11x — `area, dano, derruba, empurra`** · grupos: Vento, debuff, marciais

- Onda de Choque (debuff, Maior) · debuff.md:124
- Ventos Cruzados (Vento, Maior) · magicas-elementais.md:1357
- Vendaval Reverso (Vento, Moderado) · magicas-elementais.md:1368
- Lâminas de Ar (Vento, Moderado) · magicas-elementais.md:1379
- Fúria do Vendaval (Vento, Supremo) · magicas-elementais.md:1420
- Rodamoinho (marciais, Moderado) · marciais.md:271
- Esmagador de Ossos (marciais, Moderado) · marciais.md:315
- Grilhões da Alma (marciais, Moderado) · marciais.md:348
- Andorinhas de Bambu (marciais, sem escala) · marciais.md:383
- Onda Lunática (marciais, Moderado) · marciais.md:478
- Lampejo de Luz (marciais, Moderado) · marciais.md:525

**7x — `atordoado, dano, derruba, duracao`** · grupos: debuff, espaco-tempo, marciais

- Garra Demoníaca (debuff, Moderado) · debuff.md:27
- Abismo (debuff, Maior) · debuff.md:102
- Antigravidade (espaco-tempo, Moderado) · espaco-tempo.md:159
- Fenda Dimensional (espaco-tempo, Maior) · espaco-tempo.md:170
- Empalar (marciais, Moderado) · marciais.md:237
- Mão Infinita (marciais, Moderado) · marciais.md:395
- Golpe da Alma (marciais, Moderado) · marciais.md:501

**6x — `aliados, duracao, invocar, self`** · grupos: conjuracao

- Servo de Cinzas (conjuracao, Menor) · conjuracao.md:56
- Corpo Provisório (conjuracao, Menor) · conjuracao.md:69
- Chamar Lâmina Espectral (conjuracao, Médio) · conjuracao.md:86
- Iteração Avançada (conjuracao, Médio) · conjuracao.md:99
- Encarnação (conjuracao, Maior) · conjuracao.md:115
- Convocar Guardião do Pacto (conjuracao, Maior) · conjuracao.md:130

**6x — `area, atordoado, dano`** · grupos: Raio

- Relâmpago (Raio, Moderado) · magicas-elementais.md:185
- Campo Eletrônico (Raio, Moderado) · magicas-elementais.md:196
- Explosão em Cadeia (Raio, Maior) · magicas-elementais.md:283
- Força de Choque (Raio, Maior) · magicas-elementais.md:312
- Lágrimas da Deusa (Raio, Moderado) · magicas-elementais.md:323
- Descarga Carregada (Raio, Maior) · magicas-elementais.md:334

**5x — `bonus-dano, duracao, self`** · grupos: buff

- Módulo de Comando (buff, Maior) · buff.md:382
- Superaquecimento (buff, Maior) · buff.md:392
- Punhos do Céu e da Terra (buff, Supremo) · buff.md:433
- Liberação de Poder (buff, Supremo) · buff.md:442
- Arma Definitiva (buff, Supremo) · buff.md:451

**5x — `duracao, self, vantagem`** · grupos: buff, marciais, percepcao-arcana

- Fluidez de Combate (buff, Maior) · buff.md:580
- Presciência Divina (buff, Supremo) · buff.md:738
- Fora de Alcance (buff, Maior) · buff.md:768
- Mira Firme (marciais, Moderado) · marciais.md:820
- Banco de Dados (percepcao-arcana, Moderado) · percepcao-arcana.md:104

**5x — `area, dano, derruba`** · grupos: Terra, debuff, infiltracao, marciais

- Corte Rápido Final (debuff, Supremo) · debuff.md:427
- Choque das Sombras (infiltracao, Moderado) · infiltracao.md:7
- Petrificar (Terra, Moderado) · magicas-elementais.md:28
- Divisão Espacial (marciais, Supremo) · marciais.md:579
- Nascimento das Lâminas (marciais, Supremo) · marciais.md:803

**5x — `area, dano, derruba, queimando`** · grupos: Fogo

- Chuva de Meteoros (Fogo, Maior) · magicas-elementais.md:347
- Queda Meteórica (Fogo, Moderado) · magicas-elementais.md:548
- Erupção Vulcânica (Fogo, Supremo) · magicas-elementais.md:577
- Onda Explosiva (Fogo, Supremo) · magicas-elementais.md:669
- Ataque Ilusório (Fogo, Supremo) · magicas-elementais.md:701

**5x — `dano, derruba, dreno`** · grupos: Sombras, marciais

- Choque Maligno (Sombras, Moderado) · magicas-elementais.md:734
- Paixão Interna (Sombras, Moderado) · magicas-elementais.md:918
- Rajada Sombria (Sombras, Moderado) · magicas-elementais.md:929
- Sobrecarga (Sombras, Maior) · magicas-elementais.md:971
- Sede de Sangue (marciais, Moderado) · marciais.md:547

**4x — `area, dano, derruba, puxa`** · grupos: debuff, marciais

- Tempestade Furiosa (debuff, Supremo) · debuff.md:447
- Valsa da Imperatriz (debuff, Supremo) · debuff.md:476
- Espírito Indomável (marciais, Moderado) · marciais.md:145
- Martelo Explosivo (marciais, sem escala) · marciais.md:455

**4x — `area, atordoado, dano, teleporte`** · grupos: espaco-tempo

- Ruptura Dimensional (espaco-tempo, Supremo) · espaco-tempo.md:57
- Crescente Sombrio (espaco-tempo, Maior) · espaco-tempo.md:66
- Peso das Trevas (espaco-tempo, Maior) · espaco-tempo.md:77
- Vazio (espaco-tempo, Maior) · espaco-tempo.md:128

**4x — `area, atordoado, dano, duracao`** · grupos: Gelo, Sombras, marciais

- Investida Encadeada (Gelo, Maior) · magicas-elementais.md:154
- Pisada Colossal (Sombras, Maior) · magicas-elementais.md:829
- Erradicação (marciais, Supremo) · marciais.md:558
- Queda Celestial (marciais, Supremo) · marciais.md:589

**4x — `area, dano, movimento, queimando`** · grupos: Fogo

- Força Desesperada (Fogo, Moderado) · magicas-elementais.md:417
- Chama Investida (Fogo, Moderado) · magicas-elementais.md:460
- Punho Flamejante (Fogo, Moderado) · magicas-elementais.md:494
- Rastro Flamejante (Fogo, Moderado) · magicas-elementais.md:678

**4x — `area, dano, derruba, duracao`** · grupos: Sombras

- Corte Caótico (Sombras, Maior) · magicas-elementais.md:792
- Julgamento das Trevas (Sombras, Supremo) · magicas-elementais.md:860
- Lanças Sombrias (Sombras, Maior) · magicas-elementais.md:1011
- Apocalipse (Sombras, Supremo) · magicas-elementais.md:1082

**3x — `aliados, bonus-dano, dano, duracao, self`** · grupos: buff, percepcao-arcana, suporte

- Transformação do Lobo (buff, Maior) · buff.md:80
- Fenda no Instante (percepcao-arcana, Maior) · percepcao-arcana.md:52
- Cálculo de Impacto (suporte, Maior) · suporte.md:302

**3x — `movimento, reacao, self`** · grupos: buff, mobilidade

- Sombra Vazia (buff, Reação) · buff.md:320
- Cambalhota (mobilidade, Reação) · mobilidade.md:7
- Impulso da Soqueira (mobilidade, Reação) · mobilidade.md:47

**3x — `area, dano, duracao, empurra`** · grupos: debuff

- Fúria do Mordomo (debuff, Moderado) · debuff.md:304
- Cerco de Espinhos (debuff, Maior) · debuff.md:369
- Explosão Total (debuff, Supremo) · debuff.md:525

**3x — `atordoado, dano, duracao`** · grupos: Raio, debuff, projecao-mental

- Zona Cinzenta (debuff, Moderado) · debuff.md:380
- Astrape Sombria (Raio, Moderado) · magicas-elementais.md:215
- Repouso Forçado (projecao-mental, Maior) · projecao-mental.md:7

**3x — `atordoado, dano, teleporte`** · grupos: espaco-tempo

- Eco do Passado (espaco-tempo, Maior) · espaco-tempo.md:46
- Fissura Dimensional (espaco-tempo, Moderado) · espaco-tempo.md:97
- Colapso do Vazio (espaco-tempo, Maior) · espaco-tempo.md:139

**3x — `area, congelado, dano, duracao`** · grupos: Sombras

- Giro Espectral (Sombras, Moderado) · magicas-elementais.md:849
- Redemoinho Sombrio (Sombras, Moderado) · magicas-elementais.md:898
- Voragem (Sombras, Moderado) · magicas-elementais.md:949

**3x — `area, dano, imovel, marcado`** · grupos: Luz

- Raio Laser (Luz, Maior) · magicas-elementais.md:1157
- Restrição de Luz (Luz, Maior) · magicas-elementais.md:1168
- Fragmento do Espírito (Luz, Moderado) · magicas-elementais.md:1188

**3x — `congelado, dano, derruba, puxa`** · grupos: Água

- Bomba Shuju (Água, Moderado) · magicas-elementais.md:1281
- Correntes de Água (Água, Moderado) · magicas-elementais.md:1301
- Abraço das Profundezas (Água, Maior) · magicas-elementais.md:1324

**3x — `duracao, info, self`** · grupos: Vento, percepcao-arcana

- Olhos do Vento (Vento, Menor) · magicas-elementais.md:1411
- Ver Espíritos (percepcao-arcana, Menor) · percepcao-arcana.md:7
- Segunda Visão (percepcao-arcana, Menor) · percepcao-arcana.md:25

**3x — `area, custo-vida, dano, dreno, empurra, sangrando`** · grupos: Sangue

- Chuva de Espinhos Vermelhos (Sangue, sem escala) · magicas-elementais.md:1512
- Espinhos de Sangue (Sangue, sem escala) · magicas-elementais.md:1544
- Chuva Carmesim (Sangue, sem escala) · magicas-elementais.md:1570

**2x — `derruba, duracao, self`** · grupos: alquimia-de-mana, buff

- Corpo Fortalecido (alquimia-de-mana, Maior) · alquimia-de-mana.md:7
- Postura Inabalável (buff, Maior) · buff.md:39

**2x — `duracao, empilha, sangrando, self`** · grupos: alquimia-de-mana, necromancia

- Fúria da Arma (alquimia-de-mana, Maior) · alquimia-de-mana.md:17
- Encanto das Trevas (necromancia, Maior) · necromancia.md:41

**2x — `bonus-dano, dano, derruba, duracao`** · grupos: alquimia-de-mana, debuff

- Corrosão (alquimia-de-mana, Moderado) · alquimia-de-mana.md:92
- Ponto de Pressão (debuff, Maior) · debuff.md:155

**2x — `duracao, escudo, self`** · grupos: Terra, buff

- Escudo da Alma (buff, Maior) · buff.md:140
- Couraça de Pedra (Terra, Maior) · magicas-elementais.md:50

**2x — `reacao, self, teleporte`** · grupos: buff, mobilidade

- Fase (buff, Reação) · buff.md:301
- Postura da Sombra (mobilidade, Reação) · mobilidade.md:38

**2x — `aliados, reacao, self`** · grupos: buff, percepcao-arcana

- Escudo de Espírito (buff, Reação) · buff.md:609
- Alerta Prévio (percepcao-arcana, Reação) · percepcao-arcana.md:114

**2x — `area, dano, derruba, sangrando`** · grupos: debuff, marciais

- Esquife de Ossos (debuff, Moderado) · debuff.md:82
- Foice Mortal (marciais, Moderado) · marciais.md:204

**2x — `area, dano, empurra`** · grupos: debuff, marciais

- Impacto Grandioso (debuff, Moderado) · debuff.md:113
- Dança da Perdição (marciais, sem escala) · marciais.md:326

**2x — `area, desvantagem, duracao`** · grupos: debuff, infiltracao

- Névoa Sangrenta (debuff, Moderado) · debuff.md:239
- Fumaça Cega (infiltracao, Maior) · infiltracao.md:52

**2x — `area, dano, invocar`** · grupos: Sombras, debuff

- Fechar a Porta (debuff, Maior) · debuff.md:569
- Brilho Caótico (Sombras, Moderado) · magicas-elementais.md:774

**2x — `area, dano, derruba, imovel`** · grupos: Luz, Terra

- Fúria em Espiral (Terra, Supremo) · magicas-elementais.md:92
- Luz do Paraíso (Luz, Maior) · magicas-elementais.md:1179

**2x — `custo-vida, dano, dreno`** · grupos: Sangue, necromancia

- Lâmina de Sangue (Sangue, sem escala) · magicas-elementais.md:1486
- Preço de Sangue (necromancia, sem escala) · necromancia.md:93

**2x — `bonus-dano, dano, derruba, empurra, movimento`** · grupos: marciais, pontaria

- Carga com Lança (marciais, Moderado) · marciais.md:226
- Investida Certeira (pontaria, Moderado) · pontaria.md:18

**155 habilidades em colisão de assinatura.**


## Tamanho de cada grupo

| Grupo | Habilidades |
|---|---|
| buff | 90 |
| marciais | 83 |
| debuff | 74 |
| Sombras | 43 |
| Fogo | 36 |
| suporte | 33 |
| espaco-tempo | 18 |
| necromancia | 18 |
| Raio | 16 |
| mobilidade | 14 |
| conjuracao | 13 |
| infiltracao | 12 |
| percepcao-arcana | 12 |
| projecao-mental | 12 |
| sociais | 12 |
| alquimia-de-mana | 11 |
| pontaria | 11 |
| Luz | 10 |
| Gelo | 8 |
| Água | 8 |
| Vento | 8 |
| Sangue | 8 |
| Terra | 7 |
| Arcano | 6 |
| Veneno | 5 |

## Fechamento da Camada A

O que sobrou pra depois, por ordem de tamanho:

- **Camada B** (35 redundâncias de forma) — mesma escada com alvo/área diferente. O maior bolo
  restante está em Fogo (dois clusters de 6) e Marciais (cluster de 4).
- **Camada C** (155 colisões de assinatura) — inclui os 26 "dano + empurra + derruba" espalhados
  por 5 grupos, e o par **Pacto de Sangue / Aumento Sombrio** que abriu esta revisão e ainda
  não foi tocado.
- **Familiares de Conjuração**: Olhos Emprestados e Chama de Bolso têm ficha idêntica (Menor,
  ◈ + 6 Mana, vínculo permanente que não cresce) — só o efeito utilitário difere. Não é clone
  total, mas é o mesmo molde.
- **Lâmina de Sangue** causa **10d8 nas três Intensidades** — só o dreno escala. Anomalia notada
  de passagem, não investigada.


## Área vira Teste de Resistência (2026-08-26)

Leva separada, decidida logo após a Camada A. Registro completo no CLAUDE.md. Em resumo: 177 fichas,
4 arquivos de regra (`jogar/testes.md`, `habilidades/regras.md`, `glossario.md`, `jogar/combate.md`),
e a classificação de cada habilidade em `notas/area-resistencia.txt`.

Fica em aberto: as 3 classificações marcadas como julgamento meu (Metamorfose Forçada, Toque
Suspenso, Dominar os Mortos), e a pergunta de balanceamento que a mudança abre — **área nunca mais
zera** (resistir dá metade), o que a torna mais confiável do que era. Nenhum dado foi reduzido pra
compensar; se em mesa isso pesar, o ajuste é nos dados, não na regra.
