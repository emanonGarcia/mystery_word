import random
import string

MAX_GUESSES = 8


def lets_play():
    answer = input("Let's play: [Y]es or [N]o ")
    if answer.lower() == 'y':
        print_game_title()
        return True
    elif answer.lower() == 'n':
        print("Maybe next time...")
        exit()
    else:
        lets_play()
        return True


def get_mystery_word(lower, upper):
    with open("/usr/share/dict/words", 'r') as f:
        word_bank = [word.strip() for word in f if len(word.strip()) >= lower and len(word.strip()) <= upper]
    rand_word = random.choice(word_bank)
    print('''\nWith {} words to play, I'll pick a one at random.
    Your word is {} letters long'''.format(len(word_bank), len(rand_word)))

    return(rand_word.upper())


def easy_mode():
    word = get_mystery_word(4, 6)
    game_core(word)


def normal_mode():
    word = get_mystery_word(6, 8)
    game_core(word)


def hard_mode():
    word = get_mystery_word(8, 45)
    game_core(word)


def mystery_word_game():

    if lets_play():
        user_input = input("Pick a mode. [E]asy, [N]ormal, [H]ard: ")
        user_input = user_input.lower()
        if user_input == 'e':
            easy_mode()
        elif user_input == 'n':
            normal_mode()
        elif user_input == 'h':
            hard_mode()
        else:
            print("Doesn't match a difficulty. Bye!")
    exit()


def print_game_title():
    print('''
    ###################################################
    #                  "Mystery Word"                 #
    ###################################################
    ''')
    return


def is_correct(correct_guesses, mystery_word):
    m_list = [letter for letter in set(mystery_word)]
    correct_guesses.sort()
    m_list.sort()

    return correct_guesses == m_list


def victory(guess_count, mystery_word):
    print("\n" + "*" * 20)
    print("YOU GOT IT!")
    print("The mystery word was {}".format(mystery_word))
    print("It only took you {} guess(es)".format(guess_count))
    print("Game Over")
    print("*" * 20 + '\n')

    mystery_word_game()


def display_guesses(correct_guesses, wrong_guesses):
    print("\nWrong guesses: {}".format(wrong_guesses))


def print_guess_count(num_of_guesses):
    print("\nAttempt: {0}/8".format(num_of_guesses))


def get_user_guess():
    next_try = input("\nGuess a letter: ")
    return next_try.upper()


def game_core(mystery_word='HELP'):
    guess_count = 1
    correct_guesses = []
    wrong_guesses = []

    len_of_mystery = len(mystery_word)
    mystery_list = ['_ '] * ((len_of_mystery)-1) + ['_']

    while guess_count <= MAX_GUESSES:
        print(''.join(mystery_list))
        print_guess_count(guess_count)
        display_guesses(correct_guesses, wrong_guesses)
        user_guess = get_user_guess()

        mystery_list = [user_guess if letter == user_guess else blank for blank, letter in zip(mystery_list, mystery_word)]

        if len(user_guess) == 1 and user_guess in string.ascii_letters:
            if user_guess in mystery_word and user_guess not in correct_guesses:
                print("Great guess!\n")
                correct_guesses.append(user_guess)
            elif user_guess not in mystery_word and user_guess not in wrong_guesses:
                print("Nope, guess again\n")
                guess_count += 1
                wrong_guesses.append(user_guess)
            else:
                print("You guessed that already...")
                continue
        else:
            print("Opps, let's try again..")
            continue

        if is_correct(correct_guesses, mystery_word):
            victory(guess_count, mystery_word)

    print("\nThe mystery word was {}".format(mystery_word))
    print("All out of guesses. Game over")


def main():
    mystery_word_game()


if __name__ == '__main__':
    main()
