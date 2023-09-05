import pygame
from Classes.enemy import Enemy
from Classes.walking_enemy import WalkingEnemy

PLAYER_VEL = 5

# Function to check for vertical collisions 
def handle_vertical_collision(player, objects, enemy, dy):
    collided_objects = []
    enemies = [enemy]
    for obj in objects + enemies:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


# Function to check for collisions between the player and objects
def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_objects = []
    #enemies = [enemy]
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break 

    player.move(-dx, 0)
    player.update()
    return collided_objects


# Function to handle player movement
def handle_move(player, objects, enemies):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL * 2)
    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)

    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, enemies, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj:
            if obj.name == "fire":
                player.make_hit()
                player.die()
            elif obj.name == "spikes":
                player.make_hit()
                player.die()
            elif obj.name == "checkpoint" and player.points == 1:
                player.win()
            elif obj.name == "points":
                if obj in objects:
                    player.add_point()
                    objects.remove(obj)
            elif isinstance(obj, Enemy):
                player.die()
            elif isinstance(obj, WalkingEnemy):
                player.die()




