import requests
import json
import datetime
import time

#需求：获取朴朴善品信息
class Pupu:
    def __init__(self):
        self.url = ""

    # 定义请求头
    def shop(self):
        url = "http://j1.pupuapi.com/client/search/search_box/products?store_id=7c1208da-907a-4391-9901-35a60096a3f9&search_term=%E7%89%9B%E5%A5%B6&sort=0&search_term_from=40&place_id=e526a466-55e2-4ff4-86f8-2c5142c2f9a5&place_zip=350102&page=1&size=20"
        headers = {
            "Host": "j1.pupuapi.com",
            "Connection": "keep-alive",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            "sign" : "ac02eaf6d35a4d522163b7ecd9a70afe",
            "pp-os": "0",
            "timestamp" : "1647271072679",
            "pp-placeid": "e526a466-55e2-4ff4-86f8-2c5142c2f9a5",
            "pp-version": "2021061900",
            "pp_storeid": "7c1208da-907a-4391-9901-35a60096a3f9",
            "content-type": "application/json",
            "open-id": "oMwzt0Hj0cdix7ZvboJO6o47KZ8s",
            "Referer": "https://servicewechat.com/wx122ef876a7132eb4/155/page-frame.html"
        }

        # 发起请求，接受响应
        # 跳过证书
        response = requests.get(url=url,headers=headers,verify=False)
        pupu = json.loads(response.content.decode()) #转换json格式

        #抓取需要的信息
        title = pupu['data']['products'][0]['sub_title']  # 商品详情
        name = pupu['data']['products'][0]['name']  # 商品名
        spec = pupu['data']['products'][0]['spec']  # 商品规格
        price = pupu['data']['products'][0]['price'] / 100  # 折扣价
        price_guide = pupu['data']['products'][0]['price_guide'] / 100  # 原价



        #输出规格
        print("--------------商品:"+name+"--------------")
        print("商品规格:",spec)
        print("价格:",price)
        print("原价/折扣价:",str(price_guide)+"/"+str(price))
        print("商品详情:",title)
        print('------------"'+name+'"的价格波动------------')

        #循环10次，每3秒输出一次
        for i in range(0,10,1):
            price = pupu['data']['products'][0]['price'] / 100  # 折扣价
            print("当前时间为:", self.timeshop(), "价格为", price)
            time.sleep(3)

    def timeshop(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#时间输出格式


    def run(self):
        self.shop()
if __name__ == '__main__':
    Pupu().run()












