# Auditoria — docs/pacotes/index.md (relatório do subagente, salvo pelo consolidador)

Total: 13 achados — 3 alta, 5 média, 5 baixa.
Cobertura: 100/100 pacotes; 1.000 linhas de trilha (padrão 1-3-5...19 sem violação); ~1.100 checagens de nome com ZERO referência quebrada; ordem Básica→Avançada→Especial sem violação; anotações (Supremo)/(Maior)/(Dupla Empunhadura) 100% corretas.

## ALTA
- [PAC-01] Centurião (pacotes:619,625,29): Lança (Duas Mãos, arsenal.md:56) + Escudo Leve + Bloqueio nv3 — escudo exige arma Leve na mão principal (arsenal.md:163, 114). Conceito fala "lança curta" que não existe.
- [PAC-02] Vanguarda (pacotes:2099-2113): Espada + Escudo Torre — o Torre "ocupa as duas mãos sozinho, não pode equipar nenhuma arma junto" (arsenal.md:169). Trilha depende das duas coisas. Templário (2079, Escudo Leve) é a versão correta.
- [PAC-03] Paladino do Juramento (pacotes:1729-1743): idêntico ao PAC-02.

## MÉDIA
- [PAC-04] Encantador (939/944) e Skald (1997/2002): Violino exige Vontade +4 (arsenal.md:2558), teto de criação é +3 — inequipável no nv1 sem raça específica; e Violino ataca com Força, não com o foco (Vontade).
- [PAC-05] Portador da Luz (1833/1838): Lâmpada exige Int +5 — idem, trancada até nv4 na maioria das combinações.
- [PAC-06] Lanceiro nv17 (1416-1419): Investida Dupla exige Lança + Espada simultâneas — Lança é Duas Mãos (três mãos necessárias); exceção só existe pro par de katanas (arsenal.md:157).
- [PAC-08] 16 pacotes com "Atributo em foco" disjunto do atributo de ataque da arma inicial (pacotes:156, 256, 296, 680, 760, 780, 940, 1042, 1082, 1182, 1526, 1648, 1752, 1854, 1998, 2142) — ex.: Necromante (Int × Foice/Força), Profeta (Sab × Cajado/Int).
- (reclassificação do agente: PAC-07 baixa)

## BAIXA
- [PAC-07] Retalhador (1895,1911): Nodachi + Muramasa (duas Duas Mãos) sancionado em arsenal.md:157 mas contradiz arsenal.md:114 que não menciona a exceção.
- [PAC-09] Pirata (78, 1791-1805): "pistola numa mão, sabre na outra" impossível — ambas são pares indivisíveis.
- [PAC-10] Mentalista (52 vs 1465): conceito "sem arma visível" × arma inicial Olho Mágico.
- [PAC-11] Mago de Sangue (50 vs 1445): conceito "adagas" × kit com Manual.
- [PAC-12] Caçador de Recompensas (73 vs 495-511): conceito "boleadeiras, redes, espadas curtas" × kit de 4 armas de fogo; boleadeiras/redes não existem no arsenal.
- [PAC-13] Clérigo da Guerra (102 vs 659): conceito "maças pesadas e escudos de ferro" × Martelo Duas Mãos que proíbe escudo.

## Lições
Sólido: nomenclatura impecável (1.100 citações, zero erro); progressão e pré-requisitos respeitados nos 100; estrutura tabela↔detalhe íntegra.
Quebrou: empunhadura é o ponto cego (3 de 5 kits com escudo impossíveis — regra do Torre parece posterior aos pacotes); requisitos de arma nunca cruzados com o teto +3 da criação; tabelas de vertente divergiram dos detalhamentos; Dupla Empunhadura em contradição não-documentada com a regra de Leve; "Atributo em foco" não conversa com a arma inicial em 16 pacotes.
