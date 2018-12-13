# -*- coding:utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
jieba.load_userdict('diaoyu.txt') #添加自定义词典

#打开文本
text = open('1.txt').read()
text = ' '.join(jieba.cut(text))
#生成对象
wc = WordCloud(font_path='FONT.otf',width=1920,height=1080,mode='RGBA',background_color=None).generate(text)
#显示词云
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

#保存
wc.to_file('wordcloud.png')

