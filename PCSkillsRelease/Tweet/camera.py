import cv2
import time
import tweetomatic
import os
import path

# Open the camera
cap = cv2.VideoCapture(0)
 
while True:
    # Specify the countdown
    j = 50
    # set the key for the countdown to begin
    if j == 50:
        while j>=10:
            ret, img = cap.read()
            # Display the countdown after 10 frames so that it is easily visible otherwise,
            # it will be fast. You can set it to anything or remove this condition and put 
            # countdown on each frame
            if j%10 == 0:
                # specify the font and draw the countdown using puttext
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,str(j//10),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)
            cv2.imshow('Camera',img)
            cv2.waitKey(125)
            j = j-1
        else:
            ret, img = cap.read()
            # Display the clicked frame for 1 sec.
            # You can increase time in waitKey also
            cv2.imshow('Camera',img)
            cv2.waitKey(1000)
            # Save the frame
            cv2.imwrite(path.path + 'image.jpg',img)
            cv2.waitKey(100)
            taskvalue = 'python ' + path.path + 'tweetomatic.py -i ' + path.path + 'image.jpg' + ' -t "#PCSkillSelfie"'
            #print (taskvalue)
            #os.system('python tweetomatic.py -i .\image.jpg -t "#PCSkillSelfie"')
            os.system(taskvalue)
            break

cap.release()
cv2.destroyAllWindows()