from big_ol_pile_of_manim_imports import *

class diferencia(Scene): 
    def construct(self): 
        tit = TextMobject("asd")
        tit.scale(.85)
        symbol = TextMobject("?")
        symbol.scale(.85)

        subt1 = TextMobject("Normal")
        subt1.scale(.85)
        subt2 = TextMobject("Aplicativo")
        subt2.scale(.85)

        tit.to_edge(UP)
        subt1.move_to(tit.get_center()+(DOWN*1.5)+(RIGHT*4.5))
        subt2.move_to(tit.get_center()+(DOWN*1.5)+(LEFT*4.5))
        subt1.set_color("#2EFF00") #VERDE
        subt2.set_color("#19C4FF") #AZUL
        arrow = DoubleArrow(subt2.get_right(),subt1.get_left(),buff=.1)
        symbol.move_to(arrow.get_center())

        self.wait(2)
        self.play(Write(subt1),Write(subt2),Write(symbol))
        looper = TexMobject(r"(\lambda x.(x\quad  x)\quad  \lambda x.(x\quad x))")
        looper.scale(.9)
        looper.next_to(symbol,DOWN,buff=1.5)

        self.wait(2)
        self.play(
            Transform(symbol,looper)
        )

        self.wait(2)
        text1 = TextMobject("$loop!$")
        text2 = TextMobject("$y$")
        text1.scale(.9)
        text2.scale(.9)
        text1.next_to(subt2,DOWN,buff=1.5)
        text2.next_to(subt1,DOWN,buff=1.5)
        text1.set_color("#19C4FF")
        text2.set_color("#2EFF00")
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(3)