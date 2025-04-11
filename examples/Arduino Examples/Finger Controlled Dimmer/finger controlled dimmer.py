'''
@author: Sudip Vikram Adhikari
@company: Beyond Apogee
We will be using this example to control a dimmer by sending pwm data to an arduino.
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

    # creating a vertical slider
    htracker.draw_rectangle(fill=False)  # creates a default rectangle of default size and position
    length = htracker.length_across_landmarks()  # finds the length between the tip of our thumb and index finger
    if length:
        # find range function inside tools helps us map a range to our slider
        range_val = tools.find_range(length, min=150, max=400, lmin=20, lmax=100, order="descending")
        htracker.draw_vertical_slider(val=range_val)  # draws a slider according to the range found
        disp_range_val = tools.find_range(length, min=0, max=100, lmin=20, lmax=100, order="ascending")
        htracker.display_text(text=f"{int(disp_range_val)}%", org=(30, 440), font="duplex", font_scale=1,
                              color=(0, 255, 0), thickness=1)  # displaying the range percentage

    # determining intensity data before sending to arduino
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

            htracker.draw_vertical_slider(val=rnge)

            htracker.display_text(text=f"{rnge2}", org=(178, 38), font="duplex", font_scale=1, color=(0, 255, 0), thickness=2)

            arduino.send_serial_data(data=rnge2)


    # display the video output
    htracker.display_video()