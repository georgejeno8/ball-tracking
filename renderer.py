import numpy as np
import cv2

from drawer import draw_table, draw_ball, draw_feeder
from tracker import Tracker
from controller import Controller

#FRAME_SIZE = (1080, 1920)

cam = cv2.VideoCapture(1)#cv2.VideoCapture('feed_vid.mp4')

table = cv2.imread("table.png")

c = Controller()
t = Tracker()

img_array = []

tr = 0

size = None

while (True) :
    tr+=1
    if (tr%10==0): print(tr)
    """
    frame = np.zeros(FRAME_SIZE).astype(np.int)

    frame = draw_table(frame)
    """
    frame = np.copy(table)

    succ, v_frame = cam.read()

    if (succ) :
        found, v_frame, ball_pos, points = t.get_ball_pos(v_frame)
        if (found):
            frame = draw_ball(frame, ball_pos)
            c.update_controller(ball_pos)

        f_pos, f_theta = c.get_feeder_pos()

        frame = draw_feeder(frame, f_pos, f_theta)

        temp = np.zeros((frame.shape[0] + v_frame.shape[0], frame.shape[1], frame.shape[2])).astype(np.uint8)
        temp[:frame.shape[0],:frame.shape[1],:] = frame
        temp[frame.shape[0]:v_frame.shape[0]+frame.shape[0],:v_frame.shape[1],:] = v_frame

        #print(temp)

        size = (temp.shape[1], temp.shape[0])

        #img_array.append(v_frame)

        #cv2.imshow("sim", frame)
        #cv2.imshow("camera feed", v_frame)
        cv2.imshow("sim2", temp)

    """
    else:
        out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        break
    """
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.closeAllWindows()
