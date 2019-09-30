from big_ol_pile_of_manim_imports import *

class OrdEvaluacion(Scene): 
    def construct(self): 
        #--------------------------------definicion de variables y su tamaño------------------------------------------------------
        aux = TextMobject("2")
        aux.scale(.85)
        aux.set_color(WHITE)

        result = TexMobject("9")
        result.scale(.85)

        result2 = TexMobject("9")
        result2.scale(.85)

        result3 = TexMobject("9")
        result3.scale(.85)

        result1 = TextMobject("3")
        result1.scale(.85)
        
        tittle = TexMobject(
            "(","\\lambda", "x",".","{ x }^{ 2 }","\\quad\\quad" ,"(","\\lambda", "x",".","x","+","1","\\quad\\quad", "2",")",")"
            #0        1      2   3        4               5        6       7       8   9  10   11 12        13         14  15  16
        )
        tittle.scale(.85)

        subt1 = TextMobject("Normal")
        subt1.scale(.85)
        subt2 = TextMobject("Aplicativo")
        subt2.scale(.85)

        trans1 = TexMobject(
            "(","\\lambda", "x",".","{ x }^{ 2 }","\\quad\\quad" ,"(","\\lambda", "x",".","x","+","1","\\quad\\quad", "2",")",")"
            #0        1      2   3        4               5        6       7       8   9  10   11 12        13         14  15  16
        )
        trans1.scale(.85)



        #---------------------definicion de las posiciones de las funciones -----------------------------------------------------
        tittle.to_edge(UP)
        subt1.move_to(tittle.get_center()+(DOWN*1.5)+(RIGHT*4.5))
        subt2.move_to(tittle.get_center()+(DOWN*1.5)+(LEFT*4.5))
        result.move_to(tittle.get_center()+(DOWN*1.5)+(LEFT*4.5))
        trans1.next_to(subt1,DOWN,buff = .4)
        result.next_to(subt2,DOWN,buff=.4)
        result3.next_to(subt1,DOWN,buff=.4)
        
 
        #ya estan las posiciones de los titulos

        self.play(
            Write(tittle)
        )
        self.play(
            FadeIn(subt2),
            subt2.set_color,"#19C4FF" #AZUL
        )
        self.play(Write(result))

        self.wait(2)
        subt1.set_color("#2EFF00") #VERDE
        self.play(
            FadeIn(subt1),
            Write(subt1)
        )
        self.wait(2)
        self.play(
			ReplacementTransform(tittle[0].copy(),trans1[0]),
			ReplacementTransform(tittle[1].copy(),trans1[1]),
            ReplacementTransform(tittle[2].copy(),trans1[2]),
            ReplacementTransform(tittle[3].copy(),trans1[3]),
            ReplacementTransform(tittle[4].copy(),trans1[4]),
            ReplacementTransform(tittle[5].copy(),trans1[5]),
            ReplacementTransform(tittle[6].copy(),trans1[6]),
            ReplacementTransform(tittle[7].copy(),trans1[7]),
            ReplacementTransform(tittle[8].copy(),trans1[8]),
            ReplacementTransform(tittle[9].copy(),trans1[9]),
            ReplacementTransform(tittle[10].copy(),trans1[10]),
            ReplacementTransform(tittle[11].copy(),trans1[11]),
            ReplacementTransform(tittle[12].copy(),trans1[12]),
            ReplacementTransform(tittle[13].copy(),trans1[13]),
            ReplacementTransform(tittle[14].copy(),trans1[14]),
            ReplacementTransform(tittle[15].copy(),trans1[15]),
            ReplacementTransform(tittle[16].copy(),trans1[16]),
		)
        self.wait(2)
        brace1 = Brace(trans1[5:16], DOWN, buff = .07)
        brace1.scale(.85)
        brace1.set_color("#FF0000") #ROJO
        t1 = brace1.get_text("$M$")
        t1.scale(.85)
        t1.set_color("#FF0000")
        t1.next_to(brace1,DOWN,buff=.07)
        self.play(
            trans1[6:16].set_color,"#FF0000", 
            GrowFromCenter(brace1),
            FadeIn(t1)
        )

        self.wait(2)
        brace2 = Brace(trans1[1:5], DOWN, buff = .07)
        brace2.scale(.85)
        brace2.set_color("#FFFF00") #AMARILLO
        t2 = brace2.get_text("$E$")
        t2.scale(.85)
        t2.set_color("#FFFF00")
        t2.next_to(brace2,DOWN,buff=.07)
        self.play(
            trans1[4].set_color,"#FFFF00", #AMARILLO
            GrowFromCenter(brace2),
            FadeIn(t2[0])
        )

        self.wait(2)
        t12 = TextMobject("$E(M)$")
        t12.scale(.85)
        t12.set_color("#FF7000") #NARANJA
        t12.next_to(brace2,DOWN,buff=.07)
        self.play(
            FadeOut(t1),
            FadeOut(brace1),
            brace2.set_color,"#FF700",
            ReplacementTransform(t2,t12)
        )

        self.wait(2)
        trans1_a = TexMobject(
            r"{ (\lambda x.x+1\quad \quad 2) }^{ 2 }"
            #   0    1   23456            78     9
        )
        trans1_a.scale(.85)
        trans1_a.set_color("#FF700")
        trans1_a.next_to(trans1,DOWN,buff=.4)

        self.play(
            FadeOut(brace2),
			ReplacementTransform(t12,trans1_a)
		)

        self.wait(2)
        self.play(
            trans1_a[7].set_color,"#C9FF00" #VERDE MENTA
        )

        self.wait(2)
        self.play(
            trans1_a[4:7].set_color,"C9FF00"
        )
        self.wait(2)
        trans1_b = TexMobject(
            "x","+","1","\\quad\\quad","(", "2",")"
             #0  1   2          3        4   5   6  
        )
        trans1_b.scale(.85)
        trans1_b.set_color("#C9FF00") 
        trans1_b.next_to(trans1_a,DOWN,buff=.4)
        self.play(
			ReplacementTransform(trans1_a[0].copy(),trans1_b[4]),
            ReplacementTransform(trans1_a[4:7].copy(),trans1_b[0:3]),
            ReplacementTransform(trans1_a[7].copy(),trans1_b[5]),
            ReplacementTransform(trans1_a[8].copy(),trans1_b[6])
		)

        self.wait(2)
        result1.set_color("#C9FF00")
        result1.move_to(trans1_b.get_center())
        self.play(ReplacementTransform(trans1_b,result1))
        self.wait(2)

        auxx = TexMobject(r"{ (3) }^{ 2 }")
        auxx.scale(.85)
        auxx.set_color("#FF7000") #NARANJA
        auxx[1].set_color("#C9FF00")
        auxx.next_to(trans1,DOWN,buff=.4)
        
        self.play(
            FadeOut(result1),
            ReplacementTransform(trans1_a,auxx)
        )
        
        self.wait(2)
        result2.set_color("#FF7000")
        result2.next_to(trans1,DOWN,buff=.45)

        self.play(
            Transform(auxx,result2)
        )

        self.wait(2)
        result.set_color(WHITE)
        result2.move_to(trans1.get_center())
        result2.set_color(WHITE)

        self.play(
            FadeOut(auxx),
            Transform(trans1,result3)
        )
        self.wait(3)