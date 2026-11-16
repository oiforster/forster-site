/* Vanessa Costa Mainardi — comportamento das páginas */
(function () {
  'use strict';

  var calmo = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var temObservador = 'IntersectionObserver' in window;

  function medir(evento) {
    window.gtag && window.gtag('event', evento, { pagina: location.pathname });
  }

  /* Cliques em qualquer link do WhatsApp */
  document.addEventListener('click', function (e) {
    var link = e.target && e.target.closest ? e.target.closest('a[href*="wa.me/"]') : null;
    if (link) medir('clique_whatsapp');
  });

  /* Copiar chave Pix (script do arquivo da Silvana + medição) */
  document.querySelectorAll('.copy-btn').forEach(function (b) {
    b.addEventListener('click', function () {
      var k = b.getAttribute('data-key');
      medir('copiar_pix');
      var done = function () { b.textContent = 'Chave copiada'; setTimeout(function () { b.textContent = 'Copiar chave Pix'; }, 2000); };
      try {
        if (navigator.clipboard) { navigator.clipboard.writeText(k).then(done, function () { window.prompt('Copie a chave:', k); }); }
        else { window.prompt('Copie a chave:', k); }
      } catch (err) { window.prompt('Copie a chave:', k); }
    });
  });

  /* Vídeo da abertura: para quando sai da tela; menos movimento = imagem parada */
  var abertura = document.querySelector('.abertura');
  var videoAbertura = document.querySelector('.abertura-video');
  if (videoAbertura) {
    if (calmo) {
      videoAbertura.removeAttribute('autoplay');
      videoAbertura.pause();
    } else if (temObservador) {
      new IntersectionObserver(function (es) {
        if (es[0].isIntersecting) {
          var p = videoAbertura.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          videoAbertura.pause();
        }
      }).observe(videoAbertura);
    }
  }

  /* Barra fixa no celular: aparece depois da abertura, some no convite final e enquanto o Reel toca */
  var barra = document.querySelector('.barra');
  var ctaFinal = document.querySelector('#convite .cta');
  var reel = document.querySelector('.reel video');
  if (barra && abertura && ctaFinal && temObservador) {
    var passou = false, chegou = false, tocando = false;
    var atualizar = function () { barra.classList.toggle('visivel', passou && !chegou && !tocando); };
    new IntersectionObserver(function (es) {
      passou = !es[0].isIntersecting && es[0].boundingClientRect.top < 0;
      atualizar();
    }).observe(abertura);
    new IntersectionObserver(function (es) {
      chegou = es[0].isIntersecting || es[0].boundingClientRect.top < 0;
      atualizar();
    }).observe(ctaFinal);
    if (reel) {
      reel.addEventListener('play', function () { tocando = true; atualizar(); });
      reel.addEventListener('pause', function () { tocando = false; atualizar(); });
      reel.addEventListener('ended', function () { tocando = false; atualizar(); });
    }
  }

  /* Privacidade: "Não contar minhas visitas" grava 'sem-medicao' e desliga o GA (ver ga.js) */
  var botaoMedicao = document.querySelector('.botao-medicao');
  if (botaoMedicao) {
    var semMedicao = false;
    try { semMedicao = localStorage.getItem('sem-medicao') === '1'; } catch (err) {}
    var mostrar = function () {
      botaoMedicao.textContent = semMedicao ? 'Voltar a contar minhas visitas' : 'Não contar minhas visitas';
    };
    mostrar();
    botaoMedicao.addEventListener('click', function () {
      semMedicao = !semMedicao;
      try {
        if (semMedicao) localStorage.setItem('sem-medicao', '1');
        else localStorage.removeItem('sem-medicao');
      } catch (err) {}
      if (typeof GA4_ID !== 'undefined' && GA4_ID) window['ga-disable-' + GA4_ID] = semMedicao;
      mostrar();
    });
  }

  if (calmo) return;

  /* A página clareia: cada faixa nasce com a cor da anterior e chega à sua enquanto sobe */
  var faixas = Array.prototype.slice.call(document.querySelectorAll('[data-luz]'));
  // Cor sem transparência; seção sem cor própria fica com a do CSS (antes virava preto).
  var rgb = function (el) {
    var m = getComputedStyle(el).backgroundColor.match(/[\d.]+/g);
    if (!m || m.length < 3 || (m.length > 3 && Number(m[3]) === 0)) return null;
    return m.slice(0, 3).map(Number);
  };
  var claro = function (el) { return el.classList.contains('claro'); };
  var pares = [];
  // Só lê as cores com o CSS já aplicado: no Safari a leitura antes do load vinha sem cor e pintava preto.
  var iniciarLuz = function () {
  for (var i = 1; i < faixas.length; i++) {
    if (claro(faixas[i]) !== claro(faixas[i - 1])) continue;
    var de = rgb(faixas[i - 1]), para = rgb(faixas[i]);
    if (de && para) pares.push({ el: faixas[i], de: de, para: para });
  }
  var pedido = false;
  var pintar = function () {
    pedido = false;
    var vh = window.innerHeight || 1;
    pares.forEach(function (p) {
      var k = (vh - p.el.getBoundingClientRect().top) / (vh * 0.7);
      k = k < 0 ? 0 : k > 1 ? 1 : k;
      k = k * k * (3 - 2 * k);
      p.el.style.backgroundColor = 'rgb(' + p.de.map(function (v, j) {
        return Math.round(v + (p.para[j] - v) * k);
      }).join(',') + ')';
    });
  };
  var pedir = function () { if (!pedido) { pedido = true; requestAnimationFrame(pintar); } };
  if (pares.length) {
    window.addEventListener('scroll', pedir, { passive: true });
    window.addEventListener('resize', pedir);
    pintar();
  }
  };
  if (document.readyState === 'complete') iniciarLuz(); else window.addEventListener('load', iniciarLuz);

  /* O silêncio cresce devagar quando a linha entra na tela */
  var cresce = document.querySelector('.cresce');
  if (cresce && temObservador) {
    cresce.classList.add('espera');
    var obs = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) {
        obs.disconnect();
        requestAnimationFrame(function () { cresce.classList.remove('espera'); });
      }
    }, { threshold: 0.9 });
    obs.observe(cresce);
  }
})();
