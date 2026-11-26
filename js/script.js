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

  // 2. Mobile Nav auto-close on link click (Side Offcanvas Drawer)
  const navLinks = document.querySelectorAll('#navbarOffcanvas .nav-link, #navbarOffcanvas .header-cta-orange');
  const offcanvasEl = document.getElementById('navbarOffcanvas');
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (offcanvasEl?.classList.contains('show')) {
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasEl) || new bootstrap.Offcanvas(offcanvasEl);
        bsOffcanvas.hide();
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
    'medical': {
      title: 'Medical & Healthcare Supplies',
      category: 'Procurement Sector 01',
      description: 'Procurement and supply of hospital-grade medical equipment, clinical diagnostic devices, surgical instruments, sterilization systems, and certified clinical consumables. Compliant with ISO and CE standards.',
      items: [
        'Diagnostic & Patient Monitoring Systems',
        'Hospital Surgical Instruments & Equipment',
        'Clinical Laboratory Diagnostic Analyzers',
        'Healthcare Disposables & Sterilization Gear',
        'Emergency Care & ICU Support Hardware',
        'Direct OEM Healthcare Sourcing'
      ],
      compliance: 'Strict adherence to medical-grade standards, manufacturer calibration records, and rapid institutional delivery.'
    },
    'medical-equipment': {
      title: 'Medical & Healthcare Supplies',
      category: 'Procurement Sector 01',
      description: 'Procurement and supply of medical equipment, healthcare devices, and related clinical requirements.',
      items: ['Diagnostic Systems', 'Surgical Instruments', 'Clinical Disposables'],
      compliance: 'ISO/CE certified'
    },
    'it': {
      title: 'GCC & IT Infrastructure',
      category: 'Procurement Sector 02',
      description: 'Comprehensive computing, server hardware, cloud workstations, high-speed networking, and enterprise infrastructure tailored for Global Capability Centers and corporate enterprises.',
      items: [
        'Enterprise Servers & Data Center Racks',
        'High-Performance Workstations & Smart Laptops',
        'Managed Switches, Routers & Structured Cabling',
        'Modular UPS Power & Secure Server Cabinets',
        'GCC Command Center Systems & Displays',
        'Multi-facility Enterprise IT Hardware Deployment'
      ],
      compliance: 'OEM-backed warranty support, bulk configuration, and turn-key deployment.'
    },
    'it-infrastructure': {
      title: 'GCC & IT Infrastructure',
      category: 'Procurement Sector 02',
      description: 'Supply of enterprise servers and IT infrastructure.',
      items: ['Enterprise Servers', 'Networking Hardware', 'Cloud Workstations'],
      compliance: 'OEM-backed warranty'
    },
    'govt-education': {
      title: 'Government & Education Projects',
      category: 'Procurement Sector 03',
      description: 'Institutional procurement, school transformation programs, interactive digital classroom setups, and turnkey equipment deployments for state government initiatives.',
      items: [
        'Interactive Smart Boards & Digital Classroom Panels',
        'Computer Labs & Educational Hardware Systems',
        'Institutional Furniture & STEM Lab Equipment',
        'Public Infrastructure Project Hardware',
        'School Transformation & Turnkey Sourcing',
        'State-Wide Bulk Logistics Coordination'
      ],
      compliance: 'Government tender specifications compliance, rigorous pre-dispatch testing, and on-site commissioning.'
    },
    'industrial': {
      title: 'Industrial & Manufacturing Supplies',
      category: 'Procurement Sector 04',
      description: 'Certified structural TMT steel, heavy plates, industrial fabrication sections, raw materials, and commercial-grade textile yarn for production and manufacturing plants.',
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
    'steel-yarn': {
      title: 'Industrial & Manufacturing Supplies',
      category: 'Procurement Sector 04',
      description: 'Structural steel and industrial supplies.',
      items: ['TMT Steel', 'Industrial Sections', 'Commercial Yarn'],
      compliance: 'MTR certified'
    },
    'auto': {
      title: 'Automobile & Transportation Supplies',
      category: 'Procurement Sector 05',
      description: 'Sourcing and procurement of commercial transport vehicle spares, heavy bus assemblies, braking components, suspension units, and certified maintenance hardware for public transport workshops.',
      items: [
        'Commercial Bus Chassis & Suspension Components',
        'Heavy-Duty Braking Drums, Liners & Air Brake Valves',
        'Engine Overhaul Components, Gaskets & Bearings',
        'Transmission Gears, Clutch Assemblies & Propeller Shafts',
        'Electrical Starters, Alternators & Fleet Lighting Systems',
        'OEM & Grade-A Aftermarket Maintenance Spares'
      ],
      compliance: 'High endurance benchmarks, precision dimensional matching for commercial fleet durability.'
    },
    'automobile-parts': {
      title: 'Automobile & Transportation Supplies',
      category: 'Procurement Sector 05',
      description: 'Fleet vehicle spares and transit components.',
      items: ['Chassis Components', 'Braking Systems', 'Engine Parts'],
      compliance: 'Fleet endurance certified'
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

  // 7. Service Card Enquire Action Handler
  document.querySelectorAll('.btn-pro-enquire').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const card = btn.closest('.service-pro-card');
      const serviceTitle = card?.querySelector('.service-pro-title')?.textContent?.trim() || 'Procurement Service';
      // Smooth scroll to contact and focus inquiry
      const contactSection = document.getElementById('contact');
      if (contactSection) {
        contactSection.scrollIntoView({ behavior: 'smooth' });
      }
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


  // 8. Procurement Quote Form Interactive Submission
  const quoteForm = document.getElementById('procurementQuoteForm');
  const quoteAlert = document.getElementById('quoteFormAlert');
  if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!quoteForm.checkValidity()) {
        e.stopPropagation();
        quoteForm.classList.add('was-validated');
        return;
      }
      const submitBtn = document.getElementById('quoteSubmitBtn');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Submitting...</span>';
      }
      setTimeout(function () {
        if (quoteAlert) {
          quoteAlert.classList.remove('d-none');
        }
        quoteForm.reset();
        quoteForm.classList.remove('was-validated');
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>Submit Your Enquiry</span><i class="bi bi-chevron-right ms-2"></i>';
        }
      }, 700);
    });
  }
});
