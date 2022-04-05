class Factors:
    def __init__(self):
        self.factors = []

    def __call__(self,number):
        for value in range(1, number + 1):
            if number % value == 0:
                self.factors.append(value)
        return self.factors

def factester():
  #if user wanted to input their own numbers
    #n = int(input("What number do you want to find the factors of? 
  #print(fac_of(n))

  #tester numbers
    fac_of = Factors()
    print("Tester Number: 56")
    print(fac_of(56))
    print("Tester Number: 128")
    print(fac_of(128))
    print("Tester Number: 1024")
    print(fac_of(1024))

if __name__ == "__main__":
    factester()