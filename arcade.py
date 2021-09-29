import arcade

arcade.open_window(600, 600, "hello")
arcade.start_render()
arcade.draw_circle_filled(300, 300, 20, arcade.color.AFRICAN_VIOLET)
arcade.finish_render()
arcade.run()