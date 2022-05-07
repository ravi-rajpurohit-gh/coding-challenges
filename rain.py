from turtle import width
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line
from kivy.core.window import Window
from kivy.clock import Clock
import random

class Rain(BoxLayout):
    def __init__(self) -> None:
        super(Rain, self).__init__()
        width, height = (640,360)
        Window.size = (width, height)
        Window.clearcolor = (0.91, 0.91, 0.98, 1)

        self.drops = [Drop(width, height) for i in range(200)]

        Clock.schedule_interval(self.update_drop, 0.05)


    def update_drop(self, time) -> None:
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.54, 0.17, 0.89)
            for drop in self.drops:
                drop.fall()
                drop.show()
        

class Drop():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.x = random.randint(0, width)
        self.y = random.randint(height, height+200)

        self.length = 10
        self.thickness = 1.5
        # self.length = map(0, 20, 10, 20)
        # self.thichkness = map(0, 20, 1, 1.5)

        self.yspeed = random.randint(20,30)

    def fall(self) -> None:
        self.y -= self.yspeed

        if self.y - self.length < 0:
            self.y = random.randint(self.height, self.height+200)


    def show(self) -> None:
        return Line(points = (self.x, self.y, self.x, self.y-self.length), width = self.thickness)


class RainApp(App):
    def build(self) -> None:
        return Rain()

RainApp().run()