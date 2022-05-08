from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.window import Window
from kivy.clock import Clock
import random

'''
    Maps the number x from the range [x1, x2] to a corresponding number in the range [y1, y2]
'''
def map(x, x1, x2, y1, y2):
    return y1 + x * (y2 - y1) / (x2 - x1)

def thunderon(time):
    Window.clearcolor = (1,1,1)
    pass

def thunderoff(time):
    Window.clearcolor = (0.2,0.2,0.2)
    pass

'''
    Class that displays everything
'''
class PurpleRain(BoxLayout):

    def __init__(self):
        super(PurpleRain, self).__init__()
        Window.size = (640, 360)
        Window.clearcolor = (0.20, 0.20, 0.20)

        # create the drops
        self.drops = [Drop(*Window.size) for i in range(100)]

        # start the clock
        self.thunder_counter = 0
        Clock.schedule_interval(self.update_drops, 0.05)
        Clock.schedule_interval(thunderon, 10)
        Clock.schedule_interval(thunderoff, 0.2)

    '''
        Updates the drops locations and displays them
    '''
    def update_drops(self, time):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.9, 0.9, 0.9)
            for drop in self.drops:
                drop.fall()
                drop.show()

'''
    This class represents a single drop, and provides behaviours such 
    as falling
'''
class Drop:
    def __init__(self, width, height):
        # get the window's dimensions
        self.window_width = width
        self.window_height = height

        # pick a random location for the drop
        self.x = random.randint(0, width)
        self.y = random.randint(height, height + 500)  # the drop will start out of the screen
        self.z = random.randint(0, 10)  # represents the depth (in an attempt to make the simulation 3D)

        # The closer to the screen, the higher the gravity, the faster the drop is, the
        #   longer and thicker it is as well
        self.gravity = map(self.z, 0, 20, 0, 0.5)
        self.yspeed = map(self.z, 0, 20, 7, 10)
        self.length = map(self.z, 0, 20, 10, 20)
        self.thickness = map(self.z, 0, 20, 1, 1.5)

    '''
        Moves the drop down, and relocates it if the drop hits the bottom
    '''
    def fall(self):
        # Move the drop down faster with gravity
        self.y -= self.yspeed

        if self.yspeed < map(self.z, 0, 20, 7, 10) * 3:
            self.yspeed += self.gravity

        # If the drop hits the bottom, create the splash, pop it, then relocate the drop
        if self.y - self.length < 0:
            # relocating
            self.y = random.randint(self.window_height, self.window_height + 100)
            self.z = random.randint(0, 20)

            # creating and poping splash
            splash = Splash(self.x, 0, self.length)
            for splashline in splash.get_splashlines():
                Line(points = splashline, width = self.thickness)
            # self.yspeed = map(self.z, 0, 20, 4, 10)

    '''
        Displays the drop
    '''
    def show(self):
        return Line(points = (self.x, self.y, self.x, self.y - self.length), width = self.thickness)

'''
    Splash representation (two lines in symmetric and diagonal directions)
'''
class Splash:
    def __init__(self, x, y, drop_length):
        # location of the drop
        self.x = x
        self.y = y

        # keeps track of whether or not the splash ocuured already, in which case don't splash again
        self.splashed = False

        # the splash lines length are proportional to the drop length, but smaller
        self.length = drop_length / 15

        # make the splash lines inclined and symmetric
        self.splashlines = [
            (x + 5, y + 10, x + 5 + self.length,  y + 10 + self.length),
            (x - 5, y + 10, x - 5 - self.length, y + 10 + self.length),
        ]

    '''
        returns the splash lines
    '''
    def get_splashlines(self):
        if not self.splashed:
            return self.splashlines
        else:
            return []

class PurpleRainApp(App):
    def build(self):
        return PurpleRain()

PurpleRainApp().run()