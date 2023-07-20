# -*- coding:utf-8 -*-
import requests
import json
import time


orgId=608196190709395456
sourceId=725191327228612608

segId=742246596258111488
itemId=742246596270694400
courseId=742239030733467648

videoId=742241960656138240

cookie='_abfpc=ad95389e5cf82db96960c77bcbc1_2.0; cna=8e8c09a50183d281854fa7d6b; Hm_lvt_f0b6b943aec97c3-08cf9b7af-7a545474-144000-189713083f5374; Hm_lpvt_f0b6b943aec9775d7c6c7020bf856c6b=1689821277; passphtIiwiZXhwIjoxNjg5OTA0NDY3fQ.64QyoVNPuTWZcU3vrH3yfXjhl00VozpYlI5BxrRm0Rw; connect.sid=sroi2kRdMXj0ePe6kWuVAaOhoDOa1I.toE6a4L88Yl%2BhOf8XyhZCwHBwttbzgrhFLO3J5I; CNZZDATA1281120612=491704231-ttps%253A%252F%252Fteacher.hmarted52F%7C1689869515'


"""50s刷新"""
while True:
    res = requests.post(
        url=f"https://core.teacher.vocational.smartedu.cn/p/course/services/member/study/progress?orgId={orgId}",
        headers={
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
                'Content-Length':'202',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':'core.teacher.vocational.smartedu.cn',
                'Cookie':cookie
                 },
        data={
             'courseId': courseId,
             'itemId': itemId,
             'videoId': videoId,
             'playProgress': 1259,  #这个随便写都不影响结果
             'segId': segId,
             'type': 1,
             'tjzj': 1,
             'clockInDot': 1259,  #这个随便写都不影响结果
             'sourceId': sourceId,
             'timeLimit': '-1',
             'originP': 2,
             })

    if json.loads(res.content)['success']:

        print(res.content)

        if eval(json.loads(res.content)["data"]["progress"])==1:
            # bark通知方式 requests.get('https://api.day.app/vLSgUZSwS4jrHcy7VC/完成了')
            print('完成了')
            time.sleep(300)
            break


        print(time.asctime())
        time.sleep(51)

    else:

        print(res.content)
        print(json.loads(res.content)['success'])
        print(type(json.loads(res.content)['success']))
        print("2■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print(time.asctime())
        requests.get('https://api.day.app/vLSvc5LgUZSwS4jrHcy7VC/出错了')
        break

