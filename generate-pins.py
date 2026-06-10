"""
Pinterest Pin Generator for WM 2026 Guide
Generates multiple Pinterest pins using Pillow with Monumental Pitch design philosophy.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

PIN_W, PIN_H = 1000, 1500
OUTPUT_DIR = r"C:\Users\felix\OneDrive\Desktop\VS Code\wm2026-site\static\images\pins"
FONT_DIR = r"C:\Users\felix\.claude\skills\canvas-design\canvas-fonts"

# Color palette — Monumental Pitch
DARK_GREEN = (26, 86, 50)       # #1a5632
DEEP_GREEN = (10, 50, 30)       # deeper variant
GOLD = (200, 150, 12)           # #c8960c
GOLD_LIGHT = (230, 180, 40)     # lighter gold
WHITE = (255, 255, 255)
OFF_WHITE = (235, 240, 235)
DARK = (8, 20, 12)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_font(name, size):
    path = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(path, size)

def draw_circle(draw, cx, cy, r, fill=None, outline=None, width=1):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill, outline=outline, width=width)

def draw_hexagon(draw, cx, cy, r, fill=None, outline=None, width=1):
    points = []
    for i in range(6):
        angle = math.pi/6 + i * math.pi/3
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(points, fill=fill, outline=outline, width=width)

def create_pin(filename, headline_lines, sub_lines, bottom_text, url_text, variant="green"):
    """Create a Pinterest pin with Monumental Pitch design philosophy."""
    img = Image.new('RGB', (PIN_W, PIN_H), DEEP_GREEN)

    # Gradient background
    for y in range(PIN_H):
        ratio = y / PIN_H
        r = int(DEEP_GREEN[0] + (DARK_GREEN[0] - DEEP_GREEN[0]) * ratio * 0.6)
        g = int(DEEP_GREEN[1] + (DARK_GREEN[1] - DEEP_GREEN[1]) * ratio * 0.6)
        b = int(DEEP_GREEN[2] + (DARK_GREEN[2] - DEEP_GREEN[2]) * ratio * 0.6)
        draw = ImageDraw.Draw(img)
        draw.line([(0, y), (PIN_W, y)], fill=(r, g, b))

    draw = ImageDraw.Draw(img)

    # === GEOMETRIC ELEMENTS ===

    # Large faint circle (abstract ball/stadium reference)
    draw_circle(draw, 750, 380, 420, outline=(255, 255, 255, 15), width=1)
    draw_circle(draw, 750, 380, 350, outline=(255, 255, 255, 10), width=1)

    # Small accent circles — golden moments
    draw_circle(draw, 180, 320, 8, fill=GOLD)
    draw_circle(draw, 210, 350, 5, fill=GOLD_LIGHT)

    # Hexagonal pattern (football panel geometry) — bottom right
    for i, (hx, hy) in enumerate([(850, 1100), (920, 1180), (780, 1200), (900, 1280)]):
        r = 25 + i * 5
        draw_hexagon(draw, hx, hy, r, outline=(255, 255, 255, 8), width=1)

    # Diagonal pitch lines — abstract
    line_alpha = 12
    draw.line([(0, 800), (400, 1400)], fill=(255, 255, 255, line_alpha), width=1)
    draw.line([(600, 1500), (1000, 1200)], fill=(255, 255, 255, line_alpha), width=1)

    # Golden accent line
    draw.line([(80, 680), (920, 680)], fill=GOLD, width=2)
    draw.line([(80, 1320), (920, 1320)], fill=GOLD, width=1)

    # Small geometric dots in a grid (tactical formation reference)
    for row in range(5):
        for col in range(3):
            x, y = 820 + col * 35, 900 + row * 28
            draw_circle(draw, x, y, 2, fill=(255, 255, 255, 20 + row * 10))

    # === TYPOGRAPHY ===

    # Headline — monumental, stadium-facade scale
    try:
        headline_font = load_font("BigShoulders-Bold.ttf", 130)
    except:
        headline_font = load_font("Boldonse-Regular.ttf", 100)

    try:
        sub_font = load_font("WorkSans-Bold.ttf", 36)
        sub_font_regular = load_font("WorkSans-Regular.ttf", 30)
        url_font = load_font("WorkSans-Bold.ttf", 24)
    except:
        sub_font = load_font("InstrumentSans-Bold.ttf", 36)
        sub_font_regular = load_font("InstrumentSans-Regular.ttf", 30)
        url_font = load_font("InstrumentSans-Bold.ttf", 24)

    # Headline — centered, massive
    y_start = 720
    for line in headline_lines:
        bbox = draw.textbbox((0, 0), line, font=headline_font)
        tw = bbox[2] - bbox[0]
        x = (PIN_W - tw) // 2
        # Draw text with slight shadow for depth
        draw.text((x+3, y_start+3), line, fill=DARK, font=headline_font)
        draw.text((x, y_start), line, fill=WHITE, font=headline_font)
        y_start += 150

    # Subtitle lines
    y_start = 970
    for line in sub_lines:
        bbox = draw.textbbox((0, 0), line, font=sub_font)
        tw = bbox[2] - bbox[0]
        x = (PIN_W - tw) // 2
        draw.text((x, y_start), line, fill=GOLD_LIGHT, font=sub_font)
        y_start += 50

    # Bottom text
    bbox = draw.textbbox((0, 0), bottom_text, font=sub_font_regular)
    tw = bbox[2] - bbox[0]
    draw.text(((PIN_W - tw)//2, 1370), bottom_text, fill=WHITE, font=sub_font_regular)

    # URL
    bbox = draw.textbbox((0, 0), url_text, font=url_font)
    tw = bbox[2] - bbox[0]
    draw.text(((PIN_W - tw)//2, 1420), url_text, fill=GOLD, font=url_font)

    # Golden corner brackets
    draw.line([(60, 60), (160, 60)], fill=GOLD, width=3)
    draw.line([(60, 60), (60, 110)], fill=GOLD, width=3)
    draw.line([(PIN_W-60, 60), (PIN_W-160, 60)], fill=GOLD, width=3)
    draw.line([(PIN_W-60, 60), (PIN_W-60, 110)], fill=GOLD, width=3)
    draw.line([(60, PIN_H-60), (160, PIN_H-60)], fill=GOLD, width=3)
    draw.line([(60, PIN_H-60), (60, PIN_H-110)], fill=GOLD, width=3)

    path = os.path.join(OUTPUT_DIR, filename)
    img.save(path, 'PNG', dpi=(300, 300))
    print(f"[OK] Created: {filename}")
    return path

# =============================================
# GENERATE ALL 6 PINS
# =============================================

pins = [
    {
        "filename": "pin-01-spielplan.png",
        "headline": ["WM 2026", "SPIELPLAN"],
        "sub": ["Alle 104 Spiele + K.o.-Runde", "Gruppenphase bis Finale"],
        "bottom": "Kostenloser PDF-Download",
        "url": "WM2026-Guide.de"
    },
    {
        "filename": "pin-02-tickets.png",
        "headline": ["WM 2026", "TICKETS"],
        "sub": ["So kommst du günstig an Karten", "Preise · Phasen · Spartipps"],
        "bottom": "Jetzt Ticket-Guide lesen",
        "url": "WM2026-Guide.de"
    },
    {
        "filename": "pin-03-stadien.png",
        "headline": ["16 STADIEN", "3 LÄNDER"],
        "sub": ["Alle WM-Stadien von NY bis Mexiko", "Mit Hotel-Tipps & Anfahrtsinfos"],
        "bottom": "Stadion-Guide entdecken",
        "url": "WM2026-Guide.de"
    },
    {
        "filename": "pin-04-reise.png",
        "headline": ["WM 2026", "REISE-GUIDE"],
        "sub": ["Günstige Flüge, Hotels & Visum-Tipps", "Budget-Planung für deine WM-Reise"],
        "bottom": "Spare 500+ € mit unseren Tipps",
        "url": "WM2026-Guide.de"
    },
    {
        "filename": "pin-05-deutschland.png",
        "headline": ["DEUTSCHLAND", "WM 2026"],
        "sub": ["DFB-Team: Kader, Stars & Prognose", "Kann Nagelsmanns Team den Titel holen?"],
        "bottom": "Teams & Favoriten-Analyse",
        "url": "WM2026-Guide.de"
    },
    {
        "filename": "pin-06-countdown.png",
        "headline": ["WM 2026", "COUNTDOWN"],
        "sub": ["Nur noch 12 Monate bis zur WM!", "Jetzt vorbereiten & keine Infos verpassen"],
        "bottom": "Newsletter abonnieren + Spielplan sichern",
        "url": "WM2026-Guide.de"
    },
]

for pin in pins:
    create_pin(
        filename=pin["filename"],
        headline_lines=pin["headline"],
        sub_lines=pin["sub"],
        bottom_text=pin["bottom"],
        url_text=pin["url"]
    )

print(f"\n>>> {len(pins)} Pinterest-Pins generated in: {OUTPUT_DIR}")
