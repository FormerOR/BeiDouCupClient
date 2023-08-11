import folium

# 读取已有的地图 HTML 文件
map_file = "map2.html"
map = folium.Map(location=[32.11045911367427, 118.93391837094114], zoom_start=15)

# 在地图上绘制图形（以圆形为例）
center = [32.11245911367427, 118.92591837094114]
radius = 150  # 半径（单位：米）
folium.Circle(center, radius=radius, color='yellow', fill=False, fill_color='red').add_to(map)

# 保存修改后的地图 HTML 文件
map.save(map_file)
