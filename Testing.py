from SajiloCV import *

# creating an instance of everything
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)

htracker.update_max_hands(2)

# instantiating tools
tools = sajilo.Tools(sajilo)

while True:
    htracker.track_hands()
    #htracker.show_hand_connections()
    htracker.line_across_landmarks()

    # creating a slider
    length = htracker.length_across_landmarks()
    if length:
        range_val = tools.find_range(length,min=150,max=400,lmin=20,lmax=100,order="descending")
        print(f"Length: {length}")
        #range_val = 100 + range_val
        print(f"Range: {range_val}")
        htracker.draw_vertical_slider(val=range_val)


    htracker.display_video()