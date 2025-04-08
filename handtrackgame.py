from sajilocv import *
from sajilopygame import *

# creating instances of sajilocv
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)

# creating instances of sajilopygame
game = sajilopygame()

# one time settings for sajilopygame
game.window_title("Egg in the Basket")

# creating characters for the game
game.create_player(image_path="eggs/basket.png", org=(370, 400))
game.create_object(image_path="eggs/egg.png", org=(100, 100))


# max hands to be tracked
htracker.update_max_hands(1)    # setting it to one hand only

while True:
    htracker.track_hands()
    htracker.circle_landmark(8,15)

    # loading for game
    game.background_image(image_path="eggs/background.jpg")
    game.load_player()
    game.load_object()



    game.assign_lr_keys(type="player",intensity=(20,20))

    htracker.display_video()
    game.refresh_window()