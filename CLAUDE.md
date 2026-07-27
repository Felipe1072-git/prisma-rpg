# CLAUDE.md

Este arquivo orienta o Claude Code ao trabalhar neste projeto.

## Sobre o Projeto

**Prisma RPG** — sistema de RPG de mesa homebrew autoral, criado por Paulo Souza. É o "D&D definitivo" do autor: um d20 tradicional simplificado, sem classes, focado em liberdade total de construção de personagem.

- **Nome do sistema:** Prisma RPG (nome de trabalho — pode mudar)
- **Versão atual:** 0.1 (Rascunho inicial)
- **Pasta do projeto:** `C:\Users\Paulo Souza\Documents\Sistema RPG\`
- **Repositório:** local por enquanto (sem remoto/GitHub ainda)

### Inspirações de ambientação/tom

Mushoku Tensei, Sword Art Online, Fabula Ultima, Skyrim, Dragon Age, The Witcher, Diablo, Warcraft, animes em geral, Grand Chase. Mundo autoral — não é nenhuma dessas franquias, é uma fusão de tom e sensação.

## Decisões de Design Consolidadas

Estas são decisões **já tomadas pelo usuário** — não são sugestões, são a base do sistema.

### Sistema Base
- **d20 tradicional**, simplificado.
- **Sem sistema de classes.** Todas as habilidades do jogo estão disponíveis para todos os personagens — quem quiser ser "full mago" pode, quem quiser misturar, mistura. Sem restrições artificiais.
- **Sistema de habilidades**: personagem ganha/escolhe habilidades por nível.
- **Magia e habilidades são a mesma coisa** — não existe um sistema de magia separado. Tudo funciona pela mesma estrutura de habilidades.
- **Tudo baseado em Mana** — o recurso universal para ativar habilidades.
- **Pontos de Ação (◈)** mantidos como no sistema anterior (Diablo RPG).

### Intensidade (I / II / III)

**Não existem "Tiers de Sucesso".** Foram removidos em 2026-07-26 pra simplificar o jogo. O d20 responde só "acertou ou não" (d20 + Atributo vs Defesa); **quão forte** o golpe é já foi decidido pelo jogador ao escolher a Intensidade no momento de ativar:

| Intensidade | PA | Entrega |
|---|---|---|
| I | ◈ (1) | efeito base — normalmente só o dano |
| II | ◈◈ (2) | + efeito secundário (empurrar, Sangrando, Marcado) |
| III | ◈◈◈ (3) | efeito completo (derrubar, Atordoado) |

- O Mana sobe junto com a Intensidade (ver `docs/jogador/mana.md`).
- **Alcance e área nunca escalam** — só o efeito.
- **Crítico (20 natural):** dano máximo + rolagem extra, e **sobe 1 Intensidade de graça**.
- **Custo fixo** (sem Intensidade): áreas de raio 3+, Supremas, buffs sem rolagem.
- **Tiers de Resultado:** exceção rara pra efeitos que não devem ser confiáveis — o d20 gradua falha total / falha recuperável / sucesso. Só `Ressuscitar` usa.

### Sistema de Armas
Cada arma concede acesso a 3 habilidades, em ordem de aprendizado obrigatória:
1. **Habilidade Básica**
2. **Habilidade Avançada**
3. **Habilidade Especial**

O grau **não** define o custo — cada uma tem suas 3 Intensidades. O grau define o quanto a técnica entrega e o custo em Mana: Básica 1/3/6, Avançada 2/5/9, Especial 3/7/12.

### Grupos de Habilidades

Habilidades são organizadas por grupos temáticos (não por classe):

| Grupo | Escopo |
|---|---|
| Habilidades Marciais | Armas corpo a corpo / combate a curta distância |
| Habilidades de Pontaria | Armas à distância e precisão (inclui feitiços de precisão) |
| Habilidades Mágicas Básicas | Uso básico de magia |
| Habilidades Mágicas por Elemento | Fogo, Gelo, Terra, Sombras, Luz, etc. |
| Habilidades Sociais | Persuasão e afins |
| Habilidades de Infiltração | Furtividade, ladinagem |
| Habilidades de Mobilidade | Voo, deslocamento |
| Habilidades de Buff | Incremento de força, imbuir elementos em armas, etc. |
| Habilidades de Debuff | Desvantagens para inimigos ou em testes |

*(Lista pode crescer — usuário sinalizou que ainda vai pensar em mais grupos.)*

### Pacotes

"Pacotes" são kits/sugestões (mais do que meros kits) de Armas + Habilidades para jogar dentro de um arquétipo, inspirados em **Grand Chase**. Importante: **não são classes** — são só um ponto de partida sugerido. Nada impede montar um personagem fora de qualquer pacote.

### Raças

Variadas, no estilo **Daggerheart** e animes em geral. *(Lista de raças: a definir.)*

### Ficha de Personagem

**A foto do modelo do caderno foi descartada** (decisão de 2026-07-26) — a ficha será construída do zero. O método pedido pelo usuário: **pensar elemento por elemento**, um campo de cada vez, discutindo *o que* precisa estar lá e *por quê*, antes de desenhar qualquer layout. Não montar uma ficha inteira de uma vez e apresentar pronta.

## Criação de Conteúdo — REGRAS DE TRABALHO

- **É estritamente proibido inventar regras, mecânicas, nomes, habilidades, raças ou qualquer conteúdo de jogo sem consultar o usuário primeiro.**
- Sempre apresentar a ideia/sugestão e aguardar aprovação explícita antes de escrever em qualquer documento canônico (`docs/`).
- Pode agir de forma criativa nas *sugestões*, mas a decisão final é sempre do usuário.
- Nunca assumir que algo "faz sentido" mecanicamente sem confirmar.
- Sempre usar pop-ups de escolha (AskUserQuestion) para perguntas de sim/não ou múltipla escolha.
- Mostrar diff/preview antes de gravar alterações de conteúdo já existente.

## Estrutura de Arquivos

```
Sistema RPG/
├── docs/                    ← fonte canônica (vai virar site MkDocs)
│   ├── index.md
│   ├── jogador/             ← regras principais (d20, mana, pontos de ação, armas)
│   ├── habilidades/         ← grupos de habilidades
│   ├── pacotes/             ← "pacotes" estilo Grand Chase
│   ├── racas/                ← raças jogáveis
│   ├── mestre/               ← regras/ferramentas do mestre (futuro)
│   └── assets/                ← CSS, JS, imagens
├── notas/                    ← rascunhos e ideias soltas (não publicado)
└── referencia/                ← material de referência pessoal (não publicado)
```

## Convenções de Commit

- `feat:` nova regra, habilidade, pacote ou mecânica
- `fix:` correção de erro ou inconsistência
- `docs:` atualização de texto, revisão ou reorganização
- `refactor:` reorganização sem mudança de conteúdo

## Status

**Versão 0.2 (2026-07-26) — sistema jogável de ponta a ponta.** Publicado em
[felipe1072-git.github.io/prisma-rpg](https://felipe1072-git.github.io/prisma-rpg/), sob CC BY 4.0,
com deploy automático a cada push (workflow em `.github/workflows/deploy.yml`).

O que existe: 574 habilidades nos 9 grupos, 62 armas com 3 habilidades cada, 25 raças, 100 pacotes,
11 elementos com assinatura mecânica própria, sistema Tocado, e Livro do Mestre em 5 partes
(Bestiário, Encontros, Testes, Recompensas, Exploração).

**Nada foi testado em mesa.** Todo o equilíbrio veio de cálculo. Relato de jogo real vale mais que
qualquer simulação minha.

Em aberto:
1. **Ficha de personagem imprimível** — a construir do zero, elemento por elemento (ver acima)
2. **Dano dos PJs escala pouco** (2,7x contra 7,6x da Vida) — problema conhecido, adiado de
   propósito porque a correção mexeria nas 419 habilidades. Só reabrir se ele trouxer
3. Conteúdo novo é sempre bem-vindo, mas nenhuma lacuna estrutural de regra permanece
