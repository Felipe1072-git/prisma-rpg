# Auditoria — docs/jogador/arsenal.md (relatório do subagente, salvo pelo consolidador)

Resumo: 21 achados — alta: 4 (ARS-01 a 04) · média: 11 (ARS-05 a 15) · baixa: 6 (ARS-16 a 21).
Dados de dano das 62 armas conferidos contra o glossário: 100% batem. Escala de Mana respeitada em ~180 de ~186 habilidades.

## [ARS-01] Manopla Mística Especial custa 3 Mana onde a escala manda 12 — alta/alta
- arsenal.md:1696 ↔ mana.md:28,32. Guardião Invocado: "Custo fixo: ◈◈◈ (3 PA) + 3 Mana", dano automático sem teste (1d8 + 1d8/rodada × 2 = 3d8 garantidos). Especial deveria custar 12 no fixo. Na mesa: ~13,5 de dano que não erra, 4+ vezes por combate, nível 1.

## [ARS-02] Espada Senciente entrega Atordoado na Intensidade I — alta/alta
- arsenal.md:809 ↔ habilidades/index.md:40-42. Golpe Colossal I (1 PA + 3 Mana): 2d12 + Atordoado. Atordoado é efeito canônico de III; equivalentes cobram 2 PA + 5-7 Mana no mínimo. Na mesa: apaga o turno do alvo por 1 PA e sobram 2.

## [ARS-03] "Derruba o alvo" (117+ usos) sem definição de Derrubado — alta/alta
- arsenal.md:245,284,358… ↔ glossario.md:5-65 (sem entrada). Bestiário dá bônus contra alvo derrubado (bestiario.md:252); buffs prometem "não pode ser derrubado". Nada diz o que derrubado faz. (= TRA-01.)

## [ARS-04] Chicote Avançada: Intensidade II idêntica à I por mais que o dobro do custo — alta/alta
- arsenal.md:639 ↔ 640. Chicotada em Arco I (1 PA+2): "2d6 + empurra 1 casa cada alvo"; II (2 PA+5): idêntica. Degrau morto.

## [ARS-05] Nove Avançadas de área raio 3 com Custo fixo de 2 PA + 9 Mana — média/alta
- arsenal.md:293,525,562,679,1447,1724,1958,1993,2145 ↔ mana.md:32 e arsenal.md:17. Custo fixo deveria cobrar o valor da III (3 PA); a exceção escrita no topo só cobre Especiais. Padrão uniforme, sem regra escrita.

## [ARS-06] Punhal: Efeito Especial promete Ferimento Amaldiçoado "na III/Crítico", ficha aplica na II — média/alta
- arsenal.md:146 ↔ 2195-2196. E a III diz "o Sangrando causa 2d4" mas a habilidade nunca aplica Sangrando (aplica Ferimento Amaldiçoado).

## [ARS-07] Módulo Alado viola "toda arma tem exatamente uma de Leve/Duas Mãos" — média/alta
- arsenal.md:27,110 ↔ 106,118. "(especial — não é empunhado)": pode empunhar arma junto? Escudo? Indecidível.

## [ARS-08] Glossário chama Módulo Alado e Manopla Mística de "arma marcial"; arsenal as põe como Arcano/Inteligência — média/alta
- glossario.md:239,363 ↔ arsenal.md:102,106,1674,1865.

## [ARS-09] Armas "em par" com chave Leve — mão secundária livre ou não? — média/alta
- arsenal.md:113-116 ↔ 85,2086 (Pistolas) e Adagas:41, Garras:42, Sabres:44, Tonfas:45, Bestas:80, Rapiers:37. Par ocupa as duas mãos mas a chave Leve promete mão livre (Escudo? segundo par?).

## [ARS-10] Deslocamento do usuário só na Intensidade I das habilidades de salto/investida — média/alta
- arsenal.md:766-768 (Espada, Crítico X) e mesmo padrão em 418-420, 340-342, 945-947, 1064-1066, 1103-1105, 1146-1148, 1197-1199, 1810-1812, 1877-1879, 2029-2031, 1416-1418, 457-459, 1242. II/III reescrevem tudo menos o deslocamento — na convenção do arquivo, lê como "não se move".

## [ARS-11] Sangrando reaplicado/dobrado sem regra de acúmulo — média/média
- glossario.md:9-11 ↔ arsenal.md:745, 997, 1047, 1127, 1287, 2020, 2185, 2609… "Sangrando 2d4" sobre alvo já Sangrando 1d4: soma? substitui? renova?

## [ARS-12] Marcado aplicado no próprio turno quase nunca faz nada — média/média
- glossario.md:36-38 ↔ arsenal.md:283, 1006-1008, 1725, 2470-2471. (= TRA-04.)

## [ARS-13] Terreno Difícil criado por habilidade sem duração nem extensão — média/alta
- arsenal.md:294-295 (Chuva de Flechas), 611-612 (Círculo da Perdição) ↔ glossario.md:71-75. Duração só existe pra Zona Amaldiçoada.

## [ARS-14] Pique Básica II dá 2d10 onde as irmãs de 1d10 dão 1d10, mesmo custo — média/média
- arsenal.md:2019 ↔ 1473 (Lança), 985, 1024, 1594, 1187. Sem Risco/propriedade que justifique.

## [ARS-15] AoE de graça entre armas de mesmo dado/grau — média/média
- arsenal.md:1787 (Martelo, adjacentes) ↔ 1553 (Machado, 1 alvo); 356 (Balista, linha 12) ↔ 1826 (Metralhadora, 1); 434 (Bestas, 2 alvos) ↔ 2095 (Pistolas, 1); 2349/1493 ↔ 1005. Mesmo preço, multi-alvo grátis.

## [ARS-16] Adagas Básica: Crítico com valores fixos da Intensidade I — baixa/alta
- arsenal.md:205 ↔ 204. "dano máximo (4) + 1d4" não escala pra III (2d4).

## [ARS-17] Tridente Avançada: "puxa 3 casas" duplicado e Lento que some na II — baixa/alta
- arsenal.md:2458 ↔ 2459.

## [ARS-18] Espingarda Especial: "ignora Armadura" duas vezes na mesma linha — baixa/alta
- arsenal.md:889 ↔ 1657 (forma correta na Manopla).

## [ARS-19] Égide: o escudo do pacote dá bônus de Defesa/Bloqueio? — baixa/média
- arsenal.md:73,118 ↔ 163-171, 692-696. Texto não afirma nem nega.

## [ARS-20] "Perde a próxima Reação" × Reações dedicadas (0 PA, "sempre disponíveis") — baixa/média
- arsenal.md:204,246,285… ↔ pontos-de-acao.md:16-18. Bloqueia dedicadas ou não?

## [ARS-21] Lâmina do Crepúsculo tem Risco mas não tem a chave "Efeito Especial" — baixa/alta
- arsenal.md:64,142-149 ↔ 1357.

## Lições (do subagente)
- Espinha dorsal aguenta: dados 100%, escala de Mana ~97%.
- Problemas graves estão nas habilidades que fogem do template.
- Alcance/área nunca escalam com Intensidade — verificado, intacto.
- O maior buraco está embaixo do arsenal: derrubado, acúmulo de Sangrando, janela do Marcado (dívidas do glossário).
- Convenção de reescrever o efeito completo por Intensidade falha no deslocamento (ARS-10).
- Custo fixo tem categoria não escrita: "Avançada raio 3+" (◈◈ + 9) — padrão uniforme, falta escrever a regra.
- Multiplicar alvos é de graça no arsenal — sem sobrepreço sistemático.
