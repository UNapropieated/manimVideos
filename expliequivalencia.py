from big_ol_pile_of_manim_imports import *

class OrdEvaluacion(Scene): 
    def construct(self): 
        tittle = TexMobject(r"(\lambda x.{ x }^{ 2 }\quad \quad (\lambda x.x+1\quad \quad 2))")
        tittle.scale(.85)

        nueve1 = TextMobject("9")
        nueve2 = TextMobject("9")
        nueve3 = TextMobject("9")
        nueve1.scale(.85)
        nueve2.scale(.85)
        nueve3.scale(.85)

        subt1 = TextMobject("Normal")
        subt1.scale(.85)
        subt2 = TextMobject("Aplicativo")
        subt2.scale(.85)

        tittle.to_edge(UP)
        subt1.move_to(tittle.get_center()+(DOWN*1.5)+(RIGHT*4.5))
        subt2.move_to(tittle.get_center()+(DOWN*1.5)+(LEFT*4.5))
        subt1.set_color("#2EFF00") #VERDE
        subt2.set_color("#19C4FF") #AZUL
        nueve1.next_to(subt1,DOWN,buff=.4)
        nueve2.next_to(subt2,DOWN,buff=.4)


        self.play(Write(tittle),Write(subt1),Write(subt2),Write(nueve1),Write(nueve2))

        #-----------------------------plantilla---------------------------------

        self.wait(2)
        arrow = DoubleArrow(subt2.get_right(),subt1.get_left(),buff=.1)
        arrow.set_color_by_gradient(DARK_BLUE,TEAL_E)
        nueve3.next_to(arrow,DOWN,buff=.4)

        self.play(
            GrowArrow(arrow),
            tittle.set_color_by_gradient,"#19C4FF","#2EFF00",
            tittle.shift,DOWN*3,
            FadeOut(nueve1),
            FadeOut(nueve2),
            run_time = 2
        )

        self.wait(2)
        self.play(
            FadeOut(tittle),
            FadeOut(subt1),
            FadeOut(subt2),
            FadeOut(arrow)
        )
        self.wait(2)