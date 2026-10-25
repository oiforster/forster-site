#!/usr/bin/env python3
# Gerador do site da FORSTER (somosforster.com.br).
# Fontes visuais: revisao 25/10/2026 do projeto "Forster site implementation" no Claude Design.
# Este script emite o site institucional, o blog e as paginas de entrada em ../public
# + robots/sitemap/_headers + redirect da raiz (forsterfilmes.com via GitHub Pages).
import json, pathlib
from urllib.parse import quote

BASE = pathlib.Path(__file__).parent
PUB = BASE.parent / "public"
SITE = "https://somosforster.com.br"

WA_SAMUEL = "https://wa.me/5551981578225"
WA_SILVANA = "https://wa.me/5551980603512"
# Google Analytics 4: ID da propriedade (formato G-XXXXXXXXXX). Vazio = nenhuma medicao no site.
# Criar em analytics.google.com > Administrador > Criar propriedade > fluxo de dados Web.
GA4_ID = "G-0PH3FJRH7W"

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
.note { font-size: 13px; font-style: italic; color: #61594F; }
.conf { display: flex; flex-wrap: wrap; gap: 18px 40px; font-size: 17px; }
@media (min-width: 1200px) {
  .conf { flex-wrap: wrap; justify-content: flex-start; gap: 16px; font-size: 15px; }
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
.optout-st { font-size: 14px; color: #61594F; margin-top: 12px; }
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

CSS += """
.skip-link { position: absolute; left: 16px; top: -80px; z-index: 100; background: #262220; color: #F7F3EC; padding: 12px 18px; }
.skip-link:focus { top: 12px; }
a:focus-visible, button:focus-visible { outline: 3px solid #B0553B; outline-offset: 5px; }
.foot a:focus-visible { outline-color: #F7F3EC; }
@media (max-width: 1100px) {
  .menu-btn { display: flex; }
  .navlinks { display: none; position: absolute; top: 100%; left: 0; right: 0; z-index: 20; flex-direction: column; align-items: stretch; gap: 0; background: #F7F3EC; border-bottom: 1px solid rgba(38,34,32,0.12); padding: 6px clamp(20px, 8.3vw, 120px) 14px; }
  .navlinks.open { display: flex; }
  .navlink { padding: 13px 0; }
}
.contact-mobile { display: none; }
@media(max-width:600px) { .contact-desktop { display:none; } .contact-mobile { display:inline; } }
"""

JS = (BASE / 'site.js').read_text(encoding='utf-8')
JS = (BASE / 'site.js').read_text(encoding='utf-8')

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


NAV_ITEMS = [("inicio", "In&iacute;cio", "/"),
             ("trabalhos", "Trabalhos", "/trabalhos"),
             ("acompanhamento", "Acompanhamento", "/acompanhamento"),
             ("mentoria", "Mentoria", "/mentoria"),
             ("sites", "Sites", "/sites"),
             ("encomenda", "V&iacute;deos sob encomenda", "/sob-encomenda")]

def nav(active=""):
    links = "".join(
        f'<a class="navlink t5{" nav-on" if key == active else ""}"'
        + (' aria-current="page"' if key == active else '')
        + f' href="{href}">{label}</a>'
        for key, label, href in NAV_ITEMS)
    burger = ('<button class="menu-btn" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu">'
              '<svg width="22" height="16" viewBox="0 0 22 16" fill="none" aria-hidden="true">'
              '<path d="M1 1.5h20M1 8h20M1 14.5h20" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path></svg></button>')
    pessoa = WA_SILVANA if active == "mentoria" else WA_SAMUEL
    mensagens = {"mentoria": "Olá, Silvana! Queria conversar sobre a Comunicação Consciente.",
                 "sites": "Olá! Queria conversar sobre um site para a minha empresa.",
                 "encomenda": "Olá! Queria conversar sobre um vídeo para a minha empresa.",
                 "acompanhamento": "Olá! Queria conhecer o acompanhamento mensal da Forster."}
    destino = pessoa + ("?text=" + quote(mensagens[active]) if active in mensagens else "")
    rotulo = ('<span class="contact-desktop">Falar com a Silvana</span><span class="contact-mobile">Silvana</span>'
              if active == "mentoria" else 'Conversar')
    return (f'<nav class="topbar" aria-label="Principal"><a href="/" style="color: #262220;" aria-label="FORSTER, p&aacute;gina inicial">{lockup("20px", "currentColor")}</a>'
            f'<div class="navwrap">{burger}<div class="navlinks" id="menu">{links}</div>'
            f'<a class="tb btn btn-sm" href="{destino}" target="_blank" rel="noopener">{rotulo}</a></div></nav>')

def kicker(text, extra_cls="", heading=False):
    tag = "h2" if heading else "p"
    return f'<div class="krow{extra_cls}"><div class="kbar" aria-hidden="true"></div><{tag} class="kick">{text}</{tag}></div>'


def hero_page(kick, h1, sup, cta_label="Conversar no WhatsApp", cta_href=WA_SAMUEL, ver_trabalhos=True):
    ver = (f'<a class="tb lka" href="/trabalhos" style="font-size: 16px; color: #262220; border-bottom: 1px solid rgba(38,34,32,0.4); padding-bottom: 2px;">Ver trabalhos {ARROW}</a>'
           if ver_trabalhos else '')
    return (f'<header class="heroP">{kicker(kick, " in")}'
            f'<h1 class="h h1p in in1" style="margin: 26px 0 0;">{h1}</h1>'
            f'<p class="t sup in in2" style="margin: 24px 0 0;">{sup}</p>'
            f'<div class="in in3" style="display: flex; align-items: center; gap: 28px; margin-top: 36px; flex-wrap: wrap;">'
            f'<a class="tb btn btn-lg" href="{cta_href}" target="_blank" rel="noopener">{cta_label}</a>{ver}</div></header>')


def convite(heading, text, cta_label, cta_href):
    return (f'<div class="sec"><div class="rv">'
            f'<h2 class="h" style="font-size: clamp(32px, 4vw, 44px);">{heading}</h2>'
            f'<p class="t" style="font-size: 18px; line-height: 1.6; margin: 18px 0 0; max-width: 520px;">{text}</p>'
            f'<a class="tb btn btn-lg" href="{cta_href}" target="_blank" rel="noopener" style="margin-top: 28px;">{cta_label}</a>'
            f'</div></div>')

CONVITE_PADRAO = convite("Vamos conversar?",
                         "Conte para a gente o que voc&ecirc; precisa. Quem l&ecirc; e responde &eacute; o Samuel ou a Silvana.",
                         "Conversar no WhatsApp", WA_SAMUEL)
CONVITE_SITES = convite("Vamos conversar sobre o seu site?",
                         "Conte quais serviços sua empresa oferece e o que precisa apresentar no site. Quem lê e responde é o Samuel ou a Silvana.",
                         "Conversar no WhatsApp", WA_SAMUEL)
CONVITE_ENCOMENDA = convite("Vamos conversar sobre o seu vídeo?",
                             "Conte o que você precisa comunicar e onde pretende usar o vídeo. Quem lê e responde é o Samuel ou a Silvana.",
                             "Conversar no WhatsApp", WA_SAMUEL)
CONVITE_MENTORIA = convite("Se esse &eacute; o teu momento",
                           "Manda uma mensagem e vamos conversar para entender o que faz sentido pra ti.",
                           "Falar com a Silvana pelo WhatsApp", WA_SILVANA)


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
     "Na maior parte dos casos, sim, e é isso que faz a diferença: quem confia em você quer ver você. A gente prepara o roteiro e orienta a sua fala durante a sessão, enquanto cuida da câmera, da luz e do som. Quando faz sentido, o conteúdo também mostra a equipe, o produto ou o lugar."),
    ("Quanto conteúdo sai por mês?",
     "A quantidade e o tipo de conteúdo são definidos na proposta. O acompanhamento pode incluir só vídeos, só conteúdo ou um conjunto mais completo de serviços, conforme o que você precisa."),
    ("Vocês também publicam?",
     "Sim. A publicação dos vídeos, posts e legendas pode fazer parte do acompanhamento. O que fica com a gente é combinado na proposta."),
    ("Como começa?",
     "Com um mês de diagnóstico. Antes de gravar qualquer coisa, a gente estuda tudo o que você já publicou, o seu mercado e os seus concorrentes, e monta o documento com as diretrizes do trabalho. Só depois o ciclo mensal começa."),
]
FAQ_MENT = [
    ("Quanto tempo dura?",
     "Três meses, com cinco encontros ao vivo, quinzenais, de uma hora e meia cada, e uma aula gravada. Entre os encontros, tu conta com suporte por WhatsApp."),
    ("Preciso já publicar conteúdo?",
     "Não. O acompanhamento começa pelo teu momento e pela tua história. Se tu já publica, a gente organiza o que existe. Se ainda não, a gente constrói do zero, com um calendário que cabe na tua rotina."),
    ("Como funciona a parte de vídeo?",
     "É a aula gravada “Como me gravar sozinha”, com Silvana e Samuel. Em 28 minutos e oito capítulos, ela mostra como preparar o cenário, a luz, a posição do celular e o som para se gravar em casa ou no escritório. As dúvidas da aula são conversadas no último encontro."),
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
     "Sim. A gente conversa, escreve o roteiro e manda para você aprovar antes da sessão. Na gravação, você pode acompanhar o texto no teleprompter, sem precisar decorar. A gente orienta a fala durante a sessão."),
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
            f'<div class="t5" style="font-size: 13px; color: #61594F; margin-top: 22px;">{num}</div>'
            f'<h3 class="h" style="font-size: 26px; margin-top: 12px; min-height: 64px;">{titulo}</h3>'
            f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin: 14px 0 0;">{desc}</p>'
            f'<a class="tb lka" href="{href}" style="font-size: 14px; margin-top: auto; padding-top: 18px;">Como funciona {ARROW}</a></div>')








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
                     "Um site sob medida que apresenta seus servi&ccedil;os, facilita o contato e vem preparado para o Google entender o seu neg&oacute;cio.",
                     "/sites")
              + door("04", "Sob encomenda",
                     "V&iacute;deos institucionais, de produto e de campanha para apresentar sua empresa e o que ela oferece.",
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

# ---------------------------------------------------------------- links da Silvana (desde 25/10/2026)
# Pagina do link da bio do @silvanaforster. Camada do repo, fora do Claude Design, como o blog.
# Sem menu nem rodape do site: e uma pagina so, aberta pelo celular a partir do Instagram.
PROPOSTA_SILVANA = "https://propostas.somosforster.com.br/acompanhamento-comunicacao-consciente-363656cb/"
TELEGRAM_SILVANA = "https://t.me/+8itHEv_NC6kwOTRh"

CSS_LINKS = """.lk { background: #F7F3EC; min-height: 100vh; display: flex; flex-direction: column; }
.lk-top { position: relative; overflow: hidden; background: #3A4638; color: #F7F3EC; padding: 44px 24px 40px; text-align: center; }
.lk-top .lk-s { position: absolute; right: -70px; top: -30px; width: 300px; opacity: .22; }
.lk-top .lk-s svg { width: 100%; height: auto; overflow: visible; }
.lk-foto { position: relative; width: 116px; height: 116px; margin: 0 auto; border-radius: 50%; overflow: hidden; border: 3px solid #F7F3EC; }
.lk-foto img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 22%; display: block; }
.lk-nome { position: relative; font-size: 32px; margin-top: 20px; }
.lk-desc { position: relative; font-size: 11px; color: #D9C29A; margin-top: 12px; }
.lk-bio { position: relative; font-size: 16px; line-height: 1.55; color: rgba(247,243,236,0.88); max-width: 380px; margin: 18px auto 0; }
.lk-lista { width: 100%; max-width: 520px; box-sizing: border-box; margin: 0 auto; padding: 32px 20px 44px; flex: 1 0 auto; }
.lk-dest { display: block; color: #262220; border: 2px solid #262220; border-radius: 10px; padding: 24px 22px 22px; background: #FBF8F3; transition: transform .2s cubic-bezier(.22,1,.36,1); }
.lk-dest:hover { color: #262220; }
.lk-dest .btn { margin-top: 20px; }
.lk-item { display: flex; align-items: center; gap: 16px; color: #262220; padding: 20px 4px; border-bottom: 1px solid rgba(38,34,32,0.16); }
.lk-item:hover { color: #262220; }
.lk-item:hover h2 { color: #B0553B; }
.lk-item svg { color: #B0553B; transition: transform .25s cubic-bezier(.22,1,.36,1); }
.lk-item h2 { font-size: 20px; transition: color .2s ease; }
.lk-item p { font-size: 14px; line-height: 1.5; color: rgba(38,34,32,0.72); margin-top: 6px; }
.lk-apres { margin-top: 44px; }
.lk-apres p { font-size: 16px; line-height: 1.65; color: rgba(38,34,32,0.85); margin-top: 14px; }
.lk-pe { background: #3A4638; color: #F7F3EC; padding: 28px 24px 32px; display: flex; flex-direction: column; align-items: center; gap: 10px; }
.lk-pe a { color: #F7F3EC; }
@media (hover: hover) and (pointer: fine) {
  .lk-dest:hover { transform: translateY(-3px); }
  .lk-item:hover svg { transform: translateX(4px); }
}"""

def link_item(titulo, desc, href):
    return (f'<a class="lk-item rv" href="{href}" target="_blank" rel="noopener">'
            f'<div style="flex: 1 1 auto;"><h2 class="h">{titulo}</h2><p class="t">{desc}</p></div>'
            f'{ARROW}</a>')

def page_silvana():
    topo = (f'<header class="lk-top"><div class="lk-s sdraw">{s_svg("#D9C29A", sw="9", inline_size=False)}</div>'
            f'<div class="lk-foto in"><img src="/img/silvana-forster.jpg" alt="Silvana Forster"></div>'
            f'<h1 class="h lk-nome in in1">Silvana Forster</h1>'
            f'<div class="ds lk-desc in in1">COMUNICA&Ccedil;&Atilde;O CONSCIENTE</div>'
            f'<p class="t lk-bio in in2">Ajudo mulheres que s&atilde;o m&atilde;es e empreendem a organizar as ideias e comunicar o pr&oacute;prio trabalho. O Marketing Sist&ecirc;mico &eacute; a base desse acompanhamento.</p></header>')
    # Apresentacao revisada para esta pagina e aprovada pelo Samuel em 25/10/2026.
    apresentacao = (f'<section class="lk-apres rv">{kicker("QUEM SOU EU")}'
                    f'<h2 class="h" style="font-size: 24px; margin-top: 18px;">Ol&aacute;! Eu sou a Silvana.</h2>'
                    f'<p class="t">Sou publicit&aacute;ria e empreendedora e trabalho com comunica&ccedil;&atilde;o h&aacute; quase 20 anos. Hoje, eu e o Samuel, meu marido, temos a FORSTER, nosso ateli&ecirc; de conte&uacute;do. &Eacute; l&aacute; que planejo e escrevo os conte&uacute;dos dos nossos clientes.</p>'
                    f'<p class="t">Eu tamb&eacute;m j&aacute; tive dificuldade para apresentar minhas ideias e os projetos que queria realizar. Sei como &eacute; ter muito a dizer e travar na hora de comunicar o pr&oacute;prio trabalho.</p>'
                    f'<p class="t">Foi dessa experi&ecirc;ncia que nasceu o Acompanhamento em Comunica&ccedil;&atilde;o Consciente. Nele, eu te acompanho para organizar as tuas ideias, escrever os teus conte&uacute;dos e criar uma rotina para apresentar os teus servi&ccedil;os com as tuas palavras.</p></section>')
    destaque = (f'<a class="lk-dest in in3" href="{PROPOSTA_SILVANA}" target="_blank" rel="noopener">'
                f'{kicker("MENTORIA INDIVIDUAL")}'
                f'<h2 class="h" style="font-size: 26px; margin-top: 18px;">Acompanhamento em Comunica&ccedil;&atilde;o Consciente</h2>'
                f'<p class="t" style="font-size: 15px; line-height: 1.6; color: rgba(38,34,32,0.78); margin-top: 12px;">S&atilde;o tr&ecirc;s meses de acompanhamento para te ajudar a organizar as ideias e comunicar o teu trabalho, com cinco encontros ao vivo e uma aula gravada. Na proposta, tu encontra os detalhes de cada encontro, o que est&aacute; inclu&iacute;do e os valores.</p>'
                f'<span class="tb btn btn-lg">Ver a proposta completa</span></a>')
    itens = (link_item("Conversar comigo no WhatsApp",
                       "Para tirar uma d&uacute;vida ou me contar como est&aacute; a comunica&ccedil;&atilde;o do teu neg&oacute;cio.",
                       WA_SILVANA + "?text=" + "Oi,%20Silvana!%20Vim%20pelo%20teu%20Instagram.")
             + link_item("Uma pergunta por semana, no Telegram",
                         "No meu canal gratuito, compartilho uma reflex&atilde;o e uma pergunta por semana para te ajudar a pensar em como tu comunica o teu neg&oacute;cio no dia a dia.",
                         TELEGRAM_SILVANA)
             + link_item("FORSTER, o nosso ateli&ecirc; de conte&uacute;do",
                         "O que eu e o Samuel fazemos para empresas: conte&uacute;do mensal, v&iacute;deos e sites.",
                         "/"))
    pe = (f'<footer class="lk-pe"><a href="/" aria-label="FORSTER, p&aacute;gina inicial">{lockup("17px", "currentColor")}</a>'
          f'<div class="t" style="font-size: 13px; color: rgba(247,243,236,0.75);">Conte&uacute;do feito a quatro m&atilde;os.</div></footer>')
    return (f'<style>{CSS_LINKS}</style><div class="lk">{topo}'
            f'<main class="lk-lista">{destaque}<div style="margin-top: 14px;">{itens}</div>{apresentacao}</main>{pe}</div>')

def page_instagram():
    # Exportação atual do Claude Design; preserva o desenho e os textos da página.
    source = (BASE / "entrada-instagram-design.html").read_text(encoding="utf-8")
    style = "<style>" + source.split("<style>", 1)[1].split("</style>", 1)[0] + "</style>"
    body = source.split("<body>", 1)[1].split("</body>", 1)[0]
    return style + body

def service_ld(name, desc, path):
    return [{"@type": "Service", "name": name, "description": desc,
             "url": SITE + path, "provider": {"@id": ORG_ID}, "areaServed": AREA},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}]

PAGES = {
    "index.html": {
        "active": "", "design": "Home-2026-10-25.html", "convite": "", "path": "/",
        "title": "FORSTER · Ateliê de Conteúdo em Igrejinha, RS",
        "desc": "Vídeo, conteúdo para redes sociais, sites e mentoria de comunicação feitos a quatro mãos em Igrejinha, RS, para empresas do Vale do Paranhana e região.",
        "ld": [ORG],
    },
    "acompanhamento.html": {
        "active": "acompanhamento", "design": "Acompanhamento-2026-10-25.html", "convite": CONVITE_PADRAO, "path": "/acompanhamento",
        "title": "Gestão de redes sociais e conteúdo mensal em Igrejinha, RS | FORSTER",
        "desc": "Planejamento, vídeos, textos e publicações conforme a proposta. Acompanhamento de comunicação para empresas de Igrejinha e do Vale do Paranhana.",
        "ld": service_ld("Acompanhamento mensal de conteúdo", "Acompanhamento mensal com serviços definidos na proposta: pode incluir estudo, diretrizes, roteiros, gravação, produção e publicação de conteúdo, site, Perfil da Empresa no Google e relatório.", "/acompanhamento") + [faq_ld(FAQ_ACOMP)],
    },
    "mentoria.html": {
        "active": "mentoria", "design": "Mentoria-2026-10-25.html", "convite": CONVITE_MENTORIA, "path": "/mentoria",
        "title": "Mentoria de comunicação individual | Comunicação Consciente | FORSTER",
        "desc": "Mentoria individual de comunicação com Silvana Forster: três meses, cinco encontros ao vivo e uma aula gravada sobre como se gravar com o celular.",
        "ld": service_ld("Acompanhamento em Comunicação Consciente", "Mentoria individual de comunicação: três meses, cinco encontros ao vivo, quinzenais, de 1h30 cada, uma aula gravada e suporte por WhatsApp.", "/mentoria") + [faq_ld(FAQ_MENT)],
    },
    "sites.html": {
        "active": "sites", "design": "Sites-2026-10-25.html", "convite": CONVITE_SITES, "path": "/sites",
        "title": "Criação de sites em Igrejinha e Vale do Paranhana | FORSTER",
        "desc": "Sites sob medida, do texto ao código: leves, rápidos e prontos para o Google. Feitos em Igrejinha para empresas do Vale do Paranhana e região.",
        "ld": service_ld("Criação de sites", "Sites institucionais leves e rápidos, do texto ao código, publicados no domínio do cliente.", "/sites") + [faq_ld(FAQ_SITES)],
    },
    "sob-encomenda.html": {
        "active": "encomenda", "design": "Videos-2026-10-25.html", "convite": CONVITE_ENCOMENDA, "path": "/sob-encomenda",
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
        "active": "trabalhos", "design": "Trabalhos-2026-10-25.html", "convite": CONVITE_PADRAO, "path": "/trabalhos",
        "title": "Portfólio de sites e vídeos | FORSTER",
        "desc": "Sites, vídeos institucionais, campanhas, cursos, clipes e conteúdo mensal produzidos pela Forster. Veja os trabalhos e conheça os serviços.",
        "ld": service_ld("Trabalhos da Forster", "Seleção de sites, vídeos institucionais, campanhas e conteúdo mensal produzidos pela Forster.", "/trabalhos"),
    },
    # Link da bio do Instagram da Silvana. noindex: pagina de passagem, sem conteudo proprio para o Google.
    "silvana.html": {
        "active": "", "fn": page_silvana, "convite": "", "path": "/silvana", "noindex": True, "solo": True,
        "og": "og-silvana-forster.jpg",
        "title": "Silvana Forster · Comunicação Consciente",
        "desc": "Os links da Silvana Forster: o Acompanhamento em Comunicação Consciente, o WhatsApp, o canal no Telegram e a FORSTER.",
        "ld": [],
    },
    # Entrada do perfil da Forster, com os serviços, exemplos e contatos.
    "instagram.html": {
        "active": "", "fn": page_instagram, "convite": "", "path": "/instagram", "noindex": True, "solo": True,
        "title": "Conheça o trabalho da Forster | FORSTER · Ateliê de Conteúdo",
        "desc": "Vídeos, conteúdos, sites e acompanhamento em comunicação com Samuel e Silvana, na FORSTER, ateliê de conteúdo em Igrejinha, RS.",
        "ld": [],
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
    stylesheet = (f'<style>{p["design_doc"]["css"]}</style>' if p.get("design_doc")
                  else f'<link rel="stylesheet" href="/style.css?v={VER}">')
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
  <meta property="og:image" content="{SITE}/img/{p.get("og", "og-forster.jpg")}">
  <meta property="og:locale" content="pt_BR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap">
  {stylesheet}{ld}{ga4()}'''

def page_html(p):
    if p.get("design_doc"):
        body = p["design_doc"]["body"]
        attrs = p["design_doc"]["body_attrs"] + ' data-design-revision="2026-10-25"'
    elif p.get("solo"):
        body, attrs = p["fn"](), ""
    else:
        body = (f'<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>'
                f'<div class="page">{nav(p["active"])}<main id="conteudo">{p["fn"]()}{p["convite"]}</main></div>{FOOTER}')
        attrs = ""
    return (f'<!doctype html>\n<html lang="pt-BR">\n<head>\n  {head(p)}\n</head>\n<body {attrs}>\n'
            f'{body}\n<script src="/site.js?v={VER}" defer></script>\n</body>\n</html>\n')

from design_pages import load_design
for p in PAGES.values():
    if p.get("design"):
        p["design_doc"] = load_design(BASE / "paginas" / p["design"])

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
