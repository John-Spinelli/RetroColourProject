import numpy as np
import cv2 as cv


def nothing(x):
    print(x)

cap = cv.VideoCapture(1)
ret, img = cap.read()
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(width, height)

LOW = 0
HIGH = 255

blur_v = 0
blur_a = 5

cv.namedWindow('Tracking')
cv.createTrackbar('Thresh 1','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 2','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 3','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 4','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 5','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 6','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 7','Tracking',0,255, nothing)

'''
cv.createTrackbar('Low_HUE','Tracking',0,255, nothing)
cv.createTrackbar('Low_SATURATION','Tracking',0,255, nothing)
cv.createTrackbar('Low_VALUE','Tracking',0,255, nothing)
cv.createTrackbar('Up_HUE','Tracking',0,255, nothing)
cv.createTrackbar('Up_SATURATION','Tracking',0,255, nothing)
cv.createTrackbar('Up_VALUE','Tracking',0,255, nothing)
'''

# Create White Base
w = np.zeros([height, width,3], np.uint8)
w = cv.rectangle(w, (0,0), (width, height), (245,245,245), -1)

# Create Yellow Base
y = np.zeros([height, width,3], np.uint8)
y = cv.rectangle(y, (0,0), (width, height), (138,255,255), -1)
#cv.imshow('Yellow Colour', y)

# Create Orange Base
o = np.zeros([height, width,3], np.uint8)
o = cv.rectangle(o, (0,0), (width, height), (79,189,255), -1)
#cv.imshow('Orange Colour', o)

# Create Red Base
r = np.zeros([height, width,3], np.uint8)
r = cv.rectangle(r, (0,0), (width, height), (0,0,210), -1)

# Create Pink Base
p = np.zeros([height, width,3], np.uint8)
p = cv.rectangle(p, (0,0), (width, height), (127,0,173), -1)

# Create Blue Base
b1 = np.zeros([height, width,3], np.uint8)
b1 = cv.rectangle(b1, (0,0), (width, height), (200,0,0), -1)

# Create Dark Blue Base
b2 = np.zeros([height, width,3], np.uint8)
b2 = cv.rectangle(b2, (0,0), (width, height), (120,0,0), -1)

while(cap.isOpened()):
    ret, img = cap.read()
    if ret == True:

        cv.imshow('image',img)
        # Blur image before masking -- vs. blur result
        if blur_v == 1:
            img = cv.GaussianBlur(img, (blur_a,blur_a), 0)
            img = cv.GaussianBlur(img, (blur_a,blur_a), 0)

        # White Colours
        # 0 0 202   255 47 255  ===== likely reduce 
        w_LH = LOW
        w_LS = LOW
        w_LV = cv.getTrackbarPos('Thresh 1','Tracking')
        w_UH = HIGH
        w_US = HIGH
        w_UV = HIGH

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_w = np.array([w_LH, w_LS, w_LV])
        Upper_w = np.array([w_UH, w_US, w_UV])

        mask = cv.inRange(hsv, Lower_w, Upper_w)
        mask = mask.astype(np.uint8)
        white_mask = cv.bitwise_and(w,w,mask = mask)

        #cv.imshow('white_res', white_mask)

        # Yellow Colours
        y_LH = LOW
        y_LS = LOW
        y_LV = cv.getTrackbarPos('Thresh 2','Tracking')
        y_UH = HIGH
        y_US = HIGH
        y_UV = cv.getTrackbarPos('Thresh 1','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_y = np.array([y_LH, y_LS, y_LV])
        Upper_y = np.array([y_UH, y_US, y_UV])

        mask = cv.inRange(hsv, Lower_y, Upper_y)
        yellow_mask = cv.bitwise_and(y,y,mask = mask)

        #cv.imshow('yellow_res', yellow_mask)

        # Orange Colours
        o_LH = LOW
        o_LS = LOW
        o_LV = cv.getTrackbarPos('Thresh 3','Tracking')
        o_UH = HIGH
        o_US = HIGH
        o_UV = cv.getTrackbarPos('Thresh 2','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_o = np.array([o_LH, o_LS, o_LV])
        Upper_o = np.array([o_UH, o_US, o_UV])

        mask = cv.inRange(hsv, Lower_o, Upper_o)
        orange_mask = cv.bitwise_and(o,o,mask = mask)

        #cv.imshow('orange_res', orange_mask)

        # Red Colours
        r_LH = LOW
        r_LS = LOW
        r_LV = cv.getTrackbarPos('Thresh 4','Tracking')
        r_UH = HIGH
        r_US = HIGH
        r_UV = cv.getTrackbarPos('Thresh 3','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_r = np.array([r_LH, r_LS, r_LV])
        Upper_r = np.array([r_UH, r_US, r_UV])

        mask = cv.inRange(hsv, Lower_r, Upper_r)
        red_mask = cv.bitwise_and(r,r,mask = mask)

        # Pink Colours
        p_LH = LOW
        p_LS = LOW
        p_LV = cv.getTrackbarPos('Thresh 5','Tracking')
        p_UH = HIGH
        p_US = HIGH
        p_UV = cv.getTrackbarPos('Thresh 4','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_p = np.array([p_LH, p_LS, p_LV])
        Upper_p = np.array([p_UH, p_US, p_UV])

        mask = cv.inRange(hsv, Lower_p, Upper_p)
        pink_mask = cv.bitwise_and(p,p,mask = mask)

        #cv.imshow('pink_res', pink_mask)

        # Blue Colours    
        bl1_LH = LOW
        bl1_LS = LOW
        bl1_LV = cv.getTrackbarPos('Thresh 6','Tracking')
        bl1_UH = HIGH
        bl1_US = HIGH
        bl1_UV = cv.getTrackbarPos('Thresh 5','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_bl1 = np.array([bl1_LH, bl1_LS, bl1_LV])
        Upper_bl1 = np.array([bl1_UH, bl1_US, bl1_UV])

        mask = cv.inRange(hsv, Lower_bl1, Upper_bl1)
        blue_mask = cv.bitwise_and(b1,b1,mask = mask)

        #cv.imshow('blue_res', blue_mask)

        # Dark Blue Colours    
        bl2_LH = LOW
        bl2_LS = LOW
        bl2_LV = cv.getTrackbarPos('Thresh 7','Tracking')
        bl2_UH = HIGH
        bl2_US = HIGH
        bl2_UV = cv.getTrackbarPos('Thresh 6','Tracking')

        # Create threshold and mask
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        Lower_bl2 = np.array([bl2_LH, bl2_LS, bl2_LV])
        Upper_bl2 = np.array([bl2_UH, bl2_US, bl2_UV])

        mask = cv.inRange(hsv, Lower_bl2, Upper_bl2)
        dark_blue_mask = cv.bitwise_and(b2,b2,mask = mask)
        
        ############## Combine Layers
        final_mask = cv.addWeighted(white_mask,1,yellow_mask,1,0)
        final_mask = cv.addWeighted(final_mask,1,orange_mask,1,0)
        final_mask = cv.addWeighted(final_mask,1,red_mask,1,0)
        final_mask = cv.addWeighted(final_mask,1,pink_mask,1,0)
        final_mask = cv.addWeighted(final_mask,1,blue_mask,1,0)
        final_mask = cv.addWeighted(final_mask,1,dark_blue_mask,1,0)

        # Blur result image -- vs. blur original
        if blur_v == 2:
            final_mask = cv.GaussianBlur(final_mask, (blur_a,blur_a), 0)

        cv.imshow('FINAL', final_mask)

        # Keyboard Inputs
        k = cv.waitKey(1)  & 0xFF
        if k == 27:         # ESC
            break
        elif k == 111:      # o
            blur_v = 1
        elif k == 112:      # p
            blur_v = 2
        elif k == 105:      # i
            blur_v = 0
        elif k == 61:       # =
            blur_a += 2
        elif k == 45 and blur_a > 1:    # -
            blur_a -= 2
            
            
            

cap.release()
cv.destroyAllWindows()
