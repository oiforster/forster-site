# forster-site

Site da FORSTER · Ateliê de Conteúdo — somosforster.com.br

- `public/` é o que o Cloudflare Pages publica (build `exit 0`, output `public`).
- O domínio antigo forsterfilmes.com redireciona (301) para somosforster.com.br por uma Redirect Rule na zona forsterfilmes.com da Cloudflare; nada no repo cuida disso.
- `_fontes/gen_site.py` gera as páginas de `public/` (rodar com `python3 _fontes/gen_site.py`).
- A fonte da verdade de design é o projeto "Site Forster design" no Claude Design; alterações de
  layout nascem lá e são portadas para o gerador, nunca o contrário.

## Medição (Google Analytics 4)

- O ID da propriedade fica em `GA4_ID` no topo de `_fontes/gen_site.py` (formato `G-XXXXXXXXXX`).
  Vazio, nada é emitido. Preenchido, o gerador coloca a tag em todas as páginas.
- Consent Mode: só `analytics_storage` liberado; anúncios e personalização ficam negados.
- Sem banner de cookies: a base legal é o legítimo interesse para medição de audiência (guia de
  cookies da ANPD, p. 24). O que fica é a página `/privacidade`, linkada no rodapé, com o que é
  medido, retenção e um botão "Não contar minhas visitas" que grava `sem-medicao` no localStorage
  e liga `window['ga-disable-<ID>']` antes da tag carregar.
- Na propriedade do GA4, manter Google Signals e personalização de anúncios desligados.
- Eventos enviados por `site.js` (marcar como evento-chave no GA4 conforme o cliente):
  `clique_whatsapp` (pessoa, texto), `clique_instagram`, `clique_telefone`, `clique_email`,
  `clique_externo` (destino) e `play_video` (video, titulo).
- Para um site de cliente, o mesmo bloco vale: trocar o ID e a tabela `PESSOAS` (número → nome).
