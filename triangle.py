def triangle(): 
    a = int(input("პირველი გვერდი:"))
    b = int(input("პირველი გვერდი:"))
    c = int(input("პირველი გვერდი:"))
    
    if a+b > c and (a+c) > b and b+c > a:
        return "შესაძლებელია სამკუთხედის აგება"
    else:
        return "შეუძლებელია სამკუთხედის აგება"