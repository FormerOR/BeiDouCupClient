import time
import binascii
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time




# 解析服务端数据存入字典中
def parse_data(data):
    parsed_data = {}
    lines = data.split("\n")

    current_category = None
    for line in lines:
        line = line.strip()
        if line.endswith(":"):
            current_category = line[:-1]
            parsed_data[current_category] = {}
        elif ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if current_category is not None:
                parsed_data[current_category][key] = value

    return parsed_data


def start_web():
    # 设置Chrome驱动程序的路径
    # chrome_path = 'chromedriver.exe'

    # 设置Chrome选项
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器窗口
    chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速

    chrome_driver_path = "chromedriver.exe"  # 替换为你实际的ChromeDriver路径
    chrome_browser_path = "D://Chrome115//chrome-win64//chrome.exe"  # 替换为你实际的Chrome浏览器可执行文件路径
    # 启动Chrome浏览器驱动
    # service = Service(chrome_path)
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # 使用webdriver_manager来启动ChromeDriver
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    # 指定ChromeDriver和Chrome浏览器的路径
    chrome_options.binary_location = chrome_browser_path
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    # 打开网站
    url = 'http://tc.tastek.cn/index.htm'
    driver.get(url)

    # 登录
    login_name = '15847448988'
    login_pass = 'beidou666'

    time.sleep(3)
    # 找到账号输入框并输入账号
    login_name_xpath = '//*[@id="loginName"]'
    login_name_element = driver.find_element(By.XPATH, login_name_xpath)
    login_name_element.send_keys(login_name)

    # 找到密码输入框并输入密码
    login_pass_xpath = '//*[@id="logonPass"]'
    login_pass_element = driver.find_element(By.XPATH, login_pass_xpath)
    login_pass_element.send_keys(login_pass)

    # 提交登录表单
    login_button_xpath = '//*[@id="logonSub"]'
    login_button_element = driver.find_element(By.XPATH, login_button_xpath)
    login_button_element.click()

    # 等待登录完成（可根据实际情况调整等待时间）
    time.sleep(6)

    # 点击设置链接协议
    monitor_center_xpath = '//*[@id="tlink-sensorData"]/table/thead[2]/tr/td/div/a[2]'
    monitor_center_element = driver.find_element(By.XPATH, monitor_center_xpath)
    monitor_center_element.click()

    time.sleep(5)
    # # 点击指定按钮
    # button_xpath = '//*[@id="layui-layer1"]/span[1]/a[2]'
    # button_element = driver.find_element(By.XPATH, button_xpath)
    # button_element.click()

    time.sleep(10)

    return driver


def get_data(start_index, interval, driver):
    # 持续爬取数据
    # 构建XPath路径
    # print(start_index)
    data_xpath = f'//*[@id="receiveWindow"]/div[{start_index}]/div'

    # 获取数据
    try:

        # data_element = driver.find_element(By.XPATH, data_xpath)
        # data = data_element.get_attribute('innerHTML')
        # # 打印当前数据
        # print("当前数据:", data)

        # 获取数据
        data_element = driver.find_element(By.XPATH, data_xpath)
        data = data_element.text
    except:
        print("无法找到指定元素")
        start_index += 1
    else:
        # 打印当前数据
        print("当前数据:", data)

        # 提取16进制部分
        hex_data = data.split(":")[-1].strip()

        # 转换为ASCII字符串
        ascii_data = binascii.unhexlify(hex_data).decode()

        # 输出结果
        print("解析后的数据:", ascii_data)

        dir_data = parse_data(ascii_data)

        # 等待指定时间
        # time.sleep(interval)

    return dir_data


