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

  // A barra de filtro é sticky e muda de altura conforme a largura da tela
  // (de uma a quatro linhas). Sem esta correção, chegar num card por link
  // direto o deixa escondido atrás dela justamente no momento em que o
  // leitor quer lê-lo.
  function rolaAte(card) {
    function ajusta() {
      var barra = document.querySelector(".prg-filtro");
      if (!barra) return;
      var sobra =
        barra.getBoundingClientRect().bottom - card.getBoundingClientRect().top;
      if (sobra > 0) window.scrollBy(0, -(sobra + 12));
    }
    card.scrollIntoView({ block: "start" });
    ajusta();
    // Chegando por link direto, o :target do tema ainda reposiciona a página
    // depois de nós — a correção só se sustenta se repetir no fim da fila.
    setTimeout(ajusta, 120);
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
        rolaAte(card);
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

  // Rótulos fixos pras facetas de vocabulário pequeno e conhecido. As facetas
  // de vocabulário grande (arma, vertente, Suprema final) trazem o rótulo
  // pronto no próprio card, em data-{faceta}-nome — não vale a pena manter
  // aqui uma cópia de 62 nomes de arma que desatualiza sozinha.
  var RESUMO = {
    grupo: {
      marciais: "Marciais", pontaria: "Pontaria", arcano: "Arcano (foco mágico)",
      "magicas-basicas": "Mágicas Básicas", "magicas-elementais": "Mágicas por Elemento",
      sociais: "Sociais", infiltracao: "Infiltração", mobilidade: "Mobilidade",
      buff: "Buff", debuff: "Debuff", suporte: "Suporte"
    },
    elemento: {
      fogo: "Fogo", gelo: "Gelo", terra: "Terra", raio: "Raio", vento: "Vento",
      agua: "Água", luz: "Luz", sombras: "Sombras", veneno: "Veneno",
      sangue: "Sangue", "espaco-tempo": "Espaço-Tempo"
    },
    atributos: {
      forca: "Força", agilidade: "Agilidade", inteligencia: "Inteligência",
      sabedoria: "Sabedoria", vontade: "Vontade"
    },
    alvo: {
      unico: "Um alvo", area: "Área", "si-mesmo": "Você mesmo",
      "linha-cone": "Linha ou cone", adjacentes: "Adjacentes", aliados: "Aliados"
    }
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

  // valor -> rótulo, do jeito que os cards de fato declaram. Faceta multivalor
  // guarda os valores separados por espaço em data-{faceta} e os rótulos na
  // mesma ordem, separados por "|", em data-{faceta}-nome.
  function coletaFaceta(cards, faceta, multi) {
    var fixos = RESUMO[faceta] || {};
    var mapa = {};
    cards.forEach(function (card) {
      var bruto = card.dataset[faceta];
      if (!bruto) return;
      var nomes = card.dataset[faceta + "Nome"];
      if (multi) {
        var rotulos = nomes ? nomes.split("|") : [];
        bruto.split(" ").forEach(function (item, i) {
          if (item && !mapa[item]) mapa[item] = rotulos[i] || fixos[item] || item;
        });
      } else if (!mapa[bruto]) {
        mapa[bruto] = nomes || fixos[bruto] || bruto;
      }
    });
    return mapa;
  }

  function iniciaFiltro() {
    var barra = document.querySelector(".prg-filtro");
    if (!barra) return;

    var campo = barra.querySelector(".prg-filtro__campo");
    var contagem = barra.querySelector(".prg-filtro__contagem");
    var botao = barra.querySelector(".prg-filtro__tudo");
    var sliderMana = barra.querySelector(".prg-filtro__mana-slider");
    var valorMana = barra.querySelector(".prg-filtro__mana-valor");
    var checkDesarmado = barra.querySelector(".prg-filtro__desarmado-campo");
    var rotulo = barra.dataset.rotulo || "itens";
    var cards = Array.prototype.slice.call(document.querySelectorAll(".prg-card"));

    // --- popula cada select a partir do que de fato existe nos cards ---

    var selects = Array.prototype.slice.call(
      barra.querySelectorAll(".prg-filtro__select[data-faceta]")
    ).map(function (sel) {
      var faceta = sel.dataset.faceta;
      var multi = sel.dataset.multi === "1";
      var mapa = coletaFaceta(cards, faceta, multi);
      var valores = Object.keys(mapa).sort(function (a, b) {
        return mapa[a].localeCompare(mapa[b], "pt-BR");
      });
      preencheSelect(sel, valores.map(function (v) { return [v, mapa[v]]; }));
      return { el: sel, faceta: faceta, multi: multi };
    });

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
      var manaDisponivel = sliderMana ? Number(sliderMana.value) : Infinity;
      var soDesarmado = checkDesarmado ? checkDesarmado.checked : false;

      var visiveis = 0;
      cards.forEach(function (card) {
        var d = card.dataset;
        var bate = !termo || (d.busca || "").indexOf(termo) !== -1;
        selects.forEach(function (f) {
          if (!bate || !f.el.value) return;
          bate = f.multi
            ? (d[f.faceta] || "").split(" ").indexOf(f.el.value) !== -1
            : d[f.faceta] === f.el.value;
        });
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
          ? cards.length + " " + rotulo
          : visiveis + " de " + cards.length;
    }

    campo.addEventListener("input", atualiza);
    campo.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { campo.value = ""; atualiza(); }
    });

    selects.forEach(function (f) { f.el.addEventListener("change", atualiza); });

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

    iniciaSorteio(barra, cards, selects, campo, atualiza);
    atualiza();
  }

  /* ------------------------------------------------------------- sorteio */

  // A tabela de sorteio em papel continua existindo (Sorteio de Pacote); isto
  // é a mesma rolagem feita aqui, pra não precisar sair da listagem — e sem
  // repetir os 100 nomes numa segunda lista que teria que ser mantida junto.
  function iniciaSorteio(barra, cards, selects, campo, atualiza) {
    var botao = barra.querySelector(".prg-filtro__sortear");
    if (!botao) return;
    var seletor = barra.querySelector(".prg-filtro__sorteio-vertente");
    var saida = barra.querySelector(".prg-filtro__sorteio-saida");

    var mapa = coletaFaceta(cards, "vertente", false);
    var vertentes = Object.keys(mapa).sort(function (a, b) {
      return mapa[a].localeCompare(mapa[b], "pt-BR");
    });
    if (seletor) preencheSelect(seletor, vertentes.map(function (v) { return [v, mapa[v]]; }));

    botao.addEventListener("click", function () {
      var escolhida = (seletor && seletor.value) ||
        vertentes[Math.floor(Math.random() * vertentes.length)];
      var d20 = 1 + Math.floor(Math.random() * 20);
      var alvo = cards.filter(function (c) {
        return c.dataset.vertente === escolhida && c.dataset.d20 === String(d20);
      })[0];
      if (!alvo) return;

      // O resultado tem que aparecer mesmo que um filtro o esconda: a rolagem
      // manda mais que a peneira que estava na tela.
      campo.value = "";
      selects.forEach(function (f) { f.el.value = ""; });
      atualiza();

      cards.forEach(function (c) { c.classList.remove("is-sorteado"); });
      abre(alvo, true);
      alvo.classList.add("is-sorteado");
      rolaAte(alvo);
      if (saida) {
        saida.textContent = mapa[escolhida] + " · d20 = " + d20 + " → " +
          (alvo.querySelector(".prg-card__nome") || {}).textContent;
      }
    });
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
