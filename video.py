from manim import *
class Video(Scene):
    def construct(self):

        #expressions

        colors = [WHITE, BLUE, GREEN, YELLOW, ORANGE, RED, PURPLE]
        placeholder = Dot([-6,3,0])
        PROBLEM = Tex(r"Problem. Determine all prime numbers p and all positive\\ integers x and y satisfying:$$x^{3}+y^{3}=p(xy+p)$$", tex_environment="{minipage}{30em}")
        t = Tex(r"Solution:").shift(DOWN)
        PROBLEM.next_to(placeholder, DOWN, aligned_edge=LEFT)
        rect = SurroundingRectangle(PROBLEM, fill_color=WHITE, fill_opacity=0.2, buff=0.1, color=ORANGE)
        rect.set_z_index(-1)

        expressions1 = VGroup(MathTex(r"x^3+y^3=p(xy+p)"), MathTex(r"p|(x^3+y^3)=(x+y)(x^2-xy+y^2)"), MathTex(r"\therefore p|(x+y) \vee p|(x^2-xy+y^2)"))
        t1 = MathTex(r"x^2-xy+y^2", r"=", r"\frac{xy+p}{a}",color=BLUE)
        t1_1 = MathTex(r"a(x^2-xy+y^2)-xy", r"=", r"p",color=BLUE).shift(UP)
        t1_2 = MathTex(r"a=1 \implies (x-y)^{2}=p \Rightarrow \Leftarrow ",color=BLUE)
        t2 = MathTex(r"a\geq 2 \implies x+y=", r"a[a(x^2-xy+y^2)-xy]",color=BLUE)
        t2_1 = MathTex(r"a\geq 2 \implies x+y=", r"a^2(x^2-xy+y^2)-axy",color=BLUE)
        t3 = MathTex(r"a\geq 2 \implies x+y\geq", r"4(x^2-xy+y^2)-2xy\geq 2xy",color=BLUE)
        t4 = Tex(r"Hence by AM-GM $x=y$, we get $x=y=1, a=2, p=1$ \\ which is not true.",color=BLUE).shift(DOWN)
        case1 = Tex(r"Case 1: $p|(x+y)$, then $x+y=ap$.",color=RED).shift(3*UP)
        case2 = Tex(r"Case 2: $p|(x^2-xy+y^2)$ and $p\nmid (x+y)$,\\ then $x^2-xy+y^2=ap \implies x+y=\frac{xy+p}{a}$.",color=RED).shift(3*UP)
        
        t5 = MathTex(r"ap=x^2-xy+y^2=(x+y)^2-3xy=(x+y)^2-3[a(x+y)-p]",color=BLUE)
        t5_1 = MathTex(r"ap=(x+y)^2-3[a(x+y)-p]",color=BLUE)
        t5_2 = MathTex(r"ap=(x+y)^2-3a(x+y)",color=BLUE)
        t5_2_1 = MathTex(r"+3p",color=BLUE).next_to(t5_2, RIGHT)
        t5_2_2 = MathTex(r"-3p",color=BLUE).next_to(t5_2, LEFT)
        t5_3 = MathTex(r"p(a-3)=(x+y)(x+y-3a)",color=BLUE)

        t6 = Tex(r"If $a>3$, then we have $p|(x+y-3a)$")
        t7 = Tex(r"$x+y-3a\geq p\Rightarrow x+y\geq p+3a>a-3$,\\ which is a clear contradiction").next_to(t6, DOWN)
        t8 = Tex(r"So we must have $a\leq 3$")

        cw3 = MathTex(r"a=3", color = PURPLE)
        cw3_1 = Tex(r"We get $x+y=9$, a quick casework shows that:")          
        eq = MathTex(r"x = ", "1, ", "2, ", "3, ", "4, ", "5, ", "6, ", "7, ", "8.").shift(DOWN)
        sol1 = MathTex(r"x = 1, y =  8, p =  19", color = GREEN).shift(DOWN*2)
        sol2 = MathTex(r"x = 2, y = 7, p = 13", color = GREEN).shift(DOWN*2)
        sol3 = MathTex(r"x = 4, y = 5, p = 7", color = GREEN).shift(DOWN*2)
        nosol = Tex(r"No solution", color = RED).shift(DOWN*2)
        cw3_2 = MathTex(r"\boxed{(x, y, p)=(1, 8, 19), (8, 1, 19), (2, 7, 13), (7, 2, 13), (4, 5, 7), (5, 4, 7)}").next_to(cw3_1, DOWN).scale(0.8)

        cw2 = MathTex(r"a=2", color = PURPLE)
        cw2_1 = Tex(r"Note that: $p=(x+y)(6-x-y)$ and $x+y=\frac{xy+p}{2}$\\$p$ must be 5, but $2(x+y)=xy+5$ is a contradiction.").shift(DOWN)
        cw2_2 = MathTex(r"\boxed{\text{no solution}}")

        cw1 = MathTex(r"a=1", color = PURPLE)
        cw1_1 = MathTex(r"x+y=xy+p>xy+1\geq x+y\Rightarrow \Leftarrow").shift(DOWN * 2)
        cw1_2 = MathTex(r"\boxed{\text{no solution}}")

        ans = Tex(r"Answer:").shift(UP)    
        tfw = Tex(r"Thanks For Watching").scale(2)
        #intro
        
        self.play(Create(rect), Write(PROBLEM), run_time=5)
        self.wait(5)
        self.play(Write(t))
        self.play(Flash(t, line_length=0.5, num_lines=50, color=ORANGE, flash_radius=1.1, time_width=0.5, run_time=2, rate_func = rush_from))
        self.play(FadeOut(PROBLEM), FadeOut(t), FadeOut(rect))

        #part 1 

        already_shown = VGroup()
        for line in expressions1:
            self.play(already_shown.animate.shift(UP))
            self.play(Write(line))
            already_shown += line
            self.wait(2)
        self.play(FadeOut(expressions1))
        self.play(DrawBorderThenFill(case1))
        self.play(Write(t1))
        self.play(t1.animate.shift(UP))
        self.play(Write(t1_2))
        self.wait(2)
        self.play(Unwrite(t1_2))
        self.play(TransformMatchingTex(t1, t1_1))
        self.play(Write(t2))
        self.wait(2)
        self.play(TransformMatchingTex(t2, t2_1))
        self.play(TransformMatchingTex(t2_1, t3))
        self.play(Write(t4))
        self.wait(3)
        self.play(FadeOut(case1), FadeOut(t1_1), FadeOut(t3), FadeOut(t4))

        #part 2 

        self.play(DrawBorderThenFill(case2))
        self.wait(3)
        self.play(Write(t5))
        self.wait(5)
        self.play(Transform(t5, t5_1))
        self.wait(1)
        self.play(Transform(t5, t5_2), TransformFromCopy(t5, t5_2_1))
        self.play(Transform(t5_2_1, t5_2_2))
        self.play(FadeOut(t5_2_1), Transform(t5, t5_3))
        self.wait(2)
        self.play(FadeOut(case2), t5.animate.shift(UP*3))
        self.play(FadeToColor(t5, RED))
        self.play(Write(t6))
        self.play(Write(t7))
        self.wait(3)
        
        #casework

        self.play(Transform(t6, t8), FadeOut(t7))
        self.play(t5.animate.shift(RIGHT*3))
        self.play(FadeToColor(t6, RED))
        self.play(t6.animate.shift(UP*3, LEFT*4))
        #cw3
        self.play(DrawBorderThenFill(cw3))
        self.play(cw3.animate.shift(UP*2, LEFT*5))
        self.play(Write(cw3_1))
        #cw3.1
        self.play(Write(eq))
        self.play(Indicate(eq[1]))
        self.play(Write(sol1))
        self.play(FadeOut(sol1))
        self.play(Indicate(eq[2]))
        self.play(Write(sol2))
        self.play(FadeOut(sol2))
        self.play(Indicate(eq[3]))
        self.play(Write(nosol))
        self.play(FadeOut(nosol))
        self.play(Indicate(eq[4]))
        self.play(Write(sol3))
        self.play(FadeOut(sol3))
        for i in range(5,9):
            self.play(Indicate(eq[i]))
            self.play(Write(nosol))
            self.play(FadeOut(nosol))
        self.play(Unwrite(eq))
        self.play(Write(cw3_2), runtime = 2)
        self.play(FadeOut(cw3_1),  cw3_2.animate.shift(UP*2, LEFT * 0.66))
        #cw2
        self.play(DrawBorderThenFill(cw2))
        self.play(cw2.animate.shift(UP*0.2, LEFT*5))
        self.play(Write(cw2_1), runtime = 4)
        self.wait(3)
        self.play(Transform(cw2_1, cw2_2))
        self.play(cw2_1.animate.next_to(cw2, DOWN))
        #cw1
        self.play(DrawBorderThenFill(cw1))
        self.play(cw1.animate.next_to(cw2_1, DOWN))
        self.play(Write(cw1_1), runtime = 4)
        self.wait(2)
        self.play(Transform(cw1_1, cw1_2))
        self.play(cw1_1.animate.next_to(cw1, DOWN))
        #outro
        self.play(Unwrite(cw3), Unwrite(cw2), Unwrite(cw1))
        self.play(Unwrite(cw2_1), Unwrite(cw1_1), Unwrite(t5), Unwrite(t6))
        self.play(cw3_2.animate.move_to(0))
        self.play(Write(ans))
        texts = [cw3_2.copy().set_color(color).set_z_index(i) for i, color in enumerate(colors)]
        self.play(AnimationGroup(*map(Write, texts),lag_ratio=0.3),run_time=3)
        self.play(AnimationGroup(*map(Unwrite, texts[::-1]), lag_ratio=0.3), run_time=3)
        self.play(Transform(cw3_2, tfw), FadeOut(ans))
        self.wait(3)



