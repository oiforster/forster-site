# forster-site

Site da FORSTER · Ateliê de Conteúdo — somosforster.com.br

- `public/` é o que o Cloudflare Pages publica (build `exit 0`, output `public`).
- `index.html` na raiz é o redirecionamento do domínio antigo forsterfilmes.com (GitHub Pages).
- `_fontes/gen_site.py` gera as páginas de `public/` (rodar com `python3 _fontes/gen_site.py`).
- A fonte da verdade de design é o projeto "Site Forster design" no Claude Design; alterações de
  layout nascem lá e são portadas para o gerador, nunca o contrário.
