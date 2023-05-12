#8.  პროგრამა, რომელიც შეგვეკითხება ორ რიცხვს და დაწერს მათ უდიდეს საერთო გამყობს.

def greatestCommonDivisor():
    x = int(input("პირველი რიცხვი:"))
    y = int(input("მეორე რიცხვი:"))

    for i in range(min(x,y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
    return None


print(greatestCommonDivisor())