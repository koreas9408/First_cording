# # 사용자로 부터 입력을 받는다
#
# # 문자형태의 입력값을 정수형으로 변환
# # 10이상의 입력 제한하기
# while True:
#     num1 = int(input("몇 단을 출력하시겠습니까? (최대 9단)"))
#     num1 >= 10;
#      break
# # 1부터 9까지 반복
# for num2 in range (1, 10):
#     result = num1 * num2
#     print("{} * {} = {}".format(num1, num2, result))

# -----------------while 문은 나중에...------------------------
# #사용자로부터 입력받기
# num1 = int(input("출력할 구구단을 입력하세요/ 최대 9단 : "))
# # 제어문 생성 조건은 10이상의 수를 입력시
# if num1 >= 10:
#     num1 = int(input(" 10미만의 구구단만 출력이 가능합니다."))
# # 또 다른 조건으로 10 미만의 수를 입력시
# elif num1 < 10:
#     for num2 in range (1,10):
#         result = num1 * num2
#         print("{} * {} = {}".format(num1, num2, result)) # 출력

num1 = int(input("출력할 구구단을 입력하세요/ 최대 9단 : "))
if num1 < 10 :
    for num2 in range (1,10):
             result = num1 * num2
             print("{} * {} = {}".format(num1, num2, result))
elif num1 >= 10 :
    while num1 < 10 :
        int(input("10 미만의 구구단만 출력이 가능합니다. : "))
