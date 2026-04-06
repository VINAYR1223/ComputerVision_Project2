import math
import cv2 as cv
import sys
import os 

sys.path.append(os.path.abspath("Utility.py"))
def isopen(handlms):

    #First we will get the coordinates of wrist
    x =(handlms.landmark[0].x)
    y =(handlms.landmark[0].y)

    #We will use this variable to keep track of how many fingers are closed
    count = 0

    tips = [8,12,16,20]
    pips = [6,10,14,18]


    for i in range(4):

        #coordinate of tip of the finger
        x1 = (handlms.landmark[tips[i]].x)
        y1 = (handlms.landmark[tips[i]].y)

        #coordinate of pip/ The middle joint of the finger
        x2 = (handlms.landmark[pips[i]].x)
        y2 = (handlms.landmark[pips[i]].y)

        #calculating the distance b/w tip and the wrist 
        TipToWrist = math.hypot((x - x1),(y - y1))

        #calculating the distance b/w pip and the wrist
        PipToWrist = math.hypot((x - x2),(y - y2))

        #if the distance bw tip to wrist is more than the distance bw the pip to wrist thwn we can say that the hand is open
        if TipToWrist > PipToWrist:
            count += 1


    #if atleast 3 fingers are open we can consider the hand is open
    return count >= 3


def LoadFrames(folder):
    frames = []
    Files = sorted(os.listdir(folder))

    for file in Files:
        path = os.path.join(folder,file)
        img = cv.imread(path,cv.IMREAD_UNCHANGED)
        
        if img is None:
            continue

        frames.append(img)
    
    return frames


def OverLay(Screen, vfx, cx, cy, scale = 1.0):

    h,w = vfx.shape[:2]

    #Resize the vfx to the given scale
    vfx = cv.resize(vfx, (int(w * scale), int(h * scale)))
    new_h, new_w = vfx.shape[:2]

     #Position of the vfx on the screen
    x1 = int(cx - new_w/2)
    y1 = int(cy - new_h/2)
    x2 = x1 + new_w
    y2 = y1 + new_h


    #Clip the display position to the screen
    x1_clip = max(0,x1)
    y1_clip = max(0,y1)

    x2_clip = min(Screen.shape[1], x2)
    y2_clip = min(Screen.shape[0], y2)

    if x1_clip >= x2_clip or y1_clip >= y2_clip:
        return Screen


    #crop the part that is out of the screen
    vfx_x1 = x1_clip - x1
    vfx_y1 = y1_clip - y1

    vfx_x2 = vfx_x1 + (x2_clip - x1_clip)
    vfx_y2 = vfx_y1 + (y2_clip - y1_clip)

    vfx_cropped = vfx[vfx_y1:vfx_y2, vfx_x1:vfx_x2]

    alpha = vfx_cropped[:,:,3]/255.0 #The transperency of the image

    #Adding the vfx to the screen/the diplay image
    for c in range(3):
        Screen[y1_clip:y2_clip, x1_clip:x2_clip,c] = (alpha * vfx_cropped[:,:,c] + (1 - alpha)*Screen[y1_clip:y2_clip, x1_clip:x2_clip,c])

    return Screen



