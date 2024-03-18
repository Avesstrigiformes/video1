from manim import *
class Proof(Scene):      
    def construct(self):  
        t1 = MathTex(r"x^{3}+y^{3}=p(xy+p)", color= BLUE).scale(2)
        rect = SurroundingRectangle(t1, fill_color=WHITE, fill_opacity=0.15, buff=1, color=ORANGE)
        self.add(t1)
        self.add(rect)