# Lab 6: Custom Basemap Design & Interactive Hometown Map

## Overview
This lab combines custom cartographic design with interactive web mapping. It consists of three components:
1. **Custom Mapbox Basemap** - Art-inspired design created in Mapbox Studio
2. **Hometown Locations Dataset** - CSV file with meaningful locations
3. **Interactive Python Map** - Folium map with custom basemap and location markers

---

## Completion Checklist

### ✅ Part 1: Custom Mapbox Basemap Design
- [x] Create Mapbox Studio account (using TCU email)
- [x] Choose design inspiration (cultural artifact, film, art, etc.)
- [x] Create blank style in Mapbox Studio
- [x] Add and customize required components:
  - [x] Land, water, & sky
  - [x] Road network
  - [x] Place labels
  - [x] POI labels
  - [x] Terrain component
- [x] Minimum 12 styled layers
- [x] Style data across zoom levels (local, regional, world scales)
- [x] Publish and test style
- [x] **Style URL**: `mapbox://styles/gfranklin1401/cmm0sg7q6000s01s5204zgavt`

### ✅ Part 2: Hometown Locations Dataset
- [x] Select 10+ meaningful hometown locations
- [x] Create `hometown_locations.csv` with columns:
  - [x] Name
  - [x] Address (for geocoding)
  - [x] Type (category)
  - [x] Description (personal, 2-3 sentences)
  - [x] Image_URL
- [x] Include at least 3 different location types
- [x] No private/sensitive addresses

### ✅ Part 3: Python Interactive Map
- [x] Install required libraries: `folium`, `pandas`, `requests`
- [x] Read CSV file
- [x] Geocode addresses using Mapbox Geocoding API v6
- [x] Create Folium map with custom Mapbox basemap
- [x] Add color-coded markers by location type
- [x] Create interactive pop-ups with:
  - [x] Location name
  - [x] Personal description
  - [x] Location image
- [x] Save as HTML file (`hometown_map.html`)
- [x] Test with multiple locations
- [x] Verify custom basemap loads correctly

### ⏳ Part 4: Written Reflection (250-500 words)
- [ ] **Design Inspiration**: Explain what inspired basemap design with reference images
- [ ] **Cartographic Challenges**: Discuss multi-scale design decisions
- [ ] **Technical Challenges**: Describe coding obstacles and AI tool usage
- [ ] **Self-Assessment**: Reflect on design coherence, scale awareness, data quality, code understanding, integration, portfolio quality

---

## Getting Started with the Python Script

### Prerequisites
Install required packages:
```bash
pip install folium pandas requests
```

### Configuration
Set your Mapbox credentials as environment variables:
```bash
export MAPBOX_PUBLIC_TOKEN="your_public_token_here"
export MAPBOX_USERNAME="your_username"
export MAPBOX_STYLE_ID="your_style_id"
```

### Running the Script
```bash
cd /Users/grantfranklin/Documents/dcda-portfolio
python hometown_map.py
```

This will generate `hometown_map.html` - your interactive map!

---

## Files Included

| File | Purpose |
|------|---------|
| `hometown_locations.csv` | Dataset of hometown locations with addresses, types, descriptions, and images |
| `hometown_map.py` | Python script that geocodes addresses and creates interactive map |
| `hometown_map.html` | Generated interactive map (created when you run the script) |
| `SETUP.md` | Detailed setup instructions |
| `Lab6_Reflection.pdf` | Your written reflection (to create) |

---

## Key Features of Your Implementation

### Geocoding
- Uses Mapbox Geocoding API v6 to convert addresses to coordinates
- Handles errors gracefully with fallbacks
- Rate limiting (0.2s delay between requests)

### Custom Basemap
- Loads your custom Mapbox Studio design via tile URL
- Tile URL format: `https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/256/{z}/{x}/{y}@2x?access_token={token}`

### Interactive Markers
- Color-coded by location Type (Restaurant→red, Park→green, etc.)
- Clickable popups showing:
  - Location name
  - Personal description
  - Location image
- Hover tooltips with location name

### Map Centering
- Automatically centers map on mean coordinates of all locations
- Zoom level set to 12 for regional view

---

## Testing Checklist

Before finalizing, test:
- [ ] Script runs without errors
- [ ] All locations are geocoded correctly
- [ ] Map centers on your hometown region
- [ ] Custom Mapbox basemap is visible (not default map)
- [ ] Markers appear with correct colors
- [ ] Popups display with images and descriptions
- [ ] Map is interactive (zoom, pan work)
- [ ] HTML file is generated successfully

---

## Portfolio Integration

### Add to Your Portfolio Website

1. **Copy the HTML file** to your portfolio Lab 6 section
2. **Embed the interactive map** in your portfolio page
3. **Add your written reflection** to the same page
4. **Push to GitHub** and verify it displays correctly

### GitHub Pages

Ensure your repository structure includes:
```
portfolio/
├── lab6/
│   ├── hometown_map.html
│   └── Lab6_Reflection.md (or PDF)
└── index.html
```

View your live map at: `https://grant-franklin.github.io/dcda-portfolio/lab6/hometown_map.html`

---

## Resources

- **Mapbox Studio**: https://studio.mapbox.com
- **Mapbox Geocoding API**: https://docs.mapbox.com/api/search/geocoding/
- **Folium Documentation**: https://python-visualization.github.io/folium/
- **Google Fonts**: https://fonts.google.com/
- **Mapbox Gallery**: https://www.mapbox.com/gallery/

---

## Next Steps

1. **Complete your written reflection** (250-500 words)
2. **Generate your interactive map**:
   ```bash
   python hometown_map.py
   ```
3. **Test the map** in a web browser
4. **Add to portfolio** and push to GitHub
5. **Submit to D2L**:
   - Mapbox style URL (in .txt or reflection document)
   - `hometown_locations.csv`
   - `hometown_map.py`
   - `hometown_map.html`
   - Written reflection (PDF)
   - GitHub repository URL
   - Live GitHub Pages URL

---

## Support

For issues or questions:
- Check the Mapbox documentation
- Review the Folium examples
- Consult the setup guides in this folder
- Use AI tools to help debug code

Good luck! 🗺️✨
