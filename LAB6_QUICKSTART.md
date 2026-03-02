# Lab 6 - Quick Start Guide

## 🎯 Your Lab Status

### ✅ COMPLETED
- Custom Mapbox basemap created and published
- Hometown locations CSV with 6 locations (you may want to add more)
- Python script ready to generate the interactive map
- All required libraries configured

### ⏳ TODO (In Order)

---

## Step 1: Set Your Mapbox Credentials (2 minutes)

Run these commands in your terminal to set environment variables:

```bash
export MAPBOX_PUBLIC_TOKEN="your_token_here"
export MAPBOX_USERNAME="gfranklin1401"
export MAPBOX_STYLE_ID="cmm0sg7q6000s01s5204zgavt"
```

**Get your token:**
1. Go to https://account.mapbox.com/access-tokens/
2. Copy your "Default public token" (starts with `pk.`)
3. Replace `your_token_here` above

---

## Step 2: Generate Your Interactive Map (5 minutes)

```bash
cd /Users/grantfranklin/Documents/dcda-portfolio
python hometown_map.py
```

**Output:** `hometown_map.html` will be created in the same folder

**Verify it worked:**
- Look for "Map saved as hometown_map.html" message
- Open the HTML file in your browser
- You should see:
  - Your custom Mapbox basemap
  - Colored markers for each location
  - Clickable popups with images

---

## Step 3: Write Your Reflection (30-45 minutes)

1. Open `LAB6_REFLECTION_TEMPLATE.md`
2. Answer each section:
   - Design Inspiration (explain your Mapbox design)
   - Cartographic Challenges (multi-scale decisions)
   - Technical Challenges (geocoding, markers, popups)
   - Self-Assessment (honest reflection on quality)
3. Aim for 250-500 total words
4. Save as `LAB6_REFLECTION.pdf` when done

---

## Step 4: Add to Your Portfolio (15 minutes)

### Create Lab 6 Page
1. In your portfolio, create or update `lab6/index.html`
2. Embed your interactive map:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lab 6: Interactive Hometown Map</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .map-container { width: 100%; height: 600px; margin: 20px 0; }
        iframe { width: 100%; height: 100%; border: none; }
    </style>
</head>
<body>
    <h1>Lab 6: Custom Basemap & Interactive Hometown Map</h1>
    
    <h2>Interactive Map</h2>
    <div class="map-container">
        <iframe src="hometown_map.html"></iframe>
    </div>
    
    <h2>Reflection</h2>
    <p>[Include your reflection text here or link to PDF]</p>
    
</body>
</html>
```

### Copy Files to Portfolio
```bash
cp hometown_map.html ~/Documents/portfolio/lab6/
cp LAB6_REFLECTION.pdf ~/Documents/portfolio/lab6/
```

---

## Step 5: Push to GitHub (5 minutes)

```bash
cd ~/Documents/portfolio
git add lab6/
git commit -m "feat: add Lab 6 interactive hometown map and reflection"
git push origin main
```

---

## Step 6: Verify Everything Works (5 minutes)

1. **GitHub Repository**: https://github.com/grant-franklin/dcda-portfolio
2. **GitHub Pages**: https://grant-franklin.github.io/dcda-portfolio/lab6/
3. Open both URLs to verify map displays correctly

---

## 📋 Submission Checklist

Before submitting to D2L, verify you have:

- [ ] Environment variables set (`MAPBOX_PUBLIC_TOKEN`, etc.)
- [ ] `hometown_map.html` generated and tested
- [ ] `hometown_locations.csv` complete (10+ locations)
- [ ] `hometown_map.py` ready to run
- [ ] Written reflection (250-500 words, PDF)
- [ ] Lab 6 page added to portfolio website
- [ ] Changes pushed to GitHub
- [ ] GitHub Pages displaying correctly

### D2L Submission Items
1. Mapbox Style URL: `mapbox://styles/gfranklin1401/cmm0sg7q6000s01s5204zgavt`
2. CSV file: `hometown_locations.csv`
3. Python script: `hometown_map.py`
4. HTML map: `hometown_map.html`
5. Reflection: `LAB6_REFLECTION.pdf`
6. GitHub Repo: `https://github.com/grant-franklin/dcda-portfolio`
7. GitHub Pages: `https://grant-franklin.github.io/dcda-portfolio/lab6/`

---

## 🚨 Troubleshooting

### Map won't load / "No module named..."
```bash
pip install folium pandas requests
```

### Addresses not geocoding / Map appears blank
- Check your Mapbox token is set correctly
- Verify addresses are in proper format in CSV
- Check internet connection

### Custom basemap not showing (see default Leaflet)
- Verify Mapbox token is correct
- Check style URL and username are correct
- Ensure style is published in Mapbox Studio

### Popups show text but no images
- Verify Image_URL column has valid URLs
- Try viewing source of HTML file (Ctrl+U) to see image tags
- CORS restrictions may prevent some images from displaying

---

## ⏱️ Time Estimate

| Task | Time |
|------|------|
| Step 1: Set credentials | 2 min |
| Step 2: Generate map | 5 min |
| Step 3: Write reflection | 45 min |
| Step 4: Add to portfolio | 15 min |
| Step 5: Push to GitHub | 5 min |
| Step 6: Verify | 5 min |
| **TOTAL** | **77 minutes** |

---

## 💡 Tips for Success

1. **Test Early**: Run the script with just 2-3 locations first
2. **Check Addresses**: Verify your geocoding is working with Google Maps
3. **Customize Popups**: Edit `hometown_map.py` to adjust popup appearance
4. **Add More Locations**: The current CSV has 6 - consider adding 4+ more
5. **Personal Descriptions**: Make descriptions genuinely meaningful, not generic
6. **Reflection Writing**: Be honest - employers/programs value authentic self-assessment

---

Good luck! You've got this! 🗺️✨
