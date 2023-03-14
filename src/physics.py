import pygame

def lerp(start, end, percent):
    return start * (1 - percent) + end * percent

def pointlerp(start, end, percent):
    return (lerp(start[0], end[0], percent), lerp(start[1], end[1], percent))



class Raycast():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.dt = 0.1
        self.percent = 0
        self.hit = None
        self.point = start


    def cast(self, collisionGroup):
        while pointlerp(self.start, self.end, self.percent) != self.end:
            for other in collisionGroup:
                if other.rect.collidepoint(pointlerp(self.start, self.end, self.percent)):
                    self.hit = other
                    self.point = pointlerp(self.start, self.end, self.percent)
                    return True

            self.percent += self.dt
