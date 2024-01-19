# فراخوانی کتابخانه رنگ ها
from termcolor import colored

# معرفی تخته ی بازی و تعداد خانه ها
board = list(range(1, 10))

# معرفی ترکیب های برنده
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))

# اولویت بندی برای انتخاب کامپیوتر
moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


# تابع زیبا سازی ظاهر تخته
def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "blue"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "magenta"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


# تابع بررسی آیا بازیکن برنده شده یا خیر
def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        # زمانی که کامپیوتر برنده شدن را تست میکند تغییری در آن خانه ایجاد میشود,
        # بخش undo بعد از بررسی, تغییرات را به حالت اولیه برمیگرداند
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False


# تابع بررسی آیا کاربر میتواند حرکت کند یا خیر
def can_move(brd, mve):
    # isinstance() بررسی میکند که آیا این حرکت قبلا انجام شده یا خیر
    if mve in range(1, 10) and isinstance(brd[mve - 1], int):
        return True
    return False


# تابع بررسی آیا بازیکن برنده شده یا خیر
def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            # اگر کاربر در موقعیت برنده نبود break میکند و tuple حالت برنده بعدی را بررسی میکند
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


# تابع چک کردن فضای خالی
def has_empty_space():
    return board.count("X") + board.count("O") != 9


# تابع بازیکن کامپیوتر
def computer_move():
    mv = -1
    # بررسی آیا خود کامپیوتر میتواند برنده شود؟
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break

    # اگر کاربر میتواند برنده شود جلوی او را بگیر
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break

    # بر اساس tuple های اولویت بندی حرکت کامپیوتر, حرکت کن
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)


player, computer = "X", "O"
print("\nPlayer: Blue(X)\nComputer: Magenta(O)")


# حلقه اصلی بازی
while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print(colored(move, "yellow"), colored("is Invalid Number! Try Again!", "yellow"))
        continue
    if won:
        print(colored("You Won!", "green"))
        break
    elif computer_move()[1]:
        print(colored("You Lose!", "red"))
        break


print_board()
