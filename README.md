# forster-site

Site da FORSTER · Ateliê de Conteúdo — somosforster.com.br

- `public/` é o que o Cloudflare Pages publica (build `exit 0`, output `public`).
- O domínio antigo forsterfilmes.com redireciona (301) para somosforster.com.br por uma Redirect Rule na zona forsterfilmes.com da Cloudflare; nada no repo cuida disso.
- `_fontes/gen_site.py` gera as páginas de `public/` (rodar com `python3 _fontes/gen_site.py`).
  Não editar os HTMLs gerados diretamente.
- As fontes visuais estão no projeto [Forster site implementation](https://claude.ai/design/p/ec94a935-7c92-48fc-a4bb-4faf1766289f)
  no Claude Design. As seis páginas da revisão de 25/10/2026 ficam em `_fontes/paginas/`.
  Alterações de arte passam pelo chat do Design; antes da portagem, reler a página atual.
  As páginas antigas do projeto foram preservadas.
- `_fontes/design_pages.py` integra o corpo, o CSS e as interações dessas páginas, convertendo
  os endereços do próprio site para as rotas locais. Títulos, descrições, dados estruturados,
  Analytics e sitemap continuam no gerador. Blog e páginas de entrada mantêm suas fontes próprias.
- `_fontes/site.js` reúne o comportamento das páginas auxiliares e os eventos de medição.
  As páginas da revisão usam seu próprio diálogo de vídeo, sem reproduzir antes do clique.

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

## Prévia dos links da Casa Marco — 28/10/2026

- Rota temporária: `/previas/casa-marco-b7f4/`, com `noindex`, fora do sitemap e da navegação.
- Fonte visual: projeto Casa Marco no Claude Design, página `Links da bio - Casa Marco.dc.html`; exportação `exportacao/links-da-bio/index.html`. Reler a versão atual antes de cada portagem.
- Fonte local: `_fontes/casa-marco-links.html`, com logo e fontes incorporados. Para publicar alterações desta prévia: `cp _fontes/casa-marco-links.html public/previas/casa-marco-b7f4/index.html`.
- Esta página é independente de `gen_site.py`, de `site.js` e do GA4. A prévia não tem contador de toques; a política CSP no HTML bloqueia scripts e conexões de medição, inclusive o beacon que a hospedagem injeta automaticamente.
- Os horários por unidade foram confirmados por Samuel em 28/10/2026, a partir dos cards oficiais do Instagram. Dados e decisões editoriais ficam no Briefing e na proposta da Casa Marco no Vault.
