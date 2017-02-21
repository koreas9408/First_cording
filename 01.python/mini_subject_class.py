######## 미니과제 두번째 class 만들기

class School:
    def __init__(self, name, birth, address):
        self.name = name #이름
        self.birth = birth #설립연도
        self.address = address #주소

school1 = School("동양미래 대학교", "1939년 4월 1일", "서울시 구로구")
print(school1.name)
school2 = School("회룡초등학교", "1995년 11월 1일", "경기도 의정부시")
print(school2.birth)
