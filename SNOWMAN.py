import arcade

#snowman drawing code

#size of the game window
WIDTH = 600
HEIGHT = 600

#opens the game window
arcade.open_window(WIDTH, HEIGHT, "hello")

#draws background
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

#draws body of the snowman
arcade.draw_circle_filled(WIDTH/2, HEIGHT/3, 90, arcade.color.WHITE) #bottom circle
arcade.draw_circle_filled(WIDTH/2, HEIGHT/2, 60, arcade.color.WHITE) #middle circle
arcade.draw_circle_filled(WIDTH/2, (HEIGHT/3)*1.8, 40, arcade.color.WHITE) #top circle

#draws eyes of the snowman
arcade.draw_point(WIDTH/2 + 15, (HEIGHT/3)*1.8 + 10, arcade.color.BLACK, 7) #right eye
arcade.draw_point(WIDTH/2 - 15, (HEIGHT/3)*1.8 + 10, arcade.color.BLACK, 7) #left eye

#snowman mouth
arcade.draw_line(WIDTH/2 - 15, (HEIGHT/3)*1.8, WIDTH/2 + 15, (HEIGHT/3)*1.8, (0, 0, 0), 5)

arcade.finish_render()
arcade.run()
