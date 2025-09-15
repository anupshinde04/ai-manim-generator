from manim import *

class ConceptAnimation(Scene):
    def construct(self):
        title = Text("Stack - Data Structure")
        self.play(Write(title))
        self.wait(1)

        definition = Text("Stack follows LIFO: Last In First Out")
        self.play(Transform(title, definition))
        self.wait(2)
