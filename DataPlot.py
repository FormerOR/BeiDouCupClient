import sys
import random
import datetime
import time
import matplotlib.dates as mdates
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure

start_time = time.time()

class RealTimePlot(QWidget):
    def __init__(self, titleText, labelText, parent=None):
        super().__init__(parent)

        self.fig = Figure(figsize=(6, 4))  # 设置合适的大小
        self.fig.set_facecolor('#333333')
        self.canvas = FigureCanvas(self.fig)

        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(titleText, color='#E1E1E1')
        self.ax.set_xlabel('Time', color='#E1E1E1')
        self.ax.set_ylabel('Value', color='#E1E1E1')
        self.ax.set_facecolor('#1E1E1E')  # 设置背景颜色
        self.line_vout, = self.ax.plot([], [], label=labelText, color='#FFFF60')
        # self.line_uv, = self.ax.plot([], [], label='UV')
        self.ax.legend()

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.x_data = []
        self.vout_data = []
        # self.uv_data = []

    def update_plot(self, x, vout, uv):
        self.x_data.append(x)
        self.vout_data.append(vout)
        # self.uv_data.append(uv)

        self.line_vout.set_data(mdates.date2num(self.x_data), self.vout_data)
        # self.line_uv.set_data(mdates.date2num(self.x_data), self.uv_data)

        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
        # 在更新完图表后调用tight_layout
        # self.fig.tight_layout()

class MyWidget(QWidget):
    def __init__(self, titleText, labelText):
        super().__init__()

        self.frame = QFrame()
        self.frame.setMinimumHeight(250)

        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        self.setLayout(layout)

        self.real_time_plot = RealTimePlot(titleText, labelText, self.frame)

        self.timer = None

    def start_timer(self):
        if not self.timer:
            self.timer = FuncAnimation(self.real_time_plot.fig, self.update_plot, interval=1000)

    def update_plot(self, value):
        # Simulate UV Sensor Data update
        vout = float(value)
        uv = random.randint(0, 10)
        # 在某个时刻获取当前时间戳
        current_time = time.time()
        elapsed_time = current_time - start_time
        elapsed_time_int = round(elapsed_time)
        # current_time = datetime.datetime.now()

        self.real_time_plot.update_plot(elapsed_time_int, vout, uv)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.start_timer()
    widget.show()
    sys.exit(app.exec_())
