import re
import os
import requests

url_host = 'http://jiangnan.91job.gov.cn'
campus_url = 'http://jiangnan.91job.gov.cn/campus'

r = requests.get(campus_url)
