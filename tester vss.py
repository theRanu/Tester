r = 1
p = 2
s = 3
x = 4

import random
while x != 0:
    c = random.randint(1,3)

    x = int(input("Rock Paper or Scissors: rock(1), paper(2), scissors(3)"))
    print (x)
    if x != 1 and x!= 2 and x != 3:
        break
    elif x == c:
        print ("tie")
    elif x == 1 and c == 2 :
        print ("you lose")
    elif x == 2 and c == 3 :
        print ("you lose")
    elif x == 3 and c == 1 :
        print ("you lose")
    elif x == 1 and c == 3 :
        print ("you win")
    elif x == 2 and c == 1 :
        print ("you win")
    elif x == 3 and c == 2 :
        print ("you win")
