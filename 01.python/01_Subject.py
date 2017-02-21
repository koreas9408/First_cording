# 과제.01 맛집 추천하기 !
import random
some = input(" 어떤 맛집을 추천해 드릴까요? (한식, 일식, 중식 중 한곳을 입력하세요.) : ")
list_A = ['김밥천국', '아리솔', '담', '토박이', '남도식당']
list_B = ['중국성', '홍반장', '호화반점', '국빈', '메이탄']
list_C = ['에도긴', '우도', '진스시', '아소산', '긴자']
# menu = random.choice(some)
# print(menu)
# while True:
#     if some == "한식":
#         menu = random.choice(list_1)
#         print(menu)
#         break
#     elif some == "중식":
#         menu = random.choice(list_2)
#         print(menu)
#         break
#     elif some == "일식":
#         menu = random.choice(list_3)
#         print(menu)
#         break
#     else:
#         some = input("다시 입력해주세요! (한식, 중식, 일식) : ")

if some == "한식":
    print(random.choice(list_A))
else:
    if some == "중식":
        print(random.choice(list_B))
    else:
        if some == "일식":
            print(random.choice(list_C))
