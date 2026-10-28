// Hosts antigos (www) -> dominio final, 301, mantendo caminho e query.
// Fica aqui porque o _redirects do Pages ignora regra com host (testado em 04/09/2026: devolvia 200).
// *.pages.dev fica de fora, para preview continuar funcionando.
// forsterfilmes.com nao entra: tem Redirect Rule propria na zona dele.
const FINAL = 'somosforster.com.br';
const ANTIGOS = new Set(['www.somosforster.com.br']);

export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  if (ANTIGOS.has(url.hostname)) {
    url.hostname = FINAL;
    url.protocol = 'https:';
    return Response.redirect(url.toString(), 301);
  }
  // O link já publicado na bio usa esta campanha. Só essa entrada vai à apresentação do Instagram.
  if (url.hostname === FINAL && url.pathname === '/' &&
      url.searchParams.get('utm_source') === 'ig' &&
      url.searchParams.get('utm_medium') === 'social' &&
      url.searchParams.get('utm_content') === 'link_in_bio') {
    url.pathname = '/instagram';
    return Response.redirect(url.toString(), 302);
  }
  // Proposta Casa Marco: validade de 15 dias a partir do envio previsto em 28/10/2026.
  // Atualizar a data se o envio ocorrer em outro dia. A regra afeta somente esta proposta.
  if (url.pathname === '/propostas/casa-marco-342a90b3' ||
      url.pathname.startsWith('/propostas/casa-marco-342a90b3/')) {
    const fim = new Date('2026-10-28T23:59:59-03:00').getTime() + 15 * 86400000;
    if (Date.now() > fim) {
      return new Response(`<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Proposta encerrada · Forster</title><style>body{background:#f7f3ec;color:#262c27;font:18px/1.6 system-ui,sans-serif;max-width:600px;margin:15vh auto;padding:24px}a{color:#3a4638}</style><h1>Esta proposta encerrou o prazo de validade.</h1><p>Fale com o Samuel para atualizar as condições do projeto.</p><a href="https://wa.me/5551981578225" target="_blank" rel="noopener">Conversar pelo WhatsApp</a></html>`, {
        status: 410,
        headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' }
      });
    }
  }
  return next();
}
