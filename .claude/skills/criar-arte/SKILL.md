---
name: criar-arte
description: Gera prompts de imagem pro Gemini (ou outro gerador de IA) pra criar artes visuais do Prisma RPG — capa e lombada do fichário, contracapa, fichas ilustradas de personagem, artes de campanha, logos, etc. — mantendo o estilo visual e as regras de composição já fixados numa sessão de design extensa (pintura pesada tipo capa de D&D, paleta por arquétipo, composição em colagem). Use sempre que o usuário pedir uma arte nova, um prompt de imagem, mencionar "pedir pro Gemini fazer...", "gerar uma arte de...", "fazer uma ilustração/logo pra...", ou pedir ajuda pra montar/imprimir uma peça visual do fichário.
---

# Criar Arte — Prisma RPG

Esta skill existe porque o estilo visual do Prisma RPG (capa e lombada do fichário) foi fixado com bastante iteração numa sessão de design — várias tentativas erradas (pose de tela de seleção de personagem, arma flutuante, texto embaçado, cópia demais de uma franquia de referência) até chegar num resultado aprovado. É fácil perder essa consistência gerando peças novas do zero sem revisar o que já funcionou.

**Fonte viva:** [referencia/estilo-visual-ia.md](../../referencia/estilo-visual-ia.md) — sempre releia antes de montar um prompt novo. É lá que moram a técnica de pintura, a paleta por arquétipo, as regras de composição, os bugs conhecidos e os prompts já aprovados como referência de partida.

## O processo

1. **Descubra o que está sendo pedido:** que peça (capa, lombada, contracapa, ficha de personagem, logo, arte de campanha...), quais dimensões físicas (se for pra impressão), e que conteúdo específico precisa aparecer.
2. **Pergunte o que não for óbvio** com `AskUserQuestion` antes de montar o prompt — medida física exata, se tem elemento novo que ainda não está no guia de estilo, se o pedido menciona uma franquia/obra específica (nesse caso, redirecione pra usar só como referência de cor/mood — ver seção de bugs conhecidos no guia — nunca copiar design 1:1).
3. **Monte o prompt puxando as regras fixas** do guia de estilo (técnica de pintura, paleta, composição, bugs conhecidos a evitar). Não reinvente a técnica/paleta do zero a cada pedido.
4. **Lembre o usuário de anexar a arte aprovada mais recente** como referência visual junto do prompt no chat do Gemini, e de preferir continuar a mesma conversa em vez de abrir um chat novo — isso é o que mais garante consistência entre peças.
5. **Mostre o prompt pronto no chat** para o usuário copiar e colar. Esta skill nunca gera ou envia a imagem sozinha — só entrega o texto do prompt pronto.
6. **Depois que o usuário aprovar o resultado**, ofereça atualizar `referencia/estilo-visual-ia.md` com a peça nova como exemplo de referência, mantendo o guia vivo e crescendo.

## Checklist antes de entregar o prompt

- [ ] Técnica de pintura e paleta por arquétipo vêm do guia de estilo, não inventadas na hora
- [ ] Composição pede ação de verdade / colagem assimétrica, não fileira posada
- [ ] Reforça "uma única arma por personagem" se houver combate corpo a corpo
- [ ] Sem pedido de texto/logo na cena principal (a menos que seja um logotipo isolado — nesse caso, avisar sobre o risco de letra errada)
- [ ] Dimensões físicas exatas, se for peça impressa
- [ ] Lembrete pro usuário anexar a arte de referência aprovada + continuar a mesma conversa
