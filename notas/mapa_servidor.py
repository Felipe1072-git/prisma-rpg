"""Servidorzinho local pro modo de edição do mapa interativo salvar direto em disco.

Escuta só em 127.0.0.1 (não aparece na rede), recebe POST /salvar com os
pontos do mapa em JSON, e reescreve docs/assets/js/mapa-dados.js inteiro —
é o mesmo arquivo que o build normal do site lê, então salvar aqui já é o
suficiente pra virar conteúdo real.

Um navegador não consegue ligar um programa na sua máquina sozinho (é bloqueado
por segurança em qualquer site) — então esse script também sobe o `mkdocs serve`
junto, como subprocesso, pra virar um comando só em vez de dois.

Uso:
    python notas/mapa_servidor.py
    (Ctrl+C encerra os dois — o servidor de salvar e o mkdocs serve)
"""

import json
import subprocess
import sys
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_DADOS = RAIZ / "docs" / "assets" / "js" / "mapa-dados.js"
PORTA = 8010

CABECALHO = """// Dados do mapa interativo — os pontos de Pania e Torirue.
//
// Esse arquivo é só dados (nenhuma lógica). Editado pelo modo de edição do
// mapa (botão "Editar" + "Salvar"), que reescreve ele através do
// notas/mapa_servidor.py — última gravação em {carimbo}.
//
// Se preferir editar à mão: "imagem" é o caminho dentro de docs/assets/,
// "largura"/"altura" são o tamanho em pixels do arquivo de imagem, e cada
// ponto usa x/y de imagem normal (x da esquerda, y do topo).

var NIVEIS = """


class Handler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/salvar":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return

        tamanho = int(self.headers.get("Content-Length", 0))
        corpo = self.rfile.read(tamanho)
        try:
            dados = json.loads(corpo)
            niveis = dados["niveis"]
            if not isinstance(niveis, dict):
                raise ValueError("niveis precisa ser um objeto")
        except Exception as erro:
            self.send_response(400)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"erro": str(erro)}).encode("utf-8"))
            print(f"[mapa_servidor] recusado: {erro}")
            return

        carimbo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        texto = CABECALHO.format(carimbo=carimbo) + json.dumps(niveis, indent=2, ensure_ascii=False) + ";\n"

        if ARQUIVO_DADOS.exists():
            backup = ARQUIVO_DADOS.with_suffix(".js.bak")
            backup.write_text(ARQUIVO_DADOS.read_text(encoding="utf-8"), encoding="utf-8")

        ARQUIVO_DADOS.write_text(texto, encoding="utf-8")

        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "carimbo": carimbo}).encode("utf-8"))
        print(f"[mapa_servidor] salvo em {ARQUIVO_DADOS} ({carimbo})")

    def log_message(self, format, *args):
        pass  # o print acima já basta; sem isso o console fica poluído por request


if __name__ == "__main__":
    processo_mkdocs = subprocess.Popen(
        [sys.executable, "-m", "mkdocs", "serve"],
        cwd=str(RAIZ),
    )

    servidor = HTTPServer(("127.0.0.1", PORTA), Handler)
    print(f"[mapa_servidor] escutando em http://127.0.0.1:{PORTA} — grava em {ARQUIVO_DADOS}")
    print("[mapa_servidor] mkdocs serve também subiu junto (veja a porta dele acima)")
    print("[mapa_servidor] Ctrl+C pra parar os dois")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        processo_mkdocs.terminate()
        try:
            processo_mkdocs.wait(timeout=5)
        except subprocess.TimeoutExpired:
            processo_mkdocs.kill()
