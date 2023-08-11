import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QVBoxLayout

# 创建一个应用对象
app = QApplication(sys.argv)

# 创建一个窗口小部件
window = QWidget()

# 创建两个水平布局对象
hbox1 = QHBoxLayout()
hbox2 = QHBoxLayout()

# 创建一个垂直布局对象
vbox = QVBoxLayout()

# 创建三个frame小部件，并设置不同的背景颜色
frame1 = QFrame()
frame1.setStyleSheet("background-color: red")
frame2 = QFrame()
frame2.setStyleSheet("background-color: green")
frame3 = QFrame()
frame3.setStyleSheet("background-color: blue")

# 将frame1和frame2添加到第一个水平布局中，并设置比例为1:2
hbox1.addWidget(frame1, 1)
hbox1.addWidget(frame2, 1)

# 将frame3添加到第二个水平布局中，并设置比例为1
hbox2.addWidget(frame3, 1)

# 将两个水平布局添加到垂直布局中，并设置比例为1:3
vbox.addLayout(hbox1, 1)
vbox.addLayout(hbox2, 1)

# 将垂直布局设置为窗口小部件的布局
window.setLayout(vbox)

# 显示窗口小部件
window.show()

# 运行应用程序
sys.exit(app.exec_())
