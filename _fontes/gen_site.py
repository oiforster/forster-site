#!/usr/bin/env python3
# Gerador do site da FORSTER (somosforster.com.br).
# Fonte da verdade de design: projeto "Site Forster design" no Claude Design.
# Este script emite a versao publicada em ../public: 7 paginas + style.css + site.js
# + robots/sitemap/_headers + redirect da raiz (forsterfilmes.com via GitHub Pages).
import json, pathlib

BASE = pathlib.Path(__file__).parent
PUB = BASE.parent / "public"
SITE = "https://somosforster.com.br"

WA_SAMUEL = "https://wa.me/5551981578225"
WA_SILVANA = "https://wa.me/5551980603512"
# Google Analytics 4: ID da propriedade (formato G-XXXXXXXXXX). Vazio = nenhuma medicao no site.
# Criar em analytics.google.com > Administrador > Criar propriedade > fluxo de dados Web.
GA4_ID = "G-0PH3FJRH7W"
MEDIA = "https://media.somosforster.com.br/video"

S_PATH = "M 80 24 C 76 8, 38 0, 22 14 C 8 28, 18 46, 42 54 C 66 62, 90 66, 82 88 C 74 103, 36 107, 20 92"

YT = {
    "pelizzer": ("KOMLI07dlZU", "https://youtu.be/KOMLI07dlZU"),
    "redentor": ("jNCegP_mqKc", "https://youtu.be/jNCegP_mqKc"),
    "fug": ("N7hQKsScBpA", "https://youtu.be/N7hQKsScBpA"),
    "saif1": ("nX1vJh0ubgo", "https://youtu.be/nX1vJh0ubgo"),
    "saif2": ("BTPIWZGBpGE", "https://youtu.be/BTPIWZGBpGE"),
    "natal": ("jkRyPAjaHi4", "https://youtu.be/jkRyPAjaHi4"),
    "curso": ("2kJOIY4Nn9Y", "https://youtu.be/2kJOIY4Nn9Y"),
    "clipe": ("F_XUpLjiW-M", "https://youtu.be/F_XUpLjiW-M"),
}

CSS = """body { margin: 0; background: #3A4638; font-family: 'Bricolage Grotesque', 'Avenir Next', 'Segoe UI', sans-serif; color: #262220; -webkit-font-smoothing: antialiased; }
a { color: #B0553B; text-decoration: none; }
a:hover { color: #93462F; }
.page { background: #F7F3EC; }
.wm { font-variation-settings: 'opsz' 96, 'wdth' 100, 'wght' 620; letter-spacing: 0.05em; line-height: 1; }
.lm { display: inline-flex; align-items: baseline; gap: 0.07em; }
.ds { font-variation-settings: 'opsz' 20, 'wght' 480; letter-spacing: 0.34em; }
.h { font-variation-settings: 'opsz' 96, 'wdth' 100, 'wght' 620; line-height: 1.15; }
.t { font-variation-settings: 'opsz' 12, 'wght' 400; }
.tb { font-variation-settings: 'opsz' 12, 'wght' 600; }
.t5 { font-variation-settings: 'opsz' 12, 'wght' 500; }
h1, h2, h3, p { margin: 0; font-weight: normal; font-size: inherit; }
.kick { font-variation-settings: 'opsz' 20, 'wght' 520; letter-spacing: 0.28em; font-size: 12px; color: #3A4638; }
.krow { display: flex; align-items: center; gap: 12px; }
.kbar { width: 20px; height: 2px; background: #B0553B; flex: 0 0 auto; }
.topbar { position: relative; display: flex; align-items: center; justify-content: space-between; gap: 16px 24px; padding: 20px clamp(20px, 8.3vw, 120px); border-bottom: 1px solid rgba(38,34,32,0.12); }
.navwrap { display: flex; align-items: center; gap: 22px; }
.navlinks { display: flex; align-items: center; gap: 12px 26px; }
.navlink { font-size: 14px; color: #262220; }
.menu-btn { display: none; background: none; border: 0; padding: 8px; margin: -8px; color: #262220; cursor: pointer; }
@media (max-width: 900px) {
  .menu-btn { display: flex; }
  .navlinks { display: none; position: absolute; top: 100%; left: 0; right: 0; z-index: 20; flex-direction: column; align-items: stretch; gap: 0; background: #F7F3EC; border-bottom: 1px solid rgba(38,34,32,0.12); padding: 6px clamp(20px, 8.3vw, 120px) 14px; }
  .navlinks.open { display: flex; }
  .navlink { font-size: 16px; padding: 13px 0; border-bottom: 1px solid rgba(38,34,32,0.08); }
  .navlink:last-child { border-bottom: 0; }
  .nav-on { border-bottom: 1px solid rgba(38,34,32,0.08); color: #B0553B; }
}
.nav-on { border-bottom: 2px solid #B0553B; padding-bottom: 3px; }
.btn { background: #B0553B; color: #F7F3EC; border-radius: 6px; display: inline-block; transition: transform .15s cubic-bezier(.22,1,.36,1), background .2s ease; }
.btn:hover { color: #F7F3EC; }
.btn-sm { padding: 10px 18px; font-size: 14px; }
.btn-lg { padding: 15px 26px; font-size: 16px; }
.lka { display: inline-flex; align-items: center; gap: 8px; }
.lka svg { transition: transform .25s cubic-bezier(.22,1,.36,1); }
.sec { padding: 84px clamp(20px, 8.3vw, 120px) 88px; border-top: 1px solid rgba(38,34,32,0.12); }
.heroH { position: relative; padding: 96px clamp(20px, 8.3vw, 120px) 88px; overflow: hidden; }
.heroP { padding: 80px clamp(20px, 8.3vw, 120px) 72px; }
.heroS { position: absolute; right: -70px; top: -40px; width: 640px; }
.heroS svg { width: 100%; height: auto; overflow: visible; }
.h1p { font-size: clamp(34px, 4.5vw, 50px); max-width: 760px; }
.sup { font-size: clamp(18px, 2vw, 21px); line-height: 1.55; max-width: 620px; }
.g4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 40px; }
.g3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 40px; }
.g2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 40px; }
.col { display: flex; flex-direction: column; }
.rule { height: 2px; background: #262220; }
.mosaic { display: flex; gap: 24px; flex-wrap: wrap; }
.tile { position: relative; display: flex; align-items: center; justify-content: center; transition: transform .3s cubic-bezier(.22,1,.36,1); }
.tile img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.tile .grad { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(38,34,32,0) 55%, rgba(38,34,32,0.6) 100%); }
.playc { position: relative; transition: transform .3s cubic-bezier(.22,1,.36,1); }
.t169 { width: 704px; height: 396px; }
.t916 { width: 223px; height: 396px; }
.thalf { flex: 1 1 320px; aspect-ratio: 16 / 9; height: auto; }
.ph { background: #EFE8DA; border: 1px dashed #8A817A; }
.tlabel { position: absolute; left: 18px; bottom: 16px; font-size: 13px; }
.qf { display: flex; gap: 64px; align-items: flex-start; }
.qf-photo { flex: 0 0 440px; height: 560px; overflow: hidden; border: 1px solid rgba(38,34,32,0.15); }
.qf-photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
.silv-photo { flex: 0 0 300px; border: 1px solid rgba(38,34,32,0.15); }
.silv-photo img { width: 100%; height: auto; display: block; }
.foot { background: #3A4638; padding: 44px clamp(20px, 8.3vw, 120px); display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap; }
.note { font-size: 13px; font-style: italic; color: #8A817A; }
.conf { display: flex; flex-wrap: wrap; gap: 18px 40px; font-size: 17px; }
@media (min-width: 1200px) {
  .conf { flex-wrap: nowrap; justify-content: space-between; gap: 16px; font-size: 15px; }
}
@media (max-width: 700px) {
  .conf { flex-direction: column; gap: 14px; }
}
@media (hover: hover) and (pointer: fine) {
  .btn:hover { transform: translateY(-1px); background: #9D4A33; }
  .lka:hover svg { transform: translateX(4px); }
  .tile:hover { transform: translateY(-4px); }
  .tile:hover .playc { transform: scale(1.08); }
}
@media (max-width: 980px) {
  .g4, .g3 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .qf { flex-direction: column; gap: 36px; }
  .qf-photo { flex: none; width: 100%; height: 440px; }
  .silv-photo { flex: none; width: min(300px, 78%); }
  .t169 { width: 100%; height: auto; aspect-ratio: 16 / 9; }
  .t916 { width: calc(50% - 12px); height: auto; aspect-ratio: 9 / 16; }
  .thalf { flex: none; width: 100%; }
  .heroS { width: min(72vw, 430px); right: -18vw; top: -20px; }
}
@media (max-width: 560px) {
  .g4, .g3, .g2 { grid-template-columns: 1fr; }
}
.prosa { max-width: 680px; }
.prosa p { font-size: 17px; line-height: 1.65; margin: 22px 0 0; }
.prosa h2 { font-size: 24px; margin-top: 44px; }
.prosa ul { font-size: 17px; line-height: 1.65; margin: 22px 0 0; padding-left: 22px; }
.prosa li + li { margin-top: 8px; }
.prosa a { color: #262220; }
.optout { font: inherit; font-variation-settings: 'opsz' 12, 'wght' 600; background: none; color: #262220; border: 1px solid rgba(38,34,32,0.4); border-radius: 6px; padding: 12px 20px; font-size: 15px; cursor: pointer; margin-top: 26px; }
.optout:hover { border-color: #B0553B; color: #B0553B; }
.optout-st { font-size: 14px; color: #8A817A; margin-top: 12px; }
@media (prefers-reduced-motion: no-preference) {
  .in { animation: rise .6s cubic-bezier(.22,1,.36,1) both; }
  .in1 { animation-delay: .05s; } .in2 { animation-delay: .12s; }
  .in3 { animation-delay: .19s; } .in4 { animation-delay: .26s; }
  .sdraw path { stroke-dasharray: 400; stroke-dashoffset: 400; animation: draw 2.4s cubic-bezier(.45,.05,.55,.95) .5s forwards; }
  .heroS.sdraw path { animation-duration: 3.6s; animation-delay: .7s; }
  @keyframes draw { to { stroke-dashoffset: 0; } }
  @keyframes rise { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: none; } }
  html.js .rv { opacity: 0; transform: translateY(20px); transition: opacity .7s cubic-bezier(.22,1,.36,1), transform .7s cubic-bezier(.22,1,.36,1); }
  html.js .rv.vis { opacity: 1; transform: none; }
}
"""

JS = """if ('IntersectionObserver' in window) {
  document.documentElement.classList.add('js');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('vis'); io.unobserve(en.target); }
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
}
var mb = document.querySelector('.menu-btn');
if (mb) {
  var menu = document.getElementById('menu');
  mb.addEventListener('click', function () {
    var aberto = menu.classList.toggle('open');
    mb.setAttribute('aria-expanded', aberto ? 'true' : 'false');
    mb.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
  });
  menu.addEventListener('click', function (e) {
    if (e.target.closest('a')) { menu.classList.remove('open'); mb.setAttribute('aria-expanded', 'false'); }
  });
}
document.addEventListener('click', function (e) {
  var el = e.target.closest('[data-yt], [data-video]');
  if (!el) return;
  e.preventDefault();
  var box = document.createElement('div');
  box.className = el.className.replace('tile', 'tile-live');
  box.setAttribute('style', (el.getAttribute('style') || '') + '; position: relative; background: #262220; overflow: hidden;');
  var m;
  if (el.dataset.yt) {
    m = document.createElement('iframe');
    m.src = 'https://www.youtube-nocookie.com/embed/' + el.dataset.yt + '?autoplay=1&rel=0';
    m.allow = 'autoplay; encrypted-media; picture-in-picture';
    m.allowFullscreen = true;
    m.setAttribute('style', 'position: absolute; inset: 0; width: 100%; height: 100%; border: 0;');
  } else {
    m = document.createElement('video');
    m.src = el.dataset.video;
    m.controls = true; m.autoplay = true; m.playsInline = true;
    m.setAttribute('style', 'position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain;');
  }
  box.appendChild(m);
  el.replaceWith(box);
  var rotulo = el.querySelector('.tlabel');
  medir('play_video', { video: el.dataset.yt || el.dataset.video, titulo: rotulo ? rotulo.textContent.trim() : '' });
});
// Medicao (Google Analytics 4): so faz algo quando a tag esta na pagina.
var PESSOAS = __PESSOAS__;
function medir(nome, dados) {
  if (typeof gtag === 'function') gtag('event', nome, dados || {});
}
document.addEventListener('click', function (e) {
  var a = e.target.closest('a[href]');
  if (!a || a.dataset.yt || a.dataset.video) return;
  var href = a.getAttribute('href') || '';
  var texto = (a.textContent || '').trim().slice(0, 60);
  if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp') !== -1) {
    var pessoa = 'outro';
    for (var num in PESSOAS) { if (href.indexOf(num) !== -1) pessoa = PESSOAS[num]; }
    medir('clique_whatsapp', { pessoa: pessoa, texto: texto });
  } else if (href.indexOf('instagram.com') !== -1) {
    medir('clique_instagram', { texto: texto });
  } else if (href.indexOf('tel:') === 0) {
    medir('clique_telefone', { numero: href.slice(4) });
  } else if (href.indexOf('mailto:') === 0) {
    medir('clique_email', { email: href.slice(7) });
  } else if (/^https?:/.test(href) && a.hostname !== location.hostname) {
    medir('clique_externo', { destino: a.hostname, texto: texto });
  }
});
var ob = document.querySelector('[data-optout]');
if (ob) {
  var oid = ob.dataset.optout, ost = document.getElementById('optout-st');
  function semMedicao() { try { return localStorage.getItem('sem-medicao') === '1'; } catch (err) { return false; } }
  function pintar() {
    var off = semMedicao();
    ob.textContent = off ? 'Voltar a contar minhas visitas' : 'N\u00e3o contar minhas visitas';
    ost.textContent = off ? 'Feito. Suas visitas n\u00e3o s\u00e3o contadas neste navegador.' : 'Suas visitas neste navegador est\u00e3o sendo contadas.';
  }
  ob.addEventListener('click', function () {
    var off = !semMedicao();
    try { off ? localStorage.setItem('sem-medicao', '1') : localStorage.removeItem('sem-medicao'); } catch (err) {}
    window['ga-disable-' + oid] = off;
    pintar();
  });
  pintar();
}
"""
JS = JS.replace("__PESSOAS__", json.dumps({WA_SAMUEL.rsplit("/", 1)[1]: "samuel", WA_SILVANA.rsplit("/", 1)[1]: "silvana"}))

def s_svg(stroke, sw="14", cls="", inline_size=True):
    size = ' style="overflow: visible; width: 0.70em; height: 0.756em; position: relative; top: 0.042em;"' if inline_size else ''
    c = f' class="{cls}"' if cls else ''
    return (f'<svg{c} viewBox="0 0 100 108"{size} aria-hidden="true">'
            f'<path d="{S_PATH}" fill="none" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" transform="rotate(-2 50 54)"></path></svg>')

def lockup(px_css, color, s_cls=""):
    return (f'<div class="lm" style="font-size: {px_css}; color: {color};">'
            f'<span class="wm" style="margin-right: -0.05em;">FOR</span>'
            f'{s_svg("currentColor", cls=s_cls)}'
            f'<span class="wm">TER</span></div>')

ARROW = ('<svg width="15" height="12" viewBox="0 0 15 12" fill="none" style="flex: 0 0 auto;">'
         '<path d="M1 6h12M9 1.5 13.5 6 9 10.5" stroke="currentColor" stroke-width="1.8" '
         'stroke-linecap="round" stroke-linejoin="round"></path></svg>')

def play(color):
    return (f'<svg class="playc" width="54" height="54" viewBox="0 0 54 54" fill="none">'
            f'<circle cx="27" cy="27" r="25.5" stroke="{color}" stroke-width="2"></circle>'
            f'<path d="M22 18.5v17l14-8.5z" fill="{color}"></path></svg>')

NAV_ITEMS = [("inicio", "In&iacute;cio", "/"),
             ("trabalhos", "Trabalhos", "/trabalhos"),
             ("acompanhamento", "Acompanhamento", "/acompanhamento"),
             ("mentoria", "Mentoria", "/mentoria"),
             ("sites", "Sites", "/sites"),
             ("encomenda", "Sob encomenda", "/sob-encomenda")]

def nav(active=""):
    links = "".join(
        f'<a class="navlink t5{" nav-on" if key == active else ""}" href="{href}">{label}</a>'
        for key, label, href in NAV_ITEMS)
    burger = ('<button class="menu-btn" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu">'
              '<svg width="22" height="16" viewBox="0 0 22 16" fill="none" aria-hidden="true">'
              '<path d="M1 1.5h20M1 8h20M1 14.5h20" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg></button>')
    return (f'<nav class="topbar"><a href="/" style="color: #262220;" aria-label="FORSTER, p&aacute;gina inicial">{lockup("20px", "currentColor")}</a>'
            f'<div class="navwrap"><div class="navlinks" id="menu">{links}</div>'
            f'<a class="tb btn btn-sm" href="{WA_SAMUEL}" target="_blank" rel="noopener">Conversar</a>{burger}</div></nav>')

def kicker(text, extra_cls=""):
    return f'<div class="krow{extra_cls}"><div class="kbar"></div><div class="kick">{text}</div></div>'

def steps_grid(items, grid="g4", numbered=True):
    cols = ""
    for i, (title, desc) in enumerate(items, 1):
        num = f'<div class="t5" style="font-size: 13px; color: #8A817A; margin-top: 22px;">0{i}</div>' if numbered else ''
        mt = ' margin-top: 12px;' if numbered else ' margin-top: 22px;'
        cols += (f'<div class="col"><div class="rule rulex"></div>{num}'
                 f'<h3 class="h" style="font-size: 24px;{mt}">{title}</h3>'
                 f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin: 14px 0 0;">{desc}</p></div>')
    return f'<div class="{grid} rv" style="margin-top: 44px;">{cols}</div>'

def hero_page(kick, h1, sup, cta_label="Conversar no WhatsApp", cta_href=WA_SAMUEL, ver_trabalhos=True):
    ver = (f'<a class="tb lka" href="/trabalhos" style="font-size: 16px; color: #262220; border-bottom: 1px solid rgba(38,34,32,0.4); padding-bottom: 2px;">Ver trabalhos {ARROW}</a>'
           if ver_trabalhos else '')
    return (f'<header class="heroP">{kicker(kick, " in")}'
            f'<h1 class="h h1p in in1" style="margin: 26px 0 0;">{h1}</h1>'
            f'<p class="t sup in in2" style="margin: 24px 0 0;">{sup}</p>'
            f'<div class="in in3" style="display: flex; align-items: center; gap: 28px; margin-top: 36px; flex-wrap: wrap;">'
            f'<a class="tb btn btn-lg" href="{cta_href}" target="_blank" rel="noopener">{cta_label}</a>{ver}</div></header>')

def tile(cls_size, bg, label, light=True, dashed=False, href="", img="", alt="", yt="", video=""):
    if dashed:
        return (f'<div class="tile ph {cls_size}"><div class="t note" style="padding: 0 20px; text-align: center;">{label}</div></div>')
    ink = "#F7F3EC" if (light or img) else "#262220"
    foto = ''
    if img:
        foto = (f'<img src="/img/{img}" alt="{alt or label}" loading="lazy">'
                f'<div class="grad"></div>')
    inner = (f'{foto}{play(ink)}<div class="t5 tlabel" style="color: {ink};">{label}</div>')
    style = f'background: {bg}; overflow: hidden;'
    data = ''
    if yt:
        data = f' data-yt="{yt}"'
    if video:
        data = f' data-video="{video}"'
        href = href or video
    if href:
        return (f'<a class="tile {cls_size}" href="{href}"{data} target="_blank" rel="noopener" style="{style}">{inner}</a>')
    return (f'<div class="tile {cls_size}" style="{style}">{inner}</div>')

def convite(heading, text, cta_label, cta_href):
    return (f'<div class="sec"><div class="rv">'
            f'<h2 class="h" style="font-size: clamp(32px, 4vw, 44px);">{heading}</h2>'
            f'<p class="t" style="font-size: 18px; line-height: 1.6; margin: 18px 0 0; max-width: 520px;">{text}</p>'
            f'<a class="tb btn btn-lg" href="{cta_href}" target="_blank" rel="noopener" style="margin-top: 28px;">{cta_label}</a>'
            f'</div></div>')

CONVITE_PADRAO = convite("Vamos conversar?",
                         "Conte para a gente o que voc&ecirc; precisa. Quem l&ecirc; e responde &eacute; o Samuel ou a Silvana.",
                         "Conversar no WhatsApp", WA_SAMUEL)
CONVITE_MENTORIA = convite("Se esse &eacute; o teu momento",
                           "Manda uma mensagem e vamos conversar para entender o que faz sentido pra ti.",
                           "Falar com a Silvana pelo WhatsApp", WA_SILVANA)

REGIAO = (f'<div class="sec"><div class="rv" style="max-width: 720px;">{kicker("ONDE A GENTE ATENDE")}'
          f'<h2 class="h" style="font-size: 28px; margin-top: 26px;">De Igrejinha para o Vale do Paranhana, Novo Hamburgo, Gramado e Canela.</h2>'
          f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0;">O ateliê fica em Igrejinha, e a maior parte dos nossos clientes está por perto: Três Coroas, Taquara, Parobé, Rolante, Novo Hamburgo, Gramado e Canela. Para gravar, a gente vai até você com toda a estrutura. Para um site, a conversa pode ser por chamada de vídeo, e o trabalho chega por link.</p></div></div>')

def faq(items):
    rows = "".join(
        f'<div class="col"><div class="rule rulex"></div>'
        f'<h3 class="h" style="font-size: 22px; margin-top: 22px;">{q}</h3>'
        f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin: 14px 0 0;">{a}</p></div>'
        for q, a in items)
    return (f'<div class="sec"><div class="rv">{kicker("PERGUNTAS FREQUENTES")}</div>'
            f'<div class="g2 rv" style="margin-top: 44px;">{rows}</div></div>')

def faq_ld(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

FAQ_ACOMP = [
    ("Preciso aparecer nos vídeos?",
     "Na maior parte dos casos, sim, e é isso que faz a diferença: quem confia em você quer ver você. A gente prepara o roteiro, liga o teleprompter e cuida da luz, então você só precisa aparecer. Quando faz sentido, o conteúdo também mostra a equipe, o produto ou o lugar."),
    ("Quanto conteúdo sai por mês?",
     "Depende do plano. A base é uma sessão de gravação de até quatro horas, que rende um conjunto de vídeos curtos, além dos posts do mês com legenda. A gente monta o plano com você na conversa inicial."),
    ("Vocês também publicam?",
     "Sim. A gente publica os vídeos, os posts e as legendas nos seus perfis. Você fica livre para cuidar do seu negócio."),
    ("Como começa?",
     "Com um mês de diagnóstico. Antes de gravar qualquer coisa, a gente estuda tudo o que você já publicou, o seu mercado e os seus concorrentes, e monta o documento com as diretrizes do trabalho. Só depois o ciclo mensal começa."),
]
FAQ_MENT = [
    ("Quanto tempo dura?",
     "Três meses, com seis encontros quinzenais de uma hora e meia e suporte leve pelo WhatsApp entre eles, no teu ritmo."),
    ("Preciso já publicar conteúdo?",
     "Não. O acompanhamento começa pelo teu momento e pela tua história. Se tu já publica, a gente organiza o que existe. Se ainda não, a gente constrói do zero, com um calendário que cabe na tua rotina."),
    ("Como funciona a parte de vídeo?",
     "É um encontro prático com o Samuel: luz, enquadramento e cenário com o que tu já tem em casa, presença em vídeo, teleprompter e gravação por blocos. Tu recebe retorno sobre um vídeo que gravou e sai com o plano do primeiro lote."),
]
FAQ_SITES = [
    ("Preciso ter o texto pronto?",
     "Não. O texto nasce da nossa conversa: você conta a sua história e os seus serviços, e a gente escreve. Você revisa tudo antes de publicar."),
    ("Quanto tempo leva?",
     "Depende do tamanho do site e do quanto já existe de material. A gente combina o prazo na conversa inicial, e o que mais pesa é o texto, porque é ali que o site ganha a sua cara."),
    ("O site fica no meu domínio?",
     "Sim. O site é publicado no seu endereço, e o domínio fica no seu nome. Se você ainda não tem um, a gente ajuda a registrar."),
    ("O site vai aparecer no Google?",
     "O site sai com a estrutura que o Google precisa para entender quem você é, o que faz e onde atende: títulos, descrições, dados da empresa e mapa do site. Aparecer bem nas buscas da sua região é um trabalho que continua depois, e a gente orienta como."),
]
FAQ_ENC = [
    ("Quanto tempo leva um vídeo institucional?",
     "A gravação costuma caber em uma sessão de até quatro horas, da montagem ao desmonte. Antes dela vêm o briefing e o roteiro, e depois a edição e a sua aprovação por link. O prazo total a gente combina no briefing, de acordo com o tamanho do filme."),
    ("O roteiro está incluso?",
     "Sim. A gente conversa, escreve o roteiro e manda para você aprovar antes da sessão. No dia, o teleprompter faz o resto: ninguém precisa decorar nada."),
    ("Vocês gravam com drone?",
     "Sim, quando a história pede. As imagens aéreas entram no filme para mostrar a fábrica, a sede, a paisagem ou o tamanho do que você faz."),
    ("Onde posso usar o vídeo?",
     "No site, nas redes sociais, em apresentações para clientes, em feiras e em anúncios. A gente entrega o filme pronto nos formatos que você precisa."),
]

FOOTER = (f'<footer class="foot"><div>{lockup("19px", "#F7F3EC")}'
          '<div class="t" style="font-size: 13px; color: #D9C29A; margin-top: 10px;">Conte&uacute;do feito a quatro m&atilde;os.</div></div>'
          '<div class="t" style="font-size: 14px; color: rgba(247,243,236,0.9);"><a href="https://www.instagram.com/somosforster" style="color: rgba(247,243,236,0.9);">@somosforster</a> &middot; Igrejinha, Rio Grande do Sul &middot; <a href="/blog/" style="color: rgba(247,243,236,0.9);">Blog</a> &middot; <a href="/privacidade" style="color: rgba(247,243,236,0.7);">Privacidade</a></div></footer>')

# ---------------------------------------------------------------- paginas

def door(num, titulo, desc, href):
    return (f'<div class="col"><div class="rule rulex"></div>'
            f'<div class="t5" style="font-size: 13px; color: #8A817A; margin-top: 22px;">{num}</div>'
            f'<h3 class="h" style="font-size: 26px; margin-top: 12px; min-height: 64px;">{titulo}</h3>'
            f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin: 14px 0 0;">{desc}</p>'
            f'<a class="tb lka" href="{href}" style="font-size: 14px; margin-top: auto; padding-top: 18px;">Como funciona {ARROW}</a></div>')

def page_home():
    hero = (f'<header class="heroH"><div class="heroS">{s_svg("#D9C29A", sw="3", cls="sdraw", inline_size=False)}</div>'
            f'<div style="position: relative;">'
            f'<div class="in">{lockup("clamp(64px, 9.2vw, 132px)", "#262220", s_cls="sdraw")}</div>'
            f'<h1 class="ds in in1" style="font-size: clamp(15px, 1.5vw, 21px); margin-top: 18px; color: #262220;">ATELI&Ecirc; DE CONTE&Uacute;DO EM IGREJINHA, RS</h1>'
            f'<p class="t sup in in2" style="margin: 40px 0 0;">Planejamento, textos e v&iacute;deos feitos a quatro m&atilde;os para quem quer construir presen&ccedil;a com consist&ecirc;ncia. Atendimento direto de quem cria: Samuel e Silvana.</p>'
            f'<div class="in in3" style="display: flex; align-items: center; gap: 28px; margin-top: 40px; flex-wrap: wrap;">'
            f'<a class="tb btn btn-lg" href="{WA_SAMUEL}" target="_blank" rel="noopener">Conversar no WhatsApp</a>'
            f'<a class="tb lka" href="/trabalhos" style="font-size: 16px; color: #262220; border-bottom: 1px solid rgba(38,34,32,0.4); padding-bottom: 2px;">Ver trabalhos {ARROW}</a>'
            f'</div></div></header>')

    portas = (f'<div class="sec"><div class="rv" style="margin-bottom: 44px;">{kicker("O QUE A GENTE FAZ")}</div>'
              f'<div class="g4 rv">'
              + door("01", "Acompanhamento mensal",
                     "A gente estuda o seu perfil, o seu mercado e os seus concorrentes e, a partir disso, cuida da sua comunica&ccedil;&atilde;o digital: roteiros, v&iacute;deos, postagens, site e perfil no Google. Voc&ecirc; grava, e o resto &eacute; com a gente.",
                     "/acompanhamento")
              + door("02", "Mentoria",
                     "Para quem quer aprender a comunicar, em encontros diretos com quem faz isso todos os dias.",
                     "/mentoria")
              + door("03", "Sites",
                     "Um site simples, r&aacute;pido e sob medida, que conta a sua hist&oacute;ria e aparece na busca.",
                     "/sites")
              + door("04", "Sob encomenda",
                     "Um v&iacute;deo com come&ccedil;o, meio e fim: institucional, v&iacute;deo de produto, a hist&oacute;ria da sua empresa bem contada.",
                     "/sob-encomenda")
              + '</div></div>')

    trabalhos = (f'<div class="sec"><div class="rv" style="display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap;">{kicker("TRABALHOS")}'
                 f'<a class="tb lka" href="/trabalhos" style="font-size: 14px;">Ver todos os trabalhos {ARROW}</a></div>'
                 f'<div class="mosaic rv" style="margin-top: 44px;">'
                 + tile("t169", "#3A4638", "Institucional &middot; Pelizzer Im&oacute;veis", video=f"{MEDIA}/institucional-pelizzer-imoveis.mp4", img="thumb-institucional-pelizzer-imoveis.jpg", alt="V&iacute;deo institucional dos 30 anos da Pelizzer Im&oacute;veis")
                 + tile("t916", "#2B2724", "Conte&uacute;do mensal &middot; &Oacute;ticas Casa Marco", video="/video/reel-oticas-casa-marco.mp4", img="capa-reel-oticas-casa-marco.jpg", alt="Reel de produto das &Oacute;ticas Casa Marco")
                 + tile("t916", "#3A4638", "Conte&uacute;do mensal &middot; Fyber Show Piscinas", video="/video/reel-fyber-show.mp4", img="capa-reel-fyber-show.jpg", alt="Reel institucional da Fyber Show Piscinas")
                 + '</div></div>')

    quemfaz = (f'<div class="sec"><div class="qf rv">'
               f'<div class="qf-photo"><img src="/img/samuel-silvana-familia-corrida.jpg" alt="Samuel, Silvana e os filhos na chegada de uma prova de corrida" loading="lazy"></div>'
               f'<div style="padding-top: 26px;">{kicker("QUEM FAZ")}'
               f'<h2 class="h" style="font-size: 30px; margin-top: 26px;">Quem atende &eacute; quem cria.</h2>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0; max-width: 520px;">Forster &eacute; sobrenome: o de Samuel e o de Silvana. O ateli&ecirc; funciona na nossa casa, em Igrejinha, e cada trabalho passa pelas m&atilde;os dos dois, do planejamento &agrave; entrega.</p>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 16px 0 0; max-width: 520px;">A Forster &eacute; feita por quem acredita que o trabalho se adapta &agrave; filosofia de vida, e n&atilde;o o contr&aacute;rio. Nosso sobrenome vem do alem&atilde;o e quer dizer guardi&atilde;o: &eacute; assim que a gente cuida da comunica&ccedil;&atilde;o de quem confia na Forster.</p>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 16px 0 0; max-width: 520px;">A gente atende Igrejinha, o Vale do Paranhana, Novo Hamburgo, Gramado e Canela, e vai at&eacute; voc&ecirc; para gravar.</p>'
               f'</div></div></div>')

    nomes = ["&Oacute;ticas Casa Marco", "Fyber Show Piscinas", "Catarata Center", "Prisma Especialidades",
             "Col&eacute;gio Luterano Redentor", "Psic&oacute;loga Martina Schneider", "Vanessa Mainardi", "Teclib - GLPI"]
    confianca = (f'<div class="sec" style="padding-top: 64px; padding-bottom: 72px;"><div class="rv">{kicker("QUEM CONFIA NA FORSTER")}'
                 '<div class="conf" style="margin-top: 30px;">'
                 + "".join(f'<div class="h" style="color: rgba(38,34,32,0.55); white-space: nowrap;">{n}</div>' for n in nomes)
                 + '</div></div></div>')

    return hero + portas + trabalhos + quemfaz + confianca

def page_acompanhamento():
    hero = hero_page("ACOMPANHAMENTO MENSAL", "Planejamento, produ&ccedil;&atilde;o e const&acirc;ncia.",
                     "No nosso acompanhamento mensal, a base da sua comunica&ccedil;&atilde;o digital fica por nossa conta. Antes de produzir qualquer conte&uacute;do, a gente estuda a fundo tudo o que voc&ecirc; j&aacute; publicou, o seu mercado e os seus concorrentes, at&eacute; entender o que funciona com o seu p&uacute;blico e qual espa&ccedil;o ainda est&aacute; livre pra voc&ecirc; ocupar. Desse estudo nascem as diretrizes que v&atilde;o guiar todo o trabalho. A partir delas, a gente cuida de tudo, do roteiro &agrave; postagem, do site ao seu perfil no Google Meu Neg&oacute;cio, sempre de olho no que acontece de novo na sua &aacute;rea. No dia da grava&ccedil;&atilde;o, os roteiros j&aacute; est&atilde;o prontos: voc&ecirc; grava e o resto &eacute; com a gente. Todo m&ecirc;s, os n&uacute;meros mostram o resultado do que j&aacute; foi feito e o que precisa ser ajustado. A qualidade de produ&ccedil;&atilde;o dos nossos v&iacute;deos eleva muito a sua imagem no digital, mas o v&iacute;deo &eacute; uma parte do trabalho, n&atilde;o o trabalho inteiro. &Eacute; isso que a gente chama de conte&uacute;do feito a quatro m&atilde;os.")
    como = (f'<div class="sec"><div class="rv">{kicker("COMO FUNCIONA")}'
            f'<h2 class="h" style="font-size: 28px; margin-top: 26px;">Primeiro a gente entende. Depois a gente cria.</h2></div>'
            + steps_grid([
                ("Estudo", "Antes de qualquer conte&uacute;do, a gente estuda tudo o que voc&ecirc; j&aacute; publicou, o seu mercado e os seus concorrentes: o que funcionou, o que n&atilde;o funcionou, os assuntos que eles abordam e o espa&ccedil;o que ainda est&aacute; livre para voc&ecirc;."),
                ("Diretrizes", "Desse estudo sai um documento com as diretrizes do seu trabalho: os assuntos, a linguagem e os servi&ccedil;os que merecem destaque. &Eacute; ele que guia cada roteiro, cada post e cada v&iacute;deo."),
                ("Roteiro", "Os roteiros dos v&iacute;deos do m&ecirc;s nascem dessas diretrizes. No dia da grava&ccedil;&atilde;o eles j&aacute; est&atilde;o prontos no teleprompter, ent&atilde;o voc&ecirc; n&atilde;o precisa decorar nem improvisar nada."),
                ("Grava&ccedil;&atilde;o", "A gente vai at&eacute; voc&ecirc; com tudo que &eacute; necess&aacute;rio. Voc&ecirc; s&oacute; precisa aparecer."),
                ("Produ&ccedil;&atilde;o e publica&ccedil;&atilde;o", "Cada v&iacute;deo, carrossel e post sai com a sua identidade visual e o seu tom de voz, e a gente publica nas suas redes. Voc&ecirc; fica livre para cuidar do seu neg&oacute;cio."),
                ("E come&ccedil;a de novo", "Ao longo do m&ecirc;s, a gente segue pesquisando not&iacute;cias e estudos da sua &aacute;rea e troca ideias com voc&ecirc; sempre que aparece algo novo. Todo m&ecirc;s, um relat&oacute;rio mostra os n&uacute;meros e o que precisa ser ajustado."),
            ], grid="g3") + '</div>')
    pratica = (f'<div class="sec"><div class="qf rv" style="gap: 80px; align-items: flex-start;">'
               f'<div style="max-width: 560px;">{kicker("COMO &Eacute; NA PR&Aacute;TICA")}'
               f'<h2 class="h" style="font-size: 28px; margin-top: 26px;">Nos bastidores de uma sess&atilde;o.</h2>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0;">Um trecho real de sess&atilde;o: luz montada, teleprompter rodando e voc&ecirc; s&oacute; precisando aparecer.</p></div>'
               f'<div style="flex: 0 0 300px; border: 1px solid rgba(38,34,32,0.15);">'
               f'<video src="/video/bastidores-sessao.mp4" autoplay muted loop playsinline style="width: 100%; aspect-ratio: 9 / 16; object-fit: cover; display: block;"></video></div>'
               f'</div></div>')
    seugeito = (f'<div class="sec"><div class="qf rv" style="gap: 80px;">'
                f'<div style="max-width: 620px;">{kicker("DO SEU JEITO")}'
                f'<h2 class="h" style="font-size: 30px; margin-top: 26px;">E se voc&ecirc; preferir gravar por conta.</h2>'
                f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0;">Alguns clientes gravam os pr&oacute;prios v&iacute;deos, e funciona: a gente define as pautas, prepara os roteiros, orienta a capta&ccedil;&atilde;o e cuida da edi&ccedil;&atilde;o e dos textos. O padr&atilde;o continua sendo o do ateli&ecirc;, com a sua rotina mais leve e o seu jeito na tela.</p>'
                f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 16px 0 0;">&Eacute; um caminho natural para quem quer ganhar autonomia sem abrir m&atilde;o de acompanhamento.</p></div>'
                f'<div style="flex: 0 0 260px;"><div style="border: 1px solid rgba(38,34,32,0.15); overflow: hidden;">'
                f'<img src="/img/manual-de-campo-mentoria.jpg" alt="Manual de campo de grava&ccedil;&atilde;o feito pela Forster" loading="lazy" style="width: 100%; display: block;"></div>'
                f'<p class="t note" style="margin: 12px 0 0;">Manual de campo sob medida, feito para quem grava por conta.</p></div>'
                f'</div></div>')
    incluso_itens = ["Estudo de tudo o que voc&ecirc; j&aacute; publicou",
                     "Pesquisa do seu mercado e dos seus concorrentes",
                     "Documento com as diretrizes que guiam todo o trabalho",
                     "Roteiros dos v&iacute;deos para o Instagram e o YouTube",
                     "Grava&ccedil;&atilde;o e produ&ccedil;&atilde;o dos v&iacute;deos",
                     "Identidade visual e produ&ccedil;&atilde;o dos carross&eacute;is, posts e cards",
                     "Publica&ccedil;&atilde;o nas suas redes",
                     "Pesquisa cont&iacute;nua de not&iacute;cias e estudos da sua &aacute;rea",
                     "Cria&ccedil;&atilde;o e cuidado do site",
                     "Cuidado com o seu perfil no Google Meu Neg&oacute;cio",
                     "Relat&oacute;rio mensal com os n&uacute;meros e o que precisa ser ajustado"]
    incluso = (f'<div class="sec"><div class="rv">{kicker("DO QUE A GENTE CUIDA")}<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0;">O conjunto de cada cliente &eacute; definido na proposta.</p></div>'
               '<div class="g3 rv" style="margin-top: 40px;">'
               + "".join(f'<div><div class="rule rulex" style="height: 1px; background: rgba(38,34,32,0.35);"></div>'
                         f'<p class="t5" style="font-size: 16px; margin: 16px 0 0;">{i}</p></div>' for i in incluso_itens)
               + '</div></div>')
    perfis_data = [("perfil-instagram-oticas-casa-marco.jpg", "@oticas_casamarco"),
                   ("perfil-instagram-catarata-center.jpg", "@cataratacenter"),
                   ("perfil-instagram-fyber-show.jpg", "@fybershow"),
                   ("perfil-instagram-colegio-redentor.jpg", "@colegioredentor")]
    cards = "".join(
        f'<div><div style="aspect-ratio: 9 / 16; overflow: hidden; border: 1px solid rgba(38,34,32,0.15);">'
        f'<img src="/img/{f}" alt="Feed do Instagram {h}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: top;"></div>'
        f'<div class="t5" style="font-size: 14px; margin-top: 12px;">{h}</div></div>'
        for f, h in perfis_data)
    trab = (f'<div class="sec"><div class="rv">{kicker("PERFIS QUE A GENTE CUIDA COM CONST&Acirc;NCIA")}</div>'
            f'<div class="g4 rv" style="margin-top: 44px;">{cards}</div>'
            f'<a class="tb lka rv" href="/trabalhos" style="font-size: 14px; margin-top: 28px;">Ver os trabalhos destes perfis {ARROW}</a></div>')
    return hero + como + pratica + seugeito + incluso + trab + REGIAO + faq(FAQ_ACOMP)

def page_mentoria():
    hero = hero_page("MENTORIA", "Da teoria &agrave; pr&aacute;tica.",
                     "Acompanhamento em Comunica&ccedil;&atilde;o Consciente: um processo individual para transformar o que tu j&aacute; sabe em presen&ccedil;a real, com clareza, rotina e conte&uacute;do que flui. A Silvana conduz; a parte de v&iacute;deo &eacute; com o Samuel.",
                     cta_label="Falar com a Silvana pelo WhatsApp", cta_href=WA_SILVANA, ver_trabalhos=False)
    silvana = (f'<div class="sec"><div class="qf rv">'
               f'<div class="silv-photo">'
               f'<img src="/img/silvana-forster.jpg" alt="Silvana Forster" loading="lazy"></div>'
               f'<div style="padding-top: 26px;">{kicker("QUEM CONDUZ")}'
               f'<h2 class="h" style="font-size: 30px; margin-top: 26px;">Ol&aacute;! Eu sou a Silvana.</h2>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0; max-width: 520px;">Trabalho para que a tua comunica&ccedil;&atilde;o seja leve, coerente e sustent&aacute;vel, sem f&oacute;rmulas prontas e sem perder a tua ess&ecirc;ncia.</p>'
               f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 16px 0 0; max-width: 520px;">O Acompanhamento em Comunica&ccedil;&atilde;o Consciente nasceu para quem j&aacute; entendeu a import&acirc;ncia da comunica&ccedil;&atilde;o, mas ainda n&atilde;o conseguiu colocar em pr&aacute;tica o que sabe.</p>'
               f'</div></div></div>')
    quem_itens = ["J&aacute; tem bagagem, curso e teoria, mas trava na hora de agir.",
                  "Busca uma comunica&ccedil;&atilde;o que apresente os teus servi&ccedil;os com clareza e represente quem tu &eacute; de verdade.",
                  "Precisa de dire&ccedil;&atilde;o e companhia para organizar as ideias e construir uma comunica&ccedil;&atilde;o viva e consistente.",
                  "Deseja autonomia, n&atilde;o depend&ecirc;ncia: quer aprender a caminhar com os pr&oacute;prios p&eacute;s."]
    quem = (f'<div class="sec"><div class="rv">{kicker("PRA QUEM &Eacute;")}</div>'
            '<div class="g2 rv" style="margin-top: 40px;">'
            + "".join(f'<div><div class="rule rulex" style="height: 1px; background: rgba(38,34,32,0.35);"></div>'
                      f'<p class="t5" style="font-size: 16px; margin: 16px 0 0; line-height: 1.5;">{i}</p></div>' for i in quem_itens)
            + '</div></div>')
    como = (f'<div class="sec"><div class="rv">{kicker("COMO FUNCIONA")}'
            f'<h2 class="h" style="font-size: 28px; margin-top: 26px;">Tr&ecirc;s meses, seis encontros quinzenais de 1h30, e suporte leve pelo WhatsApp entre eles.</h2></div>'
            + steps_grid([
                ("Clareza e dire&ccedil;&atilde;o", "Entender o teu momento, a tua hist&oacute;ria e o que tu realmente quer comunicar: o qu&ecirc;, pra quem e por qu&ecirc;."),
                ("Organiza&ccedil;&atilde;o e conte&uacute;do", "Definir o assunto foco de cada m&ecirc;s, abrir o guarda-chuva de temas e montar o esqueleto da tua comunica&ccedil;&atilde;o."),
                ("Posicionamento e presen&ccedil;a", "Definir o teu tom de voz e a tua forma de aparecer, com coer&ecirc;ncia e bastidores nos stories."),
                ("Cria&ccedil;&atilde;o e estrutura", "Transformar ideias em falas, roteiros, legendas e conte&uacute;dos aplic&aacute;veis, com um banco criativo para agilizar o trabalho."),
                ("Pr&aacute;tica e grava&ccedil;&atilde;o", "Luz, enquadramento, cen&aacute;rio e presen&ccedil;a em v&iacute;deo com o Samuel, para gravar bem com o que tu tem em casa."),
                ("Revis&atilde;o e autonomia", "Revisar o caminho, ajustar o calend&aacute;rio e criar a tua rotina sustent&aacute;vel."),
            ], grid="g3") + '</div>')
    video = (f'<div class="sec"><div class="rv" style="max-width: 720px;">{kicker("A PARTE DE V&Iacute;DEO")}'
             f'<h2 class="h" style="font-size: 30px; margin-top: 26px;">Gravar bem com o que tu tem em casa.</h2>'
             f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 22px 0 0;">Um encontro pr&aacute;tico com o Samuel, com as dicas de luz, enquadramento e cen&aacute;rio pensadas para o que tu j&aacute; tem em casa, mais presen&ccedil;a em v&iacute;deo, teleprompter na pr&aacute;tica, gravar por blocos e o que fazer quando trava.</p>'
             f'<p class="t" style="font-size: 17px; line-height: 1.65; margin: 16px 0 0;">Tu recebe retorno direto sobre um v&iacute;deo que gravou, sai com o plano de grava&ccedil;&atilde;o do primeiro lote e segue com suporte pelo WhatsApp.</p></div></div>')
    return hero + silvana + quem + como + video + faq(FAQ_MENT)

def page_sites():
    hero = hero_page("CRIA&Ccedil;&Atilde;O DE SITES", "Um site sob medida, do texto ao c&oacute;digo.",
                     "Leve, r&aacute;pido e escrito por quem conhece a sua hist&oacute;ria: um site que carrega em segundos, aparece na busca e fala do jeito que voc&ecirc; fala.", ver_trabalhos=False)
    dif = (f'<div class="sec"><div class="rv">{kicker("O QUE FAZ A DIFEREN&Ccedil;A")}</div>'
           + steps_grid([
               ("Texto artesanal", "O texto nasce de conversa, n&atilde;o de modelo pronto. Quem l&ecirc; sente que &eacute; voc&ecirc; falando."),
               ("Leve e r&aacute;pido", "P&aacute;ginas enxutas, sem plataforma pesada, que abrem em qualquer celular e qualquer sinal."),
               ("Pronto para a busca", "Estrutura pensada para o Google entender quem voc&ecirc; &eacute;, o que faz e onde atende."),
           ], grid="g3", numbered=False) + '</div>')
    como = (f'<div class="sec"><div class="rv">{kicker("COMO FUNCIONA")}</div>'
            + steps_grid([
                ("Conhecer", "A gente conversa e levanta a sua hist&oacute;ria, os servi&ccedil;os e o que os seus clientes precisam encontrar."),
                ("Escrever e desenhar", "O texto vem primeiro e o desenho vem junto: cada p&aacute;gina nasce sob medida, com a sua identidade."),
                ("Publicar", "Site no ar, no seu dom&iacute;nio, com tudo conferido: velocidade, celular e busca."),
            ], grid="g3") + '</div>')
    sites_data = [("site-catarata-center.jpg", "Site &middot; Catarata Center",
                   "https://cataratacenter.com.br/"),
                  ("site-prisma-especialidades.jpg", "Site &middot; Prisma Especialidades",
                   "https://prismaespecialidades.com.br/"),
                  ("site-fyber-show.jpg", "Site &middot; Fyber Show Piscinas",
                   "https://fybershow.com.br/")]
    cards = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" style="display: block; color: #262220;">'
        f'<div style="aspect-ratio: 16 / 10; overflow: hidden; border: 1px solid rgba(38,34,32,0.15);">'
        f'<img src="/img/{f}" alt="{l}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; object-position: top; display: block;"></div>'
        f'<div class="t5" style="font-size: 14px; margin-top: 12px;">{l}</div></a>'
        for f, l, u in sites_data)
    ex = (f'<div class="sec"><div class="rv">{kicker("SITES NO AR")}</div>'
          f'<div class="g3 rv" style="margin-top: 44px;">{cards}</div></div>')
    return hero + dif + como + ex + REGIAO + faq(FAQ_SITES)

def page_encomenda():
    hero = hero_page("SOB ENCOMENDA", "Um filme com come&ccedil;o, meio e fim.",
                     "Produ&ccedil;&atilde;o de v&iacute;deo profissional, sem compromisso de recorr&ecirc;ncia: voc&ecirc; encomenda, a gente grava, edita e devolve pronto para usar. A Forster nasceu produtora de v&iacute;deo, e isso segue sendo o nosso forte.")
    tipos = (f'<div class="sec"><div class="rv">{kicker("TIPOS DE ENCOMENDA")}</div>'
             + steps_grid([
                 ("V&iacute;deo institucional", "A sua empresa apresentada com verdade: quem &eacute;, o que faz e por que faz. Para o site, para vender, para apresentar."),
                 ("V&iacute;deo de produto", "O seu produto em cena, bem iluminado e bem contado, pronto para campanha, loja e redes."),
                 ("V&iacute;deo publicit&aacute;rio", "Um filme de campanha, com ideia, roteiro e dire&ccedil;&atilde;o: para lan&ccedil;ar, para datas especiais e para a sua marca ser lembrada."),
             ], grid="g3") + '</div>')
    como = (f'<div class="sec"><div class="rv">{kicker("COMO FUNCIONA")}'
            f'<h2 class="h" style="font-size: 28px; margin-top: 26px;">Primeiro a gente entende. Depois a gente grava.</h2></div>'
            + steps_grid([
                ("Briefing", "Antes de qualquer coisa, a gente conversa: os temas, o tom e o que cada v&iacute;deo precisa comunicar. &Eacute; o que garante que o dia de grava&ccedil;&atilde;o renda ao m&aacute;ximo."),
                ("Roteiro", "O roteiro chega antes da sess&atilde;o, para voc&ecirc; aprovar ou ajustar. No dia, teleprompter: nada de decorar."),
                ("Sess&atilde;o de grava&ccedil;&atilde;o", "A gente vai at&eacute; voc&ecirc; com toda a estrutura: c&acirc;mera, ilumina&ccedil;&atilde;o profissional, microfone e teleprompter, e drone quando a hist&oacute;ria pede."),
                ("Edi&ccedil;&atilde;o e entrega", "Cortes limpos, identidade visual e o seu tom de voz. Pronto, voc&ecirc; recebe um link para ver, aprovar e baixar. Simples assim."),
            ]) + '</div>')
    trab = (f'<div class="sec"><div class="rv">{kicker("TRABALHOS SOB ENCOMENDA")}</div>'
            f'<div class="mosaic rv" style="margin-top: 44px;">'
            + tile("thalf", "#3A4638", "Institucional &middot; Pelizzer Im&oacute;veis", video=f"{MEDIA}/institucional-pelizzer-imoveis.mp4", img="thumb-institucional-pelizzer-imoveis.jpg", alt="V&iacute;deo institucional dos 30 anos da Pelizzer Im&oacute;veis")
            + tile("thalf", "#2B2724", "Institucional &middot; Col&eacute;gio Luterano Redentor", video=f"{MEDIA}/institucional-colegio-redentor.mp4", img="thumb-institucional-colegio-redentor.jpg", alt="V&iacute;deo institucional do Col&eacute;gio Luterano Redentor")
            + '</div></div>')
    return hero + tipos + como + trab + REGIAO + faq(FAQ_ENC)

def page_trabalhos():
    hero = hero_page("TRABALHOS", "O que sai do ateli&ecirc;.",
                     "Uma sele&ccedil;&atilde;o dos trabalhos, por tipo de encomenda. Toque num cart&atilde;o para assistir aqui mesmo.",
                     ver_trabalhos=False)
    inst = (f'<div class="sec"><div class="rv">{kicker("INSTITUCIONAIS")}</div>'
            f'<div class="mosaic rv" style="margin-top: 44px;">'
            + tile("thalf", "#3A4638", "Institucional &middot; Pelizzer Im&oacute;veis", video=f"{MEDIA}/institucional-pelizzer-imoveis.mp4", img="thumb-institucional-pelizzer-imoveis.jpg", alt="V&iacute;deo institucional dos 30 anos da Pelizzer Im&oacute;veis")
            + tile("thalf", "#2B2724", "Institucional &middot; Col&eacute;gio Luterano Redentor", video=f"{MEDIA}/institucional-colegio-redentor.mp4", img="thumb-institucional-colegio-redentor.jpg", alt="V&iacute;deo institucional do Col&eacute;gio Luterano Redentor")
            + tile("thalf", "#D9C29A", "Institucional &middot; Funda&ccedil;&atilde;o Ulysses Guimar&atilde;es", video=f"{MEDIA}/institucional-fundacao-ulysses-guimaraes.mp4", img="thumb-institucional-fundacao-ulysses-guimaraes.jpg", alt="V&iacute;deo Escola do Futuro, da Funda&ccedil;&atilde;o Ulysses Guimar&atilde;es")
            + '</div></div>')
    prod = (f'<div class="sec"><div class="rv">{kicker("PUBLICIT&Aacute;RIOS")}</div>'
            f'<div class="mosaic rv" style="margin-top: 44px;">'
            + tile("thalf", "#2B2724", "Publicit&aacute;rio &middot; Oli Im&oacute;veis &middot; Webs&eacute;rie Tra&ccedil;os, com Em&iacute;lio Finger", video=f"{MEDIA}/publicitario-oli-imoveis-webserie-tracos.mp4", img="thumb-publicitario-oli-imoveis-webserie-tracos.jpg", alt="Webs&eacute;rie Tra&ccedil;os, epis&oacute;dio com Em&iacute;lio Finger, da Oli Im&oacute;veis")
            + tile("thalf", "#3A4638", "Publicit&aacute;rio &middot; SAIF &middot; O Jeito de Come&ccedil;ar o Dia", video=f"{MEDIA}/publicitario-saif-jeito-de-comecar-o-dia.mp4", img="thumb-publicitario-saif-jeito-de-comecar-o-dia.jpg", alt="Campanha publicit&aacute;ria SAIF, filme O Jeito SAIF de Come&ccedil;ar o Dia")
            + tile("thalf", "#D9C29A", "Publicit&aacute;rio &middot; Emp&oacute;rio Essenza &middot; Hist&oacute;ria de Natal", video=f"{MEDIA}/publicitario-emporio-essenza-natal.mp4", img="thumb-publicitario-emporio-essenza-natal.jpg", alt="Filme de Natal do Emp&oacute;rio Essenza")
            + '</div></div>')
    outras = (f'<div class="sec"><div class="rv">{kicker("OUTRAS ENCOMENDAS")}</div>'
              f'<div class="mosaic rv" style="margin-top: 44px;">'
              + tile("thalf", "#3A4638", "Curso &middot; Dra Karol Hoppen &middot; Fada do Dente", video=f"{MEDIA}/curso-fada-do-dente.mp4", img="thumb-curso-fada-do-dente.jpg", alt="V&iacute;deo aula Fada do Dente, da Dra Karol Hoppen")
              + tile("thalf", "#2B2724", "Clipe musical &middot; Fam&iacute;lia Rolim &middot; Casa de Pedra", video=f"{MEDIA}/clipe-casa-de-pedra.mp4", img="thumb-clipe-casa-de-pedra.jpg", alt="Clipe musical Casa de Pedra, da Fam&iacute;lia Rolim")
              + tile("thalf", "#D9C29A", "Filme &middot; Kety e Serena &middot; Uma hist&oacute;ria de amor", video=f"{MEDIA}/filme-kety-e-serena.mp4", img="thumb-filme-kety-e-serena.jpg", alt="Kety e Serena, uma hist&oacute;ria de amor: filme sobre uma menina e a &eacute;gua que ela ama")
              + '</div></div>')
    mensal = (f'<div class="sec"><div class="rv">{kicker("CONTE&Uacute;DO MENSAL")}</div>'
              f'<div class="mosaic rv" style="margin-top: 44px;">'
              + tile("t916", "#3A4638", "Conte&uacute;do mensal &middot; Fyber Show Piscinas", video="/video/reel-fyber-show.mp4", img="capa-reel-fyber-show.jpg", alt="Reel Quem &eacute; a Fyber Show")
              + tile("t916", "#2B2724", "Conte&uacute;do mensal &middot; &Oacute;ticas Casa Marco", video="/video/reel-oticas-casa-marco.mp4", img="capa-reel-oticas-casa-marco.jpg", alt="Reel de produto Arma&ccedil;&otilde;es Femininas, das &Oacute;ticas Casa Marco")
              + tile("t916", "#2B2724", "Conte&uacute;do mensal &middot; Catarata Center", video="/video/reel-catarata-center.mp4", img="capa-reel-catarata-center.jpg", alt="Reel 3 Perguntas sobre Cirurgia de Catarata, do Catarata Center")
              + tile("t916", "#3A4638", "Conte&uacute;do mensal &middot; Prisma Especialidades", video="/video/reel-prisma-especialidades.mp4", img="capa-reel-prisma-especialidades.jpg", alt="Reel Ansiedade Infantil, da Prisma Especialidades")
              + '</div></div>')
    return hero + inst + prod + outras + mensal

def page_404():
    hero = hero_page("ERRO 404",
                     "Essa p&aacute;gina n&atilde;o existe.",
                     "Pode ser um endere&ccedil;o digitado errado, ou uma p&aacute;gina que mudou de lugar. "
                     "O que voc&ecirc; procura provavelmente est&aacute; em um dos caminhos abaixo.")
    portas = (f'<div class="sec"><div class="rv" style="margin-bottom: 44px;">{kicker("O QUE A GENTE FAZ")}</div>'
              f'<div class="g4 rv">'
              + door("01", "Acompanhamento mensal",
                     "A gente estuda o seu perfil, o seu mercado e os seus concorrentes e, a partir disso, cuida da sua comunica&ccedil;&atilde;o digital: roteiros, v&iacute;deos, postagens, site e perfil no Google. Voc&ecirc; grava, e o resto &eacute; com a gente.",
                     "/acompanhamento")
              + door("02", "Mentoria",
                     "Para quem quer aprender a comunicar, em encontros diretos com quem faz isso todos os dias.",
                     "/mentoria")
              + door("03", "Sites",
                     "Um site simples, r&aacute;pido e sob medida, que conta a sua hist&oacute;ria e aparece na busca.",
                     "/sites")
              + door("04", "Sob encomenda",
                     "Um v&iacute;deo com come&ccedil;o, meio e fim: institucional, v&iacute;deo de produto, a hist&oacute;ria da sua empresa bem contada.",
                     "/sob-encomenda")
              + '</div></div>')
    return hero + portas

# ---------------------------------------------------------------- SEO e montagem

AREA = ([{"@type": "City", "name": c} for c in
         ["Igrejinha", "Três Coroas", "Taquara", "Parobé", "Rolante", "Novo Hamburgo", "Gramado", "Canela"]]
        + [{"@type": "AdministrativeArea", "name": "Vale do Paranhana"},
           {"@type": "AdministrativeArea", "name": "Rio Grande do Sul"}])
ORG_ID = SITE + "/#org"
ORG = {
    "@type": "ProfessionalService",
    "@id": ORG_ID,
    "name": "FORSTER",
    "alternateName": "Forster Ateliê de Conteúdo",
    "slogan": "Conteúdo feito a quatro mãos.",
    "url": SITE + "/",
    "logo": SITE + "/img/forster-lockup.png",
    "image": SITE + "/img/og-forster.jpg",
    "telephone": "+55-51-98157-8225",
    "address": {"@type": "PostalAddress", "streetAddress": "Rua Dr. Edmundo Lauffer, 260, Bom Pastor",
                "addressLocality": "Igrejinha", "addressRegion": "RS",
                "postalCode": "95650-000", "addressCountry": "BR"},
    "areaServed": AREA,
    "sameAs": ["https://www.instagram.com/somosforster"],
    "founder": [{"@type": "Person", "name": "Samuel Forster"},
                {"@type": "Person", "name": "Silvana Forster"}],
}

def page_privacidade():
    botao = (f'<button class="optout" type="button" data-optout="{GA4_ID}">N&atilde;o contar minhas visitas</button>'
             f'<p class="t optout-st" id="optout-st"></p>') if GA4_ID else ''
    return (f'<header class="heroP">{kicker("PRIVACIDADE", " in")}'
            f'<h1 class="h h1p in in1" style="margin: 26px 0 0;">O que a gente mede neste site.</h1></header>'
            f'<div class="sec" style="padding-top: 0; border-top: 0;"><div class="prosa rv">'
            f'<p class="t" style="margin-top: 0;">Este site usa o Google Analytics para contar visitas: quantas pessoas entram, de onde v&ecirc;m, quais p&aacute;ginas abrem e se clicam no bot&atilde;o de conversar. &Eacute; o que a gente precisa para saber se o site est&aacute; cumprindo o papel dele.</p>'
            f'<p class="t">Os n&uacute;meros s&atilde;o agregados. A gente v&ecirc; que trinta pessoas vieram do Google esta semana, n&atilde;o quem s&atilde;o. Nenhum dado &eacute; usado para an&uacute;ncios, para montar perfil de quem visita ou cruzado com outras bases. O Google recebe esses dados como nosso fornecedor de medi&ccedil;&atilde;o e os guarda por 14 meses.</p>'
            f'<p class="t">Para reconhecer que duas visitas s&atilde;o da mesma pessoa, o Google Analytics grava um pequeno arquivo no seu navegador, o cookie. Ele n&atilde;o cont&eacute;m nome, e-mail nem telefone. Voc&ecirc; pode apag&aacute;-lo a qualquer momento nas configura&ccedil;&otilde;es do navegador.</p>'
            f'<p class="t">Se preferir n&atilde;o ser contado, &eacute; s&oacute; usar o bot&atilde;o abaixo. A escolha fica salva neste navegador e vale para todas as p&aacute;ginas do site.</p>'
            f'{botao}'
            f'<h2 class="h">Quando voc&ecirc; fala com a gente</h2>'
            f'<p class="t">Os bot&otilde;es de conversar abrem o WhatsApp. O que voc&ecirc; escrever ali fica entre voc&ecirc; e a FORSTER, e a gente usa s&oacute; para responder e, se virar trabalho, para fazer o trabalho. Nada vai para lista de e-mail nem para terceiros.</p>'
            f'<p class="t">Qualquer d&uacute;vida sobre os seus dados, &eacute; s&oacute; escrever para o Samuel pelo WhatsApp ou pelo Instagram. Respons&aacute;vel: FORSTER Ateli&ecirc; de Conte&uacute;do, Igrejinha, RS.</p>'
            f'</div></div>')

def service_ld(name, desc, path):
    return [{"@type": "Service", "name": name, "description": desc,
             "url": SITE + path, "provider": {"@id": ORG_ID}, "areaServed": AREA},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}]

PAGES = {
    "index.html": {
        "active": "", "fn": page_home, "convite": CONVITE_PADRAO, "path": "/",
        "title": "FORSTER · Ateliê de Conteúdo em Igrejinha, RS",
        "desc": "Vídeo, conteúdo para redes sociais, sites e mentoria de comunicação feitos a quatro mãos em Igrejinha, RS, para empresas do Vale do Paranhana e região.",
        "ld": [ORG],
    },
    "acompanhamento.html": {
        "active": "acompanhamento", "fn": page_acompanhamento, "convite": CONVITE_PADRAO, "path": "/acompanhamento",
        "title": "Gestão de redes sociais e conteúdo mensal em Igrejinha, RS | FORSTER",
        "desc": "Você grava uma vez por mês e a gente cuida do resto: roteiro, gravação, edição, publicação e relatório. Para empresas de Igrejinha e do Vale do Paranhana.",
        "ld": service_ld("Acompanhamento mensal de conteúdo", "A base da sua comunicação digital por conta da Forster: estudo do seu perfil, do seu mercado e dos seus concorrentes, diretrizes, roteiros, gravação, produção e publicação dos conteúdos, site, perfil no Google e relatório mensal.", "/acompanhamento") + [faq_ld(FAQ_ACOMP)],
    },
    "mentoria.html": {
        "active": "mentoria", "fn": page_mentoria, "convite": CONVITE_MENTORIA, "path": "/mentoria",
        "title": "Mentoria de comunicação individual | Comunicação Consciente | FORSTER",
        "desc": "Mentoria de comunicação individual com Silvana Forster: três meses para transformar o que tu já sabe em presença real, com a parte de vídeo com o Samuel.",
        "ld": service_ld("Acompanhamento em Comunicação Consciente", "Mentoria individual de comunicação: três meses, seis encontros quinzenais e suporte leve pelo WhatsApp.", "/mentoria") + [faq_ld(FAQ_MENT)],
    },
    "sites.html": {
        "active": "sites", "fn": page_sites, "convite": CONVITE_PADRAO, "path": "/sites",
        "title": "Criação de sites em Igrejinha e Vale do Paranhana | FORSTER",
        "desc": "Sites sob medida, do texto ao código: leves, rápidos e prontos para o Google. Feitos em Igrejinha para empresas do Vale do Paranhana e região.",
        "ld": service_ld("Criação de sites", "Sites institucionais leves e rápidos, do texto ao código, publicados no domínio do cliente.", "/sites") + [faq_ld(FAQ_SITES)],
    },
    "sob-encomenda.html": {
        "active": "encomenda", "fn": page_encomenda, "convite": CONVITE_PADRAO, "path": "/sob-encomenda",
        "title": "Produtora de vídeo institucional em Igrejinha, RS | FORSTER",
        "desc": "Vídeo institucional, de produto e publicitário, do roteiro à entrega, com luz profissional, teleprompter e drone. Produtora de vídeo em Igrejinha, RS.",
        "ld": service_ld("Produção de vídeo sob encomenda", "Vídeo institucional e vídeo de produto, do roteiro à entrega, sem compromisso de recorrência.", "/sob-encomenda") + [faq_ld(FAQ_ENC)],
    },
    "privacidade.html": {
        "active": "", "fn": page_privacidade, "convite": "", "path": "/privacidade",
        "title": "Privacidade | FORSTER",
        "desc": "O que o site da FORSTER mede, por quanto tempo, e como pedir para não ser contado.",
        "ld": [{"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Privacidade", "item": SITE + "/privacidade"}]}],
    },
    "trabalhos.html": {
        "active": "trabalhos", "fn": page_trabalhos, "convite": CONVITE_PADRAO, "path": "/trabalhos",
        "title": "Portfólio de vídeos e conteúdo | FORSTER",
        "desc": "Uma seleção do que sai do ateliê: vídeos institucionais, publicitários, curso, clipe e o conteúdo mensal que a Forster produz para os clientes.",
        "ld": service_ld("Trabalhos da Forster", "Seleção de vídeos institucionais, publicitários e de conteúdo mensal produzidos pela Forster.", "/trabalhos"),
    },
    # Servida pelo Cloudflare Pages em qualquer rota sem correspondencia.
    # noindex: fica fora do sitemap e sem canonical, porque nao tem URL propria.
    "404.html": {
        "active": "", "fn": page_404, "convite": CONVITE_PADRAO, "path": "/404", "noindex": True,
        "title": "Página não encontrada | FORSTER",
        "desc": "O endereço que você abriu não existe no site da FORSTER.",
        "ld": [],
    },
}

# ---------------------------------------------------------------- blog (desde 05/10/2026)
# Camada do repo, fora do Claude Design: artigos em _fontes/blog_artigos.py.
import sys as _sys
_sys.path.insert(0, str(BASE))
from blog_artigos import ARTIGOS

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]

def data_por_extenso(iso):
    ano, mes, dia = iso.split("-")
    return f"{int(dia)} de {MESES[int(mes) - 1]} de {ano}"

def page_artigo_fn(a):
    def fn():
        outros = [o for o in ARTIGOS if o["slug"] != a["slug"]][:3]
        servico, href = a["servico"]
        leia = "".join(f'<li><a href="/blog/{o["slug"]}">{o["titulo"]}</a></li>' for o in outros)
        return (f'<header class="heroP">{kicker("BLOG", " in")}'
                f'<h1 class="h h1p in in1" style="margin: 26px 0 0;">{a["titulo"]}</h1>'
                f'<p class="t note in in2" style="margin: 20px 0 0;">{data_por_extenso(a["data"])}</p></header>'
                f'<div class="sec" style="padding-top: 0; border-top: 0;"><article class="prosa rv">{a["corpo"]}'
                f'<p><a class="tb lka" href="{href}" style="font-size: 16px;">{servico} na FORSTER {ARROW}</a></p>'
                f'</article></div>'
                + faq(a["faq"])
                + (f'<div class="sec"><div class="prosa rv">{kicker("LEIA TAMBÉM")}<ul>{leia}</ul></div></div>' if leia else ''))
    return fn

def page_blog():
    itens = "".join(
        f'<div class="col"><div class="rule rulex"></div>'
        f'<div class="t note" style="margin-top: 22px;">{data_por_extenso(a["data"])}</div>'
        f'<h2 class="h" style="font-size: 24px; margin-top: 12px;"><a href="/blog/{a["slug"]}" style="color: #262220;">{a["titulo"]}</a></h2>'
        f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin: 14px 0 0;">{a["desc"]}</p>'
        f'<a class="tb lka" href="/blog/{a["slug"]}" style="font-size: 14px; margin-top: auto; padding-top: 18px;">Ler o artigo {ARROW}</a></div>'
        for a in ARTIGOS)
    return (f'<header class="heroP">{kicker("BLOG", " in")}'
            f'<h1 class="h h1p in in1" style="margin: 26px 0 0;">O que a gente aprende fazendo.</h1>'
            f'<p class="t sup in in2" style="margin: 24px 0 0;">Artigos sobre vídeo, redes sociais, sites e presença no Google, para empresas de Igrejinha e do Vale do Paranhana.</p></header>'
            f'<div class="sec"><div class="g2 rv">{itens}</div></div>')

def breadcrumb(*nivel):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": SITE + c} for i, (n, c) in enumerate(nivel, 1)]}

PAGES["blog/index.html"] = {
    "active": "", "fn": page_blog, "convite": CONVITE_PADRAO, "path": "/blog/",
    "title": "Blog | FORSTER, Ateliê de Conteúdo em Igrejinha, RS",
    "desc": "Artigos sobre vídeo, redes sociais, sites e presença no Google para empresas de Igrejinha e do Vale do Paranhana.",
    "ld": [breadcrumb(("Início", "/"), ("Blog", "/blog/"))],
}
for _a in ARTIGOS:
    _path = f"/blog/{_a['slug']}"
    PAGES[f"blog/{_a['slug']}.html"] = {
        "active": "", "fn": page_artigo_fn(_a), "convite": CONVITE_PADRAO, "path": _path,
        "title": f"{_a['titulo']} | FORSTER", "desc": _a["desc"],
        "ld": [{"@type": "BlogPosting", "headline": _a["titulo"], "description": _a["desc"],
                "datePublished": _a["data"], "dateModified": _a["data"], "inLanguage": "pt-BR",
                "mainEntityOfPage": SITE + _path, "image": SITE + "/img/og-forster.jpg",
                "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}},
               faq_ld(_a["faq"]),
               breadcrumb(("Início", "/"), ("Blog", "/blog/"), (_a["titulo"], _path))],
    }

def ga4():
    if not GA4_ID:
        return ""
    # Consent Mode: so analytics; nada de anuncios nem personalizacao.
    return f'''
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <script>try{{if(localStorage.getItem('sem-medicao')==='1')window['ga-disable-{GA4_ID}']=true;}}catch(e){{}}</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('consent', 'default', {{ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted'}});
    gtag('js', new Date());
    gtag('config', '{GA4_ID}');
  </script>'''

import hashlib
VER = hashlib.md5((CSS + JS).encode('utf-8')).hexdigest()[:8]

def head(p):
    ld = (f'\n  <script type="application/ld+json">'
          + json.dumps({"@context": "https://schema.org", "@graph": p["ld"]}, ensure_ascii=False)
          + "</script>") if p["ld"] else ""
    canonical = "" if p.get("noindex") else f'\n  <link rel="canonical" href="{SITE}{p["path"]}">'
    robots = "noindex, nofollow" if p.get("noindex") else "index, follow, max-image-preview:large"
    return f'''<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p["title"]}</title>
  <meta name="description" content="{p["desc"]}">{canonical}
  <meta name="robots" content="{robots}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="FORSTER · Ateliê de Conteúdo">
  <meta property="og:title" content="{p["title"]}">
  <meta property="og:description" content="{p["desc"]}">
  <meta property="og:url" content="{SITE}{p["path"]}">
  <meta property="og:image" content="{SITE}/img/og-forster.jpg">
  <meta property="og:locale" content="pt_BR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap">
  <link rel="stylesheet" href="/style.css?v={VER}">{ld}{ga4()}'''

def page_html(p):
    body = f'<div class="page">{nav(p["active"])}{p["fn"]()}{p["convite"]}</div>{FOOTER}'
    return (f'<!doctype html>\n<html lang="pt-BR">\n<head>\n  {head(p)}\n</head>\n<body>\n'
            f'{body}\n<script src="/site.js?v={VER}" defer></script>\n</body>\n</html>\n')

PUB.mkdir(exist_ok=True)
for fname, p in PAGES.items():
    (PUB / fname).parent.mkdir(parents=True, exist_ok=True)
    (PUB / fname).write_text(page_html(p), encoding="utf-8")
    print("ok", fname)

(PUB / "style.css").write_text(CSS, encoding="utf-8")
(PUB / "site.js").write_text(JS, encoding="utf-8")

# ATENCAO: este arquivo nao chega ao ar. A zona somosforster.com.br tem o robots.txt
# gerenciado da Cloudflare ligado (AI Crawl Control), e ele sobrescreve o do Pages.
# Para mudar o robots.txt de verdade, e no painel da Cloudflare, nao aqui.
(PUB / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")

def data_da_pagina(fname):
    """Data da última mudança real da página, para o <lastmod> do sitemap. Antes era uma data
    fixa (03/09/2026) e o Google não tinha sinal de que as páginas mudaram (05/10/2026).
    Página com mudança ainda não gravada no git: hoje. Sem mudança: data do último commit dela."""
    import datetime, subprocess
    arquivo = PUB / fname
    raiz = PUB.parent
    mudou = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", str(arquivo)], cwd=raiz).returncode != 0
    if not mudou:
        data = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(arquivo)], cwd=raiz,
                              capture_output=True, text=True).stdout.strip()
        if data:
            return data
    return datetime.date.today().isoformat()

urls = "".join(f"  <url><loc>{SITE}{p['path']}</loc><lastmod>{data_da_pagina(f)}</lastmod></url>\n"
               for f, p in PAGES.items() if not p.get("noindex"))
(PUB / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n', encoding="utf-8")

(PUB / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  X-Frame-Options: SAMEORIGIN
/img/*
  Cache-Control: public, max-age=31536000, immutable
/video/*
  Cache-Control: public, max-age=31536000, immutable
""", encoding="utf-8")

print("ok style.css site.js robots sitemap _headers")
