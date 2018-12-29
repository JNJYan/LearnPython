# encoding:utf-8
import re
import time
import json
import pandas as pd
import requests

# 评论json格式
'''
beReplied:[]
commentId:1205937997
content:"*****"
expressionUrl:null
isRemoveHotComment:false
liked:false
likedCount:3
pendantData:null
time:1533513689220
user:{
    authStatus:0
    avatarUrl:"http://p1.music.126.net/NQ9AOkXV1Qdypks6e_8QdQ==/109951163238799006.jpg"
    expertTags:null
    experts:null
    locationInfo:null
    nickname:"o_kiko"
    remarkName:null
    userId:493859934
    userType:0
    vipType:0
}
'''
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'music.163.com',
    'Cookie': '_ntes_nnid=a3d6ccdc7f2c422ce51ca556803ab815,1537186911138; _ntes_nuid=a3d6ccdc7f2c422ce51ca556803ab815; __oc_uuid=02937a80-cc36-11e8-abc4-e79ac77fb85b; __utma=187553192.1993537246.1539139307.1539139307.1539139307.1; __utmz=187553192.1539139307.1.1.utmcsr=open.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; usertrack=ezq0o1u/MkA+cg3sBwPYAg==; vjuids=27dd3591a.1666bf4ee13.0.02191a767ea9d; vjlast=1539409506.1539409506.30; vinfo_n_f_l_n3=6e34463e3a4cb582.1.0.1539409505843.0.1539409523842; _iuqxldmzr_=32; WM_TID=d%2FEA642tDulOs%2B%2BxsRxLxovD1PpU0HF4; _ga=GA1.2.1993537246.1539139307; hb_MA-9ADA-91BF1A6C9E06_source=www.baidu.com; mp_MA-9ADA-91BF1A6C9E06_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fcampus.163.com%2F%22%2C%22updatedTime%22%3A%201545708633128%2C%22sessionStartTime%22%3A%201545708633121%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22de8c3ba2-d516-4c06-91b2-b3777e5c585a%22%2C%22persistedTime%22%3A%201545708633115%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201545708633128%7D%2C%22sessionUuid%22%3A%20%22cb352d66-472f-4ec6-a38f-c652066085f4%22%7D; WM_NI=ILpiox1dx891Sd3kvm%2Btx410AU0YDCPDfkDV%2F9nO14Fiiih%2B6xJtdtQt%2BbKAAn0U7BDGMNxljHO77Enoi8s07QTrW8lYXo6J%2BdFRYot6Z2KfvN2h7hSQ8Y8AcBhSDBvROXI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8fe667b58ebf99c880fcb88fb2c44a838f8bbbbb48edb19eb6b26fb292bfabd92af0fea7c3b92a8b94c08aee74f3bcb8d9bc3b91bcfd8cf567e9acb8d5b43c838b00bac749949caa8cc75eede7a2b0b44086b7a78aeb21f6a88695e78093ace583ca4b83b200b6b64a889983affb68aa9881d8b64faeb1a7d9f23cf58f9c93d634b0879890b542e9bc8ab3dc65b8ea96d3ca6eb692fe89b664918ff8babb4ba19ea8b4c74ab68e81b9cc37e2a3; __utma=94650624.1762855987.1542436690.1545926973.1545990894.5; __utmc=94650624; __utmz=94650624.1545990894.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=lk5WKfroZU6HbZlTbdTCUejX3bmg7zqVJ4P2f2T131XBQuI7J4PcylxxEQflwi95MXCO36UowhriOYihuhWDATKh7%2BFibNY%2FcIIKsBvHWlwiO82lpydvWCiZF6reEIeGAKeYIAOY22nDkXtMQlFSn5OTNGepm0i8l9rmBu3%2BbT6U56tn%3A1545996174955; MUSIC_U=783961e50d8b516267d0dd87e0d5d12d8bc1a7682774f1c9db035c51943e152fe2cbed485b24d74030e91786701ddf8a41049cea1c6bb9b6; __remember_me=true; __csrf=2bce8e39fc7dde3ab4763af2f683d645; __utmb=94650624.28.10.1545990894',
    'Origin': 'https://music.163.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}


# timeStamp==time
def time_convert(timeStanmp):
    timeArray = time.localtime(timeStanmp/1000)
    comment_time = time.strftime("%Y-%m-%d,%H:%M:%S", timeArray)
    return comment_time.split(',')


# 以字典类型获取json数据
def get_json(url):
    r = requests.get(url, headers=headers)
    print(r)
    content_dict = json.loads(r.text)
    return content_dict


# 获取评论
def get_comment_api(song_id, offset):
    comment_api = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%d?limit=100&offset=%d' % (song_id, offset)
    comment_json = get_json(comment_api)
    comments_page = comment_json['comments']
    return comments_page


# 获取评论数量
def get_comment_num(song_id):
    comment_api = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%d?limit=100&offset=0' % (song_id)
    comment_json = get_json(comment_api)
    comments_num = comment_json['total']
    return comments_num


def store_comment(comment_api):
    comments_page= []
    for index, content in enumerate(comment_api):
        comment_info = []

        comment_info.append(content['commentId'])
        comment_info.append(content['user']['userId'])
        comment_info.append(content['user']['nickname'])
        comment_info.append(content['content'].replace('\n', '，').replace('\r', ','))
        comment_info.append(content['likedCount'])
        comment_info.extend(time_convert(int(content['time'])))
        comment_info.append(content['user']['userType'])
        comment_info.append(content['user']['authStatus'])
        comment_info.append(content['user']['vipType'])

        comments_page.append(comment_info)
    return comments_page

name = ['commentId', 'userId', 'nickname', 'comment_content', 'likedCount', 'day', 'time','userType', 'authStatus', 'vipType']
song_id = 1334849028

def get_comment(song_id):
    offset = 0
    comments_num = get_comment_num(song_id)
    print(comments_num)
    page_num = comments_num // 100
    comments_all = []
    print(page_num)
    for page in range(1, page_num):
        offset += 100
        print(page)
        comment_api = get_comment_api(song_id, offset)
        comments_page = store_comment(comment_api)
        # print(len(comments_page))
        comments_all.extend(comments_page)
        # print('page==>comments')
    comment_df = pd.DataFrame(columns=name,data=comments_all)
    comment_df.to_csv('test.csv')


if __name__ == '__main__':
    get_comment(song_id)