from random import shuffle

# Game setting
c_i_MAX_GUESS = 10
c_i_NUM_DIGITS = 3

# Main fx of the game
def main() -> None:
    print(f'''\n
            BAGELS, A BULLSHIT GAME, by HaTuongNguyen hatuongnguyen0107@hcmut.edu.vn, 
            Reference-based on "The big book of small Python projects" - AL SWEIGART

            I'm thinking of a {c_i_NUM_DIGITS}-digit number from 0 to 9 with NO REPEATED DIGITS.
            Try to guess what it is. 

            Here are some clues:
            When I say:    That means:
              Pico😮       One digit is correct but in the wrong position.
              Fermi🤙      One digit is correct and in the right position.
              Bagels🥲     No digit is correct.

            For example, if the secret number was 248 and your guess was 843, the
            clues would be Fermi Pico.\n''')
    # Main loop of the game
    while True:

        # Create a secret number
        s_answer = getSecretNum()

        # Create a value for increment
        i_timeGuess = 1

        # Keyboard Interrupt
        try:
            # Loop of taking player guess; checking guess; providing clue
            while i_timeGuess <= c_i_MAX_GUESS:
                # Create a blank string for checking datatype
                str_UserGuess = ''

                # Take the guess from player and prevent wrong datatype
                str_UserGuess = validateInput(str_UserGuess, i_timeGuess)

                # Check the guess then show the clue to player
                str_Clues = getClue(s_answer, str_UserGuess)  # Contain the clue

                if str_UserGuess == s_answer:
                    print(str_Clues + "\n")
                    break
                else:
                    print(str_Clues + "\n")
                    # Increase the TimeGuess value: Loop [while i_timeGuess <= c_i_MAX_GUESS:]
                    i_timeGuess += 1

                # If player ran out of guess
                if i_timeGuess > c_i_MAX_GUESS:
                    print(f"The answer is: {s_answer}")
                    print('\nNon cái hand =))')
                    print('Gà vcl🐣🐥🐔\n')

        except KeyboardInterrupt:
            print('U stop the game🛑!')

        # Ask player want to play again?
        if input("📍U want to play again🥰? (yes or no): ").lower().startswith('n'):
            # End of the game
            print('\nWHY U ARE LEAVING MEEEEEEEEEEEEEE🥹👉👈')
            print('BYE BYE🥲\n')
            break

        print("\n🥰🥰🥰YESSSS DADDYYYYYYYY🥰🥰🥰\n")

# Create a fx to make a secret number
def getSecretNum() -> str:
    # Create a list of number
    numbers = list('0123456789')

    # Shuffle the list of number
    shuffle(numbers)

    # Create a black string
    result = ''

    # Take the first three digits added to the black string
    for i in range(c_i_NUM_DIGITS):
        result += str(numbers[i])

    return result

# Create a fx for checking the guess from player
def getClue(secret_num: str, user_guess: str) -> str:
    # Make a black list to contain the clue
    clue = []

    # If the guess from player is correct
    if user_guess == secret_num:
        return '\nThat is a correct answer. Lucky guess😏!'

    # Checking the guess
    for i in range(len(user_guess)):
        # Correct number and index
        if user_guess[i] == secret_num[i]:
            clue.append('Fermi😮')

        # Correct number but wrong index
        elif user_guess[i] in secret_num:
            clue.append('Pico🤙')

    # All answers are wrong
    if len(clue) == 0:
        return '  🔎The clue for U is: Bagels🥲'

    # Sorting the clue list to make the game more difficult
    clue.sort()

    # return clues as a string
    return '  🔎The clue for U is: ' + ' '.join(clue)

def validateInput(user_get: str, time_guess: int) -> str:
    while (len(user_get) != c_i_NUM_DIGITS) or not (user_get.isdecimal()):
        if (len(user_get) == c_i_NUM_DIGITS) or (user_get.isdecimal()):
            print(f"📍Guess {time_guess}")
            user_get = input("  👉")

        else:
            print(f"📍Guess {time_guess}")
            user_get = input("  👉Make sure that U enter {} numbers only: ".format(c_i_NUM_DIGITS))

    return str(user_get)

if __name__ == "__main__":
    main()
