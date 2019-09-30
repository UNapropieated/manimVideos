from big_ol_pile_of_manim_imports import *

class titulo3(Scene):
    def construct(self):
        titulo = TextMobject("Curryng")
        titulo.scale(3)
        self.play(Write(titulo))
        self.wait(2)
        self.play(
            titulo.scale,1/2,
            titulo.to_edge,UP,
            titulo.set_color,"#009EFF",
        )
        self.wait(2)
        textfunc1 = TextMobject("$f(t)$")
        textfunc1.scale(1.2)
        textfunc1.move_to(titulo.get_center()+(DOWN*2)+(LEFT*4.5))
        self.play(Write(textfunc1))
        line = Line(titulo.get_bottom(),textfunc1.get_top(),buff=0.1)
        self.play(GrowArrow(line))

        self.wait(2)
        textfunc2 = TextMobject("$f(t)$")
        textfunc2.scale(1.2)
        textfunc2.move_to(titulo.get_center()+(DOWN*2)+(RIGHT*4.5))
        textfunc2.set_color("#009EFF")
        line2 = Line(titulo.get_bottom(),textfunc2.get_top(),buff=0.1)
        line2.set_color("#009EFF")
        self.play(
            ReplacementTransform(line,line2),
            ReplacementTransform(textfunc1,textfunc2)
        )

        self.wait(2)
        self.play(FadeOut(line2),FadeOut(textfunc2),run_time = 2)

        self.wait(2)
        textej1 = TexMobject(r"(Z\times Z)\rightarrow Z")
        textej1.move_to(titulo.get_center()+(DOWN*3)+(LEFT*4.5))
        self.play(Write(textej1))

        self.wait(2)
        line3 = Line(titulo.get_bottom(),textej1.get_top(),buff=0.1)
        self.play(GrowArrow(line3))

        self.wait(2)
        textej2 = TexMobject(r"Z\rightarrow (Z\rightarrow Z)")
        textej2.move_to(titulo.get_center()+(DOWN*3)+(RIGHT*4.5))
        textej2.set_color("#009EFF")
        line4 = Line(titulo.get_bottom(),textej2.get_top(),buff=0.1)
        line4.set_color("#009EFF")
        self.play(
            ReplacementTransform(line3,line4),
            ReplacementTransform(textej1.copy(),textej2)
        )
        self.wait(2)
        self.play(FadeOut(line4))
        self.wait(2)
        self.play(
            FadeOut(titulo),
            FadeOut(textej1),
            FadeOut(textej2)
        )
        self.wait(2)

