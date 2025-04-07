from sajilocv import SajiloCV

# Create an instance of SajiloCV
sajilo_cv = SajiloCV()
hand_tracker = sajilo_cv.HandTracking(sajilo_cv)

# change anything that you would want to configure here
hand_tracker.update_max_hands(2)  # Change to track 1 hand instead of 2
hand_tracker.update_frame_rate(30) # Change the frame rate to 60
hand_tracker.update_camera_index(0) # Change the camera index
hand_tracker.update_model_complexity(0)
hand_tracker.update_static_image_mode(False)
hand_tracker.update_min_detection_confidence(0.5)

while True:
    hand_tracker.track_hands()
    hand_tracker.show_hand_landmarks()
    hand_tracker.show_hand_connections()
    #hand_tracker.display_frame_rate(text="Rate: ",org=(30,50),font="script_complex", font_scale=1,color=(255,20,205),thickness=2)
    hand_tracker.display_real_fps()
    #hand_tracker.display_text(text="Press 'q' to quit",org=(30,110),font="duplex", font_scale=1,color=(0,0,255),thickness=1)
    #hand_tracker.print_landmarks()
    #hand_tracker.print_landmarks_in_pixels()
    #hand_tracker.circle_landmark(0,25)
    #hand_tracker.circle_landmark(4,10,(78,98,89))
    #hand_tracker.circle_landmark(radius=5, color=(255,255,255))
    list = hand_tracker.find_hand_position(0,False)
    if list and len(list) > 8:  # Ensure the list is not None and contains at least 9 elements
        print(list[8])

    hand_tracker.display_video()

hand_tracker.release_camera()
