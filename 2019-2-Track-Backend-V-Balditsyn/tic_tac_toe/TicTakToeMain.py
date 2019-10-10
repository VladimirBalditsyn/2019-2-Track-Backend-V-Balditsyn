import time

from platform import system as system_name  # Returns the system/OS name
from os import system as system_call  # Execute a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower() == "windows" else "clear"

    # Action
    system_call(command)


class TicTacToeGame:
    """
    Main logic of the game
    """

    output_format = '|{0[0]}|{0[1]}|{0[2]}|\n' \
                    '|{0[3]}|{0[4]}|{0[5]}|\n' \
                    '|{0[6]}|{0[7]}|{0[8]}|\n'

    welcome_words = 'Привет!\n' \
                    'Я надеюсь, ты знаешь как играть в крестики-нолики)\n' \
                    'Поэтому найди скорее себе товарища и начинай играть!\n' \
                    'Чтобы сделать ход, тебе достаточно лишь ввести номер\n' \
                    'клетки в соответсвии с таблицой ниже:\n' \
                    '\n{instruction} \n\nУдачи!'\
        .format(instruction=output_format
                .format([str(i + 1) for i in range(9)]))

    win = 'Выйграл {}'
    step = 'Ходит {}'
    first = 'первый\n'
    second = 'второй\n'
    nobody = 'Победила дружба!'
    input_command = 'Введите номер клетки: '
    input_error = 'Так нельзя, попробуй ещё\n'

    def __init__(self):
        print(self.welcome_words)
        time.sleep(5)
        self.array_of_answers = [' ' for i in range(9)]
        clear_screen()
        self.play()

    def you_win(self):
        a = self.array_of_answers  # для краткости
        if not (a[0] == ' ') and ((a[0] == a[1] and a[2] == a[3])
                                  or (a[0] == a[3] and a[3] == a[6])
                                  or (a[0] == a[4] and a[4] == a[8])):
            print(self.win.format(self.first if a[0] == 'x' else self.second))
            return True
        elif not (a[4] == ' ') and ((a[4] == a[1] and a[4] == a[7])
                                    or (a[4] == a[3] and a[4] == a[5])
                                    or (a[4] == a[6] and a[4] == a[2])):
            print(self.win.format(self.first if a[0] == 'x' else self.second))
            return True
        elif not (a[8] == ' ') and ((a[8] == a[7] and a[7] == a[6])
                                    or (a[8] == a[5] and a[5] == a[8])):
            print(self.win.format(self.first if a[0] == 0 else self.second))
            return True
        return False

    def play(self):
        first_player_step = True
        count = 9
        while not self.you_win() and count > 0:
            print(self.output_format.format(self.array_of_answers))
            print(self.step.format(self.first
                                   if first_player_step
                                   else self.second))
            digit = input(self.input_command)
            try:
                digit_int = int(digit)
                if digit_int < 1 or digit_int > 9:
                    raise ValueError
                if not (self.array_of_answers[digit_int - 1] == ' '):
                    raise ValueError
                self.array_of_answers[digit_int - 1] = 'x' \
                    if first_player_step else '0'
                first_player_step = not first_player_step
                count = count - 1
                clear_screen()
            except ValueError:
                print(self.input_error)
                time.sleep(1)
                clear_screen()
                pass
        if count == 0 and not self.you_win():
            print(self.nobody)
        time.sleep(1)
        clear_screen()


TicTacToeGame()
