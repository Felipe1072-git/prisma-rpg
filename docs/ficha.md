# Ficha de Personagem

<p class="prg-ficha__intro">
Três páginas: a ficha principal, um apêndice de Habilidades, e uma folha de consulta rápida de Estados. Imprima em A4 — ou abra o menu de impressão do navegador (<code>Ctrl+P</code> / <code>Cmd+P</code>) e salve como PDF. O apêndice de Habilidades é feito pra imprimir quantas cópias precisar — você ganha habilidades novas ao longo da campanha, não só as 10 do início.
</p>

<div class="prg-ficha__acoes">
  <button class="prg-ficha__botao" onclick="window.print()">Imprimir / Salvar como PDF</button>
</div>

<div class="prg-ficha">

<!-- ============================================================ PÁGINA 1 -->
<section class="prg-ficha__pagina">

  <header class="prg-ficha__cabecalho">
    <span class="prg-ficha__titulo">Prisma RPG — Ficha de Personagem</span>
    <span class="prg-ficha__pagina-label">1 / 3 — Personagem</span>
  </header>

  <div class="prg-linha">
    <label class="prg-campo prg-campo--grande">
      <span class="prg-campo__rotulo">Nome do Personagem</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Jogador</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Raça</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo prg-campo--pequeno">
      <span class="prg-campo__rotulo">Nível</span>
      <span class="prg-campo__valor"></span>
    </label>
  </div>

  <div class="prg-linha">
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Origem — Passado</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Origem — Ambiente</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Origem — Evento Formador</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Pacote</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Tocado (se houver)</span>
      <span class="prg-campo__valor"></span>
    </label>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Os Oito Atributos</p>
    <div class="prg-atributos">
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">FOR</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">VIT</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">AGI</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">INT</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">SAB</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">VON</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">SOR</div></div>
      <div class="prg-atributo"><div class="prg-atributo__valor"></div><div class="prg-atributo__nome">SAN</div></div>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Recursos</p>
    <div class="prg-linha">
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Vida</div>
        <div class="prg-recurso__valores">
          <span class="prg-recurso__caixa"></span><span class="prg-recurso__separador">/</span><span class="prg-recurso__caixa"></span>
        </div>
        <div class="prg-recurso__legenda">Atual / Total</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Mana</div>
        <div class="prg-recurso__valores">
          <span class="prg-recurso__caixa"></span><span class="prg-recurso__separador">/</span><span class="prg-recurso__caixa"></span>
        </div>
        <div class="prg-recurso__legenda">Atual / Total</div>
        <div class="prg-recurso__formula">10 + Nível×3 + Vontade×2 + equip.</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Estresse</div>
        <div class="prg-recurso__valores">
          <span class="prg-recurso__caixa"></span><span class="prg-recurso__separador">/</span><span class="prg-recurso__caixa"></span>
        </div>
        <div class="prg-recurso__legenda">Atual / Máximo</div>
        <div class="prg-recurso__formula">10 + Sanidade</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Dados de Vida</div>
        <div class="prg-recurso__valores">
          <span class="prg-recurso__caixa"></span><span class="prg-recurso__separador">/</span><span class="prg-recurso__caixa"></span>
        </div>
        <div class="prg-recurso__legenda">Restantes / Total</div>
        <div class="prg-recurso__formula">tamanho do dado (d4–d12): ____</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Pontos de Ação</div>
        <div class="prg-pa">
          <span class="prg-pa__ponto"></span><span class="prg-pa__ponto"></span><span class="prg-pa__ponto"></span>
        </div>
        <div class="prg-recurso__legenda">marque o gasto no turno</div>
      </div>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Defesas &amp; Combate</p>
    <div class="prg-linha">
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Defesa Física</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">8 + Agilidade + Armadura + Escudo</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Defesa Mental</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">8 + Vontade</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Outra Defesa</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">8 + ______ (Vitalidade/Sabedoria/Sanidade)</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Iniciativa</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">d20 + Agilidade + Sorte</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Movimento</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">6 + Agilidade (casas)</div>
      </div>
      <div class="prg-recurso">
        <div class="prg-recurso__nome">Rerolagens</div>
        <div class="prg-recurso__valores"><span class="prg-recurso__caixa"></span></div>
        <div class="prg-recurso__formula">1 + Sorte, por descanso longo</div>
      </div>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Traços</p>
    <div class="prg-linha">
      <div style="flex: 1.2">
        <p class="prg-campo__rotulo">Traços Raciais</p>
        <ul class="prg-lista">
          <li></li><li></li><li></li>
        </ul>
      </div>
      <div style="flex: 1.2">
        <p class="prg-campo__rotulo">Traços de Origem (Passado / Ambiente / Evento)</p>
        <ul class="prg-lista">
          <li></li><li></li><li></li>
        </ul>
      </div>
      <div style="flex: 1">
        <p class="prg-campo__rotulo">Traço Passivo de Tocado (se houver)</p>
        <ul class="prg-lista">
          <li></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Equipamento</p>
    <table class="prg-tabela">
      <thead>
        <tr><th>Arma</th><th>Dano</th><th>Tipo</th><th>Propriedades</th><th>Requisito</th><th>Material</th></tr>
      </thead>
      <tbody>
        <tr><td class="prg-vazia"></td><td class="prg-vazia"></td><td class="prg-vazia"></td><td class="prg-vazia"></td><td class="prg-vazia"></td><td class="prg-vazia"></td></tr>
      </tbody>
    </table>
    <div class="prg-linha" style="margin-top: 1.5mm">
      <label class="prg-campo">
        <span class="prg-campo__rotulo">Armadura</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo prg-campo--pequeno">
        <span class="prg-campo__rotulo">Bônus Def.</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo">
        <span class="prg-campo__rotulo">Traço da Armadura</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo">
        <span class="prg-campo__rotulo">Escudo</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo prg-campo--pequeno">
        <span class="prg-campo__rotulo">Bônus Def.</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo prg-campo--pequeno">
        <span class="prg-campo__rotulo">Cobre</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo prg-campo--pequeno">
        <span class="prg-campo__rotulo">Prata</span>
        <span class="prg-campo__valor"></span>
      </label>
      <label class="prg-campo prg-campo--pequeno">
        <span class="prg-campo__rotulo">Ouro</span>
        <span class="prg-campo__valor"></span>
      </label>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Habilidades</p>
    <p class="prg-secao__nota">Habilidade de Custo fixo (sem Intensidade — ex: <em>Solo Consagrado</em>)? Escreva o custo (◈ + Mana) e o efeito inteiro na linha "Intensidade I" e deixe II e III em branco.</p>
    <div class="prg-hab-lista">
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
    </div>
  </div>

  <div class="prg-preenchimento" style="min-height: 2mm;"></div>
  <footer class="prg-ficha__rodape">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</footer>

</section>

<!-- ============================================================ PÁGINA 2 -->
<section class="prg-ficha__pagina">

  <header class="prg-ficha__cabecalho">
    <span class="prg-ficha__titulo">Prisma RPG — Apêndice de Habilidades</span>
    <span class="prg-ficha__pagina-label">2 / 3 — Habilidades</span>
  </header>

  <p class="prg-ficha__intro" style="margin: 0 0 2mm; text-align: left; max-width: none;">Imprima esta página quantas vezes precisar — cada cópia guarda mais Habilidades conforme você ganha ao longo da campanha.</p>

  <div class="prg-linha">
    <label class="prg-campo">
      <span class="prg-campo__rotulo">Nome do Personagem</span>
      <span class="prg-campo__valor"></span>
    </label>
    <label class="prg-campo prg-campo--pequeno">
      <span class="prg-campo__rotulo">Nível</span>
      <span class="prg-campo__valor"></span>
    </label>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Habilidades</p>
    <p class="prg-secao__nota">Habilidade de Custo fixo (sem Intensidade — ex: <em>Solo Consagrado</em>)? Escreva o custo (◈ + Mana) e o efeito inteiro na linha "Intensidade I" e deixe II e III em branco.</p>
    <div class="prg-hab-lista">
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
      <div class="prg-hab-card">
        <div class="prg-hab-card__cabecalho">
          <label class="prg-campo prg-campo--grande"><span class="prg-campo__rotulo">Nome</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Chave</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Atributo</span><span class="prg-campo__valor"></span></label>
          <label class="prg-campo"><span class="prg-campo__rotulo">Alvo / Alcance</span><span class="prg-campo__valor"></span></label>
        </div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade I</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade II</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Intensidade III</span><span class="prg-hab-card__valor"></span></div>
        <div class="prg-hab-card__linha"><span class="prg-hab-card__rotulo">Crítico</span><span class="prg-hab-card__valor"></span></div>
      </div>
    </div>
  </div>

  <div class="prg-preenchimento" style="min-height: 9mm;"></div>
  <footer class="prg-ficha__rodape">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</footer>

</section>

<!-- ============================================================ PÁGINA 3 -->
<section class="prg-ficha__pagina">

  <header class="prg-ficha__cabecalho">
    <span class="prg-ficha__titulo">Prisma RPG — Consulta Rápida</span>
    <span class="prg-ficha__pagina-label">3 / 3 — Estados &amp; Notas</span>
  </header>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Condições</p>
    <div class="prg-condicoes">
      <div class="prg-condicao"><span class="prg-condicao__nome">Sangrando</span> — perde 1d4 de Vida no início do próximo turno. Não acumula (vale o maior).</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Queimando</span> — perde 1d4 ao pegar fogo + 1d4 no início de cada turno. Apaga com Ação Básica, água, ou fim da cena.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Lento</span> — Movimento reduzido à metade.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Imóvel</span> — Movimento 0, mas age normalmente (Ações, Habilidades, Reações).</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Atordoado</span> — não pode agir, mover nem reagir.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Possuído</span> — outra criatura controla o corpo. d20 + Vontade vs Defesa mental do possuidor pra expulsar.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Petrificado</span> — 3 graus: Lento → Imóvel → pedra (imóvel + Resistência física). Cura Vida remove 1 grau.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Derrubado</span> — Movimento 0; ataques corpo a corpo contra ele têm Vantagem. Levantar custa ◈.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Desprevenido</span> — não pode agir nem reagir na 1ª rodada do combate.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Agarrado</span> — fica Imóvel. Escapar custa ◈ + teste de Força ou Agilidade vs Defesa física de quem prende.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Marcado</span> — o próximo ataque de um aliado contra ele nesta rodada tem Vantagem.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Envenenado</span> — acumula até 3; perde Xd4 de Vida por turno. Cura remove tudo de uma vez.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Escudo</span> — pontos temporários que absorvem dano antes da Vida. Não acumula (vale o maior).</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Exausto</span> — 3 graus: Desvantagem → +Lento → inconsciente. Remove 1 grau por descanso longo (com a causa resolvida).</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Risco</span> — se algum dado de dano cair em 1, o usuário sofre o preço descrito na própria habilidade.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Caído (0 de Vida)</span> — inconsciente. D20 vs DC 10 no início do turno; falha piora, até o limite da Vitalidade. Estabiliza com Ação Básica de um aliado.</div>
    </div>
  </div>

  <div class="prg-secao">
    <p class="prg-secao__titulo">Termos de Resolução</p>
    <div class="prg-condicoes">
      <div class="prg-condicao"><span class="prg-condicao__nome">Vantagem</span> — role 2d20, use o melhor.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Desvantagem</span> — role 2d20, use o pior. Vantagem + Desvantagem juntas se cancelam.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Acúmulo de bônus</span> — bônus planos de buffs diferentes não somam; vale o maior. Resistências ao mesmo tipo também não somam.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Terreno Difícil</span> — cada casa custa o dobro de Movimento.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Tipos de Dano</span> — Cortante, Perfurante, Impacto (da arma); Arcano (focos mágicos); e cada elemento causa o próprio tipo.</div>
      <div class="prg-condicao"><span class="prg-condicao__nome">Resistência / Imunidade / Vulnerabilidade</span> — dano do tipo cai pela metade / é ignorado / dobra. Aplicadas depois de tudo, inclusive Crítico.</div>
    </div>
  </div>

  <div class="prg-linha">
    <div class="prg-secao" style="flex: 1">
      <p class="prg-secao__titulo">Cicatrizes</p>
      <ul class="prg-lista">
        <li></li><li></li><li></li>
      </ul>
    </div>
    <div class="prg-secao" style="flex: 1">
      <p class="prg-secao__titulo">Vício</p>
      <ul class="prg-lista">
        <li></li>
      </ul>
    </div>
  </div>

  <div class="prg-secao prg-secao--flex1" style="display: flex; flex-direction: column;">
    <p class="prg-secao__titulo">Notas &amp; Backstory</p>
    <div class="prg-notas"></div>
  </div>

  <footer class="prg-ficha__rodape">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</footer>

</section>

</div>
