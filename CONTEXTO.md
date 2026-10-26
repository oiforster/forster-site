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
- (28/09/2026, noite) Perguntas frequentes do Acompanhamento ajustadas ao briefing (sem reunião de avaliação, sem "aprovado por link"; "Como começa" agora fala do estudo e do documento de diretrizes, sem "pilares" e "calendário do primeiro trimestre") e descrição do Service no dado estruturado trocada por um resumo do texto novo.

## 05/10/2026 — Diagnóstico do Google (Search Console pela conta de serviço dos relatórios)

- Das 7 páginas do sitemap, só a home está indexada. Mentoria, Sites, Sob encomenda e Trabalhos: "Detectada, mas não indexada" (o Google nunca rastreou). Acompanhamento e Privacidade: "O Google não reconhece o URL". Jul a out: 56 aparições, todas na home; nenhuma busca por serviço.
- Técnico em ordem: títulos com cidade, canonical, FAQPage, sitemap, robots, 200 para o Googlebot, links de crédito nos sites de Catarata, Prisma e Fyber.
- Feito: `<lastmod>` do sitemap pela última mudança real de cada página (era fixo em 2026-09-03), publicado (`071a015`) e sitemap reenviado pela API.
- Recomendado ao Samuel: pedir indexação das páginas no Search Console (só pela tela), blog com artigos de busca local, como nos clientes, H1 da home sem serviço nem cidade, descrições acima de 155 caracteres, Portfólio com pouco texto.
- Mesmo dia, depois: blog no ar em /blog/ com 4 artigos (vídeo institucional, site no Google, ficha do Google, gravar o mês numa sessão), camada do repo em `_fontes/blog_artigos.py`, fora do Claude Design; link "Blog" só no rodapé. Revisados pelo `revisor-texto` (correções aplicadas: afirmações sobre o Google, "numa tarde" virou "numa sessão", nada de "você confere por link" no acompanhamento). Também: H1 da home "ATELIÊ DE CONTEÚDO EM IGREJINHA, RS", descrições até 155 caracteres, Sites aponta para cataratacenter.com.br, prismaespecialidades.com.br e fybershow.com.br (eram os endereços pages.dev de aprovação), @fybershow, Portfólio com uma frase por grupo. Sitemap reenviado. Divergência com o Design: o H1 novo e o link do Blog no rodapé só existem no gerador; portar quando o site voltar ao Design.
- Ficha da FORSTER no Google: "Forster • Ateliê de Conteúdo", 11 avaliações, nota 5,0. Link de pedir avaliação: https://g.page/r/CWEccGG4-jyWEBM/review (enviado à Elis, da Casa Marco, pelo WhatsApp do Samuel em 05/10).
- Mesmo dia: rotina `blog-quinzenal-forster` criada (dias 1 e 15, 08:00). As 5 páginas de serviço entraram no Google entre 16h20 e 16h32, depois do reenvio do sitemap pela API; os artigos do blog ainda não, conferência automática rodando.
- 06/10/2026, conferência automática: 1 de 5 páginas do blog no Google ("como gravar o conteúdo do mês numa sessão"); /blog/ e os outros 3 artigos "Detectada, mas não indexada". Sitemap reenviado (204), aviso no Telegram.
- 15/10/2026, rotina quinzenal: artigo "Vídeo vertical ou horizontal: qual usar no site, no Instagram e no YouTube" publicado em https://somosforster.com.br/blog/video-vertical-ou-horizontal-site-instagram-youtube (leva para /sob-encomenda). Revisor de texto ok, correções aplicadas (antítese, "9 por 16 parecida com o celular", explicação de Reels/Shorts e enquadramento, lista em frase completa; saíram as frases sem fonte sobre planejar o enquadramento para vários formatos).
- 15/10/2026: sitemap reenviado (204); 4 de 5 artigos do blog "Enviada e indexada" (o novo ainda não reconhecido). Aviso no Telegram.

## 25/10/2026 — Página de links da Silvana (/silvana)

- Pedido do Samuel: uma página de links dentro do somosforster para a Silvana pôr na bio do @silvanaforster, na identidade da FORSTER.
- Bio dela hoje (conferida no perfil, 25/10): dois links, `somosforster.com.br` e o canal do Telegram "Comunicação Consciente" (`t.me/+8itHEv_NC6kwOTRh`, 21 inscritos, uma reflexão e uma pergunta por semana).
- O post fixado do Acompanhamento (rascunho de 22/10) promete "a proposta inteira, com o detalhamento de cada encontro, tá no link da bio", e o valor ficou na proposta. Por isso o destaque da página é a proposta: `propostas.somosforster.com.br/acompanhamento-comunicacao-consciente-363656cb/`.
- Página: `/silvana`, feita no gerador (`page_silvana`, camada do repo fora do Claude Design, como o blog), sem menu nem rodapé do site, `noindex` e fora do sitemap. Ordem: proposta do Acompanhamento (destaque), WhatsApp dela com a mensagem "Oi, Silvana! Vim pelo teu Instagram.", canal do Telegram, FORSTER. Texto em "tu", na voz dela. Os cliques entram no GA4 pelos eventos que o `site.js` já manda.
- Pedido do Samuel no mesmo dia: miniatura do link com a foto dela (`img/og-silvana-forster.jpg`, a mesma da proposta) e a apresentação da proposta, aprovada em 25/10, no fim da página, passada de "você" para "tu".
- Cuidado: a proposta vence pela regra dos 15 dias do forster-propostas (envio 24/10, sai do ar depois de 08/11) e cada abertura conta no registro de visita. Para ficar na bio, precisa de decisão do Samuel.
- Conferida em 375 px e no computador, sem erro no console. Pendências: a Silvana ler o texto (fala em primeira pessoa por ela), publicar e trocar a bio para um link só, `somosforster.com.br/silvana`.
- Publicada em 25/10 (`676d397`), junto com a proposta sem prazo (forster-propostas `24de7bb`) e sem aviso no Telegram (forster-aprovacoes `bb6d5e6`). Link e explicação mandados à Silvana pelo WhatsApp do Samuel, a pedido dele, às 03h16. Falta ela trocar a bio.

## 25/10/2026 — Revisão dos textos da página da Silvana

- Samuel pediu uma leitura mais humanizada e fluida e aprovou a aplicação e a publicação das seis sugestões apresentadas no chat.
- Ajustados a abertura, a descrição do acompanhamento, os convites para WhatsApp e Telegram e os três parágrafos da apresentação pessoal. Preservados a voz em primeira pessoa, o uso de tu, a referência ao Marketing Sistêmico, os títulos, os links, as condições do acompanhamento e o layout.
- Alteração limitada a `page_silvana` e ao HTML gerado. Conferência visual no navegador em 375 px e no computador, com os textos legíveis e sem cortes. Conferência de estrutura, atributos e destinos dos links antes da publicação pelo fluxo automático da main.
- Nenhum valor ou contato novo informado. Não há nova decisão editorial pendente para esta revisão.


## 25/10/2026 — Entrada do Instagram e apresentação dos serviços

- Samuel autorizou atualizar e publicar a bio, dois novos fixados, os destaques e uma página de entrada para o Instagram, com revisão dele na manhã seguinte. O vídeo continua em evidência; sites, planejamento de conteúdo e a orientação conduzida pela Silvana passam a ser apresentados com exemplos e caminhos próprios. Nenhum valor ou condição de serviço foi alterado.
- Nova rota `/instagram`, criada no projeto “Instagram Forster design screens” (`f6a9c8f8-91c3-4e78-8196-6bc629c18fc1`), arquivo `Entrada Instagram Forster.html`. Exportação salva em `_fontes/entrada-instagram-design.html` e integrada ao gerador como página independente, fora do sitemap. Na portagem, os caminhos das imagens passam a ser locais e os nove destinos externos abrem outra aba com `noopener`.
- A página apresenta os quatro serviços, sites reais, as funções de Samuel e Silvana, a proposta da Comunicação Consciente, o guia da pasta da empresa e os dois WhatsApps. Mantém três meses, cinco encontros ao vivo e uma aula gravada na mentoria.
- O Instagram web não permite editar o endereço da bio. O link já salvo aponta para a raiz com `utm_source=ig&utm_medium=social&utm_content=link_in_bio`. O middleware encaminha somente essa campanha para `/instagram`, com 302 e preservação dos parâmetros. A raiz comum e as demais campanhas continuam iguais.
- As 49 artes para a reorganização (13 quadros de carrossel, 16 Stories, 10 capas e 10 aberturas de Stories adaptadas das capas do Design) ficam em `public/img/instagram-20261025/`, com hash no nome para respeitar o cache imutável. O plano e o diário de publicação do Instagram ficam na pasta de trabalho da sessão, sem credenciais no repositório.
- Verificações: os 18 arquivos anteriores de HTML, CSS, JS e sitemap permaneceram byte a byte iguais após rodar o gerador. Conferidos contatos, links e arquivos de imagem. Revisão independente aprovou os quadros e Stories; a única captura inadequada foi substituída pelas páginas reais de exames e cirurgia do Catarata Center. Fonte e imagens carregadas nas exportações, sem corte dos textos. A navegação da prévia local foi bloqueada por uma permissão salva do navegador; Samuel já havia autorizado publicar com as verificações de código e conferir depois.
- Publicações e verificações finais do perfil serão registradas no Vault: `_Interno/Conteudo Forster/CONTEXTO.md` e `2026-10 - Perfil, fixados e destaques Forster.md`.

- Conferência pública no Safari, em 390×844: acrescentados na fonte do Design quatro atalhos para os serviços e uma âncora para os contatos logo na abertura. As capas também ganharam exportação para Stories, com o mesmo símbolo central e o nome da seção acima do recorte, para serem usadas pelo seletor normal de capas dos destaques na web.


### Fechamento da atualização do Instagram — 25/10/2026

A página final corresponde à versão publicada e foi conferida no Safari em 390 × 844 com os atalhos. Os 18 arquivos anteriores de HTML, CSS, JavaScript e sitemap permaneceram iguais. Publicados dois carrosséis (https://www.instagram.com/p/De6JcXIFqnH/ e https://www.instagram.com/p/De6JmuZFok3/) e 26 Stories. Os dez destaques do Instagram foram organizados com as capas novas; Vídeos, Sites, Conteúdo, Mentoria, Sobre e Clientes aparecem na frente.

A única pendência é trocar a fixação dos dois posts, mantendo o depoimento da Joele. A ação não apareceu no Instagram web, e a tentativa final de conexão pelo Espelhamento do iPhone esgotou o tempo. Nenhuma publicação anterior, anúncio, valor ou condição foi alterado. O registro completo e os links dos destaques estão no documento do Vault indicado acima.


## 25/10/2026 — Revisão do site completo

Samuel aprovou a nova home e autorizou seguir com as sugestões da auditoria. Comunicação, organização dos processos e criatividade orientam a apresentação. A identidade e o processo devem ajudar o trabalho criativo; a pessoa precisa reconhecer uma empresa criativa ao abrir o site.

- Seis páginas da revisão de 25/10 no projeto “Forster site implementation” do Claude Design: Home, Acompanhamento, Mentoria, Sites, Videos e Trabalhos. As páginas anteriores foram preservadas. As fontes foram relidas pelo editor do Design e comparadas integralmente com as composições revisadas antes da portagem para `_fontes/paginas/`.
- Home com trabalhos desde a abertura; serviços com composições próprias, exemplos reais e processo de trabalho. Portfólio agora reúne três sites e treze vídeos, com categorias e duração medida. Os exemplos da Polaris são identificados como calendário planejado. Prisma Especialidades de Novo Hamburgo tem um caminho separado para a Prisma Clínica de Olhos e suas unidades.
- Samuel confirmou: os planos mensais variam conforme a proposta e podem reunir só vídeos, só conteúdo ou um conjunto mais completo. Usar apenas “suporte por WhatsApp” na mentoria. A Silvana dirige sua comunicação principalmente às mães empreendedoras, mas atende qualquer pessoa; ser mãe não é requisito. Notas, FAQs e descrições para busca refletem essas definições. Valores e contatos foram preservados.
- Blog: título sobre gravar os vídeos do mês; pedido de avaliações sem selecionar apenas clientes satisfeitos; explicação do Search Console e de prazos de busca sem garantia de posição. Slugs preservados.
- Navegação por teclado, foco visível, perguntas frequentes nativas e vídeos por escolha do visitante. O menu das páginas auxiliares fecha com Escape e devolve o foco. Medição, escolha de não contar visitas, canonical, dados estruturados e rotas foram mantidos. As entradas /silvana e /instagram continuam fora do sitemap.
- Verificação: 16 HTMLs com links, arquivos, âncoras, H1, main e JSON-LD conferidos; revisão visual das páginas principais em 1440/390/320, larguras intermediárias 768/1024 sem transbordamento; vídeo reproduziu, fechou com Escape, interrompeu o carregamento e devolveu o foco. Ampliação das capturas e navegação entre serviços conferidas.

O registro de propostas e da aprovação fica no Vault em `_Interno/Sites/Proposta da home Forster/CONTEXTO.md`. Nenhuma nova decisão comercial pendente nesta revisão. A manutenção de sites após a entrega não recebeu promessa nova.


## 25/10/2026 — Movimento do S na home

Samuel pediu recuperar o desenho animado do S atrás da colagem da abertura. A fonte da home foi atualizada no chat do Design e relida antes da portagem. Movimento anterior recuperado: 2,4s, atraso de 0,5s, uma execução; com movimento reduzido, o traço fica completo e parado. A curva aparece acima do filme no computador, e o símbolo permite os cliques dos trabalhos abaixo. Corpo, textos, links, imagens e demais páginas preservados.

Conferidos o desenho do traço de 400 a 0, os cliques no vídeo e as larguras de 1440, 1024, 768, 390 e 320 pixels, sem transbordamento. As observações recentes de texto e da bio da Silvana foram comparadas com a revisão publicada; as novas sugestões ficaram para avaliação no chat. Registro no Vault: `_Interno/Sites/Proposta da home Forster/CONTEXTO.md`.


## 26/10/2026 — S aprovado na abertura

Samuel aprovou a prévia com o S reconhecível e um pequeno corte no topo e na base. O SVG ocupa o fundo da abertura, sem rotação, preservando as duas curvas. No celular, a escala é limitada pela largura para preservar a letra. A home foi relida e atualizada no chat do Design; a fonte salva foi lida novamente e portada ao gerador. Texto, colagem, links, contatos e interações mantidos.

Conferência: CSS e corpo gerados correspondem à prévia aprovada; 16 páginas sem erros estruturais; larguras 1440, 768, 390 e 320 sem transbordamento. O filme reproduziu, fechou com Escape e devolveu o foco. Animação e respeito a movimento reduzido preservados. Alteração restrita à home e sua data no sitemap.
