import numpy as np
import cv2

class Tracker():
    def __init__(self):
        self.background = None

    def get_ball_pos(self, v_frame):
        scale_percent = 30 # percent of original size
        width = int(v_frame.shape[1] * scale_percent / 100)
        height = int(v_frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        v_frame = cv2.resize(v_frame, dim, interpolation = cv2.INTER_AREA)

        v_frame = v_frame[int(v_frame.shape[0]/7.):,:]
        fr = v_frame

        if (self.background is None):
            self.background = v_frame

            return False, v_frame, None, None
        else:
            new = v_frame.astype(np.int) - self.background.astype(np.int)
            new *= 2
            new[new > 255] = 255
            new[new < 0] = 0
            v_frame = new.astype(np.uint8)

            """
            grey = cv2.cvtColor(v_frame, cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(grey,20,255,0)
            """
            hsv = cv2.cvtColor(v_frame, cv2.COLOR_BGR2HSV)
            thresh = cv2.inRange(hsv, (0,100,40), (50,255,255))
            thresh[:int(thresh.shape[0]/2),:int(thresh.shape[1]/3)] = 0
            thresh[:int(thresh.shape[0]/2),2*int(thresh.shape[1]/3):] = 0
            thresh[-1*int(thresh.shape[0]/10):] = 0

            kernel = np.ones((5,5),np.uint8)
            erosion = cv2.erode(thresh,kernel,iterations = 1)
            thresh = cv2.dilate(erosion,kernel,iterations = 1)

            points = np.argwhere(thresh)

            if (points.shape[0] > 10):
                p1, p2 = points[0], points[-1]
                cv2.line(v_frame, (p1[1], p1[0]), (p2[1], p2[0]), (0,255,0), 2)
                cv2.line(fr, (p1[1], p1[0]), (p2[1], p2[0]), (0,255,0), 2)

                p = (p1+p2)/2

                y = 1.0*p[0]/v_frame.shape[0]
                x = (p[1] - (v_frame.shape[1]/2)) * (2-y) / v_frame.shape[1]
                return True, fr, (x,y), (p1, p2)

        return False, fr, None, None
