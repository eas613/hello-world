# def fact(n):
#     if n == 0 :
#         return 1
#     return fact(n-1)*n

# print (fact(4))

# def print_in_order():
#     x = int(input("enter :"))
#     if x == 0 :
#         return
#     print_in_order()
#     print(x)

# print_in_order()

# def power(a,b):
#     if b == 0:
#         return 1
#     return power(a,b-1)*a
# print(power(2,20))

# count =  0
# def power_1(a,b):
#     global count 
#     count += 1
#     if b == 0:
#         return 1 
#     elif not b % 2:
#         return power_1(a,b//2) * power_1(a,b//2)
#     else:
#         return power_1(a,b//2) * power_1(a,b//2) *a
# print (power_1(2,6),count )

# # def dec_to_binary(x):
# #     if x == 1:
# #         return 1
# #     if x == 0:
# #         return 0
# #     if x %

# def hanoi(n,source, aux , target):
#     if n == 1 :
#         print (f"move ring 1 from {source} to {target} . ")
#     else :
#         hanoi(n-1,source,target,aux)
#         print( f"move ring {n} from {source} to {target}. ")
#         hanoi(n-1,aux , source, target)

# hanoi(6, 1, 2 ,3)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
TOWER_WIDTH = 10
TOWER_HEIGHT = 150
BASE_HEIGHT = 10
NUM_DISKS = 5
DISK_COLOR = (255, 0, 0)
TOWER_COLOR = (0, 0, 255)

# Function to draw a disk
def draw_disk(x, y, width):
    pygame.draw.rect(screen, DISK_COLOR, (x - width // 2, y, width, BASE_HEIGHT))

# Function to draw a tower
def draw_tower(x):
    pygame.draw.rect(screen, TOWER_COLOR, (x - TOWER_WIDTH // 2, HEIGHT - TOWER_HEIGHT, TOWER_WIDTH, TOWER_HEIGHT))

# Function to draw the entire screen
def draw_screen(towers):
    screen.fill((255, 255, 255))
    for i, tower in enumerate(towers):
        draw_tower((i + 1) * WIDTH // 4)
        for j, disk_width in enumerate(tower):
            draw_disk((i + 1) * WIDTH // 4, HEIGHT - BASE_HEIGHT - (j + 1) * BASE_HEIGHT, disk_width)
    pygame.display.flip()

# Recursive Tower of Hanoi function
def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        towers[source].pop()
        towers[target].append(n)
        draw_screen(towers)
        pygame.time.delay(500)
        hanoi(n - 1, auxiliary, target, source)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi")

# Initialize towers
towers = [list(range(NUM_DISKS, 0, -1)), [], []]

# Main loop
draw_screen(towers)
hanoi(NUM_DISKS, 0, 2, 1)  # Start the Tower of Hanoi algorithm

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
