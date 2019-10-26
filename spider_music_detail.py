# 由歌单中的详细信息获取
import json
import time
import requests
from bs4 import BeautifulSoup
from config import headers
# import get_params_encSecKey


def get_detail(url, music_id):
    response = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    # 获取歌手名
    songer = soup.select('.des')[1].get_text()
    # 获取专辑名
    desc_name = soup.select('.des')[2].get_text()
    # 获取歌曲名
    music_name = soup.select('.f-ff2')[0].get_text()
    #
    # comment_num+zan_num 即可以估算总体的收听量
    # 此收听量远远小于真是网易云音乐的收听量
    #
    # 这个数据是动态加载的
    #######
    # url_comment = f'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{music_id}?csrf_token='
    # data_form = get_params_encSecKey.main(music_id)
    # res = requests.post(url=url_comment, headers=headers, data=data_form).text
    #######
    # 可以使用api接口获取, 更加简单
    url_comment1 = f'http://music.163.com/api/v1/resource/comments/R_SO_4_{music_id}'
    res = requests.get(url=url_comment1, headers=headers).text
    data = json.loads(res)
    # 获取评论量 comment_num
    comment_num = data['total']
    # 获取精彩评论的赞的数量 likedCount
    likedCount_num = []
    for comment in data['hotComments']:
        likedCount_num.append(comment['likedCount'])
    # 打印
    print(songer, desc_name, music_name, music_id, comment_num, likedCount_num)
    # 将获取的数据写到 totle_music_liked_num.csv
    with open('total_music_liked_num.csv', 'a+', encoding='utf-8') as f:
        f.write(songer + ',' + desc_name + ',' + music_name + ',' + music_id + ',' + str(comment_num) + ',' + str(
            likedCount_num) + '\n')


def main(url):
    music_id = url[11:]
    print(music_id)
    url = 'https://music.163.com' + url
    get_detail(url, music_id)
