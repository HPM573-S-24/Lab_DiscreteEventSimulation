from deampy.random_variats import Exponential

import DESInputData as D


class Parameters:
    # class to contain the parameters of the urgent care model
    def __init__(self):
        self.hoursOpen = D.HOURS_OPEN
        self.nExamRooms = D.N_EXAM_ROOMS
        self.arrivalTimeDist = Exponential(scale=D.MEAN_ARRIVAL_TIME)
        self.examTimeDist = Exponential(scale=D.MEAN_EXAM_DURATION)
