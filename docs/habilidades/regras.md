# Regras de Habilidade

Como toda habilidade é escrita e resolvida por baixo do capô — grupos, Intensidade, custo, Dano Desarmado e a assinatura mecânica de cada elemento. Pra navegar e filtrar as habilidades em si, veja a [Listagem de Habilidades](index.md).

## Grupos

| Grupo | Escopo |
|---|---|
| [Marciais](marciais.md) | Armas corpo a corpo / combate a curta distância |
| [Pontaria](pontaria.md) | Armas à distância e precisão (inclui feitiços de precisão) |
| [Mágicas por Elemento](magicas-elementais.md) | Fogo, Gelo, Terra, Sombras, Luz, Arcano, etc. |
| [Sociais](sociais.md) | Persuasão e afins |
| [Infiltração](infiltracao.md) | Furtividade, ladinagem |
| [Mobilidade](mobilidade.md) | Voo, deslocamento |
| [Buff](buff.md) | Incremento de força, imbuir elementos em armas, etc. |
| [Debuff](debuff.md) | Desvantagens para inimigos ou em testes |
| [Suporte](suporte.md) | Cura e apoio a aliados |
| [Necromancia](necromancia.md) | Drenar vigor, amaldiçoar, erguer mortos, gastar a própria vitalidade |
| [Projeção Mental](projecao-mental.md) | Telepatia, ler mentes, ilusão mental, dano psíquico |
| [Alquimia de Mana](alquimia-de-mana.md) | Mana altera a matéria: endurecer o corpo, transmutar, consertar objetos, imbuir armas |
| [Percepção Arcana](percepcao-arcana.md) | Enxergar o invisível, rastrear pelo resíduo de mana, premonição em combate |
| [Conjuração](conjuracao.md) | Trazer aliados de outros lugares/planos pra lutar ao seu lado |
| [Espaço-Tempo](espaco-tempo.md) | Reposicionar à força, distorcer gravidade e manipular o fluxo do tempo |

*(Lista de grupos pode crescer.)*

## Ficha de Habilidade

<div style="max-width:260px; margin:0 auto 14px; font-family:'Crimson Pro', Georgia, serif; color:#211c14;">
  <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; display:flex; flex-direction:column;">
    <span style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
      <svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg>
    </span>
    <div style="padding:4px 34px 2px 8px;">
      <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em;">Nome</div>
      <div style="border-bottom:1px solid #cabf9f; min-height:11px; font-size:10px;">&nbsp;</div>
    </div>
    <div style="display:flex; gap:9px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
      <div style="flex:1;">Chave<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      <div style="flex:1;">Atributo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      <div style="flex:1;">Tipo de Dano<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      <div style="flex:1;">Alvo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      <div style="flex:1;">Alcance<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
    </div>
    <div style="display:flex; align-items:center; gap:7px; padding:2px 8px 1px;">
      <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 28px;">Tipo</span>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Intensidade</label>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Custo Fixo</label>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Passiva</label>
    </div>
    <div style="display:flex; align-items:center; gap:7px; padding:1px 8px 2px; border-bottom:1.2px solid #83765a;">
      <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 28px;">Ação</span>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ataque</label>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Área</label>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Efeito</label>
      <label style="display:flex; align-items:center; gap:2px; font-size:6.8px;">
        <span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>
        <svg viewBox="0 0 10 10" style="width:7px; height:7px;" aria-hidden="true"><path d="M5 1 L9 9 L1 9 Z" fill="#159c56"/></svg>
        Reação <span style="color:#83765a; font-size:5.7px;">(máx. 1×/rodada)</span>
      </label>
    </div>
    <div style="padding:5px 8px 5px; display:flex; flex-direction:column; gap:3px;">
      <div style="display:flex; align-items:baseline; gap:5px;">
        <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade I</span>
        <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
        <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
        <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
      </div>
      <div style="display:flex; align-items:baseline; gap:5px;">
        <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade II</span>
        <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
        <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
        <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
      </div>
      <div style="display:flex; align-items:baseline; gap:5px;">
        <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade III</span>
        <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
        <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
        <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
      </div>
      <div style="display:flex; align-items:baseline; gap:5px;">
        <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#7ec19e;">Crítico</span>
        <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
      </div>
    </div>
  </div>
</div>

Cada habilidade é registrada com:

- **Nome**
- **Descrição breve** — 1 frase evocativa, deixando claro o que a habilidade faz
- **Chave** — para habilidades de arma: "Arma - Grau" (ex: "Espada - Básica"). Para habilidades gerais de grupo: "Grupo - Subtipo" (ex: "Marcial - Especial")
- **Atributo** — atributo usado no teste (ex: ATA)
- **Efeitos / Alvos**
- **Intensidade I / II / III** — as três versões da habilidade, cada uma com seu custo em Pontos de Ação e Mana
- **Crítico** — dentro do [limiar de Crítico](../jogar/testes.md#criticos) (Sorte ÷ 3)

### Intensidade

Toda habilidade de ataque existe em **três Intensidades**. Elas não são compradas com escolhas de nível: estão todas disponíveis desde o momento em que o personagem aprende a habilidade. O que muda é quanto custa usar cada uma — o jogador decide **na hora de ativar**, conforme quanto do turno e do Mana quer investir.

| Intensidade | Pontos de Ação | O que ela entrega |
|---|---|---|
| I | ◈ (1) | O efeito base — normalmente só o dano |
| II | ◈◈ (2) | Acrescenta o efeito secundário (empurrar, Sangrando, Marcado) |
| III | ◈◈◈ (3) | O efeito completo (derrubar, Atordoado) — consome o turno inteiro |

O custo em Mana sobe junto com a Intensidade (ver [Escala de Mana por Intensidade](../jogar/mana.md#escala-de-mana-por-intensidade)).

!!! regra "Alcance e área nunca escalam com Intensidade"
    Uma habilidade que cobre 2 casas de raio cobre 2 casas de raio em qualquer Intensidade — o que a Intensidade compra é o efeito, não o tamanho.

### Habilidades de Custo Fixo

Algumas habilidades não têm Intensidade: trazem **Custo fixo** e um único resultado de **Acerto** na ficha. São os casos em que a força da habilidade já está em outro lugar:

- **Área de 3 casas de raio ou mais** — a área já é o poder; escalar o efeito por cima seria demais
- **Habilidades Supremas** — o custo em Mana (48+) já as coloca fora da escala
- **Efeitos sem nada pra graduar** — quando o efeito é absoluto, não há degrau acima dele. Uma Reação que **anula por completo** um ataque é o caso típico: não existe "anular mais"

O preço de uma habilidade de Custo fixo segue duas regras:

- **Mana:** o valor da Intensidade III da escala em que ela viveria (18-36 pra habilidades comuns; 48+ pra Supremas).
- **PA:** **◈◈◈**, como uma Intensidade III — com duas exceções: **Avançadas de arma** de área cobram **◈◈** (padrão consolidado do Equipamento: ◈◈ + 27 Mana), e **Reações dedicadas** cobram 0. Habilidades utilitárias fora de combate podem declarar PA menor na própria ficha.

!!! regra "Custo fixo não dispensa a rolagem"
    Habilidade de Custo fixo com alvo hostil **rola teste de ataque normalmente** contra o número-alvo do defensor. Só ficam sem rolagem os casos que a [Resolução](#resolucao) isenta: buffs, cura, e Supremas declaradas como inevitáveis.

### Buffs, Suporte e Mobilidade também têm Intensidade

Não ter teste de ataque **não** significa não ter Intensidade. O que escala num buff não é a chance de acertar — é o tamanho do efeito. Cada habilidade escala pelo eixo que faz sentido pra ela:

| Eixo | Quando se aplica | Exemplo |
|---|---|---|
| **Magnitude** | Há um valor que é a identidade do buff | Escudo Mágico: Escudo de 1d8 → 2d8 → 3d8 |
| **Duração** | O efeito é absoluto e não tem número pra crescer | Postura Inabalável: não pode ser derrubado por 2 → 3 → 4 rodadas |
| **Ambos** | Buff de grupo ou transformação, que tem valor *e* prazo | Bênção Divina: +1 → +2 → +3 de bônus, por 3 → 4 → 5 rodadas |

!!! regra "Habilidades dedicadas a Reação são a exceção parcial"
    Continuam custando **0 PA** sempre — essa é a rede de segurança que permite reagir mesmo tendo gastado o turno inteiro. Nelas a Intensidade escolhe apenas **quanto Mana** queimar no momento em que você é atacado.

Como o buff mantém na Intensidade I exatamente o efeito e o custo em Mana que sempre teve, subir de Intensidade é sempre ganho — nunca um pedágio pra ter o de antes.

### Habilidades com Tiers de Resultado

Um punhado de habilidades faz algo que **não deveria ser garantido só por pagar o custo** — trazer um aliado morto de volta é o caso central. Nessas, o d100 volta a graduar o resultado: a rolagem decide entre falha catastrófica, falha recuperável e sucesso.

| Total (d100 + Atributo) | Resultado |
|---|---|
| ≤ 50 | Falha total — a pior consequência possível |
| 51–80 | Falha, mas recuperável |
| 81–99 | Sucesso |
| 100 (ou dentro do limiar de Crítico) | Sucesso ampliado |

Essas habilidades têm **Custo fixo** (não têm Intensidade) e escrevem as faixas explicitamente na ficha. São deliberadamente raras — a graduação existe justamente pra impedir que um efeito dessa magnitude se torne confiável. Hoje [Ressuscitar](suporte.md) e [Selar o Pacto](conjuracao.md) usam esse formato.

### Habilidades Passivas

Nem toda habilidade se ativa. Uma **Passiva** é escolhida no nível como qualquer outra — ocupa a mesma escolha de progressão que uma habilidade ativa —, mas fica **sempre ligada** a partir do momento em que é aprendida, sem custar PA nem Mana.

A Ficha de uma Passiva é mais enxuta: **Nome** *(Passiva)*, descrição breve, **Chave**, um bullet **Custo: nenhum — Passiva, sempre ativa desde que aprendida**, e um bullet **Efeito** com o que ela faz. **Sem Intensidade** — é binária, você tem ou não tem; não escala.

!!! regra "Passiva compete com as ativas pela mesma escolha de nível"
    Não existe um slot separado pra Passivas — escolher uma é abrir mão de uma habilidade ativa naquele nível. É uma escolha real, não um bônus de graça.

### Resolução

1. O jogador declara a habilidade e **a Intensidade**, e paga o PA + Mana daquela Intensidade.
2. Rola **d100 + Atributo da habilidade**.
3. O total precisa **igualar ou superar o número-alvo do defensor** (ver [Defesa](../glossario.md#defesa)). Por padrão isso é a **Evasão** — habilidades que impõem outra coisa (efeito mental, veneno etc.) declaram qual número testar em vez disso, mas a lógica de comparação é sempre a mesma.
4. **Acertou** → aplica o efeito da Intensidade paga. **Não acertou** → nenhum efeito; o PA e o Mana foram gastos de todo jeito.
5. **Crítico**: se o d100 puro (o número antes de somar o Atributo) for igual ou menor que o [limiar de Crítico](../jogar/testes.md#criticos) (Sorte ÷ 3, arredondado), o teste é sucesso automático e **Crítico** — soma o dano máximo do dado + mais uma rolagem normal do mesmo dado, e **sobe 1 Intensidade de graça** — aplica o efeito da Intensidade acima da que foi paga, sem pagar a diferença. Usado já em Intensidade III (ou numa habilidade de Custo fixo), o Crítico entrega o bônus de dano — mais o efeito extra de Crítico que a própria ficha declarar, se houver.

!!! regra "Cada golpe, seu próprio teste"
    Quando uma habilidade atinge mais de uma criatura, ou golpeia o mesmo alvo mais de uma vez, cada golpe é o seu **próprio teste de ataque** — pode acertar uns e errar outros, e cada golpe crítica sozinho, pela regra normal de Sorte. Habilidades com alvos ou golpes demais pra isso fazer sentido na mesa (área grande, combo com muitos hits) já usam [Custo fixo](#habilidades-de-custo-fixo): uma rolagem só, porque a abrangência em si já é o efeito.

!!! dica "Variante pra agilizar"
    Se a mesa preferir menos rolagens, o Mestre pode declarar (ou os jogadores sugerirem) resolver com uma rolagem só pro grupo de golpes/alvos daquela habilidade, comparada ao número-alvo de cada um. É opção de ritmo, não o padrão do livro.

!!! regra "Deslocamento do usuário vale em toda Intensidade"
    Quando uma habilidade desloca o usuário (salto, investida, recuo), essa cláusula vale em **todas** as Intensidades, mesmo que o texto das linhas II/III não a repita — o deslocamento é a identidade da técnica, não um efeito comprado.

O d100 responde só "acertou ou não" — **quão forte** o golpe é já foi decidido no momento em que o jogador escolheu a Intensidade.

Habilidades sem teste de ataque (buffs, cura, efeitos automáticos como uma Habilidade Suprema inevitável) **não checam número-alvo** — o efeito simplesmente acontece. Mas isso não as isenta de Intensidade: elas ainda escolhem quanto investir, e o que cresce é o tamanho do efeito (ver acima).
