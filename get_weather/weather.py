# encoding: utf-8
import re
import os
import csv
import requests

# 地区对应气象台站号
loc = {'北京市':54511, '北京市丰台区':71142, '烟台市':54765, '无锡市':58354}
# 2011-2015年
headers_old = ['date', 'temp_high', 'temp_low',
               'weather', 'wind_direction', 'wind_power']
# 2016-至今
headers_new = ['date', 'temp_high', 'temp_low',
               'weather', 'wind', 'aqi', 'aqiInfo', 'aqiLevel']


def get_reponse(loc, year, month):
    if year < 2016:
        url = 'http://tianqi.2345.com/t/wea_history/js/' + \
            str(loc) + '_' + str(year) + str(month) + '.js'
    elif year == 2016 and month < 3:
        url = 'http://tianqi.2345.com/t/wea_history/js/' + \
            str(loc) + '_' + str(year) + str(month) + '.js'
    else:
        url = 'http://tianqi.2345.com/t/wea_history/js/' + \
            str(year) + '%02d' % (month) + '/' + str(loc) + \
            '_' + str(year) + '%02d' % (month) + '.js'
    r = requests.get(url)
    if '404' in str(r.text):
        return
    return r.text


def data2csv(rows_list, year, month):
    if year < 2016:
        with open('./learnpython/get_weather/%s_2011-2015.csv' % loc_str, 'a', newline='', encoding='gbk') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows_list)
            csvfile.close()
    else:
        with open('./learnpython/get_weather/%s_2016--.csv' % loc_str, 'a', newline='', encoding='gbk') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows_list)
            csvfile.close()


def _get_data(loc_str, year, month):
    # print("正在爬取北京市%d年%d月天气情况......" % (year, month))
    r = get_reponse(loc[loc_str], year, month)
    # print(r)
    try:
        weathers1 = re.findall('(?<=\[).*(?=\])', r)[0]
        weathers = re.findall("{.+?}", weathers1)
    except TypeError as e:
        print(e)
        return 
    rows_list = []
    for x in weathers:
        row_list = []
        for y in x[1:-1].split(','):
            row = re.findall("\'.*\'", y)[0][1:-1]
            row_list.append(row)
            # print(row)
        rows_list.append(row_list)
    # print("--------------------------------------")
    data2csv(rows_list, year, month)
    print("成功爬取%s%d年%d月天气情况......" % (loc_str, year, month))


def addheaders():
    if not os.path.exists('./learnpython/get_weather/%s_2011-2015.csv' % loc_str):
        with open('./learnpython/get_weather/%s_2011-2015.csv' % loc_str, 'w', newline='', encoding='gbk') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers_old)
            csvfile.close()
    if not os.path.exists('./learnpython/get_weather/%s_2016--.csv' % loc_str):
        with open('./learnpython/get_weather/%s_2016--.csv' % loc_str, 'w', newline='', encoding='gbk') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers_new)
            csvfile.close()


if __name__ == "__main__":
    for loc_str in loc.keys():
        addheaders()
        for year in range(2011, 2019):
            for month in range(1, 13):
                _get_data(loc_str, year, month)
