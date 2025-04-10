'''
@author: Sudip Vikram Adhikari
@company: Beyond Apogee
We will be using this example to control 5 different LEDs using the tips of our thumb and index finger.
This is similar to the finger counter example except that we will be controlling the LEDs based on the number of fingers.
'''

from sajilocv import *

# instantiating
sajilo = sajilocv()
htracker = sajilo.hand_tracking(sajilo)

# instantiating tools   # we will need this for the range function
tools = sajilo.tools(sajilo,htracker)

# initializing the ucontroller class
#arduino = sajilo.ucontroller(sajilo,port="/dev/ttyACM0",baudrate=9600,timeout=1)
#arduino = sajilo.ucontroller(sajilo,port="/COM1",baudrate=9600,timeout=1)
arduino = sajilo.ucontroller(sajilo,port="/dev/ttyUSB1",baudrate=9600,timeout=1)

while True:
    # start tracking hands
    htracker.track_hands()

    # getting an image corresponding to the number of fingers  # currently only tracks the right hand
    fingers = htracker.determine_hand_position()  # this will give us the state of all five fingers
    tools.load_images_from_dir(dir_path="assets")
    if fingers:
        print(fingers)
        htracker.draw_rectangle(fill=True, color=(255, 255, 255), start=(147, 215), end=(180, 245))
        htracker.display_text(text="fingers:", org=(30, 240), font="simplex", font_scale=1, color=(255, 0, 0),
                              thickness=2)
        thumb, index, middle, ring, pinky = fingers
        if fingers == [0, 0, 0, 0, 0]:
            tools.overlay_image(org=(10, 10), img_num=0) # overlays the image corresponding to the counted fingers
            htracker.display_text(text="0", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0, 1, 0, 0, 0]:
            tools.overlay_image(org=(10, 10), img_num=1)
            htracker.display_text(text="1", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0, 1, 1, 0, 0]:
            tools.overlay_image(org=(10, 10), img_num=2)
            htracker.display_text(text="2", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0, 1, 1, 1, 0]:
            tools.overlay_image(org=(10, 10), img_num=3)
            htracker.display_text(text="3", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [0, 1, 1, 1, 1]:
            tools.overlay_image(org=(10, 10), img_num=4)
            htracker.display_text(text="4", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)
        elif fingers == [1, 1, 1, 1, 1]:
            tools.overlay_image(org=(10, 10), img_num=5)
            htracker.display_text(text="5", org=(150, 240), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)

    # sending serial data to arduino or any other microcontroller through serial
    fingers = htracker.determine_hand_position()
    if fingers:
        print(fingers)
        arduino.send_serial_data(data=fingers)

    # display the video output
    htracker.display_video()