with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = "--font-body: 'Inter', -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif;"
replacement = "--font-body: 'Inter', sans-serif;"

assert target in css, "target not found"
css = css.replace(target, replacement, 1)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Updated --font-body to pure 'Inter', sans-serif")

# Check brace count
open_b = css.count('{')
close_b = css.count('}')
print(f"CSS Braces: {open_b} open, {close_b} close (diff = {open_b - close_b})")
assert open_b == close_b
