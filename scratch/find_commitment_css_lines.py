with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'F. OUR COMMITMENT' in line or 'commitment-mockup-section' in line:
        print(f"Starts around line {i+1}")
        for j in range(i, min(len(lines), i + 80)):
            if 'G. Contact' in lines[j] or 'contact-quote-section' in lines[j]:
                print(f"Ends around line {j+1}")
                break
        break
