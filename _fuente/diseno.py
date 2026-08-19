# -*- coding: utf-8 -*-
"""Sistema de diseño de la propuesta. Paleta derivada de la escala de incandescencia."""

CSS = """
  :root{
    /* La paleta sale de la escala de incandescencia del acero: el color con el que un
       tratamista lee la temperatura a ojo. El naranja de Elyon cae en los 900 °C. */
    --horno:      #0E1013;   /* cámara fría */
    --horno-2:    #171B20;   /* superficie elevada sobre oscuro */
    --horno-3:    #22282E;
    --fibra:      #EDE7DB;   /* fibra cerámica: superficie clara para datos */
    --fibra-2:    #DED6C6;
    --tinta:      #14181B;
    --acero:      #97A2A9;   /* texto secundario sobre oscuro */
    --acero-2:    #5D6B73;   /* texto secundario sobre claro */
    --cereza:     #A4240B;   /*  700 °C */
    --naranja:    #FE6B03;   /*  900 °C · marca Elyon */
    --ambar:      #FFC24A;   /* 1100 °C */
    --calblanco:  #FFF3DF;   /* 1200 °C */
    --linea-osc:  rgba(237,231,219,.14);
    --linea-cla:  rgba(20,24,27,.14);

    --display: "Futura", "Futura PT", "Century Gothic", "URW Gothic", "Avenir Next", sans-serif;
    --texto:   "Helvetica Neue", Helvetica, Arial, sans-serif;
    --dato:    "SF Mono", ui-monospace, "Cascadia Mono", Menlo, Consolas, monospace;

    --ancho: 1180px;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
  @media (prefers-reduced-motion: reduce){
    html{scroll-behavior:auto}
    *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important}
  }
  body{
    margin:0;background:var(--horno);color:var(--fibra);
    font-family:var(--texto);font-size:16.5px;line-height:1.62;
    -webkit-font-smoothing:antialiased;
  }
  h1,h2,h3,h4{margin:0;font-family:var(--display);font-weight:500;line-height:1.06;text-wrap:balance}
  p{margin:0}
  a{color:inherit}
  img{max-width:100%}
  :focus-visible{outline:2px solid var(--naranja);outline-offset:3px}
  .wrap{max-width:var(--ancho);margin:0 auto;padding:0 28px}
  .num{font-variant-numeric:tabular-nums}

  /* ---------- etiquetas de dato ---------- */
  .rot{
    font-family:var(--dato);font-size:11px;letter-spacing:.20em;text-transform:uppercase;
    color:var(--naranja);display:block;
  }
  .rot--cla{color:var(--cereza)}

  /* ---------- secciones ---------- */
  .sec{padding:104px 0}
  @media (max-width:720px){.sec{padding:72px 0}}
  .sec--fibra{background:var(--fibra);color:var(--tinta)}
  .sec--osc{background:var(--horno)}
  .sec--osc2{background:var(--horno-2)}
  .cab{max-width:34em}
  .cab h2{
    font-size:clamp(30px,4.1vw,50px);letter-spacing:-.018em;margin:14px 0 16px;
  }
  .sec--fibra .cab h2{color:var(--tinta)}
  .cab p{color:var(--acero);font-size:17.5px}
  .sec--fibra .cab p{color:var(--acero-2)}

  /* ---------- NAV ---------- */
  .nav{
    position:sticky;top:0;z-index:60;height:72px;
    background:rgba(14,16,19,.90);backdrop-filter:blur(12px);
    border-bottom:1px solid var(--linea-osc);
  }
  .nav .wrap{display:flex;align-items:center;gap:24px;height:100%}
  .nav img{height:44px;display:block}
  .nav-links{display:flex;gap:4px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
  .nav-links::-webkit-scrollbar{display:none}
  .nav-links a{
    font-family:var(--dato);font-size:11.5px;letter-spacing:.10em;text-transform:uppercase;
    color:var(--acero);text-decoration:none;padding:9px 12px;border-radius:2px;white-space:nowrap;
    transition:color .18s ease, background .18s ease;
  }
  .nav-links a:hover{color:var(--calblanco);background:rgba(237,231,219,.07)}

  /* ---------- HERO: la escala de incandescencia ---------- */
  .hero{position:relative;padding:72px 0 0;overflow:hidden}
  .hero-grid{display:grid;grid-template-columns:1.06fr .94fr;gap:16px 56px;align-items:end}
  @media (max-width:880px){.hero-grid{grid-template-columns:1fr;gap:26px}}
  .hero h1{
    font-size:clamp(40px,5.6vw,74px);letter-spacing:-.032em;line-height:.98;
    color:var(--calblanco);margin:18px 0 0;
  }
  .hero h1 em{font-style:normal;color:var(--ambar)}
  .hero .bajada{
    font-size:17.5px;color:var(--acero);max-width:34em;padding-bottom:6px;
  }
  .hero .bajada b{color:var(--fibra);font-weight:600}
  .escala{margin:56px 0 0;position:relative}
  .escala svg{width:100%;height:auto;display:block}
  .hero-lion{
    position:absolute;right:1%;top:38px;width:clamp(120px,13vw,190px);
    opacity:.10;pointer-events:none;user-select:none;
  }
  @media (max-width:860px){.hero-lion{display:none}}
  .cifras{
    display:grid;grid-template-columns:repeat(4,1fr);
    border-top:1px solid var(--linea-osc);margin-top:8px;
  }
  @media (max-width:720px){.cifras{grid-template-columns:repeat(2,1fr)}}
  .cifras div{padding:22px 20px 26px;border-left:1px solid var(--linea-osc)}
  .cifras div:first-child{border-left:0;padding-left:0}
  .cifras .v{font-family:var(--display);font-size:34px;letter-spacing:-.02em;color:var(--calblanco)}
  .cifras .v small{font-family:var(--dato);font-size:13px;letter-spacing:0;color:var(--naranja);margin-left:3px}
  .cifras .k{font-family:var(--dato);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--acero-2);margin-top:6px}

  /* ---------- MODELOS ---------- */
  .mods{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid var(--linea-cla);background:#fff}
  @media (max-width:820px){.mods{grid-template-columns:1fr}}
  .mods button{
    all:unset;cursor:pointer;display:block;padding:26px 26px 30px;
    border-left:1px solid var(--linea-cla);position:relative;
    transition:background .2s ease;
  }
  .mods button:first-child{border-left:0}
  @media (max-width:820px){.mods button{border-left:0;border-top:1px solid var(--linea-cla)}
    .mods button:first-child{border-top:0}}
  .mods button:hover{background:rgba(164,36,11,.045)}
  .mods button[aria-pressed="true"]{background:rgba(254,107,3,.09)}
  .mods button::after{
    content:"";position:absolute;left:0;right:0;top:-1px;height:3px;background:transparent;
    transition:background .2s ease;
  }
  .mods button[aria-pressed="true"]::after{background:var(--naranja)}
  .mods .cod{font-family:var(--dato);font-size:12px;letter-spacing:.10em;color:var(--cereza)}
  .mods .lit{font-family:var(--display);font-size:44px;letter-spacing:-.03em;color:var(--tinta);margin:10px 0 2px}
  .mods .lit span{font-size:17px;letter-spacing:0;color:var(--acero-2);margin-left:4px}
  .mods .tip{font-size:14px;color:var(--acero-2)}
  .barra{height:6px;background:var(--fibra-2);margin-top:18px;position:relative}
  .barra i{position:absolute;inset:0 auto 0 0;background:var(--cereza);transition:background .2s ease}
  .mods button[aria-pressed="true"] .barra i{background:var(--naranja)}
  .barra-nota{font-family:var(--dato);font-size:10.5px;letter-spacing:.10em;color:var(--acero-2);margin-top:7px;text-transform:uppercase}

  .tabla-envoltura{overflow-x:auto;margin-top:2px;border:1px solid var(--linea-cla);border-top:0;background:#fff}
  table.espec{width:100%;border-collapse:collapse;font-size:15px}
  table.espec th,table.espec td{padding:14px 26px;text-align:left;vertical-align:top}
  table.espec tbody tr{border-top:1px solid var(--linea-cla)}
  table.espec th[scope="row"]{
    font-family:var(--dato);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
    color:var(--acero-2);font-weight:400;white-space:nowrap;width:1%;
  }
  table.espec td{font-family:var(--dato);font-size:13.5px;color:var(--tinta);border-left:1px solid var(--linea-cla)}
  table.espec td.on{background:rgba(254,107,3,.07)}
  .comun{
    margin-top:26px;font-size:15.5px;color:var(--acero-2);max-width:60em;
  }
  .comun b{color:var(--tinta);font-family:var(--dato);font-size:13.5px}

  /* ---------- TECNOLOGÍA ---------- */
  .subs{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--linea-osc);border:1px solid var(--linea-osc)}
  @media (max-width:900px){.subs{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:600px){.subs{grid-template-columns:1fr}}
  .subs article{background:var(--horno-2);padding:28px 26px 30px}
  .subs .medida{
    font-family:var(--dato);font-size:19px;letter-spacing:-.01em;color:var(--ambar);
  }
  .subs h3{font-size:21px;letter-spacing:-.01em;color:var(--calblanco);margin:14px 0 10px}
  .subs p{font-size:14.5px;color:var(--acero)}

  /* ---------- ALCANCE ---------- */
  .entrega{
    display:grid;grid-template-columns:1fr 1fr;gap:0 56px;
  }
  @media (max-width:760px){.entrega{grid-template-columns:1fr;gap:0}}
  .entrega div{
    display:flex;gap:16px;align-items:baseline;
    padding:15px 0;border-bottom:1px solid var(--linea-cla);font-size:16px;
  }
  .entrega div::before{
    content:"";flex:0 0 auto;width:9px;height:9px;background:var(--naranja);
    transform:translateY(-1px);
  }

  /* ---------- DEFINICIONES ---------- */
  .abiertas{display:grid;gap:1px;background:var(--linea-osc);border:1px solid var(--linea-osc)}
  .abiertas article{background:var(--horno-2);padding:28px 30px;display:grid;grid-template-columns:auto 1fr;gap:0 28px}
  @media (max-width:700px){.abiertas article{grid-template-columns:1fr;gap:14px}}
  .abiertas .marca{
    font-family:var(--dato);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
    color:var(--cereza);border:1px solid var(--cereza);padding:5px 9px;height:max-content;white-space:nowrap;
  }
  .abiertas h3{font-size:20px;color:var(--calblanco);margin-bottom:9px}
  .abiertas p{font-size:14.8px;color:var(--acero)}

  /* ---------- PLAN ---------- */
  .etapas{display:grid;grid-template-columns:repeat(6,1fr);border-top:2px solid var(--linea-cla)}
  @media (max-width:960px){.etapas{grid-template-columns:repeat(3,1fr)}}
  @media (max-width:560px){.etapas{grid-template-columns:1fr;border-top:0}}
  .etapas div{padding:24px 22px 30px 0;position:relative}
  .etapas div::before{
    content:"";position:absolute;top:-2px;left:0;width:26px;height:2px;background:var(--cereza);
  }
  .etapas .n{font-family:var(--dato);font-size:11px;letter-spacing:.14em;color:var(--acero-2)}
  .etapas h3{font-size:18px;color:var(--tinta);margin:12px 0 8px}
  .etapas p{font-size:14px;color:var(--acero-2)}
  .plazo{
    margin-top:44px;display:flex;flex-wrap:wrap;gap:10px 26px;align-items:baseline;
    border-top:1px solid var(--linea-cla);border-bottom:1px solid var(--linea-cla);padding:26px 0;
  }
  .plazo .v{font-family:var(--display);font-size:38px;letter-spacing:-.025em;color:var(--cereza)}
  .plazo p{font-size:15.5px;color:var(--acero-2);max-width:46em}

  /* ---------- COMERCIAL ---------- */
  .inv{display:grid;grid-template-columns:1.1fr .95fr .95fr;gap:1px;background:var(--linea-osc);border:1px solid var(--linea-osc)}
  @media (max-width:860px){.inv{grid-template-columns:1fr}}
  .inv article{background:var(--horno-2);padding:30px 28px 34px}
  .inv .rot{margin-bottom:16px}
  .inv .monto{font-family:var(--display);font-size:clamp(38px,4.6vw,56px);letter-spacing:-.03em;color:var(--calblanco)}
  .inv p{font-size:14.8px;color:var(--acero);margin-top:12px}
  .inv ul{margin:0;padding:0;list-style:none}
  .inv li{font-size:14.8px;color:var(--acero);padding:11px 0;border-bottom:1px solid var(--linea-osc)}
  .inv li:last-child{border-bottom:0}
  .inv li b{color:var(--calblanco);font-family:var(--dato);font-size:13.5px}

  /* proforma como documento */
  .pf{background:var(--fibra);color:var(--tinta);margin-top:56px;padding:38px 40px 34px;position:relative;overflow:hidden}
  @media (max-width:720px){.pf{padding:26px 22px}}
  .pf-leon{position:absolute;right:-30px;bottom:-40px;width:270px;opacity:.05;pointer-events:none}
  .pf-top{display:flex;flex-wrap:wrap;gap:22px;justify-content:space-between;align-items:flex-start;
    border-bottom:2px solid var(--tinta);padding-bottom:20px}
  .pf-top img{height:44px}
  .pf-meta{font-family:var(--dato);font-size:12.5px;text-align:right;line-height:1.85}
  .pf-meta .no{font-size:15px;letter-spacing:.04em}
  .pf-meta .venc{color:var(--cereza)}
  .pf-partes{display:grid;grid-template-columns:1fr 1fr;gap:26px;padding:24px 0 26px}
  @media (max-width:700px){.pf-partes{grid-template-columns:1fr}}
  .pf-partes h4{font-family:var(--dato);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--acero-2);margin-bottom:8px}
  .pf-partes p{font-size:14px;line-height:1.7}
  .pf-partes b{font-family:var(--display);font-size:17px}
  .pf table{width:100%;border-collapse:collapse;font-size:14px}
  .pf table th{
    font-family:var(--dato);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
    text-align:left;color:var(--acero-2);font-weight:400;border-bottom:1px solid var(--linea-cla);padding:0 12px 10px 0;
  }
  .pf table td{padding:16px 12px 16px 0;vertical-align:top;border-bottom:1px solid var(--linea-cla)}
  .pf table .r{text-align:right;font-family:var(--dato);white-space:nowrap}
  .pf-abajo{display:grid;grid-template-columns:1.4fr .8fr;gap:34px;padding-top:24px}
  @media (max-width:820px){.pf-abajo{grid-template-columns:1fr}}
  .pf-notas p{font-size:13.5px;color:var(--acero-2);margin-bottom:9px}
  .pf-notas b{color:var(--tinta)}
  .pf-bancos{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px;font-family:var(--dato);font-size:11.5px;line-height:1.8}
  @media (max-width:560px){.pf-bancos{grid-template-columns:1fr}}
  .pf-tot div{display:flex;justify-content:space-between;gap:20px;font-family:var(--dato);font-size:13.5px;padding:9px 0;border-bottom:1px solid var(--linea-cla)}
  .pf-tot div:last-child{
    border-bottom:0;border-top:2px solid var(--tinta);margin-top:6px;padding-top:14px;
    font-size:17px;
  }

  /* ---------- DIRECTORIO ---------- */
  .dir{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--linea-osc);border:1px solid var(--linea-osc)}
  @media (max-width:900px){.dir{grid-template-columns:repeat(2,1fr)}}
  @media (max-width:520px){.dir{grid-template-columns:1fr}}
  .dir article{background:var(--horno-2);padding:24px 22px 26px}
  .dir b{font-family:var(--display);font-size:16.5px;font-weight:500;color:var(--calblanco);display:block}
  .dir .cargo{font-family:var(--dato);font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--naranja);margin:7px 0 12px}
  .dir p{font-family:var(--dato);font-size:12px;color:var(--acero);line-height:1.9;word-break:break-word}

  footer{border-top:1px solid var(--linea-osc);padding:34px 0 44px}
  footer .wrap{display:flex;flex-wrap:wrap;gap:16px 30px;justify-content:space-between;align-items:center}
  footer img{height:36px;display:block}
  footer p{font-family:var(--dato);font-size:11.5px;letter-spacing:.06em;color:var(--acero-2)}
"""
