with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

client_carousel_js = '''  // 10. Client Logos Infinite Auto-Scroll Carousel Engine
  const initClientCarousel = () => {
    const track = document.getElementById('clientCarouselTrack');
    const viewport = document.getElementById('clientCarouselViewport');
    const dots = document.querySelectorAll('.client-carousel-dot');
    if (!track || !viewport || dots.length === 0) return;

    let isPaused = false;
    let currentX = 0;
    const speed = 0.85; // smooth gliding speed in px per frame
    let animId = null;
    let isTransitioning = false;

    // Helper: calculate stride (card width + gap)
    const getStride = () => {
      const firstCard = track.querySelector('.client-logo-card');
      if (!firstCard) return 380;
      const cardRect = firstCard.getBoundingClientRect();
      const style = window.getComputedStyle(track);
      const gap = parseFloat(style.gap) || 24;
      return cardRect.width + gap;
    };

    const updateDots = (activeIdx) => {
      dots.forEach((dot, idx) => {
        if (idx === activeIdx) {
          dot.classList.add('active');
          dot.setAttribute('aria-current', 'true');
        } else {
          dot.classList.remove('active');
          dot.setAttribute('aria-current', 'false');
        }
      });
    };

    const loop = () => {
      if (!isPaused && !isTransitioning) {
        const stride = getStride();
        const cycle = stride * 2; // 2 repeating cards per cycle
        currentX += speed;

        if (currentX >= cycle) {
          currentX = currentX % cycle;
        }

        track.style.transform = `translate3d(-${currentX}px, 0, 0)`;

        // Calculate active card index (0 or 1) based on current scroll position
        const activeIdx = Math.floor((currentX + stride * 0.4) / stride) % 2;
        updateDots(activeIdx);
      }
      animId = requestAnimationFrame(loop);
    };

    animId = requestAnimationFrame(loop);

    // Pause on hover
    viewport.addEventListener('mouseenter', () => { isPaused = true; });
    viewport.addEventListener('mouseleave', () => { isPaused = false; });

    // Touch swipe support for mobile
    let touchStartX = 0;
    let touchLastX = 0;
    let isTouching = false;

    viewport.addEventListener('touchstart', (e) => {
      isTouching = true;
      isPaused = true;
      touchStartX = e.touches[0].clientX;
      touchLastX = touchStartX;
    }, { passive: true });

    viewport.addEventListener('touchmove', (e) => {
      if (!isTouching) return;
      const touchX = e.touches[0].clientX;
      const deltaX = touchLastX - touchX;
      touchLastX = touchX;
      const stride = getStride();
      const cycle = stride * 2;
      currentX += deltaX;
      if (currentX < 0) currentX += cycle;
      if (currentX >= cycle) currentX = currentX % cycle;
      track.style.transform = `translate3d(-${currentX}px, 0, 0)`;
      const activeIdx = Math.floor((currentX + stride * 0.4) / stride) % 2;
      updateDots(activeIdx);
    }, { passive: true });

    viewport.addEventListener('touchend', () => {
      isTouching = false;
      setTimeout(() => {
        isPaused = false;
      }, 800);
    }, { passive: true });

    // Dot click interaction
    dots.forEach((dot) => {
      dot.addEventListener('click', (e) => {
        e.preventDefault();
        const targetIdx = parseInt(dot.getAttribute('data-index') || '0', 10);
        const stride = getStride();
        const cycle = stride * 2;

        isTransitioning = true;
        // Target scroll alignment
        const baseCycle = Math.floor(currentX / cycle) * cycle;
        let targetX = baseCycle + (targetIdx * stride);
        if (targetX < currentX - 10) {
          targetX += cycle;
        }

        // Smoothly interpolate to target position
        const startX = currentX;
        const diff = targetX - startX;
        const duration = 450;
        const startTime = performance.now();

        const stepAnim = (now) => {
          const elapsed = now - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // Ease-out cubic
          const ease = 1 - Math.pow(1 - progress, 3);
          currentX = startX + diff * ease;
          track.style.transform = `translate3d(-${currentX}px, 0, 0)`;

          if (progress < 1) {
            requestAnimationFrame(stepAnim);
          } else {
            currentX = currentX % cycle;
            track.style.transform = `translate3d(-${currentX}px, 0, 0)`;
            updateDots(targetIdx);
            setTimeout(() => {
              isTransitioning = false;
            }, 800);
          }
        };

        requestAnimationFrame(stepAnim);
      });
    });
  };

  initClientCarousel();
'''

target = "  initHeroSlider();"
if target in js:
    js_new = js.replace(target, target + "\n\n" + client_carousel_js)
    with open('js/script.js', 'w', encoding='utf-8') as f:
        f.write(js_new)
    print("Added initClientCarousel to js/script.js successfully.")
else:
    print("Could not find initHeroSlider in js/script.js")
