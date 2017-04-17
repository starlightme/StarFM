#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017-04-16 12:23

@author: Jimmy66 <jimmy66me@gmail.com>
'''

import requests
import simplejson as json

def get_song_list_info(songlist_id):
    request_url = ''.join(['http://music.163.com/api/playlist/detail?id=',songlist_id])
    raw_data  = requests.get(request_url).text
    music_dict = json.loads(raw_data)
    music_list = []
    cnt = 1
    for item in music_dict['result']['tracks']:
        # print(item['name'])               # song_name
        # print(item['mp3Url'])             # music_url
        # print(item['album']['picUrl'])    # album_pic
        try:
            r = requests.get(item['mp3Url'])
            if r.status_code is 200:
                music_list.append(  dict( id = cnt , name = item['name'] , url =  item['mp3Url'] , imgurl = item['album']['picUrl'] )  )
                cnt += 1
        except Exception as e:
            print(e)
            print(item['name'])
        finally:
            print('finish one')
    return music_list

 


if __name__ == '__main__':
    songlist_id = '61589168'
    songlist_info = get_song_list_info(songlist_id)
    # print(songlist_info)
    result = dict( songlist = songlist_info)
    #print(result)
    with open('src/common/music.json','w',encoding='utf-8') as fp:
        json.dump(result,fp,encoding="UTF-8", ensure_ascii=False,indent=4)

 