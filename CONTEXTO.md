# CONTEXTO — Site da FORSTER (somosforster.com.br)

Log de decisões datado. Fatos permanentes do projeto ficam no `README.md`;
o passo a passo de uma tarefa fechada fica em `docs/`.

## 2026-09-07 — Indexação: os dois defeitos que o Search Console apontou

Chegaram três avisos do Search Console (06/09) sobre somosforster, cataratacenter e
prismaespecialidades. A maior parte era ruído esperado. Sobraram dois defeitos reais, os dois só
no site da Forster, e os dois foram corrigidos hoje.

**1. Qualquer rota inexistente devolvia a home com 200.** O Cloudflare Pages sem `404.html`
responde 200 em vez de 404, e o Google lê isso como erro de indexação. Criada a página 404 no
gerador (`page_404`), com `noindex`, sem canonical e fora do sitemap, porque ela é servida em
qualquer endereço e não tem URL própria. Catarata e Prisma já tinham a delas desde 04/09.

**2. `www.somosforster.com.br` servia o site inteiro com 200.** O site estava no ar em dois
endereços, o que é conteúdo duplicado. Resolvido com `functions/_middleware.js`, o mesmo mecanismo
que Catarata e Prisma usam desde 04/09. O `_redirects` do Pages **não** serve para isso: ele ignora
regra que tenha host. `forsterfilmes.com` ficou de fora porque já tem Redirect Rule na zona dele.

Verificado no ar: www responde 301 mantendo caminho e query, rota inexistente responde 404, as sete
páginas seguem em 200 e o preview `forster-site.pages.dev` continua acessível.

### O que era ruído, e por quê

- **"Página com redirecionamento"**: as URLs `.html` fazem 308 para as versões sem extensão.
  Comportamento correto do Pages.
- **"Excluída pela tag noindex"** (Catarata): é a `privacidade.html` e a `404.html`, de propósito.
- **"Indexada, mas bloqueada pelo robots.txt"** (Catarata e Prisma): o robots.txt dos dois libera
  tudo hoje. Resíduo da janela de publicação nos domínios próprios em 04/09. Se o robots.txt fica
  inacessível, o Google trata como bloqueio total e guarda por cerca de 24 h. Só validar no painel.
- **"Monitorar o tráfego da Pesquisa"**: é o Google avisando que os sites começaram a aparecer.

## 2026-09-07 — robots.txt: manter o gerenciado da Cloudflare

A zona `somosforster.com.br` tem o robots.txt gerenciado da Cloudflare ligado, e ele **sobrescreve**
o `public/robots.txt` que o gerador escreve. Só a somosforster está assim.

**Decisão: manter.** A lista que ele bloqueia é quase toda de crawler de treinamento (GPTBot,
ClaudeBot, CCBot, Google-Extended, Applebot-Extended, meta-externalagent, Bytespider, Amazonbot).
Os robôs que colocam o site nas respostas de IA são outros e seguem liberados: o OAI-SearchBot do
ChatGPT não está na lista, e as AI Overviews do Google são governadas pelo Googlebot normal, não
pelo Google-Extended. Não custa busca nem descoberta.

Ficou um comentário de alerta no `gen_site.py`, acima da escrita do `robots.txt`, para o arquivo
morto não enganar ninguém depois. Para mudar o robots.txt de verdade, é no painel da Cloudflare.

## Pendências

- O `gen_site.py` ainda escreve um `index.html` na raiz do repo, o redirecionamento do
  forsterfilmes.com pelo GitHub Pages. Esse arquivo foi apagado de propósito no commit `9f502c7`,
  e hoje o redirecionamento é uma Redirect Rule na Cloudflare. O bloco deveria sair do gerador,
  senão toda execução recria o arquivo órfão.
- O Search Console também listou "Não encontrado (404)" para somosforster. Não deu para reproduzir
  nenhum 404 por fora, porque até hoje o site respondia 200 em tudo. Vale abrir o relatório de
  indexação para ver quais URLs são.

- (28/09/2026) Abertura da página /acompanhamento trocada pelo texto que o Samuel reescreveu ("No nosso acompanhamento mensal, a base da sua comunicação digital fica por nossa conta..."), sem ajuste. É o mesmo texto que vai descrever o serviço na ficha do Google. Os resumos curtos da página inicial e da 404 ficaram como estavam. A lista "O que está incluso" da página ainda não cita site nem Perfil da Empresa no Google, que o texto novo inclui.
- (28/09/2026, noite) Acompanhamento reescrito conforme o briefing do Samuel (vídeo é parte do trabalho, sem "você aprova", sem reunião mensal): "Como funciona" virou Estudo, Diretrizes, Roteiro, Gravação, Produção e publicação, E começa de novo; "O que está incluso" virou "Do que a gente cuida" (11 itens, com a linha "O conjunto de cada cliente é definido na proposta."); resumo do cartão na página inicial e na 404 trocado. As Perguntas frequentes da página ainda citam reunião de avaliação e aprovação por link: aguardando o Samuel.
