import arcade

WIDTH = 800
HEIGHT = 800
TITLE = "bouncing balls"

vel_x = 3
vel_y = 3

ball_x = 100
ball_y = 50

moving_left = False
moving_down = False

def on_draw(delta_time):
    global ball_x
    global ball_y
    global moving_left
    global moving_down
    global vel_x
    global vel_y

    arcade.start_render()
    arcade.draw_circle_filled(ball_x, ball_y, 25, arcade.color.REDWOOD)
    arcade.finish_render()

    if ball_x > WIDTH - 25:
        moving_left = True
    if ball_x < 25:
        moving_left = False

    if ball_y > HEIGHT - 25:
        moving_down = True
    if ball_y < 25:
        moving_down = False

    if moving_down == True:
        ball_y -= vel_y
    else:
        ball_y += vel_y

    if moving_left == True:
        ball_x -= vel_x
    else:
        ball_x += vel_x


arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color(arcade.color.AFRICAN_VIOLET)

arcade.schedule(on_draw, 1/60)

arcade.run()