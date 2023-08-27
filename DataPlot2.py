import sys
import time
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SensorPlot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.frame = QFrame()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.fig, self.axs = plt.subplots(2, 2, figsize=(8, 6))
        self.fig.set_facecolor('#333333')
        self.axs[0, 0].set_facecolor('#1E1E1E')  # 设置背景颜色
        self.axs[0, 1].set_facecolor('#1E1E1E')  # 设置背景颜色
        self.axs[1, 0].set_facecolor('#1E1E1E')  # 设置背景颜色
        self.axs[1, 1].set_facecolor('#1E1E1E')  # 设置背景颜色
        self.axs[0, 0].set_ylim(0, 100)
        self.axs[0, 1].set_ylim(0, 50)
        self.axs[1, 0].set_ylim(99000, 110000)
        self.axs[0, 1].set_ylim(0, 500)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

        self.ori_data = {
            'UV Sensor Data': {'Vout': '107', 'UV': '1'},
            'Humidity and Temperature Sensor Data': {'Humidity': '31.10', 'Temperature': '29.90',
                                                     'Heat Index Celsius': '28.74',
                                                     'Heat Index Fahrenheit': '83.73'},
            'Gas Sensor Data': {'PPM': '1.50'},
            'Soil Sensor Data': {'Moisture': '1014', 'State': '1'},
            'BMP Sensor Data': {'Temperature': '26.28', 'Pressure': '99947.13', 'Altitude': '115.36'},
            'Rain Sensor Data': {'Rain': '231', 'State': '1'},
            'Water Sensor Data': {'Liquid Flow Rate': '0.00', 'Total Liquid Quantity': '0.00'},
            'Wind Sensor Data': {'Wind Speed': '0.00', 'Real Speed': '0.00', 'Power': '0.00',
                                 'Power Normalized': '0.00'},
            'GPS Sensor Data': {'UTC Time': 'NONE', 'Latitude': 'NONE', 'N/S': 'NONE', 'Longitude': 'NONE',
                                'E/W': 'NONE'}
        }

        # Extract relevant data
        self.humidity_data = float(self.ori_data['Humidity and Temperature Sensor Data']['Humidity'])
        self.temperature_data = float(self.ori_data['Humidity and Temperature Sensor Data']['Temperature'])
        self.pressure_data = float(self.ori_data['BMP Sensor Data']['Pressure'])
        self.altitude_data = float(self.ori_data['BMP Sensor Data']['Altitude'])
        # 初始化数据表
        self.update_subplots(self.humidity_data, self.temperature_data, self.pressure_data, self.altitude_data)

    def update_subplots(self, humidity, temperature, pressure, altitude):
        self.axs[0, 0].clear()
        self.axs[0, 0].bar(['Humidity'], [humidity], color=(0.39, 0.58, 0.92, 0.6))
        self.axs[0, 0].set_title('Humidity')

        self.axs[0, 1].clear()
        self.axs[0, 1].bar(['Temperature'], [temperature], color=(0.39, 0.58, 0.92, 0.7))
        self.axs[0, 1].set_title('Temperature')

        self.axs[1, 0].clear()
        self.axs[1, 0].bar(['Pressure'], [pressure], color=(0.39, 0.58, 0.92, 0.8))
        self.axs[1, 0].set_title('Pressure')

        self.axs[1, 1].clear()
        self.axs[1, 1].bar(['Altitude'], [altitude], color=(0.39, 0.58, 0.92, 0.9))
        self.axs[1, 1].set_title('Altitude')

        self.axs[0, 0].set_ylim(0, 100)
        self.axs[0, 1].set_ylim(0, 50)
        self.axs[1, 0].set_ylim(99000, 110000)
        self.axs[1, 1].set_ylim(0, 500)
        plt.tight_layout()
        plt.pause(0.01)  # Pause to allow time for the plot to update


    def updateData(self,dir_data):
        # 获取数据
        self.humidity_data = float(dir_data['Humidity and Temperature Sensor Data']['Humidity'])
        self.temperature_data = float(dir_data['Humidity and Temperature Sensor Data']['Temperature'])
        self.pressure_data = float(dir_data['BMP Sensor Data']['Pressure'])
        self.altitude_data = float(dir_data['BMP Sensor Data']['Altitude'])

        # 更新数据
        self.update_subplots(self.humidity_data, self.temperature_data, self.pressure_data, self.altitude_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    plotWidget = SensorPlot()
    mainWindow.setCentralWidget(plotWidget)
    mainWindow.show()
    sys.exit(app.exec_())
