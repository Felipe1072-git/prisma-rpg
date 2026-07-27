# Auditoria — docs/habilidades/magicas-elementais.md (relatório do subagente, salvo pelo consolidador)

Total: 34 achados — 8 alta, 16 média, 10 baixa.

## ALTA
- [ELE-01] "Derrubar" assinatura de 3 elementos (Terra/Água/Vento, linhas 16-18, 35-37, 46-48, 96, 1245, 1318...) sem definição em lugar nenhum. = TRA-01.
- [ELE-02] Aceleração Temporal (1554-1561): Custo fixo 2 PA + 9 Mana pra ganhar +1 PA "neste turno" — efeito líquido NEGATIVO (termina com menos PA que sem usar).
- [ELE-03] Impacto Profundo (637-646): "todas as criaturas hostis no campo de batalha" com Intensidades desde 1 PA + 3 Mana (2d6 + Queimando em todos) — viola Custo fixo raio 3+ e supera a Suprema Julgamento Caótico (16 Mana, 617-624).
- [ELE-04] Astrape Sombria (213-220): Atordoado automático sem teste em até 5 alvos por 2 PA + 7 — mais barato que Relâmpago III (3 PA + 8, rolado, 1 linha).
- [ELE-05] Lâmina de Sangue (1447-1457): II idêntica à I custando mais; escala real metade/metade/total contra assinatura metade/total/dobrado (linha 22); sem linha de Risco apesar do "sempre sob Risco".
- [ELE-06] Pares idênticos com preços diferentes: Bomba Shuju (1248-1257, 4/7/10) ↔ Correntes de Água (1268-1277, 2/5/8); Picada Tóxica (1394-1403, 4/7/10) ↔ Toque Debilitante (1414-1423, 2/5/8); Punho Flamejante (492-502, 3/6/9) ↔ Força Desesperada/Chama Investida/Rastro Flamejante (2/5/8); Chama Espelhada (3/6/9) ↔ Chama Solar (2/5/8); Alma em Chamas (2/5/8) ↔ Impacto Meteórico/Explosão de Fogo (3/6/9); Círculo do Destino (3/6/9) ↔ Força Flamejante (2/5/8); Lança Espiritual (2d6, linha 10, 2/5/8, "Maior") ↔ Lança de Fogo (1d8, linha 12, 3/6/9); Abraço das Profundezas (4/7/10) ↔ Estrela Cadente Desperta (igual + investida, 3/6/9).
- [ELE-07] Zonas de elementos diferentes sobrepostas sem regra (não-soma do glossário presa à Zona Amaldiçoada/Sombras): Rastro em Chamas, Trilha de Fogo, Campo Estático, Zona Mortal, Aparar, Floração Eterna, Névoa Corrosiva, Poça d'Água, Bolha Temporal, Muralha de Sangue. Leitura literal empilha 3×1d6/rodada.
- [ELE-08] Custo fixo fora das exceções (alvo < raio 3, não-Suprema, efeito graduável), quase todos automáticos sem teste: Astrape (218), Pulso Eletrônico (268), Ataque Orbital (297), Rastro em Chamas (411), Trilha de Fogo (531), Chama Amaldiçoada (432, 1 criatura!), Aparar (758), Brilho Caótico (767), Esfera das Trevas (776), Véu Sombrio (813), Selo Sombrio (995), Oráculo (1201), Tempestade Caótica (1232), Poça d'Água (1264), Névoa Corrosiva (1410), Bolha Temporal (1550), Muralha de Sangue (1516), Lacaio Reanimado (1128). Casos-limite ok: Muralha de Pedra (65), Olhos do Vento (1377).

## MÉDIA
- [ELE-09] Investida Encadeada (152-159): Maior 9 Mana auto-hit (1d10 + Atordoado raio 3 sem teste) supera a Suprema de 16 do Gelo; Atordoado é assinatura do Raio, não do Gelo.
- [ELE-10] Supremas de 16 desiguais: Chamas Espirituais (1 alvo aleatório) vs Raios e Relâmpagos (campo inteiro); Olho Maligno (16) < Foco Sombrio (Maior, 9); Horizonte de Eventos (2d6) < Fonte da Explosão (2d8) mesmo preço/elemento.
- [ELE-11] Críticos de Custo fixo com efeito extra (~25 linhas: 88, 141, 150, 179, 252, 352, 553, 573...) contra index.md:92 ("apenas o bônus de dano"); Chuva Gélida (140-141) e Colheita Vermelha (1495-1496) critam PIOR que o acerto.
- [ELE-12] "Petrificado" (crítico de Petrificar, linha 38) não existe no glossário — única ocorrência em docs/.
- [ELE-13] Rótulos de grau incoerentes: nove "(Maior)" com teto 8; dezenas com teto 9-11 sem rótulo (Emboscada 9, Tremor 10, Chuva de Meteoros 10, Golpe Supremo 10 — "Supremo" no NOME de não-Suprema, Fenda Profunda 11, Corte Caótico 10, Pisada Colossal 11, Lanças Sombrias 10, Raio Laser 10, Buraco Negro...). = TRA-16.
- [ELE-14] Espalhamento do Queimando (padrão ~20x em Fogo, ex. 361-362): quem escolhe o alvo? Pega aliados? Encadeia na III?
- [ELE-15] Buffs com Custo fixo (Couraça de Pedra 51-58, Véu de Vapor 1279-1286, Passos do Vento 1354-1361, Pacto de Sangue 1459-1466) herdam o lado de mana.md:32 que index.md:57 rejeita. = TRA-10.
- [ELE-16] Esferas Sombrias I (1118): cláusula de dreno duplicada na mesma linha (metade + metade = total, igualando a II).
- [ELE-17] Buraco Negro (1640-1642): dois teleportes contraditórios na I; a identidade (puxar pra adjacente ao usuário) some na II/III.
- [ELE-18] Chuva de Espinhos Vermelhos III (1476): dois drenos empilhados ("1d6 por alvo" + "dobro do dano") sem regra de soma; padrão dos irmãos é só "dobro".
- [ELE-19] Praga Definitiva crítico (1443): "-1 em todos os atributos físicos" sem duração nem definição de "atributos físicos".
- [ELE-20] Detonação de Choque (245-252) vs Nevasca (143-150): mesmo preço/forma, Raio dá Atordoado onde Gelo dá Imóvel (degrau abaixo).
- [ELE-21] Assinaturas vazando: Gelo dá Atordoado (110, 150, 158, 179); Sombras empurra (1046-1047, 805), dá Lento (845, 894, 945), Sangrando (883, 1023-1025) e Atordoado (823, 872, 987).
- [ELE-22] Lacaio Reanimado (1123-1130): invocação sem Defesa, ataque "automático" sem teste declarado, sem limite de lacaios simultâneos.
- [ELE-23] Zonas "só hostis" (750, 260, 412, 532, 863) contradizem a filosofia da Zona Amaldiçoada ("fere todo mundo... não dano grátis", glossario.md:82); Névoa Corrosiva (1411) fere todos — sem padrão.
- [ELE-24] Dominâncias: Peso das Trevas (1d6) < Vazio (1d8) mesmos 3/6/9; Fissura Dimensional < Eco do Passado (igual + eco, mesmo preço); Carícia da Morte < Redemoinho Sombrio; Lança Ilusória (1d6, 3/6/9) < Relâmpago (1d8, 2/5/8).

## BAIXA
- [ELE-25] Selo Sombrio (996) e Bolha Temporal (1551) reinventam Imóvel e Lento sem os termos — imunidades pegam?
- [ELE-26] Gelo/Água sobre alvo Queimando: apaga? Nenhuma ficha diz (glossario.md:18 delega "água em quantidade" ao Mestre).
- [ELE-27] Soco Ígneo (509) e Punho Escaldante (560) sem linha de Alcance.
- [ELE-28] Investida Explosiva (515-524) sem a chave "Investida:"; Filo da Alma (1095-1096) desloca só na I. = ARS-10.
- [ELE-29] "Perde 2 Mana" (rider de ~10 habilidades de Sombras) é nulo contra Comum/Treinado (sem Mana, bestiario.md:91).
- [ELE-30] Críticos incompletos: Tremor (88, Terreno Difícil onde/quanto tempo?), Ira do Rei (1305, puxa sem direção), Fúria do Vendaval (1387-1388, acerto empurra 6 / crítico PUXA 2).
- [ELE-31] Duplicatas exatas: Força de Choque = Descarga Carregada; Voragem = Libertação Limitada; Vórtice das Trevas = Frenesi Sombrio; 3 investidas de Fogo idênticas.
- [ELE-32] Fúria da Natureza (29-38, cone 3) dominada por Petrificar? Não — inverso: Petrificar (41-49, raio 2 a 8 casas, mesmos efeitos/custo) domina; único trunfo o crítico sem regra.
- [ELE-33] Choque Maligno III (729-730) não entrega o "dreno crescente" da assinatura de Sombras (idem Esfera Voraz, Rajada Sombria).
- [ELE-34] Atributo misto dentro do elemento: Chamas Espirituais (SAB, único em Fogo); Luz metade INT (1138, 1169, 1190) metade SAB (1201, 1210, 1221).

## Lições
Sólido: ~60 habilidades com Intensidade — zero quebras de escada; Tiers só em Ressuscitar; área nunca escala; Zona Amaldiçoada nomeada segue o glossário nas ~15 ocorrências; Veneno exemplar (3 acúmulos + Defesa por Vitalidade declarada); Rajada Evasiva é a Reação dedicada perfeita; as 17 Supremas custam 16.
Padrões: camada "automático sem teste" é um sistema paralelo sem regra-mãe (~25 não-Supremas); glossário uma condição atrasado do uso real; regra de zonas presa a Sombras; index vs mana sobre buffs; index.md:92 contrariado por ~25 críticos; template deixou cicatrizes (duplicações, gêmeas com preços divergentes).
