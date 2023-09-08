from django.shortcuts import render
from random import shuffle

c_i_MAX_GUESS = 10
c_i_NUM_DIGITS = 3

def about(request):
    return render(request, 'bagels_game/index.html')

def bagels_game(request):
    # Lấy số bí mật
    secret_number = f_GetSecretNum()

    # Khởi tạo biến cho trạng thái trò chơi
    game_over = False
    clues = []
    guess_count = 0

    # Xử lý dữ liệu người dùng khi họ gửi form
    if request.method == 'POST':
        user_guess = request.POST.get('user_guess', '')
        guess_count += 1

        # Xử lý đoạn code kiểm tra đoán đúng/sai ở đây và thêm vào biến clues

        if user_guess == secret_number:
            # Xử lý khi đoán đúng
            game_over = True
            clues.append('That is a correct answer. Lucky guess! 🎉')
        else:
            # Xử lý khi đoán sai
            clues.append(f_GetClue(secret_number, user_guess))

        if guess_count >= c_i_MAX_GUESS:
            # Xử lý khi người chơi hết lượt đoán
            game_over = True
            clues.append(f'The answer is: {secret_number}')
            clues.append('You ran out of guesses. Better luck next time! 😔')

    # Render template HTML và truyền dữ liệu cần thiết
    return render(request, 'bagels_game/bagels_game.html', {
        'game_over': game_over,
        'clues': clues,
        'guess_count': guess_count,
    })

def f_GetSecretNum():
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

def f_GetClue(secret_num, user_guess):
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