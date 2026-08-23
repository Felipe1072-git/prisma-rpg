# Testes de d100

Há uma única fórmula no jogo inteiro, e ela resolve tudo — abrir uma fechadura, convencer um guarda, acertar um dragão:

!!! regra "d100 + Atributo vs Dificuldade"
    Role 1d100 (um par de d10, lido como percentil — 00 conta como 100), some o [Atributo](atributos.md) apropriado, e compare com a **Dificuldade** definida pelo Mestre. **Igualar ou superar é sucesso.**

Rolagens de **Habilidade** usam exatamente a mesma lógica, trocando a Dificuldade fixa pelo número-alvo do defensor — **Evasão** pra ataque físico, **Fortitude Mágica** ou **Fortitude Física** pra efeito que pula a Evasão, **Social** ou **Exploração** pra resistir a influência ou percepção (ver [Combate](combate.md#defesa)). Igualou ou superou, acertou.

E é só isso que a rolagem responde. O quanto a habilidade faz **não depende do dado**: depende da [Intensidade](../habilidades/regras.md#intensidade) que o jogador pagou antes de rolar.

## Quando rolar

Só quando a ação puder **dar errado** e o fracasso for **interessante**. Se o personagem tem tempo, ferramenta e nenhuma pressão, a ação simplesmente acontece — ver [Quando não pedir teste](../mestre/testes.md#quando-nao-pedir-teste).

A escala de Dificuldades que o Mestre usa está na [tabela de Dificuldades](../mestre/testes.md#a-tabela). Como referência rápida: **Dificuldade 50** é o que uma pessoa treinada faz na maior parte das vezes, **Dificuldade 75** exige competência real, **Dificuldade 100** é façanha.

## Vantagem e Desvantagem

<!-- prisma:verbetes Vantagem Desvantagem -->

Quando o Mestre concede uma e quando concede a outra está em [Vantagem, Desvantagem e rerrolagem](../mestre/testes.md#vantagem-desvantagem-e-rerrolagem).

Na prática: role **2d100** e fique com o maior (Vantagem) ou o menor (Desvantagem). O Crítico só checa o dado que você **manteve**.

## Críticos

<!-- prisma:verbetes Crítico -->

Não existe mais "20 natural" — o crítico escala com **Sorte**, através do **limiar de Crítico**:

!!! regra "Limiar de Crítico = Sorte ÷ 3, arredondado"
    Se o resultado do d100 (o número puro, antes de somar Atributo) for **igual ou menor que o seu limiar**, o teste é **sucesso automático e crítico** — não importa a Dificuldade. Um crítico causa dano máximo, uma rolagem de dano extra, e **sobe 1 Intensidade de graça**.

Como todo atributo nasce em 5 na criação, o limiar nunca é zero: **todo personagem mantém pelo menos 1% de chance de crítico garantido**, mesmo sem nunca investir em Sorte. Quem foca Sorte a sério chega a limiares de 20, 30, ou mais — cada vez mais perto de "sempre acerto, e sempre bem".

**Tirar exatamente 1** no d100, em qualquer teste, marca **1 ponto de [Estresse](estresse.md)** — mesmo quando o resultado é sucesso/crítico (o susto de escapar por pouco cobra um preço, mesmo quando a sorte salva você).

Não existe falha crítica ("fumble") neste sistema: uma falha é só uma falha.

## Rerolagens

O jogador pode rerolar **qualquer teste seu que tenha falhado, ou um efeito usado contra si** — não dá pra rerolar um sucesso só pra tentar upar em crítico.

**Usos por descanso longo = 1 + (Sorte ÷ 10)**, arredondado (mínimo 1). A grade reseta completamente a cada [descanso longo](exploracao.md#descanso).

É a válvula de escape do sistema: um teste ruim na hora errada não precisa ser o fim, desde que você ainda tenha carga.

## Testes Sociais

Persuadir, Intimidar, Amedrontar — resolvidos como teste normal, usando **Social**.

A diferença é que um teste social tem **alvo, não Dificuldade fixa**: a dificuldade sai do **Social** de quem está sendo convencido (ou da **Fortitude Mágica**, se o efeito for de origem mágica — ver [Combate](combate.md#defesa)), e do quanto o pedido custa a ele. Ver [Testes Sociais têm alvo, não Dificuldade fixa](../mestre/testes.md#testes-sociais-tem-alvo-nao-dificuldade-fixa).

Nenhum teste social força um PJ a nada — contra jogadores, o resultado informa a cena, não a decisão.

## Testes em grupo

Quando o grupo inteiro tenta a mesma coisa (atravessar o desfiladeiro, passar despercebido), o Mestre escolhe uma das quatro formas de resolver, conforme a ficção — ver [Testes em grupo](../mestre/testes.md#testes-em-grupo).
