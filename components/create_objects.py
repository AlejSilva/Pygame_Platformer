from Classes.object import Block, WoodBlock, ScaleBlock, GrassBlock, OrangeBlock, PinkBlock
from Classes.traps import Fire, Spikes
from Classes.points import Point

WIDTH, HEIGHT = 1000, 800


def create_objects(block_size, HEIGHT):
    #Create spikes1 object
    spike1_x_positions = [500, 550, 600, 650, 700]  
    spikes1 = [Spikes(x, HEIGHT - block_size - 64, 45, 64) for x in spike1_x_positions]

    #Create spikes1 object
    spike2_x_positions = [885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485]  
    spikes2 = [Spikes(x, HEIGHT - block_size - 64, 45, 64) for x in spike2_x_positions]

    # Calculate the number of blocks in the STONE floor
    stone_floor_blocks = int(WIDTH * 2) // block_size

    # Create the floor by generating blocks in a range
    stone_floor = [Block(i * block_size, HEIGHT - block_size, block_size)
                    for i in range(stone_floor_blocks)]

    # Calculate the starting index for the WOOD floor
    wood_floor_start = stone_floor_blocks              

    # Create the pink floor by generating blocks in a range
    wood_floor = [WoodBlock(i * block_size, HEIGHT - block_size, block_size)
                    for i in range(wood_floor_start, wood_floor_start + 15)]

    # Calculate the starting index for the SCALE floor
    scale_floor_start = wood_floor_start + 15              

    # Create the pink floor by generating blocks in a range
    scale_floor = [ScaleBlock(i * block_size, HEIGHT - block_size, block_size)
                    for i in range(scale_floor_start, scale_floor_start + 15)]

    # Calculate the starting index for the JUMPING area
    jumping_start = scale_floor_start + 15   

    #Ending floor
    ending_floor = [PinkBlock(i * block_size, HEIGHT - block_size, block_size)
                    for i in range(jumping_start + 33, jumping_start + 45)]

    #List of ScaleBlocks for the scale tunnels 
    scale_tunnel1 = [ScaleBlock(block_size * i, HEIGHT - block_size * 3, block_size)
                    for i in range(36, 46)]
    scale_tunnel2 = [ScaleBlock(block_size * i, HEIGHT - block_size * 5, block_size)
                    for i in range(36, 46)]
    scale_tunnel3 = [ScaleBlock(block_size * i, HEIGHT - block_size * 7, block_size)
                    for i in range(36, 46)]
    #Combine the scale tunnels 
    scale_tunnels = scale_tunnel1 + scale_tunnel2 + scale_tunnel3

    #The walls that are to the left of the player's starting position
    startingwall1 = [Block(0, HEIGHT - block_size * i, block_size) for i in range (2, 10)]
    startingwall2 = [Block(block_size * -1, HEIGHT - block_size * i, block_size) for i in range (1, 10)]
    startingwall3 = [Block(block_size * -2, HEIGHT - block_size * i, block_size) for i in range (1, 10)]
    startingwall4 = [Block(block_size * -3, HEIGHT - block_size * i, block_size) for i in range (1, 10)]
    startingwall5 = [Block(block_size * -4, HEIGHT - block_size * i, block_size) for i in range (1, 10)]
    #Combine the starting walls
    starting_walls = startingwall1 + startingwall2 + startingwall3 + startingwall4 + startingwall5

    #The walls at the end of the map
    endingwall1 = [PinkBlock((jumping_start + 45) * block_size, HEIGHT - block_size * i, block_size) for i in range (0, 10)]
    endingwall2 = [PinkBlock((jumping_start + 46) * block_size, HEIGHT - block_size * i, block_size) for i in range (0, 10)]
    endingwall3 = [PinkBlock((jumping_start + 47) * block_size, HEIGHT - block_size * i, block_size) for i in range (0, 10)]
    endingwall4 = [PinkBlock((jumping_start + 48) * block_size, HEIGHT - block_size * i, block_size) for i in range (0, 10)]
    endingwall5 = [PinkBlock((jumping_start + 49) * block_size, HEIGHT - block_size * i, block_size) for i in range (0, 10)]
    #Combine ending walls 
    ending_walls = endingwall1 + endingwall2 + endingwall3 + endingwall4 + endingwall5

    jumpingBlocks = [
    #Blocks on the floor level
    Block(block_size * 4, HEIGHT - block_size * 2, block_size), 
    Block(block_size * 8, HEIGHT - block_size * 2, block_size), 
    Block(block_size * 16, HEIGHT - block_size * 2, block_size), 
    WoodBlock(block_size * 20, HEIGHT - block_size * 2, block_size),
    WoodBlock(block_size * 24, HEIGHT - block_size * 2, block_size),
    WoodBlock(block_size * 28, HEIGHT - block_size * 2, block_size),
    WoodBlock(block_size * 32, HEIGHT - block_size * 2, block_size),

    #First Higher blocks
    Block(block_size * 12, HEIGHT - block_size * 4, block_size), 
    WoodBlock(block_size * 20, HEIGHT - block_size * 4, block_size),
    WoodBlock(block_size * 24, HEIGHT - block_size * 4, block_size),
    WoodBlock(block_size * 28, HEIGHT - block_size * 4, block_size),
    WoodBlock(block_size * 32, HEIGHT - block_size * 4, block_size),

    #Highest blocks 
    WoodBlock(block_size * 24, HEIGHT - block_size * 6, block_size),
    WoodBlock(block_size * 28, HEIGHT - block_size * 6, block_size),
    WoodBlock(block_size * 32, HEIGHT - block_size * 6, block_size),

    #The blocks to jump on at the end of the level 
    GrassBlock((jumping_start + 3) * block_size, HEIGHT - block_size * 1, block_size),

    GrassBlock((jumping_start + 6) * block_size, HEIGHT - block_size * 1, block_size),
    GrassBlock((jumping_start + 6) * block_size, HEIGHT - block_size * 2, block_size),

    OrangeBlock((jumping_start + 11) * block_size, HEIGHT - block_size * 1, block_size),
    OrangeBlock((jumping_start + 11) * block_size, HEIGHT - block_size * 2, block_size),

    OrangeBlock((jumping_start + 15) * block_size, HEIGHT - block_size * 1, block_size),
    OrangeBlock((jumping_start + 15) * block_size, HEIGHT - block_size * 2, block_size),
    OrangeBlock((jumping_start + 15) * block_size, HEIGHT - block_size * 3, block_size),

    PinkBlock((jumping_start + 19) * block_size, HEIGHT - block_size * 1, block_size),
    PinkBlock((jumping_start + 19) * block_size, HEIGHT - block_size * 2, block_size),
    PinkBlock((jumping_start + 19) * block_size, HEIGHT - block_size * 3, block_size),
    PinkBlock((jumping_start + 19) * block_size, HEIGHT - block_size * 4, block_size),

    PinkBlock((jumping_start + 25) * block_size, HEIGHT - block_size * 1, block_size),
    PinkBlock((jumping_start + 25) * block_size, HEIGHT - block_size * 2, block_size),
    PinkBlock((jumping_start + 25) * block_size, HEIGHT - block_size * 3, block_size),
    PinkBlock((jumping_start + 25) * block_size, HEIGHT - block_size * 4, block_size),
    PinkBlock((jumping_start + 25) * block_size, HEIGHT - block_size * 5, block_size)

]

    # List of all objects in the game including traps and spikes
    objects =  [
                *stone_floor, 
                *wood_floor,
                *scale_floor, 
                *ending_floor, 
                *ending_walls,
                *scale_tunnels,
                *starting_walls,
                *jumpingBlocks,
                *spikes1, 
                *spikes2
                ]

    return objects