# Criação de Personagem

Cinco passos, nesta ordem. Ao fim deles você tem uma ficha jogável de nível 0.

| Passo | O que você decide | Onde escolher |
|---|---|---|
| **1** | Atributos | [abaixo](#1-atributos) |
| **2** | Raça | [Raças](../racas/index.md) |
| **3** | Origem | [Origem](../origens/index.md) |
| **4** | Primeira Habilidade | [Habilidades](../habilidades/index.md) |
| **5** | Equipamento | [Equipamento](../equipamento/index.md) |

## 1. Atributos

Todo um dos oito [Atributos](../jogar/atributos.md) começa em **5** — não é escolha, é o piso de todo personagem. Depois disso, você distribui **15 pontos livres** entre os oito como quiser.

Os pontos de atributo da **Raça** (passo 2) entram por cima desses valores.

!!! nota "Métodos alternativos de distribuição"
    O sistema antigo oferecia três formas de gerar os atributos iniciais (array fixo, rolagem, ponto-compra), pra grupos que preferem mais ou menos aleatoriedade. Essas variantes ainda não foram redesenhadas pra escala 0-100 — por ora, a distribuição livre de 15 pontos é o único método.

## 2. Raça

<div style="float:right; width:160px; margin:0 0 12px 16px; font-family:'Crimson Pro', Georgia, serif;">
  <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
    <div style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M4 12h16"/><path d="M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/></svg></div>
    <div style="background:#159c56; color:#faf7ef; font-size:8px; letter-spacing:0.06em; text-transform:uppercase; padding:4px 8px; box-sizing:border-box;">Traço Racial</div>
    <div style="padding:5px 8px 8px;"><div style="font-size:6.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:9px; min-height:16px;">&nbsp;</div></div>
  </div>
</div>

Cada [Raça](../racas/index.md) concede:

- **Atributos** — um pool de 2 ou 3 atributos temáticos, com pontos a distribuir entre eles.
- **1 a 3 Traços Raciais** — capacidades fixas, disponíveis desde o nível 0.

Traços raciais **não** competem com as suas 26 escolhas de habilidade — são um extra da raça.

Nenhuma raça jogável é visualmente indistinguível de um humano: toda raça não-humana tem pelo menos um **traço físico inconfundível**, óbvio à primeira vista.

## 3. Origem

<div style="float:right; width:160px; margin:0 0 12px 16px; font-family:'Crimson Pro', Georgia, serif;">
  <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
    <div style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V10l3-2V6h2v1l3-2 3 2V6h2v2l3 2v11"/><path d="M9 21v-5h6v5"/></svg></div>
    <div style="background:#159c56; color:#faf7ef; font-size:8px; letter-spacing:0.06em; text-transform:uppercase; padding:4px 8px; box-sizing:border-box;">Passado</div>
    <div style="padding:5px 8px 8px;"><div style="font-size:6.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:9px; min-height:16px;">&nbsp;</div></div>
  </div>
</div>

A [Origem](../origens/index.md) é o que você viveu antes de virar aventureiro — **três escolhas independentes**, cada uma com 1 traço leve:

- **Passado** — a vida ou profissão antes de aventurar
- **Ambiente de Origem** — a paisagem e cultura onde cresceu (independente da Raça)
- **Evento Formador** — o momento que definiu o personagem

Cada uma pode ser escolhida livremente ou sorteada com 1d20. Somadas, as três valem o mesmo peso mecânico de uma Raça — só divididas em mais eixos.

Na [listagem de Origens](../origens/index.md) as três estão juntas: filtre pelo eixo, ou use o botão de sorteio.

## 4. Primeira Habilidade

Escolha **uma** habilidade de qualquer [grupo](../habilidades/regras.md#grupos), inclusive a Habilidade **Básica** de uma arma. Não há restrição por atributo, raça ou origem: a lista inteira está aberta.

!!! regra "Ter a arma e saber a técnica dela são coisas diferentes"
    Qualquer arma equipada já pode ser usada com **Ataque Básico** (◈, sem Mana, dano do dado da arma), mesmo que o personagem nunca tenha aprendido nenhuma Habilidade dela. Aprender a Habilidade **Básica** de uma arma é o que desbloqueia a técnica nomeada e as três [Intensidades](../habilidades/regras.md#intensidade) dela.

    Numa arma, a ordem é obrigatória: **Básica → Avançada → Especial**. Você não pode aprender a Avançada de uma arma sem ter a Básica dela.

## 5. Equipamento

- **150 de prata** pra gastar como quiser em arma, armadura e escudo na listagem de [Equipamento](../equipamento/index.md) — a arma (e o escudo, se houver) ainda precisa atender o [Requisito de Atributo](../equipamento/regras.md#requisito-de-atributo-minimo) dela.
- **Proficiência de arma** — escolha 1 arma, mesmo que não seja uma que você comprou, e já nasce sabendo a Habilidade **Básica** dela, de graça. Não conta como uma das suas 26 escolhas de habilidade de carreira.

## Valores que você calcula no fim

Com atributos, raça e equipamento fechados, anote na ficha:

| Valor | Fórmula |
|---|---|
| **Vida Máxima** | [20 + Nível + (Defesa × 2) + Vida de equipamento](../jogar/dano-e-cura.md#vida) |
| **Mana Máximo** | [20 + Nível + (Magia × 2) + Mana de equipamento](../jogar/mana.md#mana-maximo) |
| **Evasão** | [Agilidade + Escudo](../jogar/combate.md#defesa) |
| **Fortitude Física** | o próprio valor de Defesa, cru (ver [Defesa em combate](../jogar/combate.md#defesa)) |
| **Fortitude Mágica** | o próprio valor de Magia, cru |
| **Movimento** | [6 casas + (Agilidade ÷ 10)](../jogar/combate.md#movimento), arredondado (mínimo 1) |
| **Estresse Máximo** | [20 + Nível + (Sanidade × 2) + equipamento](../jogar/estresse.md) |
| **Rerolagens** | [1 + (Sorte ÷ 10)](../jogar/testes.md#rerolagens) por descanso longo, arredondado |
| **Limiar de Crítico** | [Sorte ÷ 3](../jogar/testes.md#criticos), arredondado |
| **Pontos de Ação** | 3 ◈ por turno — igual pra todo mundo |

## E depois

**Você sobe de nível a cada sessão jogada** — não há experiência pra somar. Ver [Progressão de Nível](progressao.md) pro que cada nível concede.
