# Elenco do SRD — lista de escolha pro Bestiário

Levantamento feito uma vez (2026-08-02) a partir de [dnd5eapi.co](https://www.dnd5eapi.co),
que serve o SRD 5.1. **334 criaturas.** Este arquivo não é publicado: é uma lista pra o autor
marcar o que quer, não conteúdo de jogo.

## O que se aproveita, e o que não

**Não se aproveita nenhum número.** O Prisma re-deriva tudo: a Vida vem da tabela por Tier
(8/25/60/180), a Defesa física é Base + Agilidade + Couraça. O goblin do SRD tem HP 7 e AC 15;
o nosso tem Vida 8 e Defesa 8. Importar os campos seria jogar quase todos fora.

**Aproveita-se o elenco e a forma dos traços** — *Pack Tactics*, *Undead Fortitude*,
*Nimble Escape* são exatamente o que o Livro do Mestre chama de traço que muda o alvo, a
solução ou o tempo.

**Licença:** o SRD 5.1 é CC BY 4.0, compatível com o CC BY 4.0 do Prisma, mas exige atribuição
se houver **texto copiado**. Nada aqui copia texto: a lista é de nomes, e nome de bicho de
folclore (goblin, troll, hidra) não é propriedade de ninguém. Se em algum momento uma
descrição do SRD for reaproveitada literalmente, aí a atribuição a Wizards of the Coast entra
no rodapé do site.

## Achado: CR não vira Tier

A primeira ideia era mapear CR → Tier por faixa. **Não funciona** — e a prova está nas seis
criaturas que já existem:

| Criatura | CR no SRD | Tier no Prisma | Bate? |
|---|---|---|---|
| Goblin | 1/4 | Comum | sim |
| Lobo | 1/4 | Comum | sim |
| Bandido | 1/8 | **Treinado** | não — subiu |
| Esqueleto | 1/4 | **Treinado** | não — subiu |
| Dragão Filhote | 10 (Young Red Dragon) | **Formidável** | não — desceu |

Três das cinco discordam, e por um motivo que já está escrito em *Criando uma Criatura*:
**"escolha o Tier pela função na cena, não pelo tamanho do bicho"**. O Bandido subiu porque é
um oponente com plano; o Dragão desceu porque é o primeiro chefe de um grupo de nível 1–4.

Então o CR entra aqui só como **ordem de potência** — pra a lista não ficar embaralhada. O
Tier de cada criatura escolhida é decisão sua, uma a uma.

## O que o Bestiário já cobre

Antes de escolher, o que as criaturas atuais já ensinam — porque criatura nova só se
justifica se trouxer um **problema novo**, não outro saco de Vida:

| Já coberto | Por quem |
|---|---|
| ameaça por quantidade | Goblin |
| mobilidade, punir quem se isolou | Lobo |
| oponente tático, mantém distância | Bandido |
| o tipo de dano importa (resistência + vulnerabilidade) | Esqueleto |
| a criatura se multiplica | Slime |
| chefe com Mana e Intensidade | Dragão Filhote |
| não cai quando deveria | Zumbi *(leva 1)* |
| arma não resolve; divide a casa | Enxame de Ratos *(leva 1)* |
| avança e pune quem recuou | Orc *(leva 1)* |
| tira o turno do personagem | Carniçal *(leva 1)* |
| atravessa parede e drena atributo | Sombra *(leva 1)* |
| regenera; só fogo encerra | Troll *(leva 1)* |
| ameaça aérea barata; caça o ferido | Falcão-de-sangue *(leva 2)* |
| alcance 2 casas e primeiro golpe brutal | Bugbear *(leva 2)* |
| engole; e o primeiro bicho lento (1 PA) | Cubo Gelatinoso *(leva 2)* |
| a sala é a armadilha; prende a arma | Mímico *(leva 2)* |
| **ataca a Defesa mental**; vira o grupo contra si | Súcubo *(leva 2)* |
| arremessa pedra — e arremessa personagem | Gigante da Colina *(leva 2)* |

| o chefe conhecido, crescido | Dragão Vermelho Adulto *(leva 3)* |
| matar não resolve: vira missão | Lich *(leva 3)* |
| chefe com fraquezas investigáveis | Vampiro *(leva 3)* |
| enigma de elemento; imune a controle | Golem de Ferro *(leva 3)* |

**Levas 1, 2 e 3 entregues em 2026-08-02/03** — as dezesseis marcadas abaixo já estão em
`docs/bestiario/index.md`. O Bestiário passou de 6 para **22 criaturas**, e os quatro Tiers
estão povoados.

O que sobrou de lacuna real, pra uma eventual leva 4: **petrificar** (Basilisco, Medusa —
precisaria de uma condição nova, que não existe no glossário), **criar servo** (Aparição),
**possuir um personagem** (Fantasma), **frenesi que cresce** (Gnoll, Bárbaro) e **material
específico pra ferir** (Lobisomem).

## Sugestões, por banda de potência

Marque com `x` o que quiser. Cada linha traz **o que ela acrescenta** — se a coluna estiver
fraca, a criatura provavelmente não vale uma ficha.

### Capangas (candidatos a Comum)

| | Criatura | O que acrescenta |
|---|---|---|
| [x] | Zumbi | não cai: continua de pé quando deveria ter morrido |
| [x] | Enxame de Ratos | enxame — ocupa uma casa, e espada não resolve |
| [ ] | Kobold | covarde que só é perigoso em grupo grande *(muito perto do Goblin)* |
| [ ] | Stirge | gruda no alvo e drena até ser arrancada |
| [x] | Falcão-de-sangue | voador barato — obriga o grupo a ter resposta pro ar |
| [ ] | Sprite | minúsculo, escondido, flecha de sono |

### Obstáculos (candidatos a Treinado)

| | Criatura | O que acrescenta |
|---|---|---|
| [x] | Orc | o capanga marcial que avança e bate forte |
| [ ] | Hobgoblin | inimigo com disciplina militar — formação, não bando |
| [ ] | Gnoll | frenesi: fica mais perigoso a cada abate |
| [x] | Sombra | incorpórea: atravessa parede e drena atributo |
| [x] | Carniçal | paralisia — tira o turno do personagem |
| [x] | Bugbear | emboscada: dano brutal no primeiro golpe, medíocre depois |
| [ ] | Ogro | bruto lento: muito dano, pouca precisão |
| [x] | Mímico | armadilha viva — o baú era o monstro |
| [x] | Cubo Gelatinoso | engole; o corredor inteiro vira a ameaça |
| [ ] | Gárgula | voador de pedra, aguenta pancada |
| [ ] | Bárbaro Enfurecido | quanto mais ferido, mais forte |
| [ ] | Lobisomem-rato (Wererat) | resistência que só material específico ignora |
| [ ] | Fogo-fátuo | invisível, atrai o grupo pro lugar errado |

### Chefes de arco (candidatos a Formidável)

| | Criatura | O que acrescenta |
|---|---|---|
| [ ] | Corujurso (Owlbear) | fera de força bruta, sem plano nenhum |
| [ ] | Basilisco | olhar que petrifica — ameaça sem rolar ataque |
| [ ] | Mantícora | atirador aéreo: fica no ar e dispara espinhos |
| [ ] | Múmia | medo + maldição que sobrevive ao combate |
| [ ] | Aparição (Wight) | mata e transforma o morto em servo dela |
| [ ] | Lobo do Inverno | sopro de gelo — a contraparte elemental do Dragão |
| [ ] | Fantasma | possui um personagem: o grupo luta contra o próprio aliado |
| [x] | Súcubo | ameaça social — vence sem combate se ninguém perceber |
| [x] | Troll | regeneração: só fogo resolve de vez (não existe dano de Ácido no Prisma) |
| [x] | Gigante da Colina | arremessa pedras — e arremessa personagens |
| [ ] | Elemental (Fogo/Água/Terra/Ar) | um elemento puro em forma de criatura — encaixa nos 11 |
| [ ] | Medusa | petrifica pelo olhar e ainda atira de longe |
| [ ] | Wyvern | voador com ferrão venenoso |
| [ ] | Quimera | três ataques por turno + sopro: administra recurso como chefe |
| [ ] | Oni | chefe inteligente: voa, conjura e negocia |
| [ ] | Hidra | cortar faz crescer — o Slime em escala de chefe |

### Fim de campanha (candidatos a Lendário)

| | Criatura | O que acrescenta |
|---|---|---|
| [x] | Dragão Vermelho Adulto | a escada natural do Dragão Filhote |
| [x] | Vampiro | chefe social, regenera e cria servos |
| [x] | Lich | o arquimago morto-vivo: vilão de campanha inteira |
| [x] | Golem de Ferro | construto imune a quase tudo — puzzle, não luta |
| [ ] | Treant | guardião: a floresta inteira reage |
| [ ] | Roc | escala pura — a ave que carrega o grupo embora |
| [ ] | Kraken | chefe de mar aberto |
| [ ] | Tarrasque | o fim do mundo com pernas |

## Como eu escreveria cada uma

Marcada a criatura, a ficha nasce pelos cinco passos de *Criando uma Criatura*: frase de
conceito → Tier pela função → copiar a coluna → atributos que a frase pede → 1 ou 2 traços.
O SRD entra só como lembrete de comportamento. Cada ficha passa por você antes de entrar em
`docs/bestiario/index.md`.

## Anexo: o levantamento completo

Os 334 nomes agrupados por Tier estimado (só ordem de potência) ficaram fora deste arquivo
de propósito — 80 deles são *Cat*, *Goat*, *Frog*, *Awakened Shrub* e afins. O script que
gera a lista é de uso único e não vive no repositório; regerar é uma requisição por valor de
CR em `https://www.dnd5eapi.co/api/2014/monsters?challenge_rating=N`.
