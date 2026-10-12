from microbit import *

personas = 0

def mostrar_total():
    display.scroll(str(personas))

display.show(0)

while True:
    if button_a.was_pressed():
        personas += 1
        if personas > 99:
            personas = 99
        mostrar_total()

    if button_b.was_pressed():
        if personas > 0:
            personas -= 1
        mostrar_total()

    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("TOTAL")
        mostrar_total()
        sleep(500)

    sleep(100)
