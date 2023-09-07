import os
import random
import math
import pygame
from components.reset_game import reset_game
from components.load_sprites import load_sprite_sheets
from components.get_block import get_block
from components.create_objects import create_objects
from Classes.object import Object, Block
from Classes.traps import Fire, Spikes
from Classes.points import Point
from Classes.checkpoint import Checkpoint
from Classes.custom_timer import Timer
from Classes.startpage import StartPage
from os import listdir
from os.path import isfile, join
pygame.init()
twoBitFont = os.path.join(os.path.dirname(__file__), "Classes", "fonts", "PressStart2P-Regular.ttf")

# Set up the display
pygame.display.set_caption("Platformer")
WIDTH, HEIGHT = 1000, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))

from Classes.player import Player
from Classes.enemy import Enemy
from Classes.walking_enemy import WalkingEnemy
from components.move_collide import collide, handle_move, handle_vertical_collision, removed_points


# Function to get background tiles and image
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


# Function to draw game elements on the window
def draw(window, background, bg_image, player, enemyList, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)\

    player.draw(window, offset_x)
    for enemy in enemyList:
        enemy.draw(window, offset_x)
    pygame.display.update()


#MAIN GAME LOOP
def main(window):
    #Start page
    start_page = StartPage(WIDTH, HEIGHT)
    current_state = "start"

    while True:

        if current_state == "start":
            next_state = start_page.update()
            start_page.draw()

        elif current_state == "main_game":

            # Initialize clock, load background
            clock = pygame.time.Clock()
            background, bg_image = get_background("startBackground.jpg")

            # Set the block size for creating the platforms
            block_size = 96

            # Create player/position
            player = Player(100, 100, 50, 50)

            #walking_enemy = WalkingEnemy(100, HEIGHT - block_size - 128, 150, 150) 

            # ENEMIES
            enemyList = []

            # LEFT/RIGHT
            for i in range(2):  
                enemy = Enemy(block_size * 41, HEIGHT - block_size - 128, 150, 150, "left") 
                enemyList.append(enemy)
            enemyList[1].direction = "right"
            #ENEMY Y POSITION LEFT/RIGHT
            enemyList[0].rect.y = HEIGHT - block_size * 6.05
            enemyList[1].rect.y = HEIGHT - block_size - 100
            #ENEMY X POSITION LEFT/RIGHT
            enemyList[0].rect.x = block_size * 45
            enemyList[1].rect.x = block_size * 37

            # UP/DOWN
            for i in range(6):
                enemy = Enemy(block_size * 59, 250, 150, 150, "up") 
                enemyList.append(enemy)
            #X POSITION
            enemyList[3].rect.x = block_size * 63
            enemyList[4].rect.x = block_size * 67
            enemyList[5].rect.x = block_size * 72
            enemyList[6].rect.x = block_size * 78
            enemyList[7].rect.x = block_size * 81
            #Y POSITION
            enemyList[6].rect.y = 350
            enemyList[2].rect.y = 650
            enemyList[4].rect.y = 500
            enemyList[7].rect.y = 350

            #Starting direction
            enemyList[2].direction = "down"
            enemyList[4].direction = "down"
            enemyList[6].direction = "down"

            #Score initialization
            score = player.points

            #FIRE TRAPS
            # Create a fire object list
            fireList = []
            # Create fire objects and add them to the list
            for i in range(5):  
                x_position = (block_size * 20.33) + i * 384  
                fire = Fire(x_position, HEIGHT - block_size * 2.66, 16, 32)
                fire.on()  # Turn on each fire object
                fireList.append(fire)
            fireList[1].rect.y = HEIGHT - block_size * 4.66
            fireList[3].rect.y = HEIGHT - block_size * 4.66
            fireList[4].rect.x = fireList[2].rect.x
            fireList[4].rect.y = HEIGHT - block_size * 6.66

            #POINTS
            pointList = []
            # Create fire objects and add them to the list
            for i in range(5):  
                x_position = (block_size * 20.17) + i * 384  
                point = Point(x_position, HEIGHT - block_size * 2.66, 32, 128)
                pointList.append(point)
            for i in range(2):  
                y_position = (HEIGHT - block_size - 72) 
                point = Point(block_size * 41, y_position, 32, 128)
                pointList.append(point)
            pointList[0].rect.y = HEIGHT - block_size * 4.66
            pointList[2].rect.y = HEIGHT - block_size * 4.66
            pointList[4].rect.y = HEIGHT - block_size * 6.66
            pointList[4].rect.x = pointList[3].rect.x
            pointList[5].rect.y = HEIGHT - block_size * 5.8

            #Create final checkpoint to end level if you have collected all berries
            checkpoint = Checkpoint(block_size * 93, HEIGHT - block_size - 128, 64, 64)
            checkpointList = [checkpoint]
            checkpoint.on()

            # Create objects using the create_objects function
            objects = create_objects(block_size, HEIGHT) + fireList + pointList + checkpointList

            # Initialize the camera horizontal/vertical offset 
            offset_x = 0
            offset_y = 0

            # Create an instance of the Timer class with an initial value of 60 seconds
            timer = Timer(0)

            # Start the main game loop
            run = True
            while run:

                # Limit the frame rate
                clock.tick(FPS)

                # Print timer.active for debugging
                print("Timer Active:", timer.active)

                #Update timer
                if timer.active:
                    timer.value += clock.get_time() / 1000  # Decrease timer


                # Event handling loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and player.jump_count < 2:
                            player.jump()
                        elif event.key == pygame.K_r:
                            #Player Reset
                            reset_game(player)
                            objects.extend(removed_points)
                            removed_points.clear() 

                            #Window Reset
                            window.fill((0, 0, 0))  
                            pygame.display.flip()
                            offset_x = 0
                            draw(window, background, bg_image, player, enemyList, objects, offset_x)
                            print("Window reset")

                            #Score reset
                            player.score_reset()
                    
                            #Timer reset
                            timer.value = timer.initial_value
                            timer.active = False

                # Update player/fire/points/enemy position and animation
                player.loop(FPS)
                for fire in fireList:
                    fire.loop()
                for point in pointList:
                    point.loop()
                for enemy in enemyList:
                    enemy.loop()
                checkpoint.loop()

                # Handle player movement and collisions with objects
                handle_move(player, objects, enemyList)

                # Draw the background, objects, and player on the window
                draw(window, background, bg_image, player, enemyList, objects, offset_x)

                # Define the width/height of the scroll area at the edges of the screen
                scroll_area_width = 400
                scroll_area_height = 200  


                # Scroll the camera horizontally based on player's position
                if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                        (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                    offset_x += player.x_vel 

                
                if player.is_alive:
                    timer.start()

                    #Checking to see if the player went off the bottom of the screen 
                    if player.rect.bottom > HEIGHT + 100:
                        player.die()

                    #If player points are over a certain amount, you win 
                    if player.won:
                        font = pygame.font.Font(twoBitFont, 36)
                        timer.stop()
                        win_text1 = font.render("YOU WIN!", True, (255, 255, 255))
                        win_text2 = font.render(f"FINISHED IN { int(timer.value) } SECONDS", True, (255, 255, 255))

                        # Calculate the total height of the text surfaces
                        total_height = win_text1.get_height() + win_text2.get_height()

                        # Create a combined text surface
                        combined_text_surface = pygame.Surface((max(win_text1.get_width(), win_text2.get_width()), total_height), pygame.SRCALPHA)
                        combined_text_surface.fill((0, 0, 0, 0))  # Fill the background with a transparent color

                        # Blit each line onto the combined text surface
                        combined_text_surface.blit(win_text1, ((combined_text_surface.get_width() - win_text1.get_width()) // 2, 0))
                        combined_text_surface.blit(win_text2, ((combined_text_surface.get_width() - win_text2.get_width()) // 2, win_text1.get_height()))

                        window.blit(combined_text_surface, (WIDTH // 2 - combined_text_surface.get_width() // 2, HEIGHT // 2))
                        pygame.display.update()
                        pygame.time.delay(5000)

                        #Player Reset
                        reset_game(player)

                        #Window Reset
                        window.fill((0, 0, 0))      
                        pygame.display.flip()
                        offset_x = 0
                        draw(window, background, bg_image, player, enemyList, objects, offset_x)
                        print("Window reset")

                        #Score reset
                        player.score_reset()

                        #Point reset
                        objects.extend(removed_points)
                        removed_points.clear() 
                        
                        #Timer reset
                        timer.value = timer.initial_value
                        timer.active = False
                        #Player win reset
                        player.won = False
                    
                if not player.is_alive:
                    font = pygame.font.Font(twoBitFont, 36)
                    death_text = font.render("YOU DIED!", True, (255, 255, 255))
                    window.blit(death_text, (WIDTH // 2 - death_text.get_width() // 2, HEIGHT // 2))
                    pygame.display.update()
                    pygame.time.delay(2000)

                    #Player Reset
                    reset_game(player)

                    #Point reset
                    objects.extend(removed_points)
                    removed_points.clear() 

                    #Window Reset
                    window.fill((0, 0, 0))  
                    pygame.display.flip()
                    offset_x = 0
                    draw(window, background, bg_image, player, enemyList, objects, offset_x)
                    print("Window reset")

                    #Score reset
                    player.score_reset()
                    
                    #Timer reset
                    timer.value = timer.initial_value
                    timer.active = False

        if next_state:
            # Update the current game state
            current_state = next_state  


    # Quit pygame and exit the game
    pygame.quit()
    quit()


#Entry point of game
if __name__ == "__main__":
    main(window)
