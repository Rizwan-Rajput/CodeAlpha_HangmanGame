import random
words = ["Rizwan", "Hameed", "Ahmed","Hammad"]
word = random.choice(words).lower()
guesses = ["-"] * len(word)
max_attempts = 5
attempts = 0
print("Welcome to the Hangman Game")
while "-" in guesses and attempts < max_attempts:
    print("-".join(guesses))
    guessed_letter = input("Guess a letter: ")
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter")
        continue

    if guessed_letter in guesses:
        print("You already guessed this letter")
        continue


    if guessed_letter in word:
        for i in range(len(word)):
            if word[i] == guessed_letter:
                guesses[i] = guessed_letter

    else:
         print("Wrong guess! ")
         attempts += 1
         print("Remaining attempts are ", max_attempts - attempts)



if "-" not in guesses:
    print("Congratulations! You guessed the word")
    print("The word is", word)
else:
    print("Sorry, you failed to guess the word")
    print("The word was", word)