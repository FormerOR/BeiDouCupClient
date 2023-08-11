from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
import time
import random
from PyQt5.QtCore import QTimer

class UVSlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.uv_index = 0  # 初始UV指数为0

    def set_uv_index(self, uv_index):
        self.uv_index = uv_index
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        slot_width = self.width()
        slot_height = self.height()

        # 根据UV指数计算槽的颜色和内容大小
        color_value = min(self.uv_index / 10.0, 1.0)
        color = QColor(255, 255 * (1 - color_value), 255 * (1 - color_value))
        painter.setBrush(color)

        # 绘制矩形作为槽的背景
        painter.drawRect(0, 0, slot_width, slot_height)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    uv_slot_widget = UVSlotWidget()
    uv_slot_widget.resize(200, 50)
    uv_slot_widget.show()

    def update_uv_index():
        uv_index = random.randint(0, 10)  # 模拟UV指数的变化
        uv_slot_widget.set_uv_index(uv_index)

    # 每秒更新一次UV指数
    timer = QTimer()
    timer.timeout.connect(update_uv_index)
    timer.start(1000)

    sys.exit(app.exec_())
