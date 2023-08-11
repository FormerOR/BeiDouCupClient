import datetime
import os
import random
import sys
import threading
import time

import folium
import geocoder
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, Qt, QThread
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QWidget, QFrame, \
    QVBoxLayout, QTableWidget, QTableWidgetItem, QDesktopWidget, QTextEdit, QStyleFactory, QPushButton
from qt_material import apply_stylesheet
from pyecharts import options as opts
from pyecharts.charts import Gauge
from pyecharts.commons.utils import JsCode

import BD_server
import DataPlot

# 设置起始序号和间隔时间
start_index = 1
interval = 1

# 创建一个folium地图对象
m = folium.Map(location=[32.11358911367427, 118.92591837094114], zoom_start=16)

# 保存为HTML文件
m.save("map1.html")

'''
QWebEngineView 使用Web浏览器控件显示本地HTML网页 的案例
'''


def set_data(table, data):
    table.clearContents()
    table.setRowCount(len(data) * 4)  # 调整行数为类别数的两倍

    row = 0
    for category, values in data.items():
        category_item = QTableWidgetItem(category)
        category_item.setFlags(QtCore.Qt.ItemIsEnabled)  # 设置类别行为只读
        table.setItem(row, 0, category_item)
        row += 1

        for key, value in values.items():
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(value)

            if category == 'GPS Sensor Data':  # 设置GPS Sensor Data下的单元格可编辑
                value_item.setFlags(Qt.ItemIsEditable)

            table.setItem(row, 0, key_item)
            table.setItem(row, 1, value_item)
            row += 1


gauge = None


def create_gauge(uv_index) -> Gauge:
    c = (
        Gauge()
        .add("", [("UV Index", uv_index)], title_label_opts=opts.LabelOpts(formatter="{value}"))
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}"),
        )
    )
    return c


class WebEngineViewDemo(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置定位和左上角坐标
        self.setGeometry(300, 300, 1600, 1200)
        # 设置窗口标题
        self.setWindowTitle('装载本地HTML页面并展示 的演示')
        # 设置窗口图标
        # self.setWindowIcon(QIcon('../web.ico'))

        self.browser = QWebEngineView()
        url = os.getcwd() + '/map2.html'
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)


class WebEngineViewDemo2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        self.file_path = "/gauge.html"
        self.setLayout(layout)
        self.load_html_file("/gauge.html")  # Load your HTML file

    def load_html_file(self, file_path):
        self.web_view.load(QtCore.QUrl.fromLocalFile(self.file_path))


def startDriver():
    global driver
    driver = BD_server.start_web()


logState = False


def startLog():
    global logState
    logState = True


def stopLog():
    global logState
    logState = False


def clearLog():
    logText.clear()


ori_data = {
    'UV Sensor Data': {'Vout': '107', 'UV': '1'},
    'Humidity and Temperature Sensor Data': {'Humidity': '31.10', 'Temperature': '29.90', 'Heat Index Celsius': '28.74',
                                             'Heat Index Fahrenheit': '83.73'},
    'Gas Sensor Data': {'PPM': '1.50'},
    'Soil Sensor Data': {'Moisture': '1014', 'State': '1'},
    'BMP Sensor Data': {'Temperature': '26.28', 'Pressure': '99947.13', 'Altitude': '115.36'},
    'Rain Sensor Data': {'Rain': '231', 'State': '1'},
    'Water Sensor Data': {'Liquid Flow Rate': '0.00', 'Total Liquid Quantity': '0.00'},
    'Wind Sensor Data': {'Wind Speed': '0.00', 'Real Speed': '0.00', 'Power': '0.00', 'Power Normalized': '0.00'},
    'GPS Sensor Data': {'UTC Time': 'NONE', 'Latitude': 'NONE', 'N/S': 'NONE', 'Longitude': 'NONE', 'E/W': 'NONE'}
}

dir_data = ori_data

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # 设置应用图标
    app.setWindowIcon(QIcon('../web.ico'))
    # 创建一个窗口小部件
    window = QWidget()
    # 创建一个框架小部件，并设置边框样式
    frame = QFrame()
    frame.setFrameStyle(QFrame.Box | QFrame.Raised)

    '''表格设置'''
    table = QTableWidget()
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Key", "Value"])
    # 设置表格文字大小
    font = QFont()
    font.setPointSize(18)  # 设置字号为12
    table.setFont(font)  # 设置表格的字体
    # table.setMinimumSize(600, 1600)
    table.setColumnWidth(0, 600)
    table.setColumnWidth(1, 400)
    # 初始化表格信息
    set_data(table, ori_data)

    '''日志消息框设置'''
    logText = QTextEdit()
    logText.setReadOnly(True)  # 设置为只读，用于显示提示信息
    logText.setMinimumHeight(300)  # 设置日志窗口的最小高度
    logText.setStyleSheet('font-size: 18px;')

    '''日志框按钮区'''
    button_style = "font-size: 24px;"
    startLogButton = QPushButton("开始读取日志")
    startLogButton.setStyleSheet(button_style)
    startLogButton.clicked.connect(startLog)
    stopLogButton = QPushButton("停止读取日志")
    stopLogButton.setStyleSheet(button_style)
    stopLogButton.clicked.connect(stopLog)
    clearLogButton = QPushButton("清除历史日志")
    clearLogButton.setStyleSheet(button_style)
    clearLogButton.clicked.connect(clearLog)
    # 添加到一个垂直布局里
    logControlLayout = QVBoxLayout()
    logControlLayout.addWidget(startLogButton)
    logControlLayout.addWidget(stopLogButton)
    logControlLayout.addWidget(clearLogButton)

    '''网页视图的创建'''
    w = WebEngineViewDemo()
    w2 = WebEngineViewDemo2()

    '''子界面frame的创建'''
    frame1 = QFrame()
    frame1.setFrameStyle(QFrame.Box | QFrame.Raised)
    frame1.setMinimumHeight(400)
    # 子frame的创建
    frame1_layout1 = QHBoxLayout()
    frame1.setLayout(frame1_layout1)
    frame1_1 = QFrame()
    # frame1_1.setStyleSheet("border: 2px solid #1DE9B6;")
    frame1_2 = QFrame()
    # frame1_2.setStyleSheet("border: 2px solid #1DE9B6;")
    frame1_3 = QFrame()
    # frame1_3.setStyleSheet("border: 2px solid #1DE9B6;")
    frame1_layout1.addWidget(frame1_1, 1)
    frame1_layout1.addWidget(frame1_2, 1)
    frame1_layout1.addWidget(frame1_3, 1)

    # 添加可视化图表1
    frame1_1_layout1 = QVBoxLayout()
    plot1 = DataPlot.MyWidget()
    plot1.start_timer()
    frame1_1_layout1.addWidget(plot1)
    frame1_1.setLayout(frame1_1_layout1)
    # 添加可视化仪表盘
    frame1_2_layout1 = QVBoxLayout()
    frame1_2_layout1.addWidget(w2)
    frame1_2.setLayout(frame1_2_layout1)

    # 创建一个垂直布局，并将表格添加到布局中
    layout1 = QVBoxLayout()
    layout1.addWidget(table)
    # 将垂直布局设置为frame的布局
    frame.setLayout(layout1)

    # 创建一个日志消息区的布局
    logLayout = QHBoxLayout()
    logLayout.addWidget(logText, 3)
    logLayout.addLayout(logControlLayout, 1)

    # 创建一个垂直布局，将网页视图和日志消息区加入其中
    layout3 = QVBoxLayout()
    layout3.addWidget(w, 2)
    layout3.addLayout(logLayout, 1)

    # 创建一个水平布局，并将列表框架和layout3添加到其中
    layout = QHBoxLayout()
    layout.addWidget(frame, 1)
    layout.addLayout(layout3, 1)

    # 创建一个垂直布局将layout和frame加入其中
    layout2 = QVBoxLayout()
    layout2.addLayout(layout, 2)
    layout2.addWidget(frame1, 1)

    # 将布局设置为layout2的布局
    window.setLayout(layout2)
    # 显示窗口小部件
    # 将窗口设置为全屏显示
    window.setWindowTitle('基于北斗模块的多维生态环境数据采集与自动监测')
    # 获取屏幕尺寸
    screen_size = QDesktopWidget().screenGeometry().size()
    # 设置窗口大小为屏幕尺寸
    window.resize(screen_size.width(), screen_size.height())

    '''设置整体风格样式'''
    # styles = QStyleFactory.keys()  # 获取可用的样式列表
    # app.setStyle(QStyleFactory.create("Fusion"))  # 应用Fusion样式
    # setup stylesheet
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()

    '''线程管理'''


    def update_gauge():
        global w2
        global gauge
        while True:
            uv_index = random.uniform(0, 100)  # 模拟获取UV指数数据
            if not gauge:
                gauge = create_gauge(uv_index)
                gauge.render('gauge.html')
            else:
                gauge = create_gauge(uv_index)
                gauge.render('gauge.html', re_render=True)

            # 加载仪表盘到WebEngineView
            with open('gauge.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
                w2.setHtml(html_content)

            time.sleep(1)


    # 线程1：获取数据的线程
    class DataThread(QThread):
        def __init__(self):
            super().__init__()

        def run(self):
            global start_index
            global dir_data
            while True:
                # 获取数据并更新data_dict
                # 获取当前系统时间
                current_time = datetime.datetime.now().strftime('%H:%M:%S')
                try:
                    dir_data = BD_server.get_data(start_index, interval, driver)
                except:
                    print("未找到元素")
                    if logState:
                        logText.append(current_time + ':未找到元素!')
                    start_index -= 1
                else:
                    if logState:
                        logText.append(current_time + ':成功找到元素！！!')
                    # 获取经纬度信息
                    g = geocoder.ip('me')
                    latitude = g.latlng[0]
                    longitude = g.latlng[1]

                    # 更新'GPS Sensor Data'中的时间和经纬度
                    if 'GPS Sensor Data' in dir_data:
                        dir_data['GPS Sensor Data']['UTC Time'] = current_time
                        dir_data['GPS Sensor Data']['Latitude'] = str(latitude)
                        dir_data['GPS Sensor Data']['Longitude'] = str(longitude)
                        dir_data['GPS Sensor Data']['N/S'] = 'N'
                        dir_data['GPS Sensor Data']['E/W'] = 'E'
                    start_index += 1

                set_data(table, dir_data)
                # 可以在此添加适当的延时
                time.sleep(1)


    driverThread = threading.Thread(target=startDriver)
    driverThread.start()
    time.sleep(3)
    # 启动线程
    updateUVThread = threading.Thread(target=update_gauge)
    myThread = DataThread()
    myThread.start()

    # def update_table_data():
    #     global start_index
    #     global dir_data
    #     # 获取当前系统时间
    #     current_time = datetime.datetime.now().strftime('%H:%M:%S')
    #     try:
    #         dir_data = BD_server.get_data(start_index, interval, driver)
    #     except:
    #         print("未找到元素")
    #         logText.append(current_time + ':未找到元素!')
    #         start_index -= 1
    #     else:
    #         # 获取经纬度信息
    #         g = geocoder.ip('me')
    #         latitude = g.latlng[0]
    #         longitude = g.latlng[1]
    #
    #         # 更新'GPS Sensor Data'中的时间和经纬度
    #         if 'GPS Sensor Data' in dir_data:
    #             dir_data['GPS Sensor Data']['UTC Time'] = current_time
    #             dir_data['GPS Sensor Data']['Latitude'] = str(latitude)
    #             dir_data['GPS Sensor Data']['Longitude'] = str(longitude)
    #             dir_data['GPS Sensor Data']['N/S'] = 'N'
    #             dir_data['GPS Sensor Data']['E/W'] = 'E'
    #         start_index += 1
    #     set_data(table, dir_data)

    # # 创建一个定时器，每隔一段时间执行更新表格数据的函数
    # timer = QTimer()
    # timer.timeout.connect(update_table_data)
    # timer.start(300)  # 每隔1秒更新一次数据

    sys.exit(app.exec_())
