from random import randint

eleven = 11
randNum = randint(0, 20)

if eleven > randNum:
    print("{} is greater than {}".format(eleven, randNum))
else:
    print("{} is smaller than {}").format(eleven, randNum)