# Karl the Robot
# Function concept
#
#  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def main():
    code = '''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_right()
            if not front_is_clear():
                turn_left()
                turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_left()
            turn_left()
'''
    print("Instruction:")
    print("Go the link above, paste the code below, and run")
    print(code)

if __name__ == "__main__":
    main()

