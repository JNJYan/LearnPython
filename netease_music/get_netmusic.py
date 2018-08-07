# encoding:utf-8
import re
import time
import json
import requests

# 评论json格式
'''
beReplied:[]
commentId:1205937997
content:"ćç°ĺ¨ćťĄčĺ­ä¸ĺĺ°ĺçâŚâľ"Kiki...do you love me......"âľ"Wishing and wishing...wishing on me......"đ"
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'https://music.163.com/'
}


# timeStamp==time
def time_convert(timeStanmp):
    timeArray = time.localtime(timeStanmp/1000)
    comment_time = time.strftime("%Y-%m-%d,%H:%M:%S", timeArray)
    return comment_time.split(',')


# 获取音乐id
def get_songid(songname):
    pass


# 以字典类型获取json数据
def get_json(url):
    r = requests.get(url, headers=headers)
    content_dict = json.loads(r.text)
    return content_dict


# 获取评论
def get_comment(url):
    return get_json(url)['comments']


# 获取评论数量
def get_comment_num(url):
    content = get_json(url)
    return int(content['total'])

url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%d?limit=100&offset=%d' % (song_id, offset)
total = get_comment(url)
offset = 100
song_id = 30953009

l2 = []
for index, content in enumerate(get_comment(url)):
    l1 = []
    l1.append(content['user']['nickname'])
    l1.append(content['user']['userId'])
    # 剔除评论中的换行符
    l1.append(content['content'].replace('\n', ' '))
    l1.extend(time_convert(int(content['time'])))
    l2.append(l1)
    # print(index, content['user']['nickname'],content['user'][''])
for l in l2:
    print(l)
