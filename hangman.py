import random


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game(user_word, no_of_tries, used_letters):
    print()
    print(user_word)
    print("Trial remained: ", no_of_tries)
    print("Letters used: ", used_letters)
    print()


def play_game(no_of_tries):
    used_letters = []
    while True:
        while True:
            letter = input("Enter a letter: ")

            if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                if letter not in used_letters:
                    break
                else:
                    print("The letter has already been used")
            else:
                print("The letter is supposed to be")


        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("There is no such letter")
            no_of_tries -= 1

            if no_of_tries == 0:
                return "Game over"
        else:
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                return "Nice"

        show_state_of_game(user_word, no_of_tries, used_letters)

        print("Letters used:", used_letters)


while True:
    choice = 1
    while True:
        choice = input("Difficulty levels: 1.Easy, 2. Medium, 3. Hard")
        if choice not in ('1', '2', '3'):
            print("Not an appropriate choice.")
        else:
            choice = int(choice)
            break
    no_of_tries = choice * 5
    print(no_of_tries)
    words = ["kamila", "piatek", "niedziela", "obiad"]
    word = random.choice(words)
    user_word = []
    for _ in word:
        user_word.append("_")
    print(word)
    wynik = play_game(no_of_tries)
    print("Result ", wynik)
    play_again = input('Play again? y/n: ') == 'y'
    if not play_again:
        break




