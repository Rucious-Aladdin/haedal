class crytocurrency:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print("화폐이름: ", self.name)
        print("현재 가격: ", self.price, "원")
        print("")



currency1 = crytocurrency("비트코인", 71038000)
currency2 = crytocurrency("이더리움", 5014940)
currency3 = crytocurrency("라이트코인", 486900)
currency4 = crytocurrency("비트코인캐시", 1827000)
currency5 = crytocurrency("이오스", 12920)

currency1.info()
currency2.info()
currency3.info()
currency4.info()
currency5.info()
