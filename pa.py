import requests
import re
import json
import csv
#  求出前三百视频bv号
headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': "buvid3=1E2D46E0-A391-0C1C-985A-57C095C3A39077224infoc; b_nut=1693906877; i-wanna-go-back=-1; b_ut=7; _uuid=DC375102D-8B810-8CFB-CBE9-DA7251F9544B76101infoc; home_feed_column=4; buvid4=CDCE3142-A4D9-5118-DD28-5ECB29E244C780243-023090517-%2FxwqHe8zHTXbXEYI08aKhg%3D%3D; DedeUserID=95710109; DedeUserID__ckMd5=7cea815f11230de7; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO2816939069099637; header_theme_version=CLOSE; CURRENT_FNVAL=4048; rpdid=|(u))kkYu|Ru0J'uYmJmkJ~Ru; CURRENT_QUALITY=116; fingerprint=15d91fc759a24145d5f5f86311889eb3; buvid_fp_plain=undefined; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQyNTE3NTksImlhdCI6MTY5Mzk5MjU1OSwicGx0IjotMX0.6yU5TJWfhtx3_EBG4CpmnzPUib3v33_qXaTm8HoUNdo; bili_ticket_expires=1694251759; buvid_fp=15d91fc759a24145d5f5f86311889eb3; SESSDATA=3b2913dd%2C1709722559%2Cf6012%2A91CjD_2t7oidMgBihPYurZNs7uTshU3RO-jIgl89PoqFhKzjq86mqfgYSBaImoh6d5RCsSVks3RFpiQ3dUZmVNODhwQ08xVnVrNW1NelNwVEJNczN6THhLWjZWdGVCdXZibU9xR1dKaFRzcW4tS0hySms4QUZncEJEak9uWGZQVWd1WmJWMTRNWmdRIIEC; bili_jct=2ee681367ef1ab9c45c7a9e65d281d46; sid=7iakqlm0; PVID=2; bp_video_offset_95710109=839162749106782243; b_lsid=EA104C17F_18A777A3F45; innersign=0; browser_resolution=779-594",
        'Origin': 'https://search.bilibili.com',
        'Referer': 'https://search.bilibili.com/all?keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=24',
        'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
    }
bv_id = []
def pab():
    for page in range(1, 8):
        url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
        data = {
        '__refresh__': 'true',
        '_extra': '',
        'context': '',
        'page': page,
        'page_size': '42',
        'from_source': '',
        'from_spmid': '333.337',
        'platform': 'pc',
        'highlight': '1',
        'single_column': '0',
        'keyword': '日本核污染水排海',
        'qv_id': 'sSwqpN5lRf2QMBEXCgrfe81ubNuv8B9B',
        'ad_resource': '5654',
        'source_tag': '3',
        'gaia_vtoken': '',
        'category_id': '',
        'search_type': 'video',
        'dynamic_offset': '24',
        'web_location': '1430654',
        'w_rid': '3',
        'a2c13637be5ee67ee24164727c7dcd3': '',
        'wts': '1694222560',
        }
        response1 = requests.get(url=url, headers=headers, params=data)
        for index in (response1.json()['data']['result']):
            bv_id.append(index['bvid'])
    url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
    data = {
        '__refresh__': 'true',
        '_extra': '',
        'context': '',
        'page': '8',
        'page_size': '6',
        'from_source': '',
        'from_spmid': '333.337',
        'platform': 'pc',
        'highlight': '1',
        'single_column': '0',
        'keyword': '日本核污染水排海',
        'qv_id': 'sSwqpN5lRf2QMBEXCgrfe81ubNuv8B9B',
        'ad_resource': '5654',
        'source_tag': '3',
        'gaia_vtoken': '',
        'category_id': '',
        'search_type': 'video',
        'dynamic_offset': '24',
        'web_location': '1430654',
        'w_rid': '3',
        'a2c13637be5ee67ee24164727c7dcd3': '',
        'wts': '1694222560',
    }
    response2 =requests.get(url=url,params=data,headers=headers)
    for index in (response2.json()['data']['result']):
        bv_id.append(index['bvid'])

#  已知bv号求出弹幕
def qid(id):
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={id}&jsonp=jsonp'
    response= requests.get(url)
    content=response.text
    ut =json.loads(content)
    return ut["data"][0]["cid"]

def padan():
    for i in range(0,300):
        x = bv_id[i]
        y =qid(x)
        url3 =f'https://api.bilibili.com/x/v1/dm/list.so?oid={y}'
        response4 =requests.get(url=url3,headers=headers)
        response4.encoding='utf-8'
        list=re.findall('<d p=".*?">(.*?)</d>',response4.text)
        for j in list:
            with open('danmu.csv', "a", newline='', encoding='utf-8-sig')as f:
                writer=csv.writer(f)
                danmu =[]
                danmu.append(j)
                writer.writerow(danmu)
if __name__ == '__main__':
    pab()
    padan()


