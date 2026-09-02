if ('IntersectionObserver' in window) {
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
var PESSOAS = {"5551981578225": "samuel", "5551980603512": "silvana"};
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
if (typeof gtag === 'function') {
  var visto = null;
  try { visto = localStorage.getItem('aviso-medicao'); } catch (err) {}
  if (!visto) {
    var av = document.createElement('div');
    av.className = 'aviso';
    av.setAttribute('role', 'status');
    av.innerHTML = '<span class="t">Este site usa o Google Analytics para medir visitas. Os dados são agregados e não identificam você.</span>'
      + '<button class="aviso-ok" type="button">Entendi</button>';
    document.body.appendChild(av);
    av.querySelector('button').addEventListener('click', function () {
      try { localStorage.setItem('aviso-medicao', '1'); } catch (err) {}
      av.remove();
    });
  }
}
