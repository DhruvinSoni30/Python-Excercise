number = 9
number_of_guesses = 0
guess_limit = 3
while number_of_guesses < guess_limit:
    guess =  int(input("Guess:"))
    number_of_guesses +=  1
    if guess == number:
        print("You Win!")
        break
else:
    print("You Loose!")   