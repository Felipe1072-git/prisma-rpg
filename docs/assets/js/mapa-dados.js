// Dados do mapa interativo — os pontos de Pania e Torirue.
//
// Esse arquivo é só dados (nenhuma lógica). Editado pelo modo de edição do
// mapa (botão "Editar" + "Salvar"), que reescreve ele através do
// notas/mapa_servidor.py — última gravação em 16/08/2026 12:13:16.
//
// Se preferir editar à mão: "imagem" é o caminho dentro de docs/assets/,
// "largura"/"altura" são o tamanho em pixels do arquivo de imagem, e cada
// ponto usa x/y de imagem normal (x da esquerda, y do topo).

var NIVEIS = {
  "pania": {
    "titulo": "Pania",
    "imagem": "assets/img/mapas/pania.jpg",
    "largura": 4096,
    "altura": 1669,
    "voltarPara": null,
    "pontos": [
      {
        "nome": "Torirue",
        "x": 485,
        "y": 955,
        "descricao": "Capital do Reino Humano de Poponia. Símbolo vivo da Aliança dos Três Povos — humanos, anões e elfos vivem, comerciam e lutam lado a lado ali.",
        "expande": "torirue"
      },
      {
        "nome": "Poponia",
        "x": 719,
        "y": 1150,
        "descricao": "Reino Humano."
      },
      {
        "nome": "Gorgosia",
        "x": 762,
        "y": 694
      },
      {
        "nome": "Glatenia",
        "x": 1184,
        "y": 580
      },
      {
        "nome": "Tyria",
        "x": 1186,
        "y": 910
      },
      {
        "nome": "Yan Guo",
        "x": 1505,
        "y": 130
      },
      {
        "nome": "Guang",
        "x": 1505,
        "y": 1138
      },
      {
        "nome": "Jingyuan Guo",
        "x": 1712,
        "y": 1205
      },
      {
        "nome": "Chicrid",
        "x": 2343,
        "y": 1310
      },
      {
        "nome": "Hatrinhia",
        "x": 2915,
        "y": 1425
      },
      {
        "nome": "Anri",
        "x": 1026,
        "y": 1335
      },
      {
        "nome": "Cintra",
        "x": 2906,
        "y": 436
      },
      {
        "nome": "Fronteiras de Tyria Guang",
        "x": 1328,
        "y": 948,
        "descricao": "Zona de Guerra onde Orcs e humanos lutam por território.",
        "icone": "⚔️"
      }
    ]
  },
  "torirue": {
    "titulo": "Torirue",
    "imagem": "assets/img/mapas/torirue.jpg",
    "largura": 2048,
    "altura": 1536,
    "voltarPara": "pania",
    "pontos": [
      {
        "nome": "Palácio Real",
        "x": 658,
        "y": 153
      },
      {
        "nome": "Os Jardins Suspensos",
        "x": 1051,
        "y": 270
      },
      {
        "nome": "Porto de Torirue",
        "x": 321,
        "y": 408
      },
      {
        "nome": "Museu Multirraça",
        "x": 775,
        "y": 479
      },
      {
        "nome": "Estaleiros",
        "x": 1377,
        "y": 408
      },
      {
        "nome": "Templo da Unidade",
        "x": 413,
        "y": 643
      },
      {
        "nome": "Grande Arena",
        "x": 1173,
        "y": 556,
        "descricao": "Ponto público de recrutamento pra guerra — voluntários, mercenários, batedores. Gancho de sessão 1."
      },
      {
        "nome": "O Bairro das Guildas",
        "x": 668,
        "y": 760
      },
      {
        "nome": "Guarnição de Torirue",
        "x": 1652,
        "y": 678
      },
      {
        "nome": "Mercado Central",
        "x": 1336,
        "y": 872
      },
      {
        "nome": "O Mercado das Especiarias",
        "x": 1754,
        "y": 918
      },
      {
        "nome": "Distrito Anão",
        "x": 296,
        "y": 1056
      },
      {
        "nome": "A Praça dos Artistas",
        "x": 806,
        "y": 1132
      },
      {
        "nome": "Bairro Élfico",
        "x": 138,
        "y": 1250
      }
    ]
  }
};
