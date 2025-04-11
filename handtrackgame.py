import random

from sajilocv import *
from sajilopygame import *

# creating instances of sajilocv
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)

# creating instances of sajilopygame
game = sajilopygame()
game2 = sajilopygame()
game3 = sajilopygame()

# one time settings for sajilopygame
game.window_title("Egg in the Basket")

# creating characters for the game
game.create_player(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/basket.png", org=(370, 400))
game.create_object(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/egg.png", org=(100, 100))
game.create_enemy(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/duck.png", org=(400, 10))
game2.create_enemy(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/duck.png", org=(400, 10))
game3.create_enemy(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/duck.png", org=(400, 10))

# working with sounds
game.load_sound(sound_path="examples/Hand Tracking Games/Catch the Eggs/assets/background.wav", type="background", volume=0.5)
game.load_sound(sound_path="examples/Hand Tracking Games/Catch the Eggs/assets/egg-in-basket.wav", type="collision", volume=0.5)
game.load_sound(sound_path="examples/Hand Tracking Games/Catch the Eggs/assets/egg-cracking.mp3", type="death", volume=0.5)


# max hands to be tracked
htracker.update_max_hands(1)    # setting it to one hand only

while True:
    htracker.track_hands()
    htracker.circle_landmark(8,15)

    # loading for game
    game.background_image(image_path="examples/Hand Tracking Games/Catch the Eggs/assets/background.jpg")
    game.load_player()
    game.load_object()
    game.load_enemy()
    game2.load_enemy()
    game3.load_enemy()

    # finding landmark's position using handtracking
    hx, hy = htracker.find_landmark_position(hand_no=0, landmark_id=8, draw=False)
    # moving the basket's position using hand tracking
    if hx:
        game.update_position(type="player",xpos=hx,ypos=400)

    # assigning game keys
    game.assign_lr_keys(type="player",intensity=(20,20))

    # moving the duck left to right
    game.move_right_to_left(type="enemy",speed=random.randint(5,30))
    game2.move_right_to_left(type="enemy",speed=random.randint(5,30))
    game3.move_right_to_left(type="enemy",speed=random.randint(5,30))
    ex, ey = game.find_position(type="enemy")
    # once it goes out of bounds
    if ex<0:
        game.update_position(type="enemy",xpos=900, ypos=random.randint(5,150))
    # repeating for the other two ducks
    ex2, ey2 = game2.find_position(type="enemy")
    # once it goes out of bounds
    if ex2 < 0:
        game2.update_position(type="enemy", xpos=900, ypos=random.randint(5, 150))
    ex3, ey3 = game3.find_position(type="enemy")
    # once it goes out of bounds
    if ex3 < 0:
        game3.update_position(type="enemy", xpos=900, ypos=random.randint(5, 150))

    # moving the object left to right
    game.move_top_to_bottom(type="object",speed=30)
    ox, oy = game.find_position(type="object")
    # once it goes out of bounds
    if oy>game.wheight:
        game.update_position(type="object",xpos=random.randint(50,900), ypos=0)


    '''# egg(object) shadowing the duck(enemy)
    enemy_pos = game.find_position(type="enemy")
    # updating the object's position
    x, y = enemy_pos
    x = x + 70
    y = y + 85

    # assigning triggers
    game.assign_trigger(type="object",start_pos=(x,y),dir="t2b",speed=50)'''

    # collision detection
    # assign collision effect
    game.assign_collision_effect(type="object", effect="disappear")
    #game.assign_collision_effect(type="enemy", effect="random")

    # detect collision
    game.detect_collision(collision_by="object",collision_with="player")

    # display the score
    game.display_score()

    # bounding the basket
    game.bound_to_window(type="player")

    # bare essentials
    htracker.display_video()
    game.refresh_window()