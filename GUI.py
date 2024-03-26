import algorithms
import pygame
import sys
import time
import random


pygame.init()
BORDER = 15
WIDTH, HEIGHT = 1200, 600
WINDOW_WIDTH, WINDOW_HEIGHT = WIDTH + 2 * BORDER, HEIGHT + 2 * BORDER + 50
BUTTON_WIDTH, BUTTON_HEIGHT = 240, 40
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Sorting Algorithms')
#LST_LENGTH = 500
#BAR_WIDTH = (WINDOW_WIDTH - 4 * BORDER) // LST_LENGTH
BIG_LINE = 6
SMALL_LINE = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY_LIGHT = (200, 200, 200)
PURPLE = (203, 153, 201)
RED = (200, 0, 0)
ORANGE = (200, 100, 0)
GREEN = (0, 200, 0)
BLUE_LIGHT = (180, 198, 231)
BLUE_DARK = (142, 170, 219)
FONT_VALUES = pygame.font.SysFont('Times New Roman', 20)
SPEED = 0.1
FPS = 60
ALGORITHM = None
RUN = True
ORDER = None


def main():
    global RUN
    global ORDER
    global ALGORITHM
    
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    while True:
        while RUN:
            get_events()
            mouse, click = get_mouse_events()
            draw_window(mouse=mouse, click=click, phase='start')
            if ALGORITHM != None:
                RUN = False
                pygame.time.wait(200)

        RUN = True
        while RUN:
            get_events()
            mouse, click = get_mouse_events()
            draw_window(mouse=mouse, click=click, phase='order')
            if ORDER != None:
                RUN = False
                pygame.time.wait(200)

        if ALGORITHM == 'bubble':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            algorithms.bubble_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'selection':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            algorithms.selection_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'insertion':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            algorithms.insertion_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'merge':
            lst, bar_width = initialize_list(500)
            get_started(lst, bar_width)
            algorithms.merge_sort(lst, first=True, bar_width=bar_width)
        elif ALGORITHM == 'quick':
            lst, bar_width = initialize_list(1000)
            get_started(lst, bar_width)
            algorithms.quick_sort(lst, high=len(lst)-1, bar_width=bar_width)
        elif ALGORITHM == 'heap':
            lst, bar_width = initialize_list(500)
            get_started(lst, bar_width)
            algorithms.heap_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'counting':
            lst, bar_width = initialize_list(1000)
            get_started(lst, bar_width)
            algorithms.counting_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'radix':
            lst, bar_width = initialize_list(1000)
            get_started(lst, bar_width)
            algorithms.radix_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'shell':
            lst, bar_width = initialize_list(500)
            get_started(lst, bar_width)
            algorithms.shell_sort(lst, len(lst), bar_width=bar_width)
        elif ALGORITHM == 'cocktail':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            algorithms.cocktail_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'bitonic':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            lst = algorithms.start_bitonic_sort()
            #test.main(lst)
        elif ALGORITHM == 'bogo':
            lst, bar_width = initialize_list(200)
            get_started(lst, bar_width)
            algorithms.bogo_sort(lst, bar_width=bar_width)
        elif ALGORITHM == 'cycle':
            lst, bar_width = initialize_list(250)
            get_started(lst, bar_width)
            algorithms.cycle_sort(lst, bar_width=bar_width)

        green = []
        for i, val in enumerate(lst):
            green.append(val)
            if len(lst) == 1000 and i % 4 == 0:
                algorithms.print_res(lst, green=green, bar_width=bar_width)
                time.sleep(0.0001)
            elif len(lst) == 500 and i % 2 == 0:
                algorithms.print_res(lst, green=green, bar_width=bar_width)
                time.sleep(0.0002)
            elif len(lst) == 250:
                algorithms.print_res(lst, green=green, bar_width=bar_width)
                time.sleep(0.001)


        RUN = True
        while RUN:
            get_events()
            mouse, click = get_mouse_events()
            draw_window(mouse=mouse, click=click, lst=lst, green=green, bar_width=bar_width, phase='end')
        
        ORDER = None
        ALGORITHM = None
        RUN = True
        lst = list()


def get_started(lst, bar_width):
    global RUN
    RUN = True
    while RUN:
        get_events()
        mouse, click = get_mouse_events()
        draw_window(mouse=mouse, click=click, lst=lst, bar_width=bar_width, phase='started')


def initialize_list(size):
    lst = [i + 1 for i in range(size)]
    #lst = [random.randint(1, size) for _ in range(size)]
    bar_width = (WINDOW_WIDTH - 4 * BORDER) // len(lst)
    if ORDER == 'random':
        random.shuffle(lst)
    elif ORDER == 'reverse':
        lst.reverse()
    return lst, bar_width


def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def get_mouse_events():
    return pygame.mouse.get_pos(), pygame.mouse.get_pressed()


def draw_window(mouse, click, phase='sorting', lst=None, green=[], orange=[], red=[], counter=False, bar_width=0):
    WINDOW.fill(GREY_LIGHT)
    COLUMN_1, COLUMN_2 = WINDOW_WIDTH // 2 - BUTTON_WIDTH - BORDER, WINDOW_WIDTH // 2 + BORDER
    ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8 = 20, 20 * 2 + BUTTON_HEIGHT, 20 * 3 + BUTTON_HEIGHT * 2, 20 * 4 + BUTTON_HEIGHT * 3, 20 * 5 + BUTTON_HEIGHT * 4, 20 * 6 + BUTTON_HEIGHT * 5, 20 * 7 + BUTTON_HEIGHT * 6, 20 * 8 + BUTTON_HEIGHT * 7

    if phase == 'start':
        draw_button(mouse, click, COLUMN_1, ROW_2, 'bubble', 'selection')
        value = FONT_VALUES.render('Bubble Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 77, ROW_2 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_2, 'selection', 'selection')
        value = FONT_VALUES.render('Selection Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 65, ROW_2 + 7))

        draw_button(mouse, click, COLUMN_1, ROW_3,'insertion', 'selection')
        value = FONT_VALUES.render('Insertion Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 70, ROW_3 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_3, 'merge', 'selection')
        value = FONT_VALUES.render('Merge Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 75, ROW_3 + 7))

        draw_button(mouse, click, COLUMN_1, ROW_4, 'quick', 'selection')
        value = FONT_VALUES.render('Quick Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 80, ROW_4 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_4, 'heap', 'selection')
        value = FONT_VALUES.render('Heap Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 80, ROW_4 + 7))
        
        draw_button(mouse, click, COLUMN_1, ROW_5, 'counting', 'selection')
        value = FONT_VALUES.render('Counting Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 80, ROW_5 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_5, 'radix', 'selection')
        value = FONT_VALUES.render('Radix Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 80, ROW_5 + 7))

        draw_button(mouse, click, COLUMN_1, ROW_6, 'shell', 'selection')
        value = FONT_VALUES.render('Shell Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 80, ROW_6 + 7))
        
        draw_button(mouse, click, COLUMN_2, ROW_6, 'cocktail', 'selection')
        value = FONT_VALUES.render('Cocktail Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 80, ROW_6 + 7))

        draw_button(mouse, click, COLUMN_1, ROW_7, 'cycle', 'selection')
        value = FONT_VALUES.render('Cycle Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 80, ROW_7 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_7, 'bitonic', 'selection')
        value = FONT_VALUES.render('Bitonic Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 80, ROW_7 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_8, 'bogo', 'selection')
        value = FONT_VALUES.render('Bogo Sort', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 80, ROW_8 + 7))

    elif phase == 'order':
        draw_button(mouse, click, COLUMN_1, ROW_5, 'sorted', 'order')
        value = FONT_VALUES.render('Sorted Order', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 68, ROW_5 + 7))

        draw_button(mouse, click, COLUMN_2, ROW_5, 'random', 'order')
        value = FONT_VALUES.render('Random Order', True, BLACK)
        WINDOW.blit(value, (COLUMN_2 + 60, ROW_5 +  + 7))

        draw_button(mouse, click, COLUMN_1, ROW_6, 'reverse', 'order')
        value = FONT_VALUES.render('Reverse Order', True, BLACK)
        WINDOW.blit(value, (COLUMN_1 + 60, ROW_6 + 7))

    else:
        if phase == 'started':
            draw_button(mouse, click, BORDER + 50 * 17, WINDOW_HEIGHT - 37, 'start', type='start')
            value = FONT_VALUES.render('Start', True, BLACK)
            WINDOW.blit(value, (BORDER + 50 * 17 + 30, WINDOW_HEIGHT - 34))
        pygame.draw.rect(WINDOW, WHITE, (2.2 * BORDER, 1 * BORDER, WINDOW_WIDTH - 4.2 * BORDER, WINDOW_HEIGHT - 4 * BORDER))
        pygame.draw.line(WINDOW, BLACK, (2.05 * BORDER, 1 * BORDER), (WINDOW_WIDTH - 2.05 * BORDER, 1 * BORDER), SMALL_LINE)
        pygame.draw.line(WINDOW, BLACK, (2.1 * BORDER, WINDOW_HEIGHT - 3 * BORDER), (WINDOW_WIDTH - 2.2 * BORDER, WINDOW_HEIGHT - 3 * BORDER), SMALL_LINE)
        pygame.draw.line(WINDOW, BLACK, (2.1 * BORDER, 1.1 * BORDER), (2.1 * BORDER, WINDOW_HEIGHT - 2.85 * BORDER), SMALL_LINE)
        pygame.draw.line(WINDOW, BLACK, (WINDOW_WIDTH - 2.2 * BORDER, 1.1 * BORDER), (WINDOW_WIDTH - 2.2 * BORDER, WINDOW_HEIGHT - 2.85 * BORDER), SMALL_LINE)
        
        green_counter = 0
        for i, bar in enumerate(lst):
            if bar in orange:
                pygame.draw.rect(WINDOW, ORANGE, (7.7 * BORDER + i * bar_width, 2 * BORDER + ((len(lst) - bar) / len(lst)) * WINDOW_HEIGHT * 0.86, bar_width, (bar / len(lst)) * WINDOW_HEIGHT * 0.86))
            elif bar in red:
                pygame.draw.rect(WINDOW, RED, (7.7 * BORDER + i * bar_width, 2 * BORDER + ((len(lst) - bar) / len(lst)) * WINDOW_HEIGHT * 0.86, bar_width, (bar / len(lst)) * WINDOW_HEIGHT * 0.86))
            elif bar in green and counter and green_counter == 0:
                pygame.draw.rect(WINDOW, GREEN, (7.7 * BORDER + i * bar_width, 2 * BORDER + ((len(lst) - bar) / len(lst)) * WINDOW_HEIGHT * 0.86, bar_width, (bar / len(lst)) * WINDOW_HEIGHT * 0.86))
                green_counter += 1
            elif bar in green and not counter:
                pygame.draw.rect(WINDOW, GREEN, (7.7 * BORDER + i * bar_width, 2 * BORDER + ((len(lst) - bar) / len(lst)) * WINDOW_HEIGHT * 0.86, bar_width, (bar / len(lst)) * WINDOW_HEIGHT * 0.86))
                green_counter += 1
            else:
                pygame.draw.rect(WINDOW, BLUE_DARK, (7.7 * BORDER + i * bar_width, 2 * BORDER + ((len(lst) - bar) / len(lst)) * WINDOW_HEIGHT * 0.86, bar_width, (bar / len(lst)) * WINDOW_HEIGHT * 0.86))
        pygame.draw.line(WINDOW, BLACK, (5 * BORDER, WINDOW_HEIGHT * 0.9), (WINDOW_WIDTH - 5 * BORDER, WINDOW_HEIGHT * 0.9), BIG_LINE)
        
        if phase == 'end':
            draw_button(mouse, click, BORDER + 50 * 17, WINDOW_HEIGHT - 37, 'restart', type='restart')
            value = FONT_VALUES.render('Restart', True, BLACK)
            WINDOW.blit(value, (BORDER + 50 * 17 + 21, WINDOW_HEIGHT - 34))

    pygame.display.update()


def draw_button(mouse, click, x, y, button, type=None):
    global ACTIVE
    global ALGORITHM
    global ORDER
    global RUN
    mouse_x, mouse_y = mouse
    if type == 'selection':
        width, height = BUTTON_WIDTH, BUTTON_HEIGHT
    elif type in ['start', 'restart']:
        width, height = 100, 30
    else:
        width, height = BUTTON_WIDTH, BUTTON_HEIGHT
    if x < mouse_x < x + width and y < mouse_y < y + height:
        pygame.draw.rect(WINDOW, BLUE_LIGHT, (x, y, width, height))
        pygame.draw.rect(WINDOW, BLACK, (x, y, width, height), 2)
        if click == (1, 0, 0) and type == 'selection' and ACTIVE == False:
            ACTIVE = True
            ALGORITHM = button
            RUN = False
        elif click == (1, 0, 0) and type == 'order' and ACTIVE == False:
            ACTIVE = True
            ORDER = button
            RUN = False

        elif click == (1, 0, 0) and type in ['start', 'restart'] and ACTIVE == False:
            ACTIVE = True
            RUN = False
        
        if click == (0, 0, 0):
            ACTIVE = False
    else:
        pygame.draw.rect(WINDOW, BLUE_DARK, (x, y, width, height))
        pygame.draw.rect(WINDOW, BLACK, (x, y, width, height), 2)


if __name__ == '__main__':
    main()