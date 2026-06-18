import turtle as ttle

import pandas

MAP_IMAGE = "blank_states_img.gif"


def prepare_screen():
    screen = ttle.Screen()
    screen.title("USA States Game")
    screen.addshape(MAP_IMAGE)

    return screen


def prepare_turtle():
    the_turtle = ttle.Turtle()

    the_turtle.shape(MAP_IMAGE)
    # the_turtle.penup()

    return the_turtle


def get_states_data():
    """Read the states data from the CSV file and return a StatesData object."""
    try:
        return pandas.read_csv("50_states.csv")
    except FileNotFoundError as e:
        print(f"Error loading states data: {e}")
        return None


def get_state_input(screen, score):
    return screen.textinput(
        title=f"Guess a State ({score}/50)", prompt="Enter a state's name:"
    )


def display_state(state_name, states_data):
    """Display the state name on the map at the correct coordinates."""
    try:
        # title() converts the string to title case which matches the format in the CSV file
        # (e.g. "new york" -> "New York")
        state_info = states_data[states_data.state == state_name.title()].iloc[0]
        x, y = int(state_info.x), int(state_info.y)
        the_turtle = ttle.Turtle()
        the_turtle.hideturtle()
        the_turtle.penup()

        the_turtle.goto(x, y)
        the_turtle.write(state_info.state, align="center", font=("Arial", 10, "normal"))
    except IndexError:
        print(f"State '{state_info}' not found in data.")


def play_game(states_data, state_names, screen):
    score = 0

    while score < 50:
        guess = get_state_input(screen, score).strip().lower()

        if guess in state_names:
            display_state(guess, states_data)
            score += 1

def run_app():
    print("Welcome to the USA States Game!")

    screen = prepare_screen()
    states_data = get_states_data()
    state_names = states_data.state.str.lower().tolist()

    prepare_turtle()
    play_game(states_data, state_names, screen)

if __name__ == "__main__":
    run_app()