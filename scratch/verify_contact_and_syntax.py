import re
from playwright.sync_api import sync_playwright

def check_syntax():
    with open('css/style.css', 'r', encoding='utf-8') as f:
        css = f.read()
    open_b = css.count('{')
    close_b = css.count('}')
    print(f"CSS Braces: open={open_b}, close={close_b}, diff={open_b - close_b}")
    assert open_b == close_b, "Mismatched braces in css/style.css"

def verify_and_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        
        # Load local index.html
        import os
        url = 'file:///' + os.path.abspath('index.html').replace('\\', '/')
        page.goto(url, wait_until='networkidle')
        
        # Check contact section elements
        contact_sec = page.locator('#contact')
        assert contact_sec.count() > 0, "Contact section not found!"
        
        # Measure padding
        box = contact_sec.bounding_box()
        comp_style = page.evaluate("""() => {
            const el = document.getElementById('contact');
            const style = window.getComputedStyle(el);
            const items = document.querySelectorAll('.contact-info-item');
            const itemStyles = Array.from(items).map(item => {
                const s = window.getComputedStyle(item);
                return {
                    border: s.border,
                    boxShadow: s.boxShadow,
                    background: s.backgroundColor
                };
            });
            const card = document.querySelector('.contact-quote-card');
            const cardStyle = window.getComputedStyle(card);
            
            return {
                sectionPaddingTop: style.paddingTop,
                sectionPaddingBottom: style.paddingBottom,
                itemStyles: itemStyles,
                cardBorderTop: cardStyle.borderTop,
                cardBorderRadius: cardStyle.borderRadius,
                cardBoxShadow: cardStyle.boxShadow
            };
        }""")
        
        print("Computed Style Results:")
        print(f"  Section padding-top: {comp_style['sectionPaddingTop']}")
        print(f"  Section padding-bottom: {comp_style['sectionPaddingBottom']}")
        print(f"  Contact items count: {len(comp_style['itemStyles'])}")
        for idx, item in enumerate(comp_style['itemStyles']):
            print(f"    Item {idx+1}: border={item['border']}, boxShadow={item['boxShadow']}, bg={item['background']}")
        print(f"  Quote Card borderTop: {comp_style['cardBorderTop']}")
        print(f"  Quote Card borderRadius: {comp_style['cardBorderRadius']}")
        print(f"  Quote Card boxShadow: {comp_style['cardBoxShadow']}")
        
        # Scroll to contact and screenshot
        contact_sec.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        
        artifact_path = r'C:\Users\sunseaz\.gemini\antigravity\brain\a4cbe818-6d35-404c-8a2c-b373e74e0891\contact_section_preview.png'
        contact_sec.screenshot(path=artifact_path)
        print(f"Screenshot saved to {artifact_path}")
        
        browser.close()

if __name__ == '__main__':
    check_syntax()
    verify_and_screenshot()
