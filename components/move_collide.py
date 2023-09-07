import pygame
from Classes.enemy import Enemy

PLAYER_VEL = 4
removed_points = []

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def collide(player, objects, enemies, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break
    for enemy in enemies:
        if pygame.sprite.collide_mask(player, enemy):
            collided_object = enemy
            collision_occurred = True
            break 

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects, enemies):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, enemies,  -PLAYER_VEL * 2)
    collide_right = collide(player, objects, enemies, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.die()
        if obj and obj.name == "spikes":
            player.die()
        elif obj and obj.name == "checkpoint" and player.points == 7:
                player.win()
        elif obj and obj.name == "points":
            if obj in objects:
                player.add_point()
                objects.remove(obj)
                removed_points.append(obj)
        elif isinstance(obj, Enemy):
            player.die() 



