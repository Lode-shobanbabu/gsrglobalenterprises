
const sections = Array.from(document.querySelectorAll('section'));
const data = sections.map(sec => {
    const s = window.getComputedStyle(sec);
    const id = sec.id;
    const header = sec.querySelector('.text-center, .section-header, .about-ref-content, .contact-info-panel, .commitment-content-wrap');
    
    let headerInfo = null;
    if (header) {
        const hs = window.getComputedStyle(header);
        const eyebrow = header.querySelector('[class*="eyebrow"]');
        const h2 = header.querySelector('h2, h1, .section-title, [class*="title"]');
        const p = header.querySelector('p, [class*="subtitle"], [class*="desc"]');
        
        const ebRect = eyebrow ? eyebrow.getBoundingClientRect() : null;
        const h2Rect = h2 ? h2.getBoundingClientRect() : null;
        const pRect = p ? p.getBoundingClientRect() : null;
        const headerRect = header.getBoundingClientRect();
        
        // Find next sibling or content after header
        const nextContent = header.nextElementSibling || sec.querySelector('.row, .grid, .clients-carousel-container, .contact-quote-card');
        const nextRect = nextContent ? nextContent.getBoundingClientRect() : null;
        
        headerInfo = {
            headerMarginBottom: hs.marginBottom,
            gapHeaderToContent: nextRect && pRect ? Math.round(nextRect.top - pRect.bottom) : null,
            gapHeaderTagToContent: nextRect ? Math.round(nextRect.top - headerRect.bottom) : null,
            eyebrowToTitle: ebRect && h2Rect ? Math.round(h2Rect.top - ebRect.bottom) : null,
            titleToSubtitle: h2Rect && pRect ? Math.round(pRect.top - h2Rect.bottom) : null,
        };
    }
    
    return {
        id: id,
        paddingTop: s.paddingTop,
        paddingBottom: s.paddingBottom,
        marginTop: s.marginTop,
        marginBottom: s.marginBottom,
        headerInfo: headerInfo
    };
});
console.log(JSON.stringify(data, null, 2));
