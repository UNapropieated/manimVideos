from big_ol_pile_of_manim_imports import *
import math

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$",
    }
    
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = WHITE)
        square = Square()
        text1 = TextMobject("Funci\\'on")
        arrow1 = Arrow(LEFT,RIGHT)
        arrow2 = Arrow(LEFT,RIGHT)
        arrow3 = Arrow(LEFT,RIGHT)
        arrow1.set_color("#0028DA")
        arrow2.set_color("#FA0000")
        arrow3.set_color("#AD27FF")
        
        arrow1.next_to(2*LEFT+UP,square.get_left(),buff = .1)
        arrow2.next_to(2*LEFT+DOWN,square.get_left(),buff = .1)
        arrow3.next_to(square.get_right()*2,RIGHT,buff = .1)
        square.scale(3)
        text1.scale(2)

        square.surround(text1)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait(2)
        self.delete_axes()
        self.wait(2)
        self.play(Transform(graph, square),Write(text1))
        self.wait(2)
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait(4)
        

        
    def setup_axes(self):
        GraphScene.setup_axes(self) 
        init_label_x = 1
        end_label_x = 7
        step_x = 1
        init_label_y = 5
        end_label_y = 50
        step_y = 5
        self.x_axis.label_direction = DOWN 
        self.y_axis.label_direction = LEFT
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )
        
    def delete_axes(self):
        self.play(
            Uncreate(self.x_axis),
            Uncreate(self.y_axis)
        )
