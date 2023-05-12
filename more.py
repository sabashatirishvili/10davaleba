#4.  პროგრამა, რომელიც გვეკითხება ორ რიცვს და გვიწერს, რომელია მეტი.

def moreOrLess():
    x = int(input("პირველი რიცხვი:"))
    y = int(input("მეორე რიცხვი:"))
    if x > y:
        return f"{x} მეტია {y}-ზე"
    elif x < y:
        return f"{y} მეტია {x}-ზე"
    else: 
        return f"{x} და {y} ტოლია"
    

print(moreOrLess())