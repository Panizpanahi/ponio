answer = int(input(""))
is_correct = False
try_count = 0


while try_count < 10 and is_correct == False:
    guess = int(input())
    if guess == answer:
        print("you won")
        is_correct == True
    elif guess > answer:
        print(" it's greater")
        try_count += 1
    else:
        print("it's smaller")
        try_count += 1
    is_correct == False
    print("lost")
