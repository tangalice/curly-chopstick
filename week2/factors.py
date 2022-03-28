class Factors:
    def __init__(self):
        self.factors = []

    def __call__(self,number):
        for value in range(1, number + 1):
            if number % value == 0:
                self.factors.append(value)
        return self.factors

def tester():
    n = int(input("What number do you want to find the factors of? "))
    fac_of = Factors()
    print(fac_of(n))

if __name__ == "__main__":
    tester()