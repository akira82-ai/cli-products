---
name: jekyll_setup
description: Jekyll configuration and custom layout architecture
type: reference
---

# Jekyll Setup

**Configuration File:** `_config.yml`
- Uses kramdown markdown parser with rouge syntax highlighter
- Plugins: jekyll-seo-tag, jekyll-sitemap
- Excludes Python scripts, node_modules, and development files
- Pretty permalinks format

**Custom Layouts:**
1. **home.html** — Homepage with hero section, stats, search input, and category grid
2. **category.html** — Category listing with gradient header, tool table, and back navigation
3. **default.html** — Base layout with header, footer, and theme toggle

**Design System:**
- CSS custom properties for theming (primary: #6366f1, secondary: #8b5cf6, accent: #ec4899)
- Gradient backgrounds with radial overlays
- Dark mode support via `data-theme` attribute
- Inter font for UI, JetBrains Mono for code

**JavaScript (custom.js):**
- Theme toggle with localStorage persistence
- Smooth scrolling
- Code copy buttons
- Search input debouncing
- Intersection Observer for animations
- External link indicators
- Mobile menu
- Back-to-top button
- Table wrappers for responsiveness

**Key Design Decision:** Removed just-the-docs theme dependency (commit a4bc390) in favor of custom layouts for greater design control.
