import numpy as np
from manim import *

class Updater(Scene):
    def construct(self):
        ax = Axes(x_range=[-5, 5], y_range=[-3, 3])
        graph1 = ax.plot(lambda x: 0.5*x, color=BLUE, x_range=[-5, 2])
        graph2 = ax.plot(lambda x: -1*x+2, color=BLUE, x_range=[2, 5])

        self.play(Create(ax))
        self.play(Create(graph1))
        self.play(Create(graph2))

        dot = Dot(ax.c2p(0,0))
        self.play(Create(dot))

        t = ValueTracker(0)

        def func(x):
            if int(x) < 2:
                return 0.5*x
            else:
                return -1*x+2

        def update_function(mobj):
            mobj.move_to(ax.c2p(t.get_value(), func(t.get_value())))

        dot.add_updater(update_function)

        xs = [1.5, 2.4, 1.8, 2.1, 1.95, 2.01, 1.99]
        for x in xs:
            self.play(t.animate.set_value(x), run_time=1)