import time
#你好 我的名字是FOOD 一個點餐機器人
#很高興為您服務
#**請問還有空位嗎？**
#有的 請問幾位用餐？
#**4**位大人
#好的*4*位 裡面請


print("你好我的名子是FOOD 一個點餐機器人")
print("很高興為您服務")

sit=input("")

while True:
    peoplo=input("有的 請問幾位用餐？\n")
    if int(peoplo)==4:
        break
    else:
        print("請回答4")



print("好的",peoplo,"位 裡面請")

#今天要吃什麼？
#**兩份義大利麵跟兩份燉飯**
#**義大利麵**會辣可以接受嗎？
#**請幫我把辣椒去掉**
#好的 飲料需要嗎？
#**開水 謝謝**

food=input("今天要吃什麼？\n")

print(food,"會辣可以接受嗎？")

spicy=input("")

drink=input("好的 飲料需要嗎？")
for i in range(1,10) :
    time.sleep(1)
    print(".")
    if i==5:
        print("用餐中")


#這邊幫您做買單
#**這樣總共多少錢？**
#今天消費620加上一成服務費 一共是682元
#**可以刷卡嗎？**
#只收現金喔
#那今天餐點合您胃口嗎？
#還不錯

how_much=input("這邊幫你做買單\n")

print("今天消費620加上一成服務費 一共是682元")

pay=input("")

print("只收現金喔")

taste=input("那今天餐點合您胃口嗎？\n")


#謝謝 歡迎下次光臨
#謝謝


print("謝謝 歡迎下次光臨")