def on_button_pressed_a():
    basic.clear_screen()
    basic.show_string("Vse nej Domi!!!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        # . # # #
                # . . . #
                # . . # #
                # . . . #
                # . # # #
    """)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
    basic.show_leds("""
        # . # # #
                # . . . #
                # . . # #
                # . . . #
                # . # # #
    """)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
    basic.show_leds("""
        # . # # #
                # . . . #
                # . . # #
                # . . . #
                # . # # #
    """)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
    basic.show_leds("""
        # . # # #
                # . . . #
                # . . # #
                # . . . #
                # . # # #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play_melody("C C D C F E - - ", 120)
music.play_melody("C C D C G F - - ", 120)
music.play_melody("C C C A F E D - ", 120)
music.play_melody("B B A F G F - - ", 120)