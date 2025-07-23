import requests
import json
from time import sleep
from random import randint
from pool import XieChengAccountPool

class xiechengCrawler:
    def __init__(self):
        self.account_pool = XieChengAccountPool()
        self.json_data = {
            'search': {
                'checkIn': '20250513',
                'checkOut': '20250514',
                'hotelId': 121013047,
                'subHotelId': '121013047',
                'roomId': 0,
                'fixSubhotel': 0,
                'priceType': 2,
                'adult': 1,
                'childInfoItems': [],
                'roomQuantity': 1,
                'mustShowRoomList': [],
                'location': {
                    'geo': {
                        'cityID': 1,
                    },
                },
                'cancelPolicyType': 0,
                'isFirstEnterDetailPage': 'T',
                'extras': {},
                'filters': [],
                'isUserSelectCheckInOut': 'T',
                'hotelUniqueKey': '',
                'hasAidInUrl': False,
                'abResultEntities': [
                    {
                        'key': '240605_IBU_pricH',
                        'value': 'B',
                    },
                ],
                'tripSub1': '',
                'preSaleInfo': {
                    'productId': 0,
                    'nights': 0,
                    'productUseStartDate': '',
                },
                'residenceCode': 'CN',
            },
            'genk': True,
            'head': {
                'platform': 'PC',
                'cver': 'hotels',
                'ctok': '',
                'cid': '09031167313397232673',
                'bu': 'HBU',
                'group': 'ctrip',
                'syscode': '09',
                'aid': '4902',
                'sid': '22921635',
                'ouid': '',
                'locale': 'zh-CN',
                'timezone': '8',
                'currency': 'CNY',
                'pageId': '102003',
                'vid': '1747100446387.a7a8My4kdysO',
                'guid': '09031167313397232673',
                'isSSR': False,
            },
            'ServerData': '',
        }

    def crawl_room(self, hotel_id):
        # json_data["search"]["hotelId"] = hotel_id
        # json_data["search"]["subHotelId"] = hotel_id

        response = requests.post(
            'https://m.ctrip.com/restapi/soa2/33278/json/getHotelRoomListInland',
            cookies={
                "cticket": self.account_pool.get_cookie()["cticket"]
            },
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
            },
            json=self.json_data,
        )
        print(response.json())
    
        """返回json"""
        keys_list_physicRoomMap = ["hotel_id", "room_id", "room_name", "pictureInfo_list",
                                   "facility_dict", "bed_title", "BedInfo_overall", "windowInfo_title", "smokeInfo_title",
                                   "areaInfo_title", "floorInfo_title", "wifiInfo_title"]
        keys_list_saleRoomMap = ["saleRoom_id", "bookingStatusInfo_isBooking",
                                 "bookingStatusInfo_isFullRoom", "meal_overall", "cancelInfo_title", "guestCount",
                                 "childCount", "price", "deletePrice", "promotionItem_list", "discount_title",
                                 "priceLabe_list", "rpInfos"]
    
        data_all = []
        physicRoomMaps = response.json().get("data", {}).get("physicRoomMap", [])
    
        """physicRoomMap层>>>"""
        for physicRoomMap in physicRoomMaps.values():
            physicRoomMap_list = []
            """房间信息数据"""
            # --3.房间id  room_id
            room_id = physicRoomMap.get("id", "None")
            # 将酒店的id和名称装进去（每个房间都装）
            physicRoomMap_list.append(hotel_id)
    
            physicRoomMap_list.append(room_id)
            # --4.房间名称  room_name
            room_name = physicRoomMap.get("name", "None")
            physicRoomMap_list.append(room_name)
            # --5.房间图片  pictureInfo_list
            pictureInfo_list = []
            pictureInfos = physicRoomMap.get("pictureInfo", [])
            for pictureInfo in pictureInfos:
                pictureInfo_list.append(pictureInfo.get("url", "None"))
            physicRoomMap_list.append(pictureInfo_list)
            """设施"""
            faciltityInfos = physicRoomMap.get("faciltityInfo", {}).get("list", [])
            # --6.设施字典  facility_dict
            facility_dict = {}
            for facilityInfo in faciltityInfos:
                title = facilityInfo.get("title", "None")
                subList = facilityInfo.get("subList", [])
                small_title_list = []
                for sub in subList:
                    small_title = sub.get("title", "None")
    
                    additionInfos = sub.get("additionInfo", [])
                    infoContent_list = []
                    for additionInfo in additionInfos:
                        infoContent = additionInfo.get("infoContent", "None")
                        infoContent_list.append(infoContent)
                    # 组装小标签
                    if len(infoContent_list) != 0:
                        small_title_overall = f"{small_title}({'、'.join(infoContent_list)})"
                    else:
                        small_title_overall = small_title
                    small_title_list.append(small_title_overall)
    
                facility_dict[title] = small_title_list
            physicRoomMap_list.append(facility_dict)
            """床"""
            bedInfo = physicRoomMap.get("bedInfo", {})
            # --7.床标题  bed_title
            bed_title = bedInfo.get("title", "None")
            physicRoomMap_list.append(bed_title)
            # --8.床信息  BedInfo_overall
            BedInfo_dict = {}
            BedInfo_title = bedInfo.get("title", "None")
            cpxBedInfo = bedInfo.get("cpxBedInfo", {})
            cpxBedInfo_title = cpxBedInfo.get("title", "None")
            bedDetails = cpxBedInfo.get("bedDetail", [])
            bedDetail_list = []
            for bedDetail in bedDetails:
                roomName = bedDetail.get("roomName", "None")
                details = bedDetail.get("detail", [])
                # 组装卧室信息
                if len(details) != 0:
                    room_overall = f"{roomName}({'、'.join(details)})"
                else:
                    room_overall = roomName
                bedDetail_list.append(room_overall)
    
            BedInfo_dict[cpxBedInfo_title] = bedDetail_list
            if BedInfo_dict:
                BedInfo_overall = f"{BedInfo_title}({BedInfo_dict})"
            else:
                BedInfo_overall = BedInfo_title
            physicRoomMap_list.append(BedInfo_overall)
            """告知信息"""
            # --9.窗户信息  windowInfo_title
            windowInfo_title = physicRoomMap.get("windowInfo", {}).get("title", "None")
            physicRoomMap_list.append(windowInfo_title)
            # --10.禁烟信息 smokeInfo_title
            smokeInfo_title = physicRoomMap.get("smokeInfo", {}).get("title", "None")
            physicRoomMap_list.append(smokeInfo_title)
            # --11.房间面积  areaInfo_title
            areaInfo_title = physicRoomMap.get("areaInfo", {}).get("title", "None")
            physicRoomMap_list.append(areaInfo_title)
            # --12.楼层信息 floorInfo_title
            floorInfo_title = physicRoomMap.get("floorInfo", {}).get("title", "None")
            physicRoomMap_list.append(floorInfo_title)
            # --13.wifi信息 wifiInfo_title
            wifiInfo_title = physicRoomMap.get("wifiInfo", {}).get("title", "None")
            physicRoomMap_list.append(wifiInfo_title)
    
            # 将这个房间的physicRoomMap层数据变成list装进字典中
            dict_physicRoomMap = {key: value for key, value in zip(keys_list_physicRoomMap, physicRoomMap_list)}
            dict_physicRoomMap_json = {"basicInfo": dict_physicRoomMap}
            data_all.append(dict_physicRoomMap_json)
    
        """saleRoomMaps层>>>"""
        saleRoomMaps = response.json().get("data", {}).get("saleRoomMap", [])
        for saleRoom_id, saleRoomMap in saleRoomMaps.items():
            # 装saleRoomMaps层所有值
            saleRoomMap_list = []
            # 房间id（房间顺序与上一个循环不一样，需要对比房间id来分配数据）
            sale_room_id = saleRoomMap.get("physicalRoomId", "None")
            for data in data_all:
                if data.get("basicInfo").get("room_id") == sale_room_id:
                    data_json = data
    
            # --14.saleRoom_id
            saleRoom_id = saleRoom_id.split("_")[1]
            saleRoomMap_list.append(saleRoom_id)
            # --15.房间是否可以预定  bookingStatusInfo_isBooking
            bookingStatusInfo_isBooking = saleRoomMap.get("bookingStatusInfo", {}).get("isBooking", "None")
            saleRoomMap_list.append(bookingStatusInfo_isBooking)
            # --16.房间是否满了  bookingStatusInfo_isFullRoom
            bookingStatusInfo_isFullRoom = saleRoomMap.get("bookingStatusInfo", {}).get("isFullRoom", "None")
            saleRoomMap_list.append(bookingStatusInfo_isFullRoom)
            # --17.餐食信息  meal_overall
            mealInfo = saleRoomMap.get("mealInfo", {})
            mealInfo_title = mealInfo.get("title", "None")
            mealInfo_hover = mealInfo.get("hover", [])
            # 组装餐食信息
            if len(mealInfo_hover) != 0:
                meal_overall = f"{mealInfo_title}({'、'.join(mealInfo_hover)})"
            else:
                meal_overall = mealInfo_title
            saleRoomMap_list.append(meal_overall)
            # --18.取消预定信息 cancelInfo_title
            cancelInfo_title = saleRoomMap.get("cancelInfo", {}).get("title", "None")
            saleRoomMap_list.append(cancelInfo_title)
            # --19.可入住成年人数量 guestCount
            guestCount = saleRoomMap.get("guestCountInfo", {}).get("guestCount", "None")
            saleRoomMap_list.append(guestCount)
            # --20.可入住儿童数量 childCount
            childCount = saleRoomMap.get("guestCountInfo", {}).get("childCount", "None")
            saleRoomMap_list.append(childCount)
            # --21.金额（现价） price
            price = saleRoomMap.get("priceInfo", {}).get("price", "None")
            saleRoomMap_list.append(price)
            # --22.金额（原价） deletePrice
            deletePrice = saleRoomMap.get("priceInfo", {}).get("deletePricewithOutCurrency", "None")
            if deletePrice == 0:
                deletePrice = "None"
            saleRoomMap_list.append(deletePrice)
            # --23.打折信息 promotionItem_list
            promotionItems = saleRoomMap.get("totalPriceInfo", {}).get("promotionItems", [])
            promotionItem_list = []
            for promotionItem in promotionItems:
                promotionItem_title = promotionItem.get("title", "None")
                promotionItem_content = promotionItem.get("content", "None")
                promotionItem_list.append(promotionItem_title + promotionItem_content)
            saleRoomMap_list.append(promotionItem_list)
            # --24.打折标题 discount_title
            if deletePrice != "None" and price != "None":
                discount_title = round(price / deletePrice, 2)
            else:
                discount_title = "None"
            saleRoomMap_list.append(discount_title)
            # --25.特惠一口价
            priceLabe_list = []
            priceLabes = saleRoomMap.get("priceLabelList", [])
            for priceLabe in priceLabes:
                priceLabe_list.append(priceLabe.get("text", "None"))
            saleRoomMap_list.append(priceLabe_list)
            # --26."一张床位"
            rpInfo_list = []
            rpInfos = saleRoomMap.get("rpInfos", [])
            for rpInfo in rpInfos:
                rpInfo_title = rpInfo.get("title", "None")
                rpInfo_list.append(rpInfo_title)
            saleRoomMap_list.append(rpInfo_list)
    
            # 将对应房间的saleRoomMaps层数据装进字典中
            dict_saleRoomMap = {key: value for key, value in zip(keys_list_saleRoomMap, saleRoomMap_list)}
            if data_json.get("roomInfo"):
                data_json.get("roomInfo").append(dict_saleRoomMap)
            else:
                data_json["roomInfo"] = [dict_saleRoomMap]
            # 更换对应data_all中对应房间的数据
            for index in range(len(data_all)):
                if data_all[index].get("basicInfo").get("room_id") == sale_room_id:
                    data_all[index] = data_json
    
        # 将data_all中所有房间数据按照价格排序
        data_all = sorted(data_all, key=lambda x: x.get("roomInfo", [])[0].get("price", 10000000))
    
        return data_all
        
    def main(self):
        with open('hotel_info.json', 'r', encoding='utf-8') as f:
            hotel = json.load(f)  # 用获取到的酒店id获取酒店下的所有房型

        hotel_room_info = []

        for hotel in hotel:
            hotel_id = hotel.get("酒店id") # 先获取酒店id再获取酒店下的所有房型
            try:
                json_data["search"]["hotelId"] = int(hotel_id)
                json_data["search"]["subHotelId"] = hotel_id
                data_all = crawl_room(int(hotel_id))
                hotel_room_info.append(data_all)
                with open(f"hotel_room_data1.json", 'w', encoding='utf-8') as f:
                    json.dump(hotel_room_info, f, ensure_ascii=False, indent=4)
                sleep(randint(10, 30))  # 随机等待10到30秒
            except Exception as e:
                print(f"爬取酒店ID: {hotel_id} 的房间数据时发生错误：{e}")
                continue



if __name__ == '__main__':
    crawler = xiechengCrawler()
    crawler.main()