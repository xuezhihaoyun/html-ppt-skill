(function() {
  var STAGE_WIDTH = 1600;
  var STAGE_HEIGHT = 900;
  var frames = Array.prototype.slice.call(document.querySelectorAll('iframe.frame'));
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var inMergedMode = frames.length > 0;
  var inPageMode = !inMergedMode && slides.length > 1;
  var match = location.pathname.match(/slide_(\d+)\.html$/);
  var DEFAULT = 1;
  var current = inMergedMode ? DEFAULT : (inPageMode ? getActiveSlideIndex() : (match ? parseInt(match[1], 10) : DEFAULT));

  function pad(n) { return n < 10 ? '0' + n : '' + n; }

  function applyStageScale() {
    var scale = Math.min(window.innerWidth / STAGE_WIDTH, window.innerHeight / STAGE_HEIGHT);
    document.documentElement.style.setProperty('--deck-scale', String(scale));
    document.documentElement.style.setProperty('--deck-width', STAGE_WIDTH + 'px');
    document.documentElement.style.setProperty('--deck-height', STAGE_HEIGHT + 'px');
  }

  function toggleFullscreen() {
    var doc = document;
    var root = doc.documentElement;
    var fullscreenElement = doc.fullscreenElement || doc.webkitFullscreenElement;
    if (!fullscreenElement) {
      var enter = root.requestFullscreen || root.webkitRequestFullscreen;
      if (enter) {
        var result = enter.call(root);
        if (result && result.catch) result.catch(function(){});
      }
      return;
    }
    var exit = doc.exitFullscreen || doc.webkitExitFullscreen;
    if (exit) {
      var exitResult = exit.call(doc);
      if (exitResult && exitResult.catch) exitResult.catch(function(){});
    }
  }

  function getActiveSlideIndex() {
    for (var i = 0; i < slides.length; i += 1) {
      if (slides[i].classList.contains('active')) return i + 1;
    }
    return DEFAULT;
  }

  function parseCounterText() {
    var el = document.getElementById('counter');
    if (el && el.textContent) {
      var m = el.textContent.match(/\/\s*(\d+)/);
      if (m) return parseInt(m[1], 10);
    }
    return DEFAULT;
  }

  function probeTotal(callback) {
    if (inMergedMode) { callback(frames.length); return; }
    if (inPageMode) { callback(slides.length); return; }
    if (location.protocol === 'file:') { callback(parseCounterText()); return; }

    var parsed = parseCounterText();
    if (!window.fetch || (location.protocol !== 'http:' && location.protocol !== 'https:')) {
      callback(parsed);
      return;
    }

    var found = 0;
    function tryNext(n) {
      fetch('slide_' + pad(n) + '.html', { method: 'HEAD', cache: 'no-store' })
        .then(function(response) {
          if (response.ok) {
            found = n;
            tryNext(n + 1);
            return;
          }
          callback(Math.max(found, parsed, DEFAULT));
        })
        .catch(function() {
          callback(Math.max(found, parsed, DEFAULT));
        });
    }
    tryNext(1);
  }

  var total = inMergedMode ? frames.length : (inPageMode ? slides.length : parseCounterText());
  probeTotal(function(t) { total = t; updateUI(); });

  function updateUI() {
    var counter = document.getElementById('counter');
    var progress = document.getElementById('progress');
    if (counter) counter.textContent = current + ' / ' + total;
    if (progress) progress.style.width = (current / total * 100) + '%';
  }

  function showInPage(n) {
    if (n < 1 || n > total) return;
    for (var i = 0; i < slides.length; i += 1) {
      var isActive = i === n - 1;
      slides[i].classList.toggle('active', isActive);
      slides[i].style.display = isActive ? '' : 'none';
    }
    current = n;
    updateUI();
  }

  function showMerged(n) {
    if (n < 1 || n > total) return;
    for (var i = 0; i < frames.length; i += 1) {
      frames[i].style.display = i === n - 1 ? 'block' : 'none';
    }
    current = n;
    updateUI();
  }

  function go(n) {
    if (n < 1 || n > total) return;
    if (inMergedMode) {
      showMerged(n);
      return;
    }
    if (inPageMode) {
      showInPage(n);
      return;
    }
    location.href = 'slide_' + pad(n) + '.html';
  }

  window.next = function() { go(current + 1); };
  window.prev = function() { go(current - 1); };

  function handleKey(e) {
    if (e.key === 'ArrowRight' || e.key === ' ') {
      e.preventDefault(); window.next();
    }
    if (e.key === 'ArrowLeft') {
      e.preventDefault(); window.prev();
    }
    if (e.key === 'Home') { e.preventDefault(); go(1); }
    if (e.key === 'End') { e.preventDefault(); go(total); }
    if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      toggleFullscreen();
    }
  }

  function bindTouch(target) {
    var touchStartX = 0;
    target.addEventListener('touchstart', function(e) {
      if (e.touches && e.touches.length) touchStartX = e.touches[0].clientX;
    }, { passive: true });
    target.addEventListener('touchend', function(e) {
      if (!e.changedTouches || !e.changedTouches.length) return;
      var dx = e.changedTouches[0].clientX - touchStartX;
      if (dx < -50) window.next();
      if (dx > 50) window.prev();
    }, { passive: true });
  }

  function bindInput(target) {
    if (!target || target.__htmlPptNavigationBound) return;
    target.__htmlPptNavigationBound = true;
    target.addEventListener('keydown', handleKey);
    bindTouch(target);
  }

  function bindFrameInput(frame) {
    try {
      bindInput(frame.contentDocument);
    } catch (e) {}
  }

  bindInput(document);
  if (inMergedMode) {
    frames.forEach(function(frame) {
      frame.addEventListener('load', function() { bindFrameInput(frame); });
      bindFrameInput(frame);
    });
  }

  window.addEventListener('resize', applyStageScale);
  document.addEventListener('fullscreenchange', applyStageScale);
  document.addEventListener('webkitfullscreenchange', applyStageScale);
  applyStageScale();
  if (inMergedMode) showMerged(current);
  else if (inPageMode) showInPage(current);
  else updateUI();
})();
