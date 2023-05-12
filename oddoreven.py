#3.  პროგრამა, რომელიც გვეკითხება რიცხვს და გვიწერს ლუწია თუ კენტი.

def oddOrEven():
    x = int(input("შეიყვანეთ რიცხვი:"))
    if x % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"


print(oddOrEven());