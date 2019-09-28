from big_ol_pile_of_manim_imports import *
class Arrow1(Scene):
	def construct(self):
		lamb = TexMobject(r"\lambda")
		text2 = TextMobject("M\\'aquina de Turing")
		arrow = DoubleArrow(Arrow(DOWN,UP))
		lamb.move_to(LEFT*2)
		arrow.next_to(lamb,RIGHT,buff = .1)
		text2.next_to(arrow,RIGHT,buff = .1)
		self.play(Write(lamb))
		self.wait()
		self.play(GrowArrow(arrow))
		self.play(Write(text2))
		self.wait()