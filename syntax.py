from big_ol_pile_of_manim_imports import *

##Todos los elementos del video salen en orden cronológico
class Syntax (Scene):
	CONFIG ={
	"camera_config" : {"background_color":"#070707"}
	}
	def construct(self):
		#PARTE 1: Titulo
		#1.1 Elementos de texto
		title = TextMobject(r"{\huge{SINT\'AXIS, SEM\'ANTICA}")
		subtitle = TextMobject(r"\small{y el c\'alculo per s\'e}")
		t1 = TextMobject(r"\textsc{¿C\'omo se expresa una funci\'on en el c\'alculo lambda?}")
		underline = Line(LEFT,RIGHT)

		#1.2 Posicionamiento
		subtitle.next_to(title,DOWN)
		t1.to_edge(UP)
		underline.match_width(t1)
		underline.scale(0.5)
		underline.next_to(t1, DOWN, SMALL_BUFF)
		t1.add(underline)

		#1.3 Animación
		self.play(Write(title))
		self.play(Write(subtitle))
		self.wait()
		self.play(FadeOut(subtitle))
		self.play(Transform(title,t1))
		self.wait(3)

		#PARTE 2: Breve abordaje a la función
		#2.1 Elementos de la explicación
		t2 = TextMobject(r"\textsc{\large{Relaci\'on}}")
		t3 = TextMobject(r"Dominio")
		t4 = TextMobject(r"Rango")
		t5 = TextMobject(r"$\rightarrow$")
		t6 = TextMobject(r"Notaci\'on Matem\'atica")
		t7 = TextMobject(r"$f:$")
		t8 = TextMobject(r"$\mathbb{Z}$")
		t9 = TextMobject(r"$\mathbb{Z}$")
		t10 = TextMobject(r"\large{$f(x) = x^{2}$}")
		t11 = TextMobject(r"$x$")
		t12 = TextMobject(r"$x^{2}$")

		#Definición de posición y colores
		t2.next_to(t1,DOWN,buff=1.5)
		t6.next_to(t1,DOWN,buff=1.5)
		t3.set_color(BLUE)
		t4.set_color(GREEN)
		t5.next_to(t2,DOWN,buff=0.5)
		t3.next_to(t5,LEFT,buff=0.5)
		t4.next_to(t5,RIGHT,buff=0.5)
		t7.next_to(t3,LEFT)
		t8.set_color(BLUE)
		t9.set_color(GREEN)
		t8.next_to(t5,LEFT,buff=0.5)
		t9.next_to(t5,RIGHT,buff=0.5)
		t10.next_to(t2,DOWN,buff=0.5)
		t11.set_color(BLUE)
		t12.set_color(GREEN)
		t11.next_to(t5,LEFT,buff=0.5)
		t12.next_to(t5,RIGHT,buff=0.5)

		#Animación
		self.play(GrowFromCenter(t2))
		self.play(Write(t3))
		self.wait(2)
		self.play(Write(t4))
		self.play(Write(t5))
		self.wait(2)
		self.play(Transform(t2,t6))
		self.play(Write(t7))
		self.play(Transform(t3,t8))
		self.play(Transform(t4,t9))
		self.wait(2)
		self.play(Transform(t3,t11))
		self.play(Transform(t4,t12))
		self.wait(2)
		self.play(FadeOut(t3),
			FadeOut(t4),
			FadeOut(t7))
		self.play(Transform(t5,t10))
		self.wait()
		self.play(FadeOut(title),
			FadeOut(t2))

		#PARTE 3: Elementos sintácticos del cálculo lambda
		#elementos a imprimir
		t13 = TextMobject(r"$f(x) = x^{2}$")
		t14 = TextMobject(r"Una variable.")
		t15 = TextMobject(r"Una abstracci\'on funcional.")
		t16 = TextMobject(r"La aplicaci\'on de la funci\'on.")
		t17 = TextMobject(r"$x$")
		t18 = TextMobject(r"${\lambda}x$. $x^{2}$")
		t19 = TextMobject(r"($x$ $x$)")
		t20 = TextMobject(r"\small{¿C\'omo expreso $f(x) = x^{2}$ usando el c\'alculo $\lambda$?}")

		#Posisionamiento y color
		t13.to_edge(UP)
		t14.move_to(np.array([1,2,0]))
		t14.set_color("#5E9732")
		t15.next_to(t14,DOWN, buff=0.4)
		t15.set_color("#80C54C")
		t16.next_to(t15,DOWN, buff=0.4)
		t16.set_color("#9EE865")
		t17.move_to(np.array([-3,2,0]))
		t17.set_color("#5E9732")
		t18.next_to(t17,DOWN, buff=0.4)
		t18.set_color("#80C54C")
		t19.next_to(t18,DOWN, buff=0.4)
		t19.set_color("#9EE865")
		t20.to_edge(DOWN)

		#Animación
		self.play(Transform(t5,t13))
		self.play(Write(t14),
			Write(t17))
		self.wait()
		self.play(Write(t15),
			Write(t18))
		self.wait()
		self.play(Write(t16),
			Write(t19))
		self.wait()
		self.play(Write(t20))
		self.play(FadeOut(t14),
			FadeOut(t15),
			FadeOut(t16),
			FadeOut(t17),
			FadeOut(t18),
			FadeOut(t19))

		#PARTE 4: Definición de f(x) = x²
		#4.1 Elementos a imprimir
		t21 = TextMobject(r"\small{Variable}")
		t22 = TextMobject(r"\small{Operador $\lambda$}")
		t23 = TextMobject(r"\small{Salida}")
		t24 = TextMobject(r"$x$")
		t25 = TextMobject(r"$\lambda x$.")
		t26 = TextMobject(r"$\lambda x$. $x^{2}$")
		t27 = TextMobject(r"\large{$f(2) = 2^{2} = 4$}")

		#Posicionamiento y colores
		t21.next_to(t1,DOWN,buff = 0.4)
		t22.next_to(t1,DOWN,buff = 0.4)
		t23.next_to(t1,DOWN,buff = 0.4)

		#Animación
		self.play(Write(t21))
		self.play(Write(t24))
		self.wait()
		self.play(Transform(t21,t22))
		self.play(Transform(t24,t25))
		self.wait()
		self.play(Transform(t21,t23))
		self.play(Transform(t24,t26))
		self.wait()