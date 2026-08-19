#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compone propuesta/index.html con el diseño nuevo, reusando el recorrido tal cual está."""
import json, pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))

S    = pathlib.Path(__file__).parent
BASE = S.parent.parent
OUT  = S.parent

# los módulos con guion no se importan: se leen y se ejecutan
ns_css = {}
exec(compile((S / "diseno.py").read_text(encoding="utf-8"), "diseno", "exec"), ns_css)
ns_sec = {}
exec(compile((S / "secciones.py").read_text(encoding="utf-8"), "secciones", "exec"), ns_sec)

corte  = (S / "corte.svg.html").read_text(encoding="utf-8")
motor  = (S / "motor.js.html").read_text(encoding="utf-8")
logos  = json.loads((S / "logos.json").read_text())
L = lambda k: "data:image/png;base64," + logos[k]

# ---- CSS del escenario del recorrido, en la paleta nueva ----
STAGE_CSS = """
  /* ---------- RECORRIDO ---------- */
  #recorrido{position:relative;background:var(--horno)}
  #recorrido .stage{position:sticky;top:72px;height:calc(100vh - 72px);height:calc(100dvh - 72px);overflow:hidden}
  .layer{position:absolute;inset:0;width:100%;height:100%;display:block}
  .vinieta{position:absolute;inset:0;pointer-events:none;
    background:radial-gradient(125% 92% at 50% 44%, transparent 40%, rgba(8,9,11,.62) 100%)}
  .beats{position:absolute;inset:0;pointer-events:none}
  .beat{
    position:absolute;left:0;right:0;bottom:clamp(36px,8vh,84px);
    opacity:0;transform:translateY(16px);transition:opacity .26s ease, transform .26s ease;
  }
  .beat[data-on="1"]{opacity:1;transform:none;transition:opacity .45s ease .2s, transform .45s ease .2s}
  .beat .box{
    max-width:29em;background:rgba(14,16,19,.80);backdrop-filter:blur(14px);
    border:1px solid var(--linea-osc);border-left:3px solid var(--naranja);padding:22px 24px 24px;
  }
  .beat h2{font-size:clamp(22px,2.6vw,30px);color:var(--calblanco);letter-spacing:-.015em;margin:10px 0 10px}
  .beat p{font-size:15px;color:var(--acero)}
  .beat .specs{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px}
  .beat .specs span{
    font-family:var(--dato);font-size:11px;letter-spacing:.06em;color:var(--fibra);
    background:rgba(237,231,219,.07);border:1px solid var(--linea-osc);padding:5px 9px;
  }
  .rail{position:absolute;right:20px;top:50%;transform:translateY(-50%);display:grid;gap:11px}
  .rail button{
    all:unset;cursor:pointer;width:9px;height:9px;border:1px solid rgba(237,231,219,.34);
    transition:background .22s ease, transform .22s ease, border-color .22s ease;
  }
  .rail button[aria-current="true"]{background:var(--naranja);border-color:var(--naranja);transform:scale(1.5)}
  .rail button:focus-visible{outline:2px solid var(--naranja);outline-offset:3px}
  @media (max-width:760px){.rail{right:10px}}
  .kind{
    position:absolute;left:28px;top:22px;
    font-family:var(--dato);font-size:10px;letter-spacing:.16em;text-transform:uppercase;
    color:var(--acero);background:rgba(14,16,19,.72);border:1px solid var(--linea-osc);padding:6px 10px;
  }
  .kind b{color:var(--naranja);font-weight:400}
  .pre{position:absolute;inset:0;display:grid;place-content:center;gap:14px;background:var(--horno);z-index:5}
  .pre[hidden]{display:none}
  .pre .bar{width:min(240px,58vw);height:2px;background:rgba(237,231,219,.16);overflow:hidden}
  .pre .bar i{display:block;height:100%;width:0;background:var(--naranja);transition:width .2s ease}
  .pre span{font-family:var(--dato);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--acero-2);text-align:center}
  #dg{background:radial-gradient(92% 80% at 50% 46%, #1B2126 0%, var(--horno) 100%)}
  .part{transition:opacity .5s ease}
  #dg[data-hi="camara"] .part,#dg[data-hi="resistencias"] .part,
  #dg[data-hi="chimenea"] .part,#dg[data-hi="control"] .part{opacity:.24}
  #dg[data-hi="camara"] .p-camara,#dg[data-hi="resistencias"] .p-resistencias,
  #dg[data-hi="chimenea"] .p-chimenea,#dg[data-hi="control"] .p-control{opacity:1}
  .lbl{opacity:0;transition:opacity .45s ease .1s}
  #dg[data-hi="camara"] .l-camara,#dg[data-hi="resistencias"] .l-resistencias,
  #dg[data-hi="chimenea"] .l-chimenea,#dg[data-hi="control"] .l-control{opacity:1}
  .glow{opacity:0;transition:opacity .6s ease}
  #dg[data-hi="resistencias"] .glow{opacity:1}
  .static-list{display:none;padding:72px 0;gap:52px}
  .static-list article{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:center}
  .static-list img,.static-list svg{width:100%;border:1px solid var(--linea-osc);display:block;background:var(--horno-2)}
  @media (max-width:760px){.static-list article{grid-template-columns:1fr}}
  html.no-motion #recorrido{display:none}
  html.no-motion .static-list{display:grid}
"""

RECORRIDO = """
<section id="recorrido" aria-label="Recorrido del equipo">
  <div class="stage">
    <canvas class="layer" id="cv" role="img" aria-label="Recorrido fotográfico del horno: órbita del frontal al tres cuartos derecho."></canvas>
    @CORTE@
    <div class="vinieta"></div>
    <div class="kind" id="kind">Fotografía del equipo</div>
    <div class="beats wrap" id="beats"></div>
    <div class="rail" id="rail" aria-label="Ir a un punto del recorrido"></div>
    <div class="pre" id="pre">
      <div class="bar"><i id="preBar"></i></div>
      <span id="preTxt">Cargando recorrido…</span>
    </div>
  </div>
</section>
<div class="wrap static-list" id="staticList"></div>
""".replace("@CORTE@", corte)

motor = motor.replace('document.getElementById("seq")', 'document.getElementById("recorrido")')
motor = motor.replace('.vignette', '.vinieta')

html = (
    # Sin doctype el navegador entra en quirks mode y ahí las TABLAS no heredan el color del
    # padre: el texto de la proforma salía del mismo color que su fondo, invisible.
    '<!DOCTYPE html>\n'
    '<meta charset="utf-8">\n'
    '<title>Hornos de tratamiento térmico — Propuesta técnica · Elyon Industrial</title>\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<style>' + ns_css["CSS"] + STAGE_CSS + '</style>\n'
    + ns_sec["nav"](L("nav"))
    + ns_sec["hero"](L("leon"))
    + ns_sec["RECORRIDO_INTRO"]
    + RECORRIDO
    + ns_sec["MODELOS"]
    + ns_sec["TECNOLOGIA"]
    + ns_sec["ALCANCE"]
    + ns_sec["DEFINICIONES"]
    + ns_sec["PLAN"]
    + ns_sec["comercial"](L("leon_agua"), L("logo_pf"))
    + ns_sec["DIRECTORIO"]
    + ns_sec["pie"](L("nav"))
    + motor
    + ns_sec["TABLA_JS"]
)

OUT.mkdir(exist_ok=True)
(OUT / "index.html").write_text(html, encoding="utf-8")

for juego in ("frames", "frames-movil"):
    src = BASE / "04-secuencia-scroll" / juego
    dst = OUT / juego
    if src.exists():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print("%-14s %d cuadros" % (juego + "/", len(list(dst.glob("*")))))

print("index.html: %.0f KB" % ((OUT / "index.html").stat().st_size / 1024))
