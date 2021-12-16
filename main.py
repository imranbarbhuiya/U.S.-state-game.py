import turtle

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_cord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cord)

turtle.mainloop()
