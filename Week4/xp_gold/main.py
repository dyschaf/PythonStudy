import random
# from signal import pause
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']


def get_word():
    word = random.choice(wordslist)
    word.upper()
    return word.upper()


def play(word):
    print(word)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the world")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i,  letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("you already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a vailid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats, you guess the right word! You win")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
