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

  function iniciaFiltro() {
    var barra = document.querySelector(".prg-filtro");
    if (!barra) return;

    var campo = barra.querySelector(".prg-filtro__campo");
    var contagem = barra.querySelector(".prg-filtro__contagem");
    var botao = barra.querySelector(".prg-filtro__tudo");
    var cards = Array.prototype.slice.call(document.querySelectorAll(".prg-card"));

    function atualiza() {
      var termo = normaliza(campo.value.trim());
      var visiveis = 0;
      cards.forEach(function (card) {
        var bate = !termo || (card.dataset.busca || "").indexOf(termo) !== -1;
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
