from big_ol_pile_of_manim_imports import *

class Intro(Scene): 
    def construct(self): 
        tittle = TexMobject(
            r"C\acute{a}lculo\mkern3mu\lambda",
        )
        introtitle = TextMobject("Introducci\\'on")
        subt1 = TextMobject("Creaci\\'on del c\\'alculo lambda")
        subt2 = TextMobject("Qu\\'e es el c\\'alculo lambda")
        subt3 = TextMobject("Por qu\\'e el uso del c\\'alculo lambda")

        introtitle.scale(2)
        tittle.scale(3)

        introtitle.to_corner(UL)
        underline = Line(LEFT,RIGHT)
        underline.match_width(introtitle)
        underline.scale(1.1)
        underline.next_to(introtitle, DOWN, SMALL_BUFF)
        introtitle.add(underline)

        subt1.next_to(introtitle,DOWN,buff=1)
        subt1.to_edge(LEFT)
        subt2.next_to(subt1,DOWN,buff=1)
        subt2.to_edge(LEFT)
        subt3.next_to(subt2,DOWN,buff=1)
        subt3.to_edge(LEFT)
            
        self.play(Write(tittle),run_time = 2)
        self.wait()

        self.play(Transform(tittle,introtitle),run_time = 1.5)
        self.wait(2)

        self.play(ReplacementTransform(introtitle.copy(),subt1),run_time = 1.5)
        self.wait(2)
        self.play(ReplacementTransform(subt1.copy(),subt2),run_time = 1.5)
        self.wait(2)
        self.play(ReplacementTransform(subt2.copy(),subt3),run_time = 1.5)
        self.wait(2)

        self.play(FadeOut(tittle),FadeOut(subt2),FadeOut(subt3))
        self.play(
                subt1.shift, (UP*1.8),
                run_time=2,
            )
        self.wait(2)

        subt2.to_edge(UP)
        self.play(ReplacementTransform(subt1,subt2),run_time = 1.5)
        self.wait(2)

        subt3.to_edge(UP)
        self.play(ReplacementTransform(subt2,subt3),run_time = 1.5)
        self.wait(2)

        
        