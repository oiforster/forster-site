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
  return next();
}
