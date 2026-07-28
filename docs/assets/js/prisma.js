/* =========================================================================
   Prisma RPG — comportamento de leitura.

   1. Cards de habilidade: abre/fecha, filtro por texto, expandir tudo.
   2. Realce dos degraus de Intensidade dentro do card.
   3. Popover de glossário: passar o mouse num termo mostra a definição ali
      mesmo, em vez de exigir uma viagem até a página do glossário.
   ========================================================================= */

(function () {
  "use strict";

  // Resolvido no carregamento: o JSON do glossário mora ao lado deste script.
  var URL_GLOSSARIO = (function () {
    var s = document.currentScript;
    return s ? s.src.replace(/\/js\/prisma\.js.*$/, "/glossario.json") : null;
  })();

  var glossario = null;
  var carregando = null;

  function pegaGlossario() {
    if (glossario) return Promise.resolve(glossario);
    if (carregando) return carregando;
    if (!URL_GLOSSARIO) return Promise.resolve({});
    carregando = fetch(URL_GLOSSARIO)
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (dados) { glossario = dados; return dados; })
      .catch(function () { glossario = {}; return glossario; });
    return carregando;
  }

  /* --------------------------------------------------------------- cards */

  function abre(card, aberto) {
    card.classList.toggle("is-aberto", aberto);
    var hd = card.querySelector(".prg-card__hd");
    if (hd) hd.setAttribute("aria-expanded", aberto ? "true" : "false");
  }

  function marcaIntensidades(card) {
    var itens = card.querySelectorAll(".prg-card__bd > ul > li");
    Array.prototype.forEach.call(itens, function (li) {
      var forte = li.querySelector("strong");
      if (!forte) return;
      var t = forte.textContent;
      if (/^Intensidade III/.test(t)) li.classList.add("prg-int-iii");
      else if (/^Intensidade II/.test(t)) li.classList.add("prg-int-ii");
      else if (/^Intensidade I/.test(t)) li.classList.add("prg-int-i");
      else if (/^Cr[ií]tico/.test(t)) li.classList.add("prg-critico");
      else if (/^Acerto/.test(t)) li.classList.add("prg-int-iii");
    });
  }

  function iniciaCards() {
    var cards = document.querySelectorAll(".prg-card");
    if (!cards.length) return;

    Array.prototype.forEach.call(cards, function (card) {
      marcaIntensidades(card);
      var hd = card.querySelector(".prg-card__hd");
      if (!hd) return;
      hd.addEventListener("click", function () {
        abre(card, !card.classList.contains("is-aberto"));
      });
    });

    // Chegou por link direto ou pela busca do site: o card precisa estar aberto.
    function abrePeloHash() {
      var hash = decodeURIComponent(location.hash || "").slice(1);
      if (!hash) return;
      var alvo = document.getElementById(hash);
      var card = alvo && alvo.closest(".prg-card");
      if (card) {
        abre(card, true);
        card.scrollIntoView({ block: "start" });
      }
    }
    abrePeloHash();
    window.addEventListener("hashchange", abrePeloHash);
  }

  /* -------------------------------------------------------------- filtro */

  function normaliza(txt) {
    return txt
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  // Rótulos fixos pras facetas de vocabulário pequeno e conhecido — arma é a
  // única faceta com rótulo dinâmico (data-arma-nome), porque são 62 valores.
  var RESUMO_GRUPO = {
    marciais: "Marciais", pontaria: "Pontaria", arcano: "Arcano (foco mágico)",
    "magicas-basicas": "Mágicas Básicas", "magicas-elementais": "Mágicas por Elemento",
    sociais: "Sociais", infiltracao: "Infiltração", mobilidade: "Mobilidade",
    buff: "Buff", debuff: "Debuff", suporte: "Suporte"
  };
  var RESUMO_ELEMENTO = {
    fogo: "Fogo", gelo: "Gelo", terra: "Terra", raio: "Raio", vento: "Vento",
    agua: "Água", luz: "Luz", sombras: "Sombras", veneno: "Veneno",
    sangue: "Sangue", "espaco-tempo": "Espaço-Tempo"
  };
  var RESUMO_ATRIBUTO = {
    forca: "Força", agilidade: "Agilidade", inteligencia: "Inteligência",
    sabedoria: "Sabedoria", vontade: "Vontade"
  };
  var RESUMO_ALVO = {
    unico: "Um alvo", area: "Área", "si-mesmo": "Você mesmo",
    "linha-cone": "Linha ou cone", adjacentes: "Adjacentes", aliados: "Aliados"
  };

  function preencheSelect(select, valores) {
    // valores: [[value, label], ...] já ordenado
    valores.forEach(function (par) {
      var opt = document.createElement("option");
      opt.value = par[0];
      opt.textContent = par[1];
      select.appendChild(opt);
    });
  }

  function coletaFaceta(cards, campo) {
    var vistos = {};
    cards.forEach(function (card) {
      var v = card.dataset[campo];
      if (v) vistos[v] = true;
    });
    return Object.keys(vistos);
  }

  function coletaFacetaMultipla(cards, campo) {
    // pra data-atributos, que guarda vários valores separados por espaço
    var vistos = {};
    cards.forEach(function (card) {
      var v = card.dataset[campo];
      if (!v) return;
      v.split(" ").forEach(function (item) { if (item) vistos[item] = true; });
    });
    return Object.keys(vistos);
  }

  function iniciaFiltro() {
    var barra = document.querySelector(".prg-filtro");
    if (!barra) return;

    var campo = barra.querySelector(".prg-filtro__campo");
    var contagem = barra.querySelector(".prg-filtro__contagem");
    var botao = barra.querySelector(".prg-filtro__tudo");
    var selectGrupo = barra.querySelector('[data-faceta="grupo"]');
    var selectElemento = barra.querySelector('[data-faceta="elemento"]');
    var selectArma = barra.querySelector('[data-faceta="arma"]');
    var selectAtributo = barra.querySelector('[data-faceta="atributos"]');
    var selectAlvo = barra.querySelector('[data-faceta="alvo"]');
    var sliderMana = barra.querySelector(".prg-filtro__mana-slider");
    var valorMana = barra.querySelector(".prg-filtro__mana-valor");
    var checkDesarmado = barra.querySelector(".prg-filtro__desarmado-campo");
    var cards = Array.prototype.slice.call(document.querySelectorAll(".prg-card"));

    // --- popula os selects a partir do que de fato existe nos cards ---

    if (selectGrupo) {
      var grupos = coletaFaceta(cards, "grupo").sort(function (a, b) {
        return (RESUMO_GRUPO[a] || a).localeCompare(RESUMO_GRUPO[b] || b, "pt-BR");
      });
      preencheSelect(selectGrupo, grupos.map(function (g) { return [g, RESUMO_GRUPO[g] || g]; }));
    }

    if (selectElemento) {
      var elementos = coletaFaceta(cards, "elemento").sort(function (a, b) {
        return (RESUMO_ELEMENTO[a] || a).localeCompare(RESUMO_ELEMENTO[b] || b, "pt-BR");
      });
      preencheSelect(selectElemento, elementos.map(function (e) { return [e, RESUMO_ELEMENTO[e] || e]; }));
    }

    if (selectArma) {
      var nomesArma = {};
      cards.forEach(function (card) {
        var a = card.dataset.arma;
        if (a && !nomesArma[a]) nomesArma[a] = card.dataset.armaNome || a;
      });
      var armas = Object.keys(nomesArma).sort(function (a, b) {
        return nomesArma[a].localeCompare(nomesArma[b], "pt-BR");
      });
      preencheSelect(selectArma, armas.map(function (a) { return [a, nomesArma[a]]; }));
    }

    if (selectAtributo) {
      var atributos = coletaFacetaMultipla(cards, "atributos").sort(function (a, b) {
        return (RESUMO_ATRIBUTO[a] || a).localeCompare(RESUMO_ATRIBUTO[b] || b, "pt-BR");
      });
      preencheSelect(selectAtributo, atributos.map(function (a) { return [a, RESUMO_ATRIBUTO[a] || a]; }));
    }

    if (selectAlvo) {
      var alvos = coletaFaceta(cards, "alvo").sort(function (a, b) {
        return (RESUMO_ALVO[a] || a).localeCompare(RESUMO_ALVO[b] || b, "pt-BR");
      });
      preencheSelect(selectAlvo, alvos.map(function (a) { return [a, RESUMO_ALVO[a] || a]; }));
    }

    // Mana: o teto do slider é o maior custo mínimo realmente usado — assim
    // o slider no máximo sempre mostra tudo, sem precisar hardcodar um valor
    // que desatualiza se o conteúdo mudar.
    var manaMaxima = 0;
    cards.forEach(function (card) {
      var m = card.dataset.manaMin;
      if (m !== "" && m !== undefined) manaMaxima = Math.max(manaMaxima, Number(m));
    });
    if (sliderMana) {
      sliderMana.max = String(manaMaxima);
      sliderMana.value = String(manaMaxima);
      if (valorMana) valorMana.textContent = String(manaMaxima);
    }

    function atualiza() {
      var termo = normaliza(campo.value.trim());
      var grupo = selectGrupo ? selectGrupo.value : "";
      var elemento = selectElemento ? selectElemento.value : "";
      var arma = selectArma ? selectArma.value : "";
      var atributo = selectAtributo ? selectAtributo.value : "";
      var alvo = selectAlvo ? selectAlvo.value : "";
      var manaDisponivel = sliderMana ? Number(sliderMana.value) : Infinity;
      var soDesarmado = checkDesarmado ? checkDesarmado.checked : false;

      var visiveis = 0;
      cards.forEach(function (card) {
        var d = card.dataset;
        var bate = !termo || (d.busca || "").indexOf(termo) !== -1;
        if (bate && grupo) bate = d.grupo === grupo;
        if (bate && elemento) bate = d.elemento === elemento;
        if (bate && arma) bate = d.arma === arma;
        if (bate && atributo) bate = (d.atributos || "").split(" ").indexOf(atributo) !== -1;
        if (bate && alvo) bate = d.alvo === alvo;
        if (bate && soDesarmado) bate = d.desarmado === "1";
        // Sem mana-min = custa Vida, não Mana — cabe em qualquer orçamento.
        if (bate && d.manaMin !== "" && d.manaMin !== undefined) {
          bate = Number(d.manaMin) <= manaDisponivel;
        }
        card.classList.toggle("is-oculto", !bate);
        if (bate) visiveis++;
      });
      contagem.textContent =
        visiveis === cards.length
          ? cards.length + " habilidades"
          : visiveis + " de " + cards.length;
    }

    campo.addEventListener("input", atualiza);
    campo.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { campo.value = ""; atualiza(); }
    });

    [selectGrupo, selectElemento, selectArma, selectAtributo, selectAlvo].forEach(function (sel) {
      if (sel) sel.addEventListener("change", atualiza);
    });

    if (sliderMana) {
      sliderMana.addEventListener("input", function () {
        if (valorMana) valorMana.textContent = sliderMana.value;
        atualiza();
      });
    }

    if (checkDesarmado) checkDesarmado.addEventListener("change", atualiza);

    botao.addEventListener("click", function () {
      var abrir = botao.dataset.estado !== "aberto";
      cards.forEach(function (card) {
        if (!card.classList.contains("is-oculto")) abre(card, abrir);
      });
      botao.dataset.estado = abrir ? "aberto" : "fechado";
      botao.textContent = abrir ? "Recolher tudo" : "Expandir tudo";
    });

    atualiza();
  }

  /* ------------------------------------------------------------ popover */

  var pop = null;
  var timer = null;

  function criaPop() {
    if (pop) return pop;
    pop = document.createElement("div");
    pop.className = "prg-pop";
    pop.setAttribute("role", "tooltip");
    document.body.appendChild(pop);
    return pop;
  }

  function posiciona(el) {
    var r = el.getBoundingClientRect();
    var p = criaPop();
    p.style.left = "0px";
    p.style.top = "0px";
    var largura = p.offsetWidth;
    var altura = p.offsetHeight;
    var esq = window.scrollX + r.left;
    var margem = 8;
    if (esq + largura > window.scrollX + document.documentElement.clientWidth - margem) {
      esq = window.scrollX + document.documentElement.clientWidth - largura - margem;
    }
    if (esq < window.scrollX + margem) esq = window.scrollX + margem;

    // Acima do termo quando não couber abaixo.
    var abaixo = r.bottom + altura + margem < window.innerHeight;
    var topo = abaixo
      ? window.scrollY + r.bottom + 6
      : window.scrollY + r.top - altura - 6;

    p.style.left = esq + "px";
    p.style.top = topo + "px";
  }

  function esconde() {
    clearTimeout(timer);
    if (pop) pop.classList.remove("is-visivel");
  }

  function mostra(el, verbete) {
    var p = criaPop();
    p.innerHTML =
      '<span class="prg-pop__titulo">' + verbete.titulo + "</span>" +
      verbete.corpo +
      '<span class="prg-pop__rodape">clique para abrir o verbete completo</span>';
    p.classList.add("is-visivel");
    posiciona(el);
  }

  function chaveDoLink(a) {
    var href = a.getAttribute("href") || "";
    if (href.indexOf("#") === -1) return null;
    var partes = href.split("#");
    var alvo = partes[0];
    // Só links que apontam para o glossário (mesma página ou relativo).
    var ehGlossario =
      /glossario/i.test(alvo) ||
      (alvo === "" && /\/glossario\/?$/.test(location.pathname));
    return ehGlossario ? decodeURIComponent(partes[1]) : null;
  }

  function iniciaPopover() {
    var links = document.querySelectorAll(".md-typeset a[href*='#']");
    if (!links.length) return;

    pegaGlossario().then(function (dados) {
      Array.prototype.forEach.call(links, function (a) {
        var chave = chaveDoLink(a);
        if (!chave || !dados[chave]) return;
        a.classList.add("prg-termo");

        a.addEventListener("mouseenter", function () {
          clearTimeout(timer);
          timer = setTimeout(function () { mostra(a, dados[chave]); }, 180);
        });
        a.addEventListener("mouseleave", esconde);
        a.addEventListener("focus", function () { mostra(a, dados[chave]); });
        a.addEventListener("blur", esconde);
      });
    });
  }

  /* --------------------------------------------------------------- boot */

  function inicia() {
    iniciaCards();
    iniciaFiltro();
    iniciaPopover();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(inicia);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inicia);
  } else {
    inicia();
  }

  window.addEventListener("scroll", esconde, { passive: true });
})();
