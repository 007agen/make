text_list = ["a", "b", "c"]
if input.button_is_pressed(Button.A):
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
elif input.button_is_pressed(Button.AB):
    basic.show_string("")
else:
    pass