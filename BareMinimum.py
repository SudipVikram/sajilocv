from SajiloCV import SajiloCV

# creating an instance of SajiloBot
sajilo_cv = SajiloCV()
hand_tracker = sajilo_cv.HandTracking(sajilo_cv)

hand_tracker.update_max_hands(2)
# most cameras support 640x480, 1280x720, 1920x1080
#hand_tracker.update_video_output(1920,1080)
#hand_tracker.update_min_detection_confidence(0.7)

while True:
    hand_tracker.track_hands()
    #hand_tracker.show_hand_landmarks()
    #hand_tracker.show_hand_connections()
    #hand_tracker.display_real_fps()
    #lmList = hand_tracker.find_hand_position(hand_no=0, draw=False)
    #hand_tracker.circle_landmark(4,15)
    #hand_tracker.circle_landmark(8,10)
    '''if lmList and len(lmList) > 8:
        print(lmList[2],lmList[8])
        hand_tracker.circle_landmark(2,15)
        hand_tracker.circle_landmark(8,10,(78,98,89))'''
    #hand_tracker.line_across_landmarks(landmark_ids=(4,8))
    #hand_tracker.get_landmarks_list()

    #hand_tracker.line_across_landmarks(landmark_ids=(4,8))
    #hand_tracker.line_across_landmarks(hand_no=1,landmark_ids=(4,8),color=(255,0,0))

    '''hand_tracker.line_across_landmarks(hand_no=0,landmark_ids=(4,8),color=(0,0,255),thickness=2,rcircle=10,center=True)
    hand_tracker.line_across_landmarks(hand_no=1,landmark_ids=(4,8),color=(0,255,0),thickness=2,rcircle=10,center=True)
    length1 = hand_tracker.length_across_landmarks(landmark_ids=(4,8))
    if length1:
        print(length1)
    length2 = hand_tracker.length_across_landmarks(hand_no=1,landmark_ids=(4,8))
    if length2:
        print(length2)
    #hand_tracker.center_across_landmarks(hand_no=0,landmark_ids=(4,8))
    #hand_tracker.center_across_landmarks(hand_no=1,landmark_ids=(4,8))
    if length1:
        if length1 < 20:
            hand_tracker.center_across_landmarks(hand_no=0,landmark_ids=(4,8),color=(255,0,0),rcircle=10)
            hand_tracker.center_across_landmarks(hand_no=1,landmark_ids=(4,8),color=(255,0,0),rcircle=10)
        else:
            hand_tracker.center_across_landmarks(hand_no=0,landmark_ids=(4,8),color=(0,255,0),rcircle=10)
            hand_tracker.center_across_landmarks(hand_no=1,landmark_ids=(4,8),color=(0,255,0),rcircle=10)'''

    '''hand_tracker.line_across_landmarks(landmark_ids=(4,8),color=(0,0,255),thickness=2,rcircle=10,center=True)
    autogui = sajilo_cv.AutoGUI(sajilo_cv)
    length1 = hand_tracker.length_across_landmarks(hand_no=0,landmark_ids=(4,8))
    if length1:
        if length1 < 50:
            autogui.decrease_volume()
        elif length1 > 50:
            autogui.increase_volume()
        elif length1 < 20:
            autogui.mute_volume()'''

    '''tools = sajilo_cv.Tools(sajilo_cv)
    length1 = hand_tracker.length_across_landmarks(hand_no=0,landmark_ids=(4,8))
    if length1:
        range1 = tools.find_range(length1,0,100,rangemin=30,rangemax=150)
        print(f"Length1: {length1}")
        print(f"Range1: {range1}")
    length2 = hand_tracker.length_across_landmarks(hand_no=1, landmark_ids=(4, 8))
    if length2:
        range2 = tools.find_range(length2, 0, 100, rangemin=30, rangemax=150)
        print(f"Length2: {length2}")
        print(f"Range2: {range2}")'''

    '''tools = sajilo_cv.Tools(sajilo_cv)
    length = hand_tracker.length_across_landmarks()
    if length:
        print(f"Length: {length}")
        range = tools.find_range(length,min=0,max=100,lmin=20,lmax=100)
        print(f"Range: {range}")
        #val = tools.find_range(range,min=400,max=150,lmin=30,lmax=150)
        #print(f"Val: {val}")
        #hand_tracker.draw_vertical_slider(val=val)
        hand_tracker.draw_vertical_slider(val=range)'''

    '''hand_tracker.draw_rectangle(fill=False)
    tools = sajilo_cv.Tools(sajilo_cv)
    length = hand_tracker.length_across_landmarks(hand_no=0,landmark_ids=(4,8))
    if length:
        range = tools.find_range(length,85,150,rangemin=30,rangemax=150)
        print(f"Length: {length}")
        print(f"Range: {range}")
        hand_tracker.draw_vertical_slider(val=range)'''

    #hand_tracker.draw_rectangle(fill=False)
    #hand_tracker.center_across_landmarks(hand_no=0)
    #hand_tracker.center_across_landmarks(hand_no=1,color=(255,0,0),rcircle=10)

    # bare essential - to display the video
    hand_tracker.display_video()