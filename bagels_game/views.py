from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from random import shuffle

c_i_MAX_GUESS = 10
c_i_NUM_DIGITS = 3

def index(request):
    return render(request, 'bagels_game/index.html')


def bagels_game(request):
    if 'game_data' not in request.session:
        request.session['game_data'] = {
            's_answer': getSecretNum(),
            'str_Clues': '',
            'time_guess': 1,
            'guesses': [],  # Initialize the list of guesses
        }

    game_data = request.session['game_data']

    if request.method == 'POST':
        if 'reset' in request.POST:
            # Reset the game data, including the list of guesses
            request.session['game_data'] = {
                's_answer': getSecretNum(),
                'str_Clues': '',
                'time_guess': 1,
                'guesses': [],
            }
            return render(request, 'bagels_game/bagels_game.html', {'message': 'Game has been reset.'})

        user_guess = request.POST.get('userGuess')
        s_answer = game_data['s_answer']
        str_Clues = getClue(s_answer, user_guess)

        if user_guess == s_answer:
            message = f'Congratulations! You guessed the correct number: {s_answer}'
        elif game_data['time_guess'] >= c_i_MAX_GUESS:
            message = f'Game over. The correct answer was: {s_answer}'
        else:
            message = f'Guess {game_data["time_guess"]}: {user_guess} - {str_Clues}'

        # Cập nhật danh sách guesses
        game_data['guesses'].append(f'Guess {game_data["time_guess"]}: {user_guess} - {str_Clues}')
        game_data['str_Clues'] += str_Clues + '\n'
        game_data['time_guess'] += 1
        request.session.modified = True

        context = {
            'userGuess': user_guess,
            'timeGuess': game_data['time_guess'],
            'message': message,
            'str_Clues': game_data['str_Clues'],
            'guesses': game_data['guesses'],
        }
        return render(request, 'bagels_game/bagels_game.html', context)
    else:
        return render(request, 'bagels_game/bagels_game.html')


def getSecretNum():
    numbers = list('0123456789')
    shuffle(numbers)
    result = ''
    for i in range(c_i_NUM_DIGITS):
        result += str(numbers[i])
    return result

def getClue(secret_num, user_guess):
    clue = []
    if user_guess == secret_num:
        return 'That is a correct answer. Lucky guess!'
    for i in range(len(user_guess)):
        if user_guess[i] == secret_num[i]:
            clue.append('Fermi')
        elif user_guess[i] in secret_num:
            clue.append('Pico')
    if len(clue) == 0:
        return 'The clue for you is: Bagels'
    clue.sort()
    return 'The clue for you is: ' + ', '.join(clue)
