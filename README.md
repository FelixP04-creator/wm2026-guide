# WM 2026 Guide — Hugo Static Site

> ⚽ Dein Guide zur FIFA WM 2026 in USA, Kanada & Mexiko.  
> Spielplan, Tickets, Stadien, Teams & Reisetipps — alles auf Deutsch.

## 🚀 Quick Start

```bash
# 1. Hugo installieren (falls nicht vorhanden)
# Windows: choco install hugo
# Mac: brew install hugo

# 2. Lokalen Server starten
cd wm2026-site
hugo server

# 3. Im Browser öffnen
# http://localhost:1313/wm2026/
```

## 📁 Projekt-Struktur

```
wm2026-site/
├── hugo.toml              # Konfiguration
├── assets/
│   ├── css/main.css       # Stylesheet (komplett selbst gebaut)
│   └── js/main.js         # JavaScript (minimal)
├── content/
│   ├── _index.md          # Startseite
│   ├── spielplan/         # Spielplan-Sektion
│   ├── stadien/           # Stadien-Sektion
│   ├── teams/             # Teams-Sektion
│   ├── tickets/           # Tickets & Reise
│   │   └── wm-2026-reise-guide.md
│   └── news/              # News-Blog
├── layouts/
│   ├── index.html         # Homepage-Template
│   ├── _default/
│   │   ├── baseof.html    # Basis-Layout
│   │   ├── single.html    # Einzelartikel
│   │   └── list.html      # Listenansicht
│   └── partials/          # Wiederverwendbare Komponenten
└── static/                # Statische Dateien (Bilder, PDFs)
```

## 🌍 Deployment (KOSTENLOS)

### Option 1: GitHub Pages

```bash
# GitHub Action für automatisches Deployment
# .github/workflows/hugo.yml wird automatisch ausgeführt
# Deine Seite ist dann unter: deinname.github.io/wm2026/
```

### Option 2: Cloudflare Pages (EMPFEHLUNG)

1. Gehe zu [pages.cloudflare.com](https://pages.cloudflare.com)
2. Verbinde dein GitHub-Repository
3. Framework: **Hugo**
4. Build command: `hugo`
5. Build directory: `public`
6. ✅ **SSL, CDN, unbegrenzt Traffic — gratis!**

### Option 3: Netlify

1. Gehe zu [netlify.com](https://netlify.com)
2. "New site from Git" → GitHub wählen
3. Build command: `hugo`
4. Publish directory: `public`
5. ✅ Eigene Subdomain + Formulare + SSL gratis

## ✍️ Content erstellen

### Neuen Artikel erstellen

```bash
hugo new content/news/mein-artikel.md
```

### Artikel-Struktur

```markdown
---
title: "Mein Titel"
description: "SEO-Beschreibung (max 160 Zeichen)"
date: 2025-06-10
author: "WM2026 Guide"
keywords: ["keyword1", "keyword2"]
---

## Einleitung
...
```

### Wichtige Shortcodes

```markdown
{{< now >}}        # Aktuelles Datum (für "Stand:"-Angaben)
```

## 🎨 Design

**Kein externes Theme.** Alles selbst gebaut mit:
- Modernes, cleanes Layout
- Mobile-First responsive
- WM-Farbpalette (Dunkelgrün, Gold, Akzent-Rot)
- Optimiert für SEO & Performance
- Kein JavaScript-Framework, minimales CSS

## 📈 Monetarisierung

Die Seite ist vorbereitet für:
- **Google AdSense** → einfach in `baseof.html` einfügen
- **Affiliate-Links** → transparent gekennzeichnet (⚠️)
- **Newsletter** → Mailchimp-Formular bereits integriert
- **Gumroad** → Links zu digitalen Produkten

## ⚙️ Vor dem Live-Gang

- [ ] `YOUR_AID` in Affiliate-Links durch echte IDs ersetzen
- [ ] `baseURL` in `hugo.toml` anpassen
- [ ] Impressum mit echten Kontaktdaten ausfüllen
- [ ] Datenschutzerklärung prüfen
- [ ] Mailchimp-Formular-URL in `newsletter-form.html` eintragen
- [ ] Google Analytics ID eintragen
- [ ] Google Search Console einrichten
