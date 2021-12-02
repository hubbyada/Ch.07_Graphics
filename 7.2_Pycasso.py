'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade

arcade.open_window(500,400, "Adan Hubby")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
#grid
for x_offset in range(0,500,20):
    arcade.draw_line(0+x_offset,400,0+x_offset,0,arcade.color.RED, 1)
for y_offset in range(0,400,20):
    arcade.draw_line(500,0+y_offset,0,0+y_offset,arcade.color.RED, 1)
#x=20 per line
#y=20 per line

#character
#legs
arcade.draw_arc_filled(140,160,60,60,arcade.color.RED,90,270)
arcade.draw_arc_filled(140,220,60,60,arcade.color.RED,90,270)
arcade.draw_rectangle_filled(170,220,60,60,arcade.color.RED)
arcade.draw_rectangle_filled(170,160,60,60,arcade.color.RED)
#torso
arcade.draw_rectangle_filled(190,190,100,119,arcade.color.RED)
arcade.draw_ellipse_filled(240,190,60,120,arcade.color.DARK_RED)
arcade.draw_ellipse_filled(240,190,40,100,arcade.color.BLACK)
#bone
arcade.draw_ellipse_filled(240,190,20,30.5,arcade.color.WHITE)
arcade.draw_rectangle_filled(275,190,70,30,arcade.color.WHITE)
arcade.draw_circle_filled(320,205,20,arcade.color.WHITE)
arcade.draw_circle_filled(320,180,20,arcade.color.WHITE)

#text
arcade.draw_text("A body has been found!",20,340,arcade.color.WHITE,35)
arcade.finish_render()

arcade.run()




