# Testes de d100

| Resumo rápido | |
|---|---|
| Teste básico | **d100 + Atributo vs Dificuldade** — igualou ou superou, sucesso |
| Vantagem / Desvantagem | 2d100, fica com o melhor / o pior |
| Limiar de Crítico | **Sorte ÷ 3** (arredondado) |
| Rerolagens por descanso longo | **1 + (Sorte ÷ 10)** |

Há uma única fórmula no jogo inteiro, e ela resolve tudo — abrir uma fechadura, convencer um guarda, acertar um dragão:

!!! regra "d100 + Atributo vs Dificuldade"
    Role 1d100 (um par de d10, lido como percentil — 00 conta como 100), some o [Atributo](atributos.md) apropriado, e compare com a **Dificuldade** definida pelo Mestre. **Igualar ou superar é sucesso.**

Rolagens de **Habilidade** usam exatamente a mesma lógica, trocando a Dificuldade fixa pelo número-alvo do defensor — **Evasão** pra ataque físico, **Fortitude Mágica** ou **Fortitude Física** pra efeito que pula a Evasão, **Social** ou **Exploração** pra resistir a influência ou percepção (ver [Combate](combate.md#defesa)). Igualou ou superou, acertou.

E é só isso que a rolagem responde. O quanto a habilidade faz **não depende do dado**: depende da [Intensidade](../glossario.md#intensidade) que o jogador pagou antes de rolar.

## Quando rolar

Só quando a ação puder **dar errado** e o fracasso for **interessante**. Se o personagem tem tempo, ferramenta e nenhuma pressão, a ação simplesmente acontece — ver [Quando não pedir teste](../mestre/testes.md#quando-nao-pedir-teste).

A escala de Dificuldades que o Mestre usa está na [tabela de Dificuldades](../mestre/testes.md#a-tabela). Como referência rápida: **Dificuldade 50** é o que uma pessoa treinada faz na maior parte das vezes, **Dificuldade 75** exige competência real, **Dificuldade 100** é façanha.

## Vantagem e Desvantagem

<!-- prisma:verbetes Vantagem Desvantagem -->

Quando o Mestre concede uma e quando concede a outra está em [Vantagem, Desvantagem e rerrolagem](../mestre/testes.md#vantagem-desvantagem-e-rerrolagem).

Na prática: role **2d100** e fique com o maior (Vantagem) ou o menor (Desvantagem). O Crítico só checa o dado que você **manteve**.

## Críticos

<div style="float:right; width:150px; margin:0 0 12px 16px; font-family:'Crimson Pro', Georgia, serif;">
  <div style="position:relative; border:1.2px solid #b39422; border-radius:3px; text-align:center; padding:6px 0; background:#f1ebdc;">
    <div style="position:absolute; top:6px; right:6px; width:15px; height:15px; background:#b39422; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg></div>
    <div style="font-size:8px; color:#b39422; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Lim. Crítico</div>
    <div style="font-size:7px; color:#5b5343; margin-top:3px;">Sorte÷3</div>
  </div>
</div>

<!-- prisma:verbetes Crítico -->

Não existe mais "20 natural" — o crítico escala com **Sorte**, através do **limiar de Crítico**:

!!! regra "Limiar de Crítico = Sorte ÷ 3, arredondado"
    Se o resultado do d100 (o número puro, antes de somar Atributo) for **igual ou menor que o seu limiar**, o teste é **sucesso automático e crítico** — não importa a Dificuldade. Um crítico causa dano máximo, uma rolagem de dano extra, e **sobe 1 Intensidade de graça**.

Como todo atributo nasce em 5 na criação, o limiar nunca é zero: **todo personagem mantém pelo menos 1% de chance de crítico garantido**, mesmo sem nunca investir em Sorte. Quem foca Sorte a sério chega a limiares de 20, 30, ou mais — cada vez mais perto de "sempre acerto, e sempre bem".

**Tirar exatamente 1** no d100, em qualquer teste, marca **1 ponto de [Estresse](../glossario.md#estresse)** — mesmo quando o resultado é sucesso/crítico (o susto de escapar por pouco cobra um preço, mesmo quando a sorte salva você).

Não existe falha crítica ("fumble") neste sistema: uma falha é só uma falha.

## Rerolagens

<div style="float:right; width:150px; margin:0 0 12px 16px; font-family:'Crimson Pro', Georgia, serif;">
  <div style="position:relative; border:1.2px solid #b39422; border-radius:3px; text-align:center; padding:6px 0; background:#f1ebdc;">
    <div style="position:absolute; top:6px; right:6px; width:15px; height:15px; background:#b39422; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-14 5M4 20v-5h5"/></svg></div>
    <div style="font-size:8px; color:#b39422; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Rerolagens</div>
    <div style="font-size:7px; color:#5b5343; margin-top:3px;">1+Sorte÷10/desc.</div>
  </div>
</div>

O jogador pode rerolar **qualquer teste seu que tenha falhado, ou um efeito usado contra si** — não dá pra rerolar um sucesso só pra tentar upar em crítico.

**Usos por descanso longo = 1 + (Sorte ÷ 10)**, arredondado (mínimo 1). A grade reseta completamente a cada [descanso longo](exploracao.md#descanso).

É a válvula de escape do sistema: um teste ruim na hora errada não precisa ser o fim, desde que você ainda tenha carga.

## Testes Sociais

Persuadir, Intimidar, Amedrontar — resolvidos como teste normal, usando **Social**.

A diferença é que um teste social tem **alvo, não Dificuldade fixa**: a dificuldade sai do **Social** de quem está sendo convencido (ou da **Fortitude Mágica**, se o efeito for de origem mágica — ver [Combate](combate.md#defesa)), e do quanto o pedido custa a ele. Ver [Testes Sociais têm alvo, não Dificuldade fixa](../mestre/testes.md#testes-sociais-tem-alvo-nao-dificuldade-fixa).

Nenhum teste social força um PJ a nada — contra jogadores, o resultado informa a cena, não a decisão.

## Testes em grupo

Quando o grupo inteiro tenta a mesma coisa (atravessar o desfiladeiro, passar despercebido), o Mestre escolhe uma das quatro formas de resolver, conforme a ficção — ver [Testes em grupo](../mestre/testes.md#testes-em-grupo).
