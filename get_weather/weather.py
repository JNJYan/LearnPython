# encoding: utf-8
import re
import os
import csv
import time
# import asyncio
import requests

# 地区对应气象台站号
loc = {'北京市':54511, '北京市丰台区':71142, '烟台市':54765, '无锡市':58354}

# 表头
headers = ['date', 'temp_high', 'temp_low',
               'weather', 'wind_direction', 'wind_power', 'aqi', 'aqiInfo', 'aqiLevel']


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


def data2csv(rows_year, year, month):
    print("正在存储%s%d年天气数据......"  % (loc_str, year))
    with open('./learnpython/get_weather/%s_2018-2018.csv' % loc_str, 'a', newline='', encoding='gbk') as csvfile:
        writer = csv.writer(csvfile)
        for rows_month in rows_year:
            try:
                writer.writerows(rows_month)
            except:
                pass
        csvfile.close()
    print("添加成功")



def _get_data(loc_str, year, month):
    # print("正在爬取北京市%d年%d月天气情况......" % (year, month))
    r = get_reponse(loc[loc_str], year, month)
    # print(r)
    try:
        weathers1 = re.findall('(?<=\[).*(?=\])', r)[0]
        weathers = re.findall("{.+?}", weathers1)
    except:
        return 
    rows_list = []
    for x in weathers:
        row_list = []
        for y in x[1:-1].split(','):
            row = re.findall("\'.*\'", y)[0][1:-1]
            row_list.append(row)
            # print(row)
        rows_list.append(row_list)
    # print("成功爬取%s%d年%d月天气情况......" % (loc_str, year, month))
    return rows_list


def addheaders():
    if not os.path.exists('./learnpython/get_weather/%s_2018-2018.csv' % loc_str):
        with open('./learnpython/get_weather/%s_2018-2018.csv' % loc_str, 'w', newline='', encoding='gbk') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            csvfile.close()


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    start = time.clock()
    for loc_str in loc.keys():
        addheaders()
        for year in range(2018, 2019):
            rows_year = []
            for month in range(1, 6):
                rows_month = _get_data(loc_str, year, month)
                rows_year.append(rows_month)
            data2csv(rows_year, year, month)
    end = time.clock()
    # loop.close()
    print(end - start)
            
