# Os Oito Atributos

Todo personagem e toda criatura do jogo é descrito pelos mesmos oito números, de **0 a
100**. Eles entram em tudo: no d100 que você rola, na Evasão que o inimigo precisa superar,
na Vida que você aguenta e no tanto de Mana que você carrega.

<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:16px 0; font-family:'Crimson Pro', Georgia, serif; max-width:520px;">
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #b8502e; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#b8502e; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:8px; height:8px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M45.95 14.553c-19.38.81-30.594 11.357-30.282 30.283l19.768 30.78c4.43-1.213 9.36-3.838 14.248-7.335l42.474 59.935c-17.018 20.83-31.258 44.44-42.71 70.836l26.55 26.552c11.275-23.6 24.634-44.826 39.918-63.864l210.82 297.475 166.807 33.213L460.33 325.62 162.78 114.745c19.907-16.108 41.842-29.91 65.652-41.578l-26.553-26.55c-27.206 11.803-51.442 26.576-72.735 44.292L69.39 48.56c3.443-4.823 6.062-9.735 7.342-14.242l-30.78-19.765zm400.84 86.933v.008l.003-.008h-.002zm0 .008-28.028 124.97-25.116-80.593-18.105 70.667-26.862-49.64-.584 57.818 128.484 91.69 15.184 87.017-1.168-186.885-34.457 39.713-9.346-154.756zm-300.95 27.98 222.224 196.368 25.645 66.75-66.75-25.645L130.6 144.734a308.453 308.453 0 0 1 15.238-15.26zm32.305 196.274v.004h.005l-.005-.004zm.005.004 28.028 22.775-36.21 4.088 57.82 19.272-105.706 4.09 115.05 27.45L136.1 422.114l127.316 25.696-67.164 43.803 208.494 1.752-87.017-15.185-104.54-150.676-35.037-1.752z"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Ataque</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #a3781a; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#a3781a; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 5-3.5 8-7 9-3.5-1-7-4-7-9V6z"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Defesa</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #4c7a3d; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#4c7a3d; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15c4-7 13-7 17-7"/><path d="M15 4l5 4-5 4"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Agilidade</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #3f5fa0; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#3f5fa0; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="14" r="6.5"/><path d="M18 1 L19.5 4.5 L23 6 L19.5 7.5 L18 11 L16.5 7.5 L13 6 L16.5 4.5 Z" fill="currentColor" stroke="none"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Magia</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #a04570; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#a04570; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v12H9l-5 4z"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Social</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #2d7a6e; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#2d7a6e; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15 9l-2 6-6 2 2-6z"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Exploração</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #b39422; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#b39422; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="8.5" cy="8.5" r="1" fill="currentColor" stroke="none"/><circle cx="15.5" cy="8.5" r="1" fill="currentColor" stroke="none"/><circle cx="8.5" cy="15.5" r="1" fill="currentColor" stroke="none"/><circle cx="15.5" cy="15.5" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Sorte</div>
  </div>
  <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #6a3fa0; background:#f1ebdc; text-align:center; padding:6px 0 5px;">
    <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#6a3fa0; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13h4l2-7 4 14 2-7h6"/></svg></div>
    <div style="font-size:8px; letter-spacing:0.04em; color:#5b5343; text-transform:uppercase;">Sanidade</div>
  </div>
</div>

| Atributo | Representa | Onde mais aparece |
|---|---|---|
| **Ataque** | Poder físico bruto e técnica com armas — corpo a corpo ou à distância | [Dano Físico](dano-e-cura.md) |
| **Defesa** | Resistência física — encaixar, aguentar pancada | [Vida](../glossario.md#vida) e Fortitude Física |
| **Magia** | Poder mágico — controlar e canalizar Mana | [Mana Máximo](../glossario.md#mana), Fortitude Mágica e Dano Mágico |
| **Agilidade** | Reflexos e velocidade — desviar de golpes, reagir rápido | [Evasão](../glossario.md#evasao), [Movimento](../glossario.md#movimento) e [Iniciativa](../glossario.md#iniciativa) |
| **Sorte** | Acaso e fortuna — estar no lugar certo na hora certa | [Taxa de Crítico](testes.md#criticos), [Iniciativa](../glossario.md#iniciativa) e usos de [Rerolagem](testes.md#rerolagens) |
| **Sanidade** | Estabilidade mental — resistir a horror e colapso psicológico | [Estresse Máximo](../glossario.md#estresse) |
| **Social** | Presença e habilidade de influenciar os outros (o "Carisma" deste sistema) — persuadir, enganar, intimidar, e resistir a tudo isso | testes sociais, nos dois sentidos |
| **Exploração** | Atenção ao ambiente e competência de aventureiro — notar o escondido, rastrear, se orientar, sobreviver | testes de viagem, percepção |

Atributos podem assumir valores **negativos** — por penalidades, dano ou debuffs. Um -10 em
Agilidade rebaixa a Evasão e o Movimento do mesmo jeito que um +10 os aumentaria.

## A faixa de valores

**Na criação, todo atributo começa em 5**, e o jogador distribui **15 pontos livres** entre
os oito como quiser (ver [Distribuição na Criação](../criacao/index.md#1-atributos)).

A partir do **nível 2**, a cada nível par o personagem ganha **5 pontos** pra distribuir
livremente (ver [Progressão](../criacao/progressao.md)) — 250 pontos ao longo dos 100
níveis. Um atributo focado a carreira inteira chega ao teto de **100** bem antes do fim de
jogo; um atributo dividido com outro ("misto") chega perto do teto só no fim; um atributo
disperso entre vários nunca chega lá.

Contra a maioria das Dificuldades, um atributo bem investido deixa a rolagem quase
automática — é a recompensa de ter focado ali. Mas as duas Dificuldades mais altas da
[Tabela de Dificuldades](../mestre/testes.md#a-tabela) (125 e 150) continuam exigindo
desafio real mesmo pro personagem mais especializado do jogo: nem um 100 natural sozinho
alcança, sem atributo investido.

## Qual atributo a minha habilidade usa

Cada habilidade declara o atributo dela na própria ficha, no campo **Atributo** — é o que
você soma ao d100 quando ativa ela. A [Listagem de Habilidades](../habilidades/index.md)
filtra por esse campo: dá pra ver de uma vez tudo o que um personagem de Magia alta
consegue usar bem.

Como não há classes, **nada impede um personagem de aprender uma habilidade cujo atributo
ele não tem**. Ele só vai acertar menos — e, se o atributo estiver muito abaixo do
recomendado pra Escala daquela habilidade, rola com [Desvantagem](testes.md#vantagem-e-desvantagem)
(ver [Requisito suave de Atributo](mana.md#requisito-suave-de-atributo)). Essa é toda a
"restrição de classe" que o sistema tem.

## Do lado do Mestre

Criaturas usam os mesmos oito atributos, mas a ficha delas é mais enxuta — só o que entra
em rolagem — e os valores são **escritos à mão**, não calculados por uma fórmula de
progressão: o Tier dela (Comum/Treinado/Formidável/Lendário) é só uma referência de faixa
esperada, não uma obrigação. Ver [Bestiário](../mestre/criando-criaturas.md#como-ler-uma-ficha-de-criatura).
