import itchat
import numpy as numpy
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image

itchat.auto_login(enableCmdQR=2)

print('hi')
friends = itchat.get_friends(update=True)

# NickName = friends[0].NickName
# os.mkdir(NickName)

# file = '\%s' % NickName
# cp = os.getcwd()
# path = os.path.join(cp+file)
# os.chdir(path)

number_of_friends = len(friends)

df_friends = pd.DataFrame(friends)

Province = df_friends.Province

Province_count = Province.value_counts()

Province_count = Province_count[Province_count.index!='']

