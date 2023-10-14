class 화연이네붕어빵가게:
    total = 0

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다. 가격은 {self.price}원입니다.")
        화연이네붕어빵가게.total += self.price

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹었습니다.")
        print(f"먹는 붕어빵 종류 : {self.contents}")

슈크림붕어빵 = 화연이네붕어빵가게("슈크림", 1000)
팥붕어빵 = 화연이네붕어빵가게("팥", 1000)
김치붕어빵 = 화연이네붕어빵가게("김치", 1000)

# 판매 함수 호출과 가격 출력
슈크림붕어빵.sell()
슈크림붕어빵.sell()
슈크림붕어빵.sell()

팥붕어빵.sell()
팥붕어빵.sell()
팥붕어빵.sell()

김치붕어빵.sell()
김치붕어빵.sell()
김치붕어빵.sell()

# 모든 붕어빵 객체의 총 판매금 출력
print(화연이네붕어빵가게.total)
