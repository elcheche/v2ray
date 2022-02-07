import base64
import requests
subLink='https://dy.manaocloud.com/api/v1/client/subscribe?token=053b36535ffbbf8008cc5dc0ed4c70a7'
# 获取订阅信息
serverListLink = base64.b64decode(requests.get(subLink).content).splitlines()
serverLink=[]
for i in serverListLink:
    i=bytes.decode(i)
    serverLink.append(i+'\n')
print(serverLink)
with open('./v2ray.txt','w') as f:
    f.writelines(serverLink)