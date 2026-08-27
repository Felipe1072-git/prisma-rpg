// Mapa interativo de Pania (protótipo). Usa Leaflet em modo "imagem" (CRS.Simple):
// em vez de latitude/longitude, as coordenadas são pixels da própria imagem do mapa.
//
// Os dados dos pontos moram em mapa-dados.js (carregado antes deste arquivo,
// declara `var NIVEIS` global) — esse arquivo aqui é só o motor: desenha o
// mapa, os pontos, e o modo de edição.
//
// Pontos são escritos em coordenada de imagem normal (x a partir da esquerda,
// y a partir do topo, como num editor de imagem) e convertidos pra o sistema
// de baixo-pra-cima do Leaflet por `pontoImagem`.

(function () {
  function baseDosAssets() {
    var scripts = document.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].getAttribute("src") || "";
      var m = src.match(/^(.*)assets\/js\/mapa\.js(\?.*)?$/);
      if (m) return m[1];
    }
    return "";
  }

  var BASE = baseDosAssets();
  var CHAVE_LOCAL = "prisma-mapa-edicoes-v1";

  var ICONES_RAPIDOS = [
    { emoji: "📍", rotulo: "Pino padrão" },
    { emoji: "🏰", rotulo: "Capital / castelo" },
    { emoji: "⚔️", rotulo: "Batalha / guarnição" },
    { emoji: "🏠", rotulo: "Vila / bairro" },
    { emoji: "⚓", rotulo: "Porto" },
    { emoji: "⛪", rotulo: "Templo" },
    { emoji: "🎪", rotulo: "Arena / evento" },
    { emoji: "🏪", rotulo: "Mercado" },
    { emoji: "🌲", rotulo: "Natureza" },
    { emoji: "🗻", rotulo: "Montanha" },
    { emoji: "💀", rotulo: "Perigo / masmorra" }
  ];

  function pontoImagem(altura, x, y) {
    return [altura - y, x];
  }

  function imagemDoPonto(altura, latlng) {
    return { x: Math.round(latlng.lng), y: Math.round(altura - latlng.lat) };
  }

  function escapeHtml(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function carregaEdicoesLocais() {
    try {
      var salvo = localStorage.getItem(CHAVE_LOCAL);
      return salvo ? JSON.parse(salvo) : null;
    } catch (e) { return null; }
  }

  function salvaEdicoesLocais(niveis) {
    try { localStorage.setItem(CHAVE_LOCAL, JSON.stringify(niveis)); } catch (e) { /* ignora */ }
  }

  function criaIcone(ponto) {
    if (!ponto.icone) return new L.Icon.Default();
    return L.divIcon({
      className: "prisma-mapa-pin-emoji-wrap",
      html: '<div class="prisma-mapa-pin-emoji">' + escapeHtml(ponto.icone) + "</div>",
      iconSize: [30, 30],
      iconAnchor: [15, 28],
      popupAnchor: [0, -26]
    });
  }

  function iniciaMapaPrisma(containerId, nivelInicial) {
    var container = document.getElementById(containerId);
    if (!container || typeof L === "undefined") return;

    var dadosArquivo = window.NIVEIS || {};
    var NIVEIS = carregaEdicoesLocais() || dadosArquivo;

    var mapa = L.map(containerId, {
      crs: L.CRS.Simple,
      zoomSnap: 0.1,
      minZoom: -6,
      maxZoom: 4,
      attributionControl: false
    });

    var camadaAtual = null;
    var marcadoresAtuais = [];
    var nivelAtual = null;
    var nivelAtualChave = null;
    var editando = false;

    // ---------------------------------------------------------- controles

    var controleVoltar = L.control({ position: "topleft" });
    controleVoltar.onAdd = function () {
      var div = L.DomUtil.create("div", "prisma-mapa-voltar leaflet-bar");
      L.DomEvent.disableClickPropagation(div);
      div.style.display = "none";
      var btn = L.DomUtil.create("a", "", div);
      btn.href = "#";
      btn.title = "Voltar";
      btn.innerHTML = "‹ Voltar";
      btn.style.width = "auto";
      btn.style.padding = "0 10px";
      L.DomEvent.on(btn, "click", function (e) {
        L.DomEvent.preventDefault(e);
        if (nivelAtual && nivelAtual.voltarPara) carregaNivel(nivelAtual.voltarPara);
      });
      this._div = div;
      return div;
    };
    controleVoltar.addTo(mapa);

    var controleCoord = L.control({ position: "bottomleft" });
    controleCoord.onAdd = function () {
      var div = L.DomUtil.create("div", "prisma-mapa-coord");
      div.style.background = "rgba(0,0,0,0.55)";
      div.style.color = "#fff";
      div.style.padding = "2px 6px";
      div.style.fontSize = "12px";
      div.style.fontFamily = "monospace";
      div.textContent = "x: – / y: –";
      this._div = div;
      return div;
    };
    controleCoord.addTo(mapa);

    mapa.on("mousemove", function (e) {
      if (!nivelAtual) return;
      var p = imagemDoPonto(nivelAtual.altura, e.latlng);
      controleCoord._div.textContent = "x: " + p.x + " / y: " + p.y;
    });

    var controleEditar = L.control({ position: "topright" });
    controleEditar.onAdd = function () {
      var div = L.DomUtil.create("div", "leaflet-bar prisma-mapa-editar-ctrl");
      L.DomEvent.disableClickPropagation(div);
      var btn = L.DomUtil.create("a", "", div);
      btn.href = "#";
      btn.innerHTML = "✏️ Editar";
      btn.style.width = "auto";
      btn.style.padding = "0 10px";
      L.DomEvent.on(btn, "click", function (e) {
        L.DomEvent.preventDefault(e);
        editando = !editando;
        btn.innerHTML = editando ? "✓ Editando" : "✏️ Editar";
        L.DomUtil[editando ? "addClass" : "removeClass"](div, "ativo");
        container.style.cursor = editando ? "crosshair" : "";
      });
      return div;
    };
    controleEditar.addTo(mapa);

    var controleSalvar = L.control({ position: "topright" });
    controleSalvar.onAdd = function () {
      var div = L.DomUtil.create("div", "leaflet-bar");
      L.DomEvent.disableClickPropagation(div);
      var btn = L.DomUtil.create("a", "", div);
      btn.href = "#";
      btn.title = "Salvar os pontos em mapa-dados.js (precisa do notas/mapa_servidor.py rodando)";
      btn.innerHTML = "💾 Salvar";
      btn.style.width = "auto";
      btn.style.padding = "0 10px";
      L.DomEvent.on(btn, "click", function (e) {
        L.DomEvent.preventDefault(e);
        salvar();
      });
      return div;
    };
    controleSalvar.addTo(mapa);

    var controleDescartar = L.control({ position: "topright" });
    controleDescartar.onAdd = function () {
      var div = L.DomUtil.create("div", "leaflet-bar");
      L.DomEvent.disableClickPropagation(div);
      var btn = L.DomUtil.create("a", "", div);
      btn.href = "#";
      btn.title = "Descartar edições feitas aqui que ainda não foram salvas";
      btn.innerHTML = "↺";
      var confirmandoDescarte = false;
      L.DomEvent.on(btn, "click", function (e) {
        L.DomEvent.preventDefault(e);
        if (!confirmandoDescarte) {
          confirmandoDescarte = true;
          btn.innerHTML = "clique de novo";
          btn.style.width = "auto";
          setTimeout(function () { confirmandoDescarte = false; btn.innerHTML = "↺"; btn.style.width = ""; }, 3000);
          return;
        }
        localStorage.removeItem(CHAVE_LOCAL);
        location.reload();
      });
      return div;
    };
    controleDescartar.addTo(mapa);

    function mostraAviso(msg) {
      var div = document.createElement("div");
      div.className = "prisma-mapa-aviso";
      div.textContent = msg;
      document.body.appendChild(div);
      setTimeout(function () { div.remove(); }, 2400);
    }

    function salvar() {
      fetch("http://127.0.0.1:8010/salvar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ niveis: NIVEIS })
      }).then(function (resp) {
        if (!resp.ok) return resp.json().then(function (j) { throw new Error(j.erro || ("HTTP " + resp.status)); });
        return resp.json();
      }).then(function () {
        localStorage.removeItem(CHAVE_LOCAL);
        mostraAviso("Salvo em mapa-dados.js ✓");
      }).catch(function (erro) {
        abreExportador(erro);
      });
    }

    // -------------------------------------------------------- popups

    function abrePopupLeitura(marcador, ponto) {
      var html = "<strong>" + escapeHtml(ponto.nome) + "</strong>";
      if (ponto.descricao) html += "<p>" + escapeHtml(ponto.descricao) + "</p>";
      if (ponto.expande) html += '<button type="button" class="prisma-mapa-expandir">Ver mapa da cidade</button>';
      var popup = L.popup().setLatLng(marcador.getLatLng()).setContent(html).openOn(mapa);
      if (ponto.expande) {
        var el = popup.getElement();
        var btn = el && el.querySelector(".prisma-mapa-expandir");
        if (btn) btn.addEventListener("click", function () { carregaNivel(ponto.expande); });
      }
    }

    function abreFormPonto(chave, indice, latlng) {
      var nivel = NIVEIS[chave];
      var novo = (indice === null || indice === undefined);
      var ponto = novo
        ? { nome: "", descricao: "", icone: "", expande: "" }
        : { nome: nivel.pontos[indice].nome, descricao: nivel.pontos[indice].descricao || "", icone: nivel.pontos[indice].icone || "", expande: nivel.pontos[indice].expande || "" };
      var xy = imagemDoPonto(nivel.altura, latlng);

      var outrosNiveis = Object.keys(NIVEIS).filter(function (k) { return k !== chave; });
      var opcoesExpande = '<option value="">— nenhum —</option>' + outrosNiveis.map(function (k) {
        return '<option value="' + k + '"' + (ponto.expande === k ? " selected" : "") + ">" + escapeHtml(NIVEIS[k].titulo || k) + "</option>";
      }).join("");

      var opcoesIcones = ICONES_RAPIDOS.map(function (ic) {
        var valor = ic.emoji === "📍" ? "" : ic.emoji;
        var selecionado = valor === (ponto.icone || "") ? " selecionado" : "";
        return '<button type="button" class="prisma-mapa-icone-opcao' + selecionado + '" data-icone="' + valor + '" title="' + escapeHtml(ic.rotulo) + '">' + ic.emoji + "</button>";
      }).join("");

      var html = ''
        + '<div class="prisma-mapa-form">'
        + '<strong>' + (novo ? "Novo ponto" : "Editar ponto") + '</strong>'
        + '<label>Nome<br><input type="text" class="pmf-nome" value="' + escapeHtml(ponto.nome) + '"></label>'
        + '<label>Descrição<br><textarea class="pmf-descricao" rows="3">' + escapeHtml(ponto.descricao) + '</textarea></label>'
        + '<label>Ícone</label>'
        + '<div class="prisma-mapa-icones-rapidos">' + opcoesIcones + '</div>'
        + '<input type="text" class="pmf-icone" placeholder="vazio = pino padrão, ou cole um emoji" value="' + escapeHtml(ponto.icone) + '">'
        + '<label>Vira porta pra outro mapa<br><select class="pmf-expande">' + opcoesExpande + '</select></label>'
        + '<div class="prisma-mapa-form-botoes">'
        + '<button type="button" class="pmf-salvar">Salvar</button>'
        + (novo ? '' : '<button type="button" class="pmf-excluir">Excluir</button>')
        + '<button type="button" class="pmf-cancelar">Cancelar</button>'
        + '</div>'
        + '</div>';

      var popup = L.popup({ minWidth: 240, maxWidth: 280, closeOnClick: false })
        .setLatLng(latlng)
        .setContent(html)
        .openOn(mapa);

      var el = popup.getElement();
      el.querySelector(".prisma-mapa-icones-rapidos").addEventListener("click", function (e) {
        var btn = e.target.closest(".prisma-mapa-icone-opcao");
        if (!btn) return;
        el.querySelector(".pmf-icone").value = btn.getAttribute("data-icone");
        el.querySelectorAll(".prisma-mapa-icone-opcao").forEach(function (b) { b.classList.remove("selecionado"); });
        btn.classList.add("selecionado");
      });
      el.querySelector(".pmf-cancelar").addEventListener("click", function () { mapa.closePopup(popup); });
      el.querySelector(".pmf-salvar").addEventListener("click", function () {
        var novoPonto = {
          nome: el.querySelector(".pmf-nome").value.trim() || "Sem nome",
          x: xy.x,
          y: xy.y,
          descricao: el.querySelector(".pmf-descricao").value.trim(),
          icone: el.querySelector(".pmf-icone").value.trim(),
          expande: el.querySelector(".pmf-expande").value
        };
        if (!novoPonto.descricao) delete novoPonto.descricao;
        if (!novoPonto.icone) delete novoPonto.icone;
        if (!novoPonto.expande) delete novoPonto.expande;
        if (!novo) {
          novoPonto.x = nivel.pontos[indice].x;
          novoPonto.y = nivel.pontos[indice].y;
        }
        if (novo) nivel.pontos.push(novoPonto);
        else nivel.pontos[indice] = novoPonto;
        salvaEdicoesLocais(NIVEIS);
        mapa.closePopup(popup);
        carregaNivel(chave);
      });
      if (!novo) {
        var botaoExcluir = el.querySelector(".pmf-excluir");
        var confirmando = false;
        botaoExcluir.addEventListener("click", function () {
          if (!confirmando) {
            confirmando = true;
            botaoExcluir.textContent = "Clique de novo pra confirmar";
            return;
          }
          nivel.pontos.splice(indice, 1);
          salvaEdicoesLocais(NIVEIS);
          mapa.closePopup(popup);
          carregaNivel(chave);
        });
      }
    }

    function abreExportador(erro) {
      var texto = "// Dados do mapa interativo — exportado do modo de edição em "
        + new Date().toLocaleString("pt-BR") + ".\n"
        + "// Cole isso substituindo TODO o conteúdo de docs/assets/js/mapa-dados.js\n\n"
        + "var NIVEIS = " + JSON.stringify(NIVEIS, null, 2) + ";\n";

      var overlay = document.createElement("div");
      overlay.className = "prisma-mapa-exportar-overlay";
      overlay.innerHTML = ''
        + '<div class="prisma-mapa-exportar-caixa">'
        + '<strong>Não consegui salvar automaticamente</strong>'
        + '<p>' + (erro ? escapeHtml(erro.message) + " — " : "") + 'confirme que o servidor local está rodando '
        + '(<code>python notas/mapa_servidor.py</code> numa aba de terminal, ao lado do <code>mkdocs serve</code>) '
        + 'e clique em "💾 Salvar" de novo.</p>'
        + '<p>Se preferir resolver na mão agora: copie o texto abaixo e cole por cima de <strong>todo</strong> '
        + 'o conteúdo do arquivo <code>docs/assets/js/mapa-dados.js</code>.</p>'
        + '<textarea readonly></textarea>'
        + '<div class="prisma-mapa-exportar-botoes">'
        + '<button type="button" class="pme-copiar">Copiar</button>'
        + '<button type="button" class="pme-fechar">Fechar</button>'
        + '</div></div>';
      document.body.appendChild(overlay);
      var textarea = overlay.querySelector("textarea");
      textarea.value = texto;
      overlay.querySelector(".pme-fechar").addEventListener("click", function () { document.body.removeChild(overlay); });
      overlay.querySelector(".pme-copiar").addEventListener("click", function () {
        textarea.focus();
        textarea.select();
        var botao = overlay.querySelector(".pme-copiar");
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(texto).then(function () { botao.textContent = "Copiado!"; });
        } else {
          document.execCommand("copy");
          botao.textContent = "Copiado!";
        }
      });
    }

    // ---------------------------------------------------------- níveis

    function carregaNivel(chave) {
      var nivel = NIVEIS[chave];
      if (!nivel) return;
      nivelAtual = nivel;
      nivelAtualChave = chave;

      if (camadaAtual) mapa.removeLayer(camadaAtual);
      marcadoresAtuais.forEach(function (m) { mapa.removeLayer(m); });
      marcadoresAtuais = [];

      var bounds = [[0, 0], [nivel.altura, nivel.largura]];
      camadaAtual = L.imageOverlay(BASE + nivel.imagem, bounds).addTo(mapa);
      mapa.setMaxBounds(bounds);
      mapa.fitBounds(bounds);

      controleVoltar._div.style.display = nivel.voltarPara ? "" : "none";

      nivel.pontos.forEach(function (ponto, indice) {
        var latlng = pontoImagem(nivel.altura, ponto.x, ponto.y);
        var marcador = L.marker(latlng, { icon: criaIcone(ponto) }).addTo(mapa);
        marcador.on("click", function () {
          if (editando) abreFormPonto(chave, indice, marcador.getLatLng());
          else abrePopupLeitura(marcador, ponto);
        });
        marcadoresAtuais.push(marcador);
      });
    }

    mapa.on("click", function (e) {
      if (!editando) return;
      abreFormPonto(nivelAtualChave, null, e.latlng);
    });

    carregaNivel(nivelInicial);
  }

  window.iniciaMapaPrisma = iniciaMapaPrisma;
})();
