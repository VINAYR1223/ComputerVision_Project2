import cv2 as cv
import mediapipe as mp
import Utility as Utility


def main():

    #Setting up the camera resolution for capturing the image.
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)

    #Setting up the hand detection model.
    mphands = mp.solutions.hands
    hands = mphands.Hands(
        max_num_hands = 2,
        min_detection_confidence = 0.7,
        min_tracking_confidence=0.5
    )
    wasopen = [False,False]
    jutsu_scale = [0.5,0.5]
    frameNumber = [0,0]



    #Loading the animation frames
    Rasengan = Utility.LoadFrames(r"C:\Users\ADMIN\Documents\Naruto_Organized\Effects\Effect1")
    Chidori = Utility.LoadFrames(r"C:\Users\ADMIN\Documents\Naruto_Organized\Effects\Effect2")


    mpdraw = mp.solutions.drawing_utils #we will use it to draw the landmark and the connection between them.

    #start caputing the hand
    while cap.isOpened():

        det, img = cap.read()
         
        #If no image is captured or detected then exit the loop
        if not det:
            break
        
        #height and width of the captured image
        h,w,_ = img.shape

        #Since front camera flips the img we will flip it back to make it like a mirror
        img = cv.flip(img,1)

        #OpenCv use BGR format but MediaPipe used RGB format so we will convert the BGR img to RGB img
        RGBimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        
        #processes the img and detects the hands
        processed = hands.process(RGBimg)
        if processed.multi_hand_landmarks and processed.multi_handedness:
            
            for i,handlms in enumerate(processed.multi_hand_landmarks):
                # print(processed.multi_handedness)
                label = processed.multi_handedness[i].classification[0].label
                isRight = (label == "Right")

                idx = 1 if isRight else 0
                isOpen = Utility.isopen(handlms)


                #Reset the justsu if the hand was closed and open
                if isOpen and not wasopen[idx]:
                    jutsu_scale[idx] = 0.5
                    frameNumber[idx] = 0



                #Increas the scale to give the growing effect if the hand is open
                if isOpen and isRight:
                    jutsu_scale[idx] = min(0.7,jutsu_scale[idx]+0.005)
                    color = (0,140,255) #Orange color for right hand to show the activation of RasenShuriken

                elif isOpen and not isRight:
                    jutsu_scale[idx] = min(0.8,jutsu_scale[idx]+0.005)
                    color = (255,0,200) #Purpel color for left hand to show the activation of Chidori
                else:
                    color = (200,200,200)
                #Changing the color of the hand connection in accordance with the jutsu
                mpdraw.draw_landmarks(img,handlms,mphands.HAND_CONNECTIONS,
                                      landmark_drawing_spec = mpdraw.DrawingSpec(color = color,thickness =2),
                                      connection_drawing_spec = mpdraw.DrawingSpec(color = color,thickness =3))
                


                #Coordinate or the position on the hand to display the vfx
                wrist = handlms.landmark[0]

                cx = int(wrist.x * w)
                cy = int(wrist.y * h)


                #Adding the vfx to the image
                if isOpen and isRight:
                    if frameNumber[idx] >= len(Rasengan):
                        frameNumber[idx] = 139

                    vfx = Rasengan[frameNumber[idx]]
                    img = Utility.OverLay(img,vfx, cx+25, cy - 150, jutsu_scale[idx])
                    frameNumber[idx] += 2    

                elif isOpen and not isRight:
                    vfx = Chidori[frameNumber[idx] % len(Chidori)]
                    img = Utility.OverLay(img,vfx,cx,cy - 75,jutsu_scale[idx])
                    frameNumber[idx] += 2
                        
                wasopen[idx] = isOpen
        
        cv.imshow("CAPTURE",img)

        if cv.waitKey(1) == 27:
            break
            

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

            
        


