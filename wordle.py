import pygame
import engine as engine
pygame.init()

Game_State = engine.Game_State()

WIDTH = HEIGHT = 900
SQ_SIZE = WIDTH//10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
BG_COLOR = (18, 18, 19)
BRIGHT_SQ = (58, 58, 60)
DARK_SQ = (20, 20, 25)
YELLOW_SQ = (181, 159, 59)
GREEN_SQ = (83, 141, 78)
LETTER_COLOR = (248, 248, 248)
font = pygame.font.SysFont('Helvicta', WIDTH//10, True, False)

def draw_background(screen):
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH+WIDTH*0.1, HEIGHT+WIDTH*0.1))

def draw_letterquares(screen, board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            pygame.draw.rect(screen, BRIGHT_SQ, (column*SQ_SIZE+WIDTH*0.25, row*SQ_SIZE+WIDTH*0.06, SQ_SIZE-SQ_SIZE*0.1, SQ_SIZE-SQ_SIZE*0.1))
            pygame.draw.rect(screen, DARK_SQ, (column*SQ_SIZE+WIDTH*0.255, row*SQ_SIZE+WIDTH*0.065, SQ_SIZE-SQ_SIZE*0.18, SQ_SIZE-SQ_SIZE*0.18))

def draw_letters(screen, board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if Game_State.board[row][column][1] == "Y":
                pygame.draw.rect(screen, YELLOW_SQ, (column*SQ_SIZE+WIDTH*0.25, row*SQ_SIZE+WIDTH*0.06, SQ_SIZE-SQ_SIZE*0.1, SQ_SIZE-SQ_SIZE*0.1))
            if Game_State.board[row][column][1] == "G":
                pygame.draw.rect(screen, GREEN_SQ, (column*SQ_SIZE+WIDTH*0.25, row*SQ_SIZE+WIDTH*0.06, SQ_SIZE-SQ_SIZE*0.1, SQ_SIZE-SQ_SIZE*0.1))
                            
            if Game_State.board[row][column][0] != "_":
                rect = pygame.Rect(column*SQ_SIZE+WIDTH*0.25, row*SQ_SIZE+WIDTH*0.06, SQ_SIZE-SQ_SIZE*0.1, SQ_SIZE-SQ_SIZE*0.1)
                text_object = font.render(f'{board[row][column][0]}', True, LETTER_COLOR)
                text_location = (text_object.get_rect(center = rect.center))
                screen.blit(text_object, text_location)

def draw_endgame_text(font, screen, text):
    text_object = font.render(text, 0, LETTER_COLOR)
    text_location = pygame.Rect(0,0, WIDTH, HEIGHT).move(WIDTH/2 - text_object.get_width()/2, HEIGHT/2 - text_object.get_height()/2+SQ_SIZE*2)
    screen.blit(text_object, text_location)

def draw_board(screen):
    draw_background(screen)
    draw_letterquares(screen, Game_State.board)
    draw_letters(screen, Game_State.board)

running = True

word = ""
pygame.key.start_text_input()

    
while running:
    draw_board(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if Game_State.gameover == False:
            if Game_State.win == False:
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        if len(word) < 5:
                            word += event.unicode
                            Game_State.board[Game_State.guess_count][len(word)-1] = f'{event.unicode.upper()}_'

                    if event.key == pygame.K_BACKSPACE:
                        word = word[:-1]
                        Game_State.board[Game_State.guess_count][len(word)] = "__"
                    elif event.key == pygame.K_RETURN:  # K_RETURN — это клавиша Enter
                            if len(word) == 5:
                                Game_State.guess(Game_State.dictionary, Game_State.guess_count, word, Game_State.random_word)
                                word = ""
                                if Game_State.guess_count < 6:
                                    Game_State.board[Game_State.guess_count] = ["__", "__", "__", "__", "__"]
                        

    if Game_State.gameover:
            draw_endgame_text(font, screen, (f'{Game_State.random_word}'))
    if Game_State.win:
                draw_endgame_text(font, screen, (f'молодес'))
    clock.tick(FPS)
    pygame.display.flip()

# словарь
# Выбор рандомного слова из словаря
# отрисовка
# фона
#  6 рядов по 5 клеток (функция, ряд принимает инпут, если слово есть в словаре,
# проверяет побуквенно с выбранным словом: буква в слове - красит в желтый, буква в слове и в этом же месте - в зеленый, переходит на следующий ряд)
# прорисовка букв реалтайм
# исправить проверку одной и той же буквы

#  клавиатура (функция нажал кнопку = инпут, использованные буквы темнеют), 