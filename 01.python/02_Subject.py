"""
과제 02. 조직도 만들기
"""

class Human:
    def __init__(self, name, age, gender, rank):
        self.name = name
        self.age = age
        self.gender = gender
        self.rank = rank

class Worker(Human):
    # rank = "대리"
    rank = ()


workers = Worker("임승현", "24살", "남자", "대리")

print(workers.name)
print(workers.age)
print(workers.gender)
print(workers.rank)
