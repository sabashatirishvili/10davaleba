#10.  პროგრამა, რომელიც გვეკითხება რიცხვების სიას და დაწერს მათ შორის მაქსიმალურს და მინიმალურს.

def minmax():
    x = input("შეიყვანეთ რიცხვების სია, გამოყავით ადგილებით:")
    numbers = list(map(int,x.split(" ")))
    minimum = min(numbers)
    maximum = max(numbers)

    return f"მაქსიმალური: {maximum} \n მინიმალური: {minimum}"

print(minmax())