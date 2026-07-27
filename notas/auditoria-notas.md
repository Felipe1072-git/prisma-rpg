# Notas da Auditoria de Consistência — 2026-07-27

Lições sobre como o sistema se encaixa, descobertas durante a auditoria completa de `docs/`.
Uma lição por bloco, resumo em negrito no topo de cada uma. Registra o que quebrou E o que
se confirmou sólido — só o que se enxerga cruzando arquivos, não o que cada arquivo já diz.

## O glossário segura; o vocabulário fora dele é que quebra

**As condições formalizadas no glossário são consistentes — os buracos estão nos termos que todo mundo usa e ninguém formalizou.** Sangrando, Queimando, Envenenado, Imóvel etc. são citados por link e com o significado certo em todos os arquivos que verifiquei. Mas o sistema inteiro se apoia num segundo vocabulário informal — "derrubado" (dezenas de usos, até bônus de Bestiário contra alvo derrubado), "Vantagem/Desvantagem" (87 usos, definição só em testes.md do Mestre), "rodada" (245 usos), "agarrado", "Desprevenido", "Medo" — que nunca ganhou definição. A lição: no Prisma, o risco não está no que foi formalizado, está no que parecia óbvio demais pra formalizar.

## Referências nomeadas entre arquivos conferem

**Toda promessa nominal de "ver habilidade X em Y" que testei existia de verdade.** Bloqueio (arsenal → buff.md:515), Impulso da Soqueira (arsenal → mobilidade.md:47), Esferas Sombrias (arsenal → elementais:1112), e o exemplo didático Corte Duplo da introdução bate número por número com a ficha real em marciais.md:43. A disciplina de linkar por nome segurou a integridade — as vitrines estão sincronizadas com o conteúdo.

## Regra nova convive com texto antigo sem revisão retroativa

**Quando uma regra evoluiu, as páginas mais antigas não foram atualizadas juntas.** O caso claro: buffs ganharam Intensidade (habilidades/index.md dedica seção a isso), mas mana.md:32 ainda lista "buffs" entre as habilidades de Custo fixo, sem o qualificador "sem rolagem" do CLAUDE.md. Mesmo padrão no equipamento inicial (sistema-d20 dá só a arma; a introdução, escrita depois, dá arma + armadura + 50 prata). A lição: cada decisão de design nova precisa de um grep pelas formulações antigas dela.

## A camada numérica é disciplinada; a camada de rótulo não acompanhou

**Verificação mecânica de todo o sistema: zero violações de PA = Intensidade e zero triplas de Mana fora das escadas sancionadas (1/3/6, 2/5/9, 3/7/12, +3/+3) — mas 12 habilidades carregam rótulo de Grau de Poder fora da própria faixa de custo.** Os números finos (custos linha a linha) foram mantidos com rigor de template; o metadado de classificação ("Maior", "Supremo") descolou — 10 "Maior" custam 8 (faixa Moderado) e 2 "Maior" custam 16 (faixa Suprema). A lição: o que o template força, fica certo; o que é julgamento manual por cima do template, deriva.

## Links e âncoras internas: zero quebradas

**Script conferiu toda âncora `[...](arquivo#ancora)` de docs/ contra os headings reais: 0 quebradas em 28 arquivos.** A correção em massa de âncoras acentuadas (commit 4d63c7b) segurou. Confirmação de que a malha de referências do site é confiável — os problemas de consistência são semânticos, nunca de navegação.

## O template protege; o desvio do template é onde mora o perigo

**Nos sete domínios, os achados graves se concentram exatamente nas fichas que fogem do molde padrão.** Onde o template reina (Intensidade I/II/III com escada de +3, Crítico com fórmula genérica, condição linkada ao glossário), a taxa de erro é quase zero — o arsenal tem ~180 de 186 habilidades limpas. Onde alguém improvisou (Custo fixo, efeito "automático", invocação, efeito atrasado, dreno em Vida), estão a Manopla Mística de 3 Mana, a Zona Cinzenta que atordoa dragão sem rolar, o Vínculo Selvagem permanente e a Aceleração Temporal que se auto-anula. Lição operacional: qualquer ficha futura que diga "Sem Intensidade", "automático" ou "permanente" merece revisão dupla — são as três palavras mais caras do sistema.

## Quem paga rolagem compete com quem não rola — e perde

**A fronteira "rola contra Defesa" vs "efeito automático" é o maior furo estrutural de jogo (não de texto).** A regra só isenta buffs, cura e Supremas inevitáveis, mas ~25 habilidades comuns se declararam automáticas — e como automático ignora a Defesa (o único freio contra alvos Lendários), qualquer jogador otimizador converge pra elas. O padrão só se enxerga cruzando os arquivos: cada ficha automática parece inofensiva sozinha; juntas, formam um sistema paralelo que desativa Defesa e Intensidade ao mesmo tempo.

## Atordoado escapou do degrau III em seis lugares diferentes, por seis mãos diferentes

**A régua "Atordoado = Intensidade III" foi violada de forma independente no arsenal (Espada Senciente, I), em Marciais (Destruição, II), em Debuff (Domador da Natureza e Fenda Dimensional, I), em Elementais (Astrape e Investida Encadeada, automáticas) e num traço racial (Corrente Elétrica da Enguia, II).** Seis violações independentes da mesma régua indicam que a régua nunca foi escrita como checklist de criação — só como exemplo na tabela de Intensidade. O que é exemplo, e não regra nomeada, não segura conteúdo escrito em meses diferentes.

## Precificação foi feita ficha a ficha, nunca prateleira a prateleira

**Todos os pares "mesma entrega, preço diferente" (ELE-06, APO-06, COM-25/26, ARS-14/15…) envolvem habilidades escritas em arquivos ou épocas diferentes — dentro de uma mesma leva, os preços são coerentes.** O sistema tem um vocabulário de preço disciplinado (as escadas) mas nunca teve um passo de revisão comparativa: ninguém perguntou "quem mais entrega isso, e por quanto?". É por isso que os clones divergem e que Pontaria inteira ficou taxada contra Marciais. Qualquer habilidade nova deveria nascer com uma linha "comparável a X (custo Y)".

## O Livro do Mestre cobra dívidas que o lado do jogador nunca emitiu

**"Derrubado", "surpreendido" e "provoca reação" aparecem no Bestiário como se fossem regras conhecidas — o Bandido dá até bônus de dado contra derrubado — mas o lado do jogador nunca as escreveu.** O padrão inverso também existe: traços de Origem cancelam penalidades (água, doença, Medo) que nenhuma regra impõe. Os dois lados do livro assumem um "sistema imaginado" maior que o publicado, e a mesa é onde os dois vãos se encontram. O gabarito de como fazer certo já existe no próprio projeto: a seção de luz/escuridão de exploracao.md, escrita citando nominalmente cada traço que depende dela.

## Regra copiada em dois lugares sempre derivou; regra num lugar só nunca quebrou

**Exaustão, clima, Estresse, equipamento inicial e a tabela de PA existem em duas páginas cada — e as cópias divergem em todos os cinco casos; descanso, DCs e Defesa vivem numa página só e estão íntegros nos três arquivos que os citam.** A cópia mais nova sempre ganhou nuance que a antiga não recebeu retroativamente. Regra de escrita pro projeto: regra mora num lugar; todo outro lugar linka.

## A remoção dos Tiers (2026-07-26) não foi acompanhada de um grep

**Três habilidades ainda rodavam no sistema removido** (Dança Élfica era literalmente irresolvível; Choque das Sombras e Armadilha Oculta pediam um "tier obtido" que não existe). Toda remoção de mecânica precisa de uma varredura por vocabulário órfão — "tier" sobreviveu 1 dia no texto e teria travado a primeira mesa que tocasse nessas fichas.

## Dez entradas de glossário valeram mais que cem correções de ficha

**Ao aplicar as correções, a proporção ficou clara: escrever Derrubado, Vantagem, rodada, cena, empurrar, agarrado, Desprevenido, acúmulo de bônus, zonas e voo resolveu mais problemas de mesa do que as ~180 edições de habilidade somadas.** Cada ficha corrigida conserta uma habilidade; cada termo definido conserta todas as fichas que o usam — e no Prisma, "derrubado" sozinho aparecia em mais de 150 pontos. A lição para o futuro: quando um achado se repete em muitos arquivos, o conserto quase nunca é nos arquivos.

## O erro se repete onde a régua é exemplo, e não regra nomeada

**"Atordoado = Intensidade III" foi violado seis vezes independentes, em seis arquivos, por seis mãos — porque estava só como exemplo na tabela de Intensidade, nunca como regra com nome.** Já "alcance e área nunca escalam", que tem bloco de regra próprio e destacado, foi respeitado em ~760 fichas com uma única exceção (o dragão do Bestiário). Mesma disciplina de autor, resultados opostos: o que virou regra nomeada segurou; o que ficou como exemplo derreteu. Vale promover a regra do Atordoado (e do degrau de cada condição) a texto próprio antes de escrever conteúdo novo.

## Automático e permanente são as duas palavras mais caras do sistema

**Toda habilidade que dizia "efeito automático, sem teste" ou "companheiro permanente" estava, sem exceção, dominando as vizinhas.** Não por serem fortes no papel — por saírem do sistema de custo: automático ignora a Defesa (que é o único freio contra alvos Lendários) e permanente ignora o Mana (que é o freio de tudo). Ao converter as ~15 automáticas em roladas e dar prazo ao Vínculo Selvagem, nenhuma ficha precisou perder poder — só voltar para dentro das regras. Regra prática: uma habilidade que escapa de um dos dois recursos precisa de justificativa explícita (Suprema, zona de chão), nunca de silêncio.

## O que o sistema tem de mais sólido (pra não mexer sem precisar)

**Verificado mecanicamente ou número a número: zero violações de PA=Intensidade e das escadas de Mana em ~760 fichas; zero âncoras quebradas; zero referências de nome quebradas nos 100 pacotes (~1.100 checagens); dados de dano 100% consistentes entre arsenal e glossário; matemática de Defesa do Bestiário fechando nas 8 fichas; descanso idêntico nos 3 arquivos; área/alcance jamais escalando com Intensidade; Ressuscitar como único Tiers de Resultado; 22 Supremas todas a 16+.** A fundação aguenta — os problemas são de vocabulário não formalizado, fronteiras entre páginas e comparação entre prateleiras, não de estrutura.
