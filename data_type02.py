# list [] 목록
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))
# index는 0부터 시작합니다.
# 0,1 이진수로 되어있기 때문에 0이 시작.

print(list_a[0])
print(list_a[1])
print(list_a[2])

# slice 자른다는 의미
print(list_a[0:2])

# append // 새로운 항목을 추가
list_a.append(4)
print(list_a)

# clear //
list_a.clear()
print(list_a)

# remove 지우는 기능
list_a.remove(3)
print(list_a)

tuple (1, )
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type((tuple_a)))
# 튜플은 한번 생성된 값 변경 불가
tuple_a.append(4)

# dict (map) {}
# ket & value
dict_a = {"apple" : "a type of fruits",
"pen" : "a thing to write"}
print(dict_a)
print(dict_a["apple"])
# apple이라는 키를 넣었을때 해당하는 값을 알려줌
dict_a["pen"] = "something to write"
print(dict_a)
# dict 값을 변경 할 때 ;

# set set([]) 집합이라고 생각하면 됨
set_a = set([1, 2, 3, 2])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# ☆☆☆중복이 없다. 중복이 자동 제거.
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)

# 다 외우겠다고 생각하지말고 익숙해 지려고 노력하기.
