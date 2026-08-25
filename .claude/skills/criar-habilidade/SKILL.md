---
name: criar-habilidade
description: Cria ou ajusta habilidades de jogo do Prisma RPG (o RPG de mesa homebrew deste repositório), mantendo o padrão mecânico e de formatação já estabelecido no projeto. Use esta skill sempre que o usuário pedir pra criar, desenhar, balancear ou revisar uma habilidade, feitiço, magia, golpe de arma, ou "poder" de personagem — inclusive quando o pedido vier como "cria uma habilidade parecida com X do anime/filme/jogo Y", ou como uma ideia solta tipo "queria algo tipo controle mental" ou "e se tivesse voo?". Também use ao criar uma arma nova (que precisa de 3 graus de habilidade) ou um elemento/subgrupo novo dentro de Mágicas por Elemento.
---

# Criar Habilidade — Prisma RPG

Esta skill existe porque o padrão de habilidades do Prisma RPG foi fixado com bastante detalhe numa sessão de design, e é fácil perder essa consistência em sessões futuras (esquecer um campo, comprimir as Intensidades numa linha só, inventar uma habilidade sem consultar o usuário). Ela é uma referência de consulta rápida — leia as fontes vivas linkadas abaixo quando precisar do valor exato de algo, não confie de cor em números que possam ter mudado.

**Fontes vivas** (sempre a verdade mais atual — releia se um número aqui parecer estranho):
- [docs/habilidades/regras.md](../../docs/habilidades/regras.md) — Ficha de Habilidade, Intensidade, Custo fixo, Resolução, Componentes, Concentração, Cooldown, Ritual, lista de grupos
- [docs/jogador/arsenal.md](../../docs/jogador/arsenal.md) — armas existentes e suas 3 habilidades
- [docs/jogador/mana.md](../../docs/jogador/mana.md) — Escala de Mana por Intensidade
- [docs/habilidades/magicas-elementais.md](../../docs/habilidades/magicas-elementais.md) — Assinatura de Elemento (o que cada elemento faz de único)
- [docs/glossario.md](../../docs/glossario.md) — todo termo que pode virar link de Chave, **e a lista fechada de Condições**
- [docs/habilidades/marciais.md](../../docs/habilidades/marciais.md) — tabela de Dano Desarmado (pra habilidades de soco/chute sem arma, escala por nível)
- [CLAUDE.md](../../CLAUDE.md) — regras gerais do projeto (nunca inventar sem consultar, sempre AskUserQuestion pra escolhas)

## O processo, não pule etapas

O CLAUDE.md do projeto proíbe escrever conteúdo de jogo em `docs/` sem aprovação explícita. Isso vale em dobro pra habilidades novas:

1. **Proponha no chat primeiro** — nome, descrição evocativa, Chave, atributo, e as três Intensidades com valores já preenchidos (nunca "TBD"). O usuário precisa conseguir avaliar a habilidade pronta, não uma ideia vaga.
2. **Pergunte o que não é óbvio.** Se o atributo, o grupo, um valor numérico ou uma escolha de design não tiver uma resposta clara a partir do que já existe no projeto, use `AskUserQuestion` em vez de decidir sozinho. É melhor perguntar demais do que inventar uma regra que o usuário depois tem que desfazer.
3. **Só grave depois do "pode gravar" / aprovação explícita.** Mostre o preview, espere confirmação, então edite o arquivo.

Se a habilidade for inspirada numa obra (anime, filme, jogo — Grand Chase é a referência usada até agora), pode pesquisar a fonte pra entender o conceito. O usuário prefere usar o **nome original da habilidade/personagem-fonte** quando existir um bom (ficou "bem mais legal" segundo ele, e foi o que aconteceu com Lire/Arme/Lass — só a Elesis ficou pra trás com nomes genéricos no início da sessão, e depois precisou ser corrigida). A **mecânica e os números**, esses sim precisam ser originais — desenhados a partir do conceito, não copiados de uma versão em vídeo game com números totalmente diferentes de contexto. No chat, parafraseie o conceito da fonte em 1-2 frases — nunca reproduza texto longo dela.

**As 3 habilidades de arma são temáticas da ARMA, não necessariamente do personagem-fonte.** Ficou claro no caso da Amy: o moveset dela na fonte é todo chutes/socos (desarmado), nada a ver com o Chakram que ela empunha. Se o moveset do personagem não combina com a arma dele, é válido (e melhor) buscar outra referência SÓ pra desenhar as 3 habilidades de arma — pode ser outra mídia (ex: o Chakram acabou inspirado na Xena, não em Grand Chase) — e usar o kit inteiro do personagem-fonte como habilidades gerais de grupo. Pergunte ao usuário quando não estiver óbvio se o kit combina com a arma ou não.

## A Ficha de Habilidade

Toda habilidade — sem exceção — tem estes campos, cada um em seu próprio bullet:

- **Nome**
- *Descrição breve*, em itálico, logo abaixo do nome: 1 frase evocativa que deixa claro o que a habilidade faz. Evite números específicos que o jogador possa confundir com regra (ex: não diga "cinco flechas" se mecanicamente é só 1 rolagem de dano — isso já aconteceu e gerou confusão).
- **Chave** — ver seção própria abaixo
- **Atributo**
- **Alvos**, **Alcance** e **Área**, sempre explícitos — nunca vago tipo "uma área", sempre um número de casas; "corpo a corpo" ou "—" quando não se aplica (Alcance e Área nunca escalam com Intensidade)
- **Vs** — contra qual número-alvo a Resolução compara (Evasão por padrão pra ataque físico; Fortitude Mágica/Física, Social ou Exploração pra efeito que a pula — declare mesmo quando for o padrão)
- **Resolução** — **Ataque** (o usuário rola, é a maioria) ou **Teste de Resistência** (o alvo rola — use pra efeito que o corpo resiste por dentro: veneno, maldição plantada, algo que dispara depois) — ver [Resolução](../../docs/habilidades/regras.md#resolucao) e [Teste de Resistência](../../docs/habilidades/regras.md#teste-de-resistencia)
- **Duração** — Instantânea, X rodadas, até 0 de Vida, até descanso, etc.
- **Componentes** — Verbal/Somático/Material. Tem padrão por Grupo (Marciais/Pontaria = Somático+Material; magias em geral = Verbal+Somático; Projeção Mental = só Somático, por definição própria do grupo; Sociais = só Verbal; Infiltração/Mobilidade/Percepção Arcana = só Somático) — só declare diferente do padrão se a habilidade tiver um motivo pra isso. Em **Buff/Debuff/Suporte** quem decide é o Atributo: Magia = Verbal+Somático, Ataque/Agilidade = só Somático, mais Material se a ficha exigir um item. **Passiva não tem componente** — não se ativa. Ver [Componentes](../../docs/habilidades/regras.md#componentes)
- **Concentração** — Sim, só se for Buff/Debuff/invocação de Conjuração com **duração contínua**; toda outra habilidade é Não. Ver [Concentração](../../docs/habilidades/regras.md#concentracao)
- **Cooldown** — segue a Escala da habilidade (Básica/Menor sem cooldown; Avançada/Moderado 1–2 rodadas; Especial/Maior 3–4 rodadas; Supremo 1x por cena, ou 1x por descanso se for excepcionalmente forte). Só declare valor explícito quando fugir do padrão baixo da faixa. Ver [Cooldown](../../docs/habilidades/regras.md#cooldown)
- **Ritual** — Sim só quando a habilidade for algo que se faz com calma fora de combate (utilidade, invocar, transmutar) — nunca em dano de combate. A maioria é Não. Ver [Ritual](../../docs/habilidades/regras.md#ritual)
- **Intensidade I / II / III**, um bullet cada, com o PA, o Mana e o valor numérico completo já resolvido (nunca "dano da arma" genérico, nunca duas Intensidades comprimidas na mesma linha com `|`)
- **Crítico**

Todo campo aparece sempre, mesmo quando a resposta é "—" ou "Não" — o jogo é deliberadamente explícito, nada fica subentendido.

Quando o efeito é longo (mais de ~150 caracteres — acontece em buffs de grupo e invocações), repetir o texto inteiro três vezes fica ilegível: nesses casos a Intensidade II/III pode dizer **"o mesmo, com 2d6 de dano"**, apontando só o que mudou. O que nunca se abrevia é o **número** — "o mesmo, mas mais forte" não serve.

Mecânicas que valem em **qualquer** Intensidade (um deslocamento de investida, um requisito de arma, uma linha de Risco) ganham **bullet próprio** acima das Intensidades — não repita dentro de cada uma. Isso já causou perda de conteúdo: seis investidas de Fogo tinham "o usuário se desloca até o alvo" só na Intensidade I e o texto sumia quando o jogador subia a Intensidade.

### Intensidade

O teste é **d20 + Atributo vs Defesa** e responde só **acertou ou não**. Quão forte o golpe é não vem da rolagem — vem da **Intensidade que o jogador escolheu pagar** ao ativar:

| Intensidade | PA | O que entrega |
|---|---|---|
| I | ◈ (1) | O efeito base — **nunca só o dano** (ver abaixo) |
| II | ◈◈ (2) | O efeito secundário aparece ou cresce |
| III | ◈◈◈ (3) | O efeito completo — consome o turno inteiro |
| Crítico | 20 natural | Dano máximo + rolagem extra, e **sobe 1 Intensidade de graça** |

**Alcance e área nunca escalam com Intensidade** — só o efeito. Uma habilidade de 2 casas de raio cobre 2 casas de raio na Intensidade I.

**A Intensidade I precisa valer mais que o Ataque Básico.** Essa é a regra mais importante desta seção, e a orientação anterior desta skill ("pra Tier 1, dano puro costuma bastar") produziu **163 habilidades defeituosas** que o usuário teve que apontar numa captura de tela. O Ataque Básico custa ◈ e **0 Mana**, e já causa o dado da arma: se a Intensidade I entrega só o dado da arma, o jogador pagou Mana **e** uma escolha de nível de progressão para ter o que qualquer um tem de graça. Toda Intensidade I precisa de dano maior, um efeito, ou área.

**Hierarquia de grau de arma.** A Básica parte de 1x o dado + um efeito; a Avançada e a Especial partem de **2x** o dado e alcançam condições que a Básica não impõe; a Especial costuma somar área. Em qualquer Intensidade, o grau superior tem que ser visivelmente melhor — senão a Avançada custa mais Mana pra entregar o mesmo, o que já aconteceu e o usuário reclamou.

**Habilidades de Custo fixo não têm Intensidade.** Use `- **Custo fixo:** ◈◈◈ (3 PA) + N Mana` e um único bullet **Acerto** quando: a área é de raio 3+ (a área já é o poder), a habilidade é Suprema (16+ Mana), ou o efeito é **absoluto** e não tem degrau acima (uma Reação que anula um ataque por completo — não existe "anular mais"). Nesse caso o custo cobra o valor da Intensidade III, porque é o efeito que ela entrega.

**Buff e cura também têm Intensidade** — não ter teste de ataque não isenta de escala. O que cresce é o efeito, e o eixo é escolhido caso a caso: **magnitude** quando há um valor que é a identidade (Escudo de 1d8 → 2d8 → 3d8), **duração** quando o efeito é absoluto e não tem número (não pode ser derrubado por 2 → 3 → 4 rodadas), ou **ambos** em buff de grupo e transformação. Diferente dos ataques, aqui a Intensidade I **mantém o efeito e o custo em Mana que a habilidade já tinha** — o jogador nunca paga um pedágio pra ter o de antes.

**Reações dedicadas custam 0 PA em qualquer Intensidade** — a rede de segurança precisa funcionar mesmo com o PA todo gasto. Nelas a Intensidade escolhe só quanto Mana queimar: `- **Intensidade I — 0 PA + 3 Mana:**`, depois 6, depois 9.

**Tiers de Resultado — exceção rara.** Quando o efeito não faz sentido em meio-sucesso (reviver um aliado é o único caso hoje), o d20 volta a graduar o **resultado**: `≤10` falha catastrófica, `11–16` falha recuperável, `≥17` sucesso, 20 natural sucesso ampliado. Custo fixo, sem Intensidade. O usuário aprovou isso justamente para que ressurreição não vire efeito confiável — não estenda o padrão sem perguntar.

**Todo efeito automático periódico ("por N rodadas", "no início de cada rodada") precisa deixar explícito se a primeira aplicação é imediata.** Já corrigimos essa ambiguidade 3 vezes (Raios e Relâmpagos, Chamas Espirituais, e depois Brilho Caótico/Esfera das Trevas/Espada Vingadora do Dio) — é fácil escrever "no início de cada rodada" sem dizer se isso inclui o momento do lançamento. Escreva sempre no formato: "X de dano automático imediatamente ao usar/invocar, e mais uma vez no início de cada uma das N rodadas seguintes (N+1 aplicações no total)". Confira isso *toda vez* que escrever uma habilidade com efeito de zona/DoT — não só quando o usuário reclamar.

### Assinatura: a habilidade escala o que ela É

A Intensidade **amplifica** o efeito característico da habilidade, em vez de trocá-lo por outro. Escolha uma assinatura (o verbo daquela habilidade) e construa a escada em cima dela:

```
Corte Impactante (assinatura: desequilibrar)
I   1d4 + empurra 1 casa
II  1d4 + empurra 2 casas e derruba
III 2d4 + empurra 3 casas, derruba, e ele perde a próxima Reação
```

**Não caia sempre em "empurra 1 casa" / "derruba".** Isso já virou padrão repetitivo duas vezes no projeto e o usuário reclamou nas duas. Menu de assinaturas possíveis:

- **Condição negativa:** [Sangrando], [Queimando], [Lento], [Imóvel], [Atordoado], [Envenenado], perde a próxima Ação Básica/Reação
- **Controle de campo:** empurra/puxa, área que persiste ferindo quem fica nela (assinatura de Sombras), Terreno Difícil
- **Suporte a aliados:** [Marcado] (próximo ataque aliado tem Vantagem), concede [Escudo] ao usuário
- **Recurso do alvo:** drena Mana (Rey/Latido Drenante) — bom pra tema de "sugar" poder
- **Rolagem prejudicada:** Desvantagem (Rin/Passo Sombrio) — rola 2x e fica com o **pior**
- **Controle de comportamento:** Provocação (Lime) — força o alvo a só atacar o usuário
- **Dreno:** usuário recupera Vida em fração do dano (assinatura de Sangue e de Sombras em alvo único)
- **Risco:** se algum dado de dano cair em 1, a habilidade cobra um preço de quem a usou — só pra tema perigoso (lâmina amaldiçoada, magia de sangue). Ver [Risco](../../docs/glossario.md#risco)

1-2 bem escolhidos, coerentes com o conceito (um golpe cortante sangra, um de impacto derruba), valem mais que variedade por variedade.

### Condições: vocabulário fechado

**Não invente nome de condição.** O projeto já pagou por isso: "Paralisado" (9 usos), "prostrado" e "preso no lugar" foram criados solto e depois tiveram que ser normalizados. As canônicas vivem em [Condições](../../docs/glossario.md#condições) — sempre linke (`[Sangrando](../glossario.md#sangrando)`) em vez de repetir a definição no corpo do texto:

| Condição | O que faz |
|---|---|
| **Sangrando** | 1d4 de Vida no início do próximo turno — uma vez só |
| **Queimando** | 1d4 por turno, **não para sozinho** até apagarem (assinatura de Fogo) |
| **Lento** | Movimento pela metade |
| **Imóvel** | Movimento 0, mas continua agindo |
| **Atordoado** | Não pode agir — nem ação, nem movimento, nem reação |
| **Marcado** | Próximo ataque de aliado contra ele rola com Vantagem |
| **Envenenado** | 1d4 por turno até ser curado; acumula |
| **Escudo** | Pontos temporários que absorvem dano antes da Vida |

Há também **efeitos de terreno**, que grudam no chão em vez de numa criatura: [Zona Amaldiçoada](../../docs/glossario.md#zona-amaldiçoada) (assinatura de Sombras em área) fere quem entrar ou terminar o turno nela, **inclusive aliados**, é visível, e zonas sobrepostas não somam.

Se precisar de uma condição que não existe, isso é decisão de design: **pergunte antes**, e se aprovada, adicione a entrada em `docs/glossario.md` no mesmo lote de edição.

**Efeito periódico exige dizer se a primeira aplicação é imediata** — a regra acima na seção de Ficha vale em dobro aqui, e é fácil escorregar: Queimando causa dano na hora, Envenenado só no início do próximo turno do alvo, e a Zona Amaldiçoada não repete o dano do impacto. Se criar uma mecânica periódica nova, decida isso explicitamente.

### Elemento tem assinatura própria

Se a habilidade é de Mágicas por Elemento, ela **precisa** carregar a assinatura do elemento — é o que faz Fogo e Sombras jogarem diferente mesmo com o mesmo dano. Consulte [Assinatura de Elemento](../../docs/habilidades/magicas-elementais.md#assinatura-de-elemento) antes de escrever; em resumo: Fogo consome, Gelo trava, Raio rouba a ação, Terra põe no chão, Água arrasta, Vento arremessa, Luz prende, Sombras nega terreno e drena, Veneno acumula, Sangue troca Vida por poder, Espaço-Tempo reposiciona.

## Chave — e por que ela precisa ser um link

Toda habilidade deve linkar seus termos pro [Glossário](../../docs/glossario.md), pra funcionar como navegação cruzada quando o site for publicado.

- **Habilidade de arma:** `[Arma](../glossario.md#arma) - [Grau](../glossario.md#grau)` — ex: `[Espada](../glossario.md#espada) - [Básica](../glossario.md#básica)`
- **Habilidade geral de grupo, sem subtipo:** `[Grupo](../glossario.md#grupo)` — ex: `[Buff](../glossario.md#buff)`
- **Habilidade geral de grupo, com subtipo** (hoje só Mágicas por Elemento tem subtipos): `[Grupo](../glossario.md#grupo) - [Subtipo](../glossario.md#subtipo)` — ex: `[Mágicas por Elemento](../glossario.md#mágicas-por-elemento) - [Terra](../glossario.md#terra)`

O caminho relativo depende de onde o arquivo da habilidade mora: tanto `docs/jogador/` quanto `docs/habilidades/` ficam um nível abaixo de `docs/`, então ambos usam `../glossario.md`.

**Propriedades de arma** (Finesse = Força ou Agilidade; Híbrida = Força ou Inteligência) entram como um 3º segmento na Chave, mas **só nas habilidades da própria arma que tem a propriedade** — ex: `[Adagas](../glossario.md#adagas) - [Básica](../glossario.md#básica) - [Finesse](../glossario.md#finesse)`, `[Gládio](../glossario.md#gládio) - [Básica](../glossario.md#básica) - [Híbrida](../glossario.md#híbrida)`. Habilidades gerais de grupo que apenas *mencionam* a propriedade condicionalmente no texto (ex: "Força, ou Agilidade se a arma equipada for Finesse") não ganham esse segmento — a Chave descreve o que a habilidade **é**, não toda regra que ela pode tocar de leve. Se o personagem-fonte tiver uma identidade "híbrida" (guerreiro-mago, ladino-atirador etc.), considere se uma propriedade nova desse tipo faz sentido pra arma dele, em vez de travar num único atributo.

**Se a habilidade introduzir um termo que ainda não existe no Glossário** (uma arma nova, um grupo novo, um elemento novo), adicione uma entrada `###` correspondente em `docs/glossario.md` no mesmo lote de edição — senão o link fica quebrado.

## Atributo de Mágicas por Elemento: Inteligência por padrão, Sabedoria pra personagens Divino

Toda habilidade de Mágicas por Elemento até a Rin usou Inteligência, sem exceção, mesmo quando o personagem-fonte não era um "mago" clássico (ex: ventos da Rin). Isso mudou com a Lime — como ela é explicitamente uma paladina (Holy Knight/Saint, poder "divino" e não "arcano"), suas habilidades de Luz usam **Sabedoria**, aproveitando a distinção que já existe na tabela de Tipos de Ataque (Arcano→Inteligência, Divino→Sabedoria) mas que antes só aparecia em Suporte.

**Critério pra decidir:** se o personagem-fonte é claramente um conjurador arcano (bruxa, feiticeira, invocador) → Inteligência, como sempre. Se é claramente um conjurador divino (paladino, clérigo, algo com tema de deusa/bênção/oração) → Sabedoria. Na dúvida, pergunte ao usuário — foi o que gerou essa própria distinção.

## Atributo de Vontade: comando, voz, coerção — nunca resiliência própria

Vontade é o atributo de habilidades cuja fonte é a **voz, o som ou a coerção do usuário projetada sobre outra mente** — grito, canto, ordem falada, encantamento que convoca ou vincula. **Não é** sobre a resiliência de quem usa a habilidade: um efeito em que o próprio usuário resiste a ser derrubado, interrompido ou atordoado continua sendo Força/físico, mesmo que a descrição use palavras como "inabalável" ou "impenetrável". Isso ficou definido em 2026-08-16 quando o usuário rejeitou Postura Inabalável, Repouso Silencioso e Reforço Momentâneo (Buff) como candidatos a Vontade — a mecânica delas é o corpo do próprio usuário aguentando algo, não a vontade dele saindo e atingindo outra pessoa.

**Critério pra decidir:** o efeito precisa **sair** do usuário e **atingir** outra mente — grito, canto, ordem, encantamento que compele ou convoca. Exemplos já aprovados: **Provocação** e **Grito Dissonante** (grito/presença que subjuga), **Exorcismo**, **Selo de Exílio** e **Fechar a Porta** (ordem falada de comando/expulsão — repare como as três compartilham quase a mesma frase de sabor, "a ordem não é gritada, é dita uma vez"), **Servo de Cinzas**, **Chamar Lâmina Espectral** e **Convocar Guardião do Pacto** (um espírito que "responde ao chamado", ecoando **Selar o Pacto**), **Lamento dos Mortos** (coro que instala pavor), **Hora da Dança** (melodia) e **Zona de Paz** (decreto/coerção sobre uma área).

**Projeção Mental fica de fora por definição própria** — o grupo inteiro é telepatia/leitura de mente que "funciona em qualquer mente, sem depender de palavras" (ver `docs/habilidades/projecao-mental.md`), então mesmo quando o efeito mexe com a mente do alvo, o poder ali é intelecto silencioso (Inteligência), não voz. Não converta habilidades desse grupo pra Vontade só porque afetam a mente de alguém.

**Em armas:** se o Requisito de uma arma exige Vontade (ex: Violino, Vontade +4) ou Sabedoria (ex: Vajras, Sabedoria +6), as 3 habilidades dela devem usar esse mesmo atributo pra atacar — não faz sentido exigir um mínimo pra equipar uma arma cujo golpe não usa esse atributo pra rolar. Esse bug concreto apareceu em Vajras e Violino (ambas tinham Requisito num atributo e as 3 habilidades em Força) e foi corrigido em 2026-08-16; confira isso ao criar ou revisar qualquer arma com Requisito.

## Custos: PA vem da Intensidade, Mana escala com ela

**O PA não é mais escolha de design** — ele é a Intensidade (I=◈, II=◈◈, III=◈◈◈). O que você define é a **escala de Mana**. Ver [docs/jogador/mana.md](../../docs/jogador/mana.md).

**Habilidades de arma** usam escala fixa pelo grau, para o investimento na arma ficar visível:

| Grau | Intensidade I | II | III |
|---|---|---|---|
| Básica | 1 Mana | 3 | 6 |
| Avançada | 2 Mana | 5 | 9 |
| Especial | 3 Mana | 7 | 12 |

**Habilidades gerais de grupo** usam **1 / 3 / 6**. Se a habilidade é mais forte que a média do grupo, parta do custo dela e suba **+3 Mana por Intensidade** (2/5/8, 3/6/9, 4/7/10). O teto da habilidade — o custo da Intensidade III — classifica o Grau de Poder dela:

| Grau de Poder | Mana na Intensidade III | Uso esperado |
|---|---|---|
| Menor | 1–3 | Várias vezes por combate |
| Moderado | 4–8 | 2–4 vezes por descanso |
| Maior | 9–15 | 1–2 vezes por descanso |
| Supremo | 16+ | 1 vez por descanso, com Custo fixo e possivelmente restrição extra |

**Escadas rasas são defeito.** Se subir da Intensidade I à III custa 2 Mana no total, ninguém usa a I. Já corrigimos 17 habilidades assim (Ressuscitar chegou a ficar 16/17/18) — mantenha os degraus de 3 em 3.

**Custo pode ser em Vida em vez de Mana** (Rin/Aumento Sombrio, e o elemento Sangue) — escolha válida pra risco/recompensa temático. Nesse caso a **Vida** é que escala com a Intensidade: `◈ (1 PA) + 1d4 de Vida`, `◈◈ + 2d4`, `◈◈◈ + 3d4`. Nunca deixe implícito que "sem custo em Mana" significa "de graça".

## Habilidades usadas como Reação

O sistema é deliberadamente livre aqui: **qualquer Habilidade pode ser usada como Reação**, fora do turno do personagem, contanto que ele ainda tenha PA sobrando no pool (do turno anterior) pra pagar o custo normal dela — não existe uma lista fechada de "isso pode ser reação, isso não pode".

A exceção são **habilidades dedicadas a Reação** — o texto diz explicitamente "usada como Reação" (ex: Defesa Mágica, Cambalhota) — essas custam **0 PA, só Mana**, e ficam sempre disponíveis mesmo se o personagem já gastou todo o PA no próprio turno. Isso evita que gastar PA atacando deixe o personagem sem nenhuma defesa reativa.

Ao criar uma habilidade dedicada a Reação: escreva `**Nome** *(usada como Reação)*` no título, e use `- **Custo fixo:** X Mana | 0 PA (habilidade dedicada a Reação)` — sem Intensidade, já que não há PA para graduar.

## Escopo por personagem: todas as classes, a partir do Dio

Os primeiros 10 personagens (Elesis→Mari) só tiveram a arma/kit da **1ª classe** coberto, por decisão consciente de ritmo — isso não é retroativo, não precisa completá-los. **A partir do Dio, o padrão virou cobrir as 4 classes completas de cada personagem** (todas as habilidades nomeadas de cada árvore de talentos/kit, não só uma seleção). Isso gera bem mais habilidades por personagem (o Dio sozinho gerou 23), o que é intencional — o usuário quer volume.

Na prática:
- Pesquise a página de cada uma das 4 classes do personagem (e a árvore de talentos de cada uma, se existir — geralmente em `Árvore de Talentos do <Classe>`), não só a 1ª.
- Se as classes compartilham a mesma arma (caso do Dio, que usa "Deathstar" nas 4 classes), ela vira **uma única entrada no Arsenal**, com 3 habilidades mundanas originais — não recrie a arma pra cada classe.
- Se uma habilidade suprema/especial se repete idêntica entre classes (também o caso do Dio com "Império Sombrio"), trate como **uma única habilidade geral**, não duplique.
- Nomes de talento redundantes entre si (várias variações de "golpe + lança pro ar", por exemplo) podem virar habilidades gerais distintas mesmo assim — diferencie pela assinatura de cada uma (ver o menu de assinaturas acima), não precisa inventar uma mecânica nova pra cada uma.
- Pode pular nós de talento puramente passivos/incrementais (bônus de dano genérico, redução de intervalo, etc.) — foque nas habilidades **ativas e nomeadas**.

**Nem todo personagem AP compartilha UMA arma entre as classes.** Dio/Zero/Ley reusam a mesma arma nas 4 classes (vira 1 entrada no Arsenal). O Rufus (Lupus) é diferente: ele mantém a arma da 1ª classe (Eyeteeth/Presas) e cada classe seguinte **acrescenta** uma arma de suporte nova (faca → espingarda → metralhadora) — 4 armas fisicamente distintas, não reskins. Pra esse padrão, pergunte ao usuário se prefere (a) dobrar as armas extras em habilidades gerais de Marciais/Pontaria como se fosse o padrão Dio/Zero, ou (b) dar Arsenal próprio pra cada arma (3 habilidades cada). O Rufus usou a opção (b) — 4 entradas no Arsenal, uma combo/ultimate que usa todas as armas juntas vira Supremo geral (não cabe em nenhum slot de arma sozinho).

## Golpes desarmados não travam em arma nenhuma

Se o moveset do personagem-fonte é literalmente socos e chutes (sem depender de segurar nada — caso da Amy e do Jin), essas habilidades vão pra **Habilidades Gerais de Marciais** usando o [Dano Desarmado](../../docs/habilidades/marciais.md#dano-desarmado) (escala por nível, não por arma), não pra uma arma. É a mesma lógica de "arma mágica não trava feitiço": ninguém deveria precisar equipar um objeto específico só pra usar um soco.

Isso **não impede** de também criar uma arma tematicamente relacionada (ex: Manopla) — só que as habilidades dela precisam ter identidade própria, desenhada do zero (ver seção acima sobre arma ≠ personagem-fonte), e não podem ser os mesmos golpes desarmados só travados atrás de um item.

## Armas mágicas são genéricas — não travam feitiços

Isso é uma decisão de design deliberada, ligada ao fato de o Prisma RPG não ter classes: as 3 habilidades de uma arma mágica (Cetro é o único exemplo até agora) são canalizações **neutras**, sem elemento ou tema fixo (ex: "Investida Arcana", um pulso de dano sem forma definida). Se uma arma mágica travasse "Petrificar" ou "Cura" como sua Habilidade Básica, isso empurraria o jogo de volta pra uma lógica de classe ("mago do cetro só petrifica"), o que contradiz a premissa central do sistema.

Os feitiços temáticos (fogo, cura, controle mental, o que for) **não** vivem no Arsenal — vivem soltos nos grupos de Habilidades (Mágicas por Elemento, Buff, Debuff, Suporte etc.), disponíveis pra qualquer personagem, com qualquer arma, sem lock algum. Se o usuário pedir uma habilidade nova claramente mágica/temática, ela quase certamente é uma "Habilidade Geral" de grupo, não uma habilidade de arma.

**Essa regra vale pra QUALQUER arma, não só armas mágicas.** Descobrimos isso tarde (Espada Flamejante e Onda de Chamas da Lâmina nasceram com efeito elemental — fogo, energia sombria — travado numa arma puramente física, e tivemos que corrigir depois). Habilidades de arma devem ser sempre **mundanas**: técnica, força, momento, peso — coisa que qualquer wielder daquela arma consegue fazer treinando, sem precisar de nenhuma afinidade mágica. Se a ideia pra uma habilidade de arma envolve fogo, gelo, energia sombria, cura, ou qualquer efeito claramente elemental/arcano/divino, ela é uma habilidade geral de Mágicas por Elemento (ou Buff/Debuff/Suporte), e a arma ganha uma substituta mundana no lugar. Habilidades gerais "Especial" de grupo com flavor grandioso (espadas fantasmas, pilares de energia) ainda podem ficar em Marciais/Pontaria contanto que usem `dado de dano da arma equipada` e Atributo físico (Força/Agilidade) — a linha é: precisa de Inteligência/Sabedoria pra fazer sentido? Então é magia, vai pra Mágicas por Elemento.

## Onde a habilidade mora

- Habilidade de arma → `docs/jogador/arsenal.md`, na seção `## NomeDaArma`
- Habilidade geral de grupo → `docs/habilidades/<grupo>.md`, numa seção `## Habilidades Gerais` (crie a seção se ainda não existir)
- Feitiço elemental → `docs/habilidades/magicas-elementais.md`, numa sub-seção `## NomeDoElemento` (crie se o elemento ainda não tiver seção — e adicione o elemento na lista do topo do arquivo e no Glossário)
- Se o pedido não se encaixa em nenhum grupo existente, isso é uma decisão de design (criar grupo novo) — pergunte ao usuário antes de inventar um, mesma lógica do resto do processo. "Suporte" foi criado assim durante a sessão que gerou esta skill.

## Checklist antes de gravar

- [ ] Descrição breve é 1 frase evocativa, sem número que confunda mecânica com narrativa
- [ ] Chave é um link válido pros 1-2 termos corretos no Glossário (e o Glossário tem essas entradas)
- [ ] **A Intensidade I entrega mais que o Ataque Básico** (dano maior, efeito, ou área — nunca só o dado da arma)
- [ ] As três Intensidades são diferentes entre si, e a escada de Mana sobe de 3 em 3
- [ ] Se é habilidade de arma: o grau superior é visivelmente melhor que o inferior em toda Intensidade
- [ ] Se é de elemento: carrega a assinatura daquele elemento
- [ ] Só condições canônicas, sempre linkadas ao Glossário — nenhum nome inventado
- [ ] Alcance/raio em casas, se não for corpo a corpo (e nunca escala com Intensidade)
- [ ] Vs, Resolução, Duração, Componentes, Concentração, Cooldown e Ritual estão todos declarados — nenhum ficou implícito
- [ ] Cada Intensidade é seu próprio bullet, com valor numérico completo (ou é Custo fixo, com o motivo claro: área raio 3+, Suprema, ou efeito absoluto sem degrau acima)
- [ ] Se é buff/cura/mobilidade: escala pelo eixo que faz sentido (magnitude, duração ou ambos), e a Intensidade I preserva o efeito e o Mana que a habilidade já tinha
- [ ] Se é Reação dedicada: 0 PA em todas as Intensidades, escalando só o Mana
- [ ] Mecânica que vale em toda Intensidade está em bullet próprio, não repetida dentro de cada uma
- [ ] Crítico definido
- [ ] Usuário aprovou explicitamente antes da escrita no arquivo

## Exemplo completo (referência de formatação)

Habilidade de arma com as 3 Intensidades, de `docs/jogador/arsenal.md` (Básica das Adagas — note que a Intensidade I já empurra, não é dano puro):

```markdown
**Corte Impactante** — *Básica*

*Um corte horizontal rápido, cravado no ponto certo pra desequilibrar o inimigo.*

- **Chave:** [Adagas](../glossario.md#adagas) - [Básica](../glossario.md#básica) - [Finesse](../glossario.md#finesse)
- **Atributo:** Força ou Agilidade | **Alvos:** 1 criatura
- **Intensidade I — ◈ (1 PA) + 1 Mana:** 1d4 de dano + empurra 1 casa
- **Intensidade II — ◈◈ (2 PA) + 3 Mana:** 1d4 de dano + empurra 2 casas e derruba o alvo
- **Intensidade III — ◈◈◈ (3 PA) + 6 Mana:** 2d4 de dano + empurra 3 casas, derruba o alvo, e ele perde a próxima Reação
- **Crítico (20 natural):** dano máximo (4) + 1d4 extra, e sobe 1 Intensidade
```

Custo fixo por área grande, de `docs/jogador/arsenal.md` (Especial das Adagas — raio 3, então cobra o Mana da Intensidade III):

```markdown
**Golpe Final** — *Especial*

*Recua num salto enquanto crava lâminas certeiras no chão, longe do alcance de contra-ataques.*

- **Chave:** [Adagas](../glossario.md#adagas) - [Especial](../glossario.md#especial) - [Finesse](../glossario.md#finesse)
- **Custo fixo:** ◈◈◈ (3 PA) + 12 Mana | **Atributo:** Força ou Agilidade | **Alvos:** todas as criaturas em 3 casas de raio ao redor da posição original do usuário
- **Alcance do recuo:** até o valor de Movimento do personagem, em casas — o usuário se desloca pra trás, saindo da área afetada
- **Acerto:** 2d4 de dano em cada alvo + cada alvo fica [Lento](../glossario.md#lento) e é derrubado
- **Crítico (20 natural):** dano máximo (8) + 2d4 extra em todos, [Lento](../glossario.md#lento), e derruba cada alvo
```

Buff escalando por **magnitude**, de `docs/habilidades/buff.md` (sem teste de ataque, mas com Intensidade):

```markdown
**Escudo Mágico**

*Uma barreira translúcida se ergue, absorvendo o impacto antes que ele chegue.*

- **Chave:** [Buff](../glossario.md#buff)
- **Atributo:** Inteligência | **Alvos:** 1 criatura (pode ser o próprio usuário)
- **Intensidade I — ◈ (1 PA) + 4 Mana:** o alvo ganha um [Escudo](../glossario.md#escudo) de 1d8 + Inteligência pontos, que absorve dano antes da Vida ser afetada. Dura até o fim do próximo turno do alvo, ou até ser destruído.
- **Intensidade II — ◈◈ (2 PA) + 7 Mana:** o alvo ganha um [Escudo](../glossario.md#escudo) de 2d8 + Inteligência pontos, que absorve dano antes da Vida ser afetada. Dura até o fim do próximo turno do alvo, ou até ser destruído.
- **Intensidade III — ◈◈◈ (3 PA) + 10 Mana:** o alvo ganha um [Escudo](../glossario.md#escudo) de 3d8 + Inteligência pontos, que absorve dano antes da Vida ser afetada. Dura até o fim do próximo turno do alvo, ou até ser destruído.
```

Reação dedicada, que escala **só por Mana**:

```markdown
**Defesa Mágica** *(usada como Reação)*

*A lâmina se ergue no último instante, desviando o golpe que viria.*

- **Chave:** [Buff](../glossario.md#buff)
- **Atributo:** Força | **Alvos:** o próprio usuário
- *(Dedicada a Reação — sempre 0 PA; a Intensidade escolhe só quanto Mana gastar)*
- **Intensidade I — 0 PA + 3 Mana:** quando for alvo de um ataque à distância ou mágico, o usuário pode usar esta habilidade como Reação pra ganhar +4 de Defesa contra aquele ataque, antes do teste de acerto ser resolvido.
- **Intensidade II — 0 PA + 6 Mana:** quando for alvo de um ataque à distância ou mágico, o usuário pode usar esta habilidade como Reação pra ganhar +5 de Defesa contra aquele ataque, antes do teste de acerto ser resolvido.
- **Intensidade III — 0 PA + 9 Mana:** quando for alvo de um ataque à distância ou mágico, o usuário pode usar esta habilidade como Reação pra ganhar +6 de Defesa contra aquele ataque, antes do teste de acerto ser resolvido.
```
