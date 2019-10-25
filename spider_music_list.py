from bs4 import BeautifulSoup
import requests
import time
from config import headers

def get_music_lists(url):
    time.sleep(1)
    response = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    # 找到所有的a标签以及包含的信息
    a_lists = soup.select('.dec a')
    li_lists = soup.select('#m-pl-container li')
    for i in range(len(a_lists)):
        url = a_lists[i]['href']
        title = a_lists[i]['title'].replace(',', '，')
        play_num = li_lists[i].select('.nb')[0].get_text()
        author = li_lists[i].select('p')[1].select('a')[0].get_text()
        print(url, title, play_num, author)
        # 将获取的数据存到csv文件中方便后序获取其他信息
        with open('music_lists_0_1500.csv', 'a+', encoding='utf-8') as f:
            f.write(url+','+title+','+play_num+','+author+'\n')


if __name__ == '__main__':
    language_lists = ['华语', '欧美', '日语', '粤语', '韩语']
    for language in language_lists:
        for i in range(0, 1500, 35):
            url = f'https://music.163.com/discover/playlist/?cat={language}&order=hot&limit=35&offset={i}'
            get_music_lists(url)
    print('OK')
