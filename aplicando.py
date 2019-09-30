from big_ol_pile_of_manim_imports import *

class Aplicacion(Scene): 
    def construct(self): 
        func = TexMobject(r"f(x)=x+x")
        func2 = TextMobject(r"f(4/2)")
        subt1 = TextMobject("Normal")
        subt2 = TextMobject("Aplicativo")

        func.to_corner(UL)
        func2.to_edge(UP)
        arrow = Arrow(func.get_right(),func2.get_left(),buff=.1)
        subt1.move_to(func2.get_center()+DOWN)
        subt2.move_to(func2.get_center()+DOWN*4)
        subt1.set_color("#2EFF00") #VERDE
        subt2.set_color("#19C4FF") #AZUL

        self.play(Write(func))

        self.wait(2)
        self.play(GrowArrow(arrow))
        self.play(Write(func2))

        self.wait(2)
        self.play(Write(subt1))
        self.wait(2)
        clone1 = TexMobject(r"f(4/2)=4/2+4/2=2+2=4")
        clone1.next_to(subt1,DOWN,buff=.5)
        self.play(ReplacementTransform(func2[0:6].copy(),clone1[0:6]))
        self.wait(2)
        self.play(Write(clone1[6]))
        self.wait(2)
        self.play(Write(clone1[7:14]))
        self.wait(2)
        self.play(Write(clone1[14]))
        self.wait(2)
        self.play(Write(clone1[15:18]))
        self.wait(2)
        self.play(Write(clone1[18]))
        self.wait(2)
        self.play(Write(clone1[19]))

        self.wait(2)
        self.play(Write(subt2))
        self.wait(2)
        clone2 = TexMobject(r"f(4/2)=f(2)=2+2=4")
        clone2.next_to(subt2,DOWN,buff=.5)
        self.play(ReplacementTransform(func2[0:6].copy(),clone2[0:6]))
        self.wait(2)
        self.play(Write(clone2[6]))
        self.wait(2)
        self.play(Write(clone2[7:11]))
        self.wait(2)
        self.play(Write(clone2[11]))
        self.wait(2)
        self.play(Write(clone2[12:15]))
        self.wait(2)
        self.play(Write(clone2[15]))
        self.wait(2)
        self.play(Write(clone2[16]))
        self.wait(2)
        