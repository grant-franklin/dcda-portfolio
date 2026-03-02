import time
import urllib.parse
import requests
import pandas as pd
import folium
import os

# ==============================
# MAPBOX CONFIGURATION (from environment variables)
# ==============================

ACCESS_TOKEN = os.getenv("MAPBOX_PUBLIC_TOKEN", "")
username = os.getenv("MAPBOX_USERNAME", "gfranklin1401")
style_id = os.getenv("MAPBOX_STYLE_ID", "cmm0sg7q6000s01s5204zgavt")

if not ACCESS_TOKEN:
    print("⚠️  ERROR: MAPBOX_PUBLIC_TOKEN environment variable not set")
    print("   Please set it: export MAPBOX_PUBLIC_TOKEN='your_token_here'")
    exit(1)

TILES_URL = f"https://api.mapbox.com/styles/v1/{username}/{style_id}/tiles/256/{{z}}/{{x}}/{{y}}@2x?access_token={ACCESS_TOKEN}"

# ==============================
# Marker Colors by Type
# ==============================

TYPE_TO_COLOR = {
    "Restaurant": "red",
    "Park": "green",
    "Cultural": "purple",
    "School": "blue",
    "Historical": "orange",
    "Recreation": "cadetblue",
    "Shopping": "darkblue",
}

# ==============================
# Geocoding Function
# ==============================

def geocode_address(address):
    encoded_address = urllib.parse.quote(address)
    url = f"https://api.mapbox.com/search/geocode/v6/forward?q={encoded_address}&access_token={ACCESS_TOKEN}&limit=1"
    
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    features = data.get("features", [])
    if not features:
        return None

    coordinates = features[0]["geometry"]["coordinates"]
    lon, lat = coordinates
    return lat, lon

# ==============================
# Popup HTML Builder
# ==============================

def create_popup(name, description, image_url):
    return f"""
    <div style="width:280px;">
        <h4>{name}</h4>
        <p>{description}</p>
        <img src="{image_url}" style="width:100%; border-radius:8px;">
    </div>
    """

# ==============================
# Main Program
# ==============================

def main():
    df = pd.read_csv("hometown_locations.csv")

    latitudes = []
    longitudes = []

    for _, row in df.iterrows():
        result = geocode_address(row["Address"])
        if result:
            lat, lon = result
        else:
            lat, lon = None, None

        latitudes.append(lat)
        longitudes.append(lon)

        time.sleep(0.2)

    df["Latitude"] = latitudes
    df["Longitude"] = longitudes

    df = df.dropna(subset=["Latitude", "Longitude"])

    center_lat = df["Latitude"].mean()
    center_lon = df["Longitude"].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles=None)

    folium.TileLayer(
        tiles=TILES_URL,
        attr="Mapbox",
        name="Custom Basemap"
    ).add_to(m)

    for _, row in df.iterrows():
        color = TYPE_TO_COLOR.get(row["Type"], "gray")

        popup_html = create_popup(
            row["Name"],
            row["Description"],
            row["Image_URL"]
        )

        popup = folium.Popup(popup_html, max_width=300)

        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=popup,
            tooltip=row["Name"],
            icon=folium.Icon(color=color, icon="info-sign")
        ).add_to(m)

    m.save("hometown_map.html")
    print("Map saved as hometown_map.html")

if __name__ == "__main__":
    main()