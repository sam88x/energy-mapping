import folium
from folium.plugins import HeatMap
import pandas as pd

def generate_heat_map(df, heat_value, plant_name, type_of_tech, output_file="energy_heatmap.html"):
    """
    Expects 'data' to be a list of dicts or a DataFrame with keys:
    ['latitude', 'longitude', 'nameplate_capacity_mw']
    """

    df = df.dropna()

    start_coords = [df['latitude'].mean(), df['longitude'].mean()]
    m = folium.Map(location=start_coords, zoom_start=6, tiles="CartoDB dark_matter")


    heat_data = df[['latitude', 'longitude', heat_value]].values.tolist()

    HeatMap(
        heat_data,
        radius=15,       # Adjusts how "spread out" each point is
        blur=10,         # Adjusts how smooth the heat looks
        max_zoom=1,      # Adjusts intensity scaling
        gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'} # Custom colors for the legend
    ).add_to(m)

    # --- PART B: The Hover Layer (Information) ---
    # We add transparent circles on top of the heat spots.
    # When you hover over them, you see the specific info.
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,                  # Size of the clickable area
            color=None,                # No border
            fill=True,
            fill_opacity=0.0,          # 0.0 = Invisible (just for hovering)
                                       # Change to 0.5 if you want to see the dots too
            tooltip=f"""
                <b>{row[plant_name]}</b><br>
                Capacity: {row[heat_value]} MW<br>
                Tech: {row[type_of_tech]}
            """
        ).add_to(m)


    legend_html = '''
     <div style="
     position: fixed; 
     bottom: 50px; left: 50px; width: 150px; height: 90px; 
     background-color: white; border:2px solid grey; z-index:9999; font-size:14px;
     padding: 10px; opacity: 0.8;">
     <b>Capacity Density</b><br>
     <i style="background:red; width:10px; height:10px; display:inline-block;"></i> High<br>
     <i style="background:lime; width:10px; height:10px; display:inline-block;"></i> Medium<br>
     <i style="background:blue; width:10px; height:10px; display:inline-block;"></i> Low
     </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))

    m.save(output_file)
    print(f"Map saved to {output_file}")