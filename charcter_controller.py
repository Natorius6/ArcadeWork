import arcade

WIDTH = 800
HEIGHT = 800
TITLE = "character controller"

ball_x = 100
ball_y = 50

def on_draw(delta_time):
    global ball_x
    global ball_y

    arcade.start_render()
    arcade.draw_circle_filled(ball_x, ball_y, 25, arcade.color.GOLD)
    arcade.finish_render()

arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color(arcade.color.JET)

arcade.schedule(on_draw, 1/60)

arcade.run()
