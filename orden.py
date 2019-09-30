from big_ol_pile_of_manim_imports import *

class OrdEvaluacion(Scene): 
    def construct(self): 
        #--------------------------------definicion de variables y su tamaño------------------------------------------------------
        aux = TextMobject("2")
        aux.scale(.85)
        aux.set_color(WHITE)

        result = TextMobject("9")
        result.scale(.85)

        result1 = TextMobject("3")
        result1.scale(.85)
        
        tittle = TexMobject(
            "(","\\lambda", "x",".","{ x }^{ 2 }","\\quad\\quad" ,"(","\\lambda", "x",".","x","+","1","\\quad\\quad", "2",")",")"
            #0        1      2   3   4         5          6       7       8   9  10  11   12        13       14   15  16
        )
        tittle.scale(.85)

        subt2 = TextMobject("Aplicativo")
        subt2.scale(.85)

        trans2 = TexMobject(
            "(","\\lambda", "x",".","{ x }^{ 2 }","\\quad\\quad" ,"(","\\lambda", "x",".","x","+","1","\\quad\\quad", "2",")",")"
            #0        1      2   3   4         5          6       7       8   9  10  11   12        13       14   15  16
        )
        trans2.scale(.85)
        newtrans2 = TexMobject(
            "(","\\lambda", "x",".","{ x }^{ 2 }","\\quad\\quad", "3",")"
            #0       1       2   3        4              5         6   7
        )
        newtrans2.scale(.85)
        newtrans2[6].set_color("#19FFFF")
        newtrans2_a = TexMobject(
            "{ x }^{ 2 }","\\quad\\quad","(", "3",")"
            #      0              1       2    3   4         
        )
        newtrans2_a.scale(.85)

        arrow = Arrow(LEFT,RIGHT)
        arrow.scale(.85)


        #---------------------definicion de las posiciones de las funciones -----------------------------------------------------
        tittle.to_edge(UP)
        arrow.next_to(tittle,LEFT,buff=SMALL_BUFF)
        subt2.move_to(tittle.get_center()+(DOWN*1.5)+(LEFT*4.5))
        result.move_to(tittle.get_center()+(DOWN*1.5)+(LEFT*4.5))
        trans2.next_to(subt2,DOWN,buff = .4)
        newtrans2.next_to(subt2,DOWN,buff=.4)
        
 
        #ya estan las posiciones de los titulos

        self.play(
            GrowArrow(arrow),
            Write(tittle),
        )
        self.wait(2)
        self.play(FadeOutAndShift(arrow,LEFT))
        self.wait(2)
        subt2.set_color("#19C4FF")
        self.play(
            FadeIn(subt2),
            Write(subt2)
        )
        self.wait(2)
        self.play(
			ReplacementTransform(tittle[0].copy(),trans2[0]),
			ReplacementTransform(tittle[1].copy(),trans2[1]),
            ReplacementTransform(tittle[2].copy(),trans2[2]),
            ReplacementTransform(tittle[3].copy(),trans2[3]),
            ReplacementTransform(tittle[4].copy(),trans2[4]),
            ReplacementTransform(tittle[5].copy(),trans2[5]),
            ReplacementTransform(tittle[6].copy(),trans2[6]),
            ReplacementTransform(tittle[7].copy(),trans2[7]),
            ReplacementTransform(tittle[8].copy(),trans2[8]),
            ReplacementTransform(tittle[9].copy(),trans2[9]),
            ReplacementTransform(tittle[10].copy(),trans2[10]),
            ReplacementTransform(tittle[11].copy(),trans2[11]),
            ReplacementTransform(tittle[12].copy(),trans2[12]),
            ReplacementTransform(tittle[13].copy(),trans2[13]),
            ReplacementTransform(tittle[14].copy(),trans2[14]),
            ReplacementTransform(tittle[15].copy(),trans2[15]),
            ReplacementTransform(tittle[16].copy(),trans2[16]),
		)
        self.wait(3)
        self.play(
            trans2[6:16].set_color,"#19FFFF"
        )
        brace1 = Brace(trans2[5:16], DOWN, buff = .07)
        brace1.scale(.85)
        brace1.set_color("#19FFFF")
        self.wait(3)
        t1 = brace1.get_text("$argumento$")
        t1.scale(.85)
        t1.set_color("#19FFFF")
        t1.next_to(brace1,DOWN,buff=.07)
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        brace2 = Brace(trans2[0:16], DOWN, buff = 1)
        brace2.scale(.85)
        self.wait(3)
        t2 = brace2.get_text("expresi\\'on")
        t2.scale(.85)
        t2.next_to(brace2,DOWN,buff=.07)
        self.play(
            GrowFromCenter(brace2),
            FadeIn(t2),
        )

        self.wait(2)
        self.play(
            FadeOut(brace1),FadeOut(t1),
            FadeOut(brace2),FadeOut(t2),
        )
        
        #definimos las lineas siguientes para las transformaciones de la evaluación
        self.wait(2)

        trans2_a = TexMobject(
            "(","\\lambda", "x",".","x","+","1","\\quad\\quad", "2",")"
            #0        1      2   3   4   5   6         7         8    9  
        )
        trans2_a.scale(.85)
        trans2_a.set_color("#19FFFF")
        trans2_a.next_to(trans2,DOWN,buff=.4)

        self.play(
			ReplacementTransform(trans2[6].copy(),trans2_a[0]),
			ReplacementTransform(trans2[7].copy(),trans2_a[1]),
            ReplacementTransform(trans2[8].copy(),trans2_a[2]),
            ReplacementTransform(trans2[9].copy(),trans2_a[3]),
            ReplacementTransform(trans2[10].copy(),trans2_a[4]),
            ReplacementTransform(trans2[11].copy(),trans2_a[5]),
            ReplacementTransform(trans2[12].copy(),trans2_a[6]),
            ReplacementTransform(trans2[13].copy(),trans2_a[7]),
            ReplacementTransform(trans2[14].copy(),trans2_a[8]),
            ReplacementTransform(trans2[15].copy(),trans2_a[9])
		)
        self.wait(2)
        self.play(trans2_a[8].set_color,"#E900F8")
        brace3 = Brace(trans2_a[7:9], DOWN, buff = .07)
        brace3.scale(.85)
        brace3.set_color("#E900F8")
        self.wait(3)
        t3 = brace3.get_text("$argumento$")
        t3.scale(.85)
        t3.set_color("#E900F8")
        t3.next_to(brace3,DOWN,buff=.07)
        self.play(
            GrowFromCenter(brace3),
            FadeIn(t3),
        )
        brace4 = Brace(trans2_a[0:9], DOWN, buff = 1)
        brace4.scale(.85)
        brace4.set_color("#19FFFF")
        self.wait(3)
        t4 = brace4.get_text("expresi\\'on")
        t4.scale(.85)
        t4.next_to(brace4,DOWN,buff=.07)
        t4.set_color("#19FFFF")
        self.play(
            GrowFromCenter(brace4),
            FadeIn(t4),
        )

        self.wait(2)
        self.play(
            FadeOut(brace3),FadeOut(t3),
            FadeOut(brace4),FadeOut(t4),
        )
        self.wait(2)
        self.play(
            trans2_a[4].set_color,"#E900F8",
            trans2_a[5].set_color,"#E900F8",
            trans2_a[6].set_color,"#E900F8"
        )
        self.wait(2)
        
        trans2_b = TexMobject(
            "x","+","1","\\quad\\quad","(", "2",")"
             #0  1   2          3        4   5   6  
        )
        trans2_b.scale(.85)
        trans2_b.set_color("#00FE7F") #verdesito
        trans2_b.next_to(trans2_a,DOWN,buff=.4)
        self.play(
			ReplacementTransform(trans2_a[0].copy(),trans2_b[4]),
			ReplacementTransform(trans2_a[8].copy(),trans2_b[5]),
            ReplacementTransform(trans2_a[9].copy(),trans2_b[6]),
            ReplacementTransform(trans2_a[7].copy(),trans2_b[3]),
            ReplacementTransform(trans2_a[6].copy(),trans2_b[2]),
            ReplacementTransform(trans2_a[5].copy(),trans2_b[1]),
            ReplacementTransform(trans2_a[4].copy(),trans2_b[0])
		)

        result1.set_color("#00FE7F")
        self.wait(2)
        result1.move_to(trans2_b.get_center())
        self.play(ReplacementTransform(trans2_b,result1)
        )

        self.wait(2)
        trans2_b.set_color("#E900F8")
        trans2_b.move_to(trans2_a.get_center())
        self.play(FadeOut(result1)) 
        self.play(ReplacementTransform(trans2_a,trans2_b)) 

        
        self.wait(2)
        self.play(FadeOut(trans2_b))
        self.play(ReplacementTransform(trans2,newtrans2))

        self.wait(2)
        brace5 = Brace(newtrans2[5:7], DOWN, buff = .07)
        brace5.scale(.85)
        brace5.set_color("#19FFFF")
        self.wait(2)
        t5 = brace5.get_text("$argumento$")
        t5.scale(.85)
        t5.set_color("#19FFFF")
        t5.next_to(brace5,DOWN,buff=.07)
        self.play(
            GrowFromCenter(brace5),
            FadeIn(t5),
        )
        brace6 = Brace(newtrans2[0:7], DOWN, buff = 1)
        brace6.scale(.85)
        self.wait(2)
        t6 = brace6.get_text("expresi\\'on")
        t6.scale(.85)
        t6.next_to(brace6,DOWN,buff=.07)
        self.play(
            GrowFromCenter(brace6),
            FadeIn(t6),
        )

        self.wait(2)
        self.play(
            FadeOut(brace5),FadeOut(t5),
            FadeOut(brace6),FadeOut(t6),
        )
        self.wait(2)
        self.play(newtrans2[4].set_color,"#19FFFF")
        self.wait(2)

        newtrans2_a.next_to(newtrans2,DOWN,buff=.4)
        newtrans2_a.set_color("#19FFFF")
        self.play(
            ReplacementTransform(newtrans2[0].copy(),newtrans2_a[2]),
            ReplacementTransform(newtrans2[4].copy(),newtrans2_a[0]),
            ReplacementTransform(newtrans2[6].copy(),newtrans2_a[3]),
            ReplacementTransform(newtrans2[7].copy(),newtrans2_a[4]),
            ReplacementTransform(newtrans2[5].copy(),newtrans2_a[1])
        )
        self.wait(2)
        result.move_to(newtrans2_a.get_center())
        result.set_color("#19FFFF")
        self.play(ReplacementTransform(newtrans2_a,result))

        self.wait(3)
        newtrans2_a.set_color(WHITE)
        newtrans2_a.next_to(subt2,DOWN,buff=.4)
        self.play(FadeOut(result))
        self.play(ReplacementTransform(newtrans2,newtrans2_a))
        self.wait(3)
