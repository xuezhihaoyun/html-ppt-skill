(function() {
  // 获取当前页码，例如 slide_03.html → 3
  const match = location.pathname.match(/slide_(\d+)\.html$/);
  const current = match ? parseInt(match[1], 10) : 1;

  // 总页数 —— 根据实际页数修改
  const total = 28;

  // 更新计数器和进度条
  function updateUI() {
    const counter = document.getElementById('counter');
    const progress = document.getElementById('progress');
    const slideNum = document.getElementById('slide-num');
    if (counter) counter.textContent = `${current} / ${total}`;
    if (progress) progress.style.width = `${(current / total) * 100}%`;
    if (slideNum) slideNum.textContent = String(current).padStart(2, '0');
  }

  function go(n) {
    if (n < 1 || n > total) return;
    const filename = `slide_${String(n).padStart(2, '0')}.html`;
    location.href = filename;
  }

  window.next = function() { go(current + 1); };
  window.prev = function() { go(current - 1); };

  // 键盘控制
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Space') {
      e.preventDefault();
      window.next();
    }
    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      window.prev();
    }
    if (e.key === 'Home') { e.preventDefault(); go(1); }
    if (e.key === 'End')  { e.preventDefault(); go(total); }
    if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
  });

  // 触摸滑动
  let touchStartX = 0;
  document.addEventListener('touchstart', e => {
    touchStartX = e.touches[0].clientX;
  });
  document.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (dx < -50) window.next();
    if (dx > 50) window.prev();
  });

  updateUI();
})();
