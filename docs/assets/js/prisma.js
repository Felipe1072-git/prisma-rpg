/* =========================================================================
   Prisma RPG — comportamento de leitura.

   1. Cards de habilidade: abre/fecha, filtro por texto, expandir tudo.
   2. Realce dos degraus de Intensidade dentro do card.
   3. Popover de glossário: passar o mouse num termo mostra a definição ali
      mesmo, em vez de exigir uma viagem até a página do glossário.
   4. Lightbox: clicar numa imagem de conteúdo (retrato de Mundo, foto de
      lugar) abre ela em tela cheia; X ou Esc fecha.
   ========================================================================= */

(function () {
  "use strict";

  // Resolvidos no carregamento: os dois JSON moram ao lado deste script.
  // Glossário responde "o que esse termo quer dizer"; habilidades responde
  // "o que essa habilidade faz" — mesma interação, dicionários diferentes.
  function urlDe(nome) {
    var s = document.currentScript;
    return s ? s.src.replace(/\/js\/prisma\.js.*$/, "/" + nome + ".json") : null;
  }

  var URL = { glossario: urlDe("glossario"), habilidades: urlDe("habilidades"), mundo: urlDe("mundo") };

  // Raiz do site (com o prefixo do GitHub Pages incluso), pra resolver link
  // de página de Mundo pelo caminho — diferente de glossário/habilidades,
  // cada página de Mundo é o próprio verbete, não uma âncora numa listagem.
  var RAIZ_SITE = (function () {
    var s = document.currentScript;
    return s ? s.src.replace(/assets\/js\/prisma\.js.*$/, "") : null;
  })();
  var dicionarios = {};
  var carregando = {};

  function pegaDicionario(nome) {
    if (dicionarios[nome]) return Promise.resolve(dicionarios[nome]);
    if (carregando[nome]) return carregando[nome];
    if (!URL[nome]) return Promise.resolve({});
    carregando[nome] = fetch(URL[nome])
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { dicionarios[nome] = d; return d; })
      .catch(function () { dicionarios[nome] = {}; return dicionarios[nome]; });
    return carregando[nome];
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
  // Um link pode apontar pra dentro de um bloco `???` fechado. Sem abrir o
  // bloco, o leitor cai numa página que aparentemente ignorou o clique.
  function abreAncestrais(el) {
    var d = el.closest("details");
    while (d) {
      d.open = true;
      d = d.parentElement && d.parentElement.closest("details");
    }
  }

  function rolaAte(card) {
    abreAncestrais(card);
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
    // Na ficha de criatura a lista de Intensidades mora dentro do bloco da
    // ação, não solta no corpo do card — daí o descendente, não o filho.
    var itens = card.querySelectorAll(".prg-card__bd ul > li");
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

  // Chegar num verbete por link direto (`glossario/#atordoado`, o destino de
  // mais de mil links no site) precisa da mesma correção de rolagem que os
  // cards: sem ela o termo fica escondido atrás da barra sticky, justamente
  // no momento em que o leitor quer lê-lo.
  function iniciaVerbetes() {
    var verbetes = document.querySelectorAll(".prg-verbete");
    if (!verbetes.length) return;

    function vaiPeloHash() {
      var hash = decodeURIComponent(location.hash || "").slice(1);
      if (!hash) return;
      var alvo = document.getElementById(hash);
      var verbete = alvo && alvo.closest(".prg-verbete");
      if (verbete) rolaAte(verbete);
    }
    vaiPeloHash();
    window.addEventListener("hashchange", vaiPeloHash);
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
      "magicas-elementais": "Mágicas por Elemento",
      sociais: "Sociais", infiltracao: "Infiltração", mobilidade: "Mobilidade",
      buff: "Buff", debuff: "Debuff", suporte: "Suporte",
      necromancia: "Necromancia", "projecao-mental": "Projeção Mental",
      "alquimia-de-mana": "Alquimia de Mana", "percepcao-arcana": "Percepção Arcana",
      conjuracao: "Conjuração"
    },
    elemento: {
      fogo: "Fogo", gelo: "Gelo", terra: "Terra", raio: "Raio", vento: "Vento",
      agua: "Água", luz: "Luz", sombras: "Sombras", veneno: "Veneno",
      sangue: "Sangue", "espaco-tempo": "Espaço-Tempo", arcano: "Arcano"
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

  // Facetas que têm ordem própria — escala de ameaça, peso de arma. Ordenar
  // "Comum, Formidável, Treinado" por alfabeto esconde justamente o que a
  // faceta quer dizer. Quem não está aqui continua em ordem alfabética.
  var ORDEM = {
    tier: ["comum", "treinado", "formidavel", "lendario"],
    couraca: ["nenhuma", "coriacea", "escamada", "blindada", "draconica"],
    eixo: ["passado", "ambiente", "evento"]
  };

  function ordenaFaceta(faceta, mapa) {
    var fixa = ORDEM[faceta];
    return Object.keys(mapa).sort(function (a, b) {
      if (fixa) {
        var ia = fixa.indexOf(a), ib = fixa.indexOf(b);
        if (ia !== -1 || ib !== -1) return (ia === -1 ? 99 : ia) - (ib === -1 ? 99 : ib);
      }
      return mapa[a].localeCompare(mapa[b], "pt-BR");
    });
  }

  function iniciaFiltro() {
    var barra = document.querySelector(".prg-filtro");
    if (!barra) return;

    var campo = barra.querySelector(".prg-filtro__campo");
    var contagem = barra.querySelector(".prg-filtro__contagem");
    var botao = barra.querySelector(".prg-filtro__tudo");
    var checkDesarmado = barra.querySelector(".prg-filtro__desarmado-campo");
    var rotulo = barra.dataset.rotulo || "itens";
    // O glossário filtra verbetes, não cards: mesma barra, alvo diferente.
    var cards = Array.prototype.slice.call(
      document.querySelectorAll(barra.dataset.alvo || ".prg-card")
    );
    if (!cards.length) return;
    var grupos = Array.prototype.slice.call(document.querySelectorAll(".prg-grupo"));

    // --- popula cada select a partir do que de fato existe nos cards ---

    var selects = Array.prototype.slice.call(
      barra.querySelectorAll(".prg-filtro__select[data-faceta]")
    ).map(function (sel) {
      var faceta = sel.dataset.faceta;
      var multi = sel.dataset.multi === "1";
      var mapa = coletaFaceta(cards, faceta, multi);
      var valores = ordenaFaceta(faceta, mapa);
      preencheSelect(sel, valores.map(function (v) { return [v, mapa[v]]; }));
      return { el: sel, faceta: faceta, multi: multi };
    });

    // --- sliders de orçamento ("o que eu consigo pagar com X?") ---
    //
    // O mesmo controle serve pro Mana das Habilidades e pra prata do
    // Equipamento: o card declara o seu custo em data-{campo}, e passa quem
    // couber no valor escolhido. O teto do slider é o maior custo realmente
    // usado — assim o slider no máximo sempre mostra tudo, sem hardcodar um
    // número que desatualiza junto com o conteúdo.
    var sliders = Array.prototype.slice.call(
      barra.querySelectorAll(".prg-filtro__slider[data-campo]")
    ).map(function (el) {
      var chave = el.dataset.campo.replace(/-(\w)/g, function (_, c) {
        return c.toUpperCase();
      });
      var teto = 0;
      cards.forEach(function (card) {
        var v = card.dataset[chave];
        if (v !== "" && v !== undefined) teto = Math.max(teto, Number(v));
      });
      var saida = barra.querySelector(
        '.prg-filtro__slider-valor[data-campo="' + el.dataset.campo + '"]'
      );
      el.max = String(teto);
      el.value = String(teto);
      if (saida) saida.textContent = String(teto);
      // Card sem valor no campo significa coisas opostas em cada listagem: uma
      // habilidade que cobra Vida cabe em qualquer Mana, mas uma arma lendária
      // sem preço não cabe em orçamento nenhum — ela não se compra.
      return { el: el, chave: chave, saida: saida, ocultaSemValor: el.dataset.semValor === "oculta" };
    });

    function atualiza() {
      var termo = normaliza(campo.value.trim());
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
        sliders.forEach(function (s) {
          if (!bate) return;
          var v = d[s.chave];
          if (v !== "" && v !== undefined) {
            bate = Number(v) <= Number(s.el.value);
          } else if (s.ocultaSemValor && s.el.value !== s.el.max) {
            bate = false;
          }
        });
        card.classList.toggle("is-oculto", !bate);
        if (bate) visiveis++;
      });
      // Categoria sem nenhum item visível some junto com o próprio título —
      // senão o glossário filtrado vira uma sequência de cabeçalhos vazios.
      grupos.forEach(function (g) {
        g.classList.toggle(
          "is-oculto",
          !g.querySelector(".prg-verbete:not(.is-oculto), .prg-card:not(.is-oculto)")
        );
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

    sliders.forEach(function (s) {
      s.el.addEventListener("input", function () {
        if (s.saida) s.saida.textContent = s.el.value;
        atualiza();
      });
    });

    if (checkDesarmado) checkDesarmado.addEventListener("change", atualiza);

    // O glossário não tem botão de expandir: os verbetes já vêm abertos.
    if (botao) {
      botao.addEventListener("click", function () {
        var abrir = botao.dataset.estado !== "aberto";
        cards.forEach(function (card) {
          if (!card.classList.contains("is-oculto")) abre(card, abrir);
        });
        botao.dataset.estado = abrir ? "aberto" : "fechado";
        botao.textContent = abrir ? "Recolher tudo" : "Expandir tudo";
      });
    }

    iniciaSorteio(barra, cards, selects, campo, atualiza);
    atualiza();
  }

  /* ------------------------------------------------------------- sorteio */

  // A tabela de sorteio em papel continua existindo (Sorteio de Pacote, e as
  // três tabelas d20 de Origem); isto é a mesma rolagem feita aqui, pra não
  // precisar sair da listagem — e sem repetir os nomes numa segunda lista que
  // teria que ser mantida junto.
  //
  // O botão declara em que faceta ele sorteia (data-faceta), quantos lados tem
  // o dado (data-lados) e em que campo do card está o número sorteado
  // (data-campo). Pacote sorteia dentro de uma vertente; Origem, dentro de um
  // eixo. A mecânica é a mesma.
  function iniciaSorteio(barra, cards, selects, campo, atualiza) {
    var botao = barra.querySelector(".prg-filtro__sortear");
    if (!botao) return;
    var faceta = botao.dataset.faceta;
    var lados = Number(botao.dataset.lados) || 20;
    var chave = botao.dataset.campo || "d20";
    var seletor = barra.querySelector(".prg-filtro__sorteio-grupo");
    var saida = barra.querySelector(".prg-filtro__sorteio-saida");

    var mapa = coletaFaceta(cards, faceta, false);
    var grupos = ordenaFaceta(faceta, mapa);
    if (seletor) preencheSelect(seletor, grupos.map(function (v) { return [v, mapa[v]]; }));

    botao.addEventListener("click", function () {
      var escolhido = (seletor && seletor.value) ||
        grupos[Math.floor(Math.random() * grupos.length)];
      var dado = 1 + Math.floor(Math.random() * lados);
      var alvo = cards.filter(function (c) {
        return c.dataset[faceta] === escolhido && c.dataset[chave] === String(dado);
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
        saida.textContent = mapa[escolhido] + " · d" + lados + " = " + dado + " → " +
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

  function mostra(el, verbete, rodape) {
    var p = criaPop();
    p.innerHTML =
      '<span class="prg-pop__titulo">' + verbete.titulo + "</span>" +
      verbete.corpo +
      '<span class="prg-pop__rodape">' +
      (rodape || "clique para abrir o verbete completo") + "</span>";
    p.classList.add("is-visivel");
    posiciona(el);
  }

  // Qual dicionário responde por este link, e com que chave.
  //
  // Glossário: qualquer link pra `glossario#termo` (ou pra uma âncora da
  // própria página do glossário). Habilidades: link pra um card da listagem,
  // reconhecido pelo prefixo `hab-` do id — o mesmo que o hook gera.
  function fonteDoLink(a) {
    var href = a.getAttribute("href") || "";

    // Mundo: a própria página é o verbete, casada pelo caminho (sem
    // fragmento) — diferente de glossário/habilidades, que são âncoras
    // dentro de uma listagem única.
    if (RAIZ_SITE) {
      var semFragmento = href.split("#")[0];
      if (semFragmento) {
        try {
          // "URL" aqui embaixo já é o dicionário de JSONs (variável local
          // deste arquivo) — precisa do construtor nativo via `window.URL`.
          var alvoAbs = new window.URL(semFragmento, location.href).pathname;
          var raizAbs = new window.URL(RAIZ_SITE).pathname;
          if (alvoAbs.indexOf(raizAbs) === 0) {
            var caminho = alvoAbs.slice(raizAbs.length).replace(/^\/+/, "");
            if (caminho.indexOf("mundo/") === 0 &&
                caminho !== "mundo/" &&
                !/^mundo\/(index\/)?$/.test(caminho) &&
                caminho.indexOf("mundo/mapa") !== 0) {
              return { dic: "mundo", chave: caminho };
            }
          }
        } catch (e) { /* href inválido — ignora */ }
      }
    }

    if (href.indexOf("#") === -1) return null;
    var partes = href.split("#");
    var alvo = partes[0];
    var chave = decodeURIComponent(partes.slice(1).join("#"));
    if (!chave) return null;

    if (/glossario/i.test(alvo) ||
        (alvo === "" && /\/glossario\/?$/.test(location.pathname))) {
      return { dic: "glossario", chave: chave };
    }
    if (chave.indexOf("hab-") === 0) {
      return { dic: "habilidades", chave: chave };
    }
    return null;
  }

  var RODAPE = {
    glossario: "clique para abrir o verbete completo",
    habilidades: "clique para abrir a ficha completa",
    mundo: "clique para abrir a página completa"
  };

  function iniciaPopover() {
    var links = document.querySelectorAll(".md-typeset a[href]");
    if (!links.length) return;

    // Só busca o dicionário que esta página de fato usa: uma página de prosa
    // não precisa baixar as 571 habilidades.
    var precisa = {};
    Array.prototype.forEach.call(links, function (a) {
      var f = fonteDoLink(a);
      if (f) precisa[f.dic] = true;
    });

    Object.keys(precisa).forEach(function (nome) {
      pegaDicionario(nome).then(function (dados) {
        Array.prototype.forEach.call(links, function (a) {
          var f = fonteDoLink(a);
          if (!f || f.dic !== nome || !dados[f.chave]) return;
          // Link pro card que está nesta mesma página não precisa de espiada:
          // clicar já abre a ficha logo ali.
          if (document.getElementById(f.chave)) return;
          a.classList.add("prg-termo");

          var verbete = dados[f.chave];
          var rodape = RODAPE[nome];
          a.addEventListener("mouseenter", function () {
            clearTimeout(timer);
            timer = setTimeout(function () { mostra(a, verbete, rodape); }, 180);
          });
          a.addEventListener("mouseleave", esconde);
          a.addEventListener("focus", function () { mostra(a, verbete, rodape); });
          a.addEventListener("blur", esconde);
        });
      });
    });
  }

  /* --------------------------------------------------------------- boot */

  // Rede de segurança pra qualquer âncora: se o destino estiver dentro de um
  // bloco colapsável fechado, abre antes de rolar. Vale pros casos que não são
  // card nem verbete — um título dentro de "Como funcionam as Raças", por
  // exemplo.
  function iniciaAncoras() {
    function trata() {
      var hash = decodeURIComponent(location.hash || "").slice(1);
      if (!hash) return;
      var alvo = document.getElementById(hash);
      if (!alvo || !alvo.closest("details")) return;
      abreAncestrais(alvo);
      alvo.scrollIntoView({ block: "start" });
    }
    trata();
    window.addEventListener("hashchange", trata);
  }

  // ------------------------------------------------- montador de encontro
  //
  // Somar pontos de cabeça abrindo cinco cards é o trabalho que a página pode
  // fazer sozinha. O botão vive fora do <button> do cabeçalho (botão dentro de
  // botão é HTML inválido) e é criado aqui, no JS: sem script ele não existe,
  // e sem ele o card continua exatamente como era.

  var LIMIARES = [
    [1, "Leve"],
    [2, "Padrão"],
    [3, "Difícil"],
    [4, "Mortal"],
    [6, "muito além de Mortal"]
  ];

  // O mesmo encontro não vale o mesmo no nível 1 e no 12. As proporções são
  // as que a tabela de Vida por faixa já usava — só que aplicadas ao
  // orçamento, e não à Vida da criatura, pra a ficha continuar valendo.
  var FAIXAS = [[4, 1], [10, 1.8], [15, 2.7], [20, 3.7]];

  function multiplicador(nivel) {
    for (var i = 0; i < FAIXAS.length; i++) {
      if (nivel <= FAIXAS[i][0]) return FAIXAS[i][1];
    }
    return FAIXAS[FAIXAS.length - 1][1];
  }

  function dificuldade(pontos, pjs, nivel) {
    if (!pontos) return "";
    var porPj = pontos / (pjs * multiplicador(nivel));
    if (porPj < 1) return "abaixo de Leve";
    var nome = "muito além de Mortal";
    for (var i = 0; i < LIMIARES.length; i++) {
      if (porPj < LIMIARES[i][0] + 1) { nome = LIMIARES[i][1]; break; }
    }
    return nome;
  }

  function iniciaEncontro() {
    var barra = document.querySelector(".prg-filtro");
    if (!barra) return;
    var cards = Array.prototype.slice.call(
      document.querySelectorAll(".prg-card--criatura[data-ameaca]")
    ).filter(function (c) { return c.dataset.ameaca; });
    if (!cards.length || barra.querySelector(".prg-encontro")) return;

    var escolhidas = {};

    var painel = document.createElement("div");
    painel.className = "prg-encontro";
    var niveis = "";
    for (var nv = 1; nv <= 20; nv++) {
      niveis += "<option" + (nv === 1 ? " selected" : "") + ">" + nv + "</option>";
    }
    painel.innerHTML =
      '<span class="prg-encontro__resumo">Nenhuma criatura escolhida</span>' +
      '<label class="prg-encontro__pjs">para ' +
      '<select class="prg-encontro__grupo">' +
      '<option>3</option><option selected>4</option><option>5</option>' +
      '<option>6</option></select> personagens de nível ' +
      '<select class="prg-encontro__nivel">' + niveis + "</select></label>" +
      '<button type="button" class="prg-encontro__limpar">limpar</button>';
    barra.appendChild(painel);

    var resumo = painel.querySelector(".prg-encontro__resumo");
    var grupo = painel.querySelector(".prg-encontro__grupo");
    var nivel = painel.querySelector(".prg-encontro__nivel");

    function atualiza() {
      var total = 0;
      var bichos = 0;
      Object.keys(escolhidas).forEach(function (id) {
        total += escolhidas[id].pontos * escolhidas[id].qtd;
        bichos += escolhidas[id].qtd;
      });
      painel.classList.toggle("is-ativo", bichos > 0);
      if (!bichos) {
        resumo.textContent = "Nenhuma criatura escolhida";
        return;
      }
      var nv = parseInt(nivel.value, 10);
      var mult = multiplicador(nv);
      var nome = dificuldade(total, parseInt(grupo.value, 10), nv);
      resumo.innerHTML =
        "<b>" + bichos + "</b> criatura" + (bichos > 1 ? "s" : "") +
        " · <b>" + total + "</b> pontos · <b>" + nome + "</b>" +
        (mult > 1
          ? ' <span class="prg-encontro__mult">(orçamento ×' +
            String(mult).replace(".", ",") + " pela faixa de nível)</span>"
          : "");
    }

    cards.forEach(function (card) {
      var pontos = parseInt(card.dataset.ameaca, 10);
      if (!pontos) return;
      var id = card.id;

      var caixa = document.createElement("div");
      caixa.className = "prg-somar";
      caixa.innerHTML =
        '<button type="button" class="prg-somar__b" data-d="-1" ' +
        'aria-label="Tirar uma do encontro">−</button>' +
        '<span class="prg-somar__n">0</span>' +
        '<button type="button" class="prg-somar__b" data-d="1" ' +
        'aria-label="Somar uma ao encontro">+</button>';
      card.appendChild(caixa);
      var n = caixa.querySelector(".prg-somar__n");

      caixa.addEventListener("click", function (ev) {
        var b = ev.target.closest(".prg-somar__b");
        if (!b) return;
        var atual = escolhidas[id] ? escolhidas[id].qtd : 0;
        var novo = Math.max(0, atual + parseInt(b.dataset.d, 10));
        if (novo) escolhidas[id] = { qtd: novo, pontos: pontos };
        else delete escolhidas[id];
        n.textContent = novo;
        caixa.classList.toggle("is-ativo", novo > 0);
        atualiza();
      });
    });

    grupo.addEventListener("change", atualiza);
    nivel.addEventListener("change", atualiza);
    painel.querySelector(".prg-encontro__limpar").addEventListener("click", function () {
      escolhidas = {};
      cards.forEach(function (c) {
        var caixa = c.querySelector(".prg-somar");
        if (!caixa) return;
        caixa.querySelector(".prg-somar__n").textContent = "0";
        caixa.classList.remove("is-ativo");
      });
      atualiza();
    });
  }

  // A barra de filtro (.prg-filtro) gruda com `position: sticky` logo abaixo
  // do header do site — mas a altura do header muda (abas de navegação, modo
  // mobile, busca aberta), e um `top` fixo em CSS não acompanha isso. Sem essa
  // sincronia, a barra gruda alta demais e o header cobre a linha de busca.
  function ajustaOffsetFiltro() {
    var header = document.querySelector(".md-header");
    if (!header) return;
    document.documentElement.style.setProperty(
      "--prg-header-h", header.getBoundingClientRect().height + "px"
    );
  }

  // ------------------------------------------------------------- lightbox
  //
  // Imagem de conteúdo (retrato na ficha lateral de Mundo, foto de lugar no
  // corpo do texto) abre em tela cheia ao clicar. O mapa de Pania (Leaflet)
  // fica de fora: ele já tem a própria interação de zoom/arraste, e um clique
  // ali é pra abrir o popover do ponto, não a imagem de fundo inteira.

  function iniciaLightbox() {
    if (document.querySelector(".prg-lightbox")) return;
    var imagens = Array.prototype.slice
      .call(document.querySelectorAll(".md-typeset img"))
      .filter(function (img) { return !img.closest(".leaflet-container"); });
    if (!imagens.length) return;

    var overlay = document.createElement("div");
    overlay.className = "prg-lightbox";
    overlay.innerHTML =
      '<button class="prg-lightbox__fechar" type="button" aria-label="Fechar">✕</button>' +
      '<img alt="">';
    document.body.appendChild(overlay);
    var imgGrande = overlay.querySelector("img");

    function abre(img) {
      imgGrande.src = img.currentSrc || img.src;
      imgGrande.alt = img.alt || "";
      overlay.classList.add("prg-lightbox--aberta");
    }
    function fecha() {
      overlay.classList.remove("prg-lightbox--aberta");
      imgGrande.src = "";
    }

    imagens.forEach(function (img) {
      img.classList.add("prg-lightbox-abre");
      img.addEventListener("click", function () { abre(img); });
    });
    overlay.addEventListener("click", function (ev) {
      if (ev.target === overlay) fecha();
    });
    overlay.querySelector(".prg-lightbox__fechar").addEventListener("click", fecha);
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") fecha();
    });
  }

  function inicia() {
    ajustaOffsetFiltro();
    iniciaCards();
    iniciaVerbetes();
    iniciaAncoras();
    iniciaFiltro();
    iniciaEncontro();
    iniciaPopover();
    iniciaLightbox();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(inicia);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inicia);
  } else {
    inicia();
  }

  window.addEventListener("scroll", esconde, { passive: true });
  window.addEventListener("resize", ajustaOffsetFiltro, { passive: true });
})();
