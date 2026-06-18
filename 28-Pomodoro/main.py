from pomodoro_timer import Timer
from ui import PomodoroUI

# pylint: disable=possibly-used-before-assignment

def _on_start():
    if timer:
        print("Start")
        timer.start()

def _on_reset():
    if timer and ui:
        print("Reset")
        ui.reset()
        timer.reset()

if __name__ == "__main__":
    ui = PomodoroUI(_on_start, _on_reset)
    timer = Timer(ui.update_time_remaining, ui.set_state, ui.add_check_mark)

    ui.start_loop()
