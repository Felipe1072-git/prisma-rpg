# Auditoria — Marciais, Pontaria, Infiltração, Mobilidade (relatório do subagente, salvo pelo consolidador)

Total: 37 achados — 9 alta, 18 média, 10 baixa.

## ALTA
- [COM-01] "Derrubar" sem regra (≈50 usos nos 4 arquivos; bestiario.md:252, racas:53/195, buff.md:44-46 assumem que existe). = TRA-01/ARS-03.
- [COM-02] Dança Élfica (pontaria.md:13-14) referencia "os tiers da Rajada de Flechas" — sistema removido; Rajada atual (arsenal.md:283-285) só tem Intensidades. Habilidade irresolvível.
- [COM-04] mana.md:32 (buff = Custo fixo) ↔ index.md:57-70 (buff tem Intensidade). Herdeiros: Caminho da Espada (marciais.md:39), Desaparecimento (infiltracao.md:22), Fumaça Cega (infiltracao.md:55). = TRA-10.
- [COM-05] Marciais cobra 1/3/6 igual pra 1 alvo ou área/linha 8/cone (marciais.md:50-52 vs 62-64, 110-112, 171-173, 265-267, 289-291, 313-315, 481-483, 529-531). Dano 2x também grátis (373-375, 517-519, 277-279, 241-243).
- [COM-06] Pontaria paga mais que Marciais pela mesma entrega: Investida Certeira 1/4/7 1d6 (pontaria.md:22-24) vs Carga com Lança 1/3/6 dado da arma (marciais.md:217-219); Rodamoinho de Balas 3/6/9 (55-57) vs Turbilhão de Chutes 1/3/6 (110-112); Tiro Concentrado 2/5/8 (44-46) vs Pressão Brutal 1/3/6 (337-339); Salto Certeiro 2/5/8 (33-35) vs Grilhões da Alma 2/5/8 melhor (349-351). Investida Certeira I < Ataque Básico de Arco grátis.
- [COM-07] Chute Navalha (marciais.md:361-363) = clone do Ataque Desarmado (29-31) por 2/5/8 em vez de 1/3/6; Hanuman (373-375) dá 2x dano por 1/3/6.
- [COM-08] Chute do Vento Cortante (marciais.md:158,160): "se derrubar 1 alvo, recupera 3 Mana" e a II (3 Mana) derruba automaticamente ao acertar — AoE de custo líquido zero.
- [COM-09] Destruição II (marciais.md:242): Atordoado por 2 PA + 3 Mana; Empalar (231), Golpe da Alma (507), Ataque Frenético (100) cobram a III (6 Mana) pelo mesmo; Supremas de 16 só derrubam (564).
- [COM-10] Voo sem regra: mobilidade.md:3 anuncia, nenhuma habilidade voa; racas/index.md:77,128,233 já concedem; queda/Atordoado no ar/derrubar voador indefinidos; Dragão (bestiario.md:311,325-327) tem regras próprias que o jogador não tem.

## MÉDIA
- [COM-03] Sobras de "tier" em infiltracao.md:13,32 (Choque das Sombras, Armadilha Oculta).
- [COM-11] Mão Infinita III idêntica à II (marciais.md:398-399).
- [COM-12] Escapista (infiltracao.md:65-68) diz "como Reação" mas cobra 1/2/3 PA — dedicada ou não? (pontos-de-acao.md:18).
- [COM-13] Custos fixos abaixo do valor de III: Caminho da Espada 3, Dança Élfica 3, Desaparecimento 5, Fumaça Cega 5, Postura da Sombra 4 (III válidos: 6-12/16).
- [COM-14] PA dos fixos varia 1/2/3 sem regra (marciais 3 PA; infiltracao.md:12,22,55 = 2 PA; :100 = 1 PA).
- [COM-15] Desaparecimento/Fumaça Cega não se qualificam pra Custo fixo (não são raio 3+/Suprema/absoluto; duração é eixo escalável, index.md:63-65).
- [COM-16] Postura da Sombra (0 PA + 4 fixo, anula corpo a corpo garantido, mobilidade.md:43-44) domina Cambalhota (0 PA + 2/5/8 condicional, 14-16).
- [COM-17] Escala 1/4/7 não documentada: Investida Certeira, Armadilha Oculta (33-35), Golpe Furtivo (45-47).
- [COM-18] Armadilha Oculta (infiltracao.md:32): teste ao armar, sem alvo — contra Defesa de quem?
- [COM-19] Choque das Sombras (infiltracao.md:12-14): detonação atrasada — pega quem estava no lançamento ou na detonação?
- [COM-20] Lento/Imóvel vs deslocamentos de habilidade e auto-teleporte: glossario.md:21-30 sustenta as duas leituras (Passo Sombrio, Postura da Sombra).
- [COM-21] Montaria de Guerra (mobilidade.md:65-67): sem duração e sem ficha do corcel.
- [COM-22] Multi-alvo: uma rolagem vs Defesa de cada, ou uma por alvo? index.md:87-90 só cobre 1v1; Crítico em área no limbo.
- [COM-23] exploracao.md:100 cita "Sentidos Apurados" — não existe; hoje chama "Instinto Ladino" (infiltracao.md:95-103).
- [COM-24] Supremas marciais: Erradicação (563-564, raio 3, acerta aliados) estritamente pior que Queda Celestial (594, raio 4, hostis) e Nascimento das Lâminas (681, raio 5, hostis), mesmo custo.
- [COM-25] Mergulho Furioso (632-634, 1/3/6) domina Combo Punitivo (619-621, 2/5/8) no mesmo kit.
- [COM-26] Fúria das Lâminas Gêmeas (671-673, 1/3/6, todas adjacentes) domina Corte Cruzado (658-660, 2/5/8, 2 alvos).
- [COM-27] "Ataques que exijam vê-lo" indefinido; sem furtividade em combate (infiltracao.md:23,56 ↔ testes.md:66-68).

## BAIXA
- [COM-28] Armadilha Oculta III derruba duas vezes na mesma linha (infiltracao.md:35); III = II + nada.
- [COM-29] Golpe Furtivo Crítico fixa "+2d6" ignorando a Intensidade (infiltracao.md:48).
- [COM-30] Tiro Colossal III: "e ele perde a próxima Reação" — plural→singular (pontaria.md:99).
- [COM-31] Gerais de Pontaria não exigem arma (Sentença Final 3d8 de mãos vazias).
- [COM-32] Chave "Marciais - Especial" linka pro grau de arma (3/7/12) mas custa 1/3/6 (marciais.md:38 etc. ↔ glossario.md:131-133).
- [COM-33] "Para trás"/"à frente" num jogo sem facing (mobilidade.md:24-26; marciais.md:191,287).
- [COM-34] "Perde a próxima Reação" sem prazo (marciais.md:31 e dezenas).
- [COM-35] Empurrar/puxar sem regra de colisão (parede, criatura, precipício, Zona Amaldiçoada).
- [COM-36] Rótulo "(Maior)" inconsistente em pontaria.md:60,91 vs :49 sem rótulo, mesmo teto.
- [COM-37] Arrombamento I: 1 PA + "a Ação Básica inteira"? (infiltracao.md:90).

## Lições
Sólido: Dano Desarmado coerente nas 3 pontas; aritmética das escalas certa dentro da ficha; Infiltração usa bem a tabela de Defesas; Reações dedicadas de Mobilidade seguem o template; as 5 Supremas custam 16.
Quebrou em padrão: preço não conversa com entrega (área/dado 2x grátis em Marciais; Pontaria taxada); "Custo fixo" virou zona franca (sem valor de III, sem PA padrão); remoção dos Tiers deixou cadáveres (grep "tier"); efeitos mais usados são os menos definidos (derrubar, perde Reação, empurrar, área); Mobilidade promete Voo e não entrega; renomeações vazam ("Sentidos Apurados").
