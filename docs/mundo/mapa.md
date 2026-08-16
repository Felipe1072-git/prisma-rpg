# Mapa de Pania

Clique num ponto pra ver a descrição. Em Torirue, clique em "Ver mapa da cidade" pra
entrar no mapa da capital.

??? info "Como editar os pontos"
    Antes de editar, deixe rodando numa aba de terminal (esse comando já sobe o site
    localhost **e** o salvamento automático juntos — não precisa mais rodar o
    `mkdocs serve` por separado):

    ```
    python notas/mapa_servidor.py
    ```

    Clique em **✏️ Editar** (canto superior direito) pra ligar o modo de edição: clique em
    qualquer lugar do mapa pra criar um ponto novo, ou num ponto existente pra editá-lo —
    dá pra mudar nome, descrição, ícone (ou deixar em branco pro pino padrão) e se ele vira
    porta pra outro mapa. As edições ficam salvas neste navegador enquanto você trabalha.

    Clique em **💾 Salvar** pra gravar direto em `docs/assets/js/mapa-dados.js` — é isso
    que torna a edição definitiva e manda ela pro site publicado no próximo `git push`. Se
    o servidor local não estiver rodando, aparece um texto pra copiar na mão como plano B.
    O botão **↺** descarta as edições locais não salvas (por exemplo, pra recomeçar do que
    já está gravado no arquivo).

<div id="prisma-mapa" style="height: 75vh; border-radius: 8px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  iniciaMapaPrisma("prisma-mapa", "pania");
});
</script>

Mapas: Paulo Souza, feitos no Inkarnate.
