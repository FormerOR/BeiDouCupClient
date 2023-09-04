import time
import random
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from gauge import Gauge

# 创建一个Matplotlib子图
fig, ax = plt.subplots(figsize=(6, 6))

# 创建一个仪表盘对象
gauge = Gauge(ax, unit='UV Index', min_value=0, max_value=10, colors='Spectral')

# 设置仪表盘的刻度和标签
gauge.set_scale(0, 2, 4, 6, 8, 10)
gauge.set_label('UV Index')

# 显示仪表盘
plt.show(block=False)

# 模拟实时更新仪表盘数据
while True:
    uv_index = random.uniform(0, 10)  # 模拟获取UV指数数据
    gauge.set_value(uv_index)
    fig.canvas.draw()
    time.sleep(1)
    plt.pause(0.01)
