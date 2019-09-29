from big_ol_pile_of_manim_imports import *
class Arrow1(Scene):
	def construct(self):
		lamb = TexMobject(r"\lambda")
		text2 = TextMobject("MT")
		text2.to_edge(DOWN,buff =2)
		lamb.next_to(text2,UP,buff = 4)
		lamb.scale(3)
		text2.scale(3)
		arrow2 = DoubleArrow(lamb.get_bottom(),text2.get_top(),buff=.1)
		group = VGroup(lamb,arrow2,text2)

		brace1 = Brace(group, RIGHT, buff = SMALL_BUFF)
		t1 = brace1.get_text("Java")
		t2 = TextMobject("Pascal")
		t2.next_to(brace1,RIGHT, buff = SMALL_BUFF)
		t3 = TextMobject("C++")
		t3.next_to(brace1,RIGHT, buff = SMALL_BUFF)

		self.play(Write(lamb))
		self.wait(2)
		self.play(Write(text2))
		self.play(GrowArrow(arrow2))
		self.wait(2)
		self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
		self.play(Transform(t1,t3))
		self.wait()
		self.play(Transform(t1,t2))
		self.wait(3)
		self.play(
			FadeOut(lamb),
			FadeOut(text2),
			FadeOut(t1),
			FadeOut(brace1),
			FadeOut(arrow2)
		)
		self.wait(3)
		