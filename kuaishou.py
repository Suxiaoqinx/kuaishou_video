import requests
import json
import re 
response = requests.get(input('请输入你需要解析的快手链接:'))
#正则获取链接中的快手视频id
ksid = re.findall('photoId=(.*?)&',response.url)
url = "https://v.m.chenzhongtech.com/rest/wd/photo/info"
payload = '{"photoId": "'+ksid[0]+'","isLongVideo": false}'
headers = {
   'Cookie': 'did=web_9bceee20fa5d4a968535a27e538bf51b; didv=1655992503000;', #如果解析失败可以尝试替换cookie
   'Referer': response.url,
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
#格式化json
jsonobj = json.loads(response.text)
if jsonobj['photo']['mainMvUrls'][0]['url'] in jsonobj:
    print('获取视频直链失败！')
else:
    print('提示：获取成功！' + '\n'+'视频标题：'+jsonobj['photo']['caption']+'\n'+'视频图片：'+jsonobj['photo']['coverUrls'][0]['url']+'\n'+'视频直链：'+jsonobj['photo']['mainMvUrls'][0]['url']+'\n'+'作者：'+jsonobj['photo']['userName'])
