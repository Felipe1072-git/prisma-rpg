# Estilo Visual (IA) — Prisma RPG

Manual de referência pra gerar prompts de imagem consistentes (Gemini ou outro gerador) pras artes do Prisma RPG. Fixado numa sessão de design que produziu a capa e a lombada do fichário. Atualize este arquivo sempre que uma peça nova validar uma regra nova ou quebrar uma regra antiga.

Este arquivo é referência pessoal (pasta `referencia/`), não conteúdo publicado do jogo.

## Técnica de pintura

Pintura digital pesada: pincelada visível, textura de tela, luz e sombra dramáticas — como capa de livro de RPG de mesa impresso (referência: livros core de D&D 5ª edição). **Nunca** cel-shading liso de anime, **nunca** flat design de asset de jogo mobile/gacha.

## Paleta por arquétipo

A "trinca" heróica do Prisma RPG usa cor como identidade visual:

| Papel | Cor dominante |
|---|---|
| Guerreiro espadachim | Vermelho/carmesim + dourado |
| Arqueiro | Verde + dourado |
| Mago | Roxo/violeta + dourado |

**Gênero fica livre** — já tentamos travar "todos homens" e ficou forçado/artificial. Deixe o gerador escolher o que ficar mais bonito e coeso, sem restrição de gênero no prompt.

## Composição

- **Colagem dinâmica e assimétrica.** Nunca uma fileira simétrica de frente pra câmera — isso lembra tela de seleção de personagem de jogo mobile.
- **Escalas variadas** entre os personagens (um em destaque mais perto da câmera, outros menores/mais ao fundo) pra dar profundidade e hierarquia visual.
- **Fluxo diagonal** geral na composição.
- **Ação de verdade acontecendo** — golpe em andamento, flecha sendo disparada, feitiço saindo das mãos. Nunca personagens parados "posando".
- Ângulo de câmera com leve dinamismo, não frontal e reto.

## Bugs conhecidos e como evitar

- **Arma duplicada/flutuando:** reforçar explicitamente "UMA ÚNICA arma, segura firme nas mãos — nunca duas armas nem lâminas soltas". Esse bug já apareceu 2x sem esse reforço.
- **Texto/logo na cena principal:** geradores de imagem erram letras com frequência. Pra artes de cena (capa, lombada), nunca peça texto — deixe uma área (geralmente o terço superior, ou uma faixa central na lombada) com menos detalhe e sem elementos importantes, pra inserir o título depois num editor. Só peça texto gerado quando o pedido for especificamente um **logotipo isolado** (fundo branco/transparente, texto como elemento central) — mesmo assim, confira a legibilidade de perto antes de aprovar, e tenha como plano B tipografar manualmente (Canva/Photopea + fonte de fantasia) se sair errado.
- **Citar franquia/personagem específico no texto do prompt** (ex: nome de jogo ou personagem existente) puxa a geração pra replicar demais o design original. Descreva só cor + arquétipo. Se for anexar imagens de personagens existentes como referência visual, instrua explicitamente: *"use apenas como inspiração de paleta/silhueta/técnica de pintura — crie designs originais, não replique roupas, armas, penteados ou acessórios específicos"*. Nunca anexe a arte de referência se ela tiver o logotipo/marca do jogo original desenhado dentro da própria imagem (risco de a IA tentar reproduzir a marca).

## Fluxo de trabalho pra manter consistência entre peças

1. **Sempre anexar a arte já aprovada mais recente** (ex: a capa final) como referência de estilo/paleta junto do prompt de texto, ao gerar uma peça nova relacionada. Foi isso que manteve a lombada coerente com a capa — prompt de texto sozinho, sem imagem de referência, tende a derivar estilisticamente.
2. **Preferir continuar a mesma conversa com o Gemini** em vez de abrir um chat novo do zero, quando for gerar uma peça relacionada — o contexto da conversa ajuda a manter a linha visual.
3. Descrever sempre as **dimensões físicas exatas** de peças que serão impressas (importa pra proporção da composição).

## Notas de impressão física

- Fichário atual: **hemon "para personalizar"**, 4 argolas A4, lombada de **60mm** (420 folhas).
- Peça de capa/contracapa: A4 retrato (210 x 297mm).
- Peça de lombada: 60mm de largura x 297mm de altura (proporção ~1:5, bem estreita).
- Gerar/exportar sempre em resolução alta (300 DPI) nas dimensões físicas exatas antes de imprimir.
- Impressoras domésticas raramente imprimem até a borda de verdade (depende do driver/hardware, não só do app) — o plano seguro é imprimir com a margem mínima possível e **aparar com estilete** depois. Pra lombada, imprime numa folha A4 normal e corta na largura exata.
- Pra combinar duas artes (ex: logo + fundo), o Gemini já fez isso bem quando pedido diretamente na mesma conversa (anexando as duas artes de referência). Alternativa manual: Photopea, camada do elemento com fundo branco em cima, modo de mesclagem "Multiply" pra sumir o branco sem precisar recortar.

## Peças aprovadas (referência de prompt — adapte, não copie literalmente)

### Capa da frente (A4 retrato) — versão final aprovada

```
Estou anexando imagens de referência — use-as pra puxar paleta de cor, silhueta geral e, principalmente, a TÉCNICA DE PINTURA: quero pincelada visível, textura de tela, luz e sombra dramáticas, como uma capa de livro de RPG de mesa impresso — NÃO um estilo de anime com cel-shading liso.

Gere uma ilustração de capa de fichário em formato A4 (retrato, 210x297mm):

CENA: os três heróis em confronto direto com um grupo de monstros — ação de combate real, não personagens posando.

HERÓIS:
1. Guerreiro espadachim — cabelo vermelho/carmesim curto, em primeiro plano, no meio de um golpe de espada (UMA ÚNICA espada — nunca duas, nunca lâminas soltas), armadura leve em vermelho e dourado, capa em movimento.
2. Arqueiro — cabelo verde, disparando uma flecha de energia verde contra os monstros, armadura leve em verde e dourado, pés firmes no chão.
3. Mago — cabelo roxo/violeta, conjurando energia roxa das mãos contra os monstros, vestes leves em roxo e dourado.

MONSTROS (avançando contra os heróis, do lado oposto da composição):
- Um ou dois goblins — humanoides pequenos e verdes, crus e ameaçadores, com armas rústicas.
- Um slime — criatura gelatinosa translúcida com brilho interno colorido.

COMPOSIÇÃO: colagem dinâmica e assimétrica, heróis e monstros em rota de colisão, fluxo diagonal, escalas variadas.

FUNDO: paisagem de fantasia sombria e atmosférica, luz dramática cortando nuvens ou ruínas, textura de pintura a óleo/tela.

Deixe o terço superior com menos elementos, livre pra inserir um título depois — sem texto, letra ou logo na imagem. Sem marcas d'água, sem bordas, preenchendo o quadro A4 inteiro.
```

### Lombada (60mm x 297mm)

```
Crie uma ilustração vertical estreita para a lombada de um fichário A4, nas dimensões 60mm de largura por 297mm de altura (proporção bem alta e fina — gere numa proporção de imagem equivalente, tipo 1:5).

Estilo: a mesma técnica de pintura digital pesada, com pincelada visível e textura de tela, da arte de capa anexada como referência de estilo e paleta de cor.

Conteúdo: continue a atmosfera da cena da capa — céu tempestuoso com raios de luz, ruínas cobertas de musgo, névoa — mas SEM personagens (a lombada é estreita demais pra caber gente sem ficar espremido). Foque em um elemento vertical natural da cena (coluna de ruína, fresta de luz, névoa subindo), continuando visualmente a mesma paisagem/mundo.

Mantenha a faixa central com menos detalhe visual, mais uniforme em tom, pra sobrepor o título do sistema verticalmente ali depois.

Sem texto, letra ou logo na imagem. Pintura digital de alto nível, sem bordas, preenchendo o quadro inteiro.
```

### Logotipo vertical isolado

```
Crie um logotipo/título decorativo em formato vertical (mais alto que largo) para "PRISMA RPG" — o texto deve ficar empilhado ou organizado verticalmente, não numa linha horizontal única.

Estilo: tipografia de fantasia ornamentada, entalhada ou com filete dourado, como títulos de capas de livros de RPG de mesa premium — combinando com a paleta de cor quente-pra-fria (vermelho a roxo) da arte de capa anexada como referência.

Pode incluir pequenos elementos decorativos ao redor do texto (moldura, floreios, um pequeno símbolo/emblema central que remeta a um prisma/cristal), mas o texto "PRISMA RPG" deve ser o elemento central e legível.

Fundo transparente ou branco liso — isso é só o logotipo isolado, para sobrepor em outras peças depois.
```

### Retrato de personagem único (NPC/divindade)

Validado com as 4 divindades do Panteão de Pania (Jovar, Kai, Bran, Val) — os quatro
prompts saíram consistentes entre si e fiéis ao pedido, sem precisar de retentativa.
Formato vertical ~3:4 (a ficha lateral da wiki de Mundo corta pra esse enquadramento e
mostra a imagem inteira no lightbox ao clicar). Diferente da capa/lombada, aqui é um
personagem só, sem cena de grupo — mas a regra de "ação de verdade, não pose de boneco"
continua valendo: pose de comando/gesto de poder, nunca frontal e parado.

Também validado num **NPC mortal sem facção** (Ondrus — sábio itinerante, espécie e idade
propositalmente incertas na lore). Duas adaptações que funcionaram bem e valem pra qualquer
NPC no mesmo espírito:

- **Ambiguidade que é lore, não indecisão:** quando a própria descrição do personagem deixa
  espécie/idade em aberto de propósito, o prompt pede pra arte *preservar* isso — "humanoide,
  mas não deixe claro se é X ou Y", rosto atemporal — em vez de a IA resolver a ambiguidade
  escolhendo uma raça/idade concreta sozinha.
- **Neutralidade de facção via paleta:** personagem sem facção não usa a paleta de nenhum
  lado em conflito — vestes em tons neutros (cinza, marrom terroso, branco sujo), e o único
  ponto de cor viva é o efeito mágico em si, descrito como "sem cor fixa" (branco/prateado/
  levemente prismático) quando a lore diz que a magia dele não tem assinatura elemental.

```
Estou anexando uma arte de referência — use-a pra puxar a TÉCNICA DE PINTURA: pincelada visível, textura de tela, luz e sombra dramáticas, como ilustração de personagem numa capa de livro de RPG de mesa impresso. NÃO estilo anime de cel-shading liso, NÃO flat design de jogo mobile.

Gere um retrato de corpo inteiro ou 3/4, em formato vertical (proporção aproximada 3:4, resolução alta), de Ondrus — um sábio itinerante, mestre de magia Arcana, de espécie e idade indeterminadas. Ele não serve a nenhuma facção e não é um combatente: é uma figura enigmática que aparece pouco antes de algo importante acontecer e some logo depois.

APARÊNCIA: humanoide, mas deliberadamente ambíguo — não deixe claro se é humano, élfico ou algo mais estranho; a idade também deve parecer indefinida (nem jovem, nem visivelmente idoso — um rosto sereno e atemporal, quase impossível de datar). Vestes de viajante simples e desgastadas pelo tempo, em camadas — manto/capuz que cobre parte do rosto em sombra, sugerindo alguém que passou por muitas estradas. Carrega um único cajado de viajante entalhado (não duas armas, nunca objetos duplicados flutuando).

MAGIA: ele conjura Arcano puro — mana sem elemento, sem assinatura de cor fixa. Mostre isso como uma energia branca/prateada/levemente prismática (reflexos sutis de várias cores, nunca uma cor dominante única) se formando em um símbolo ou círculo arcano saindo de uma das mãos — um gesto calmo e controlado, não um ataque.

PALETA: tons neutros e discretos nas vestes — cinza, marrom terroso, branco sujo — para não remeter à cor de nenhuma facção específica. A energia arcana branco-prateada-prismática é o único ponto de cor viva da cena.

POSE: um momento de poder tranquilo e deliberado — conjurando o feitiço, ou meio virado como se estivesse prestes a desaparecer de novo — nunca uma pose estática de "boneco de vitrine", nunca uma pose de combate.

FUNDO: um cruzamento de estradas ao entardecer ou amanhecer, névoa baixa, luz difusa e ambígua (nem claramente de um exército nem de outro) — um lugar de passagem, não um campo de batalha.

Sem texto, letra ou logo na imagem. Sem bordas, preenchendo o quadro inteiro.
```

```
Estou anexando uma arte de referência — use-a pra puxar a TÉCNICA DE PINTURA: pincelada visível, textura de tela, luz e sombra dramáticas, como ilustração de deus numa capa de livro de RPG de mesa impresso. NÃO estilo anime de cel-shading liso, NÃO flat design de jogo mobile.

Gere um retrato de corpo inteiro ou 3/4, em formato vertical (proporção aproximada 3:4, resolução alta), de uma divindade da guerra e da estratégia — um general-imperador de presença imponente e disciplinada, meia-idade, expressão calculista e severa (não fúria selvagem).

Armadura de placas ornamentada em aço polido e dourado, com detalhes de comandante militar (não uma armadura genérica de soldado raso). Empunha UMA ÚNICA espada curta de aço (nunca duas armas, nunca lâminas soltas) e carrega um grande escudo redondo/retangular com brasão vermelho e dourado.

Paleta: aço/prata, dourado, vermelho carmesim de estandarte de legião.

Fundo: campo de batalha ao entardecer, fileiras de soldados marchando em formação ao longe, estandartes tremulando, poeira e luz dourada cortando a cena. Pose de comando — braço erguido dando ordem, ou espada baixa em posição de repouso pós-vitória — não uma pose estática de "boneco de vitrine".

Sem texto, letra ou logo na imagem. Sem bordas, preenchendo o quadro inteiro.
```

### Cena de facção (retrato-cena, não retrato-único)

Validado com a Guarda do Véu (ordem religiosa militante devota a Val, mas "algo à parte"
da própria fé que a originou). Diferente do retrato-único das divindades, uma facção pede
**ação de verdade** — a mesma regra de composição da capa/lombada, só que com 2-3
personagens em vez de 3 heróis completos, e formato horizontal (~16:9) em vez de vertical.
Serve pro mesmo campo **Retrato** da ficha lateral — a wiki não distingue formato, só
mostra a imagem no topo.

Ponto que funcionou bem: pedir **paleta distinta** da referência anexada quando a peça
precisa comunicar uma identidade visual diferente da fonte (aqui, a Guarda precisava
parecer "à parte" do clero regular de Val) — anexar a arte de referência só pra técnica de
pintura, e escrever explicitamente qual paleta NOVA usar em vez da paleta da referência.

```
Estou anexando o retrato de [personagem/divindade relacionado] — use-o SÓ como referência
de TÉCNICA DE PINTURA (pincelada visível, textura de tela, luz e sombra dramáticas, como
ilustração de livro de RPG de mesa impresso — NÃO cel-shading de anime, NÃO flat design de
jogo mobile). A paleta desta cena é DIFERENTE da paleta da referência: [descreva a paleta
nova e por que ela precisa ser diferente].

Gere uma cena de combate, formato horizontal, [N] membros de [facção] enfrentando
[antagonista, descrito com o mesmo cuidado dos heróis — não deixe genérico].

PERSONAGENS (ação real de combate, não pose parada):
1. [Personagem 1] em primeiro plano, no meio de [ação específica] — [armadura/vestes,
símbolo distintivo da facção]. Empunha UMA ÚNICA arma corpo a corpo (escolha uma só,
nunca duas armas nem lâminas soltas).
2. [Personagem 2] [papel/posição na composição, contraste com o personagem 1].

INIMIGO: [descrição específica, não "monstro genérico"].

COMPOSIÇÃO: colagem dinâmica assimétrica, fluxo diagonal, escalas variadas.

FUNDO: [cenário que reforça o conflito/tema da facção].

Sem texto, letra ou logo na imagem. Sem bordas, preenchendo o quadro inteiro.
```

Convenção técnica pra encaixar na wiki: salvar em `docs/assets/img/mundo/<nome>.jpg`
(redimensionado pra ~1400px de altura, qualidade JPEG ~87 — dá pra cortar um arquivo de
~3MB gerado pelo Gemini pra ~300KB sem perda visível), e na página de Mundo (`tipo:
divindade`, `pessoa` etc.) adicionar `**Retrato:** ![Nome](../../caminho/pro/arquivo.jpg)`
como primeiro campo da ficha — o hook (`hooks/prisma.py`, campo especial `retrato`) tira o
rótulo em negrito e mostra como imagem grande no topo. Clicar na imagem abre ela inteira
em tela cheia (lightbox em `prisma.js`/`prisma.css`).

### Ilustração de página de regra (Jogando o Jogo, Criação, Livro do Mestre)

Validado com as 18 páginas de regra do site (2026-08-23) — banner de abertura em 16:9 nas
páginas mais "de capítulo" (Combate, Exploração, os três índices), inserção menor em
formato retrato (~4:5) flutuando ao lado da prosa nas páginas mais "de conceito único"
(Mana, Estresse, Atributos). Sem elenco fixo — cada cena tem personagens genéricos
próprios, sem vínculo com o trio da capa/lombada; a técnica de pintura é o que amarra
tudo, não o elenco.

Duas armadilhas de composição que apareceram nessa leva e valem registrar:

- **"Tela de seleção de personagem"** também acontece fora de retrato de NPC único: uma
  cena pensada como "vários personagens genéricos representando uma lista" (ex: as raças
  na Criação de Personagem) puxa fácil pra fileira simétrica de frente pra câmera. A
  correção foi a mesma da regra geral — profundidade e ângulo variados, uma figura em
  destaque, nunca todas iguais e de frente.
- **Progressão em 3 estágios não deve virar 3 painéis lado a lado** (ex: Progressão de
  Nível, Intensidade de Habilidade) — isso lembra infográfico técnico, não pintura. Melhor
  resolver como uma cena só, contínua: camadas translúcidas do mesmo personagem se
  fundindo numa pintura (Progressão), ou um efeito único crescendo em escala dentro do
  próprio quadro (Intensidade), em vez de repetir a figura em compartimentos separados.

Convenção técnica: salvar em `docs/assets/img/regras/<nome>.jpg` (banner ~1440px de
largura, retrato ~700px), e no topo da página (logo abaixo do `#` título) adicionar
`<img class="prg-arte" src="../assets/img/regras/<nome>.jpg" alt="">` pro banner, ou
`<img class="prg-arte prg-arte--retrato" ...>` pra inserção flutuante — classes definidas
em `docs/assets/css/prisma.css`. Sem legenda de propósito, igual ao retrato de Mundo.

### Capa como hero da home

A mesma arte de capa do fichário (peça aprovada acima) também vira a primeira coisa que
quem abre o site vê: `docs/assets/img/capa.jpg` (900px de largura, ~85% qualidade),
inserida logo no topo de `docs/index.md` como `<img class="prg-capa-hero" ...>`,
substituindo o logo pequeno que existia ali. Não precisou gerar peça nova — a mesma arte
de impressão serve pros dois usos.
