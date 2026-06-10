"""
Pinterest Pin Generator V2 — Monumental Pitch design philosophy.
Professional, high-contrast, museum-quality sports pins.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PIN_W, PIN_H = 1000, 1500
OUTPUT_DIR = r"C:\Users\felix\OneDrive\Desktop\VS Code\wm2026-site\static\images\pins"
FONT_DIR = r"C:\Users\felix\.claude\skills\canvas-design\canvas-fonts"

DEEP_GREEN = (8, 42, 28)
MID_GREEN = (20, 70, 42)
GOLD = (200, 150, 12)
GOLD_BRIGHT = (240, 185, 30)
WHITE = (255, 255, 255)
OFF_WHITE = (235, 242, 235)
DARK = (5, 15, 8)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

def create_master_pin(filename, headline, sub1, sub2, cta, url_text):
    """Professional Pinterest pin with layered visual depth."""

    # --- BASE LAYER: Rich gradient ---
    img = Image.new('RGB', (PIN_W, PIN_H))
    for y in range(PIN_H):
        t = y / PIN_H
        r = int(DEEP_GREEN[0] + (5 - DEEP_GREEN[0]) * t * 0.3)
        g = int(DEEP_GREEN[1] + (35 - DEEP_GREEN[1]) * t * 0.5)
        b = int(DEEP_GREEN[2] + (25 - DEEP_GREEN[2]) * t * 0.3)
        for x in range(PIN_W):
            img.putpixel((x, y), (r, g, b))

    draw = ImageDraw.Draw(img, 'RGBA')

    # --- RADIAL GLOW (stadium lights) ---
    glow_center = (500, 550)
    for radius in range(600, 50, -30):
        alpha = int(4 * (1 - radius/600))
        draw.ellipse(
            [glow_center[0]-radius, glow_center[1]-radius,
             glow_center[0]+radius, glow_center[1]+radius],
            fill=(255, 255, 220, alpha)
        )

    # --- GEOMETRIC ARCHITECTURE ---

    # Main circle — abstract ball, perfectly placed
    draw.ellipse([620, 180, 980, 600], outline=(255,255,255,18), width=2)
    draw.ellipse([660, 220, 940, 560], outline=(255,255,255,10), width=1)
    # Pentagon inside (classic football panel)
    cx, cy, r = 800, 390, 80
    pent_pts = [(cx+r*math.cos(2*math.pi*i/5-math.pi/2), cy+r*math.sin(2*math.pi*i/5-math.pi/2)) for i in range(5)]
    draw.polygon(pent_pts, outline=(255,255,255,20), width=1)

    # Small golden accent circles
    for px, py, pr in [(150, 250, 6), (170, 280, 3), (130, 300, 4)]:
        draw.ellipse([px-pr, py-pr, px+pr, py+pr], fill=GOLD_BRIGHT+(180,))

    # Hexagonal grid — bottom, abstracted football geometry
    for row in range(6):
        for col in range(4):
            x = 780 + col * 42 + (row % 2) * 21
            y = 950 + row * 36
            pts = [(x+15*math.cos(2*math.pi*i/6), y+15*math.sin(2*math.pi*i/6)) for i in range(6)]
            draw.polygon(pts, outline=(255,255,255, 6 + row*2), width=1)

    # Diagonal pitch line
    for offset in range(0, 800, 40):
        draw.line([(100+offset, 900), (200+offset, 1480)], fill=(255,255,255,6), width=1)

    # --- GOLDEN RULE OF THIRDS LINES ---
    draw.line([(80, 650), (920, 650)], fill=GOLD+(100,), width=1)
    draw.line([(80, 1320), (920, 1320)], fill=GOLD+(80,), width=1)

    # --- CORNER BRACKETS (museum framing) ---
    bracket_color = GOLD_BRIGHT+(200,)
    bw, bh = 3, 60
    for corner, dx, dy in [((60,60), 1, 1), ((PIN_W-60,60), -1, 1), ((60,PIN_H-60), 1, -1)]:
        cx, cy = corner
        draw.line([(cx, cy), (cx+dx*bh, cy)], fill=bracket_color, width=bw)
        draw.line([(cx, cy), (cx, cy+dy*bh)], fill=bracket_color, width=bw)

    # --- TYPOGRAPHY ---
    headline_font = load_font("BigShoulders-Bold.ttf", 135)
    sub_font = load_font("WorkSans-Bold.ttf", 34)
    sub2_font = load_font("WorkSans-Regular.ttf", 28)
    cta_font = load_font("WorkSans-Bold.ttf", 28)
    url_font = load_font("WorkSans-Bold.ttf", 22)

    # Headline — drop shadow then white
    lines = headline.split('\n')
    y_pos = 700
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=headline_font)
        tw = bbox[2] - bbox[0]
        x = (PIN_W - tw) // 2
        draw.text((x+4, y_pos+4), line, fill=DARK+(180,), font=headline_font)
        draw.text((x, y_pos), line, fill=WHITE, font=headline_font)
        y_pos += 155

    # Subtitle 1 — gold
    bbox = draw.textbbox((0,0), sub1, font=sub_font)
    draw.text(((PIN_W-bbox[2]+bbox[0])//2, 970), sub1, fill=GOLD_BRIGHT, font=sub_font)

    # Subtitle 2 — white
    bbox = draw.textbbox((0,0), sub2, font=sub2_font)
    draw.text(((PIN_W-bbox[2]+bbox[0])//2, 1020), sub2, fill=OFF_WHITE+(200,), font=sub2_font)

    # CTA
    bbox = draw.textbbox((0,0), cta, font=cta_font)
    draw.text(((PIN_W-bbox[2]+bbox[0])//2, 1370), cta, fill=WHITE, font=cta_font)

    # URL
    bbox = draw.textbbox((0,0), url_text, font=url_font)
    draw.text(((PIN_W-bbox[2]+bbox[0])//2, 1420), url_text, fill=GOLD_BRIGHT+(200,), font=url_font)

    # Save
    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path, 'PNG', dpi=(300,300))
    print(f"[OK] {filename} ({os.path.getsize(path)//1024} KB)")


# =============================================
# 6 HIGH-QUALITY PINS
# =============================================

pins = [
    ("pin-01-spielplan.png",
     "WM 2026\nSPIELPLAN",
     "Alle 104 Spiele + K.o.-Runde",
     "Gruppenphase · Sechzehntelfinale · Finale",
     "Kostenloser PDF-Download",
     "WM2026-Guide.de"),

    ("pin-02-tickets.png",
     "WM 2026\nTICKETS",
     "So kommst du gunstig an Karten",
     "Preise · Verkaufsphasen · Spartipps",
     "Jetzt Ticket-Guide lesen",
     "WM2026-Guide.de"),

    ("pin-03-stadien.png",
     "16 STADIEN\n3 LANDER",
     "Alle WM-Arenen von NYC bis Mexiko",
     "Kapazitaten · Hotel-Tipps · Anfahrtsinfos",
     "Stadion-Guide entdecken",
     "WM2026-Guide.de"),

    ("pin-04-reise.png",
     "WM 2026\nREISE-GUIDE",
     "Gunstig zu den Spielen reisen",
     "Fluge · Hotels · Visum · 10-Tage-Routen",
     "Spare 500+ Euro mit unseren Tipps",
     "WM2026-Guide.de"),

    ("pin-05-deutschland.png",
     "DEUTSCHLAND\nBEI DER WM",
     "DFB-Kader, Stars & Titel-Chancen",
     "Musiala, Wirtz, Havertz & Co. analysiert",
     "Teams & Favoriten-Analyse lesen",
     "WM2026-Guide.de"),

    ("pin-06-countdown.png",
     "WM 2026\nCOUNTDOWN",
     "Bereit fur die grosste WM aller Zeiten",
     "48 Teams · 104 Spiele · 3 Lander",
     "Newsletter abonnieren + Spielplan sichern",
     "WM2026-Guide.de"),
]

print("Generating Monumental Pitch pins...\n")
for args in pins:
    create_master_pin(*args)

print(f"\n>>> {len(pins)} professional pins ready.\n")
