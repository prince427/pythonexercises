import itertools
import time

Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.")
Password = input("What is your password?\n")

start = time.time()

counter = 1
CharLength = 1

for CharLength in range(25):
    passwords = (itertools.product(Alphabet, repeat= CharLength))
    print("\n \n")
    print("currently working on passwords with ", CharLength, " chars")
    print("It has been ", time.time() - start, " seconds!")
    print("We have tried ", counter, " possible passwords!")
    for i in passwords:
        counter += 1
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        if i == Password:
            end = time.time()
            timetaken = end - start
            print("Found it in ", timetaken, " seconds and ", counter, "attempts")
            print(i)
            input("Press enter when you have finished")
            exit()

