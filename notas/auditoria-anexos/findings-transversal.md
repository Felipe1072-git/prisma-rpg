# Achados transversais (auditoria do consolidador)

## [TRA-01] "derrubado" é usado em todo o sistema e nunca é definido
- Severidade: alta — Confiança: alta
- Onde: usado em docs/jogador/arsenal.md:203,225, docs/habilidades/magicas-elementais.md:1245-1305, docs/habilidades/debuff.md:248-249, docs/habilidades/buff.md:44-46,216-218,297,434-486, docs/racas/index.md:53,195, docs/mestre/bestiario.md:252 ↔ definição: inexistente (glossário não tem entrada)
- O quê: dezenas de habilidades derrubam; raças e buffs prometem "não pode ser derrubado"; o Bestiário dá bônus "contra alvo já derrubado" (2d8 em vez de 1d8). Mas nenhum texto diz o que estar derrubado FAZ: perde movimento? ataques contra ele têm Vantagem? levantar custa ◈? Além disso o nome colide com "Caído" (sistema-d20.md:137), que é o estado de 0 de Vida.
- Na mesa: o jogador paga Intensidade III pra derrubar o chefe e pergunta "tá, e daí?" — o livro não responde. E quando alguém diz "estou caído", a mesa não sabe se é chão ou morte.

## [TRA-02] Vantagem/Desvantagem: 87 usos, definição só no Livro do Mestre
- Severidade: alta — Confiança: alta
- Onde: docs/mestre/testes.md:88-89 (única definição) ↔ 87 ocorrências em 14 arquivos, inclusive origem.md (40), sociais.md (9), debuff.md (5); glossário: sem entrada
- O quê: a mecânica mais usada do sistema é definida numa lista de ferramentas do Mestre. Algumas habilidades re-explicam inline ("rola 2x e fica com o pior" — mobilidade.md:24), a maioria não. E o empilhamento é indefinido: duas fontes de Vantagem? Vantagem e Desvantagem ao mesmo tempo (ex.: Exausto grau 1 + Marcado no mesmo ataque)?
- Na mesa: jogador que só leu o Livro do Jogador e o Glossário não encontra a regra; e a primeira vez que Vantagem e Desvantagem coincidirem, a sessão trava.

## [TRA-03] "rodada" tem 245 usos e nenhuma definição
- Severidade: alta — Confiança: alta
- Onde: 245 ocorrências em 14 arquivos (buff.md sozinho tem 120) ↔ definição: inexistente; convive com "turno" (condições padrão duram "até o fim do próximo turno do alvo", glossario.md:7)
- O quê: durações inteiras do sistema ("por 2 rodadas", "1d4 rodadas") dependem de um termo que nunca é ancorado: uma rodada começa e termina quando? No turno de quem expira o efeito?
- Na mesa: buff de "3 rodadas" ativado no meio da ordem de iniciativa — ninguém sabe se conta a rodada corrente, nem em que turno cai.

## [TRA-04] Marcado, como escrito, quase nunca pode disparar
- Severidade: média — Confiança: alta
- Onde: docs/glossario.md:38 ("O próximo ataque de um aliado contra ele neste turno rola com Vantagem") ↔ docs/jogador/arsenal.md:601-602 (mesma redação)
- O quê: se "turno" é individual (como em todo o resto do sistema), o aliado só ataca no turno DELE — que não é "neste turno". A janela só existe se aqui "turno" significar "rodada", o que reforça o TRA-03.
- Na mesa: jogador paga Intensidade II pra Marcar, aliado ataca no próprio turno, e o Mestre precisa decidir na hora se a Vantagem ainda vale.

## [TRA-05] "Desprevenido" citado e nunca definido
- Severidade: média — Confiança: alta
- Onde: docs/jogador/origem.md:22 ("Órfão de Rua — Nunca fica Desprevenido no primeiro turno de um combate") ↔ definição: inexistente (única ocorrência do termo em docs/)
- O quê: o traço protege de um estado que nenhuma regra cria. Não existe regra de surpresa/emboscada.
- Na mesa: o traço é letra morta — o jogador que o pegou nunca vai usá-lo, e o Mestre não sabe o que aplicar aos demais no 1º turno.

## [TRA-06] "efeitos de Medo" citados e mecânica de Medo inexistente
- Severidade: média — Confiança: alta
- Onde: docs/jogador/origem.md:60 (Floresta Amaldiçoada) e :75 (Testemunhou algo Sobrenatural) ↔ definição: inexistente (nenhuma condição/mecânica de Medo em docs/)
- O quê: dois traços dão Vantagem contra "efeitos de Medo", categoria que nenhuma habilidade ou criatura produz nominalmente (o mais próximo é a linha de Defesa "Mental/comportamental (charme, medo, provocação)" em sistema-d20.md:210, que é atributo de teste, não um efeito rotulado).
- Na mesa: o Mestre precisa decidir caso a caso o que "conta como Medo" — exatamente o tipo de pergunta que o livro deveria responder.

## [TRA-07] "agarrado" citado como estado, sem regra de agarrão
- Severidade: média — Confiança: alta
- Onde: docs/jogador/tocado.md:76 ("Funciona mesmo estando Imóvel ou agarrado") e docs/habilidades/infiltracao.md:65 ("amarrado, algemado, agarrado") ↔ regra de agarrar: inexistente
- O quê: dois textos tratam "agarrado" como estado conhecido; nenhuma habilidade, ação ou condição define como alguém agarra ou o que o agarrado sofre (o Chicote "puxa e prende", glossario.md:371, sem mecânica de prisão).
- Na mesa: monstro agarra um PJ (cena óbvia de jogo) e não há regra nenhuma pra resolver.

## [TRA-08] A tabela de PA lista "Reação — ◈ (1)", mas nenhuma Reação custa isso
- Severidade: alta — Confiança: alta
- Onde: docs/jogador/pontos-de-acao.md:12 (tabela: "Reação | ◈ (1) — consome do mesmo pool") ↔ docs/jogador/pontos-de-acao.md:16-18 (texto: habilidade usada como Reação paga o custo NORMAL dela, 1-3 PA; Reações dedicadas custam 0 PA)
- O quê: na mesma página, a tabela diz que Reação custa 1 PA fixo e o texto diz que custa o PA da habilidade (ou zero). Os dois não podem valer juntos.
- Na mesa: jogador quer reagir com habilidade em Intensidade II — paga 1 (tabela) ou 2 (texto)?

## [TRA-09] Estresse: quantidade indefinida nos dois gatilhos principais
- Severidade: média — Confiança: alta
- Onde: docs/jogador/sistema-d20.md:263 (gatilhos: sofrer crítico, 1 natural, teste pedido) ↔ docs/jogador/sistema-d20.md:267 (só o teste falho quantifica: "1-2 pontos", sem dizer quem escolhe 1 ou 2)
- O quê: sofrer um crítico e tirar 1 natural geram Estresse em quantidade que nenhum texto dá. (A Katana Muramasa, arsenal.md:1219, precisou definir "1 ponto" por conta própria.)
- Na mesa: primeiro crítico sofrido da campanha, e o Mestre inventa o número.

## [TRA-10] Buffs têm Intensidade ou são Custo fixo? As duas páginas discordam
- Severidade: média — Confiança: alta
- Onde: docs/jogador/mana.md:32 ("Habilidades de Custo fixo (áreas de raio 3+, Supremas, buffs) cobram o valor da Intensidade III") ↔ docs/habilidades/index.md:57-70 ("Buffs, Suporte e Mobilidade também têm Intensidade", com exemplos nomeados) e a prática de buff.md (Intensidades em quase tudo)
- O quê: mana.md coloca "buffs" na lista de Custo fixo, sem qualificação; habilidades/index.md dedica uma seção inteira a dizer o contrário. O CLAUDE.md fala "buffs sem rolagem" — a palavra "sem rolagem" se perdeu em mana.md.
- Na mesa: jogador lê mana.md e conclui que todo buff cobra o custo cheio; a ficha do buff diz outra coisa.

## [TRA-11] Ferimento Amaldiçoado: "não cicatriza" vs efeito de uma vez só
- Severidade: média — Confiança: alta
- Onde: docs/jogador/arsenal.md:146 ("causa um Ferimento Amaldiçoado, que não cicatriza por cura normal") ↔ docs/jogador/arsenal.md:2195 ("como Sangrando — perde 1d4 no início do próximo turno — mas não pode ser removido ou curado por nenhum efeito até terminar o curso")
- O quê: Sangrando é "efeito de uma vez só — ferida que fecha" (glossario.md:11). Se o Ferimento é "como Sangrando", o curso dele é 1 tick — e "não pode ser curado até terminar o curso" protege por um turno, o que torna vazia a promessa de ferida que "não cicatriza".
- Na mesa: o alvo toma 1d4 uma vez e o efeito acaba — ou o Mestre rala pra decidir se a ferida persiste dias. As duas leituras cabem no texto.

## [TRA-12] Equipamento inicial definido de dois jeitos
- Severidade: média — Confiança: alta
- Onde: docs/jogador/sistema-d20.md:11 ("Equipamento inicial — a arma (ou armas) que o personagem carrega, escolhida livremente") ↔ docs/jogador/introducao.md:55 ("a arma que você carrega, armadura, e 50 de prata")
- O quê: a página canônica de criação não menciona armadura nem dinheiro; a introdução dá armadura e 50 prata. Nenhuma das duas diz se a arma/armadura inicial é grátis (armas custam 40-200p no arsenal, armadura Pesada 250p) nem se vale escolher arma com Requisito de Atributo alto.
- Na mesa: um jogador começa com Escudo Torre (200p) de graça e outro compra com os 50p? Cada mesa decide diferente.

## [TRA-13] Contagem oficial (574 habilidades, "nove grupos") não bate com o conteúdo
- Severidade: baixa — Confiança: alta
- Onde: docs/index.md:5,9,25 e docs/jogador/introducao.md:7,54 ("574") ↔ contagem real de fichas com linha "**Chave:**": 573 (sendo 2 delas raciais gratuitas, em racas/index.md:97,322); docs/index.md:44 diz "os nove grupos" ↔ habilidades/index.md lista 10
- O quê: os números-vitrine divergem do conteúdo real por 1 habilidade e 1 grupo.
- Na mesa: sem efeito direto — mas é o tipo de furo que mina confiança no material publicado.

## [TRA-14] "Escudo" nomeia duas mecânicas diferentes
- Severidade: baixa — Confiança: média
- Onde: docs/glossario.md:49 (condição Escudo: pontos temporários que absorvem dano) ↔ docs/jogador/arsenal.md:161-171 (item Escudo: bônus passivo de Defesa)
- O quê: mesma palavra pra duas mecânicas sem parentesco. O Mangual "ignora bônus de Escudo na Especial" (glossario.md:375) — o arsenal.md:1615 esclarece que é o item, mas o glossário não distingue.
- Na mesa: "ele tem Escudo" — de Defesa ou de pontos? Toda vez precisa perguntar.

## [TRA-15] Avatar Nephilim é rotulado "(Maior)" com teto de Mana na faixa Suprema
- Severidade: média — Confiança: alta
- Onde: docs/habilidades/buff.md:478 ("**Avatar Nephilim** *(Maior)*") e :486 (Intensidade III = 16 Mana) ↔ docs/jogador/mana.md:38-43 (Grau de Poder mede o TETO, o custo da III: Maior = 9-15, Supremo = 16+) e docs/habilidades/index.md:54 (Supremas 16+ ficam fora da escala de Intensidade, com Custo fixo)
- O quê: pelo critério oficial (teto = custo da III), Avatar Nephilim com III a 16 Mana é Supremo — mas está rotulado Maior e mantém Intensidades I/II/III, o que a regra das Supremas não permite. Ou o rótulo está errado, ou o custo, ou "Supremo" não é uma faixa automática (e aí mana.md precisa dizer isso).
- Na mesa: dúvida sobre se a habilidade segue a regra Suprema ("1x por descanso, possivelmente com restrição extra") ou não.

## [TRA-16] 12 habilidades com rótulo de Grau de Poder fora da própria faixa de custo
- Severidade: média — Confiança: alta
- Onde: verificação mecânica (script) do rótulo *(Grau)* contra o teto de Mana (custo da III ou do Custo fixo), régua em docs/jogador/mana.md:38-43 (Menor 1-3, Moderado 4-8, Maior 9-15, Supremo 16+)
- O quê: 12 habilidades rotuladas fora da faixa:
  - buff.md:200 Transformação da Deusa (Maior) teto 16 → faixa Suprema
  - buff.md:478 Avatar Nephilim (Maior) teto 16 → faixa Suprema (ver TRA-15)
  - debuff.md:328 Chuva de Sangue (Maior) Custo fixo 8 → faixa Moderado
  - magicas-elementais.md:254 Campo Estático (Maior) fixo 8 → Moderado
  - magicas-elementais.md:272 Convergência Elétrica (Maior) fixo 8 → Moderado
  - magicas-elementais.md:504 Soco Ígneo (Maior) III=8 → Moderado
  - magicas-elementais.md:526 Trilha de Fogo (Maior) fixo 8 → Moderado
  - magicas-elementais.md:546 Queda Meteórica (Maior) fixo 8 → Moderado
  - magicas-elementais.md:566 Explosão Extrema (Maior) fixo 8 → Moderado
  - magicas-elementais.md:595 Lança Espiritual (Maior) III=8 → Moderado
  - magicas-elementais.md:897 Lamento Uivante (Maior) fixo 8 → Moderado
  - magicas-elementais.md:906 Paixão Interna (Maior) III=8 → Moderado
- Na mesa: o Grau de Poder é a régua declarada de "quantas vezes por descanso" (mana.md:38-43) — rótulo errado calibra expectativa errada de frequência de uso; e dez "Maior" a 8 Mana são, na prática, mais baratas que o grau anuncia.

## Observação fora de docs/
- CLAUDE.md diz "574 habilidades nos 9 grupos" — docs têm 10 grupos (Suporte entrou depois). Atualizar junto com o TRA-13.
