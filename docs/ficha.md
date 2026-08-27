# Ficha de Personagem

<p class="prg-ficha__intro">
Seis páginas: a ficha principal, um apêndice de Habilidades, um resumo de Como Jogar, uma Consulta Rápida (Condições, Dano & Ambiente, Atributos), uma página de Recursos (Mana, Estresse, Descanso, Exaustão) e uma de Notas. Imprima em A4 — ou abra o menu de impressão do navegador (<code>Ctrl+P</code> / <code>Cmd+P</code>) e salve como PDF. O apêndice de Habilidades é feito pra imprimir quantas cópias precisar — você ganha habilidades novas ao longo da campanha, não só as 10 do início.
</p>

<div class="prg-ficha__acoes">
  <button class="prg-ficha__botao" onclick="window.print()">Imprimir / Salvar como PDF</button>
</div>

<div class="prg-ficha">

<!-- ============================================================ PÁGINA 1 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:24px 28px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:7px; margin-bottom:12px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:22px; height:22px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:15px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Ficha de Personagem</div>
    </div>
    <div style="font-size:9px; color:#5b5343;">pág. 1 / 6</div>
  </div>

  <div style="display:grid; grid-template-columns:2.2fr 1.3fr 0.7fr; gap:12px; margin-bottom:11px; font-size:10.5px;">
    <div><div style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1px;">Nome do Personagem</div><div style="border-bottom:1px solid #cabf9f; min-height:15px;">&nbsp;</div></div>
    <div><div style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1px;">Jogador</div><div style="border-bottom:1px solid #cabf9f; min-height:15px;">&nbsp;</div></div>
    <div><div style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1px;">Nível</div><div style="border-bottom:1px solid #cabf9f; min-height:15px;">&nbsp;</div></div>
  </div>

  <div style="display:flex; align-items:baseline; gap:6px; margin-bottom:7px;">
    <span style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase;">Raça</span>
    <span style="flex:1; border-bottom:1px solid #cabf9f; font-size:10.5px; min-height:13px;">&nbsp;</span>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px 10px; margin-bottom:4px; font-size:7px; letter-spacing:0.08em; text-transform:uppercase; color:#83765a;">
    <div>Traços raciais</div><div>Origem</div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; grid-auto-rows:1fr; gap:4px; margin-bottom:14px;">
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M4 12h16"/><path d="M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Traço 1</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="m255.95 27.11-75.35 80.504 150.7 1.168-75.35-81.674h-.003zM25 109.895v68.01l19.412 25.99h71.06l19.528-26v-68h-14v15.995h-18v-15.994H89v15.995H71v-15.994H57v15.995H39v-15.994H25zm352 0v68l19.527 26h71.06L487 177.906v-68.01h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14zm-176 15.877V260.89h110V126.63l-110-.857zm55 20.118c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zM41 221.897V484.89h78V221.897H41zm352 0V484.89h78V221.897h-78zM56 241.89c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-303 37v23h-16v183h87v-55c0-24 16-36 32-36s32 12 32 36v55h87v-183h-16v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14zm-49 43c4 0 8 4 8 12v32H96v-32c0-8 4-12 8-12zm72 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm72 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-352 64c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12z"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Passado</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M4 12h16"/><path d="M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Traço 2</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="m255.95 27.11-75.35 80.504 150.7 1.168-75.35-81.674h-.003zM25 109.895v68.01l19.412 25.99h71.06l19.528-26v-68h-14v15.995h-18v-15.994H89v15.995H71v-15.994H57v15.995H39v-15.994H25zm352 0v68l19.527 26h71.06L487 177.906v-68.01h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14zm-176 15.877V260.89h110V126.63l-110-.857zm55 20.118c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zM41 221.897V484.89h78V221.897H41zm352 0V484.89h78V221.897h-78zM56 241.89c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-303 37v23h-16v183h87v-55c0-24 16-36 32-36s32 12 32 36v55h87v-183h-16v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14zm-49 43c4 0 8 4 8 12v32H96v-32c0-8 4-12 8-12zm72 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm72 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-352 64c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12z"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Ambiente</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M4 12h16"/><path d="M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Traço 3</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
    <div style="position:relative; border:1px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; display:flex; flex-direction:column;">
      <div style="position:absolute; top:5px; right:5px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="m255.95 27.11-75.35 80.504 150.7 1.168-75.35-81.674h-.003zM25 109.895v68.01l19.412 25.99h71.06l19.528-26v-68h-14v15.995h-18v-15.994H89v15.995H71v-15.994H57v15.995H39v-15.994H25zm352 0v68l19.527 26h71.06L487 177.906v-68.01h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14v15.995h-18v-15.994h-14zm-176 15.877V260.89h110V126.63l-110-.857zm55 20.118c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zM41 221.897V484.89h78V221.897H41zm352 0V484.89h78V221.897h-78zM56 241.89c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-303 37v23h-16v183h87v-55c0-24 16-36 32-36s32 12 32 36v55h87v-183h-16v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14v23h-18v-23h-14zm-49 43c4 0 8 4 8 12v32H96v-32c0-8 4-12 8-12zm72 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm80 0c8 0 16 4 16 12v32h-32v-32c0-8 8-12 16-12zm72 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12zm-352 64c4 0 8 4 8 12v32H48v-32c0-8 4-12 8-12zm400 0c4 0 8 4 8 12v32h-16v-32c0-8 4-12 8-12z"/></svg></div>
      <div style="background:#159c56; color:#faf7ef; font-size:7px; letter-spacing:0.06em; text-transform:uppercase; padding:2px 6px; min-height:16px; box-sizing:border-box; display:flex; align-items:center;">Evento Formador</div>
      <div style="padding:2px 6px 3px; flex:1;"><div style="font-size:5.5px; color:#5b5343; text-transform:uppercase;">Efeito</div><div style="font-size:7.5px; min-height:12px;">&nbsp;</div></div>
    </div>
  </div>

  <div style="font-size:9.5px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#83765a; margin-bottom:5px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Atributos
  </div>
  <div style="display:grid; grid-template-columns:repeat(8,1fr); gap:6px; margin-bottom:12px;">
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #b8502e; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#b8502e; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:8px; height:8px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M45.95 14.553c-19.38.81-30.594 11.357-30.282 30.283l19.768 30.78c4.43-1.213 9.36-3.838 14.248-7.335l42.474 59.935c-17.018 20.83-31.258 44.44-42.71 70.836l26.55 26.552c11.275-23.6 24.634-44.826 39.918-63.864l210.82 297.475 166.807 33.213L460.33 325.62 162.78 114.745c19.907-16.108 41.842-29.91 65.652-41.578l-26.553-26.55c-27.206 11.803-51.442 26.576-72.735 44.292L69.39 48.56c3.443-4.823 6.062-9.735 7.342-14.242l-30.78-19.765zm400.84 86.933v.008l.003-.008h-.002zm0 .008-28.028 124.97-25.116-80.593-18.105 70.667-26.862-49.64-.584 57.818 128.484 91.69 15.184 87.017-1.168-186.885-34.457 39.713-9.346-154.756zm-300.95 27.98 222.224 196.368 25.645 66.75-66.75-25.645L130.6 144.734a308.453 308.453 0 0 1 15.238-15.26zm32.305 196.274v.004h.005l-.005-.004zm.005.004 28.028 22.775-36.21 4.088 57.82 19.272-105.706 4.09 115.05 27.45L136.1 422.114l127.316 25.696-67.164 43.803 208.494 1.752-87.017-15.185-104.54-150.676-35.037-1.752z"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#b8502e; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Ataque</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #a3781a; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#a3781a; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 5-3.5 8-7 9-3.5-1-7-4-7-9V6z"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#a3781a; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Defesa</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #4c7a3d; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#4c7a3d; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 15c4-7 13-7 17-7"/><path d="M15 4l5 4-5 4"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#4c7a3d; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Agilidade</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #3f5fa0; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#3f5fa0; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="14" r="6.5"/><path d="M18 1 L19.5 4.5 L23 6 L19.5 7.5 L18 11 L16.5 7.5 L13 6 L16.5 4.5 Z" fill="currentColor" stroke="none"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#3f5fa0; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Magia</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #a04570; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#a04570; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v12H9l-5 4z"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#a04570; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Social</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #2d7a6e; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#2d7a6e; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15 9l-2 6-6 2 2-6z"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#2d7a6e; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Exploração</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #b39422; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#b39422; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="3"/><circle cx="8.5" cy="8.5" r="1" fill="currentColor" stroke="none"/><circle cx="15.5" cy="8.5" r="1" fill="currentColor" stroke="none"/><circle cx="8.5" cy="15.5" r="1" fill="currentColor" stroke="none"/><circle cx="15.5" cy="15.5" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#b39422; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Sorte</div>
    </div>
    <div style="position:relative; clip-path:polygon(7px 0,100% 0,100% calc(100% - 7px),calc(100% - 7px) 100%,0 100%,0 7px); border:1.4px solid #6a3fa0; background:#f1ebdc; text-align:center; padding:5px 0 4px;">
      <div style="position:absolute; top:4px; right:4px; width:13px; height:13px; background:#6a3fa0; border:1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:7px; height:7px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13h4l2-7 4 14 2-7h6"/></svg></div>
      <div style="font-size:16px; font-weight:700; color:#6a3fa0; line-height:1;">&nbsp;</div><div style="font-size:6.2px; letter-spacing:0.01em; color:#5b5343; margin-top:3px; text-transform:uppercase; line-height:1.05; min-height:13px; display:flex; align-items:center; justify-content:center;">Sanidade</div>
    </div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:5px;">
    <div style="font-size:9.5px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#83765a; display:flex; align-items:center; gap:5px;">
      <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Recursos
    </div>
    <div style="font-size:7.5px; color:#5b5343;">descanso curto recupera metade · descanso longo recupera tudo</div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-bottom:2px;">
    <div style="position:relative; clip-path:polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px); border:1.4px solid #a3781a; background:#f1ebdc;">
      <div style="position:absolute; top:5px; right:5px; width:17px; height:17px; background:#a3781a; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-8-5.5-8-11a5 5 0 0 1 8-3.9A5 5 0 0 1 20 10c0 5.5-8 11-8 11z"/></svg></div>
      <div style="font-size:10.5px; font-weight:700; color:#a3781a; letter-spacing:0.08em; text-transform:uppercase; text-align:center; padding:4px 0 3px; border-bottom:1px solid #cabf9f;">Vida</div>
      <div style="display:flex;"><div style="flex:1; text-align:center; padding:5px 0 6px; border-right:1px solid #cabf9f;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Atual</div><div style="font-size:16px; font-weight:700; min-height:19px;">&nbsp;</div></div><div style="flex:1; text-align:center; padding:5px 0 6px;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Máx</div><div style="font-size:16px; font-weight:700; color:#a3781a;">&nbsp;</div></div></div>
    </div>
    <div style="position:relative; clip-path:polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px); border:1.4px solid #3f5fa0; background:#f1ebdc;">
      <div style="position:absolute; top:5px; right:5px; width:17px; height:17px; background:#3f5fa0; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2c4 5 7 9 7 12a7 7 0 0 1-14 0c0-3 3-7 7-12z"/></svg></div>
      <div style="font-size:10.5px; font-weight:700; color:#3f5fa0; letter-spacing:0.08em; text-transform:uppercase; text-align:center; padding:4px 0 3px; border-bottom:1px solid #cabf9f;">Mana</div>
      <div style="display:flex;"><div style="flex:1; text-align:center; padding:5px 0 6px; border-right:1px solid #cabf9f;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Atual</div><div style="font-size:16px; font-weight:700; min-height:19px;">&nbsp;</div></div><div style="flex:1; text-align:center; padding:5px 0 6px;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Máx</div><div style="font-size:16px; font-weight:700; color:#3f5fa0;">&nbsp;</div></div></div>
    </div>
    <div style="position:relative; clip-path:polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px); border:1.4px solid #6a3fa0; background:#f1ebdc;">
      <div style="position:absolute; top:5px; right:5px; width:17px; height:17px; background:#6a3fa0; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="14" r="7"/><path d="M7 9c1-2 3-3 5-3s4 1 5 3"/><path d="M13 10l-2 4h3l-2 4"/></svg></div>
      <div style="font-size:10.5px; font-weight:700; color:#6a3fa0; letter-spacing:0.08em; text-transform:uppercase; text-align:center; padding:4px 0 3px; border-bottom:1px solid #cabf9f;">Estresse</div>
      <div style="display:flex;"><div style="flex:1; text-align:center; padding:5px 0 6px; border-right:1px solid #cabf9f;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Atual</div><div style="font-size:16px; font-weight:700; min-height:19px;">&nbsp;</div></div><div style="flex:1; text-align:center; padding:5px 0 6px;"><div style="font-size:6.5px; letter-spacing:0.06em; color:#5b5343; text-transform:uppercase;">Máx</div><div style="font-size:16px; font-weight:700; color:#6a3fa0;">&nbsp;</div></div></div>
    </div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-bottom:11px;">
    <div style="font-size:6.8px; color:#5b5343; font-style:italic; text-align:center;">20 + Nível + (Defesa × 2)</div>
    <div style="font-size:6.8px; color:#5b5343; font-style:italic; text-align:center;">20 + Nível + (Magia × 2)</div>
    <div style="font-size:6.8px; color:#5b5343; font-style:italic; text-align:center;">20 + Nível + (Sanidade × 2)</div>
  </div>

  <div style="font-size:9.5px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#83765a; margin-bottom:5px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Defesa &amp; Combate
  </div>
  <div style="display:grid; grid-template-columns:repeat(5,1fr); gap:6px; margin-bottom:5px;">
    <div style="position:relative; border:1.2px solid #4c7a3d; border-radius:3px; text-align:center; padding:4px 0;">
      <div style="position:absolute; top:5px; right:5px; width:15px; height:15px; background:#4c7a3d; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6l6 6-6 6"/><path d="M11 6l6 6-6 6"/></svg></div>
      <div style="font-size:6.3px; color:#4c7a3d; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Evasão</div><div style="font-size:13px; font-weight:700; margin:2px 0;">&nbsp;</div><div style="font-size:5.5px; color:#5b5343;">Agi+Escudo/Couraça</div>
    </div>
    <div style="position:relative; border:1.2px solid #83765a; border-radius:3px; text-align:center; padding:4px 0; background:linear-gradient(90deg,#4c7a3d22,#b3942222);">
      <div style="position:absolute; top:5px; right:5px; width:15px; height:15px; background:#5b5343; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg></div>
      <div style="font-size:6.3px; color:#5b5343; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Iniciativa</div><div style="font-size:13px; font-weight:700; margin:2px 0;">&nbsp;</div><div style="font-size:5.5px;"><span style="color:#4c7a3d;">Agi</span>+<span style="color:#b39422;">Sorte</span></div>
    </div>
    <div style="position:relative; border:1.2px solid #4c7a3d; border-radius:3px; text-align:center; padding:4px 0;">
      <div style="position:absolute; top:5px; right:5px; width:15px; height:15px; background:#4c7a3d; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h13M13 6l6 6-6 6"/></svg></div>
      <div style="font-size:6.3px; color:#4c7a3d; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Movimento</div><div style="font-size:13px; font-weight:700; margin:2px 0;">&nbsp;</div><div style="font-size:5.5px; color:#5b5343;">6+Agi÷10</div>
    </div>
    <div style="position:relative; border:1.2px solid #b39422; border-radius:3px; text-align:center; padding:4px 0;">
      <div style="position:absolute; top:5px; right:5px; width:15px; height:15px; background:#b39422; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5M20 4v5h-5"/><path d="M20 12a8 8 0 0 1-14 5M4 20v-5h5"/></svg></div>
      <div style="font-size:6.3px; color:#b39422; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Rerolagens</div><div style="font-size:13px; font-weight:700; margin:2px 0;">&nbsp;</div><div style="font-size:5.5px; color:#5b5343;">1+Sorte÷10/desc.</div>
    </div>
    <div style="position:relative; border:1.2px solid #b39422; border-radius:3px; text-align:center; padding:4px 0;">
      <div style="position:absolute; top:5px; right:5px; width:15px; height:15px; background:#b39422; border:1.1px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:9px; height:9px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg></div>
      <div style="font-size:6.3px; color:#b39422; font-weight:700; letter-spacing:0.04em; text-transform:uppercase;">Lim. Crítico</div><div style="font-size:13px; font-weight:700; margin:2px 0;">&nbsp;</div><div style="font-size:5.5px; color:#5b5343;">Sorte÷3</div>
    </div>
  </div>
  <div style="font-size:9.5px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#83765a; margin-bottom:5px; margin-top:6px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Equipado
  </div>
  <div style="display:grid; grid-template-columns:repeat(4,1fr); grid-auto-rows:1fr; gap:8px; flex:1;">

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:13px; height:13px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M43.53 15.75c-15.73 0-28.31 12.583-28.31 28.313 0 14.086 10.092 25.644 23.5 27.906L42.687 68 68.81 41.906l2.626-2.625C69.188 25.86 57.63 15.75 43.53 15.75zm33.72 44.125-17 17c15.885 39.37 43.45 66.684 78.75 87.406a512.629 512.629 0 0 1 25.438-24.936c-22.488-35.103-51.535-62.294-87.188-79.47zM322.594 79.03l-51.25 4.314c-79.356 48.134-143.878 108.1-186.72 186.53l-4.31 51.47 44.155-18.656-2.94-34.094-.25-3.063 1.626-2.624c35.94-58.47 79.93-109.41 141.5-141.25l2.406-1.25 2.688.25 34.125 2.906 18.97-44.53zm-62.438 66.376c-10.008 5.886-19.5 12.338-28.562 19.313 46.688 47.93 87.208 108.588 114.72 166.5l11.248 23.717-23.718-11.28c-57.995-27.554-117.918-67.57-165.688-113.907a497.06 497.06 0 0 0-20.625 29.28c101.918 94.91 227.05 177.304 347.845 234.69-57.063-120.125-140.038-246.18-235.22-348.314zm-43.03 31.22c-13.37 11.703-25.72 24.58-37.282 38.436 39.36 38.452 88.085 72.83 136.687 98.844-26.054-48.633-60.754-97.847-99.405-137.28z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Arma</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; border-right:1px solid #cabf9f; color:#5b5343;">Dano</div><div style="flex:1; padding:2px 5px; color:#5b5343;">Atrib.</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Técnicas</div>
        <div style="display:flex; flex-direction:column; gap:2px; flex:1;">
          <div style="display:flex; gap:3px; align-items:baseline;"><span style="font-size:5.8px; color:#159c56; width:28px; flex-shrink:0;">Básica</span><span style="flex:1; border-bottom:1px dotted #cabf9f;">&nbsp;</span></div>
          <div style="display:flex; gap:3px; align-items:baseline;"><span style="font-size:5.8px; color:#159c56; width:28px; flex-shrink:0;">Avanç.</span><span style="flex:1; border-bottom:1px dotted #cabf9f;">&nbsp;</span></div>
          <div style="display:flex; gap:3px; align-items:baseline;"><span style="font-size:5.8px; color:#159c56; width:28px; flex-shrink:0;">Espec.</span><span style="flex:1; border-bottom:1px dotted #cabf9f;">&nbsp;</span></div>
        </div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:12px; height:12px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 5-3.5 8-7 9-3.5-1-7-4-7-9V6z"/><path d="M12 8v8M8.5 10l7 4M15.5 10l-7 4"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Escudo</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Evasão +</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Habilidade</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:12px; height:12px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M260.22 21.75c-35.407 0-63.024 5.19-82.345 12.844-9.66 3.827-17.072 8.22-22.78 13.437-2.856 2.61-5.355 5.53-7.126 8.75-20.707 18.986-35.955 48.755-45.845 81.72-9.45 31.5-13.837 66.035-11.47 97.563-1.78 22.768 10.688 55.117 24.97 81.03l.063.126.03.03c33.913 34.964 83.458 60.827 135.313 67.563V129.625c3.036.106 6.094.188 9.19.188 3.204 0 6.36-.088 9.5-.22v254.97c61.97-8.614 120.527-44.526 152.592-90.188 6.31-18.61 9.023-38.46 7.344-54.875 2.966-32.438-1.393-68.354-11.187-101-9.96-33.2-25.327-63.16-46.25-82.125-1.754-3.06-4.144-5.847-6.876-8.344-5.71-5.217-13.12-9.61-22.78-13.436-19.323-7.653-46.94-12.844-82.345-12.844zm0 18.688c33.573 0 59.057 5.236 75.342 11.687 8.143 3.224 14.168 6.298 17.5 9.344 3.333 3.043 3.5 5.482 3.5 5.843 0 10.54-8.305 21.148-25.687 29.78-17.382 8.633-42.673 14.032-70.656 14.032-28.098 0-53.343-5.08-70.658-13.438-17.314-8.355-25.718-18.457-25.718-30.374 0-.36.76-2.8 4.094-5.844 3.332-3.047 8.794-6.12 16.937-9.345 16.285-6.45 41.77-11.688 75.344-11.688zm111.374 43.25c11.81 15.68 21.998 36.85 29 60.187 7.59 25.3 11.598 53.038 11.22 78.625-16.25-13.403-28.542-34.667-36.627-57.406-8.665-24.372-12.573-51-8.03-73.844a45.597 45.597 0 0 0 4.437-7.563zm-222.875.374a44.406 44.406 0 0 0 1.874 3.813c5.502 25.973.96 54.837-8.875 80.25-7.943 20.52-19.176 39.02-32.97 51.75-.08-24.852 3.918-51.563 11.25-76 6.946-23.153 17.027-44.17 28.72-59.813zm242.06 269.344c-36.57 28.03-82.68 46.99-130.56 51.063l-.783.06-.812-.06c-47.334-4.036-92.797-22.698-129.125-50.19-.956 3.05-1.438 6.11-1.438 9.158 0 15.545 12.548 31.48 36.438 43.937 23.89 12.458 58.006 20.563 95.78 20.563 37.777 0 71.893-8.105 95.783-20.563 23.89-12.458 36.437-28.392 36.437-43.938 0-3.338-.573-6.697-1.72-10.03zm-275.655 33.28c-17.37 12.854-26.563 27.47-26.563 41.845 0 11.535 10.293 29.294 26.157 43.095 14.044 12.22 31.883 21.216 47.31 23.125 9.7-22.68 20.252-41.555 31.657-56.438-13.913-3.702-26.666-8.546-37.843-14.375-18.425-9.608-33.094-22.287-40.72-37.25zm290.28.095c-7.636 14.925-22.297 27.568-40.686 37.158-11.228 5.854-24.048 10.697-38.033 14.406 11.398 14.872 21.96 33.744 31.657 56.375 14.686-1.997 32.556-10.938 46.72-23.095 16.113-13.833 26.748-31.68 26.748-43.094 0-14.332-9.13-28.923-26.406-41.75z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Armadura</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Vida +</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Habilidade</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:13px; height:13px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M255.406 17.75C189.313 39.42 124.536 85.124 79.03 150.344c21.238 57.44 32.72 94.314 32.72 131.375 0 36.493-11.52 73.723-32.125 129.655 49.72 36.73 100.08 58.95 150.313 64.938-5.052-60.378-9.83-120.748 1.593-181.125-30.644-3.28-61.384-13.286-92.03-30.72v-71.312c80.67 42.255 158.908 41.547 242.063 0v71.313c-30.06 14.376-60.192 24.722-90.25 29.28 8.684 60.46 7.723 120.915 2.03 181.375 46.386-7.335 92.89-28.824 139.032-64.312-33.966-112.954-34.03-145.933.594-260.47C391.162 84.844 317.924 39.89 255.405 17.75zm-75.125 212c-11.16-.13-19.646 3.174-21.25 9.156-2.33 8.7 10.778 19.76 29.282 24.72 18.505 4.957 35.388 1.92 37.72-6.782 2.33-8.7-10.775-19.76-29.282-24.72-5.783-1.55-11.396-2.315-16.47-2.374zm160.69 0c-5.074.06-10.687.825-16.47 2.375-18.507 4.96-31.613 16.018-29.28 24.72 2.33 8.7 19.213 11.738 37.717 6.78 18.505-4.958 31.613-16.018 29.282-24.72-1.604-5.98-10.09-9.286-21.25-9.155z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Elmo</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Bônus</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Efeito</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 24 24" style="width:12px; height:12px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5a9 9 0 0 0 14 0"/><path d="M12 12l-2.5 3.5L12 19l2.5-3.5z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Colar</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Bônus</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Efeito</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:13px; height:13px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M201.837 53.087 177.547 21h55.676zM278.766 21l30.82 31.465L333.065 21h-54.298zm12.428 38.12L256 23.18l-35.25 35.985h70.5zm82.091 0-23.511-30.855-23.003 30.9h46.57zM161.096 28.683 138.5 59.188h45.746zm51.248 48.242L256 196.821l43.69-119.896h-87.38zm-73.166 0 90.384 99.017-36.153-99.017h-54.231zm233.712 0h-54.23l-36.076 99.017zm-19.455 48.142-29.059 31.838a154.298 154.298 0 0 1 85.786 138.119C410.14 380.008 340.995 449.197 256 449.197s-154.14-69.144-154.14-154.14a154.298 154.298 0 0 1 85.787-138.119L158.588 125.1a196.044 196.044 0 0 0-98.53 169.924C60.057 403.056 147.955 491 256 491c108.044 0 195.943-87.899 195.943-195.943a196.044 196.044 0 0 0-98.542-169.99z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Anel 1</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Bônus</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Efeito</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:13px; height:13px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M201.837 53.087 177.547 21h55.676zM278.766 21l30.82 31.465L333.065 21h-54.298zm12.428 38.12L256 23.18l-35.25 35.985h70.5zm82.091 0-23.511-30.855-23.003 30.9h46.57zM161.096 28.683 138.5 59.188h45.746zm51.248 48.242L256 196.821l43.69-119.896h-87.38zm-73.166 0 90.384 99.017-36.153-99.017h-54.231zm233.712 0h-54.23l-36.076 99.017zm-19.455 48.142-29.059 31.838a154.298 154.298 0 0 1 85.786 138.119C410.14 380.008 340.995 449.197 256 449.197s-154.14-69.144-154.14-154.14a154.298 154.298 0 0 1 85.787-138.119L158.588 125.1a196.044 196.044 0 0 0-98.53 169.924C60.057 403.056 147.955 491 256 491c108.044 0 195.943-87.899 195.943-195.943a196.044 196.044 0 0 0-98.542-169.99z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Anel 2</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Bônus</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Efeito</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; font-size:7.8px; display:flex; flex-direction:column;">
      <div style="position:absolute; top:6px; right:6px; width:20px; height:20px; background:#159c56; border:1.3px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);"><svg viewBox="0 0 512 512" style="width:13px; height:13px; transform:rotate(-45deg); color:#faf7ef;" fill="currentColor"><path d="M173.438 56.625c-24.197.254-51.41 8.524-76.125 23.875C56.04 106.135 22.91 150.185 21.5 204.813c23.035 23.153 37.246 53.802 48.72 86.312 37.776-75.574 103.61-112.37 154.28-109.22-12.233-36.11-9.912-77.263-10.344-115.968-10.255-5.718-22.525-8.79-35.906-9.25-1.585-.054-3.2-.08-4.813-.062zm42.78 144c-36.993 1.83-87.634 28.563-121.218 84.094 25.173 56.788 58.682 115.636 94.688 155.25 30.954-10.902 72.793-30.752 113.093-54.408-19.64-45.728-15.747-92.128 1.595-128.812-9.745.435-18.834-.526-27.313-2.906-2.768-.777-5.445-1.726-8.062-2.78l.375.655c-5.122 2.997-12.668 10.257-18.813 19.03-6.144 8.773-11.073 19.095-12.75 27.688l-18.343-3.563c2.4-12.312 8.46-24.392 15.78-34.844 5.023-7.17 10.564-13.568 16.438-18.56-5.982-4.3-11.545-9.33-16.688-15.032-19.934 9.052-40.194 31.397-43.313 50.156l-18.437-3.063c4.4-26.468 25.81-49.992 49.938-62.155-2.39-3.44-4.697-7.03-6.97-10.75zm185.813 2.78c-.733.002-1.483.004-2.217.032-11.748.45-23.438 4.37-34.625 11.063-44.48 26.61-76.574 99.088-42.72 169.563l7.25 7.25-10.25 6.156c-46.5 27.946-95.11 51.027-130.75 62.53l12.345 17.875c92.26-33.88 212.588-103.56 290.843-165.78-13.427-54.603-34.915-85.3-57.062-99-10.753-6.654-21.793-9.703-32.813-9.69z"/></svg></div>
      <div style="padding:4px 6px; background:#159c56; color:#faf7ef;">Botas</div>
      <div style="padding:3px 5px 2px; min-height:10px; border-bottom:1px solid #cabf9f;">&nbsp;</div>
      <div style="display:flex; border-bottom:1px solid #cabf9f; font-size:6.6px;"><div style="flex:1; padding:2px 5px; color:#159c56;">Bônus</div></div>
      <div style="padding:3px 5px; flex:1; display:flex; flex-direction:column;">
        <div style="font-size:5.8px; letter-spacing:0.05em; color:#5b5343; text-transform:uppercase; margin-bottom:2px;">Efeito</div>
        <div style="flex:1;">&nbsp;</div>
      </div>
    </div>

  </div>

  <div style="margin-top:8px; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

<!-- ============================================================ PÁGINA 2 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:24px 28px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:7px; margin-bottom:9px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:20px; height:20px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:14px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Apêndice de Habilidades</div>
    </div>
    <div style="font-size:9px; color:#5b5343;">pág. 2 / 6</div>
  </div>

  <p style="font-size:8.5px; color:#5b5343; font-style:italic; margin:0 0 8px;">Imprima quantas vezes precisar — cada cópia guarda mais Habilidades conforme você ganha ao longo da campanha.</p>

  <div style="display:grid; grid-template-columns:2fr 1fr; gap:12px; margin-bottom:10px; font-size:10.5px;">
    <div><div style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1px;">Nome do Personagem</div><div style="border-bottom:1px solid #cabf9f; min-height:14px;">&nbsp;</div></div>
    <div><div style="color:#83765a; font-size:8px; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:1px;">Nível</div><div style="border-bottom:1px solid #cabf9f; min-height:14px;">&nbsp;</div></div>
  </div>

  <div style="font-size:9.5px; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#83765a; margin-bottom:6px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Habilidades
  </div>

  <div style="display:flex; flex-direction:column; gap:4px; flex:1;">

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; flex:1; display:flex; flex-direction:column;">
      <span style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg>
      </span>
      <div style="padding:4px 34px 2px 8px;">
        <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em;">Nome</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:11px; font-size:10px;">&nbsp;</div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Chave<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Atributo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Dano<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alvos<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alcance<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Área<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Duração<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Componentes<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Cooldown<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Vs<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Escala<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:2px 8px 1px;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Custo</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Intensidade</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Custo Fixo</label>
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 34px;">Ação</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ação</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Reação <span style="color:#83765a; font-size:5.7px;">(máx. 1×/rodada)</span></label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Passiva</label>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:1px 8px 2px; border-bottom:1.2px solid #83765a;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Resolução</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ataque</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Teste de Resistência</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Automática</label>
      </div>
      <div style="padding:5px 8px 5px; display:flex; flex-direction:column; justify-content:space-evenly; flex:1;">
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Efeito</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade I</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade II</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade III</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#7ec19e;">Crítico</span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; flex:1; display:flex; flex-direction:column;">
      <span style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg>
      </span>
      <div style="padding:4px 34px 2px 8px;">
        <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em;">Nome</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:11px; font-size:10px;">&nbsp;</div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Chave<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Atributo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Dano<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alvos<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alcance<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Área<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Duração<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Componentes<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Cooldown<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Vs<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Escala<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:2px 8px 1px;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Custo</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Intensidade</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Custo Fixo</label>
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 34px;">Ação</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ação</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Reação <span style="color:#83765a; font-size:5.7px;">(máx. 1×/rodada)</span></label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Passiva</label>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:1px 8px 2px; border-bottom:1.2px solid #83765a;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Resolução</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ataque</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Teste de Resistência</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Automática</label>
      </div>
      <div style="padding:5px 8px 5px; display:flex; flex-direction:column; justify-content:space-evenly; flex:1;">
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Efeito</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade I</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade II</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade III</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#7ec19e;">Crítico</span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
      </div>
    </div>
    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; flex:1; display:flex; flex-direction:column;">
      <span style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg>
      </span>
      <div style="padding:4px 34px 2px 8px;">
        <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em;">Nome</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:11px; font-size:10px;">&nbsp;</div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Chave<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Atributo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Dano<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alvos<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alcance<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Área<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Duração<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Componentes<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Cooldown<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Vs<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Escala<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:2px 8px 1px;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Custo</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Intensidade</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Custo Fixo</label>
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 34px;">Ação</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ação</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Reação <span style="color:#83765a; font-size:5.7px;">(máx. 1×/rodada)</span></label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Passiva</label>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:1px 8px 2px; border-bottom:1.2px solid #83765a;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Resolução</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ataque</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Teste de Resistência</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Automática</label>
      </div>
      <div style="padding:5px 8px 5px; display:flex; flex-direction:column; justify-content:space-evenly; flex:1;">
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Efeito</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade I</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade II</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade III</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#7ec19e;">Crítico</span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; flex:1; display:flex; flex-direction:column;">
      <span style="position:absolute; top:6px; right:6px; width:18px; height:18px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:11px; height:11px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2 14 10 22 12 14 14 12 22 10 14 2 12 10 10z"/></svg>
      </span>
      <div style="padding:4px 34px 2px 8px;">
        <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em;">Nome</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:11px; font-size:10px;">&nbsp;</div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Chave<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Atributo<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Dano<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alvos<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Alcance<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Área<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; gap:8px; padding:2px 8px; font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em;">
        <div style="flex:1.3;">Duração<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Componentes<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Cooldown<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Vs<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
        <div style="flex:1;">Escala<div style="border-bottom:1px solid #cabf9f; min-height:9px; color:#211c14; font-size:8.5px; text-transform:none;">&nbsp;</div></div>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:2px 8px 1px;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Custo</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Intensidade</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Custo Fixo</label>
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 34px;">Ação</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ação</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Reação <span style="color:#83765a; font-size:5.7px;">(máx. 1×/rodada)</span></label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Passiva</label>
      </div>
      <div style="display:flex; align-items:center; gap:7px; padding:1px 8px 2px; border-bottom:1.2px solid #83765a;">
        <span style="font-size:6.1px; color:#83765a; text-transform:uppercase; letter-spacing:0.04em; flex:0 0 48px;">Resolução</span>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Ataque</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Teste de Resistência</label>
        <label style="display:flex; align-items:center; gap:2px; font-size:6.5px;"><span style="width:6px; height:6px; border:1.1px solid #159c56; display:inline-block;"></span>Automática</label>
      </div>
      <div style="padding:5px 8px 5px; display:flex; flex-direction:column; justify-content:space-evenly; flex:1;">
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Efeito</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade I</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade II</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#159c56;">Intensidade III</span>
          <span style="flex:0 0 24px; display:flex; gap:2px;"><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg><svg viewBox="0 0 10 10" style="width:6px;height:6px;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="none" stroke="#159c56" stroke-width="1.1"/></svg></span>
          <span style="flex:0 0 38px; font-size:6px; color:#83765a; display:flex; align-items:baseline; gap:2px;">Mana<span style="flex:1; border-bottom:1px solid #cabf9f; min-height:8px;">&nbsp;</span></span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
        <div style="display:flex; align-items:baseline; gap:5px;">
          <span style="flex:0 0 60px; font-size:6.6px; font-weight:700; color:#7ec19e;">Crítico</span>
          <span style="flex:1; border-bottom:1px dotted #cabf9f; min-height:9px;">&nbsp;</span>
        </div>
      </div>
    </div>

  </div>

  <div style="margin-top:8px; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

<!-- ============================================================ PÁGINA 3 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:16.5px 26px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:6px; margin-bottom:7.2px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:19px; height:19px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:13.5px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Como Jogar</div>
    </div>
    <div style="font-size:8.5px; color:#5b5343;">pág. 3 / 6</div>
  </div>

  <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px; margin-bottom:6.4px;">
    <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">O teste básico</div>
    <div style="font-size:9px; line-height:1.35;"><b>d100 + Atributo vs Dificuldade</b> — role 1d100, some o Atributo indicado, e compare. Igualou ou superou, é sucesso. <span style="color:#5b5343;">Contra uma Habilidade, a Dificuldade vira o número-alvo do defensor (tabela abaixo).</span></div>
  </div>

  <div style="display:flex; gap:8px; margin-bottom:6.4px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Vantagem / Desvantagem</div>
      <div style="font-size:8.2px; line-height:1.35;">Role <b>2d100</b> e use o melhor (Vantagem) ou o pior (Desvantagem). Se as duas se aplicam, cancelam — rola 1d100 normal.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Crítico</div>
      <div style="font-size:8.2px; line-height:1.35;"><b>Limiar = Sorte ÷ 3</b> (arred.). Se o d100 puro cair nele ou abaixo: sucesso automático, dano máximo + rolagem extra, e sobe 1 Intensidade de graça.</div>
    </div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:3.2px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>O turno — 3 Pontos de Ação (◈◈◈)
  </div>
  <div style="font-size:8px; line-height:1.4; margin-bottom:4px;">Mover, Ação Básica e Ataque Básico custam <b>◈ (1)</b> cada. Uma Habilidade custa a Intensidade escolhida — o que ela <i>entrega</i>, não o quanto o dado acerta:</div>
  <table style="width:100%; border-collapse:collapse; font-size:7.4px; margin-bottom:6.4px;">
    <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Intensidade</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">PA</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Entrega</th></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">I</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">◈</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Efeito base — normalmente só o dano</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">II</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">◈◈</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">+ efeito secundário (empurrar, Sangrando, Marcado)</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">III</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">◈◈◈</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Efeito completo (derrubar, Atordoado)</td></tr>
  </table>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:3.2px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Quem rola, e contra o quê
  </div>
  <div style="font-size:8px; line-height:1.4; margin-bottom:4px;">Depende da <b>Resolução</b> da Habilidade. Em <b>Ataque</b>, <b>você</b> rola d100 + Atributo contra o número-alvo do alvo, que não rola nada. Em <b>Teste de Resistência</b> — toda área, e todo efeito que o corpo aguenta por dentro — é o <b>alvo</b> quem rola, contra o seu Atributo cru: igualou ou superou, sofre metade do dano e nenhuma condição (e escapa por completo se o d100 puro dele cair no próprio limiar de Crítico).</div>
  <table style="width:100%; border-collapse:collapse; font-size:7.2px; margin-bottom:6.4px;">
    <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Tipo de efeito</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Número-alvo</th></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Físico (dano, empurrar, derrubar)</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#a3781a; font-weight:700;">Evasão</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Controle mental mágico, maldição, petrificação</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#3f5fa0; font-weight:700;">Fortitude Mágica (Magia)</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Persuadir, enganar, intimidar</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#a04570; font-weight:700;">Social</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Veneno, doença, exaustão</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#a3781a; font-weight:700;">Fortitude Física (Defesa)</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Horror, insanidade, colapso mental</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#6a3fa0; font-weight:700;">Sanidade</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Furtividade, detecção</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#2d7a6e; font-weight:700;">Exploração</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;"><i>Área, ou efeito de que não se esquiva</i></td><td style="border:1px solid #cabf9f; padding:1.5px 5px; color:#b8502e; font-weight:700;">o <i>alvo</i> rola, contra o seu Atributo cru</td></tr>
  </table>

  <div style="display:flex; gap:8px; margin-bottom:4.8px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Movimento</div>
      <div style="font-size:8px; line-height:1.35;"><b>6 + (Agilidade ÷ 10)</b> casas, mínimo 1. Terreno Difícil custa o dobro por casa. Voo usa o mesmo Movimento, em 3 dimensões.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Reações</div>
      <div style="font-size:7.3px; line-height:1.32;"><b>Limite: 1 Reação por rodada</b>, sempre — não importa quanto ◈ sobrou. Pra reagir com uma Habilidade comum, ainda precisa ter ◈ sobrando do turno anterior; a <b>dedicada a Reação</b> custa 0 PA — só Mana.<br><b>Ataque de Oportunidade:</b> quem <i>deixa</i> o alcance corpo a corpo de alguém leva um Ataque Básico — e gasta a Reação de quem ficou. Empurrar, puxar e teleporte não provocam.</div>
    </div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:3.2px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>A Resolução, no card de Habilidade
  </div>
  <div style="font-size:7.6px; line-height:1.4; margin-bottom:4px;">Toda Habilidade declara uma <b>Resolução</b> — quem rola o dado, e contra o quê. <b>Reação</b> não é resolução: é <i>quando</i> ela é usada, e vem explicada no card acima.</div>
  <div style="display:flex; gap:8px; margin-bottom:4.8px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Ataque</div>
      <div style="font-size:7.6px; line-height:1.35;">Faz um teste (d100 + Atributo) contra o número-alvo de 1 criatura.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Teste de Resistência</div>
      <div style="font-size:7.6px; line-height:1.35;">O <b>alvo</b> é que rola, contra o seu Atributo cru. Toda área usa esta.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Automática</div>
      <div style="font-size:7.6px; line-height:1.35;">Ninguém rola: o efeito acontece (buff, cura, escudo, zona).</div>
    </div>
  </div>

  <div style="display:flex; gap:8px; margin-bottom:4.8px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Iniciativa</div>
      <div style="font-size:8px; line-height:1.35;"><b>d100 + Agilidade + Sorte.</b> Ordem decrescente vale o combate inteiro — não rerola a cada rodada. Empate: maior Agilidade, depois maior Sorte, depois o Mestre decide.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:4.5px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:1.6px;">Turno, rodada e cena</div>
      <div style="font-size:7.6px; line-height:1.35;"><b>Turno</b> — a vez de um participante agir. <b>Rodada</b> — um ciclo completo da Iniciativa; termina quando todos jogaram, e é quando um efeito "de X rodadas" conta. <b>Cena</b> — o combate inteiro; usos "por cena" resetam ao fim.</div>
    </div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:3.2px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Viagem
  </div>
  <div style="font-size:7.6px; line-height:1.35; margin-bottom:3.2px;">Distância se mede em <b>trechos</b> (meio dia de marcha, mesma abstração das casas em combate). Terreno Difícil conta cada trecho como dois.</div>
  <table style="width:100%; border-collapse:collapse; font-size:7px; margin-bottom:4px;">
    <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Ritmo</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Trechos/dia</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Custo / ganho</th></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Cauteloso</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">1</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Vantagem pra notar perigo/emboscada; ninguém cansa</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Normal</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">2</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">padrão, nada de especial</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Forçado</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">3</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">ao fim do dia, 1 grau de Exausto pra cada um</td></tr>
  </table>
  <div style="font-size:7.6px; line-height:1.3; margin-bottom:2.4px;">Cada personagem assume <b>uma função</b> por dia de viagem:</div>
  <table style="width:100%; border-collapse:collapse; font-size:7px; margin-bottom:4.8px;">
    <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Função</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Teste</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:left; color:#159c56;">Se passar</th></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Guiar</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Exploração vs terreno</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">grupo não se perde nem gasta trecho extra</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Vigiar</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Exploração vs 60</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">grupo não fica Desprevenido numa emboscada</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Forragear</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Exploração vs 60</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">comida e água pra todos naquele dia</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Rastrear</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">Exploração vs rastro</td><td style="border:1px solid #cabf9f; padding:1.5px 5px;">descobre o que passou ali, quando e quantos</td></tr>
  </table>

  <div style="margin-top:auto; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

<!-- ============================================================ PÁGINA 4 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:22px 26px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:6px; margin-bottom:8px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:19px; height:19px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:13.5px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Consulta Rápida</div>
    </div>
    <div style="font-size:8.5px; color:#5b5343;">pág. 4 / 6</div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Condições
  </div>
  <div style="columns:2; column-gap:14px; font-size:6.9px; line-height:1.35; margin-bottom:9px;">
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Sangrando</b> — 4d4 Vida no início do próximo turno; marque o mesmo valor em Estresse. Não acumula (vale o maior).</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Queimando</b> — 4d4 ao pegar fogo + 4d4 por turno; cada rolagem vale o mesmo em Estresse. Apaga com Ação Básica, água, dano de Gelo/Água, ou fim da cena. Não acumula.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Lento</b> — Movimento reduzido à metade (só a ação ◈).</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Imóvel</b> — Movimento 0, mas age normalmente (Ações/Habilidades/Reações).</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Atordoado</b> — não pode agir, mover nem reagir. +3d6 Estresse ao ficar Atordoado.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Amedrontado</b> — Desvantagem em testes de ataque. +3d6 Estresse ao ficar Amedrontado.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Cego</b> — Desvantagem em ataques; ataques contra ele têm Vantagem. +2d6 Estresse ao ficar Cego.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Possuído</b> — outra criatura controla o corpo. ◈◈◈ + d100 Magia vs Fortitude Mágica do possuidor expulsa. Dano de Luz fere o possuidor, não o corpo; corpo a 0 de Vida encerra a possessão na hora. +5d6 Estresse ao ser possuído.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Petrificado</b> — 3 graus: Lento → Imóvel → pedra (Resistência física; 0 de Vida no grau 3 mata de vez). Cura Vida remove 1 grau. +5d6 Estresse ao atingir o grau 1.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Derrubado</b> — Movimento 0; corpo a corpo contra ele com Vantagem. Levantar custa ◈.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Desprevenido</b> — não age nem reage na 1ª rodada do combate.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Agarrado</b> — fica Imóvel. Escapar: ◈ + Ataque ou Agilidade vs Evasão de quem prende. +2d6 Estresse ao ser agarrado.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Marcado</b> — o próximo ataque de um aliado nesta rodada tem Vantagem.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Envenenado</b> — acumula até 3; Xd4 de Vida por turno (1=4d4, 2=8d4, 3=12d4); cada rolagem vale o mesmo em Estresse. Cura remove tudo de uma vez.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Escudo</b> — pontos temporários que absorvem dano antes da Vida. Não acumula (vale o maior).</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Exausto</b> — 3 graus: Desvantagem → +Lento → inconsciente. Descanso longo remove 1 grau (causa resolvida). +3d6 Estresse ao atingir o grau 3.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Risco</b> — assinatura do elemento Sangue: se um dado de dano cair em 1, o próprio usuário sofre o preço descrito na habilidade (normalmente perde Vida).</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px;"><b style="color:#159c56;">Caído (0 de Vida)</b> — inconsciente. d100 vs Dificuldade 50 no início do próximo turno: sucesso Estável, falha morre.</div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Dano & Ambiente
  </div>
  <div style="columns:2; column-gap:14px; font-size:6.9px; line-height:1.35; margin-bottom:6px;">
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Assinatura do tipo de dano</b> — o tipo escolhe um <i>verbo</i>, e ele vem junto com o golpe, sem custo à parte. Sobe com a Intensidade (I → II → III):<div style="margin-top:1.5px; padding-left:5px; line-height:1.35;"><b>Cortante</b> — a ferida não fecha: Sangrando → 8d4 → 12d4<br><b>Impacto</b> — derruba a postura: derruba → e Lento → levantar custa ◈ a mais<br><b>Perfurante</b> — acha a brecha: +1d6 → +2d6 → +3d6, <i>só contra alvo preso</i><br><b>Arcano</b> — o golpe realimenta: devolve 1 → 2 → 3 Mana</div><div style="font-size:6.1px; color:#5b5343; margin-top:1.5px;"><b>Alvo preso:</b> Lento, Imóvel, Atordoado, Agarrado ou Derrubado.</div></div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Arcano</b> — dano de magia sem assinatura elemental (focos mágicos, Espaço-Tempo). Fogo, Gelo, Raio e os outros elementos verdadeiros causam dano do próprio tipo, não Arcano.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Resist. / Imunidade / Vulnerab.</b> — dano cai pela metade / é ignorado / dobra, depois de tudo (inclusive Crítico). Nunca as duas primeiras juntas — cancelam. Resistência a um tipo <b>físico</b> também apaga a assinatura dele: resistente a Cortante não fica Sangrando.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Acúmulo de bônus</b> — bônus planos de fontes diferentes não somam; vale o maior. Resistências ao mesmo tipo também não acumulam.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Luz e Escuridão</b> — parcial: Desvantagem em testes visuais. Total: só age com quem está adjacente, sem ataque à distância.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px; border-bottom:1px dotted #cabf9f;"><b style="color:#159c56;">Água</b> — nadar é Terreno Difícil. Fôlego: 1+(Defesa÷10) rodadas antes de afogar; depois, 1 grau de Exausto/rodada. Sem traço aquático, corpo a corpo com Desvantagem.</div>
    <div style="break-inside:avoid; padding-bottom:2.5px; margin-bottom:2.5px;"><b style="color:#159c56;">Clima Extremo</b> — calor/frio sem proteção: 1 grau de Exausto/dia. Tempestade: Terreno Difícil geral + Desvantagem pra Vigiar/Rastrear.</div>
  </div>
  <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
    <div style="flex:0 0 100px; font-size:6.6px; line-height:1.3;"><b style="color:#159c56; font-size:7px; text-transform:uppercase; letter-spacing:0.05em;">Dano Desarmado</b><br>Socos e chutes não usam dado de arma — escalam sozinhos pelo nível. Impacto, salvo traço racial diferente.</div>
    <table style="flex:1; border-collapse:collapse; font-size:6.8px;">
      <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:1.5px 5px; color:#159c56;">Nível 0–25</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; color:#159c56;">26–50</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; color:#159c56;">51–75</th><th style="border:1px solid #cabf9f; padding:1.5px 5px; color:#159c56;">76–100</th></tr>
      <tr><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">2d6</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">2d12</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">2d20</td><td style="border:1px solid #cabf9f; padding:1.5px 5px; text-align:center;">3d20</td></tr>
    </table>
  </div>
  <div style="font-size:6.3px; line-height:1.25; color:#5b5343; margin-bottom:6px;">Traço racial de "1 grau acima" empurra pra faixa seguinte da tabela. Habilidades Marciais que dizem "usa o Dano Desarmado" (Ataque Desarmado, Toma Toma Toma, Chute Meteoro...) têm esse dado fixo em qualquer Intensidade — só o efeito extra (derrubar, Lento, Atordoado) muda.</div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Para que serve cada Atributo
  </div>
  <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:4px 8px; margin-bottom:8px;">
    <div style="border-left:3px solid #b8502e; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#b8502e; font-size:7px;">Ataque</div><div>Poder físico bruto e técnica com armas.</div></div>
    <div style="border-left:3px solid #a3781a; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#a3781a; font-size:7px;">Defesa</div><div>Resistência física — encaixar, aguentar pancada.</div></div>
    <div style="border-left:3px solid #4c7a3d; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#4c7a3d; font-size:7px;">Agilidade</div><div>Reflexos e velocidade — desviar, reagir rápido.</div></div>
    <div style="border-left:3px solid #3f5fa0; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#3f5fa0; font-size:7px;">Magia</div><div>Poder mágico — controlar e canalizar Mana.</div></div>
    <div style="border-left:3px solid #a04570; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#a04570; font-size:7px;">Social</div><div>Presença e influência — persuadir, enganar, intimidar.</div></div>
    <div style="border-left:3px solid #2d7a6e; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#2d7a6e; font-size:7px;">Exploração</div><div>Atenção ao ambiente — notar, rastrear, sobreviver.</div></div>
    <div style="border-left:3px solid #b39422; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#b39422; font-size:7px;">Sorte</div><div>Acaso e fortuna — estar no lugar certo na hora certa.</div></div>
    <div style="border-left:3px solid #6a3fa0; padding:1.5px 6px; font-size:6.4px; line-height:1.25;"><div style="font-weight:700; color:#6a3fa0; font-size:7px;">Sanidade</div><div>Estabilidade mental — resistir a horror e colapso.</div></div>
  </div>

  <div style="margin-top:auto; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

<!-- ============================================================ PÁGINA 5 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:22px 26px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:6px; margin-bottom:9px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:19px; height:19px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:13.5px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Recursos</div>
    </div>
    <div style="font-size:8.5px; color:#5b5343;">pág. 5 / 6</div>
  </div>

  <div style="display:flex; gap:8px; margin-bottom:6px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Rerolagens</div>
      <div style="font-size:7.6px; line-height:1.35;"><b>1 + (Sorte ÷ 10)</b> usos por descanso longo. Rerola um teste seu que falhou, ou um efeito usado contra você — não dá pra rerolar sucesso pra upar em crítico.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Mana e Intensidade</div>
      <div style="font-size:7.6px; line-height:1.35;">Cada Intensidade (I/II/III) tem seu próprio custo de Mana, além do PA — quanto mais forte o efeito, mais das duas coisas ele consome. <b>Separadamente:</b> Atributo abaixo do recomendado pra Escala da habilidade rola com Desvantagem.</div>
    </div>
  </div>

  <div style="display:flex; gap:8px; margin-bottom:8px;">
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Cooldown</div>
      <div style="font-size:7.3px; line-height:1.32;">Vem do que a habilidade <b>custa</b>, não do que entrega. Só existem quatro degraus:<br><b>3–9 Mana</b> (Básica) sem cooldown · <b>12–24</b> (Avançada) 1 rodada · <b>27–45</b> (Especial) 2 rodadas · <b>48+</b> 1x por cena.<br>Reação e Passiva <b>nunca</b> têm cooldown — o gatilho já as limita.</div>
    </div>
    <div style="flex:1; position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px;">
      <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Escala de Poder</div>
      <div style="font-size:7.3px; line-height:1.32;"><b>Menor · Moderada · Notável · Maior · Suprema.</b> Responde <i>quão grande é</i>, não quanto custa — existe habilidade barata que faz muito. É calculada: dano, alcance, controle e permanência valem 0, 1 ou 2 cada, e vale a <b>soma dos dois maiores</b>.</div>
    </div>
  </div>

  <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px; margin-bottom:8px;">
    <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">0 de Vida / Caído</div>
    <div style="font-size:7.8px; line-height:1.4;">Personagem chega a 0 de Vida e fica <b>Caído</b> — não morre na hora (criatura, sim). No início do turno seguinte, rola d100 vs Dificuldade 50: sucesso fica <b>Estável</b>, falha <b>morre</b>. Um aliado pode Estabilizar antes disso (◈ + Exploração vs 50), ou qualquer cura resolve na hora. <b>Último Turno</b> é a alternativa: em vez de rolar contra a morte, o jogador levanta o personagem pra jogar um turno completo (3 PA, tudo) — nesse turno, todo acerto vira Crítico automático, e nenhuma cura funciona. Ao fim dele, o personagem morre, mas com o golpe garantido.</div>
  </div>

  <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(6px 0,100% 0,100% 100%,6px 100%,0 calc(100% - 6px),0 6px); background:#f1ebdc; padding:6px 10px; margin-bottom:8px;">
    <div style="font-size:7px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Estresse — ganho e recuperação</div>
    <div style="font-size:7.8px; line-height:1.4;"><b>Automático (1d6 cada):</b> tirar exatamente 1 no d100 em qualquer teste, ou sofrer um crítico. <b>Narrativo (4d6 fixo):</b> presenciar horror, cair a 0, ver aliado cair a 0, falhar em algo que importava, ferir/matar quem não devia — role d100 + Sanidade vs Dificuldade do Mestre; falhando, marca 4d6. <b>Recuperação:</b> igual Vida e Mana — metade do máximo no descanso curto, tudo no longo.</div>
  </div>

  <div style="display:flex; gap:8px; margin-bottom:8px;">
    <div style="flex:1;">
      <div style="font-size:8px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#83765a; margin-bottom:3px;">Colapso — barra cheia, 1d6</div>
      <div style="font-size:6.6px; line-height:1.35;">
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">1 Fuga</b> — foge da cena; Indisponível pelo resto dela.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">2 Pânico</b> — trava 1 rodada inteira, sem agir.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">3 Fúria Cega</b> — ataca o mais próximo 1x, sem escolha.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">4 Colapso Físico</b> — desmaia, Indisponível 1d4 rodadas.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">5 Dissociação</b> — solta tudo até fim do turno.</div>
        <div><b style="color:#159c56;">6 Bloqueio</b> — trava até ajuda ou fim de cena.</div>
      </div>
    </div>
    <div style="flex:1;">
      <div style="font-size:8px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#83765a; margin-bottom:3px;">Cicatriz — depois do surto, 1d6</div>
      <div style="font-size:6.6px; line-height:1.35;">
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">1 Fobia Específica</b> — Desvantagem geral perto do gatilho.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">2 Gatilho de Fúria</b> — evento força teste de Estresse extra.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">3 Tique Nervoso</b> — Desvantagem no 1º teste social da cena.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">4 Isolamento</b> — Apoio Social cura só metade do Estresse.</div>
        <div style="border-bottom:1px dotted #cabf9f; padding-bottom:1.5px; margin-bottom:1.5px;"><b style="color:#159c56;">5 Paranoia</b> — Desvantagem em Iniciativa.</div>
        <div><b style="color:#159c56;">6 Exaustão Crônica</b> — descanso curto não recupera Mana.</div>
      </div>
    </div>
  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Descanso
  </div>
  <table style="width:100%; border-collapse:collapse; font-size:7px; margin-bottom:8px;">
    <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:2px 5px; text-align:left; color:#159c56;">Tipo</th><th style="border:1px solid #cabf9f; padding:2px 5px; text-align:left; color:#159c56;">Dura</th><th style="border:1px solid #cabf9f; padding:2px 5px; text-align:left; color:#159c56;">Recupera</th></tr>
    <tr><td style="border:1px solid #cabf9f; padding:2px 5px;">Curto</td><td style="border:1px solid #cabf9f; padding:2px 5px;">~1 hora</td><td style="border:1px solid #cabf9f; padding:2px 5px;">Metade de Vida, Mana e Estresse</td></tr>
    <tr><td style="border:1px solid #cabf9f; padding:2px 5px;">Longo</td><td style="border:1px solid #cabf9f; padding:2px 5px;">~8h, lugar seguro</td><td style="border:1px solid #cabf9f; padding:2px 5px;">Tudo (Vida/Mana/Estresse) + 1 grau de Exausto (causa resolvida) + reseta "1x/descanso longo" e Rerolagens</td></tr>
  </table>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:4px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Exaustão
  </div>
  <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
    <table style="flex:1; border-collapse:collapse; font-size:7px;">
      <tr style="background:#e5ddc4;"><th style="border:1px solid #cabf9f; padding:2px 5px; text-align:left; color:#159c56;">Grau</th><th style="border:1px solid #cabf9f; padding:2px 5px; text-align:left; color:#159c56;">Efeito (acumulativo)</th></tr>
      <tr><td style="border:1px solid #cabf9f; padding:2px 5px; text-align:center;">1</td><td style="border:1px solid #cabf9f; padding:2px 5px;">Desvantagem em todos os testes</td></tr>
      <tr><td style="border:1px solid #cabf9f; padding:2px 5px; text-align:center;">2</td><td style="border:1px solid #cabf9f; padding:2px 5px;">também fica Lento</td></tr>
      <tr><td style="border:1px solid #cabf9f; padding:2px 5px; text-align:center;">3</td><td style="border:1px solid #cabf9f; padding:2px 5px;">cai inconsciente até ajuda ou descanso</td></tr>
    </table>
    <div style="flex:0 0 100px; text-align:center;">
      <div style="font-size:6.3px; color:#83765a; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:3px;">Grau atual</div>
      <div style="display:flex; justify-content:center; gap:5px;">
        <span style="width:11px; height:11px; border:1.2px solid #159c56; display:inline-block;"></span>
        <span style="width:11px; height:11px; border:1.2px solid #159c56; display:inline-block;"></span>
        <span style="width:11px; height:11px; border:1.2px solid #159c56; display:inline-block;"></span>
      </div>
    </div>
  </div>
  <div style="font-size:6.6px; line-height:1.3; color:#5b5343; margin-bottom:6px;">Ganha 1 grau por: dia sem comida/água (a partir do 2º), noite sem descanso longo adequado, dia de ritmo Forçado, ou dia de clima extremo sem proteção. Remove 1 grau por descanso longo — só se a causa estiver resolvida.</div>

  <div style="margin-top:auto; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

<!-- ============================================================ PÁGINA 6 -->
<section class="prg-ficha__pagina" style="display:flex; flex-direction:column; padding:22px 26px; font-family:'Crimson Pro', Georgia, serif; color:#211c14; font-size:13px;">

  <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #83765a; padding-bottom:6px; margin-bottom:9px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg viewBox="0 0 64 64" style="width:19px; height:19px; color:#159c56;">
        <path d="M32 3 L61 32 L32 61 L3 32z" fill="none" stroke="currentColor" stroke-width="1.2" opacity=".45"/>
        <path d="M32 9 L55 32 L32 55 L9 32z" fill="currentColor" opacity=".07"/>
        <path d="M32 14 L50 32 L32 50 L14 32z" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".8"/>
        <path d="M32 22 L42 32 L32 42 L22 32z" fill="currentColor" opacity=".9"/>
        <path d="M32 22 L42 32 L32 32z" fill="currentColor" opacity=".35"/>
        <circle cx="32" cy="6" r="1.6" fill="currentColor" opacity=".7"/><circle cx="32" cy="58" r="1.6" fill="currentColor" opacity=".7"/>
        <circle cx="6" cy="32" r="1.6" fill="currentColor" opacity=".7"/><circle cx="58" cy="32" r="1.6" fill="currentColor" opacity=".7"/>
      </svg>
      <div style="font-size:13.5px; font-weight:700; color:#159c56; letter-spacing:0.02em;">Prisma RPG — Notas</div>
    </div>
    <div style="font-size:8.5px; color:#5b5343;">pág. 6 / 6</div>
  </div>

  <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin-bottom:9px;">

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 3v18M18 3v18M6 12h12" stroke-dasharray="3 2"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Cicatrizes</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">1 por surto de Estresse (tabela pág. 5)</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.5-9.5-9C1 8 3 4 7 4c2 0 4 1.3 5 3.2C13 5.3 15 4 17 4c4 0 6 4 4.5 8-2.5 4.5-9.5 9-9.5 9z"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Vício</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">Um hábito, mania ou compulsão pessoal</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 5-3.5 8-7 9-3.5-1-7-4-7-9V6z"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Facções & Aliados</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">Quem apoia, quem deve, quem se opõe</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10M7 21h10M8 3c0 4 3 6 4 9-1 3-4 5-4 9M16 3c0 4-3 6-4 9 1 3 4 5 4 9"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Efeitos Temporários</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">Buffs e debuffs em aberto entre cenas</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="10" cy="10" r="6"/><path d="M20 20l-5.5-5.5"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Pistas</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">O que ainda não fecha, o que falta juntar</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

    <div style="position:relative; border:1.2px solid #159c56; clip-path:polygon(7px 0,100% 0,100% 100%,7px 100%,0 calc(100% - 7px),0 7px); background:#f1ebdc; padding:7px 9px;">
      <span style="position:absolute; top:6px; right:6px; width:16px; height:16px; background:#159c56; border:1.2px solid #f1ebdc; transform:rotate(45deg); z-index:2; display:flex; align-items:center; justify-content:center; box-shadow:0 1px 2px rgba(0,0,0,.25);">
        <svg viewBox="0 0 24 24" style="width:10px; height:10px; transform:rotate(-45deg); color:#faf7ef;" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 11h6M9 15h6"/></svg>
      </span>
      <div style="font-size:8.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:#159c56; margin-bottom:2px;">Quests & Rumores</div>
      <div style="font-size:6.3px; color:#5b5343; margin-bottom:6px; line-height:1.25;">O que fazer, o que ouviu por aí</div>
      <div style="display:flex; flex-direction:column; gap:9px;">
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
        <div style="border-bottom:1px solid #cabf9f; min-height:10px;">&nbsp;</div>
      </div>
    </div>

  </div>

  <div style="font-size:9px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; color:#83765a; margin-bottom:5px; display:flex; align-items:center; gap:5px;">
    <svg viewBox="0 0 10 10" style="width:6px; height:6px; color:#159c56;"><path d="M5 0 L10 5 L5 10 L0 5z" fill="currentColor" opacity=".7"/></svg>Notas & Backstory
  </div>
  <div style="flex:1; background-image:repeating-linear-gradient(to bottom, transparent, transparent 21px, #cabf9f 21px, #cabf9f 22px); min-height:0;"></div>

  <div style="margin-top:8px; padding-top:5px; border-top:1px solid #cabf9f; font-size:6pt; color:#5b5343; text-align:center;">Prisma RPG — Ficha de Personagem — felipe1072-git.github.io/prisma-rpg</div>

</section>

</div>
