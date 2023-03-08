# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import turtle
import sys
import import_helper as ih

turtle.tracer(2)

if len(sys.argv) == 2:
    obs = ih.dynamic_import('maze.obstacles')
elif len(sys.argv) == 3:
    if sys.argv[1] == 'turtle' and sys.argv[2] == 'simple_maze':
        obs = ih.dynamic_import('maze.simple_maze')

# variables tracking position and direction
position_x = 0
position_y = 0
min_y, max_y = -250, 250
min_x, max_x = -250, 250
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
robot = turtle.Turtle()
screen = turtle.Screen()

def set_up_robot_environment():
    screen.bgcolor("#141D2A")
    screen.setup(width=720, height=1000)
    screen.title("Robot Environment")
    robot.pencolor("#4E9A06")
    robot.penup()
    robot.home()
    robot.setheading(90)
    robot.pensize(2)
    turtle.update()
    
def set_border():
    robot.speed(10)
    robot.setheading(90)
    robot.penup()
    robot.setx(-250)
    robot.sety(-250)
    robot.pendown()
    robot.pensize(5)
    for i in range(4):
        robot.forward(500)
        robot.right(90)
    robot.penup()
    robot.home()
    robot.setheading(90)
    turtle.update()


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps, robot_name):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y
 
    if directions[current_direction_index] == 'forward':
        new_y += steps
    elif directions[current_direction_index] == 'right':
        new_x += steps
    elif directions[current_direction_index] == 'back':
        new_y -= steps
    elif directions[current_direction_index] == 'left':
        new_x -= steps

    if obs.is_position_blocked(new_x, new_y) or (
        obs.is_path_blocked(new_x, new_y, position_x, position_y)):
            return None 

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        robot.forward(steps)
        turtle.update()
        return True
    else:
        return False


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    robot.right(90)
    turtle.update()
    
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    robot.left(90)
    turtle.update()

    return True, ' > '+robot_name+' turned left.'

if __name__ != '__main__':
    set_up_robot_environment()