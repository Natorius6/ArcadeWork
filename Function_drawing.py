import arcade

#size of the game window
WIDTH = 600
HEIGHT = 600

#function for drawing snowman
def draw_snowman(x, y):
    # draws body of the snowman
    arcade.draw_circle_filled(x, y - 80, 90, arcade.color.WHITE)  # bottom circle
    arcade.draw_circle_filled(x, y, 60, arcade.color.WHITE)  # middle circle
    arcade.draw_circle_filled(x, y + 70, 40, arcade.color.WHITE)  # top circle

    # draws eyes of the snowman
    arcade.draw_point(x + 15, y + 100, arcade.color.BLACK, 7)  # right eye
    arcade.draw_point(x - 15, y + 100, arcade.color.BLACK, 7)  # left eye

    # snowman mouth
    arcade.draw_line(x - 15, y + 90, x + 15, y + 90, (0, 0, 0), 5)

#opens the game window
arcade.open_window(WIDTH, HEIGHT, "hello")

#draws background
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

draw_snowman(150, 150)

arcade.finish_render()
arcade.run()
