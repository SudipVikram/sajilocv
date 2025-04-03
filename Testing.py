from SajiloCV import *

# creating an instance of everything
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)

htracker.update_max_hands(1)

# instantiating tools
tools = sajilo.Tools(sajilo,htracker)
#tools = sajilo.Tools(sajilo)

while True:
    htracker.track_hands()
    htracker.show_hand_connections()
    #htracker.line_across_landmarks()

    # creating a slider
    '''htracker.draw_rectangle(fill=False)
    length = htracker.length_across_landmarks()
    if length:
        range_val = tools.find_range(length,min=150,max=400,lmin=20,lmax=100,order="descending")
        print(f"Length: {length}")
        #range_val = 100 + range_val
        print(f"Range: {range_val}")
        htracker.draw_vertical_slider(val=range_val)
        disp_range_val = tools.find_range(length, min=0, max=100, lmin=20, lmax=100, order="ascending")
        htracker.display_text(text=f"{int(disp_range_val)}%",org=(30,440),font="duplex", font_scale=1,color=(0,255,0),thickness=1)
    '''
    # working with files in a dir
    #tools.print_dir_list(dir_path="fingers")

    #fileList = tools.find_dir_list(dir_path="fingers")
    '''list_of_overlays = tools.load_images_from_dir(dir_path="fingers")
    #print(list_of_overlays)
    tools.slice_image(img_num=1)'''

    ''' finding the right image for the number of fingers tracked '''
    #htracker.print_landmarks()
    #htracker.find_hand_position(draw=False)

    ''' getting an image corresponding to the number of fingers'''
    fingers = htracker.determine_hand_position()
    tools.load_images_from_dir(dir_path="fingers")
    if fingers:
        print(fingers)
        thumb, index, middle, ring, pinky = fingers
        if fingers == [0,0,0,0,0]:
            tools.overlay_image(img_num=3)
        elif fingers == [0,1,0,0,0]:
            tools.overlay_image(img_num=0)
        elif fingers == [0,1,1,0,0]:
            tools.overlay_image(img_num=4)
        elif fingers == [0,1,1,1,0]:
            tools.overlay_image(img_num=2)
        elif fingers == [0,1,1,1,1]:
            tools.overlay_image(img_num=1)
        elif fingers == [1,1,1,1,1]:
            tools.overlay_image(img_num=5)

    htracker.display_video()