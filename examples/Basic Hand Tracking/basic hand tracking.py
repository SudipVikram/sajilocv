'''
@author: Sudip Vikram Adhikari
@company: Beyond Apogee
This is a basic working example of sajilocv's hand tracking. Just the bare minimum code to get things working.
'''

from sajilocv import *

# instantiating
sajilo = sajilocv()
htracker = sajilo.hand_tracking(sajilo)

while True:
    # start tracking hands
    htracker.track_hands()

    # show hand landmarks along with its connections
    htracker.show_hand_connections()

    # display the video output
    htracker.display_video()