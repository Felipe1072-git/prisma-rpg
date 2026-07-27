# Prompt — Auditoria de Consistência (para sessão com Claude Fable 5)

Uso: abrir conversa nova, selecionar **Fable 5**, thinking em **alto**, colar o bloco abaixo
como primeira e única mensagem. Não vá adicionando contexto aos poucos — Fable rende mais
com a tarefa inteira especificada de uma vez.

---

Quero uma auditoria de consistência do Prisma RPG inteiro.

**Por que isso importa agora.** Este sistema foi escrito ao longo de meses, habilidade por
habilidade, e nunca foi lido de uma vez como um corpo único. Hoje são 574 habilidades em 10
grupos, 62 armas com 3 habilidades cada (186), 25 raças, 100 pacotes, 11 elementos com
assinatura mecânica própria e um Livro do Mestre em 5 partes — 11.318 linhas em 28 arquivos
sob `docs/`. Nada disso foi testado em mesa: todo o equilíbrio veio de cálculo meu, sozinho.
O risco real não é uma habilidade forte demais — é uma regra que contradiz outra a 3.000
linhas de distância e que só vai aparecer quando um jogador tentar a combinação na mesa, com
a sessão travada esperando uma resposta que o livro não dá.

Leia o `CLAUDE.md` do projeto primeiro: ele traz o sistema base, a estrutura da Intensidade
I/II/III, a tabela de custos por grau e as decisões de design já consolidadas. Elas são
premissa, não sugestão — um achado não pode ser "eu faria diferente".

**O que quero de você:** os pontos onde o sistema se contradiz, se define mal, ou deixa uma
pergunta de mesa sem resposta. O que caracteriza um achado válido:

- **Contradição direta** — duas regras que não podem valer ao mesmo tempo. Um traço racial que
  viola uma regra geral, uma condição definida de um jeito no glossário e usada de outro numa
  habilidade, um pacote que sugere uma combinação que outra regra proíbe.
- **Interação indefinida** — duas coisas que vão se encontrar em mesa e cujo resultado o texto
  não determina. Duas condições sobrepostas, um efeito de área contra um alvo que já está sob
  outro efeito, uma Reação disparando dentro de uma habilidade de duração.
- **Preço incoerente** — duas habilidades que entregam essencialmente o mesmo por custos
  diferentes em PA ou Mana, sem que a diferença de grau ou grupo justifique.
- **Escala quebrada** — algo cuja progressão se descola do resto do sistema ao longo dos 20
  níveis.

Não me traga preferência estética, sugestão de conteúdo novo, ou "poderia ser mais claro".
Traga o que está errado ou indefinido.

**Cobertura antes de filtro.** Reporte tudo que encontrar, incluindo o que você considera menor
ou está incerto — marque cada achado com severidade e o seu nível de confiança, e eu filtro
depois. Prefiro descartar um achado a nunca ver um problema real porque você o julgou pequeno.
Para cada um: onde está (arquivo e linha), o que colide com o quê, e o que acontece na mesa
quando um jogador tenta.

**O que você pode e não pode fazer.** Você pode ler tudo, calcular, e escrever o relatório em
`notas/auditoria.md`. Pode aplicar correções em **no máximo 15 habilidades** como amostra, para
eu ver o efeito na prática — escolha as que melhor demonstrem cada tipo de problema. Fora dessa
amostra, **não edite nada em `docs/`**: eu quero aprovar o resto antes. Não faça commit.

**Delegue.** A auditoria é naturalmente paralelizável por grupo de habilidade, por elemento, por
família de arma. Use subagentes para varrer em paralelo e siga trabalhando enquanto eles rodam;
intervenha se algum sair do rumo ou estiver sem o contexto necessário. Consolide você mesmo — a
comparação entre grupos é onde as contradições reais aparecem.

**Anote o que aprender.** Mantenha `notas/auditoria-notas.md` com o que você for descobrindo
sobre como o sistema se encaixa: uma lição por bloco, com uma linha de resumo no topo. Registre
tanto o que quebrou quanto o que se confirmou sólido, e por quê. Não anote o que os arquivos já
dizem — anote o que só se enxerga cruzando eles.

**Antes de afirmar progresso, confira cada afirmação contra um resultado de ferramenta desta
sessão.** Só relate o que você pode apontar evidência; se algo ainda não foi verificado, diga
isso explicitamente. Se um cálculo não fechou, mostre os números.

**Como escrever pra mim.** Escreva o relatório para quem não acompanhou seu trabalho. Abra com o
resultado — quantos achados, de que tipos, e qual é o pior. Depois o detalhe. Frases completas,
termos por extenso, sem taquigrafia de setas nem rótulos que você inventou no meio do caminho.
Legível importa mais que curto: corte o que não muda o que eu vou fazer, não comprima a escrita.
Responda em português.
