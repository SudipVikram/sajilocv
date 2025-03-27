from BareMinimum import tools
from SajiloCV import *

# creating an instance of everything
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)

htracker.update_max_hands(2)

# instantiating tools
tools = sajilo.Tools(sajilo)

while True:
    htracker.track_hands()
    htracker.show_hand_connections()

    # creating a slider
    length = htracker.length_across_landmarks()
    if length:
        range_val = tools.find_range(length,min=0,max=100,lmin=150,lmax=400,order="inverted")
        upd_val = range_val + 400
        #print(f"Length: {length}")
        print(f"Range: {upd_val}")
        print("hello Slacker")
        htracker.draw_vertical_slider(val=upd_val)


    htracker.display_video()