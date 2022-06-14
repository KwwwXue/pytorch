import requests
import re
import csv


url = 'https://movie.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
}

res = requests.get(url, headers=headers)
page_content = res.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*? <p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)</span>', re.S)
# re.S 让 . 能匹配换行符
# 匹配数据
result = obj.finditer(page_content)
# finditer 返回一个可迭代的对象
f = open('data.csv', 'w')
csvfile = csv.writer(f)
for i in result:
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvfile.writerow(dic.values())

    # print(i.group('name'))
    # print(i.group('rating'))
    # print(i.group('num'))
    # print(i.group('year').strip())
f.close()
print('over')




