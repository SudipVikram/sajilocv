'''
@author: Sudip Vikram Adhikari
@company: Beyond Apogee
In this game our index finger will work as a controller for the astronaut who has to hunt down aliens
by colliding with them to score a point. Rest is similar to the game controlled by arrow keys.
'''

from sajilocv import *
from sajilopygame import *

# initializing window
game = sajilopygame(wwidth=800, wheight=600)
sajilo = sajilocv()
htracking = sajilo.hand_tracking(sajilo)

# changing widow title and icon
game.window_title("Superman Astronaut")
game.favicon("assets/favicon.png")

# creating characters
game.create_player("assets/astronaut.png")
game.create_enemy("assets/alien.png")

# loading sounds
game.load_sound(sound_path="assets/happy.mp3", type="collision", volume=1)
game.load_sound(sound_path="assets/gameloop.mp3", type="background", volume=0.2)

htracking.update_max_hands(1)

while True:
    htracking.track_hands()
    htracking.circle_landmark(8, 15)

    # changing background parameters
    game.background_color(color=(255, 0, 0))
    game.background_image(image_path="assets/background.png")

    # loading characters
    game.load_enemy()
    game.load_player()

    # assigning arrow keys
    game.assign_lr_keys(type="player", intensity=(5, 10))
    game.assign_ud_keys(type="player", intensity=(10, 5))

    # moving enemy left right and up and down
    game.bounce_left_right(type="enemy", speed=10)
    game.bounce_up_down(type="enemy", speed=20)

    # getting position of landmark no. 8 and updating the player's position with it
    htx, hty = htracking.find_landmark_position(hand_no=0, landmark_id=8, draw=False)
    if htx and hty:
        game.update_position(type="player", xpos=htx, ypos=hty)

    # collision event
    game.assign_collision_effect(type="enemy", effect="random")
    game.detect_collision(collision_by="player", collision_with="enemy")

    # displaying the scoreboard
    game.display_score()
    game.display_lives()

    # bounding the characters inside the window
    game.bound_to_window(type="player")
    game.bound_to_window(type="enemy")

    # output video for hand tracking
    htracking.display_video()

    # refreshing window
    game.refresh_window()



