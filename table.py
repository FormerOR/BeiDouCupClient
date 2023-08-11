import tkinter as tk
from tkinter import font

# 创建Tkinter窗口
root = tk.Tk()
root.title("Sensor Data")

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算表格所占窗口区域高度
table_height = int(screen_height * 0.8)

# 设置窗口尺寸为全屏
root.geometry(f"{screen_width}x{screen_height}")

# 创建容器框架
container = tk.Frame(root, bg="white")
container.pack(fill=tk.BOTH, expand=True)

# 创建表格容器
table_container = tk.Frame(container, height=table_height, width=screen_width, bg="light blue")
table_container.pack(fill=tk.BOTH, expand=True)

# 创建表格
table = tk.Text(table_container, height=table_height, width=screen_width, font=font.Font(size=14))
table.pack(fill=tk.BOTH, expand=True)

# 设置表格边框
table.configure(borderwidth=1, relief=tk.SOLID)

# 添加行分隔线
for i in range(1, int(table_height / 18)):
    table.insert(tk.END, "_" * screen_width + "\n")

# 初始数据
data = {
    "UV Sensor Data:": {
        "Vout:": 107,
        "UV:": 1
    },
    "Humidity and Temperature Sensor Data:": {
        "Humidity:": 31.10,
        "Temperature:": 29.90,
        "Heat Index Celsius:": 28.74,
        "Heat Index Fahrenheit:": 83.73
    },
    "Gas Sensor Data:": {
        "PPM:": 1.50
    },
    "Soil Sensor Data:": {
        "Moisture:": 1014,
        "State:": 1
    },
    "BMP Sensor Data:": {
        "Temperature:": 26.28,
        "Pressure:": 99947.13,
        "Altitude:": 115.36
    },
    "Rain Sensor Data:": {
        "Rain:": 231,
        "State:": 1
    },
    "Water Sensor Data:": {
        "Liquid Flow Rate:": 0.00,
        "Total Liquid Quantity:": 0.00
    },
    "Wind Sensor Data:": {
        "Wind Speed:": 0.00,
        "Real Speed:": 0.00,
        "Power:": 0.00,
        "Power Normalized:": 0.00
    },
    "GPS Sensor Data:": {
        "UTC Time:": "NONE",
        "Latitude:": "NONE",
        "N/S:": "NONE",
        "Longitude:": "NONE",
        "E/W:": "NONE"
    }
}


# 更新数据
def update_data():
    # 模拟更新数据
    data["UV Sensor Data:"]["Vout:"] = 108
    data["Gas Sensor Data:"]["PPM:"] = 1.60
    data["Wind Sensor Data:"]["Wind Speed:"] = 2.35
    data["GPS Sensor Data:"]["UTC Time:"] = "12:34:56"

    # 清空表格
    table.delete('1.0', tk.END)

    # 更新表格数据
    for category, values in data.items():
        table.insert(tk.END, category + "\n")
        for key, value in values.items():
            table.insert(tk.END, key + " " + str(value) + "\n")
        table.insert(tk.END, "\n")
    table.config(state=tk.DISABLED)


# 更新按钮
update_button = tk.Button(root, text="Update", command=update_data)
update_button.pack()

# 初始显示数据
update_data()

# 启动Tkinter事件循环
root.mainloop()
