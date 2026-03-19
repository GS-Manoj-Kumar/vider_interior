const track = document.getElementById('reels-track');
const container = document.getElementById('reels-container');

if (track && container) {

  // --- Auto scroll ---
  let autoScrollSpeed = 0.5;
  let isUserInteracting = false;
  let animationId;

  function autoScroll() {
    if (!isUserInteracting) {
      container.scrollLeft += autoScrollSpeed;
      // seamless loop — when we reach halfway, reset to start
      if (container.scrollLeft >= track.scrollWidth / 2) {
        container.scrollLeft = 0;
      }
    }
    animationId = requestAnimationFrame(autoScroll);
  }

  animationId = requestAnimationFrame(autoScroll);

  // --- Drag to scroll (mouse) ---
  let isDragging = false;
  let startX = 0;
  let scrollStart = 0;

  container.addEventListener('mousedown', (e) => {
    isDragging = true;
    isUserInteracting = true;
    startX = e.pageX - container.offsetLeft;
    scrollStart = container.scrollLeft;
    container.style.cursor = 'grabbing';
  });

  container.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    e.preventDefault();
    const x = e.pageX - container.offsetLeft;
    const walk = (x - startX) * 2;
    container.scrollLeft = scrollStart - walk;
  });

  container.addEventListener('mouseup', () => {
    isDragging = false;
    container.style.cursor = 'grab';
    setTimeout(() => { isUserInteracting = false; }, 1500);
  });

  container.addEventListener('mouseleave', () => {
    isDragging = false;
    container.style.cursor = 'grab';
    setTimeout(() => { isUserInteracting = false; }, 1500);
  });

  // --- Touch scroll ---
  container.addEventListener('touchstart', () => {
    isUserInteracting = true;
  }, { passive: true });

  container.addEventListener('touchend', () => {
    setTimeout(() => { isUserInteracting = false; }, 3000);
  });

  // --- Set initial cursor ---
  container.style.cursor = 'grab';
}