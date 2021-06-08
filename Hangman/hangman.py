import random
import string

words = []
with open("words.txt", "r") as f:
    for line in f.readlines():
        words.append(line.strip().upper())

def hangman():
    word = random.choice(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        print("You have used these letters: ", ' '.join(used_letters))
        print("Remaining Lives:", lives)

        guess_letter = input("Enter guess: ").upper()

        if guess_letter in alphabets-used_letters:
            used_letters.add(guess_letter)

            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
                print("Good one! Keep Going\n")
            else:
                lives = lives-1
                print("Oops! Letter not in word. Try Again..\n")

        elif guess_letter in used_letters:
            print("Already used! Try Again...\n")

        else:
            print("Invalid input. Try Again...\n")

    if lives == 0:
        print("Sorry, You couldn't guess it. The correct word is", word, "\n")
    else:
        print("Congrats! You guessed it right. The correct word is", word, "\n")


if __name__=="__main__":
    while True:
        hangman()
        again = input("Play again?\nPress y to continue, any other key to exit\n").upper()
        if again != 'Y':
            print('Thanks for playing, see you next time.')
            break
