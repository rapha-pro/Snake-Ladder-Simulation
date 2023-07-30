# Name: Raphael Onana
# SID: 101267225

# pygame.draw.circle(screen, (r,g,b), (x, y), R, w) #(r, g, b) is color, (x, y) is center, R is radius and w
# is the thickness of the circle border.

# pygame.draw.line(surface, color, start_pos, end_pos, width)

import pygame
import random

pygame.init()

# where to start drawing
start = 4


w_in_squares = 12
h_in_squares = 7
square_dim = 50

# adding space for text
game_space = start * square_dim

screen = pygame.display.set_mode((w_in_squares * square_dim, h_in_squares * square_dim))

screen_width, screen_height = screen.get_size()

screen.fill((127, 127, 127))

colour_green = (0, 255, 0)
colour_red = (255, 0, 0)
Black = (0, 0, 0)
white = (255, 255, 255)

pawn1_colour = (0, 0, 255)
pawn2_colour = (255, 255, 255)
pawn_radius = 20
pawn_width = 2

ladder_points = [(575, 225), (275, 325), (425, 275)]
ladder_moves = [4, 4, 4]

snake_points = [(375, 25), (475, 25), (275, 25), (525, 225)]
snake_moves = [6, 6, 1, 2]


def draw_ladder(start_pos, end_pos):
    pygame.draw.line(screen, (0, 0, 0), (start_pos[0] - 15, start_pos[1]), (end_pos[0] - 15, end_pos[1]), 3)
    pygame.draw.line(screen, (0, 0, 0), (start_pos[0] + 15, start_pos[1]), (end_pos[0] + 15, end_pos[1]), 3)

    for i in range(7):
        pygame.draw.line(screen, (0, 0, 0), (start_pos[0] - 15, start_pos[1] + 20 + i*25), (start_pos[0] + 15, start_pos[1] + 20 + i*25), 3)

    pygame.display.update()

# print text on pygame window
def print_numbers_pygame(text, fontsize, x, y):
    # FONTS TEXT
    LETTER_FONT = pygame.font.SysFont('arial', fontsize)

    scrn = LETTER_FONT.render(f"{text}", 1, Black)
    screen.blit(scrn, (x, y))

    pygame.display.update()


def draw_game_board():
    current_colour = colour_green

    k = (w_in_squares - start) * h_in_squares + 1  # 57
    for i in range(0, h_in_squares):
        pygame.display.update()

        for j in range(start, w_in_squares):
            k -= 1
            pygame.draw.rect(screen, current_colour, (j * square_dim, i * square_dim, square_dim, square_dim))
            print_numbers_pygame(k, 15, j*square_dim, i*square_dim)

            draw_ladder((575, 25), (575, 225))
            draw_ladder((275, 125), (275, 325))
            draw_ladder((425, 75), (425, 275))

            # draw snakes
            pygame.draw.line(screen, (127, 127, 0), (375, 25), (375, 325), 3)
            pygame.draw.line(screen, (127, 127, 0), (475, 25), (475, 325), 3)
            pygame.draw.line(screen, (127, 127, 0), (275, 25), (275, 75), 3)
            pygame.draw.line(screen, (127, 127, 0), (525, 225), (525, 325), 3)

            pygame.display.update()

            pygame.time.delay(8)
            if current_colour == colour_green:
                current_colour = colour_red
            else:
                current_colour = colour_green

        if current_colour == colour_green:
            current_colour = colour_red
        else:
            current_colour = colour_green


def move_forward(a, b, wide, square, direct, space):
    if direct == 0:
        if a > ((square // 2) + space):
            a -= square
        else:
            b -= square
            direct = 1

    elif direct == 1:
        if a < wide * square - square/2:
            a += square
        else:
            b -= square
            direct = 0
    return [a, b, direct]


def move_backward(a, b, wide, square, direct, space):
    if direct == 0:  # left to right
        if a < wide * square - square // 2:
            a += square
        else:
            b += square
            direct = 1

    elif direct == 1:
        if a > ((square // 2) + space):
            a -= square
        else:
            b += square
            direct = 0
    return [a, b, direct]


def refresh_draw(current, a1, b1, a2, b2):
    draw_game_board()
    if current == 0:
        pygame.draw.circle(screen, pawn1_colour, (a1, b1), pawn_radius)
        pygame.draw.circle(screen, pawn2_colour, (a2, b2), pawn_radius)
    else:
        pygame.draw.circle(screen, pawn2_colour, (a1, b1), pawn_radius)
        pygame.draw.circle(screen, pawn1_colour, (a2, b2), pawn_radius)

    pygame.display.update()


def display_message(message):
    word_font = pygame.font.SysFont('comicsans', 30)

    pygame.time.delay(1500)
    screen.fill((127, 127, 127))
    text = word_font.render(message, 1, (0, 255, 0))
    screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2 - square_dim))
    pygame.display.update()
    pygame.time.delay(3500)


def print_pygame(text, fontsize, x, y):
    # FONTS TEXT

    pygame.draw.rect(screen, (127, 127, 127), (11,150, 186, 100))
    pygame.display.update()

    LETTER_FONT = pygame.font.SysFont('arial', fontsize)

    scrn = LETTER_FONT.render(f"{text}", 1, Black)
    screen.blit(scrn, (x, y))

    pygame.display.update()


x_initial = w_in_squares * square_dim - square_dim // 2
y_initial = h_in_squares * square_dim - square_dim // 2

# x_initial = (square_dim // 2) + game_space
# y_initial = square_dim // 2

x1 = x_initial
y1 = y_initial

x2 = x_initial
y2 = y_initial

direction = 0  # 0 means right to left and 1 means left to right

print_pygame("Snake Ladder Game", 25, 11, 15)

print_pygame("Yellow line is 'Snake'", 19, 11, 75)


draw_game_board()
pygame.draw.circle(screen, pawn1_colour, (x1, y1), pawn_radius)
pygame.draw.circle(screen, pawn2_colour, (x2, y2), pawn_radius)
pygame.display.update()

pygame.time.delay(1000)

current_player = 0  # 0 means player 1 --> Blue pawn

player1 = [x1, y1, direction]
player2 = [x2, y2, direction]

# MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # def check if player wins
    def check_win(pos_x, pos_y):
        if (pos_y == square_dim // 2) and (pos_x == (square_dim // 2) + game_space):

            # terminal
            print("--------You won-------")
            screen.fill((127, 127, 127))

            # pygame window
            if current_player == 0:
                display_message(" Blue Pawn WINS")
            else:
                display_message(" White Pawn WINS")

            pygame.quit()

    dice = random.randint(0, 6)

    if current_player == 0:
        # on terminal (debugging)
        print(f"player 1 played {dice}")

        # print on pygame window
        print_pygame(f"Blue pawn plays {dice}", 21, 13, 150)

        if dice == 6:
            pygame.time.delay(680)
            print_pygame(f"Blue pawn gets a double move", 15, 13, 150)

        elif dice == 0:
            pygame.time.delay(600)
            print_pygame(f"Blue pawn gets a missed turn", 15, 13, 150)

        x = player1[0]
        y = player1[1]

        direction = player1[2]
    else:
        # on terminal (debugging)
        print(f"player 2 played {dice}")

        print_pygame(f"White pawn plays {dice}", 21, 13, 150)

        if dice == 6:
            pygame.time.delay(680)
            print_pygame(f"White pawn gets a double move", 15, 13, 170)

        elif dice == 0:
            pygame.time.delay(600)
            print_pygame(f"White pawn gets a missed turn", 15, 13, 150)

        x = player2[0]
        y = player2[1]

        direction = player2[2]

    # For debugging
    # print_pygame(f"x: {x}, y:{y}", 21, 43, 95)

    # check if player win
    if (y == square_dim//2) and (x == (square_dim // 2) + game_space):

        # terminal
        print("--------You won-------")
        screen.fill((127, 127, 127))

        # pygame window
        if current_player == 0:
            display_message(" BLUE PAWN WINS")
        else:
            display_message(" WHITE PAWN WINS")

        pygame.quit()

        # make the player stay in the last row until he wins
    elif (y == square_dim//2) and ((x - dice * square_dim) < (square_dim // 2) + game_space):
        # For debugging
        print(f"x: {x}, y:{y}")

        if current_player == 0:
            print_pygame(f"Blue pawn plays {dice}", 21, 13, 150)
            pygame.time.delay(550)
            print_pygame(f"But can't move", 21, 13, 170)
        else:
            print_pygame(f"White pawn plays {dice}", 21, 13, 150)
            pygame.time.delay(550)
            print_pygame(f"But can't move", 21, 13, 170)

    else:
        # move forward and print the player's position at each step
        for i in range(dice):
            data = move_forward(x, y, w_in_squares, square_dim, direction, game_space)
            x = data[0]
            y = data[1]
            direction = data[2]
            if current_player == 0:
                pygame.draw.circle(screen, pawn2_colour, (player2[0], player2[1]), pawn_radius)
                refresh_draw(current_player, x, y, player2[0], player2[1])

            else:
                pygame.draw.circle(screen, pawn1_colour, (player1[0], player1[1]), pawn_radius)
                refresh_draw(current_player, x, y, player1[0], player1[1])


    pygame.time.delay(700)

    # check if pawn fell on a ladder
    if (x, y) in ladder_points:
        if current_player == 0:
            print_pygame("Blue pawn climbs a ladder", 17, 13, 150)
        else:
            print_pygame("White pawn climbs a ladder", 17, 13, 150)
        for i in range(len(ladder_points)):
            if (x, y) == ladder_points[i]:
                for j in range(ladder_moves[i]):
                    y -= square_dim
                    if direction == 0:
                        direction = 1
                    else:
                        direction = 0

                    if current_player == 0:
                        refresh_draw(current_player, x, y, player2[0], player2[1])
                    else:
                        refresh_draw(current_player, x, y, player1[0], player1[1])

    # check if pawn fell on a snake
    elif (x, y) in snake_points:
        if current_player == 0:
            print_pygame("Blue pawn steps on a snake", 18, 12, 150)
        else:
            print_pygame("White pawn steps on a snake", 17, 11, 150)
        for i in range(len(snake_points)):
            if (x, y) == snake_points[i]:
                for j in range(snake_moves[i]):
                    y += square_dim
                    if direction == 0:
                        direction = 1
                    else:
                        direction = 0

                    if current_player == 0:
                        refresh_draw(current_player, x, y, player2[0], player2[1])
                    else:
                        refresh_draw(current_player, x, y, player1[0], player1[1])

    pygame.time.delay(1000)



    if current_player == 0:
        check_win(player1[0], player1[1])
        player1 = [x, y, direction]
        x1 = player1[0]
        y1 = player1[1]

        # save current position and then get double move
        if dice == 6:
            continue

        current_player = 1
    else:
        check_win(player2[0], player2[1])
        player2 = [x, y, direction]
        x2 = player2[0]
        y2 = player2[1]

        if dice == 6:
            continue

        current_player = 0



