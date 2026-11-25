/**
 * GSR GLOBAL ENTERPRISES - Corporate Frontend Script
 * Minimal vanilla JS for performance, smooth navigation, and client validation
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // 1. Navigation Scroll Effect
  const navbar = document.querySelector('.navbar-corporate');
  const backToTopBtn = document.getElementById('backToTopBtn');

  const handleScroll = () => {
    const scrollY = window.scrollY || window.pageYOffset;

    // Navbar solid state on scroll
    if (scrollY > 50) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }

    // Back to top visibility
    if (scrollY > 400) {
      backToTopBtn?.classList.add('show');
    } else {
      backToTopBtn?.classList.remove('show');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Initial check

  // Back to top click handler
  backToTopBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  // 2. Mobile Nav auto-collapse on link click
  const navLinks = document.querySelectorAll('.navbar-corporate .nav-link:not(.dropdown-toggle)');
  const navbarCollapse = document.querySelector('.navbar-collapse');
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (navbarCollapse?.classList.contains('show')) {
        // Trigger Bootstrap collapse if available
        const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
        if (bsCollapse) {
          bsCollapse.hide();
        } else {
          navbarCollapse.classList.remove('show');
        }
      }
    });
  });

  // 3. ScrollSpy / Active Link Highlighting
  const sections = document.querySelectorAll('section[id], footer[id]');
  const observeActiveSection = () => {
    const scrollPosition = (window.scrollY || window.pageYOffset) + 160;

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        navLinks.forEach((link) => {
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', observeActiveSection, { passive: true });

  // 4. Subtle Section Reveal using IntersectionObserver
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        root: null,
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
      }
    );

    document.querySelectorAll('.fade-up-element').forEach((el) => {
      revealObserver.observe(el);
    });
  } else {
    // Fallback if browser doesn't support IntersectionObserver
    document.querySelectorAll('.fade-up-element').forEach((el) => {
      el.classList.add('in-view');
    });
  }

  // 5. Service Quick Details Data and Modal Integration
  const serviceDetailsData = {
    'medical-equipment': {
      title: 'Medical Equipment & Devices Procurement',
      category: 'Procurement Sector 01',
      description: 'Procurement and supply of medical equipment, healthcare devices, and related clinical requirements. We partner with ISO and CE compliant manufacturers to ensure precision, reliability, and regulatory safety for medical centers.',
      items: [
        'Diagnostic & Patient Monitoring Systems',
        'Hospital Surgical Instruments & Equipment',
        'Clinical Laboratory Diagnostic Analyzers',
        'Healthcare Disposables & Sterilization Gear',
        'Emergency Care & ICU Support Hardware',
        'Custom Institutional Medical Sourcing'
      ],
      compliance: 'Strict adherence to medical-grade standards, manufacturer calibration records, and rapid institutional delivery.'
    },
    'it-infrastructure': {
      title: 'Computers & IT Infrastructure',
      category: 'Procurement Sector 02',
      description: 'Supply of computers, IT equipment, and digital infrastructure solutions specifically tailored for school transformation projects, academic institutions, and educational development programs.',
      items: [
        'Educational Desktop Workstations & Smart Laptops',
        'Interactive Smart Boards & Digital Classroom Displays',
        'Institutional Networking, Routers & Structured Cabling',
        'UPS Power Backup & Secure Server Cabinets',
        'Computer Lab Setup & Peripherals Supply',
        'Multi-facility Hardware Deployment'
      ],
      compliance: 'OEM-backed warranty support, bulk configuration, and turn-key deployment for state and private educational setups.'
    },
    'steel-yarn': {
      title: 'Iron, Steel & Yarn Procurement',
      category: 'Procurement Sector 03',
      description: 'Comprehensive procurement and supply of structural iron, TMT steel, and commercial yarn materials to satisfy demanding industrial, construction, and textile production requirements.',
      items: [
        'TMT Steel Bars (Fe 500 / 550 Grade Standards)',
        'Structural Steel Sections (Beams, Channels, Angles, Pipes)',
        'Industrial Grade Plates & Cold-Rolled Sheets',
        'Commercial & Industrial Cotton/Synthetic Yarn',
        'Specialty Textile Fibers & Heavy Filament Yarns',
        'Custom Bulk Mill-Direct Freight Coordination'
      ],
      compliance: 'Certified mill test reports (MTR), standard metallurgical tolerances, and transparent weight verification.'
    },
    'automobile-parts': {
      title: 'Automobile & Bus Spare Parts Procurement',
      category: 'Procurement Sector 04',
      description: 'Sourcing and procurement of automobile industry components and heavy-duty spare parts, with dedicated focus on commercial bus fleets, public transportation workshops, and transit vehicles.',
      items: [
        'Commercial Bus Chassis & Suspension Components',
        'Heavy-Duty Braking Drums, Liners & Air Brake Valves',
        'Engine Overhaul Components, Gaskets & Bearings',
        'Transmission Gears, Clutch Assemblies & Propeller Shafts',
        'Electrical Starters, Alternators & Fleet Lighting Systems',
        'OEM & Grade-A Aftermarket Maintenance Spares'
      ],
      compliance: 'High endurance benchmarks, precision dimensional matching for commercial fleet durability and workshop compatibility.'
    },
    'solar-procurement': {
      title: 'Solar Panel Procurement',
      category: 'Procurement Sector 05',
      description: 'Procurement and supply of premium solar panels, photovoltaic modules, and allied solar energy balance-of-system equipment for commercial, industrial, and institutional setups.',
      items: [
        'Tier-1 Monocrystalline & Polycrystalline Solar PV Modules',
        'Bifacial High-Efficiency Photovoltaic Arrays',
        'Grid-Tied & Hybrid Solar Inverters',
        'Galvanized Mounting Structures & Cable Connectors',
        'Solar Water Pumping & Institutional Arrays',
        'Comprehensive Component Procurement'
      ],
      compliance: 'MNRE / IEC approved certifications, verified wattage tolerances, and weather-resistant packaging.'
    }
  };

  const serviceModalElement = document.getElementById('serviceDetailModal');
  const serviceModal = serviceModalElement ? new bootstrap.Modal(serviceModalElement) : null;
  const modalTitle = document.getElementById('modalServiceTitle');
  const modalCategory = document.getElementById('modalServiceCategory');
  const modalDesc = document.getElementById('modalServiceDesc');
  const modalList = document.getElementById('modalServiceList');
  const modalCompliance = document.getElementById('modalServiceCompliance');
  const modalEnquireBtn = document.getElementById('modalEnquireBtn');

  // Trigger modal when clicking "Learn More"
  document.querySelectorAll('[data-service-key]').forEach((button) => {
    button.addEventListener('click', (e) => {
      e.preventDefault();
      const serviceKey = button.getAttribute('data-service-key');
      const data = serviceDetailsData[serviceKey];

      if (data && serviceModal) {
        if (modalTitle) modalTitle.textContent = data.title;
        if (modalCategory) modalCategory.textContent = data.category;
        if (modalDesc) modalDesc.textContent = data.description;
        if (modalCompliance) modalCompliance.textContent = data.compliance;

        if (modalList) {
          modalList.innerHTML = '';
          data.items.forEach((item) => {
            const li = document.createElement('li');
            li.className = 'mb-2 d-flex align-items-center gap-2';
            li.innerHTML = `<i class="bi bi-check-circle-fill text-bronze"></i> <span>${item}</span>`;
            modalList.appendChild(li);
          });
        }

        // Configure Enquire button inside modal
        if (modalEnquireBtn) {
          modalEnquireBtn.onclick = () => {
            serviceModal.hide();
            directEnquiryEmail(data.title);
          };
        }

        serviceModal.show();
      }
    });
  });

  // Direct Enquiry Email Helper
  const directEnquiryEmail = (serviceName) => {
    const subject = encodeURIComponent(`Procurement Enquiry: ${serviceName || 'GSR Global Services'}`);
    const body = encodeURIComponent(
      `Dear GSR Global Enterprises,\n\nI would like to enquire about your procurement and supply solutions for ${serviceName || 'your services'}.\n\nPlease share technical specifications, pricing, and supply timelines.\n\nBest regards`
    );
    window.location.href = `mailto:gsrglobalenterprises@gmail.com?subject=${subject}&body=${body}`;
  };

  // Wire quick "Enquire Now" buttons on service cards directly
  document.querySelectorAll('.service-enquire-btn').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetService = btn.getAttribute('data-service-name');
      directEnquiryEmail(targetService || '');
    });
  });

  // 6. About Section Pill Tab Switcher
  const aboutPillButtons = document.querySelectorAll('#aboutTab .nav-link');
  aboutPillButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetSelector = btn.getAttribute('data-bs-target');
      if (!targetSelector) return;

      // Update button active states
      aboutPillButtons.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      // Update pane states
      const allPanes = document.querySelectorAll('#aboutTabContent .tab-pane');
      allPanes.forEach((pane) => {
        pane.classList.remove('show', 'active');
      });

      const targetPane = document.querySelector(targetSelector);
      if (targetPane) {
        targetPane.classList.add('show', 'active');
      }
    });
  });

  // 7. Services Section Carousel Controls
  const servicesTrack = document.getElementById('servicesCarouselTrack');
  const servicesPrevBtn = document.getElementById('servicesCarouselPrev');
  const servicesNextBtn = document.getElementById('servicesCarouselNext');

  if (servicesTrack && servicesPrevBtn && servicesNextBtn) {
    const getScrollStep = () => {
      const firstCard = servicesTrack.querySelector('.service-carousel-card');
      return firstCard ? firstCard.getBoundingClientRect().width + 24 : 340;
    };

    servicesNextBtn.addEventListener('click', () => {
      const maxScroll = servicesTrack.scrollWidth - servicesTrack.clientWidth;
      if (servicesTrack.scrollLeft + 10 >= maxScroll) {
        servicesTrack.scrollTo({ left: 0, behavior: 'smooth' }); // Loop back
      } else {
        servicesTrack.scrollBy({ left: getScrollStep(), behavior: 'smooth' });
      }
    });

    servicesPrevBtn.addEventListener('click', () => {
      if (servicesTrack.scrollLeft <= 10) {
        servicesTrack.scrollTo({ left: servicesTrack.scrollWidth, behavior: 'smooth' }); // Loop to end
      } else {
        servicesTrack.scrollBy({ left: -getScrollStep(), behavior: 'smooth' });
      }
    });
  }

  // 8. Service Card "Enroll Now" Action Handler
  document.querySelectorAll('.btn-enroll-now').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const serviceCard = btn.closest('.service-carousel-card');
      const serviceTitle = serviceCard?.querySelector('.service-card-title')?.textContent?.trim() || 'Procurement Service';
      directEnquiryEmail(serviceTitle);
    });
  });

  // 9. Dedicated Professional Hero Cross-Fade Auto-Slider Engine
  const initHeroSlider = () => {
    const sliderEl = document.getElementById('heroSlider');
    const slides = document.querySelectorAll('.hero-slide');
    const prevBtn = document.getElementById('heroPrevBtn');
    const nextBtn = document.getElementById('heroNextBtn');
    const heroSection = document.getElementById('hero');

    if (!sliderEl || slides.length === 0) return;

    let currentSlide = 0;
    const totalSlides = slides.length;
    const slideDuration = 5500; // 5.5 seconds per slide
    let autoPlayTimer = null;

    const showSlide = (index) => {
      // Handle wrapping
      if (index >= totalSlides) {
        currentSlide = 0;
      } else if (index < 0) {
        currentSlide = totalSlides - 1;
      } else {
        currentSlide = index;
      }

      // Update slide active state
      slides.forEach((slide, idx) => {
        if (idx === currentSlide) {
          slide.classList.add('active');
          slide.setAttribute('aria-hidden', 'false');
        } else {
          slide.classList.remove('active');
          slide.setAttribute('aria-hidden', 'true');
        }
      });
    };

    const nextSlide = () => {
      showSlide(currentSlide + 1);
    };

    const prevSlide = () => {
      showSlide(currentSlide - 1);
    };

    const startAutoPlay = () => {
      stopAutoPlay();
      autoPlayTimer = setInterval(nextSlide, slideDuration);
    };

    const stopAutoPlay = () => {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
    };

    // Arrow controls
    prevBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      prevSlide();
      startAutoPlay();
    });

    nextBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      nextSlide();
      startAutoPlay();
    });

    // Pause on hover
    heroSection?.addEventListener('mouseenter', () => {
      stopAutoPlay();
    });

    heroSection?.addEventListener('mouseleave', () => {
      startAutoPlay();
    });

    // Touch swipe gestures for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    heroSection?.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    heroSection?.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) {
        nextSlide();
        startAutoPlay();
      } else if (touchEndX - touchStartX > 50) {
        prevSlide();
        startAutoPlay();
      }
    }, { passive: true });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      const heroRect = heroSection?.getBoundingClientRect();
      const isHeroVisible = heroRect && heroRect.top < window.innerHeight && heroRect.bottom > 0;
      if (isHeroVisible) {
        if (e.key === 'ArrowLeft') {
          prevSlide();
          startAutoPlay();
        } else if (e.key === 'ArrowRight') {
          nextSlide();
          startAutoPlay();
        }
      }
    });

    // Initial trigger
    showSlide(0);
    startAutoPlay();
  };

  initHeroSlider();

  // 10. 3D Cover-Flow Testimonials Carousel Engine
  const initTestimonialsCoverflow = () => {
    const stageWrapper = document.getElementById('testimonialsCoverflow');
    const cards = document.querySelectorAll('.coverflow-card');
    const dots = document.querySelectorAll('.coverflow-dot');
    const prevBtn = document.getElementById('coverflowPrevBtn');
    const nextBtn = document.getElementById('coverflowNextBtn');

    if (!stageWrapper || cards.length === 0) return;

    let currentIndex = 0;
    const totalCards = cards.length;
    const slideDuration = 5500;
    let autoPlayTimer = null;

    const updateCoverflow = () => {
      const windowWidth = window.innerWidth;

      // Determine responsive spacing steps
      let step1 = 260;
      let step2 = 450;
      let zStep1 = -120;
      let zStep2 = -240;
      let scale1 = 0.86;
      let scale2 = 0.74;

      if (windowWidth < 1200 && windowWidth >= 992) {
        step1 = 210;
        step2 = 380;
      } else if (windowWidth < 992 && windowWidth >= 768) {
        step1 = 150;
        step2 = 280;
        scale1 = 0.84;
        scale2 = 0.72;
      } else if (windowWidth < 768) {
        step1 = 65;
        step2 = 120;
        scale1 = 0.82;
        scale2 = 0.7;
        zStep1 = -60;
        zStep2 = -120;
      }

      cards.forEach((card, i) => {
        // Calculate shortest circular difference between i and currentIndex
        let diff = (i - currentIndex + totalCards) % totalCards;
        if (diff > totalCards / 2) {
          diff = diff - totalCards;
        }

        if (diff === 0) {
          // Active Center Card
          card.style.transform = 'translateX(0) scale(1) translateZ(0)';
          card.style.opacity = '1';
          card.style.zIndex = '5';
          card.style.filter = 'none';
          card.classList.add('active');
          card.setAttribute('aria-hidden', 'false');
        } else if (diff === 1) {
          // 1st Card to Right
          card.style.transform = `translateX(${step1}px) scale(${scale1}) translateZ(${zStep1}px)`;
          card.style.opacity = windowWidth < 768 ? '0.45' : '0.62';
          card.style.zIndex = '4';
          card.style.filter = 'brightness(0.92)';
          card.classList.remove('active');
          card.setAttribute('aria-hidden', 'true');
        } else if (diff === -1) {
          // 1st Card to Left
          card.style.transform = `translateX(-${step1}px) scale(${scale1}) translateZ(${zStep1}px)`;
          card.style.opacity = windowWidth < 768 ? '0.45' : '0.62';
          card.style.zIndex = '4';
          card.style.filter = 'brightness(0.92)';
          card.classList.remove('active');
          card.setAttribute('aria-hidden', 'true');
        } else if (diff === 2) {
          // 2nd Card to Right
          card.style.transform = `translateX(${step2}px) scale(${scale2}) translateZ(${zStep2}px)`;
          card.style.opacity = windowWidth < 768 ? '0.15' : '0.28';
          card.style.zIndex = '3';
          card.style.filter = 'brightness(0.8)';
          card.classList.remove('active');
          card.setAttribute('aria-hidden', 'true');
        } else if (diff === -2) {
          // 2nd Card to Left
          card.style.transform = `translateX(-${step2}px) scale(${scale2}) translateZ(${zStep2}px)`;
          card.style.opacity = windowWidth < 768 ? '0.15' : '0.28';
          card.style.zIndex = '3';
          card.style.filter = 'brightness(0.8)';
          card.classList.remove('active');
          card.setAttribute('aria-hidden', 'true');
        } else {
          // Cards further away
          card.style.transform = `translateX(${diff > 0 ? step2 + 50 : -step2 - 50}px) scale(0.6) translateZ(-300px)`;
          card.style.opacity = '0';
          card.style.zIndex = '1';
          card.classList.remove('active');
          card.setAttribute('aria-hidden', 'true');
        }
      });

      // Update dots
      dots.forEach((dot, idx) => {
        if (idx === currentIndex) {
          dot.classList.add('active');
          dot.setAttribute('aria-selected', 'true');
        } else {
          dot.classList.remove('active');
          dot.setAttribute('aria-selected', 'false');
        }
      });
    };

    const goToCard = (index) => {
      if (index >= totalCards) {
        currentIndex = 0;
      } else if (index < 0) {
        currentIndex = totalCards - 1;
      } else {
        currentIndex = index;
      }
      updateCoverflow();
    };

    const nextCard = () => goToCard(currentIndex + 1);
    const prevCard = () => goToCard(currentIndex - 1);

    const startAutoPlay = () => {
      stopAutoPlay();
      autoPlayTimer = setInterval(nextCard, slideDuration);
    };

    const stopAutoPlay = () => {
      if (autoPlayTimer) {
        clearInterval(autoPlayTimer);
        autoPlayTimer = null;
      }
    };

    // Card click directly navigates to that card
    cards.forEach((card, idx) => {
      card.addEventListener('click', () => {
        goToCard(idx);
        startAutoPlay();
      });
    });

    // Arrow navigation
    prevBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      prevCard();
      startAutoPlay();
    });

    nextBtn?.addEventListener('click', (e) => {
      e.preventDefault();
      nextCard();
      startAutoPlay();
    });

    // Dot indicators
    dots.forEach((dot, idx) => {
      dot.addEventListener('click', (e) => {
        e.preventDefault();
        goToCard(idx);
        startAutoPlay();
      });
    });

    // Pause on hover
    stageWrapper.addEventListener('mouseenter', stopAutoPlay);
    stageWrapper.addEventListener('mouseleave', startAutoPlay);

    // Touch Swipe handling
    let touchStartX = 0;
    let touchEndX = 0;

    stageWrapper.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    stageWrapper.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) {
        nextCard();
        startAutoPlay();
      } else if (touchEndX - touchStartX > 50) {
        prevCard();
        startAutoPlay();
      }
    }, { passive: true });

    // Responsive update on resize
    let resizeTimer = null;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(updateCoverflow, 100);
    }, { passive: true });

    // Initialize
    updateCoverflow();
    startAutoPlay();
  };

  initTestimonialsCoverflow();
});
