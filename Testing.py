from SajiloCV import *

# creating an instance of everything
sajilo = SajiloCV()
htracker = sajilo.HandTracking(sajilo)
arduino = sajilo.Controller(sajilo,port="/dev/ttyACM0",baudrate=9600,timeout=1)

htracker.update_max_hands(1)

# instantiating tools
tools = sajilo.Tools(sajilo,htracker)
#tools = sajilo.Tools(sajilo)

while True:
    htracker.track_hands()
    #htracker.show_hand_connections()
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

    ''' getting an image corresponding to the number of fingers 
    fingers = htracker.determine_hand_position()
    tools.load_images_from_dir(dir_path="fingers")
    if fingers:
        print(fingers)
        htracker.draw_rectangle(fill=True, color=(255, 255, 255),start=(147,215),end=(180,245))
        htracker.display_text(text="fingers:", org=(30, 240), font="simplex", font_scale=1, color=(255, 0, 0), thickness=2)
        thumb, index, middle, ring, pinky = fingers
        if fingers == [0,0,0,0,0]:
            tools.overlay_image(org=(10,10),img_num=3)
            htracker.display_text(text="0",org=(150,240),font="duplex", font_scale=1,color=(0,255,0),thickness=2)
        elif fingers == [0,1,0,0,0]:
            tools.overlay_image(org=(10,10),img_num=0)
            htracker.display_text(text="1", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0,1,1,0,0]:
            tools.overlay_image(org=(10,10),img_num=4)
            htracker.display_text(text="2", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0,1,1,1,0]:
            tools.overlay_image(org=(10,10),img_num=2)
            htracker.display_text(text="3", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0,1,1,1,1]:
            tools.overlay_image(org=(10,10),img_num=1)
            htracker.display_text(text="4", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [1,1,1,1,1]:
            tools.overlay_image(org=(10,10),img_num=5)
            htracker.display_text(text="5", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)'''


    ''' getting the position of the landmark
    index_tip = htracker.find_landmark_position(hand_no=0,landmark_id=8,draw=True,color=(0,0,255))
    thumb_tip = htracker.find_landmark_position(hand_no=0,landmark_id=4,draw=True)

    print(f"Thumb tip: {thumb_tip}", f"Index tip: {index_tip}")'''

    ''' sending serial data to arduino
    fingers = htracker.determine_hand_position()
    if fingers:
        print(fingers)
        arduino.send_serial_data(data=fingers)'''

    ''' sending intensity data to arduino '''
    len = htracker.determine_hand_position()
    if len:
        htracker.draw_rectangle(fill=True, color=(255, 255, 255), start=(175, 13), end=(540, 45))
        htracker.display_text(text="Intensity:", org=(30, 40), font="simplex", font_scale=1, color=(255, 0, 0),
                              thickness=2)
        htracker.line_across_landmarks(hand_no=0, landmark_ids=(4, 8))
        len = htracker.length_across_landmarks(hand_no=0, landmark_ids=(4, 8))
        if len:
            rnge = tools.find_range(len, 150, 400, lmin=30, lmax=150,order="descending")
            rnge2 = tools.find_range(len, 0, 1023, lmin=30, lmax=150,order="ascending")

            #print(f"Length: {len}")
            htracker.draw_vertical_slider(val=rnge)

            print(f"Range: {rnge2}")
            htracker.display_text(text=f"{rnge2}", org=(178, 38), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)

            arduino.send_serial_data(data=rnge2)

    htracker.display_video()