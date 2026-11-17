"""Catálogo público de produtos. As condições completas ficam nas páginas de venda."""
from html import escape

PRODUTOS = [
    {
        "id": "stories", "tipo": "Aula gravada com Silvana", "tema": "telha",
        "titulo": "O que postar nos stories",
        "texto": "Encontre assuntos nas experiências da sua rotina e aprenda a organizar essas ideias em uma história para quem acompanha seu perfil.",
        "detalhe": "Aproximadamente 1h40 · PDF de 34 páginas · 12 meses de acesso",
        "imagem": "/img/produtos/aula-stories-9399b9870909.png", "largura": 1200, "altura": 675,
        "alt": "Capa da aula O que postar nos stories, de Silvana",
        "url": "https://materiais.somosforster.com.br/aulas-stories-e-gravacao/#stories",
        "botao": "Conhecer a aula de stories",
    },
    {
        "id": "gravacao", "tipo": "Aula gravada com Samuel e Silvana", "tema": "verde",
        "titulo": "Grave seus próprios vídeos",
        "texto": "Veja como escolher o lugar, aproveitar a luz da janela e posicionar o celular para preparar a imagem e o som antes de gravar.",
        "detalhe": "28 minutos · Resumo em PDF e demonstrações · 12 meses de acesso",
        "imagem": "/img/produtos/aula-gravacao-8a3c244fdf42.jpg", "largura": 1200, "altura": 630,
        "alt": "Samuel e Silvana na capa da aula de gravação com o celular",
        "url": "https://materiais.somosforster.com.br/aulas-stories-e-gravacao/#gravacao",
        "botao": "Conhecer a aula de gravação",
    },
    {
        "id": "pasta-da-empresa", "tipo": "Modelos e guia prático", "tema": "areia",
        "titulo": "Como integrar a IA ao seu negócio",
        "texto": "Crie a base de informações que a IA precisa consultar para trabalhar com você. Você recebe modelos prontos, uma entrevista que ajuda a preenchê-los e um guia para começar.",
        "detalhe": "Modelos de arquivos · Entrevista guiada · Guia da primeira meia hora",
        "imagem": "/img/produtos/pasta-da-empresa-a180978f3414.jpg", "largura": 1280, "altura": 720,
        "alt": "Demonstração da entrevista com a IA para preencher os arquivos da empresa",
        "url": "https://materiais.somosforster.com.br/pasta-da-empresa-b58d20f6/",
        "botao": "Conhecer os modelos e o guia",
    },
]

CSS_PRODUTOS = """
.produtos-abertura{padding:72px clamp(20px,8.3vw,120px) 60px;background:#EFE8DA}
.produtos-abertura .kick{margin-bottom:22px}
.produtos-abertura h1{font-size:clamp(38px,4.8vw,68px);line-height:1.05;max-width:18ch;letter-spacing:-.025em}
.produtos-abertura .sup{margin-top:26px;max-width:58ch}
.produtos-indice{display:flex;gap:12px 28px;flex-wrap:wrap;margin-top:30px}
.produtos-indice a{color:#3A4638;min-height:44px;display:inline-flex;align-items:center;border-bottom:1px solid #3A4638;font-size:15px}
.produto{--acento:#93462F;--fundo:#F7F3EC;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);align-items:center;padding:64px clamp(20px,8.3vw,120px);background:var(--fundo);border-top:1px solid rgba(38,34,32,.14);scroll-margin-top:20px}
.produto-verde{--acento:#3A4638;--fundo:#EEF0E8}
.produto-areia{--acento:#3A4638;--fundo:#EFE8DA}
.produto-imagem{margin:0;min-width:0}
.produto-imagem img{display:block;width:100%;height:auto;border:1px solid rgba(38,34,32,.15)}
.produto .kick{color:var(--acento);font-size:11px;letter-spacing:.13em;line-height:1.6}
.produto h2{font-size:clamp(29px,3.1vw,44px);line-height:1.12;margin:17px 0 20px;letter-spacing:-.015em}
.produto-texto{font-size:17px;line-height:1.65;max-width:48ch}
.produto-detalhe{font-size:14px;line-height:1.65;margin-top:22px;color:#61594F}
.produto-botao{display:inline-flex;align-items:center;justify-content:space-between;gap:20px;min-height:46px;padding:12px 19px;border:1px solid var(--acento);border-radius:4px;color:var(--acento);font-size:15px;line-height:1.5;margin-top:24px;box-sizing:border-box}
.produto-botao:hover{color:#F7F3EC;background:var(--acento)}
.produtos-pacote{padding:38px clamp(20px,8.3vw,120px);display:flex;justify-content:space-between;align-items:center;gap:24px 40px;flex-wrap:wrap;background:#3A4638;color:#F7F3EC}
.produtos-pacote h2{font-size:26px;line-height:1.2}
.produtos-pacote p{font-size:16px;line-height:1.6;margin-top:10px;max-width:56ch}
.produtos-pacote a{color:#F7F3EC;border-color:#F7F3EC;margin:0}
.produtos-pacote a:hover{background:#F7F3EC;color:#3A4638}
.produtos-pacote a:focus-visible{outline-color:#F7F3EC}
@media(max-width:760px){.produtos-abertura{padding-top:44px;padding-bottom:42px}.produto{grid-template-columns:1fr;padding-top:40px;padding-bottom:44px;gap:28px}.produto-botao{max-width:100%}.produtos-indice{gap:8px 22px}.produtos-abertura h1{max-width:19ch}}
"""


def page_produtos():
    partes = ['''<section class="produtos-abertura" aria-labelledby="titulo-produtos">
<p class="kick">PRODUTOS DA FORSTER</p>
<h1 class="h" id="titulo-produtos">Aulas e materiais para aplicar no seu trabalho.</h1>
<p class="sup t">Aprenda a contar o que faz, prepare seus vídeos e comece a integrar a IA ao seu negócio. Conheça os conteúdos que você pode comprar e usar no seu ritmo.</p>
<nav class="produtos-indice" aria-label="Produtos disponíveis"><a href="#stories">Stories</a><a href="#gravacao">Gravação com o celular</a><a href="#pasta-da-empresa">IA no negócio</a></nav>
</section>''']
    for n, produto in enumerate(PRODUTOS):
        p = {chave: escape(str(valor), quote=True) for chave, valor in produto.items()}
        imagem = f'''<figure class="produto-imagem"><img src="{p['imagem']}" alt="{p['alt']}" width="{p['largura']}" height="{p['altura']}" loading="lazy" decoding="async"></figure>'''
        texto = f'''<div><p class="kick">{p['tipo']}</p><h2 class="h" id="titulo-{p['id']}">{p['titulo']}</h2><p class="produto-texto t">{p['texto']}</p><p class="produto-detalhe t">{p['detalhe']}</p><a class="produto-botao t5" href="{p['url']}" target="_blank" rel="noopener noreferrer">{p['botao']}<span aria-hidden="true">→</span></a></div>'''
        partes.append(f'''<section class="produto produto-{p['tema']}" id="{p['id']}" aria-labelledby="titulo-{p['id']}">{imagem}{texto}</section>''')
        if n == 1:
            partes.append('''<section class="produtos-pacote" aria-labelledby="titulo-pacote"><div><h2 class="h" id="titulo-pacote">As duas aulas também estão disponíveis juntas.</h2><p class="t">O pacote reúne stories e gravação com o celular, com todos os materiais das duas aulas.</p></div><a class="produto-botao t5" href="https://materiais.somosforster.com.br/aulas-stories-e-gravacao/#comprar" target="_blank" rel="noopener noreferrer">Ver as opções de compra<span aria-hidden="true">→</span></a></section>''')
    return "\n".join(partes)
