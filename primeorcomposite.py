#9.  პროგრამა, რომელიც გვეკითხება რიცხვს და ამოწმებს მარტივია თუ რთული. შედეგი უნდა დაწეროს ეკრანზე.



def primeOrComposite():
    x = int(input("შეიყვანეთ რიცხვი:"))

    if x < 2:
        return "არც მარტივია და არც შედგენილია"

    for i in range(2, x):
        if x % i == 0:
            return "შედგენილია"
    
    return "მარტივია"

print(primeOrComposite())
