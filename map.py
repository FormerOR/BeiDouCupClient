import tkinter as tk
from tkintermapview import TkinterMapView

# 创建Tkinter窗口
root = tk.Tk()
root.title("Map Example")

# 创建TkinterMapView组件
map_view = TkinterMapView(root)
map_view.pack(fill=tk.BOTH, expand=True)

# 设置坐标为赫尔辛基的中心
map_view.set_position(24.9384, 60.1699)

# 设置地址为赫尔辛基的中心
map_view.set_address("Kaivokatu 1, 00100 Helsinki, Finland")

# 启动Tkinter事件循环
root.mainloop()
