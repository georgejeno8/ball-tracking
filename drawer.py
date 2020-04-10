import numpy as np
import cv2

DRAW_COLOR = (221,242,255)
DRAW_COLOR_MUTED = (179,196,206)

width = 900 * 7/10
height = 500 * 7/10

def draw_table(frame):
    f_height, f_width, _ = frame.shape

    #cv2.rectangle(frame, (f_width/2 - width/2, f_height/2 - height/2), (f_width/2 + width/2, f_height/2 + height/2), DRAW_COLOR, 4)
    cv2.rectangle(frame, (int(f_width/2 - width/2), int(f_height/2 - height/2)), (int(f_width/2 + width/2), int(f_height/2 + height/2)), DRAW_COLOR, 4)

    cv2.line(frame, (int(f_width/2), int(f_height/2 - height/2)), (int(f_width/2), int(f_height/2 + height/2)), DRAW_COLOR, 4)
    cv2.line(frame, (int(f_width/2 - width/2), int(f_height/2)), (int(f_width/2 + width/2), int(f_height/2)), DRAW_COLOR, 4)

    cv2.rectangle(frame, (195, int(f_height/2 - height/2)), (215, int(f_height/2 + height/2)), DRAW_COLOR_MUTED, -1)

    return frame


def draw_ball(frame, ball_pos):
    f_height, f_width, _ = frame.shape

    scaled_bp_x = int(f_width/2 + width/2 - ball_pos[1] * width)
    scaled_bp_y = int(ball_pos[0] * (height/2) + f_height/2)

    cv2.circle(frame, (scaled_bp_x, scaled_bp_y), 20, DRAW_COLOR, -1)

    return frame


def draw_feeder(frame, f_pos, f_theta):
    f_height, f_width, _ = frame.shape

    feeder_pos = (205, int((height/2)*f_pos + f_height/2))

    cv2.circle(frame, (feeder_pos[0], feeder_pos[1]), 40, DRAW_COLOR, -1)

    rot_mat = np.array([[np.cos(f_theta), np.sin(f_theta)],[-1*np.sin(f_theta), np.cos(f_theta)]])
    disp = (rot_mat @ np.array([40,0])).astype(np.int)

    cv2.line(frame, (feeder_pos[0]+int(disp[0]/2), feeder_pos[1]+int(disp[1]/2)), (feeder_pos[0]+disp[0], feeder_pos[1]+disp[1]), DRAW_COLOR_MUTED, 24)

    return frame
