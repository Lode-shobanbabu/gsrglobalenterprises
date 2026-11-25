# GSR GLOBAL ENTERPRISES — Corporate Website

A premium, modern corporate web application for **GSR GLOBAL ENTERPRISES**, a multi-sector procurement, industrial supply, and infrastructure solutions enterprise based in Andhra Pradesh, India.

---

## 🏢 Company Profile & Regulatory Credentials

- **Enterprise Name:** GSR GLOBAL ENTERPRISES
- **GSTIN:** `37ABDFG9557A1ZC`
- **Official Phone:** [+91 7989635764](tel:+917989635764)
- **Official Email:** [gsrglobalenterprises@gmail.com](mailto:gsrglobalenterprises@gmail.com)
- **Registered Office:**  
  #1-1, Near ZPH School, Patha Duppada, Kanapaka, Vizianagaram – 535003, Andhra Pradesh, India.
- **Branch Office:**  
  #303, 3rd Floor, Sri Sampath Residency, Mithilapur Colony, Madhurawada, Visakhapatnam – 530041, Andhra Pradesh, India.

---

## 📦 Core Procurement Sectors

1. **Medical Equipment & Devices Procurement**
   - Diagnostic devices, clinical laboratory instruments, patient monitors, sterilization equipment, and healthcare consumables.
2. **Computers & IT Infrastructure**
   - High-performance workstations, laptops, interactive classroom smart boards, networking hardware, and power backups tailored for school transformation projects and educational development.
3. **Iron, Steel & Yarn Procurement**
   - Structural TMT steel bars (Fe 500/550), beams, angles, heavy plates, industrial pipes, and commercial cotton/synthetic yarn for industrial engineering and textile mills.
4. **Automobile & Bus Spare Parts Procurement**
   - Heavy-duty transit bus brake drums, liners, engine assemblies, transmission gears, suspension units, and fleet electrical spares.
5. **Solar Panel Procurement**
   - High-efficiency monocrystalline and bifacial solar PV modules, grid-tied/hybrid inverters, and galvanized mounting arrays for commercial, institutional, and green infrastructure installations.

---

## 🏛️ Institutional Client References

- **Central Prison, Visakhapatnam** (Government Institutional Facility Supply)
- **APSRTC Zonal Workshop, Vizianagaram** (Andhra Pradesh State Road Transport Corporation — Heavy Bus Spare Parts & Automobile Components)

---

## 🎨 Design System & Aesthetic Principles

- **Primary Colors:**
  - Deep Corporate Navy: `#060d18` / `#0b1a30` / `#0e223f`
  - Crisp Architectural White: `#ffffff`
  - Slate Backgrounds: `#f8fafc` / `#f1f5f9`
- **Accents:**
  - Sophisticated Warm Bronze / Gold: `#c59d5f` / `#b89047` / `#dfc27e`
- **Typography:**
  - Headings: `Outfit`, `Manrope` (Google Fonts)
  - Body Text: `Plus Jakarta Sans`, `Inter` (Google Fonts)
- **Visuals & Micro-interactions:**
  - Sticky glassmorphic navbar with transparent-to-solid transition on scroll.
  - IntersectionObserver subtle fade-up element reveal animations.
  - Active ScrollSpy navigation indicator.
  - Interactive service cards with deep-spec quick view modal and 1-click pre-filled enquiry.
  - Front-end validated contact form with real-time feedback and direct Email Client / WhatsApp dispatch links.

---

## 📂 Project Structure

```text
GSR GLOBAL ENTERPRISES/
├── index.html           # Semantic, SEO-optimized HTML5 corporate website
├── css/
│   └── style.css        # Custom CSS variables, responsive design, animations
├── js/
│   └── script.js        # Vanilla JS (scroll spy, validation, modals, back-to-top)
├── assets/
│   └── images/
│       └── logo.svg     # Clean geometric corporate monogram & typography logo
└── README.md            # Technical documentation & handover guide
```

---

## 🔄 How to Replace the Logo Later

When the permanent official logo image is ready:

1. Copy your logo file (e.g. `logo.png` or `logo.svg`) into `assets/images/logo.png`.
2. In `index.html`, locate the `.brand-crest` container in the `<nav>` and in the `<footer>`:
   ```html
   <!-- Replace the SVG inside .brand-crest or replace the container with: -->
   <a class="navbar-brand brand-container" href="#hero">
     <img src="assets/images/logo.png" alt="GSR GLOBAL ENTERPRISES" height="42">
   </a>
   ```

---

## 🚀 How to Run the Website Locally

You can open `index.html` directly in any web browser, or launch a lightweight local server:

### Using Python:
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000/` in your browser.

### Using VS Code / Cursor:
Right-click `index.html` and select **"Open with Live Server"**.
