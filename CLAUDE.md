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

### Sistema de Armas
Cada arma concede acesso a 3 níveis de habilidade:
1. **Habilidade Básica**
2. **Habilidade Avançada**
3. **Habilidade Especial**

*(Detalhes de como essas habilidades funcionam por tipo de arma: a definir.)*

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

Usuário já desenhou um modelo em um caderno físico — foto pendente de envio. Não inventar estrutura de ficha até receber a referência.

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

Projeto recém-criado (2026-07-16). Estrutura inicial montada, aguardando:
1. Foto do modelo de ficha do usuário
2. Definição dos grupos de habilidade restantes
3. Conteúdo detalhado de cada grupo de habilidade
4. Lista de raças
5. Lista de pacotes
