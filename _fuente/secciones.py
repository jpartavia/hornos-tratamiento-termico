# -*- coding: utf-8 -*-
"""Secciones de la propuesta. El contenido es real; lo que falta va marcado con [[...]]."""

# ---------------------------------------------------------------- hero
def hero(logo_leon):
    return """
<header class="hero">
  <img class="hero-lion" src="@LEON@" alt="">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <span class="rot">Propuesta técnica · Elyon Industrial</span>
        <h1>Calor parejo,<br>ciclo tras <em>ciclo</em></h1>
      </div>
      <p class="bajada">Hornos de tratamiento térmico con <b>calefacción en tres caras</b>, cámara
      de fibra cerámica y control programable por recetas. La temperatura máxima la da cualquiera;
      lo difícil es que el calor quede igual en todo el volumen y que el ciclo se repita idéntico
      mañana.</p>
    </div>

    <!-- La escala con la que un tratamista lee la temperatura a ojo, por el color del metal.
         La ventana de operación del equipo va marcada sobre ella. -->
    <div class="escala">
      <svg viewBox="0 -18 1180 174" role="img" aria-label="Escala de incandescencia del acero, de 500 a 1300 grados centígrados, con la ventana de operación del horno marcada entre 65 y 1200 grados. Operación continua hasta 1100 grados.">
        <defs>
          <linearGradient id="inc" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0.00" stop-color="#1B1113"/>
            <stop offset="0.14" stop-color="#5E1206"/>
            <stop offset="0.32" stop-color="#A4240B"/>
            <stop offset="0.52" stop-color="#E14A05"/>
            <stop offset="0.68" stop-color="#FE6B03"/>
            <stop offset="0.84" stop-color="#FFC24A"/>
            <stop offset="1.00" stop-color="#FFF3DF"/>
          </linearGradient>
          <clipPath id="recorte"><rect id="revela" x="0" y="34" width="1180" height="34"/></clipPath>
        </defs>

        <rect x="0" y="34" width="1180" height="34" fill="#1B1113"/>
        <g clip-path="url(#recorte)">
          <rect x="0" y="34" width="1180" height="34" fill="url(#inc)"/>
        </g>

        <!-- marcas de temperatura, en su color real -->
        <g font-family="SF Mono, ui-monospace, Menlo, monospace" font-size="11.5" fill="#97A2A9">
          <g stroke="#EDE7DB" stroke-opacity=".30">
            <line x1="118" y1="68" x2="118" y2="80"/><line x1="378" y1="68" x2="378" y2="80"/>
            <line x1="638" y1="68" x2="638" y2="80"/><line x1="898" y1="68" x2="898" y2="80"/>
            <line x1="1158" y1="68" x2="1158" y2="80"/>
          </g>
          <text x="118" y="96" text-anchor="middle">500 °C</text>
          <text x="378" y="96" text-anchor="middle">700 °C</text>
          <text x="638" y="96" text-anchor="middle">900 °C</text>
          <text x="898" y="96" text-anchor="middle">1100 °C</text>
          <text x="1158" y="96" text-anchor="end">1300 °C</text>
          <text x="118" y="114" text-anchor="middle" fill="#5D6B73">rojo oscuro</text>
          <text x="378" y="114" text-anchor="middle" fill="#5D6B73">rojo cereza</text>
          <text x="638" y="114" text-anchor="middle" fill="#5D6B73">naranja</text>
          <text x="898" y="114" text-anchor="middle" fill="#5D6B73">amarillo</text>
          <text x="1158" y="114" text-anchor="end" fill="#5D6B73">blanco</text>
        </g>

        <!-- ventana de operación del equipo -->
        <g id="ventana">
          <path d="M2 26 V14 H1028 V26" fill="none" stroke="#FE6B03" stroke-width="1.6"/>
          <text x="8" y="8" font-family="SF Mono, ui-monospace, Menlo, monospace" font-size="11.5"
                fill="#FE6B03" letter-spacing="1.4">OPERACIÓN DEL EQUIPO · 65 – 1200 °C</text>
          <line x1="898" y1="30" x2="898" y2="72" stroke="#FFF3DF" stroke-width="1.4" stroke-dasharray="3 4"/>
          <text x="890" y="146" text-anchor="end" font-family="SF Mono, ui-monospace, Menlo, monospace"
                font-size="11.5" fill="#FFF3DF" letter-spacing="1.2">1100 °C CONTINUO</text>
          <text x="906" y="146" font-family="SF Mono, ui-monospace, Menlo, monospace"
                font-size="11.5" fill="#97A2A9" letter-spacing="1.2">1200 °C MÁXIMO</text>
        </g>
      </svg>
    </div>

    <div class="cifras">
      <div><div class="v num">1200<small>°C</small></div><div class="k">Temperatura máxima</div></div>
      <div><div class="v num">1100<small>°C</small></div><div class="k">Operación continua</div></div>
      <div><div class="v num">±1<small>°C</small></div><div class="k">Precisión de control</div></div>
      <div><div class="v num">3<small>caras</small></div><div class="k">Calefacción de la cámara</div></div>
    </div>
  </div>
</header>
""".replace("@LEON@", logo_leon)


# ---------------------------------------------------------------- recorrido (intro)
RECORRIDO_INTRO = """
<section class="sec sec--osc2" id="equipo">
  <div class="wrap">
    <div class="cab">
      <span class="rot">El equipo</span>
      <h2>Por fuera y por dentro</h2>
      <p>Al avanzar, el horno gira sobre sí mismo. Después la fotografía se disuelve en un corte
      técnico rotulado que muestra cómo está construido adentro. La etiqueta de la esquina dice
      siempre qué se está viendo: fotografía del equipo o esquema.</p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- modelos
MODELOS = """
<section class="sec sec--fibra" id="modelos">
  <div class="wrap">
    <div class="cab">
      <span class="rot rot--cla">Tres capacidades</span>
      <h2>Un mismo control, tres tamaños de cámara</h2>
      <p>Toque un modelo para compararlo. Lo que cambia es el volumen útil y la potencia; el
      control, el material de cámara, la precisión y la tensión de trabajo son los mismos en
      los tres.</p>
    </div>

    <div class="mods" id="mods" role="group" aria-label="Elegir modelo">
      <button type="button" data-m="0" aria-pressed="true">
        <span class="cod">STM-30-12W</span>
        <div class="lit num">30<span>litros</span></div>
        <div class="tip">Muffle de mesa · 7.5 kW</div>
        <div class="barra"><i style="width:31.25%"></i></div>
        <div class="barra-nota">volumen relativo</div>
      </button>
      <button type="button" data-m="1" aria-pressed="false">
        <span class="cod">STM-36-12</span>
        <div class="lit num">36<span>litros</span></div>
        <div class="tip">Muffle de mesa · 9 kW</div>
        <div class="barra"><i style="width:37.5%"></i></div>
        <div class="barra-nota">volumen relativo</div>
      </button>
      <button type="button" data-m="2" aria-pressed="false">
        <span class="cod">STD-96-12</span>
        <div class="lit num">96<span>litros</span></div>
        <div class="tip">Industrial de piso · 18 kW</div>
        <div class="barra"><i style="width:100%"></i></div>
        <div class="barra-nota">volumen relativo</div>
      </button>
    </div>

    <div class="tabla-envoltura">
      <table class="espec" id="espec"><tbody></tbody></table>
    </div>

    <div class="tension">
      <div class="tension-cab">
        <span class="rot rot--cla">Alimentación</span>
        <h3>Los tres se entregan en la tensión que usted tenga</h3>
      </div>
      <div class="tension-ops">
        <div><span class="v num">240<small>V</small></span><span class="k">estándar</span></div>
        <div><span class="v num">480<small>V</small></span><span class="k">estándar</span></div>
        <div><span class="v v--txt">Cualquiera</span><span class="k">bajo pedido</span></div>
      </div>
      <p>No hay que adaptar la planta al horno. Los equipos se fabrican para 240 V o 480 V como
      estándar, y para cualquier otra tensión si su instalación lo pide.</p>
    </div>

    <p class="comun">Iguales en los tres — <b>1200 °C</b> de diseño y <b>1100 °C</b> continuos ·
    precisión <b>± 1 °C</b> · termopar <b>tipo N</b> · cámara de <b>fibra cerámica de alúmina</b> ·
    calefacción por <b>tres caras</b> · controlador de <b>pantalla táctil</b> · marcado <b>CE</b> ·
    accesorios estándar de operación a temperatura.</p>
  </div>
</section>
"""

# ---------------------------------------------------------------- tecnología
TECNOLOGIA = """
<section class="sec sec--osc" id="tecnologia">
  <div class="wrap">
    <div class="cab">
      <span class="rot">Por qué el calor queda parejo</span>
      <h2>Seis decisiones de diseño, una sola meta</h2>
      <p>Cada subsistema lleva la magnitud que gobierna. En tratamiento térmico el número que
      vende es la temperatura máxima; el que importa es la uniformidad.</p>
    </div>
    <div class="subs">
      <article>
        <div class="medida">3 caras</div>
        <h3>Calefacción envolvente</h3>
        <p>Resistencia de alambre de alta aleación en las dos paredes laterales y el fondo.
        Calentar por tres caras a la vez es lo que reparte el calor en todo el volumen y no solo
        en el centro de la cámara.</p>
      </article>
      <article>
        <div class="medida">Alúmina</div>
        <h3>Cámara de fibra cerámica</h3>
        <p>Baja inercia térmica: el horno sube rápido y responde al control en vez de arrastrar
        calor acumulado. En el STD-96-12 la fibra es policristalina grado 1500.</p>
      </article>
      <article>
        <div class="medida">± 1 °C</div>
        <h3>Termopar tipo N</h3>
        <p>El tipo N sostiene la estabilidad mejor que el K en servicio prolongado a alta
        temperatura, que es exactamente el régimen de estos equipos.</p>
      </article>
      <article>
        <div class="medida">15 × 30</div>
        <h3>Recetas programables</h3>
        <p>Quince programas de treinta segmentos cada uno. Las rampas y los sostenimientos se
        programan una vez y se repiten igual en cada corrida, con descarga por USB.</p>
      </article>
      <article>
        <div class="medida">Doble capa</div>
        <h3>Envolvente aislada</h3>
        <p>Acero en doble capa con aislamiento interno de fibra cerámica: la superficie exterior
        se mantiene manejable mientras la cámara trabaja a temperatura de proceso.</p>
      </article>
      <article>
        <div class="medida">Techo</div>
        <h3>Chimenea de evacuación</h3>
        <p>Salida superior para los gases del proceso, con los accesorios estándar de operación
        segura: guantes de alta temperatura y pinzas para crisol.</p>
      </article>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- alcance
ALCANCE = """
<section class="sec sec--fibra" id="alcance">
  <div class="wrap">
    <div class="cab">
      <span class="rot rot--cla">Alcance</span>
      <h2>Qué entrega Elyon</h2>
      <p>La responsabilidad no termina en la bodega. Termina cuando el horno corre su primer ciclo
      con su gente operándolo.</p>
    </div>
    <div class="entrega">
      <div>Suministro del horno con sus accesorios estándar de operación</div>
      <div>Importación, trámites aduanales y transporte hasta el sitio</div>
      <div>Verificación del área y de la ruta de ingreso antes del despacho</div>
      <div>Definición de la conexión eléctrica con la tensión disponible en sitio</div>
      <div>Instalación y conexionado del equipo</div>
      <div>Puesta en marcha con pruebas de calentamiento y control</div>
      <div>Carga de la primera receta junto con su personal</div>
      <div>Capacitación de operación y cuidados, en español</div>
      <div>Garantía y soporte técnico local durante el período de cobertura</div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- definiciones
DEFINICIONES = """
<section class="sec sec--osc2" id="definiciones">
  <div class="wrap">
    <div class="cab">
      <span class="rot">Antes de la orden de compra</span>
      <h2>Dos cosas que hay que definir con usted</h2>
      <p>Preferimos ponerlas por escrito ahora y no encontrarlas el día de la instalación.</p>
    </div>
    <div class="abiertas">
      <article>
        <span class="marca">abierto</span>
        <div>
          <h3>Área de instalación y ruta de ingreso</h3>
          <p>Los modelos de mesa necesitan una superficie firme y nivelada con espacio de servicio
          alrededor. El de 96 litros es de piso y llega con su gabinete de control. Verificamos
          medidas y ruta antes del despacho.</p>
        </div>
      </article>
      <article>
        <span class="marca">abierto</span>
        <div>
          <h3>El proceso y el modelo</h3>
          <p>Qué se va a tratar, a qué temperatura y con qué ciclo. De eso depende la capacidad que
          conviene y la receta con la que se entrega el equipo configurado.</p>
        </div>
      </article>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- plan
PLAN = """
<section class="sec sec--fibra" id="plan">
  <div class="wrap">
    <div class="cab">
      <span class="rot rot--cla">Plan de ejecución</span>
      <h2>Cómo llega el equipo</h2>
      <p>El orden importa: cada etapa depende de que la anterior esté cerrada por escrito.</p>
    </div>
    <div class="etapas">
      <div><span class="n">01</span><h3>Orden de compra</h3><p>Modelo, tensión de operación y configuración confirmados.</p></div>
      <div><span class="n">02</span><h3>Producción en origen</h3><p>Fabricación con la configuración definida y pruebas de fábrica.</p></div>
      <div><span class="n">03</span><h3>Embarque</h3><p>Logística, documentación de origen y seguimiento del tránsito.</p></div>
      <div><span class="n">04</span><h3>Aduanas</h3><p>Importación y transporte interno hasta su sitio.</p></div>
      <div><span class="n">05</span><h3>Instalación</h3><p>Ubicación, conexionado eléctrico y verificación de servicios.</p></div>
      <div><span class="n">06</span><h3>Arranque</h3><p>Pruebas de calentamiento y control, receta inicial y capacitación.</p></div>
    </div>
  </div>
</section>
"""

def nav(logo):
    return """
<nav class="nav">
  <div class="wrap">
    <img src="@LOGO@" alt="Elyon Industrial">
    <div class="nav-links">
      <a href="#equipo">El equipo</a>
      <a href="#modelos">Modelos</a>
      <a href="#tecnologia">Tecnología</a>
      <a href="#alcance">Alcance</a>
      <a href="#definiciones">Definiciones</a>
      <a href="#plan">Plan</a>
    </div>
  </div>
</nav>
""".replace("@LOGO@", logo)


def pie(logo):
    return """
<footer>
  <div class="wrap">
    <img src="@LOGO@" alt="Elyon Industrial">
    <p>PROPUESTA DE SUMINISTRO · HORNOS DE TRATAMIENTO TÉRMICO · 2026</p>
  </div>
</footer>
""".replace("@LOGO@", logo)


TABLA_JS = """
<script>
(function(){
  "use strict";
  var M = [
    { cod:"STM-30-12W", tipo:"Muffle de mesa",     vol:"30 L", camara:"300 × 500 × 200 mm",
      kw:"7.5 kW", alim:"240 V o 480 V · 50/60 Hz",
      puerta:"Apertura lateral", fibra:"Fibra cerámica de alúmina", extra:"Chimenea en el techo" },
    { cod:"STM-36-12",  tipo:"Muffle de mesa",     vol:"36 L", camara:"300 × 400 × 300 mm",
      kw:"9 kW",   alim:"240 V o 480 V · 50/60 Hz",
      puerta:"Apertura lateral", fibra:"Fibra cerámica de alúmina",
      extra:"Envolvente de doble capa · pinza para crisol" },
    { cod:"STD-96-12",  tipo:"Industrial de piso", vol:"96 L", camara:"400 × 600 × 400 mm",
      kw:"18 kW",  alim:"240 V o 480 V · trifásico",
      puerta:"—", fibra:"Fibra cerámica policristalina grado 1500",
      extra:"Guantes de alta temperatura · pinzas para crisol" }
  ];
  var FILAS = [["Tipo","tipo"],["Volumen útil","vol"],["Cámara","camara"],["Potencia","kw"],
               ["Alimentación","alim"],["Puerta","puerta"],["Material de cámara","fibra"],
               ["Incluye","extra"]];

  var cuerpo = document.querySelector("#espec tbody");
  FILAS.forEach(function(f){
    var tr = document.createElement("tr");
    tr.innerHTML = '<th scope="row">' + f[0] + '</th>' +
      M.map(function(m,i){ return '<td data-c="' + i + '">' + m[f[1]] + '</td>'; }).join("");
    cuerpo.appendChild(tr);
  });

  var botones = document.querySelectorAll("#mods button");
  function elegir(i){
    botones.forEach(function(b){ b.setAttribute("aria-pressed", Number(b.dataset.m) === i ? "true" : "false"); });
    document.querySelectorAll("#espec [data-c]").forEach(function(el){
      el.classList.toggle("on", Number(el.dataset.c) === i);
    });
  }
  botones.forEach(function(b){ b.addEventListener("click", function(){ elegir(Number(b.dataset.m)); }); });
  elegir(0);

  /* La escala del hero se calienta una vez al entrar: es el único momento animado de la página. */
  var rev = document.getElementById("revela"), ven = document.getElementById("ventana");
  if (rev && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    rev.setAttribute("width", "0");
    if (ven) ven.style.opacity = "0";
    requestAnimationFrame(function(){
      rev.style.transition = "width 1.5s cubic-bezier(.22,.8,.24,1) .25s";
      rev.setAttribute("width", "1180");
      if (ven) { ven.style.transition = "opacity .6s ease 1.5s"; ven.style.opacity = "1"; }
    });
  }
})();
</script>
"""
