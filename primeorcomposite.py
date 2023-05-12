import math

def primeOrComposite():
    x = int(input("შეიყვანეთ რიცხვი:"))

    if x < 2:
        return "არც მარტივია და არც შედგენილია"

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return "მარტივია"
    
    return "შედგენილია"

print(primeOrComposite())