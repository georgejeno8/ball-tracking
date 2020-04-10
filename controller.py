import numpy as np
import cv2

class Controller:

    def __init__(self):
        self.f_x = 0
        self.f_v = 0
        self.f_a = 0

        self.f_tx = 0
        self.f_tv = 0
        self.f_ta = 0

    def update_controller(self,ball_pos):
        self.f_x = (ball_pos[0])
        self.f_tx = np.arctan2((2.5*self.f_x), (9.0))

        return

    def get_feeder_pos(self):
        return self.f_x, self.f_tx
