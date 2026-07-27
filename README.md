# Prisma RPG

**Um d20 de mesa sem classes, onde a força de um golpe é escolha do jogador — não resultado do dado.**

Sistema de RPG de mesa homebrew autoral, em português. Todas as habilidades do jogo estão disponíveis para qualquer personagem desde o nível 1: não existe "lista de magias do mago" nem "manobras do guerreiro". Um espadachim que aprendeu a conjurar fogo é tão válido quanto um mago puro.

## A ideia central: Intensidade

Em quase todo d20, você rola e o dado decide o quanto o golpe fez. Aqui não.

Toda habilidade existe em **três Intensidades**, e você escolhe qual pagar **antes de rolar**:

| Intensidade | Custa | Entrega |
|---|---|---|
| **I** | ◈ | o efeito base |
| **II** | ◈◈ | acrescenta o efeito secundário |
| **III** | ◈◈◈ | o efeito completo — consome o turno inteiro |

O d20 só responde *"acertou ou não"*. E como cada personagem tem **3 Pontos de Ação (◈)** por turno, a pergunta é sempre a mesma: **um golpe grande, ou três pequenos?**

```
Corte Duplo, com uma Espada (1d8):

Intensidade I   — ◈   + 1 Mana:  1d8 + empurra 1 casa
Intensidade II  — ◈◈  + 3 Mana:  1d8 + derruba o alvo
Intensidade III — ◈◈◈ + 6 Mana:  1d8 + derruba, e o alvo perde a próxima Reação
```

Três golpes em Intensidade I somam mais dano que um em Intensidade III. A Intensidade III não existe para maximizar dano — existe para **controlar**.

## O que tem aqui

| | |
|---|---|
| **574** habilidades | marciais, mágicas por elemento, sociais, infiltração, mobilidade, buff, debuff, suporte |
| **62** armas | cada uma com 3 habilidades próprias (186 no total), tipo de dano e preço |
| **25** raças | todas com traço físico inconfundível — nenhuma é "humano com poderes" |
| **100** pacotes | kits de arquétipo prontos; sugestão, nunca obrigação |
| **11** elementos | cada um com assinatura mecânica própria: Fogo consome, Gelo trava, Sombras nega terreno |
| **Livro do Mestre** | bestiário, montagem de encontro, tabelas de dificuldade, recompensas e exploração |

## Por onde começar

- **Vai jogar?** [Introdução](docs/jogador/introducao.md) — explica um turno inteiro com números reais e o caminho até a sua primeira rolagem.
- **Vai mestrar?** [Livro do Mestre](docs/mestre/index.md) — criaturas prontas, como montar um encontro que não mata o grupo por acidente, e o que pedir num teste.
- **Quer só olhar as regras?** [O Sistema d20](docs/jogador/sistema-d20.md).

## Rodando o site localmente

O conteúdo canônico vive em [`docs/`](docs/index.md) e é publicado como site com [MkDocs](https://www.mkdocs.org/) + tema Material:

```bash
pip install mkdocs-material
mkdocs serve
```

Depois abra `http://localhost:8000`.

## Estado do projeto

**Versão 0.2** — jogável de ponta a ponta: regras completas, o conteúdo listado acima e um Livro do Mestre em cinco partes.

**Nada foi testado em mesa ainda.** Todo o equilíbrio foi validado por cálculo — dano médio por Intensidade, Vida por Tier de criatura, letalidade de encontro, duração de combate. Isso pega desequilíbrio de escala, mas não pega problema de ritmo e de legibilidade, que só aparece jogando. Se você rodar uma sessão, relatos são bem-vindos.

## Inspirações

Mushoku Tensei, Sword Art Online, Fabula Ultima, Skyrim, Dragon Age, The Witcher, Diablo, Warcraft, animes em geral e Grand Chase — em tom e sensação. O mundo é próprio, não é nenhuma dessas franquias.

## Licença

Sistema autoral de **Paulo Souza**, licenciado sob [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br).

**Você pode**, sem pedir permissão:

- usar em mesa, do jeito que quiser
- copiar, imprimir e distribuir
- adaptar, remixar e criar material derivado — inclusive para fins comerciais

**A única condição** é dar crédito: mencione Paulo Souza como autor do Prisma RPG, com link para este repositório, e indique se você fez mudanças.

O texto legal completo está em [`LICENSE`](LICENSE).
