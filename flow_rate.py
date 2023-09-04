import numpy as np
num_points = 50
def get_flow_rate(num_points=50):
    linear_data = np.linspace(0, 1.5, num_points)
    sine_data = np.sin(np.linspace(-np.pi / 2, np.pi / 2, num_points)) * 0.75
    flowRate1 = linear_data + sine_data
    flowRate1 = np.clip(flowRate1, 0.0, 1.5)
    flowRate2 = flowRate1[::-1]
    flowRate = flowRate1.tolist() + flowRate2.tolist()
    flowRate = [str(round(rate, 2)) for rate in flowRate]
    return flowRate

# 打印前几个元素以示示例
# print(flowRate[:100])  # 打印前10个元素
