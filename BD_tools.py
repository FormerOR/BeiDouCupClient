import random


def transNumber(number_str, percentage_range=20, sub=2):
    if percentage_range < 0 or percentage_range > 100:
        raise ValueError("Percentage range should be between 0 and 100")
    number = float(number_str)
    percentage = random.uniform(-percentage_range, percentage_range)
    adjustment = number * (percentage / 100)
    result = number + adjustment
    result_str = str(round(result, sub))
    return result_str


def trans2Str(input_dict):
    input_dict['UV Sensor Data']['Vout'] = transNumber(input_dict['UV Sensor Data']['Vout'], 20, 0)
    input_dict['Humidity and Temperature Sensor Data']['Humidity'] = transNumber(
        input_dict['Humidity and Temperature Sensor Data']['Humidity'],2)
    input_dict['Humidity and Temperature Sensor Data']['Temperature'] = transNumber(
        input_dict['Humidity and Temperature Sensor Data']['Temperature'], 0.5)
    input_dict['Humidity and Temperature Sensor Data']['Heat Index Celsius'] = transNumber(
        input_dict['Humidity and Temperature Sensor Data']['Heat Index Celsius'],2)
    input_dict['Humidity and Temperature Sensor Data']['Heat Index Fahrenheit'] = transNumber(
        input_dict['Humidity and Temperature Sensor Data']['Heat Index Fahrenheit'],2)
    input_dict['Gas Sensor Data']['PPM'] = transNumber(input_dict['Gas Sensor Data']['PPM'], 20, 0)
    # input_dict['Soil Sensor Data']['Moisture'] = transNumber(input_dict['Soil Sensor Data']['Moisture'], 2, 0)
    input_dict['Water Sensor Data']['Liquid Flow Rate'] = transNumber(input_dict['Water Sensor Data']['Liquid Flow Rate'])
    input_dict['BMP Sensor Data']['Temperature'] = transNumber(input_dict['BMP Sensor Data']['Temperature'], 0.5)
    input_dict['Water Sensor Data']['Total Liquid Quantity'] = transNumber(input_dict['Water Sensor Data']['Total Liquid Quantity'])

    return input_dict


if __name__ == "__main__":
    ori_data = {
        'UV Sensor Data': {'Vout': '107', 'UV': '1'},
        'Humidity and Temperature Sensor Data': {'Humidity': '50.10', 'Temperature': '29.90',
                                                 'Heat Index Celsius': '28.74',
                                                 'Heat Index Fahrenheit': '83.73'},
        'Gas Sensor Data': {'PPM': '1.50'},
        'Soil Sensor Data': {'Moisture': '1014', 'State': '1'},
        'BMP Sensor Data': {'Temperature': '30.30', 'Pressure': '99947.13', 'Altitude': '115.36'},
        'Rain Sensor Data': {'Rain': '231', 'State': '1'},
        'Water Sensor Data': {'Liquid Flow Rate': '0.00', 'Total Liquid Quantity': '0.00'},
        'Wind Sensor Data': {'Wind Speed': '0.00', 'Real Speed': '0.00', 'Power': '0.00', 'Power Normalized': '0.00'},
        'GPS Sensor Data': {'UTC Time': 'NONE', 'Latitude': 'NONE', 'N/S': 'NONE', 'Longitude': 'NONE', 'E/W': 'NONE'}
    }
    keys_to_update_ = ['Vout', 'Humidity', 'Heat Index Celsius', 'Heat Index Fahrenheit', 'PPM',
                       'Moisture', 'Temperature', 'Rain', 'Liquid Flow Rate', 'Total Liquid Quantity']
    # print(trans2Str(ori_data,keys_to_update_))

    # 直接访问并修改特定值，同时将结果转换为字符串并四舍五入到2位小数
    ori_data['UV Sensor Data']['Vout'] = transNumber(ori_data['UV Sensor Data']['Vout'], 20, 0)
    ori_data['Humidity and Temperature Sensor Data']['Humidity'] = transNumber(
        ori_data['Humidity and Temperature Sensor Data']['Humidity'])
    ori_data['Humidity and Temperature Sensor Data']['Temperature'] = transNumber(
        ori_data['Humidity and Temperature Sensor Data']['Temperature'],2)
    ori_data['Humidity and Temperature Sensor Data']['Heat Index Celsius'] = transNumber(
        ori_data['Humidity and Temperature Sensor Data']['Heat Index Celsius'])
    ori_data['Humidity and Temperature Sensor Data']['Heat Index Fahrenheit'] = transNumber(
        ori_data['Humidity and Temperature Sensor Data']['Heat Index Fahrenheit'])
    ori_data['Gas Sensor Data']['PPM'] = transNumber(ori_data['Gas Sensor Data']['PPM'], 20, 0)
    ori_data['Soil Sensor Data']['Moisture'] = transNumber(ori_data['Soil Sensor Data']['Moisture'], 20, 0)
    ori_data['Water Sensor Data']['Liquid Flow Rate'] = transNumber(ori_data['Water Sensor Data']['Liquid Flow Rate'])
    ori_data['BMP Sensor Data']['Temperature'] = transNumber(ori_data['BMP Sensor Data']['Temperature'])
    ori_data['Water Sensor Data']['Total Liquid Quantity'] = transNumber(ori_data['Water Sensor Data']['Total Liquid Quantity'])


    print(ori_data)
