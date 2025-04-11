'''
@author: Sudip Vikram Adhikari
@company: Beyond Apogee
In this game our index finger will work as a controller for the basket. Rest is similar to the game controlled by arrow keys.
'''

from sajilocv import *
from sajilopygame import *

# creating instances of sajilocv
sajilo = sajilocv()
htracker = sajilo.hand_tracking(sajilo)

# creating instances of sajilopygame
game = sajilopygame()
goose2 = sajilopygame()
goose3 = sajilopygame()

# one time settings for sajilopygame
game.window_title("Catch the Eggs")

# creating characters for the game
game.create_player(image_path="assets/basket.png", org=(370, 400))
game.create_object(image_path="assets/egg.png", org=(100, 100))
game.create_enemy(image_path="assets/duck.png", org=(400, 10))
goose2.create_enemy(image_path="assets/duck.png", org=(400, 10))
goose3.create_enemy(image_path="assets/duck.png", org=(400, 10))

# working with sounds
game.load_sound(sound_path="assets/background.wav", type="background", volume=0.5)
game.load_sound(sound_path="assets/egg-in-basket.wav", type="collision", volume=0.5)

# max hands to be tracked
htracker.update_max_hands(1)    # setting it to one hand only

while True:
    htracker.track_hands()
    htracker.circle_landmark(8,15)

    # loading characters for the game
    game.background_image(image_path="assets/background.jpg")
    game.load_player()
    game.load_object()
    game.load_enemy()
    goose2.load_enemy()
    goose3.load_enemy()

    # finding landmark's position using handtracking
    hx, hy = htracker.find_landmark_position(hand_no=0, landmark_id=8, draw=False)
    # moving the basket's position using hand tracking
    if hx:
        game.update_position(type="player", xpos=hx, ypos=400)

    # assigning game keys   # just for redundancy
    game.assign_lr_keys(type="player", intensity=(20, 20))

    # moving the geese left to right
    game.move_right_to_left(type="enemy",speed=random.randint(5,30))
    goose2.move_right_to_left(type="enemy",speed=random.randint(5,30))
    goose3.move_right_to_left(type="enemy",speed=random.randint(5,30))
    # finding the position of the enemy, which is the main goose
    ex, ey = game.find_position(type="enemy")
    # once it goes out of bounds    # checking for edge
    if ex<0:
        game.update_position(type="enemy",xpos=900, ypos=random.randint(5,150))     # randomising the y-axis position
    # repeating for the other two goose
    ex2, ey2 = goose2.find_position(type="enemy")
    # once it goes out of bounds
    if ex2 < 0:
        goose2.update_position(type="enemy", xpos=900, ypos=random.randint(5, 150))
    ex3, ey3 = goose3.find_position(type="enemy")
    # once it goes out of bounds
    if ex3 < 0:
        goose3.update_position(type="enemy", xpos=900, ypos=random.randint(5, 150))

    # moving the object left to right  # object here meaning the egg
    game.move_top_to_bottom(type="object",speed=20)
    ox, oy = game.find_position(type="object")
    # once it goes out of bounds
    if oy>game.wheight:
        game.update_position(type="object",xpos=random.randint(50,900), ypos=0)

    # collision detection
    # assign collision effect
    game.assign_collision_effect(type="object", effect="disappear")

    # detect collision
    game.detect_collision(collision_by="object",collision_with="player")

    # display the scoreboard
    game.display_score()

    # bounding the basket
    game.bound_to_window(type="player")

    # bare essentials
    htracker.display_video()
    game.refresh_window()