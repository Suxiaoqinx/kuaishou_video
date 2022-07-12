import requests
import json
import re 

geturl = "https://v.kuaishouapp.com/s/NTuYIMTy" #替换为你的视频链接
# 请求网页
response = requests.get(geturl)
#正则获取链接中的快手视频id
surl = re.findall('photoId=(.*?)&',response.url)
url = "https://v.m.chenzhongtech.com/rest/wd/photo/info"
payload = '{"photoId": "'+surl[0]+'","isLongVideo": false}'
headers = {
   'Cookie': 'did=web_9bceee20fa5d4a968535a27e538bf51b; didv=1655992503000;', #如果失效了的话 请更新一下cookie！
   'Referer': response.url,
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
#格式化json
jsonobj = json.loads(response.text)
print(
   '视频标题：'+jsonobj['photo']['caption']+'\n'+
   '视频图片：'+jsonobj['photo']['coverUrls'][0]['url']+'\n'+
   '视频直链：'+jsonobj['photo']['mainMvUrls'][0]['url'])
