n = int(input().strip())
for n in range(1,101):
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
