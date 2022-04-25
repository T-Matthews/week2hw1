#Question 1 Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
i=1
number=0
while number**3<1000:
    number+=1
    print(number**3)







#QUESTION 2: Get first prime numbers up to 100

for num in range (1, 101):
    flag = 0
    for i in range(2, num):
        if(num % i == 0):
            flag = flag + 1
            break

    if (flag == 0 and num != 1):
        print(num, end = ' ')
          






#QUESTION 3: Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
print("\n\n")
try:
    age=int(input('Please put in your age!'))
    if age<18:
        print("You\'re still just a kid!")
    elif age<65:
        print('You\'re now an adult!')
    else:
        print('You\'re getting up there old timer!')
except:
    print("That didn\'t seem to work! You should know what a number is by now!")