class Testing (Scene):
	def construct(self):
		title = TextMobject(r"\huge{SINT\'AXIS Y BLABLABLA}")
		self.play(Write(title))
		self.wait(3)
		self.remove()