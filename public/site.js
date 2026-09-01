if ('IntersectionObserver' in window) {
  document.documentElement.classList.add('js');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('vis'); io.unobserve(en.target); }
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.rv').forEach(function (el) { io.observe(el); });
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
});
