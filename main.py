import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 创建Tkinter窗口
root = tk.Tk()
root.title("数据可视化")

# 创建一个画布，用于绘制图表
figure = plt.figure()
line, = plt.plot([], [], 'b-')


# 数据更新函数
def update_data(i):
    # 模拟获取数据
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 6, 3]

    # 更新折线图数据
    return x, y  # 返回两个数组


# 动画更新函数
def update_animation(i):
    line.set_data(update_data(i))
    return line,  # 注意这里的逗号，将line包装为元组


# 创建动画对象
ani = animation.FuncAnimation(figure, update_animation, frames=range(10), interval=1000, blit=True)

# 显示Tkinter窗口
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# 启动Tkinter事件循环
root.mainloop()
