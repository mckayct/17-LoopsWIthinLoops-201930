"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Colton McKay.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # -------------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # First L.
    # -------------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click to run Test 2.')

    # -------------------------------------------------------------------------
    # Second L.
    # -------------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------

    original_x = circle.center.x
    original_y = circle.center.y
    radius = circle.radius
    fill_color = circle.fill_color
    orig_c = c
    orig_r = r


    x = original_x
    y = original_y
    c = 3
    for i in range(r):  # Loop through the rows
        for j in range(c):  # Loop through the columns
            new_circle = rg.Circle(rg.Point(x, y), radius)
            new_circle.fill_color = fill_color
            new_circle.attach_to(window)
            window.render(0.1)

            x = x + (2 * radius)  # Move x to the right, for next circle

        y = y + 2 * radius  # Move y down, for the next row of circles
        x = original_x  # Reset x to the left-edge, for the next row

    r = 3

    for i in range(c):  # Loop through the rows
        for j in range(r):  # Loop through the columns
            new_circle = rg.Circle(rg.Point(x, y), radius)
            new_circle.fill_color = fill_color
            new_circle.attach_to(window)
            window.render(0.1)

            x = x + (2 * radius)  # Move x to the right, for next circle

        y = y + 2 * radius  # Move y down, for the next row of circles
        x = original_x  # Reset x to the left-edge, for the next row

    #r = orig_r
    c = orig_c
    original_x = x + 6*radius
    y = y - 6*radius

    x = x + 6*radius
    for i in range(r):  # Loop through the rows
        for j in range(c):  # Loop through the columns
            new_circle = rg.Circle(rg.Point(x, y), radius)
            new_circle.fill_color = fill_color
            new_circle.attach_to(window)
            window.render(0.1)

            x = x + (2 * radius)  # Move x to the right, for next circle

        y = y + 2 * radius  # Move y down, for the next row of circles
        x = original_x  # Reset x to the left-edge, for the next row


def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # -------------------------------------------------------------------------


    original_lower_left = rectangle._lower_left_corner
    original_upper_right = rectangle._upper_right_corner
    orig_width = rectangle.get_width()
    orig_height = rectangle.get_height()

    lower_left = original_lower_left.clone()
    upper_right = original_upper_right.clone()
    for j in range(n):  # Loop through the rows
        for _ in range(j + 1):  # Loop through the columns
            new_rect = rg.Rectangle(lower_left,upper_right)
            new_rect.attach_to(window)
            window.render(0.1)

            lower_left.x = lower_left.x - orig_width # Move x to the right, for next circle
            upper_right.x = upper_right.x - orig_width

        lower_left.y = lower_left.y + orig_height # Move y down, for the next row of circles
        upper_right.y = upper_right.y + orig_height
        lower_left.x = original_lower_left.x
        upper_right.x = original_upper_right.x # Reset x to the left-edge, for the next row


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
