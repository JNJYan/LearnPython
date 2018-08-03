import re 
import os
import csv
import requests


# 北京
loc = 54511
headers = ['date', 'temp_high', 'temp_low', 'weather', 'wind_direction', 'wind_power']


# weathers1 = re.findall('(?<=\[).*(?=\])', r.text)[0]
# weathers = re.findall("{.+?}", weathers1)
# with open('weather.csv', 'w', newline='',encoding='gbk') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(headers)
#     rows_list = []
#     for x in weathers:
#         row_list = []
#         for y in x[1:-1].split(','):
#             row = re.findall("\'.*\'", y)[0][1:-1]
#             row_list.append(row)
#         rows_list.append(row_list)
#     writer.writerows(rows_list)
#     csvfile.close()


def get_reponse(loc, year, month):
    url = 'http://tianqi.2345.com/t/wea_history/js/' + str(loc) + '_' + str(year) + str(month) + '.js'
    r = requests.get(url)
    if '404' in str(r.text):
        url = 'http://tianqi.2345.com/t/wea_history/js/' + str(year) + '%02d' % (month) + '/'+ str(loc) + '_' + str(year) + '%02d' % (month) + '.js'
        r = requests.get(url)
        if '404' in str(r.text):
            return 
    return r.text


def data2csv(rows_list):
    with open('./learnpython/get_weather/weather.csv', 'a', newline='',encoding='gbk') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows_list)
        csvfile.close()


if __name__ == "__main__":
    # with open('weather.csv', 'w', newline='', encoding='gbk') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(headers)
    #     csvfile.close()
    for year in range(2011,2012):
        for month in range(1, 5):
            print("正在爬取北京市%d年%d月天气情况......" % (year, month))
            r = get_reponse(loc, year, month)
            weathers1 = re.findall('(?<=\[).*(?=\])', r)[0]
            weathers = re.findall("{.+?}", weathers1)
            rows_list = []
            for x in weathers:
                row_list = []
                for y in x[1:-1].split(','):
                    row = re.findall("\'.*\'", y)[0][1:-1]
                    row_list.append(row)
                rows_list.append(row_list)
            data2csv(rows_list)
            print("成功爬取北京市%d年%d月天气情况......" % (year, month))

        

    








