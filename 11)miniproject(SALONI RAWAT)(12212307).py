import random as r
a='Y'
while a.upper()=='Y' or a.upper()=='YES':
    print('Enter the range between which you want to check number')
    start=int(input('Start : '))
    end=int(input('End : '))
    rand_no=r.randint(start,end)
    print('Randomly selected number is ',rand_no,', and its properties are : ')
    if rand_no>0:
        print(rand_no,'is a positive number')
    else:
        print(rand_no,'is a negative number')
    if rand_no%2==0:
        print(rand_no,'is an even number')
    else:
        print(rand_no,'is an odd number')
    count=0
    for i in range(2,rand_no):
        if rand_no==2:
            count=0
        else:
            if rand_no%i==0:
                count=count+1
    if count>0:
        print(rand_no,'is a composite number')
    else:
        print(rand_no,'is a prime number')
    a=input('Do you want to check more number Y/N : ')
