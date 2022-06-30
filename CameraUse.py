import cv2
import time
class CameraUse():
    def UseCamera():
        # SET THE COUNTDOWN TIMER       for simplicity we set it to 3        We can also take this as input
        TIMER = int(1)

        cap = cv2.VideoCapture(0)

        while True:
             # Read and display each frame
            ret, img = cap.read()
            cv2.imshow('a', img)

            # check for the key pressed
            k = cv2.waitKey(10)

            # set the key for the countdown         # to begin. Here we set q       # if key pressed is q
            if True:
                prev = time.time()

                while TIMER >= 0:
                    ret, img = cap.read()

                    # Display countdown on each frame   # specify the font and draw the     # countdown using puttext
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img, str(TIMER),
                                (200, 250), font,
                                7, (0, 255, 255),
                                4, cv2.LINE_AA)
                    cv2.imshow('a', img)
                    cv2.waitKey(10)

                    # current time
                    cur = time.time()

                    # Update and keep track of Countdown    # if time elapsed is one second      # than decrease the counter
                    if cur-prev >= 1:
                        prev = cur
                        TIMER = TIMER-1

                else:
                    ret, img = cap.read()

                    # Display the clicked frame for 2      # sec.You can increase time in       # waitKey also
                    cv2.imshow('a', img)

                    # time for which image displayed    #cv2.waitKey(20)         # Save the frame
                    cv2.imwrite('camera.jpg', img)

                    # HERE we can reset the Countdown timer     # if we want more Capture without closing        # the camera
                    break

            # Press Esc to exit
            elif k == 27:
                break
            
        cap.release()
        cv2.destroyAllWindows()


    UseCamera()